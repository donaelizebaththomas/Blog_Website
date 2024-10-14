from rest_framework import serializers
from django.contrib.auth.models import User
from .models import BlogPost
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404
from rest_framework.validators import UniqueValidator


# User Serializer for registration and detail
class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, min_length=6)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email','password']


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'date_joined']


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email','password']


# BlogPost Serializer
class BlogPostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'content', 'author', 'created_at', 'updated_at']


class BlogPostCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'content']

    def create(self, validated_data):
        return BlogPost.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.save()
        return instance


# User Login Serializer
class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)



























# users/serializers.py
# from rest_framework import serializers
# from django.contrib.auth.models import User
# from app.models import BlogPost
# from django.contrib.auth import authenticate
# from rest_framework.exceptions import AuthenticationFailed
#
#
# class UserLoginSerializer(serializers.Serializer):
#     email = serializers.CharField()
#     password = serializers.CharField(write_only=True)
#
#     def validate(self, data):
#         email = data.get('email')
#         password = data.get('password')
#
#         if email and password:
#             user = authenticate(email=email, password=password)
#             if user is None:
#                 raise AuthenticationFailed('Invalid credentials')
#         else:
#             raise AuthenticationFailed('Username and password are required')
#
#         return data
#
#
# class BlogPostSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = BlogPost
#         fields = ['id', 'title', 'content', 'created_at', 'updated_at', 'author']
#         read_only_fields = ['id', 'created_at', 'updated_at', 'author']
#
# class UserSerializer(serializers.ModelSerializer):
#     """ to display all the users details"""
#     class Meta:
#         model=User
#         fields=['id','username','email']
#
#
# class BlogPostCreateUpdateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = BlogPost
#         fields = ['title', 'content']
#
# class UserRegistrationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password']
#         extra_kwargs = {
#             'password': {'write_only': True},
#         }
#
#     def create(self, validated_data):
#         user = User.objects.create_user(
#             username=validated_data['username'],
#             email=validated_data['email'],
#             password=validated_data['password']
#         )
#         user.save()
#         return user
#
#     # def create(self, validated_data):
#     #     user=User.objects.create_user(username=validated_data['username'],password=validated_data['password'])
#     #     user.save()
#     #     return user
#
#
# class UserDetailSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password']
#
# class UserUpdateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password']
#         extra_kwargs = {
#             'password': {'write_only': True},
#         }
#
#     def update(self, instance, validated_data):
#         password = validated_data.get('password')
#         if password:
#             instance.set_password(password)
#         instance.username = validated_data.get('username', instance.username)
#         instance.email = validated_data.get('email', instance.email)
#         instance.save()
#         return instance
#
# # class UserBlogSerializer(serializers.ModelSerializer):
# #     class meta:
# #         model=blog
# #         fields=all
