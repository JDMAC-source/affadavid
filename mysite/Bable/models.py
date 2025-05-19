# Copyright Aden Handasyde 2019

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User, UserManager, AbstractBaseUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
import os
from django.urls import reverse
from django import forms
from mptt.models import MPTTModel, TreeForeignKey
from webpreview import web_preview

from django.conf import settings

import PIL.Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys

from datetime import timedelta
from random import choice
# from resizeimage import resizeimage

#from videofield.models import VideoField
# Create your models here.
def get_image_path(instance, filename):
    return settings.MEDIA_ROOT + str(instance.id) + '{}'.format(filename)
#Repeat of Words with OVERTOPVISION

# '/media/' for heroku
# settings.MEDIA_ROOT for local
class File(models.Model):
	file = models.FileField(upload_to='files', null=True)
	url2 = models.URLField(max_length=2000)
	filename = models.CharField(max_length=200, default='')
	public = models.BooleanField(default=False)
	creation_date = models.DateTimeField(default=timezone.now)

# Many to many fields create a A = .m2m(B), into a A_B hidden table. ie. it's backwards compatable with .m2m(B, through='AB')

class Notification(models.Model):
	text = models.CharField(max_length=200)
	link = models.URLField(max_length=2000, default='')
	username = models.CharField(max_length=150, default='', unique=True)
	sent = models.BooleanField(default=False)
	new = models.BooleanField(default=True)
	creation_date = models.DateTimeField(default=timezone.now)
	read_date = models.DateTimeField(default=timezone.now)
	click_date = models.DateTimeField(default=timezone.now)


# trying to save every change within the new saves, but not need a mirage of every other class.
class ChangeDate(models.Model):
	def __init__(self, charfield=None, textfield=None, **kwargs):
		if charfield:
			self.charfield = models.CharField(max_length=200, default='', unique=True)
		if textfield:
			self.textfield = models.TextField(max_length=1000, default='')
	each = models.DateTimeField(default=timezone.now)

class Requested_Agent(models.Model):
	user_agent = models.CharField(max_length=200, default='')
	datetime = models.DateTimeField(default=timezone.now)
	page = models.CharField(max_length=200, default='')
	if_username = models.CharField(max_length=200, default='')
	if_loggedin = models.BooleanField(default=False)



class Author(models.Model):
	username = models.CharField(max_length=150, default='', unique=True)
	
	def to_anon(self):
		if Anon.objects.filter(username__username=self.username[0:149]).count():
			if not User.objects.filter(username=self.username[0:149]).count():
				user = User.objects.create(username=self.username[0:149], password="Password-2")
			else:
				user = User.objects.get(username=self.username[0:149])
			anon = Anon.objects.get(username=user)
			author, created = Author.objects.get_or_create(username=self.username[0:149])
			anons_posts = Post.objects.filter(author=author)
			for post in anons_posts:
				if post not in anon.posts.all():
					anon.posts.add(post)
			anon.save()
			return anon
		else:
			if not User.objects.filter(username=self.username[0:149]).count():
				user = User.objects.create(username=self.username[0:149], password="Password-2")
			else:
				user = User.objects.get(username=self.username[0:149])
			
			if Anon.objects.filter(username=user).count():
				anon = Anon.objects.get(username=user)
				anons_posts = Post.objects.filter(author=Author.objects.get(username=self.username[0:149]))
				for post in anons_posts:
					if post not in anon.posts.all():
						anon.posts.add(post)
				anon.save()
				return anon
			else:
				anon, created = Anon.objects.create(username=user)
				anons_posts = Post.objects.all().filter(author=Author.objects.get(username=self.username[0:149]))
				for post in anons_posts:
					if post not in anon.posts.all():
						anon.posts.add(post)
				anon.save()
				return anon


class Comment_Edit(models.Model):
	author = models.ForeignKey(Author, on_delete=models.CASCADE, default=None)
	body = models.TextField(max_length=1440, default='')
	comment_id = models.IntegerField(default=0)
	creation_date = models.DateTimeField(default=timezone.now)

class Comment(MPTTModel):
	author = models.ForeignKey(Author, on_delete=models.CASCADE, default=None)
	body = models.TextField(max_length=1440, default='')
	edit_history = models.ManyToManyField(Comment_Edit, default=None, related_name="edit_history")
	suggested_edits = models.ManyToManyField(Comment_Edit, default=None, related_name="suggested_edits")
	viewcount = models.IntegerField(default=0)
	latest_change_date = models.DateTimeField(default=timezone.now)
	creation_date = models.DateTimeField(default=timezone.now)
	has_commented = models.ManyToManyField(Author, default=None, related_name='comments_has_commented')
	sum_has_commented = models.IntegerField(default=0)
	has_viewed = models.ManyToManyField(Author, default=author, related_name='comments_has_viewed')
	sum_has_viewed = models.IntegerField(default=0)
	has_accuracy = models.ManyToManyField(Author, default=None, related_name='comment_has_accuracy')
	sum_has_accuracy = models.IntegerField(default=0)
	has_credibilities = models.ManyToManyField(Author, default=None, related_name='comment_has_credible')
	sum_has_credibilities = models.IntegerField(default=0)

	likes = models.ManyToManyField(Author, default=None, related_name='comment_likes')
	dislikes = models.ManyToManyField(Author, default=None, related_name='comment_dislikes')
	parent = TreeForeignKey('self', on_delete=models.CASCADE, default=None, null=True, blank=True, related_name='children', db_index=True)
	children_count = models.IntegerField(default=0)

	

	def __str__(self):
		return self.body

	def __unicode__(self):
   		return unicode(self.body) or u''

	def children(self):
		return Comments.objects.filter(parent=self)

	@property
	def is_parent(self):
		if self.parent is not None:
			return False
		return True

	class MPTTMeta:
		order_insertion_by = ['sum_has_voted', 'children_count']

	

COMMENT_SORT_CHOICES_CHAR = (
	("sum_has_accurated", "Less Accurate"),
	("-sum_has_accurated", "More Accurate"),
	("sum_has_credibilities", "Less Credible"),
	("-sum_has_credibilities", "More Credible"),
	("-viewcount", "Viewcount"),
	("viewcount", "Unseen"),
	("-latest_change_date", "Latest Edit"),
	("latest_change_date", "Unchanged Since"),
	("-creation_date", "Latest Made"),
	("creation_date", "Earliest Made"),
	("-sum_has_commented", "Discussed"),
	("sum_has_commented", "Unspoken"),
)

class Views(models.Model):
	author = models.ForeignKey(Author, on_delete=models.PROTECT, default=None, null=True)
	creation_date = models.DateTimeField(default=timezone.now)
	sentence_id = models.IntegerField(default=0)

class Sentence_Edit(models.Model):
	sentence = models.TextField(max_length=14400)
	creation_date = models.DateTimeField(default=timezone.now)
	sentence_prior = models.TextField(max_length=14400)
	
	accuracy = models.ManyToManyField(Author, default=None, related_name="sentence_edit_accuracy")
	credibility = models.ManyToManyField(Author, default=None, related_name="sentence_edit_credibility")
	
	post_views_before_sentence_edit = models.ManyToManyField(Views, default=None, related_name="post_views_before_sentence_editing")
	post_views_after_sentence_edit = models.ManyToManyField(Views, default=None, related_name="post_views_after_sentence_editing")
	
	one_day_has_passed = models.BooleanField(default=False)
	
	one_day_view_bump_from_sentence_edit = models.IntegerField(default=0)
	odvbfse_with_assumed_information_decay = models.IntegerField(default=0)
	
	two_days_have_passed = models.BooleanField(default=False)
	
	odvbfse_waid_virality_day_two = models.IntegerField(default=0)
	odvbfse_woaid_virality_day_two = models.IntegerField(default=0)

	post_id = models.IntegerField(default=0)
	edit_id = models.IntegerField(default=0)
	
	author = models.ForeignKey(Author, on_delete=models.PROTECT, default=None, null=True)

class Sentence(models.Model):
	sentence = models.TextField(max_length=14400, default='')


	collaborated_sentence_edits = models.ManyToManyField(Sentence_Edit, default=None, related_name="collaborated_sentence_edits")
	contributed_sentence_edits = models.ManyToManyField(Sentence_Edit, default=None, related_name="contributed_sentence_edits")
	suggested_sentence_edits = models.ManyToManyField(Sentence_Edit, default=None, related_name="suggested_sentence_edits")
	
	accuracy = models.ManyToManyField(Author, default=None, related_name="sentence_accuracy")
	credibility = models.ManyToManyField(Author, default=None, related_name="sentence_credibility")
	post_views_before_sentence_edit = models.ManyToManyField(Views, default=None, related_name="post_views_before_sentence_edit")
	post_views_after_sentence_edit = models.ManyToManyField(Views, default=None, related_name="post_views_after_sentence_edit")
	one_day_has_passed = models.BooleanField(default=False)
	one_day_view_bump_from_sentence_edit = models.IntegerField(default=0)
	odvbfse_with_assumed_information_decay = models.IntegerField(default=0)
	two_days_have_passed = models.BooleanField(default=False)
	odvbfse_waid_virality_day_two = models.IntegerField(default=0)
	odvbfse_woaid_virality_day_two = models.IntegerField(default=0)

	post_id = models.IntegerField(default=0)
	edit_id = models.IntegerField(default=0)
	author = models.ForeignKey(Author, on_delete=models.PROTECT, default=None)
	creation_date = models.DateTimeField(default=timezone.now)

	
class Edit(models.Model):
	new_body = models.TextField(max_length=144000, default='')
	old_body = models.TextField(max_length=144000, default='')
	sentences = models.ManyToManyField(Sentence, default=None)
	post_id = models.IntegerField(default=0)
	author = models.ForeignKey(Author, on_delete=models.PROTECT, default=None)
	creation_date = models.DateTimeField(default=timezone.now)

	
	

class Post(models.Model):
	author = models.ForeignKey(Author, on_delete=models.CASCADE, default=None, null=True)
	sentences = models.ManyToManyField(Sentence, default=None)
	collaborated_sentence_edits = models.ManyToManyField(Sentence_Edit, default=None, related_name="post_collaborated_sentence_edits")
	contributed_sentence_edits = models.ManyToManyField(Sentence_Edit, default=None, related_name="post_contributed_sentence_edits")
	suggested_sentence_edits = models.ManyToManyField(Sentence_Edit, default=None, related_name="post_suggested_sentence_edits")
	edits = models.ManyToManyField(Edit, default=None)
	title = models.CharField(max_length=200, default='')
	img = models.OneToOneField(File, default=None, on_delete=models.PROTECT, related_name="display_image")
	imgs = models.ManyToManyField(File, default=None, related_name="other_images")
	has_commented = models.ManyToManyField(Author, default=None, related_name='post_has_commented')
	sum_has_commented = models.IntegerField(default=0)
	has_viewed = models.ManyToManyField(Author, default=None, related_name='post_has_viewed')
	sum_has_viewed = models.IntegerField(default=0)
	has_credibilities = models.ManyToManyField(Author, default=None, related_name='post_has_credibilities')
	sum_has_credibilities = models.IntegerField(default=0)
	has_accuracy = models.ManyToManyField(Author, default=None, related_name='post_has_accuracy')
	sum_has_accuracy = models.IntegerField(default=0)
	body = models.TextField(max_length=1440, default='')
	comments = models.ManyToManyField(Comment, default=None)
	sum_comments = models.IntegerField(default=0)
	
	viewcount = models.IntegerField(default=0)
	change_count = models.IntegerField(default=0)
	republished_count = models.IntegerField(default=0)
	latest_change_date = models.DateTimeField(default=timezone.now)
	pub_date = models.DateTimeField(default=timezone.now)
	published = models.BooleanField(default=1)
	allowed_to_view_authors = models.ManyToManyField(Author, default=None, related_name='allowed_to_view_authors')
	allowed_to_edit_authors = models.ManyToManyField(Author, default=None, related_name='allowed_to_edit_authors')
	blocked_from_commenting = models.ManyToManyField(Author, default=None, related_name='blocked_from_commenting')
	
	def __str__(self):
		return self.title

	def __eq__(self, other):
		return self.id == other.id

	def __hash__(self):
		return hash(('id', self.id))
	
	def __unicode__(self):
   		return unicode(self.title) or u''

	def pass_sentence_to_collaborative_edit(self, new_sentence, old_sentence, appearance_order=0):
		unedited_sentence = self.sentences.filter(sentence=old_sentence).order_by('creation_date')[appearance_order]
		sentence_edit = Sentence_Edit.objects.create(sentence=new_sentence, sentence_prior=old_sentence, accuracy=unedited_sentence.accuracy.all(), credibility=unedited_sentence.credibility.all(), author=unedited_sentence.author, post_views_before_sentence_edit=unedited_sentence.post_views_before_sentence_edit.all(), post_views_after_sentence_edit=unedited_sentence.post_views_after_sentence_edit.all(), one_day_has_passed=unedited_sentence.one_day_has_passed, one_day_view_bump_from_sentence_edit=unedited_sentence.one_day_view_bump_from_sentence_edit, odvbfse_with_assumed_information_decay=unedited_sentence.odvbfse_with_assumed_information_decay, odvbfse_waid_virality_day_two=unedited_sentence.odvbfse_waid_virality_day_two, odvbfse_woaid_virality_day_two=unedited_sentence.odvbfse_woaid_virality_day_two, two_days_have_passed=unedited_sentence.two_days_have_passed)
		unedited_sentence.collaborated_sentence_edits.add(sentence_edit)
		self.post_collaborated_sentence_edits.add(sentence_edit)
		self.sentences.remove(unedited_sentence)
		new_edited_sentence = Sentence.objects.create(sentence=new_sentence, accuracy=unedited_sentence.accuracy.all(), credibility=unedited_sentence.credibility.all(), author=unedited_sentence.author, post_views_before_sentence_edit=unedited_sentence.post_views_before_sentence_edit.all())
		for view in unedited_sentence.post_views_after_sentence_edit.all():
			new_edited_sentence.post_views_before_sentence_edit.add(view)
		new_edited_sentence.save()
		self.sentences.add(new_edited_sentence)

		splitting = self.body.split(old_sentence)
		for bit in splitting[0:appearance_order]:
			if not appearance_order:
				new_body += bit + old_sentence
		new_body += new_sentence
		for bit in splitting[appearance_order:]:
			new_body += bit

		self.edits.add(Edit.objects.create(new_body=new_body, old_body=self.body, sentences=self.sentences.all(), author=self.author, post_id=self.id))
		self.body = new_body

		self.save()

		anons_with_unedited_sentence_in_saved = Anon.objects.filter(anon_saved_sentences=unedited_sentence)
		for anon in anons_with_unedited_sentence_in_saved.all():
			anon.anon_saved_sentence_edits.add(sentence_edit)
			anon.save()

		anons_with_unedited_sentence_in_collaborated = Anon.objects.filter(anon_collaborated_sentences=unedited_sentence)
		for anon in anons_with_unedited_sentence_in_collaborated.all():
			anon.anon_collaborated_sentence_edits.add(sentence_edit)
			anon.save()

		anons_with_unedited_sentence_in_contributed = Anon.objects.filter(anon_contributed_sentences=unedited_sentence)
		for anon in anons_with_unedited_sentence_in_contributed.all():
			anon.anon_contributed_sentence_edits.add(sentence_edit)
			anon.save()

		anons_with_unedited_sentence_in_suggested = Anon.objects.filter(anon_suggested_sentences=unedited_sentence)
		for anon in anons_with_unedited_sentence_in_suggested.all():
			anon.anon_suggested_sentence_edits.add(sentence_edit)
			anon.save()


	def pass_sentence_to_contributive_edit(self, new_sentence, old_sentence, appearance_order=0):
		unedited_sentence = self.sentences.filter(sentence=old_sentence).order_by('creation_date')[appearance_order]
		sentence_edit = Sentence_Edit.objects.create(sentence=new_sentence, sentence_prior=old_sentence, accuracy=unedited_sentence.accuracy.all(), credibility=unedited_sentence.credibility.all(), author=unedited_sentence.author, post_views_before_sentence_edit=unedited_sentence.post_views_before_sentence_edit.all(), post_views_after_sentence_edit=unedited_sentence.post_views_after_sentence_edit.all(), one_day_has_passed=unedited_sentence.one_day_has_passed, one_day_view_bump_from_sentence_edit=unedited_sentence.one_day_view_bump_from_sentence_edit, odvbfse_with_assumed_information_decay=unedited_sentence.odvbfse_with_assumed_information_decay, odvbfse_waid_virality_day_two=unedited_sentence.odvbfse_waid_virality_day_two, odvbfse_woaid_virality_day_two=unedited_sentence.odvbfse_woaid_virality_day_two, two_days_have_passed=unedited_sentence.two_days_have_passed)
		unedited_sentence.contributed_sentence_edits.add(sentence_edit)
		self.post_collaborated_sentence_edits.add(sentence_edit)
		self.sentences.remove(unedited_sentence)
		new_edited_sentence = Sentence.objects.create(sentence=new_sentence, accuracy=unedited_sentence.accuracy.all(), credibility=unedited_sentence.credibility.all(), author=unedited_sentence.author, post_views_before_sentence_edit=unedited_sentence.post_views_before_sentence_edit.all())
		for view in unedited_sentence.post_views_after_sentence_edit.all():
			new_edited_sentence.post_views_before_sentence_edit.add(view)
		new_edited_sentence.save()
		self.sentences.add(new_edited_sentence)

		splitting = self.body.split(old_sentence)
		for bit in splitting[0:appearance_order]:
			if not appearance_order:
				new_body += bit + old_sentence
		new_body += new_sentence
		for bit in splitting[appearance_order:]:
			new_body += bit

		self.edits.add(Edit.objects.create(new_body=new_body, old_body=self.body, sentences=self.sentences.all(), author=self.author, post_id=self.id))
		self.body = new_body

		self.save()

		anons_with_unedited_sentence_in_saved = Anon.objects.filter(anon_saved_sentences=unedited_sentence)
		for anon in anons_with_unedited_sentence_in_saved.all():
			anon.anon_saved_sentence_edits.add(sentence_edit)
			anon.save()

		anons_with_unedited_sentence_in_collaborated = Anon.objects.filter(anon_collaborated_sentences=unedited_sentence)
		for anon in anons_with_unedited_sentence_in_collaborated.all():
			anon.anon_collaborated_sentence_edits.add(sentence_edit)
			anon.save()

		anons_with_unedited_sentence_in_contributed = Anon.objects.filter(anon_contributed_sentences=unedited_sentence)
		for anon in anons_with_unedited_sentence_in_contributed.all():
			anon.anon_contributed_sentence_edits.add(sentence_edit)
			anon.save()

		anons_with_unedited_sentence_in_suggested = Anon.objects.filter(anon_suggested_sentences=unedited_sentence)
		for anon in anons_with_unedited_sentence_in_suggested.all():
			anon.anon_suggested_sentence_edits.add(sentence_edit)
			anon.save()

	def pass_sentence_to_suggestive_edit(self, new_sentence, old_sentence, appearance_order=0):
		unedited_sentence = self.sentences.filter(sentence=old_sentence).order_by('creation_date')[appearance_order]
		sentence_edit = Sentence_Edit.objects.create(sentence=new_sentence, sentence_prior=old_sentence, accuracy=unedited_sentence.accuracy.all(), credibility=unedited_sentence.credibility.all(), author=unedited_sentence.author, post_views_before_sentence_edit=unedited_sentence.post_views_before_sentence_edit.all(), post_views_after_sentence_edit=unedited_sentence.post_views_after_sentence_edit.all(), one_day_has_passed=unedited_sentence.one_day_has_passed, one_day_view_bump_from_sentence_edit=unedited_sentence.one_day_view_bump_from_sentence_edit, odvbfse_with_assumed_information_decay=unedited_sentence.odvbfse_with_assumed_information_decay, odvbfse_waid_virality_day_two=unedited_sentence.odvbfse_waid_virality_day_two, odvbfse_woaid_virality_day_two=unedited_sentence.odvbfse_woaid_virality_day_two, two_days_have_passed=unedited_sentence.two_days_have_passed)
		unedited_sentence.suggested_sentence_edits.add(sentence_edit)
		self.post_collaborated_sentence_edits.add(sentence_edit)
		self.sentences.remove(unedited_sentence)
		new_edited_sentence = Sentence.objects.create(sentence=new_sentence, accuracy=unedited_sentence.accuracy.all(), credibility=unedited_sentence.credibility.all(), author=unedited_sentence.author, post_views_before_sentence_edit=unedited_sentence.post_views_before_sentence_edit.all())
		for view in unedited_sentence.post_views_after_sentence_edit.all():
			new_edited_sentence.post_views_before_sentence_edit.add(view)
		new_edited_sentence.save()
		self.sentences.add(new_edited_sentence)

		splitting = self.body.split(old_sentence)
		for bit in splitting[0:appearance_order]:
			if not appearance_order:
				new_body += bit + old_sentence
		new_body += new_sentence
		for bit in splitting[appearance_order:]:
			new_body += bit

		self.edits.add(Edit.objects.create(new_body=new_body, old_body=self.body, sentences=self.sentences.all(), author=self.author, post_id=self.id))
		self.body = new_body

		self.save()

		anons_with_unedited_sentence_in_saved = Anon.objects.filter(anon_saved_sentences=unedited_sentence)
		for anon in anons_with_unedited_sentence_in_saved.all():
			anon.anon_saved_sentence_edits.add(sentence_edit)
			anon.save()

		anons_with_unedited_sentence_in_collaborated = Anon.objects.filter(anon_collaborated_sentences=unedited_sentence)
		for anon in anons_with_unedited_sentence_in_collaborated.all():
			anon.anon_collaborated_sentence_edits.add(sentence_edit)
			anon.save()

		anons_with_unedited_sentence_in_contributed = Anon.objects.filter(anon_contributed_sentences=unedited_sentence)
		for anon in anons_with_unedited_sentence_in_contributed.all():
			anon.anon_contributed_sentence_edits.add(sentence_edit)
			anon.save()

		anons_with_unedited_sentence_in_suggested = Anon.objects.filter(anon_suggested_sentences=unedited_sentence)
		for anon in anons_with_unedited_sentence_in_suggested.all():
			anon.anon_suggested_sentence_edits.add(sentence_edit)
			anon.save()

   	# split by sentences. find location of cursor. count sentence repitition.

	def check_one_and_two_day_view_bumps(self):
		# BIG VIEW BUMPS ONE DAY -> sentence change highly impactful, value improvement score percentage
		# BIG VIEW BUMPS DAY TWO -> sentence change highly impactful and sustained, value improvement score viral percentage
		
		# BIG VIEW BUMPS ONE DAY with decay -> sentence change impactful, value improvement score percentage
		# BIG VIEW BUMPS DAY TWO with decay -> sentence change impactful, value improvement score viral percentage
		for sentence in self.sentences.all():
			if not sentence.one_day_has_passed:
				if timezone.now - sentence.creation_date > timedelta(+1):
					sentence.one_day_has_passed = True
					sentence.save()
					if sentence.post_views_after_sentence_edit.count() > sentence.post_views_before_sentence_edit.filter(creation_date__range=[sentence.creation_date - timedelta(+1), sentence.creation_date]).count():
						sentence.one_day_view_bump_from_sentence_edit = sentence.post_views_after_sentence_edit.count() - sentence.post_views_before_sentence_edit.filter(creation_date__range=[sentence.creation_date - timedelta(+1), sentence.creation_date]).count()
						sentence.save()
					if sentence.post_views_after_sentence_edit.count() > sentence.post_views_before_sentence_edit.filter(creation_date__range=[sentence.creation_date - timedelta(+1), sentence.creation_date]).count() - sentence.post_views_before_sentence_edit.filter(creation_date__range=[sentence.creation_date - timedelta(+2), sentence.creation_date]).count():
						sentence.odvbfse_with_assumed_information_decay = sentence.post_views_after_sentence_edit.count() - (sentence.post_views_before_sentence_edit.filter(creation_date__range=[sentence.creation_date - timedelta(+1), sentence.creation_date]).count() - sentence.post_views_before_sentence_edit.filter(creation_date__range=[sentence.creation_date - timedelta(+2), sentence.creation_date]).count())
						sentence.save()
					

				if not sentence.two_days_have_passed:
					if timezone.now - sentence.creation_date > timedelta(+2):
						sentence.two_days_have_passed = True
						sentence.save()
						if sentence.post_views_after_sentence_edit.count() - sentence.one_day_view_bump_from_sentence_edit > sentence.post_views_before_sentence_edit.filter(creation_date__range=[sentence.creation_date - timedelta(+1), sentence.creation_date]).count():
							sentence.odvbfse_woaid_virality_day_two = sentence.post_views_after_sentence_edit.count() - sentence.post_views_before_sentence_edit.filter(creation_date__range=[sentence.creation_date - timedelta(+1), sentence.creation_date]).count()
							sentence.save()
						if sentence.post_views_after_sentence_edit.count() - sentence.one_day_view_bump_from_sentence_edit > sentence.post_views_before_sentence_edit.filter(creation_date__range=[sentence.creation_date - timedelta(+1), sentence.creation_date]).count() - sentence.post_views_before_sentence_edit.filter(creation_date__range=[sentence.creation_date - timedelta(+2), sentence.creation_date]).count():
							sentence.odvbfse_waid_virality_day_two = sentence.post_views_after_sentence_edit.count() - sentence.one_day_view_bump_from_sentence_edit - (sentence.post_views_before_sentence_edit.filter(creation_date__range=[sentence.creation_date - timedelta(+1), sentence.creation_date]).count() - sentence.post_views_before_sentence_edit.filter(creation_date__range=[sentence.creation_date - timedelta(+2), sentence.creation_date]).count())
							sentence.save()




POST_SORT_CHOICES_CHAR = (
	("-viewcount", "Viral"),
	("viewcount", "Early"),
	("-latest_change_date", "Freshest"),
	("latest_change_date", "Eldest"),
	("-sum_has_viewed", "Most Viewed"),
	("sum_has_viewed", "Least Viewed"),
	("-sum_has_credibility", "Credibility"),
	("sum_has_credibility", "Non-credible"),
	("-sum_has_accuracy", "Accuracy"),
	("sum_has_accuracy", "Inaccurate"),
	("-sum_comments", "Most Commented On"),
	("sum_comments", "Least Commented On"),
	
)


ANON_SORT_CHOICES_CHAR = (
	("-sum_excluded_authors", "Most Authors Blocked"),
	("sum_excluded_authors", "Least Authors Blocked"),
	("-sum_posts", "Most Posts"),
	("sum_posts", "Least Posts"),
	("-sum_posted_comments", "Most Posted Comments"),
	("sum_posted_comments", "Least Posted Comments"),
	("-sum_saved_comments", "Most Saved Comments"),
	("sum_saved_comments", "Least Saved Comments"),
	("-sum_saved_posts", "Most Saved Posts"),
	("sum_saved_posts", "Least Saved Posts"),
	("-sum_following", "Following the Most"),
	("sum_following", "Following the Least"),
	("-sum_follows", "Followed by the Most"),
	("sum_follows", "Followed by the Least"),
	("-latest_change_date", "Most Recent Update"),
	("latest_change_date", "Least Recent Update"),
	("-latest_login_date", "Most Recent Login"),
	("latest_login_date", "Least Recent Login"),
	("-creation_date", "Newest Account Creation"),
	("creation_date", "Oldest Account Creation"),
)

class Densitivity(models.Model):
	scroll_height = models.IntegerField(default=0)
	duration_ms = models.IntegerField(default=0)
	
class Post_id(models.Model):
	post_id = models.IntegerField(default=0)
	author_id = models.IntegerField(default=0)
	
class Page_Density(models.Model):
	ip = models.CharField(max_length=15, default="")
	time_spent = models.IntegerField(default=0)
	density = models.ManyToManyField(Densitivity, default=None)
	post_ids = models.ManyToManyField(Post_id, default=None)
	scroll_height = models.IntegerField(default=0)
	scroll_type = models.CharField(choices=POST_SORT_CHOICES_CHAR, default="latest_change_date", max_length=180)
	client_height = models.IntegerField(default=0)
	duration = models.IntegerField(default=2)
	creation_date = models.DateTimeField(default=timezone.now)


DATE_CHOICES_CHAR = (
	("0,0,0,0","0 Minutes"),
	("15,0,0,0","15 Minutes"),
	("30,0,0,0","30 Minutes"),
	("45,0,0,0","45 Minutes"),
	("0,1,0,0","Hourly"),
	("0,2,0,0","2 Hourly"),
	("0,4,0,0","4 Hourly"),
	("0,6,0,0","6 Hourly"),
	("0,8,0,0","8 Hourly"),
	("0,10,0,0","10 Hourly"),
	("0,12,0,0","12 Hourly"),
	("0,16,0,0","16 Hourly"),
	("0,18,0,0","18 Hourly"),
	("0,20,0,0","20 Hourly"),
	("0,0,1,0","1 Daily"),
	("0,36,0,0","1.5 Daily"),
	("0,0,2,0","2 Daily"),
	("0,0,3,0","3 Daily"),
	("0,0,4,0","4 Daily"),
	("0,0,5,0","5 Daily"),
	("0,0,0,1","Weekly"),
	("0,0,0,2","2 Weekly"),
	("0,0,0,4","4 Weekly"),
	("0,0,0,8","8 Weekly"),
	("0,0,0,12","12 Weekly"),
	("0,0,0,16","16 Weekly"),
	("0,0,0,26","26 Weekly"),
	("0,0,0,39","39 Weekly"),
	("0,0,0,52","52 Weekly"),
	("0,0,0,78","78 Weekly"),
	("0,0,0,104","104 Weekly"),
	("0,0,0,156","156 Weekly"),
	("0,0,0,208","208 Weekly"),
	("0,0,0,260","260 Weekly"),
	("0,0,0,10000","All Time"),
)


LOCATION_CHOICES_CHAR = (
	("on_site","On-site"),
	("remote","Remote"),
	("hybrid","Hybrid"),
)

class JobSearching(models.Model):
	job_search_id = models.IntegerField(default=0)
	creation_date = models.DateTimeField(default=timezone.now)

class JobApplication(models.Model):
	author = models.ForeignKey(Author, on_delete=models.CASCADE, default=None)
	public = models.BooleanField(default=False)

	job_searchings_appeared = models.ManyToManyField(JobSearching, default=None)

	job_id = models.CharField(max_length=2000, default="")

	invite_only = models.BooleanField(default=False)
	invite_active = models.BooleanField(default=False)
	invite_code = models.CharField(max_length=200, default='')

	

	views = models.IntegerField(default=0)
	latest_change_date = models.DateTimeField(default=timezone.now)
	creation_date = models.DateTimeField(default=timezone.now)

	location_type = models.CharField(choices=LOCATION_CHOICES_CHAR, default="on_site", max_length=180)
	location = models.CharField(max_length=200, default='')

	company_name = models.CharField(max_length=200, default='')
	reference_link = models.URLField(max_length=20000, default='')

	character_description = models.TextField(max_length=1400, default="Character Description: ")
	character_values = models.TextField(max_length=1400, default="Character Values: ")
	personal_vision = models.TextField(max_length=1400, default="Personal Vision: ")
	personal_mission = models.TextField(max_length=1400, default="Personal Mission: ")
	impact_desires = models.TextField(max_length=1400, default="Impact Desires: ")
	related_job_description = models.TextField(max_length=1400, default="Related Job Description: ")
	related_position_summary = models.TextField(max_length=1400, default="Related Position Summary: ")
	related_qualifications = models.TextField(max_length=1400, default="Related Qualifications: ")
	related_knowledge = models.TextField(max_length=1400, default="Related Knowledge: ")
	related_skills = models.TextField(max_length=1400, default="Related Skills: ")
	related_experience = models.TextField(max_length=1400, default="Related Experience: ")
	desired_compensation = models.TextField(max_length=1400, default="Desired Compensation: ")
	additional_information = models.TextField(max_length=1400, default="Additional Information: ")

	



class Job(models.Model):
	author = models.ForeignKey(Author, on_delete=models.CASCADE, default=None)
	public = models.BooleanField(default=False)

	invite_only = models.BooleanField(default=False)
	invite_active = models.BooleanField(default=False)
	invite_code = models.CharField(max_length=200, default='')

	expires_by = models.DateTimeField(default=timezone.now)

	job_searchings_appeared = models.ManyToManyField(JobSearching, default=None)

	
	views = models.IntegerField(default=0)
	latest_change_date = models.DateTimeField(default=timezone.now)
	creation_date = models.DateTimeField(default=timezone.now)

	location_type = models.CharField(choices=LOCATION_CHOICES_CHAR, default="on_site", max_length=180)
	location = models.CharField(max_length=200, default='')

	company_name = models.CharField(max_length=200, default='')
	reference_link = models.URLField(max_length=20000, default='')

	company_description = models.TextField(max_length=1400, default="Company Description: ")
	company_values = models.TextField(max_length=1400, default="Company Values: ")
	company_vision = models.TextField(max_length=1400, default="Company Vision: ")
	company_mission = models.TextField(max_length=1400, default="Company Mission: ")
	impact_report = models.TextField(max_length=1400, default="Impact Report: ")
	job_description = models.TextField(max_length=1400, default="Job Description: ")
	position_summary = models.TextField(max_length=1400, default="Position Summary: ")
	qualifications = models.TextField(max_length=1400, default="Qualifications: ")
	knowledge_required = models.TextField(max_length=1400, default="Knowledge Required: ")
	skills_required = models.TextField(max_length=1400, default="Skills Required: ")
	experience_required = models.TextField(max_length=1400, default="Experience Required: ")
	compensation = models.TextField(max_length=1400, default="Compensation: ")
	additional_information = models.TextField(max_length=1400, default="Additional Information: ")

	job_applications = models.ManyToManyField(JobApplication, default=None, related_name="job_applications")
	interviewing_applications = models.ManyToManyField(JobApplication, default=None, related_name="interviewing_applications")
	successful_applications = models.ManyToManyField(JobApplication, default=None, related_name="successful_applications")

class JobSearch(models.Model):
	author = models.ForeignKey(Author, on_delete=models.CASCADE, default=None)
	creation_date = models.DateTimeField(default=timezone.now)
	keyword = models.CharField(max_length=200, default='')
	location = models.CharField(max_length=200, default='')
	ip = models.CharField(max_length=200, default='')

	on_site = models.BooleanField(default=False)
	remote = models.BooleanField(default=False)
	hybrid = models.BooleanField(default=False)

	free_intern = models.BooleanField(default=False)
	entry_level = models.BooleanField(default=False)
	junior = models.BooleanField(default=False)
	mid_level = models.BooleanField(default=False)
	senior = models.BooleanField(default=False)
	manager = models.BooleanField(default=False)
	executive = models.BooleanField(default=False)

	full_time = models.BooleanField(default=False)
	full_time_contract = models.BooleanField(default=False)
	part_time = models.BooleanField(default=False)
	contract_to_hire = models.BooleanField(default=False)

	company_name = models.CharField(max_length=200, default='')

	company_description = models.CharField(max_length=140, default="")
	company_values = models.CharField(max_length=140, default="")
	company_vision = models.CharField(max_length=140, default="")
	company_mission = models.CharField(max_length=140, default="")
	impact_report = models.CharField(max_length=140, default="")
	job_description = models.CharField(max_length=140, default="")
	position_summary = models.CharField(max_length=140, default="")
	qualifications = models.CharField(max_length=140, default="")
	knowledge_required = models.CharField(max_length=140, default="")
	skills_required = models.CharField(max_length=140, default="")
	experience_required = models.CharField(max_length=140, default="")
	compensation = models.CharField(max_length=140, default="")
	additional_information = models.CharField(max_length=140, default="")

	returns = models.ManyToManyField(Job, default=None)
	application_returns = models.ManyToManyField(JobApplication, default=None)
	job_searchings = models.ManyToManyField(JobSearching, default=None)



class RQAnswers(models.Model):
	author = models.ForeignKey(Author, on_delete=models.PROTECT, null=True)
	answer = models.TextField(max_length=140)


class RequestQuestion(models.Model):
	author = models.ForeignKey(Author, on_delete=models.PROTECT, null=True)
	question = models.TextField(max_length=140)
	answers = models.ManyToManyField(RQAnswers, default=None)


class Availability(models.Model):
	author = models.ForeignKey(Author, on_delete=models.PROTECT, null=True)
	
	concerning = models.TextField(max_length=140, default="All")
	location = models.TextField(max_length=140, default="Zoom/Meets/Messenger/WhatsApp/Instagram/Discord")
	request_questions = models.ManyToManyField(RequestQuestion, default=None, related_name="request_questions")
	post_request_questions = models.ManyToManyField(RequestQuestion, default=None, related_name="post_request_questions")
	start_time = models.DateTimeField(timezone.now)
	end_time = models.DateTimeField(timezone.now)
	available_and_not_unavailable = models.BooleanField(default=False) #mark either when you're availabilities are, or your unavailabilities are. "I can do any time from X" vs "I can't do these times"


class Keyword(models.Model):
	key_word = models.CharField(default='', max_length=66)

class BodyCounter(models.Model):
	keyword = models.CharField(default='', max_length=66)
	appearances_in_body_text = models.IntegerField(default=0)


class DoubleRightAdjacentBodyCounter(models.Model):
	left_keyword = models.CharField(default='', max_length=66)
	right_keyword = models.CharField(default='', max_length=66)
	rightmost_keyword = models.CharField(default='', max_length=66)
	appearances_in_body_text = models.IntegerField(default=0)

	def one_skip_one_by_two_count_in_body(self, body):
		split_body = body.split(self.left_keyword)
		for i in range(1, split_body.length - 1):
			splitsplit_body = split_body[i].split(" ")
			if splitsplit_body.length > 2:
				if splitsplit_body[1].startswith(self.right_keyword):
					if splitsplit_body[2].startswith(self.rightmost_keyword):
						self.appearances_in_body_text += 1
		self.save()

	def one_skip_two_by_two_count_in_body(self, body):
		split_body = body.split(self.left_keyword)
		for i in range(1, split_body.length - 1):
			splitsplit_body = split_body[i].split(" ")
			if splitsplit_body.length > 3:
				if splitsplit_body[2].startswith(self.right_keyword):
					if splitsplit_body[3].startswith(self.rightmost_keyword):
						self.appearances_in_body_text += 1
		self.save()

	def one_skip_three_by_two_count_in_body(self, body):
		split_body = body.split(self.left_keyword)
		for i in range(1, split_body.length - 1):
			splitsplit_body = split_body[i].split(" ")
			if splitsplit_body.length > 4:
				if splitsplit_body[3].startswith(self.right_keyword):
					if splitsplit_body[4].startswith(self.rightmost_keyword):
						self.appearances_in_body_text += 1
		self.save()

	def one_skip_four_by_two_count_in_body(self, body):
		split_body = body.split(self.left_keyword)
		for i in range(1, split_body.length - 1):
			splitsplit_body = split_body[i].split(" ")
			if splitsplit_body.length > 5:
				if splitsplit_body[4].startswith(self.right_keyword):
					if splitsplit_body[5].startswith(self.rightmost_keyword):
						self.appearances_in_body_text += 1
		self.save()

	def one_skip_five_by_two_count_in_body(self, body):
		split_body = body.split(self.left_keyword)
		for i in range(1, split_body.length - 1):
			splitsplit_body = split_body[i].split(" ")
			if splitsplit_body.length > 6:
				if splitsplit_body[5].startswith(self.right_keyword):
					if splitsplit_body[6].startswith(self.rightmost_keyword):
						self.appearances_in_body_text += 1
		self.save()


class DoubleLeftAdjacentBodyCounter(models.Model):
	leftmost_keyword = models.CharField(default='', max_length=66)
	left_keyword = models.CharField(default='', max_length=66)
	right_keyword = models.CharField(default='', max_length=66)
	appearances_in_body_text = models.IntegerField(default=0)

	def two_skip_one_by_one_count_in_body(self, body):
		split_body = body.split(self.leftmost_keyword+' 'self.left_keyword)
		for i in range(1, split_body.length - 1):
			splitsplit_body = split_body[i].split(" ")
			if splitsplit_body.length > 1:
				if splitsplit_body[1].startswith(self.right_keyword):
				self.appearances_in_body_text += 1
		self.save()

	def two_skip_two_by_one_count_in_body(self, body):
		split_body = body.split(self.leftmost_keyword+' 'self.left_keyword)
		for i in range(1, split_body.length - 1):
			splitsplit_body = split_body[i].split(" ")
			if splitsplit_body.length > 2:
				if splitsplit_body[2].startswith(self.right_keyword):
				self.appearances_in_body_text += 1
		self.save()

	def two_skip_three_by_one_count_in_body(self, body):
		split_body = body.split(self.leftmost_keyword+' 'self.left_keyword)
		for i in range(1, split_body.length - 1):
			splitsplit_body = split_body[i].split(" ")
			if splitsplit_body.length > 3:
				if splitsplit_body[3].startswith(self.right_keyword):
				self.appearances_in_body_text += 1
		self.save()

	def two_skip_four_by_one_count_in_body(self, body):
		split_body = body.split(self.leftmost_keyword+' 'self.left_keyword)
		for i in range(1, split_body.length - 1):
			splitsplit_body = split_body[i].split(" ")
			if splitsplit_body.length > 4:
				if splitsplit_body[4].startswith(self.right_keyword):
					self.appearances_in_body_text += 1
		self.save()

	def two_skip_five_by_one_count_in_body(self, body):
		split_body = body.split(self.leftmost_keyword+' 'self.left_keyword)
		for i in range(1, split_body.length - 1):
			splitsplit_body = split_body[i].split(" ")
			if splitsplit_body.length > 5:
				if splitsplit_body[5].startswith(self.right_keyword):
					self.appearances_in_body_text += 1
		self.save()

class AdjacentBodyCounter(models.Model):
	left_keyword = models.CharField(default='', max_length=66)
	right_keyword = models.CharField(default='', max_length=66)
	appearances_in_body_text = models.IntegerField(default=0)

	def one_by_one_count_in_body(self, body):
		split_body = body.split(self.left_keyword)
		for i in range(1, split_body.length):
			if split_body[i][1:].startswith(self.right_keyword):
				self.appearances_in_body_text += 1
		self.save()

	def one_skip_one_by_one_count_in_body(self, body):
		split_body = body.split(self.left_keyword)
		for i in range(1, split_body.length - 1):
			splitsplit_body = split_bdy[i].split(" ")
			if splitsplit_body.length > 1:
				if splitsplit_body[1].startswith(self.right_keyword):
					self.appearances_in_body_text += 1
		self.save()

	def one_skip_two_by_one_count_in_body(self, body):
		split_body = body.split(self.left_keyword)
		for i in range(1, split_body.length - 2):
			splitsplit_body = split_bdy[i].split(" ")
			if splitsplit_body.length > 2:
				if splitsplit_body[2].startswith(self.right_keyword):
					self.appearances_in_body_text += 1
		self.save()

	def one_skip_three_by_one_count_in_body(self, body):
		split_body = body.split(self.left_keyword)
		for i in range(1, split_body.length - 3):
			splitsplit_body = split_bdy[i].split(" ")
			if splitsplit_body.length > 2:
				if splitsplit_body[3].startswith(self.right_keyword):
					self.appearances_in_body_text += 1
		self.save()

	def one_skip_four_by_one_count_in_body(self, body):
		split_body = body.split(self.left_keyword)
		for i in range(1, split_body.length - 4):
			splitsplit_body = split_bdy[i].split(" ")
			if splitsplit_body.length > 3:
				if splitsplit_body[4].startswith(self.right_keyword):
					self.appearances_in_body_text += 1
		self.save()

	def one_skip_five_by_one_count_in_body(self, body):
		split_body = body.split(self.left_keyword)
		for i in range(1, split_body.length - 5):
			splitsplit_body = split_bdy[i].split(" ")
			if splitsplit_body.length > 4:
				if splitsplit_body[5].startswith(self.right_keyword):
					self.appearances_in_body_text += 1
		self.save()

class TripleAdjacentBodyCounter(models.Model):
	left_keyword = models.CharField(default='', max_length=66)
	middle_keyword = models.CharField(default='', max_length=66)
	right_keyword = models.CharField(default='', max_length=66)
	appearances_in_body_text = models.IntegerField(default=0)

	def one_by_one_by_one_count_in_body(self, body):
		three = self.left_keyword + ' ' + self.middle_keyword + ' ' + self.right_keyword
		for three in body:
			self.appearances_in_body_text += 1
		self.save()


class DoubleDoubleAdjacentBodyCounter(models.Model):
	leftmost_keyword = models.CharField(default='', max_length=66)
	left_keyword = models.CharField(default='', max_length=66)
	right_keyword = models.CharField(default='', max_length=66)
	rightmost_keyword = models.CharField(default='', max_length=66)
	appearances_in_body_text = models.IntegerField(default=0)

	def one_by_one_by_one_by_one_count_in_body(self, body):
		four = self.leftmost_keyword + ' ' + self.left_keyword + ' ' + self.right_keyword + ' ' + self.rightmost_keyword
		for four in body:
			self.appearances_in_body_text += 1
		self.save()

class SpacelessAdjacentBodyCounter(models.Model):
	left_keyword = models.CharField(default='', max_length=66)
	right_keyword = models.CharField(default='', max_length=66)
	appearances_in_body_text = models.IntegerField(default=0)

	def spaceless_count_in_body(self, body):
		spaceless = self.left_keyword + self.right_keyword
		for spaceless in body:
			self.appearances_in_body_text += 1
		self.save()


class TripleSpacelessAdjacentBodyCounter(models.Model):
	left_keyword = models.CharField(default='', max_length=66)
	middle_keyword = models.CharField(default='', max_length=66)
	right_keyword = models.CharField(default='', max_length=66)
	appearances_in_body_text = models.IntegerField(default=0)

	def spaceless_count_in_body(self, body):
		spaceless = self.left_keyword + self.middle_keyword + self.right_keyword
		for spaceless in body:
			self.appearances_in_body_text += 1
		self.save()


class DuoDuoBodyCounter(models.Model):
	leftmost_keyword = models.CharField(default='', max_length=66)
	left_keyword = models.CharField(default='', max_length=66)
	right_keyword = models.CharField(default='', max_length=66)
	rightmost_keyword = models.CharField(default='', max_length=66)

	appearances_in_body_text = models.IntegerField(default=0)

	def spaceless_by_spaceless_count_in_body(self, body):
		space_left = self.leftmost_keyword + self.left_keyword
		space_right = self.right_keyword + self.rightmost_keyword
		for space_left + ' ' + space_right in body:
			self.appearances_in_body_text += 1
		self.save()

class SpacelessQuatroBodyCounter(models.Model):
	leftmost_keyword = models.CharField(default='', max_length=66)
	left_keyword = models.CharField(default='', max_length=66)
	right_keyword = models.CharField(default='', max_length=66)
	rightmost_keyword = models.CharField(default='', max_length=66)

	appearances_in_body_text = models.IntegerField(default=0)

	def spaceless_by_spaceless_count_in_body(self, body):
		space_left = self.leftmost_keyword + self.left_keyword
		space_right = self.right_keyword + self.rightmost_keyword
		for space_left + space_right in body:
			self.appearances_in_body_text += 1
		self.save()

class ZipfsLawStatSignature(models.Model):
	one_of_one = models.ManyToManyField(BodyCounter, default=None)
	one_by_one = models.ManyToManyField(AdjacentBodyCounter, default=None, related_name="one_by_one")
	
	two_of_one = models.ManyToManyField(SpacelessAdjacentBodyCounter, default=None, related_name="two_of_one")

	one_skip_one_by_one = models.ManyToManyField(AdjacentBodyCounter, default=None, related_name="one_skip_one_by_one")
	one_skip_two_by_one = models.ManyToManyField(AdjacentBodyCounter, default=None, related_name="one_skip_two_by_one")
	one_skip_three_by_one = models.ManyToManyField(AdjacentBodyCounter, default=None, related_name="one_skip_three_by_one")
	one_skip_four_by_one = models.ManyToManyField(AdjacentBodyCounter, default=None, related_name="one_skip_four_by_one")
	one_skip_five_by_one = models.ManyToManyField(AdjacentBodyCounter, default=None, related_name="one_skip_five_by_one")

	one_by_one_by_one = models.ManyToManyField(TripleAdjacentBodyCounter, default=None)
	
	three_of_one = models.ManyToManyField(TripleSpacelessAdjacentBodyCounter, default=None)

	two_skip_one_by_one = models.ManyToManyField(DoubleLeftAdjacentBodyCounter, default=None, related_name="two_skip_one_by_one")
	two_skip_two_by_one = models.ManyToManyField(DoubleLeftAdjacentBodyCounter, default=None, related_name="two_skip_two_by_one")
	two_skip_three_by_one = models.ManyToManyField(DoubleLeftAdjacentBodyCounter, default=None, related_name="two_skip_three_by_one")
	two_skip_four_by_one = models.ManyToManyField(DoubleLeftAdjacentBodyCounter, default=None, related_name="two_skip_four_by_one")
	two_skip_five_by_one = models.ManyToManyField(DoubleLeftAdjacentBodyCounter, default=None, related_name="two_skip_five_by_one")

	one_skip_one_by_two = models.ManyToManyField(DoubleRightAdjacentBodyCounter, default=None, related_name="one_skip_one_by_two")
	one_skip_two_by_two = models.ManyToManyField(DoubleRightAdjacentBodyCounter, default=None, related_name="one_skip_two_by_two")
	one_skip_three_by_two = models.ManyToManyField(DoubleRightAdjacentBodyCounter, default=None, related_name="one_skip_three_by_two")
	one_skip_four_by_two = models.ManyToManyField(DoubleRightAdjacentBodyCounter, default=None, related_name="one_skip_four_by_two")
	one_skip_five_by_two = models.ManyToManyField(DoubleRightAdjacentBodyCounter, default=None, related_name="one_skip_five_by_two")

	one_by_one_by_one_by_one = models.ManyToManyField(DoubleDoubleBodyCounter, default=None)
	two_by_two = models.ManyToManyField(DuoDuoBodyCounter, default=None)
	four_of_one = models.ManyToManyField(SpacelessQuatroBodyCounter, default=None)



class Topic(models.Model):
	topic_name = models.CharField(default='Topic Name', max_length=66)
	privacy_settings = models.IntegerField(default=0)
	active_admins = models.ManyToManyField(Author, default=None)
	key_words_to_include = models.ManyToManyField(Keyword, default=None, related_name="key_words_to_include")
	key_words_to_exclude = models.ManyToManyField(Keyword, default=None, related_name="key_words_to_exclude")
	exact_match = models.CharField(default='', max_length=66)
	date_range_start = models.DateTimeField(default=timezone.now)
	date_range_end = models.DateTimeField(default=timezone.now)

class SubFolder(models.Model):
	folder_id = models.IntegerField(default=1)

CATEGORY_CHOICES = (
	("Public"),
	("Private"),
	("Organisation")
)

class Folder(models.Model):
	name = models.CharField(default='Folder Name', max_length=66)
	sub_folders = models.ManyToManyField(SubFolder, default=None)
	order = models.IntegerField(default=0)
	collaborators = models.ManyToManyField(Author, default=None)
	comments = models.ManyToManyField(Comment, default=None)
	category = models.CharField(choices=CATEGORY_CHOICES, default="Public")

class CollaborationWorkspace(models.Model):
	folders = models.ManyToManyField(Folder, default=None)



def validate_phone_number(value):
    phone_regex = r"^\+?1?\d{9,15}$"
    if not re.match(phone_regex, value):
        raise ValidationError("Invalid phone number format.")






from random import randrange
class VerificationNumbers(models.Model):
	verification_number = models.IntegerField(default=int(str(randrange(10))+str(randrange(10))+str(randrange(10))+str(randrange(10))+str(randrange(10))+str(randrange(10))+str(randrange(10))+str(randrange(10))+str(randrange(10))))


class Anon(models.Model):
	username = models.OneToOneField(User, on_delete=models.CASCADE)
	email = models.EmailField(max_length=144, default='', null=True)
	email_verify = models.OneToOneField(VerificationNumbers, default=None, null=True, on_delete=models.CASCADE, blank=True, related_name="email_verify")
	phone = models.CharField(max_length=16, validators=[validate_phone_number], blank=True, null=True)
	phone_verify = models.OneToOneField(VerificationNumbers, default=None, null=True, on_delete=models.CASCADE, blank=True, related_name="phone_verify")
	
	friends = models.ManyToManyField(Author, default=None, related_name="friends")
	following = models.ManyToManyField(Author, default=None, related_name="following")
	followed_by = models.ManyToManyField(Author, default=None, related_name="followed_by")
	
	blocked_authors = models.ManyToManyField(Author, default=None, related_name="blocked_authors")
	blocked_by_authors = models.ManyToManyField(Author, default=None, related_name="blocked_by_authors")

	latest_change_date = models.DateTimeField(default=timezone.now)
	creation_date = models.DateTimeField(default=timezone.now)
	sent_messages = models.ManyToManyField(Comment, default=None, related_name='sent_messages')
	sum_sent_messages = models.IntegerField(default=0)
	received_messages = models.ManyToManyField(Comment, default=None, related_name='received_messages')
	sum_received_messages = models.IntegerField(default=0)
	posted_comments = models.ManyToManyField(Comment, default=None, related_name='posted_comments')
	sum_posted_comments = models.IntegerField(default=0)
	saved_comments = models.ManyToManyField(Comment, default=None, related_name='saved_comments')
	sum_saved_comments = models.IntegerField(default=0)
	reposting_comments = models.ManyToManyField(Comment, default=None, related_name='reposting_comments')
	sum_reposting_comments = models.IntegerField(default=0)
	reposted_comments = models.ManyToManyField(Comment, default=None, related_name='reposted_comments')
	sum_reposted_comments = models.IntegerField(default=0)
	comment_sort_char = models.CharField(choices=COMMENT_SORT_CHOICES_CHAR, default="latest_change_date", max_length=180)
	comment_sort_depth_char = models.CharField(choices=DATE_CHOICES_CHAR, default="0,0,0,10000", max_length=180)
	comment_sort_from_date_char = models.CharField(choices=DATE_CHOICES_CHAR, default="0,0,0,0", max_length=180)
	

	posts = models.ManyToManyField(Post, blank=True, default=None, related_name="anon_posts")
	sum_posts = models.IntegerField(default=0)
	edits = models.ManyToManyField(Edit, default=None)
	sum_edits = models.IntegerField(default=0)
	reposts = models.ManyToManyField(Post, blank=True, default=None, related_name="reposts")
	sum_reposts = models.IntegerField(default=0)

	contributed_on_posts = models.ManyToManyField(Post, blank=True, default=None, related_name="contributed_on_posts")
	sum_contributed_on_posts = models.IntegerField(default=0)
	commented_on_posts = models.ManyToManyField(Post, blank=True, default=None, related_name="commented_on_posts")
	sum_commented_on_posts = models.IntegerField(default=0)
	collaborated_on_posts = models.ManyToManyField(Post, blank=True, default=None, related_name="collaborated_on_posts")
	sum_collaborated_on_posts = models.IntegerField(default=0)
	contributed_on_posts = models.ManyToManyField(Post, blank=True, default=None, related_name="contributed_on_posts")
	sum_contributed_on_posts = models.IntegerField(default=0)
	suggested_on_posts = models.ManyToManyField(Post, blank=True, default=None, related_name="suggested_on_posts")
	sum_suggested_on_posts = models.IntegerField(default=0)

	saved_sentences = models.ManyToManyField(Sentence, default=None, related_name="anon_saved_sentences")
	sum_saved_sentences = models.IntegerField(default=0)
	collaborated_sentences = models.ManyToManyField(Sentence, default=None, related_name="anon_collaborated_sentences")
	sum_collaborated_sentences = models.IntegerField(default=0)
	contributed_sentences = models.ManyToManyField(Sentence, default=None, related_name="anon_contributed_sentences")
	sum_contributed_sentences = models.IntegerField(default=0)
	suggested_sentences = models.ManyToManyField(Sentence, default=None, related_name="anon_suggested_sentences")
	sum_suggested_sentences = models.IntegerField(default=0)

	saved_sentence_edits = models.ManyToManyField(Sentence_Edit, default=None, related_name="anon_saved_sentence_edits")
	sum_saved_sentence_edits = models.IntegerField(default=0)
	collaborated_sentence_edits = models.ManyToManyField(Sentence_Edit, default=None, related_name="anon_collaborated_sentence_edits")
	sum_collaborated_sentence_edits = models.IntegerField(default=0)
	contributed_sentence_edits = models.ManyToManyField(Sentence_Edit, default=None, related_name="anon_contributed_sentence_edits")
	sum_contributed_sentence_edits = models.IntegerField(default=0)
	suggested_sentence_edits = models.ManyToManyField(Sentence_Edit, default=None, related_name="anon_suggested_sentence_edits")
	sum_suggested_sentence_edits = models.IntegerField(default=0)



	invite_to_collaborate_on_posts = models.ManyToManyField(Post, blank=True, default=None, related_name="invite_to_collaborate_on_posts")
	sum_invite_to_collaborate_on_posts = models.IntegerField(default=0)
	
	sum_earnt_from_posts = models.IntegerField(default=0)
	sum_earnt_from_collaborations = models.IntegerField(default=0)
	sum_earnt_from_comments = models.IntegerField(default=0)
	sum_earnt_from_contributions = models.IntegerField(default=0)
	post_sort_char = models.CharField(choices=POST_SORT_CHOICES_CHAR, default="latest_change_date", max_length=180)
	post_sort_depth_char = models.CharField(choices=DATE_CHOICES_CHAR, default="0,0,0,120", max_length=180)
	post_sort_from_date_char = models.CharField(choices=DATE_CHOICES_CHAR, default="0,0,0,0", max_length=180)
	
	anon_sort_char = models.CharField(choices=ANON_SORT_CHOICES_CHAR, default="latest_change_date", max_length=180)
	anon_sort_depth_char = models.CharField(choices=DATE_CHOICES_CHAR, default="0,0,0,120", max_length=180)
	anon_sort_from_date_char = models.CharField(choices=DATE_CHOICES_CHAR, default="0,0,0,0", max_length=180)
	

	past_credibility_sort_depth_char = models.CharField(choices=DATE_CHOICES_CHAR, default="0,0,0,120", max_length=180)
	past_credibility_sort_from_date_char = models.CharField(choices=DATE_CHOICES_CHAR, default="0,0,0,0", max_length=180)
	
	past_accuracy_sort_depth_char = models.CharField(choices=DATE_CHOICES_CHAR, default="0,0,0,120", max_length=180)
	past_accuracy_sort_from_date_char = models.CharField(choices=DATE_CHOICES_CHAR, default="0,0,0,0", max_length=180)
	
	past_sentence_before_edit_views_sort_depth_char = models.CharField(choices=DATE_CHOICES_CHAR, default="0,0,0,120", max_length=180)
	past_sentence_before_edit_views_sort_from_date_char = models.CharField(choices=DATE_CHOICES_CHAR, default="0,0,0,0", max_length=180)
	
	past_sentence_after_edit_views_sort_depth_char = models.CharField(choices=DATE_CHOICES_CHAR, default="0,0,0,120", max_length=180)
	past_sentence_after_edit_views_sort_from_date_char = models.CharField(choices=DATE_CHOICES_CHAR, default="0,0,0,0", max_length=180)
	

	is_viewing = models.BooleanField(default=False)


	all_files = models.ManyToManyField(File, default=None, related_name="all_files")
	public_files = models.ManyToManyField(File, default=None, related_name="public_files")

	notifications = models.ManyToManyField(Notification, default=None, related_name="old_notifications")
	new_notifications = models.ManyToManyField(Notification, default=None, related_name="new_notifications")

	availabilities = models.ManyToManyField(Availability, default=None, related_name="availabilities")
	shared_with_availabilities = models.ManyToManyField(Availability, default=None, related_name="shared_with_availabilities")
	students = models.ManyToManyField(Author, default=None, related_name="students")
	student_of = models.ManyToManyField(Author, default=None, related_name="student_of")
	employees = models.ManyToManyField(Author, default=None, related_name="employees")
	employed_by = models.ManyToManyField(Author, default=None, related_name="employed_by")

	job_searches = models.ManyToManyField(JobSearch, default=None)
	job_listings = models.ManyToManyField(Job, default=None, related_name="job_listings")
	job_interviews = models.ManyToManyField(Job, default=None, related_name="job_interviews")
	jobs_accepted = models.ManyToManyField(Job, default=None, related_name="jobs_accepted")
	job_applications = models.ManyToManyField(JobApplication, default=None)

	
	def __unicode__(self):
		return unicode(self.username) or u''

	
		
			


import datetime

class IpAddress(models.Model):
	ip_address = models.TextField(default='', max_length=200)

class UserViews(models.Model):
	anon = models.ForeignKey(Anon, default=None, on_delete=models.PROTECT, null=True)
	view_date = models.DateTimeField(default=timezone.now)
	ip_address = models.TextField(default='', max_length=200, null=True)
	httpxforwardfor = models.TextField(default='', max_length=20000, null=True)
	page_view = models.CharField(max_length=200, default='', null=True)
	previous_view_id = models.CharField(max_length=144, default='', null=True)
	previous_page = models.CharField(max_length=200, default='', null=True)
	previous_view_date = models.DateTimeField(default=timezone.now)
	previous_view_time_between_pages = models.DurationField(default=datetime.timedelta(days=0, seconds=1))

	

class Pageviews(models.Model):
	page = models.CharField(max_length=200, default='')
	views = models.IntegerField(default=0)
	ip_addresses = models.ManyToManyField(IpAddress, default=None)
	user_views = models.ManyToManyField(UserViews, default=None)
	translation = models.CharField(max_length=2, default='en')




