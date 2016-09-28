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
    description = factory.LazyAttribute(lambda x: faker.text())
    phone_number = factory.LazyAttribute(lambda x: faker.phone_number())
    avatar = factory.LazyAttribute(lambda x: faker.url())
    website = factory.LazyAttribute(lambda x: faker.url())
    github = factory.LazyAttribute(lambda x: faker.url())
    bitbucket = factory.LazyAttribute(lambda x: faker.url())
    facebook = factory.LazyAttribute(lambda x: faker.url())
    instagram = factory.LazyAttribute(lambda x: faker.url())
    behance = factory.LazyAttribute(lambda x: faker.url())
    twitter = factory.LazyAttribute(lambda x: faker.url())
    linkedin = factory.LazyAttribute(lambda x: faker.url())
    stackoverflow = factory.LazyAttribute(lambda x: faker.url())


class CustomerFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = models.Customer

    name = factory.LazyAttribute(lambda x: faker.name())
    website = factory.LazyAttribute(lambda x: faker.url())
    email = factory.LazyAttribute(lambda x: faker.email())


class EntryFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = models.Entry

    developer = None
    customer = None
    title = factory.LazyAttribute(lambda x: faker.word().title())
    description = factory.LazyAttribute(lambda x: faker.text())
    website = factory.LazyAttribute(lambda x: faker.url())
    start_date = factory.LazyAttribute(lambda x: faker.date())
    end_date = factory.LazyAttribute(lambda x: faker.date())


class ImageFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = models.Image

    entry = None
    name = factory.LazyAttribute(lambda x: faker.word().title())
    image = factory.LazyAttribute(lambda x: faker.image_url())


class TestimonyFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = models.Testimony

    entry = None
    description = factory.LazyAttribute(lambda x: faker.text())
