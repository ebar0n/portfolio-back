from colorfield.fields import ColorField
from django.conf import settings
from django.db import models
from django.utils.translation import ugettext as _


class Tag(models.Model):
    """tag model

    Attributes:
        name = Is the name of the object.
        created_at = Is the date when the object is created.
            (Note: Automatically generated when the object is created.).
        updated_at = Is the date when the object is updated (Note: Automatically created).
            (Note: Automatically generated when the object is updated.).
    """
    name = models.CharField(verbose_name=_('name'), max_length=80)
    color = ColorField(default='#FF0000')
    created_at = models.DateTimeField(verbose_name=_('created at'), auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(verbose_name=_('updated at'), auto_now=True, editable=False)

    class Meta:
        verbose_name = _('tag')
        verbose_name_plural = _('tags')

    def __str__(self):
        return self.name


class Developer(models.Model):
    """Developer model

    Attributes:
        user = Is the user of the object.
        avatar = Is the avatar of the object.
        website = Is the website of the object.
        github = Is the github of the object.
        twitter = Is the twitter of the object.
        linkedin = Is the linkedin of the object.
        stackoverflow = Is the stackoverflow of the object.
        created_at = Is the date when the object is created
            (Note: Automatically generated when the object is created.).
        updated_at = Is the date when the object is updated (Note: Automatically created).
            (Note: Automatically generated when the object is updated.).
    """
    user = models.OneToOneField(settings.AUTH_USER_MODEL, verbose_name=_('user'))
    avatar = models.ImageField(verbose_name=_('avatar'), upload_to='images/developer/')
    website = models.URLField(verbose_name=_('website'), blank=True)
    github = models.URLField(verbose_name=_('github'), blank=True)
    twitter = models.URLField(verbose_name=_('twitter'), blank=True)
    linkedin = models.URLField(verbose_name=_('linkedIn'), blank=True)
    stackoverflow = models.URLField(verbose_name=_('stackOverFlow'), blank=True)
    created_at = models.DateTimeField(verbose_name=_('created at'), auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(verbose_name=_('updated at'), auto_now=True, editable=False)

    class Meta:
        verbose_name = _('developer')
        verbose_name_plural = _('developer')

    def __str__(self):
        return str(self.user)


class Entry(models.Model):
    """Entry model

    Attributes:
        title = Is the title of the object.
        description = Is the description of the object.
        tags = Is the tags of the object.
        website = Is the website of the object.
        created_at -- Is the date when the object is created
            (Note: Automatically generated when the object is created.).
        updated_at -- Is the date when the object is updated (Note: Automatically created).
            (Note: Automatically generated when the object is updated.).
    """
    developer = models.ForeignKey(Developer, verbose_name=_('developer'))
    title = models.CharField(verbose_name=_('title'), max_length=80)
    description = models.TextField(verbose_name=_('description'))
    date = models.DateField(verbose_name=_('date'))
    tags = models.ManyToManyField(Tag, verbose_name=_('tags'))
    created_at = models.DateTimeField(verbose_name=_('created at'), auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(verbose_name=_('updated at'), auto_now=True, editable=False)

    class Meta:
        verbose_name = _('entry')
        verbose_name_plural = _('entries')
        ordering = ['date', 'title']

    def __str__(self):
        return self.title


class Image(models.Model):
    """Image model

    Attributes:
        name = Is the name of the object.
        image = Is the image file of the object.
        entry = Is the entry file of the object.
        created_at = Is the date when the object is created
            (Note: Automatically generated when the object is created.).
        updated_at = Is the date when the object is updated (Note: Automatically created).
            (Note: Automatically generated when the object is updated.).
    """
    entry = models.ForeignKey(Entry, verbose_name=_('entry'))
    name = models.CharField(verbose_name=_('name'), max_length=80, blank=True)
    image = models.ImageField(verbose_name=_('avatar'), upload_to='images/developer/')
    created_at = models.DateTimeField(verbose_name=_('created at'), auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(verbose_name=_('updated at'), auto_now=True, editable=False)

    class Meta:
        verbose_name = _('image')
        verbose_name_plural = _('images')

    def __str__(self):
        return self.name
