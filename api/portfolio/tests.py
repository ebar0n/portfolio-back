import pytest
from django.conf import settings
from django.utils import translation
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APIClient

from portfolio import factories, models

translation.activate(factories.faker.random_element(settings.LANGUAGES)[0])


@pytest.fixture
def client():
    """
    Fixture responsible for build the api client
    Returns APIClient object:
    """
    return APIClient()


@pytest.fixture
def url_tags():
    """
    Fixture responsible for build the api url for main endpoint
    Returns Func:
    """
    return reverse('tags-list')


@pytest.fixture
def url_developers():
    """
    Fixture responsible for build the api url for main endpoint
    Returns Func:
    """
    return reverse('developers-list')


@pytest.fixture
def url_entries():
    """
    Fixture responsible for build the api url for main endpoint
    Returns Func:
    """
    return reverse('entries-list')


@pytest.fixture
def tags():
    """
    Fixture responsible for build a list of Tags
    Returns List of Tag Objects:
    """
    return factories.TagFactory.create_batch


@pytest.fixture
def customer():
    """
    Fixture responsible for build a list of customer
    Returns Object of customer
    """
    return factories.CustomerFactory.create()


@pytest.fixture
def developer():
    """
    Fixture responsible for build a list of developer
    Returns Object of developer
    """
    return factories.DeveloperFactory.create(user=factories.UserFactory.create())


@pytest.fixture
def entries(tags, developer, customer):
    """
    Fixture responsible for build a list of entries
    Returns List of entries Objects:
    """
    number_of_objects_tags = factories.faker.random_digit_not_null()
    tags(number_of_objects_tags)
    tag = models.Tag.objects.all().first()

    number_of_objects_entries = factories.faker.random_digit_not_null()

    for i in range(0, number_of_objects_entries):
        entry = factories.EntryFactory.create(developer=developer, customer=customer)
        entry.tags.add(tag)

        number_of_objects_images = factories.faker.random_digit_not_null()
        for j in range(0, number_of_objects_images):
            factories.ImageFactory.create(entry=entry)

        number_of_objects_testimonies = factories.faker.random_digit_not_null()
        for j in range(0, number_of_objects_testimonies):
            factories.TestimonyFactory.create(entry=entry)

    return number_of_objects_entries, tag


@pytest.mark.django_db
def test_tags_list(client, url_tags, tags):
    """
    Testing list of tags

    Args:
        client: ApiClient
        url_tags: Endpoint Url
        tags: function to create a list of objects
    """
    # Create N objects
    number_of_objects = factories.faker.random_digit_not_null()
    tags(number_of_objects)

    request = client.get(path=url_tags, format='json')

    assert request.status_code == status.HTTP_200_OK, 'Fails to list tags'
    assert len(request.data) == (number_of_objects), 'Incorrect number objects in data'
    assert models.Tag.objects.count() == (number_of_objects), 'Incorrect number objects of tag'


@pytest.mark.django_db
def test_tags_search(client, url_tags, tags):
    """
    Testing search of tags

    Args:
        client: ApiClient
        url_tags: Endpoint Url
        tags: function to create a list of objects
    """
    # Create N objects
    number_of_objects = factories.faker.random_digit_not_null() + 1
    tags(number_of_objects)

    tag = models.Tag.objects.all()[0]
    request = client.get(path='{}?search={}'.format(url_tags, tag.name), format='json')

    assert request.status_code == status.HTTP_200_OK, 'Fails to list tags'
    assert len(request.data) != number_of_objects, 'Incorrect number objects in data'


@pytest.mark.django_db
def test_developers_list(client, url_developers, developer):
    """
    Testing list of developers

    Args:
        client: ApiClient
        url_developers: Endpoint Url
        developer: function to create a object
    """
    number_of_objects = 1

    request = client.get(path=url_developers, format='json')

    assert request.status_code == status.HTTP_200_OK, 'Fails to list developers'
    assert request.data.get('count') == (number_of_objects), 'Incorrect number objects in data'
    assert models.Developer.objects.count() == (number_of_objects), 'Incorrect number objects of developer'


@pytest.mark.django_db
def test_developers_search(client, url_developers, developer):
    """
    Testing search of developers

    Args:
        client: ApiClient
        url_developers: Endpoint Url
        developer: function to create a object
    """
    # Create N objects
    number_of_objects = 1

    request = client.get(path='{}?search={}'.format(url_developers, developer.user.username), format='json')

    assert request.status_code == status.HTTP_200_OK, 'Fails to list developers'
    assert len(request.data) != number_of_objects, 'Incorrect number objects in data'


@pytest.mark.django_db
def test_developers_retrive(client, url_developers, developer):
    """
    Testing retrive of developers

    Args:
        client: ApiClient
        url_developers: Endpoint Url
        developer: function to create a object
    """
    request = client.get(path='{}{}/'.format(url_developers, developer.id), format='json')

    assert request.status_code == status.HTTP_200_OK, 'Fails to list developers'
    assert request.data.get('id') == developer.id, 'Incorrect id objects in data'


@pytest.mark.django_db
def test_entries_list(client, url_entries, entries, developer):
    """
    Testing list of entry

    Args:
        client: ApiClient
        url_entries: Endpoint Url
        entries: function to create a list of objects
        developer: function to create a object
    """
    number_of_objects = models.Entry.objects.count()
    tag = models.Tag.objects.all().first()

    request = client.get(
        path='{}?developer={}&?tags={}'.format(url_entries, developer.id, tag.id),
        format='json'
    )

    assert request.status_code == status.HTTP_200_OK, 'Fails to list entries'
    assert request.data.get('count') == (number_of_objects), 'Incorrect number objects in data'
    assert models.Entry.objects.count() == (number_of_objects), 'Incorrect number objects of entry'


@pytest.mark.django_db
def test_entries_search(client, url_entries, entries):
    """
    Testing search of entry

    Args:
        client: ApiClient
        url_entries: Endpoint Url
        entries: function to create a list of objects
    """

    entry = models.Entry.objects.all().first()
    request = client.get(
        path='{}?search={}'.format(url_entries, entry.title),
        format='json'
    )

    assert request.status_code == status.HTTP_200_OK, 'Fails to list entries'
    assert request.data.get('count') >= 1, 'Incorrect number objects in data'


@pytest.mark.django_db
def test_entries_retrive(client, url_entries, entries):
    """
    Testing retrive of entry

    Args:
        client: ApiClient
        url_entries: Endpoint Url
        entries: function to create a list of objects
    """

    entry = models.Entry.objects.all().first()
    request = client.get(
        path='{}{}/'.format(url_entries, entry.id),
        format='json'
    )

    assert request.status_code == status.HTTP_200_OK, 'Fails to list entries'
    assert request.data.get('id') == entry.id, 'Incorrect id objects in data'
