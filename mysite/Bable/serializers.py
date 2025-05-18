from django.contrib import admin

# Register your models here.
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer



from .models import *


class AuthorSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = Author
		fields =  ( 'username', )

class PostSerializer(WritableNestedModelSerializer):
	class Meta:
		model = Post
		fields = ('title', 'body',)

	def create(self,validated_data):
		return Post.objects.create(**validated_data)


	def update(self, instance, validated_data):
		"""
		Update and return an existing `Snippet` instance, given the validated data.
		"""
		instance.title = validated_data.get('title', instance.title)
		instance.body = validated_data.get('body', instance.body)
		instance.public = validated_data.get('public', instance.public)
		

		instance.save()
		return instance


