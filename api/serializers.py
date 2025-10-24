from rest_framework import serializers
# best way to get user model name
from django.contrib.auth import get_user_model
from .models import Blog


user_model = get_user_model()

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = user_model
        fields = ["id", "username", "email", "first_name", "last_name", "password"]
        # this will make the password write only not read
        extra_kwargs = {
            'password': {'write_only':True}
        }

    def create(self, vaildated_data):
        new_user = user_model.objects.create_user(**vaildated_data)
        return new_user


class UpdateUserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = user_model
        fields = ["id", "username", "email", "first_name", "last_name", "bio", "profile_picture", "facebook", "instagram", "youtube", "twitter"]


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = user_model
        fields = ["id", "username","first_name","last_name"]


class BlogSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    class Meta:
        model = Blog
        fields = "__all__"


