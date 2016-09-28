import os

from fabric.api import cd, env
from fabric.colors import green
from fabric.operations import prompt

env.user = 'root'
env.key_filename = '~/.ssh/id_rsa.pub'

LOCAL = prompt(green('Execute local: y/n'), default='y') in ['y', 'Y']

if LOCAL:
    from fabric.api import local as run
    YML = ''
    HOME_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
else:
    from fabric.api import run
    YML = '-f docker-compose-production.yml'
    HOME_DIRECTORY = '/root/portfolio-back'

HOME_DIRECTORY = prompt(
    green('Directory: '),
    default=HOME_DIRECTORY
)


def log(containder='api', lines='100'):
    """
    Get the last N lines from container log.

    Args:
        containder: Name container
        lines: Number lines

    Example:
        $ fab log:containder='api',prefix=''
    """
    with cd(HOME_DIRECTORY):
        run(
            'docker-compose {} logs {} | tail -n {}'
            ''.format(YML, containder, lines)
        )


def pull(branch='master'):
    """
    Pull repostory by branch

    Args:
        branch: Name branch

    Example:
        $ fab pull:branch=master
    """
    with cd(HOME_DIRECTORY):
        run('git fetch -a')
        run('git reset origin/{}'.format(branch))
        run('git checkout .')
        run('git checkout {}'.format(branch))


def build(branch='master', containder=''):
    """
    Build for containers by branch

    Args:
        branch: Name branch
        containder: Name container

    Example:
        $ fab build
    """
    if not LOCAL:
        pull(branch=branch)
    with cd(HOME_DIRECTORY):
        run('docker-compose {} build {}'.format(YML, containder))


def deploy(branch='master', containder=''):
    """
    Deploy for containers by branch

    Args:
        branch: Name branch
        containder: Name container

    Example:
        $ fab deploy

        Perform deployment
        $ fab deploy:branch='master',containder=''
    """
    with cd(HOME_DIRECTORY):
        if containder == '':
            run('docker-compose {} down'.format(YML))
        else:
            run('docker-compose {} stop {}'.format(YML, containder))
            run('docker-compose {} rm {}'.format(YML, containder))
    build(branch=branch, containder=containder)
    with cd(HOME_DIRECTORY):

        run('docker-compose {} up -d postgres'.format(YML))
        run(
            'docker-compose {} run --rm api python manage.py '
            'migrate --noinput'.format(YML)
        )
        run(
            'docker-compose {} run --rm api python manage.py '
            'collectstatic --noinput'.format(YML)
        )
        run(
            'docker-compose {} run --rm api python manage.py '
            'compilemessages'.format(YML)
        )
        run('docker-compose {} up -d {}'.format(YML, containder))


def test(branch='master'):
    """
    Test for containers by branch

    Args:
        branch: Name branch
        containder: Name container

    Example:
        $ fab test
    """
    from fabric.api import local as run
    with cd(HOME_DIRECTORY):
        run('docker-compose run --rm --no-deps api isort -c -rc -df')
        run('docker-compose run --rm --no-deps api flake8')
        run('docker-compose run --rm api python manage.py check')
        run('docker-compose run --rm api py.test')
