import factory
from django.contrib.auth.models import User
from faker import Factory as FakerFactory

from portfolio import models

faker = FakerFactory.create()


class TagFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = models.Tag

    name = factory.LazyAttribute(lambda x: faker.name())
    color = factory.LazyAttribute(lambda x: faker.hex_color())


class UserFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = User

    username = factory.LazyAttribute(lambda x: faker.user_name())
    is_active = True


class DeveloperFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = models.Developer

    user = None
    avatar = factory.LazyAttribute(lambda x: faker.url())
    website = factory.LazyAttribute(lambda x: faker.url())
    github = factory.LazyAttribute(lambda x: faker.url())
    twitter = factory.LazyAttribute(lambda x: faker.url())
    linkedin = factory.LazyAttribute(lambda x: faker.url())
    stackoverflow = factory.LazyAttribute(lambda x: faker.url())


class EntryFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = models.Entry

    developer = None
    title = factory.LazyAttribute(lambda x: faker.word().title())
    description = factory.LazyAttribute(lambda x: faker.text())
    date = factory.LazyAttribute(lambda x: faker.date())


class ImageFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = models.Image

    entry = None
    name = factory.LazyAttribute(lambda x: faker.word().title())
    image = factory.LazyAttribute(lambda x: faker.image_url())
