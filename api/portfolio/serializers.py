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

    class Meta:
        fields = (
            'id', 'user', 'avatar', 'website', 'github', 'twitter',
            'linkedin', 'stackoverflow', 'created_at', 'updated_at'
        )
        model = models.Developer

    def getter_user(self, obj):
        serializer = UserSerializer(obj.user)
        return serializer.data


class ImageSerializer(serializers.ModelSerializer):
    """
        Image Serializer
    """

    class Meta:
        fields = ('name', 'image')
        model = models.Image


class EntrySerializer(serializers.ModelSerializer):
    """
        Entry Serializer
    """

    image_set_filter = serializers.SerializerMethodField('image_set')

    class Meta:
        fields = (
            'id', 'developer', 'title', 'description', 'date', 'tags',
            'image_set_filter', 'created_at', 'updated_at'
        )
        model = models.Entry

    def image_set(self, obj):
        serializer = ImageSerializer(
            obj.image_set.all(),
            many=True
        )
        return serializer.data
