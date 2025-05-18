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
	spent_invoices = models.ManyToManyField(Invoice, default=None, related_name='spentinvoices')
	earnt_invoices = models.ManyToManyField(Invoice, default=None, related_name='earntinvoices')

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


class Commend_Edit(models.Model):
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
	author = models.ForeignKey(Author, on_delete=models.PROTECT, default=None)
	creation_date = models.DateTimeField(default=timezone.now)
	sentence_id = models.IntegerField(default=0)

class Sentence(models.Model):
	sentence = models.TextField(max_length=1440)
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
	body = models.TextField(max_length=144000, default='')
	sentences = models.ManyToManyField(Sentence, default=None)
	post_id = models.IntegerField(default=0)
	author = models.ForeignKey(Author, on_delete=models.PROTECT, default=None)
	creation_date = models.DateTimeField(default=timezone.now)

	
	

class Post(models.Model):
	author = models.ForeignKey(Author, on_delete=models.CASCADE, default=None, null=True)
	sentences = models.ManyToManyField(Sentence, default=None)
	edits = models.ManyToManyField(Edit, default=None)
	title = models.CharField(max_length=200, default='')
	has_commented = models.ManyToManyField(Author, default=None, related_name='post_has_commented')
	sum_has_commented = models.IntegerField(default=0)
	has_viewed = models.ManyToManyField(Author, default=None, related_name='post_has_viewed')
	sum_has_viewed = models.IntegerField(default=0)
	has_credibilities = models.ManyToManyField(Author, default=None, related_name='post_has_voted')
	sum_has_credibilities = models.IntegerField(default=0)
	has_accuracy = models.ManyToManyField(Author, default=None, related_name='post_has_voted')
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


class Page_Density(models.Model):
	ip = models.CharField(max_length=15, default="")
	time_spent = models.IntegerField(default=0)
	density = models.ManyToManyField(Densitivity, default=None)
	post_ids = models.ManyToManyField(Post_id, default=None)
	scroll_height = models.IntegerField(default=0)
	scroll_type = models.CharField(choices=POST_SORT_CHOICES_CHAR, default="latest_change_date", max_length=180)
	client_height = models.IntegerField(default=0)
	duration = models.IntegerField(default=2)


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


class Anon(models.Model):
	username = models.OneToOneField(User, on_delete=models.CASCADE)
	email = models.EmailField(max_length=144, default='', null=True)
	
	friends = models.ManyToManyField(Author, default=None, related_name="friends")
	following = models.ManyToManyField(Author, default=None, related_name="following")
	followed_by = models.ManyToManyField(Author, default=None, related_name="followed_by")
	
	latest_change_date = models.DateTimeField(default=timezone.now)
	creation_date = models.DateTimeField(default=timezone.now)
	sent_messages = models.ManyToManyField(Comment, default=None, related_name='sent_messages')
	sum_sent_messages models.IntegerField(default=0)
	received_messages = models.ManyToManyField(Comment, default=None, related_name='received_messages')
	sum_received_messages = models.IntegerField(default=0)
	posted_comments = models.ManyToManyField(Comment, default=None, related_name='posted_comments')
	sum_posted_comments = models.IntegerField(default=0)
	saved_comments = models.ManyToManyField(Comment, default=None, related_name='saved_comments')
	sum_saved_comments = models.IntegerField(default=0)
	reposting_comments = models.ManyToManyField(Comment, default=None, related_name='reposting_comments')
	sum_reposting_comments = models.IntegerField(default=0)
	reposted_comments = models.ManyToManyField(Comment, default=None, related_name='reposting_comments')
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

	invite_to_collaborate_on_posts = models.ManyToManyField(Post, blank=True, default=None, related_name="invite_to_collaborate_on_posts")
	sum_invite_to_collaborate_on_posts = models.IntegerField(default=0)
	
	sum_earnt_from_posts = models.IntegerField(default=0)
	sum_earnt_from_collaborations = models.IntegerField(default=0)
	sum_earnt_from_comments = models.IntegerField(default=0)
	sum_earnt_from_contributions = models.IntegerField(default=0)
	post_sort_char = models.CharField(choices=POST_SORT_CHOICES_CHAR, default="latest_change_date", max_length=180)
	post_sort_depth_char = models.CharField(choices=DATE_CHOICES_CHAR, default="0,0,0,120", max_length=180)
	post_sort_from_date_char = models.CharField(choices=DATE_CHOICES_CHAR, default="0,0,0,0", max_length=180)
	
	spaces = models.ManyToManyField(Space, blank=True, default=None, related_name='spaces')
	sum_spaces = models.IntegerField(default=0)
	currently_monthly_spaces_earnings = models.IntegerField(default=0)
	sum_earnt_from_spaces = models.IntegerField(default=0)

	saved_spaces = models.ManyToManyField(Space, blank=True, default=None, related_name='saved_spaces')
	
	purchased_spaces = models.ManyToManyField(Space, blank=True, default=None, related_name='purchased_spaces')
	currently_monthly_spaces_spendings = models.IntegerField(default=0)
	sum_purchased_spaces = models.IntegerField(default=0)
	sum_spent_on_spaces = models.IntegerField(default=0)
	space_sort = models.IntegerField(choices=SPACE_SORT_CHOICES, default=0)
	space_sort_char = models.CharField(choices=SPACE_SORT_CHOICES_CHAR, default="latest_change_date", max_length=180)
	space_sort_depth_char = models.CharField(choices=DATE_CHOICES_CHAR, default="0,0,0,10000", max_length=180)
	space_sort_from_date_char = models.CharField(choices=DATE_CHOICES_CHAR, default="0,0,0,0", max_length=180)
	
	created_votestyles = models.ManyToManyField(Votes, default=None, related_name='created_votestyles')
	sum_created_votestyles = models.IntegerField(default=0)
	saved_votestyles = models.ManyToManyField(Votes, default=None, related_name='saved_votestyles')
	applied_votestyles = models.ManyToManyField(Votes, default=None, related_name='applied_votestyles')
	excluded_votestyles = models.ManyToManyField(Votes, default=None, related_name='excluded_votestyles')

	past_votes = models.ManyToManyField(Votings, default=None, related_name='past_votes')
	past_votes_sort_depth_char = models.CharField(choices=DATE_CHOICES_CHAR, default="0,0,0,10000", max_length=180)
	past_votes_sort_from_date_char = models.CharField(choices=DATE_CHOICES_CHAR, default="0,0,0,0", max_length=180)

	sum_past_votes = models.IntegerField(default=0)
	sum_past_votes_earnings = models.IntegerField(default=0)
	search_urls = models.ManyToManyField(SearchURL, default=None)
	
	monero_wallet = models.CharField(max_length=200, default='')
	false_wallet = models.IntegerField(default=0)

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

	owned_variable_views = models.ManyToManyField(UserSpecificJavaScriptVariableViewLearning, default=None, related_name="owned_variable_views")
	viewed_variable_views = models.ManyToManyField(UserSpecificJavaScriptVariableViewLearning, default=None, related_name="viewed_variable_views")


	settings_word_ads = models.BooleanField(default=True)
	settings_post_ads = models.BooleanField(default=True)
	settings_dictionary_ads = models.BooleanField(default=True)
	settings_space_ads = models.BooleanField(default=True)


	loans = models.ManyToManyField(Loan, default=None)


	def __unicode__(self):
		return unicode(self.username) or u''

	def lotallet(self):
		if str(self.false_wallet).endswith("0"):
			self.false_wallet += 8
		elif str(self.false_wallet).endswith("1"):
			self.false_wallet += 0
		elif str(self.false_wallet).endswith("2"):
			self.false_wallet += 1
		elif str(self.false_wallet).endswith("3"):
			self.false_wallet += 1
			if self.monero_wallet == "half":
				self.false_wallet += 1
			else:
				self.monero_wallet = "half"

		elif str(self.false_wallet).endswith("4"):
			self.false_wallet += 9
		elif str(self.false_wallet).endswith("5"):
			self.false_wallet += 3
		elif str(self.false_wallet).endswith("6"):
			self.false_wallet -= 4
		elif str(self.false_wallet).endswith("7"):
			self.false_wallet += 1
		elif str(self.false_wallet).endswith("8"):
			self.false_wallet += 880
		elif str(self.false_wallet).endswith("11"):
			self.false_wallet += 77
		elif str(self.false_wallet).endswith("12"):
			self.false_wallet -= 12
		elif str(self.false_wallet).endswith("13"):
			self.false_wallet -= 12
		elif str(self.false_wallet).endswith("28"):
			self.false_wallet -= 5
		elif str(self.false_wallet).endswith("23"):
			self.false_wallet += 5
		elif str(self.false_wallet).endswith("16"):
			self.false_wallet += 2
		elif str(self.false_wallet).endswith("18"):
			self.false_wallet -= 2
		elif str(self.false_wallet).endswith("21"):
			self.false_wallet -= 4
		elif str(self.false_wallet).endswith("22"):
			self.false_wallet += 1
		elif str(self.false_wallet).endswith("24"):
			self.false_wallet -= 24
		elif str(self.false_wallet).endswith("25"):
			self.false_wallet -= 24
		elif str(self.false_wallet).endswith("26"):
			self.false_wallet -= 25
		elif str(self.false_wallet).endswith("27"):
			self.false_wallet += 59
		elif str(self.false_wallet).endswith("29"):
			self.false_wallet -= 28
		elif str(self.false_wallet).endswith("30"):
			self.false_wallet += 1
		elif str(self.false_wallet).endswith("31"):
			self.false_wallet += 2
		elif str(self.false_wallet).endswith("32"):
			self.false_wallet += 0
		elif str(self.false_wallet).endswith("33"):
			self.false_wallet += 11
		elif str(self.false_wallet).endswith("40"):
			self.false_wallet += 4
		elif str(self.false_wallet).endswith("44"):
			self.false_wallet -= 11
		elif str(self.false_wallet).endswith("55"):
			self.false_wallet += 11
		elif str(self.false_wallet).endswith("66"):
			self.false_wallet += 1
		elif str(self.false_wallet).endswith("69"):
			self.false_wallet -= 58
		elif str(self.false_wallet).endswith("77"):
			self.false_wallet -= 6
		elif str(self.false_wallet).endswith("81"):
			self.false_wallet += 7
		elif str(self.false_wallet).endswith("88"):
			self.false_wallet -= 6
		elif str(self.false_wallet).endswith("99"):
			self.false_wallet -= 30
		elif str(self.false_wallet).endswith("100"):
			self.false_wallet -= 100
		elif str(self.false_wallet).endswith("101"):
			self.false_wallet += 101
		elif str(self.false_wallet).endswith("102"):
			self.false_wallet += 1
		elif str(self.false_wallet).endswith("103"):
			self.false_wallet += 1 - 1 + 1 - 1
			if self.monero_wallet == "half":
				self.false_wallet += 1
			else:
				self.monero_wallet = "half"
		elif str(self.false_wallet).endswith("123"):
			self.false_wallet += 5
		elif str(self.false_wallet).endswith("124"):
			self.false_wallet -= 116
		elif str(self.false_wallet).endswith("128"):
			self.false_wallet -= 5
		elif str(self.false_wallet).endswith("142"):
			self.false_wallet -= 18
		elif str(self.false_wallet).endswith("148"):
			self.false_wallet -= 20
		elif str(self.false_wallet).endswith("210"):
			self.false_wallet += 678
		elif str(self.false_wallet).endswith("600"):
			self.false_wallet += 288
		elif str(self.false_wallet).endswith("333"):
			self.false_wallet += 555
		elif str(self.false_wallet).endswith("555"):
			self.false_wallet += 333
		elif str(self.false_wallet).endswith("888"):
			self.false_wallet += 1
		elif str(self.false_wallet).endswith("999"):
			self.false_wallet -= 666
		elif str(self.false_wallet).endswith("1238"):
			self.false_wallet += 45
		elif str(self.false_wallet).startswith("1"):
			leg = len(str(self.false_wallet))
			legs = 0
			for l in leg:
				self.false_wallet -= int(str(self.false_wallet)[:legs])
				self.false_wallet += 8 * (1+legs*10)
				legs += 1
			self.false_wallet -= 8 * legs * 10
		elif str(self.false_wallet).startswith("2"):
			leg = len(str(self.false_wallet))
			legs = 0
			for l in leg:
				self.false_wallet -= int(str(self.false_wallet)[:legs])
				self.false_wallet += 8 * (1+legs*10)
				legs += 1
			self.false_wallet -= 8 * legs * 10
		elif str(self.false_wallet).startswith("3"):
			leg = len(str(self.false_wallet))
			legs = 0
			for l in leg:
				self.false_wallet -= int(str(self.false_wallet)[:legs])
				self.false_wallet += 8 * (1+legs*10)
				legs += 1
			self.false_wallet -= 8 * legs * 10
		elif str(self.false_wallet).startswith("8"):
			leg = len(str(self.false_wallet))
			legs = 0
			for l in leg:
				self.false_wallet -= int(str(self.false_wallet)[:legs])
				self.false_wallet += 8 * (1+legs*10)
				legs += 1
			self.false_wallet -= 8 * legs * 10
		elif str(self.false_wallet).startswith("6"):
			leg = len(str(self.false_wallet))
			legs = 0
			for l in leg:
				self.false_wallet -= int(str(self.false_wallet)[:legs])
				self.false_wallet += 9 * (1+legs*10)
				legs += 1
			self.false_wallet -= 9 * legs * 10
		elif str(self.false_wallet).startswith("0"):
			leg = len(str(self.false_wallet))
			self.false_wallet += 1*leg
		elif len(str(self.false_wallet)) > 6:
			if str(self.false_wallet)[2] == "3":
				self.false_wallet += 600000
		elif len(str(self.false_wallet)) > 9:
			if str(self.false_wallet)[5] == "6":
				self.false_wallet += 999999999

				
				

		
			


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




