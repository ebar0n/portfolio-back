from django.contrib.auth.models import User
from rest_framework import serializers

from portfolio import models


class TagSerializer(serializers.ModelSerializer):
    """
        Tag Serializer
    """

    class Meta:
        fields = ('id', 'name', 'color')
        model = models.Tag


class UserSerializer(serializers.ModelSerializer):
    """
        User Serializer
    """

    class Meta:
        fields = (
            'id', 'username', 'first_name', 'last_name', 'email'
        )
        model = User


class DeveloperSerializer(serializers.ModelSerializer):
    """
        Developer Serializer
    """

    user = serializers.SerializerMethodField('getter_user')
    skills = serializers.SerializerMethodField('getter_skills')

    class Meta:
        fields = (
            'id', 'user', 'description', 'phone_number', 'avatar', 'skills', 'website',
            'github', 'bitbucket', 'twitter', 'behance', 'facebook', 'instagram', 'linkedin',
            'stackoverflow', 'created_at', 'updated_at'
        )
        model = models.Developer

    def getter_user(self, obj):
        serializer = UserSerializer(obj.user)
        return serializer.data

    def getter_skills(self, obj):
        serializer = TagSerializer(obj.skills, many=True)
        return serializer.data


class ImageSerializer(serializers.ModelSerializer):
    """
        Image Serializer
    """

    class Meta:
        fields = ('name', 'image')
        model = models.Image


class TestimonySerializer(serializers.ModelSerializer):
    """
        Testimony Serializer
    """

    class Meta:
        fields = ('description', 'created_at', 'updated_at')
        model = models.Testimony


class CustomerSerializer(serializers.ModelSerializer):
    """
        Customer Serializer
    """

    class Meta:
        fields = ('name', 'website', 'email')
        model = models.Customer


class EntrySerializer(serializers.ModelSerializer):
    """
        Entry Serializer
    """

    tags = serializers.SerializerMethodField('getter_tags')
    image_get_filter = serializers.SerializerMethodField('image_set')

    class Meta:
        fields = (
            'id', 'developer', 'title', 'start_date', 'end_date', 'tags', 'image_get_filter'
        )
        model = models.Entry

    def getter_tags(self, obj):
        serializer = TagSerializer(obj.tags, many=True)
        return serializer.data

    def image_set(self, obj):
        serializer = ImageSerializer(
            obj.image_set.all().first(),
        )
        return serializer.data


class EntryRetrieveSerializer(serializers.ModelSerializer):
    """
        Entry Retrieve Serializer
    """

    tags = serializers.SerializerMethodField('getter_tags')
    image_get_filter = serializers.SerializerMethodField('image_set')
    testimony_get_filter = serializers.SerializerMethodField('testimony_set')
    customer = serializers.SerializerMethodField('getter_customer')

    class Meta:
        fields = (
            'id', 'developer', 'title', 'description', 'customer', 'start_date', 'end_date',
            'tags', 'website', 'testimony_get_filter', 'image_get_filter', 'created_at', 'updated_at'
        )
        model = models.Entry

    def getter_tags(self, obj):
        serializer = TagSerializer(obj.tags, many=True)
        return serializer.data

    def image_set(self, obj):
        serializer = ImageSerializer(
            obj.image_set.all(),
            many=True
        )
        return serializer.data

    def testimony_set(self, obj):
        serializer = TestimonySerializer(
            obj.testimony_set.all(),
            many=True
        )
        return serializer.data

    def getter_customer(self, obj):
        serializer = CustomerSerializer(
            obj.customer
        )
        return serializer.data
