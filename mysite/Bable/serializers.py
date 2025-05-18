from django.contrib import admin

# Register your models here.
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer



from .models import *

class AngelNumberSerializer(serializers.ModelSerializer):
	class Meta:
		model = AngelNumber
		fields = ('digits', 'numbers', 'description',)

class AuthorSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = Author
		fields =  ( 'username', )

class PostSerializer(WritableNestedModelSerializer):
	class Meta:
		model = Post
		fields = ('title', 'body', 'url2',)

	def create(self,validated_data):
		return Post.objects.create(**validated_data)


	def update(self, instance, validated_data):
		"""
		Update and return an existing `Snippet` instance, given the validated data.
		"""
		instance.title = validated_data.get('title', instance.title)
		instance.url2 = validated_data.get('url2', instance.url2)
		instance.img = validated_data.get('img', instance.img)
		instance.body = validated_data.get('body', instance.body)
		instance.words = validated_data.get('words', instance.words)
		instance.dictionaries = validated_data.get('dictionaries', instance.dictionaries)
		instance.spaces = validated_data.get('spaces', [(space, SpaceSource.objects.filter(the_space_itself=Word.objects.get(the_word_itself=space, dictionary__purchased_dictionaries=Anon.objects.get(username=request.user), spaces__the_sace_itself__the_word_itself=word).to_source(), allowed_view_authors=loggedinauthor).first()) for space in instance.spaces]) 
		instance.public = validated_data.get('public', instance.public)
		instance.cc = validated_data.get('cc', instance.cc)


		instance.save()
		return instance


class ExampleSerializer(WritableNestedModelSerializer):
	class Meta:
		model = Example
		fields = ('the_example_itself',)


class WordSerializer(WritableNestedModelSerializer):
	class Meta:
		model = Word
		fields = ('the_word_itself',)


class SponsorSerializer(WritableNestedModelSerializer):
	class Meta:
		model = Sponsor
		fields = ('the_sponsorship_phrase', 'img', 'url2', 'payperview', 'price_limit', 'allowable_expenditure', 'author')
