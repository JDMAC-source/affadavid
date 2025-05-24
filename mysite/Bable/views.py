# Copyright Aden Handasyde 2019

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.db.models import F, Q, Count
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from .models import *
# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import AuthenticationForm
from .forms import *
#from instantiatetotality import *
from django.core.mail import EmailMessage


from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.forms import formset_factory, modelformset_factory
from paypal.standard.forms import PayPalPaymentsForm
from django.urls import reverse
from django.conf import settings

from django.utils import timezone

from unidecode import unidecode
from django.template import defaultfilters

from .serializers import *
from rest_framework import status
from rest_framework import viewsets, permissions, authentication
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.utils.text import slugify
from django.template.loader import render_to_string
#from weasyprint import HTML

from django.http import HttpResponseRedirect
from django.utils.translation import gettext as _


from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import ListAPIView
from rest_framework.generics import UpdateAPIView
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated, BasePermission # new import

# Create your views here.
from Bable.models import Post
from Bable.serializers import PostSerializer

#from coinbase_commerce.client import Client

from django.http import StreamingHttpResponse
import datetime
from datetime import date
from datetime import timedelta
import time




# Stripe Auth here
from django.http import HttpResponseRedirect

import stripe
from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator

from django.contrib.auth.mixins import LoginRequiredMixin

class dotdict(dict):
    """dot.notation access to dictionary attributes"""
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__

'''
@login_required
def stream(request):
	loggedinuser = User.objects.get(username=request.user.username)
	loggedinanon = Anon.objects.get(username=loggedinuser)
	now = datetime.datetime.now()
	def event_stream():
		while True:
			time.sleep(1)
			notifications = loggedinanon.notifications.filter(new=True)
			if not notifications:
				yield 'retry: 100000\n\n'
				break
			else:
				yield 'retry: 100000\n\n'
				yield 'data: {}'.format(notifications.count())

	return StreamingHttpResponse(event_stream(), content_type='text/event-stream')


@login_required
def stream_unseen(request):
	loggedinuser = User.objects.get(username=request.user.username)
	loggedinanon = Anon.objects.get(username=loggedinuser)
	def event_stream():
		while True:
			time.sleep(1)
			notifications = loggedinanon.notifications.filter(new=True)
			recent_notification = notifications.filter(sent=False).order_by('creation_date').first()
			if not recent_notification:
				yield 'retry: 100000\n\n'
				break
			else:
				yield 'retry: 100000\n\n'
				yield 'data: {}'.format(recent_notification.text)
	return StreamingHttpResponse(event_stream(), content_type='text/event-stream')


def send_notification(author, text):
    Notification.objects.create(
        author=author, text=text
    )
'''

from django.http import HttpResponseRedirect, JsonResponse

def grabusername(request):
	if request.GET.get('name'):
		q = request.GET['name']
		if not User.objects.filter(username__startswith=q):
			return True



def autocomplete_votestyles(request):
	if request.GET.get('q'):
		q = request.GET.get('q')
		if Votes.objects.filter(the_vote_name__startswith=q):
			data = Votes.objects.filter(the_vote_name__startswith=q).order_by('-creation_date').values_list('the_vote_name',flat=True)
			json = list(data)
			return JsonResponse(json, safe=False)
		return JsonResponse([], safe=False)
	else:
		data = Votes.objects.all().order_by('-creation_date').values_list('the_vote_name',flat=True)
		json = list(data)
		return JsonResponse(json, safe=False)




class ExampleAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        username = request.META.get('HTTP_X_USERNAME')
        if not username:
            return None

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed('No such user')

        return (user, None)


from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response



class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(CustomObtainAuthToken, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        return Response({'token': token.key, 'id': token.user_id})

from django.contrib.auth.decorators import user_passes_test
def email_check(user):
   return user.email.endswith('.com')


@user_passes_test(email_check)
def email_all_emails(request):

	return HttpResponse("Finished")

class IsSuperUser(BasePermission):
    """
    Allows access only to admin users.
    """

    def has_permission(self, request, view):
        is_superuser = request.user and request.user.is_superuser
        if not is_superuser and request.user:
            # Your ban logic goes here
            pass
        return is_superuser


# Create your views here.

class ListPostAPIView(ListAPIView):
    """This endpoint list all of the available Posts from the database"""
    permission_classes = (permissions.AllowAny,) #permission classes
    queryset = Post.objects.all()[:10]
    serializer_class = PostSerializer
    '''
    def get_queryset(self):
    	
        if self.request.user.is_authenticated:
            start_date = datetime.utcnow().replace(tzinfo=pytz.utc)
            end_date = start_date - timedelta(days=7)
            queryset = Post.objects.all().order_by('latest_change_date')[:10]
            return queryset
        else:
            pass
    '''




class ListCreatePostAPIView(ListCreateAPIView):
    """This endpoint allows for creation of a Post"""
    permission_classes = (permissions.AllowAny,)#permission classes
    queryset = Post.objects.all()[:10]
    posts = Post.objects.all()
    serializer_class = PostSerializer

    



'''
OPEN_AI_API_KEY = settings.OPEN_AI_API_KEY
from openai import OpenAI
import json
from django.http import JsonResponse

def barcode_ai(request, numbers):
	client = OpenAI(api_key=OPEN_AI_API_KEY)
	page_views, created = Pageviews.objects.get_or_create(page="barcode_ai")
	page_views.views += 1
	page_views.save()

	translation = page_views.translation

	x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
	if x_forwarded_for:
		x_forwarded_for = x_forwarded_for.split(',')[0]
	ip = request.META.get('REMOTE_ADDR')
	ip_addy, created = IpAddress.objects.get_or_create(ip_address=ip)
	page_views.ip_addresses.add(ip_addy)

	if request.user.is_authenticated:
		loggedinuser = User.objects.get(username=request.user.username)
		loggedinanon = Anon.objects.get(username=loggedinuser)
		loggedinauthor = Author.objects.get(username=request.user.username)
		if loggedinanon.false_wallet < 10:
			return JsonResponse("Buy more credits.", safe=False)
		else:
			loggedinanon.false_wallet -= 10
		previous_view = UserViews.objects.filter(anon=loggedinanon).order_by('-view_date').first()
		pages_view = UserViews.objects.create(page_view="barcode_ai", anon=loggedinanon, ip_address=ip, httpxforwardfor=x_forwarded_for)
		page_views.user_views.add(pages_view)
		if previous_view:
			pages_view.previous_view_id = previous_view.id
			pages_view.previous_page = previous_view.page_view
			pages_view.previous_view_date = previous_view.view_date
			pages_view.previous_view_time_between_pages = datetime.datetime.now(timezone.utc) - previous_view.view_date
	else:
		previous_view = UserViews.objects.filter(ip_address=ip).order_by('-view_date').first()
		pages_view = UserViews.objects.create(page_view="barcode_ai", ip_address=ip, httpxforwardfor=x_forwarded_for)
		page_views.user_views.add(pages_view)
		if previous_view:
			pages_view.previous_view_id = previous_view.id
			pages_view.previous_page = previous_view.page_view
			pages_view.previous_view_date = previous_view.view_date
			pages_view.previous_view_time_between_pages = datetime.datetime.now(timezone.utc) - previous_view.view_date
		if not created:
			return JsonResponse("Too many barcodes scanned, create an account to buy credits. Costs 1 cent per barcode", safe=False)

		
	chat_completion = client.chat.completions.create(messages=[{"role": "user","content": "I have the following content about a given numerological number: "+ numbers + "Write me a single paragraph that fits this number. "}],model="gpt-3.5-turbo",)
	return JsonResponse(chat_completion.choices[0].message.content, safe=False)

'''


class UpdatePostAPIView(UpdateAPIView):
    """This endpoint allows for updating a specific Post by passing in the id of the Post to update"""
    permission_classes = (IsAuthenticated,)#permission classes
    queryset = Post.objects.all()[:10]
    serializer_class = PostSerializer


class DeletePostAPIView(DestroyAPIView):
    """This endpoint allows for deletion of a specific Post from the database"""
    permission_classes = (IsAuthenticated,)#permission classes
    queryset = Post.objects.all()[:10]
    serializer_class = PostSerializer



class AuthorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]


    queryset = Author.objects.all()[:100]
    serializer_class = AuthorSerializer

    def list(self, request):
        queryset = Author.objects.all()
        serializer = AuthorSerializer(queryset, context={'request': request}, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Author.objects.all()
        author = get_object_or_404(queryset, pk=pk)
        serializer = AuthorSerializer(author, context={'request': request})
        return Response(serializer.data)

from rest_framework.decorators import action


def robots_txt(request):
    lines = [
        "User-Agent: *",
        "Allow: *"
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")



class PostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    #authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]



    permission_classes = [permissions.AllowAny, ]
    queryset = Post.objects.all()[:10]
    serializer_class = PostSerializer

    def list(self, request):
        queryset = Post.objects.all()
        serializer = PostSerializer(queryset, context={'request': request}, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Post.objects.all()
        post = get_object_or_404(queryset, pk=pk)
        serializer = PostSerializer(post, context={'request': request}, many=True)
        return Response(serializer.data)



import re

@login_required
def tob_email(request, token_id, count=0):
		count = int(count)
		if count > 25:
			mcount = count - 25
		else:
			mcount = 0
		count100 = count + 25
		if (token_id == "3456789") and (request.user.username == "test"):
			


			valid_email_users = []

			for user in User.objects.all().order_by('email'):
				if re.match(r"[^@]+@[^@]+\.[^@]+", user.email):
					if len(valid_email_users) < 2000:
						valid_email_users.append({'email': user.email, 'username': user.username, 'id': user.id})

			all_anons = valid_email_users[count:count100]
			the_response = render(request, 'tob_view_emails.html', {"all_anons": all_anons, "count": count, "mcount": mcount, "count100": count100, })
			the_response.set_cookie('current', 'tob_email')
			the_response.set_cookie('count', count)
			return the_response
		return base_redirect(request, 0)


def roadmap(request):

	return render(request, 'roadmap.html', {})


# which is true comment, or the source comment.
def delete_own_comment(request, comment_id):
	user_themself = User.objects.get(username=request.user.username)
	user_anon = Anon.objects.get(username=user_themself)
	com = int(comment_id)
	if request.user.is_authenticated:
		loggedinuser = User.objects.get(username=request.user.username)
		loggedinanon = Anon.objects.get(username=loggedinuser)
		loggedinauthor = Author.objects.get(username=request.user.username)

		
		if loggedinanon.username.username == user_anon.username.username:
			if Comment.objects.filter(author=loggedinauthor, id=com):
				users_com = Comment.objects.filter(author=loggedinauthor, id=com).first()
				users_com.delete()

				
	return base_redirect(request, 0)





def delete_own_post(request, user, post_id):
	user_themself = User.objects.get(username=user)
	user_anon = Anon.objects.get(username=user_themself)
	users_post = Post.objects.get(id=int(post))

	if request.user.is_authenticated:
		loggedinuser = User.objects.get(username=request.user.username)
		loggedinanon = Anon.objects.get(username=loggedinuser)
		loggedinauthor = Author.objects.get(username=request.user.username)

		if loggedinanon.username.username == user_anon.username.username:
			if users_post:
				users_post.delete()
				if loggedinanon.sum_posts:
					loggedinanon.sum_posts -= 1


	return redirect('Bable:tob_user_view_count', user=user, count=0)


def base_redirect(request, error):
	if request.COOKIES['current'] == ('tob_view_users' or 'tower_of_bable') :
		response = redirect("Bable:"+request.COOKIES['current'])
		response.set_cookie('error', error)
		return response
	elif request.COOKIES['current'] == ('tower_of_bable_count' or 'tob_view_users'):
		response = redirect("Bable:"+request.COOKIES['current'], count=request.COOKIES['count'])
		response.set_cookie('error', error)
		return response
	elif request.COOKIES['current'] == ('tob_user_view_count' or 'tob_users_posts'):
		response = redirect("Bable:"+request.COOKIES['current'], user=request.COOKIES['viewing_user'], count=request.COOKIES['count'])
		response.set_cookie('error', error)
		return response
	elif request.COOKIES['current'] == ('tob_users_post'):
		response = redirect("Bable:"+request.COOKIES['current'], user=request.COOKIES['viewing_user'], post=request.COOKIES['post'], count=request.COOKIES['count'])
		response.set_cookie('error', error)
		return response
	elif request.COOKIES['current'] == ('tob_users_posts_comment'):
		response = redirect("Bable:"+request.COOKIES['current'], user=request.COOKIES['viewing_user'], post=request.COOKIES['post'], comment=request.COOKIES['comment'])
		response.set_cookie('error', error)
		return response
	return redirect('Bable:tower_of_bable')
'''
def sign_wallet(request):
	data = requests.get("http://"+request.META['HTTP_HOST']+"/metamask/"+request.user.username)
	print(data)
	return redirect('Bable:tower_of_bable')
'''

# Redirects to index
def logout_user(request):
	user = request.user
	logout(request)
	return redirect('Bable:tower_of_bable')

def login_view(request):
	loginform = AuthenticationForm(data=request.POST)
	if loginform.is_valid():
		user = loginform.get_user()
		login(request, user)
		Author.objects.get_or_create(username=user.username)
		Anon.objects.get_or_create(username=user)
		#requests.post("http://"+request.META['HTTP_HOST']+"/metamask/", data={'user': {'username': user.username}, 'public_address': user.username})
	

	### Input redirect to previous page.

	return redirect('Bable:tower_of_bable')

from django.contrib.auth import authenticate

# Needs to be AJAX with Rails-style Flash Messages
def register_view(request):
	loginform = AuthenticationForm()
	login_error = "Try getting it right."
	register_error = "Don't fuck it up."
	registerform = UserCreationForm(request.POST)
	
		
	

	if registerform.is_valid():
		new_user = registerform.save()
		register_error = "Register Successful."
		#must log in after
		user = authenticate(request, username=new_user.username, password=registerform.cleaned_data['password1'])
		if user is not None:
			login(request, user)
			anon = Anon.objects.create(username=User.objects.get(username=new_user.username))
			anon.save()
			Author.objects.create(username=new_user.username)
			# Send email.
			# Record IP, record username, record email, record time.
		else:
			login_error = "Not a known Combo, try using a PS4 controller."
	else:
		register_error = "Couldn't register that."
	
	count = 0
	count100 = 100
	mcount = 0
	page_views, created = Pageviews.objects.get_or_create(page="register_view")
	page_views.views += 1
	page_views.save()
	total = 0

	base_product, created = Price.objects.get_or_create(id=1)
	if created:
		base_product.name = "Donate - Predictionary.us"
		base_product.stripe_price_id = "price_1Nf8jMIDEcA7LIBjpnt385yZ"
		base_product.anon_user_id = 1
		base_product.stripe_product_id = "prod_OS2pk9gZWam5Ye"
		base_product.price = 500
		base_product.save()
		
	for page in Pageviews.objects.all():
		total += page.views

	posts_by_viewcount = Post.objects.order_by('-viewcount')[0:25]
	the_response = render(request, 'tower_of_bable.html', {"basic_price": base_product, "viewsponsor": viewsponsor, "register_error":register_error, "login_error":login_error, "total": total, "count": count, "mcount": mcount, "count100": count100, "posts": posts_by_viewcount, 'loginform': loginform, 'registerform': registerform, })
	
	the_response.set_cookie('current', 'tower_of_bable')
	return base_redirect(request, 0)

def owner(request):
	#recently_modified_post = Post.objects.order_by('-latest_change_date')[:100]
	registerform = UserCreationForm()
	
		
	
	loginform = AuthenticationForm()
	
	dic_form = DictionaryForm()
	post_form = PostForm(request)
	space_form = SpaceForm(request)
	task_form = TaskForm()
	word_form = WordForm(request)

	if request.user.is_authenticated:
		loggedinanon = Anon.objects.get(username=User.ojects.get(username=request.user.username))

		apply_votestyle_form = ApplyVotestyleForm(request)
		create_votes_form = CreateVotesForm(request)
		exclude_votes_form = ExcludeVotesForm(request)
		apply_dic_form = ApplyDictionaryForm(request)
		exclude_dic_form = ExcludeDictionaryAuthorForm()
		return render(request, 'jackdonmclovin.html', {"loggedinanon": loggedinanon, 'loginform': loginform, 'registerform': registerform,  'registerterms': registerterms, 'word_form': word_form, 'dic_form':dic_form, 'space_form': space_form, "post_form": post_form, 'task_form': task_form})

	return render(request, 'jackdonmclovin.html', {'loginform': loginform, 'registerform': registerform,  'registerterms': registerterms, 'word_form': word_form, 'dic_form':dic_form, 'space_form': space_form, "post_form": post_form, 'task_form': task_form})





def feedback(request):
	# https://stackoverflow.com/questions/31324005/django-1-8-sending-mail-using-gmail-smtp
	# email = EmailMessage('title', 'body', from_email=[], to=[jackdonmclovin@gmail.com])
	# email.send()
	#recently_modified_post = Post.objects.order_by('-latest_change_date')[:100]
	registerform = UserCreationForm()
	
		
	
	loginform = AuthenticationForm()
	
	
	contact_form = ContactForm()

	if request.user.is_authenticated:
		loggedinanon = Anon.objects.get(username=User.objects.get(username=request.user.username))
		post_form = PostForm(request)
		return render(request, 'feedback.html', {"loggedinanon": loggedinanon, 'contact_form':contact_form, 'loginform': loginform, 'registerform': registerform, 'word_form': word_form, 'dic_form':dic_form, 'space_form': space_form, "post_form": post_form, 'task_form': task_form})

	return render(request, 'feedback.html', {'contact_form':contact_form, 'loginform': loginform, 'registerform': registerform})


def create_feedback(request):
	contactform = ContactForm(request.POST)
	if contactform.is_valid():
		from_email = contactform.cleaned_data['from_email']
		title = contactform.cleaned_data['title']
		message = contactform.cleaned_data['message']
		
		# uncomment if interested in the actual smtp conversation
		# s.set_debuglevel(1)
		# do the smtp auth; sends ehlo if it hasn't been sent already
		
		email = EmailMessage(title+' from: '+from_email, message + "BablyonPolice.com", to=['jackdonmclovin@gmail.com'])
		email.send()
		return redirect('Bable:thanks')
	registerform = UserCreationForm()
	
		
	
	loginform = AuthenticationForm()

	if request.user.is_authenticated:
		post_form = PostForm()
		
		return render(request, 'feedback.html', {'loginform': loginform, 'registerform': registerform, "post_form": post_form,})
	return render(request, 'feedback.html', {'loginform': loginform, 'registerform': registerform})


def thanks(request):
	registerform = UserCreationForm()
	
		
	
	loginform = AuthenticationForm()
	
	
	if request.user.is_authenticated:
		loggedinanon = Anon.objects.get(username=User.objects.get(username=request.user.username))


		post_form = PostForm(request)
		return render(request, 'thanks.html', {"loggedinanon": loggedinanon, 'loginform': loginform, 'registerform': registerform,  'registerterms': registerterms, "post_form": post_form, })

	return render(request, 'thanks.html', {'loginform': loginform, 'registerform': registerform,  'registerterms': registerterms, "post_form": post_form, })


def about(request):
	#recently_modified_post = Post.objects.order_by('-latest_change_date')[:100]
	registerform = UserCreationForm()
	
		
	
	loginform = AuthenticationForm()
	
	

	if request.user.is_authenticated:
		loggedinanon = Anon.objects.get(username=User.objects.get(username=request.user.username))

		post_form = PostForm(request)
		return render(request, 'about.html', {"loggedinanon": loggedinanon, 'loginform': loginform, 'registerform': registerform, "post_form": post_form, })


	return render(request, 'about.html', {'loginform': loginform, 'registerform': registerform})


def management(request):
	#recently_modified_post = Post.objects.order_by('-latest_change_date')[:100]
	registerform = UserCreationForm()
	
		
	
	loginform = AuthenticationForm()
	
	

	if request.user.is_authenticated:
		loggedinanon = Anon.objects.get(username=User.objects.get(username=request.user.username))

		post_form = PostForm(request)
		return render(request, 'management.html', {"loggedinanon": loggedinanon, 'loginform': loginform, 'registerform': registerform, "post_form": post_form, })


	return render(request, 'management.html', {'loginform': loginform, 'registerform': registerform})




@login_required
def create_post(request):
	loggedinanon = Anon.objects.get(username=request.user)
	loggedinauthor = Author.objects.get(username=request.user.username)
	post_form = PostForm(request, data=request.POST)
	if post_form.is_valid():
		if Post.objects.filter(spaces__the_space_itself__the_word_itself=[(e,e) for e in post_form.cleaned_data['spaces']], author=loggedinauthor, title=post_form.cleaned_data['title'], dictionaries__the_dictionary_itself=[(e, e) for e in post_form.cleaned_data['dictionaries']]).count():
			return base_redirect(request, 'duplicate post')
		else:
			new_post = Post.objects.create(author=loggedinauthor, title=post_form.cleaned_data['title'], body=post_form.cleaned_data['body'])
			pre_body = post_form.cleaned_data['body']
			exclude = ''
			new_post.save()
			loggedinanon.posts.add(new_post)
			loggedinanon.sum_posts += 1
			loggedinanon.save()
			return redirect('Bable:tob_users_post', user=request.user.username, post=new_post.id, count=0)
	else:
		return HttpResponse(post_form.errors)
	return redirect('Bable:tob_users_posts', user=request.user.username, count=0)


@login_required
def edit_post(request, post_id):
	loggedinanon = Anon.objects.get(username=request.user)
	loggedinauthor = Author.objects.get(username=request.user.username)
	post_form = PostForm(request, data=request.POST)
	new_post = Post.objects.get(id=post_id)
	if new_post.author.username == loggedinauthor.username:
		if post_form.is_valid():
			pre_body = post_form.cleaned_data['body']
			new_post.title = post_form.cleaned_data['title']
			new_post.body = pre_body
			exclude = ''
			new_post.save()
			loggedinanon.save()
			return redirect('Bable:tob_users_post', user=request.user.username, post=new_post.id, count=0)
	return redirect('Bable:tob_users_posts', user=request.user.username, count=0)




@login_required
def create_comment(request, source_type, source_id, comment_id):
	loggedinanon = Anon.objects.get(username=request.user)
	loggedinauthor = Author.objects.get(username=request.user.username)
	commentform = Comment_SourceForm(request, data=request.POST)
	source = int(source)
	com = int(com)
	new_com = 0
	if source_type == 'post':
		commentform = CommentForm(request, data=request.POST)
		if commentform.is_valid():
			if com == 0:
				if commentform.cleaned_data['dictionaries'] == 0:
					new_com = Comment.objects.create(body=commentform.cleaned_data['body'], author=loggedinauthor)
				else:
					new_com = Comment.objects.create(body=commentform.cleaned_data['body'], author=loggedinauthor)
					for dic in commentform.cleaned_data['dictionaries']:
						new_com.dictionaries.add(loggedinanon.purchased_dictionaries.get(the_dictionary_itself=dic))
					new_com.sum_dictionaries = new_com.dictionaries.count()
					new_com.save()
			else:
				if commentform.cleaned_data['dictionaries'] == 0:
					parent_comment = Comment.objects.get(id=com)
					parent_comment.children_count += 1
					parent_comment.save()
					new_com = Comment.objects.create(body=commentform.cleaned_data['body'], author=loggedinauthor, parent=Comment.objects.get(id=com))
				else:
					parent_comment = Comment.objects.get(id=com)
					parent_comment.children_count += 1
					parent_comment.save()
					new_com = Comment.objects.create(body=commentform.cleaned_data['body'], author=loggedinauthor, parent=Comment.objects.get(id=com))
					for dic in commentform.cleaned_data['dictionaries']:
						new_com.dictionaries.add(loggedinanon.purchased_dictionaries.get(the_dictionary_itself=dic))
					new_com.sum_dictionaries = new_com.dictionaries.count()
					new_com.save()
			the_post = Post.objects.get(id=source)
			the_post.comments.add(new_com)
			the_post.sum_comments = the_post.comments.count()
			the_post.under_talked = float(the_post.votes_uniques) / float(the_post.sum_comments)
			the_post.save()

					

	if commentform.is_valid():
		if com == 0:
			if com:
				parent_comment = Comment.objects.get(id=com)
				parent_comment.children_count += 1
				parent_comment.save()
				new_com = Comment_Source.objects.create(body=commentform.cleaned_data['body'], author=loggedinauthor, original=com)
			else:
				new_com = Comment_Source.objects.create(body=commentform.cleaned_data['body'], author=loggedinauthor)
		else:
			if com:
				parent_comment = Comment.objects.get(id=com)
				parent_comment.children_count += 1
				parent_comment.save()
				new_com = Comment_Source.objects.create(body=commentform.cleaned_data['body'], author=loggedinauthor, original=com)
			else:
				new_com = Comment_Source.objects.create(body=commentform.cleaned_data['body'], author=loggedinauthor, parent=Comment_Source.objects.get(id=com))
			
		
	else:
		print(commentform.errors)
	
	return base_redirect(request, 0)



from coinbase_commerce.client import Client


def roadmap(request):
	return render(request, 'roadmap.html')



import validators
from django.utils import dateformat, timezone
def search(request, search_id, count):
	#recently_modified_post = Post.objects.order_by('-latest_change_date')[:100]
	registerform = UserCreationForm()
	
		
	
	loginform = AuthenticationForm()
	count = int(count)
	count100 = count+25
	mcount = 0
	if count > 25:
		mcount = count - 25
	if ('q' in request.GET) and request.GET['q'].strip():
		query_string = request.GET['q']
		if validators.url(query_string):
			if request.user.is_authenticated:
				loggedinuser = User.objects.get(username=request.user.username)
				loggedinanon = Anon.objects.get(username=loggedinuser)
				#searcher = SearchURL.objects.create(name='/u/'+request.user.username+'/'+dateformat.format(timezone.now(), 'Y-m-d H:i:s'), url=query_string, author=Author.objects.get(username=request.user.username))
				loggedinanon.search_urls.add(searcher)
				return redirect('Bable:annotate_url', search_url_id=searcher.id)

	page_views, created = Pageviews.objects.get_or_create(page="search")
	page_views.views += 1
	page_views.save()

	x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
	if x_forwarded_for:
		x_forwarded_for = x_forwarded_for.split(',')[0]
	ip = request.META.get('REMOTE_ADDR')

	total = 0
	for page in Pageviews.objects.all():
		total += page.views

	if request.user.is_authenticated:
		loggedinuser = User.objects.get(username=request.user.username)
		loggedinanon = Anon.objects.get(username=loggedinuser)
		loggedinauthor = Author.objects.get(username=request.user.username)
		post_form = PostForm(request)
		
		previous_view = UserViews.objects.filter(anon=loggedinanon).order_by('-view_date').first()
		pages_view = UserViews.objects.create(page_view="search__"+query_string+"__"+str(count), anon=loggedinanon, ip_address=ip, httpxforwardfor=x_forwarded_for)
		page_views.user_views.add(pages_view)
		if previous_view:
			pages_view.previous_view_id = previous_view.id
			pages_view.previous_page = previous_view.page_view
			pages_view.previous_view_date = previous_view.view_date
			pages_view.previous_view_time_between_pages = datetime.datetime.now(timezone.utc) - previous_view.view_date

		search_post = Post.objects.filter(title__icontains=query_string).filter(Q(public=True)|Q(allowed_to_view_authors=loggedinauthor)).order_by('-latest_change_date')[count:count100]
		search_space = Space.objects.filter(the_space_itself__the_word_itself__icontains=query_string).filter(Q(public=True)|Q(approved_voters=loggedinauthor)).order_by('-latest_change_date')[count:count100]
		search_words = Word.objects.filter(the_word_itself__icontains=query_string).order_by('-latest_change_date')[count:count100]
		search_dics = Dictionary.objects.filter(the_dictionary_itself__icontains=query_string).filter(Q(public=True)|Q(allowed_to_view_authors=loggedinauthor)).order_by('-latest_change_date')[count:count100]
		posts_by_viewcount = search_post
		
		the_response = render(request, 'tob_search.html', {"query_string": query_string, "loggedinanon": loggedinanon, "mcount": mcount, "count100": count100, "posts": posts_by_viewcount, "spaces": search_space, "words": search_words, "dics": search_dics, 'loginform': loginform, 'registerform': registerform,  'word_form': word_form, 'dic_form':dic_form, 'space_form': space_form, "post_form": post_form, 'task_form': task_form, 
			"apply_votestyle_form": apply_votestyle_form, "create_votes_form": create_votes_form, "exclude_votes_form": exclude_votes_form, "apply_dic_form": apply_dic_form, "exclude_dic_form": exclude_dic_form})
	else:
		previous_view = UserViews.objects.filter(ip_address=ip).order_by('-view_date').first()
		pages_view = UserViews.objects.create(page_view="search__"+query_string+"__"+str(count), ip_address=ip, httpxforwardfor=x_forwarded_for)
		page_views.user_views.add(pages_view)
		if previous_view:
			pages_view.previous_view_id = previous_view.id
			pages_view.previous_page = previous_view.page_view
			pages_view.previous_view_date = previous_view.view_date
			pages_view.previous_view_time_between_pages = datetime.datetime.now(timezone.utc) - previous_view.view_date
		
		search_post = Post.objects.filter(title__icontains=query_string).filter(public=True)[count:count100]
		posts_by_viewcount = search_post
		the_response = render(request, 'tob_search.html', {"query_string": query_string, "mcount": mcount, "count100": count100, "posts": posts_by_viewcount, 'loginform': loginform, 'registerform': registerform, })
	
	the_response.set_cookie('current', 'search')
	return the_response


from django.views.generic import TemplateView


import discord
import requests





def tower_of_bable(request):
	#recently_modified_post = Post.objects.order_by('-latest_change_date')[:100]
	registerform = UserCreationForm()
	loginform = AuthenticationForm()

	
	
	lower = 0
	count100 = 25
	mcount = 0

	
	test, x = Author.objects.get_or_create(username='test')
	
	if Anon.objects.all().count():
		user, x = User.objects.get_or_create(username="test")
		user.set_password("thattickles")
		anon, x = Anon.objects.get_or_create(username=user)
		author, x = Author.objects.get_or_create(username="test")


	page_views, created = Pageviews.objects.get_or_create(page="tower_of_bable")
	page_views.views += 1
	page_views.save()

	translation = page_views.translation

	x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
	if x_forwarded_for:
		x_forwarded_for = x_forwarded_for.split(',')[0]
	ip = request.META.get('REMOTE_ADDR')

	total = 0
	for page in Pageviews.objects.all():
		total += page.views

	if request.user.is_authenticated:
		loggedinuser = User.objects.get(username=request.user.username)
		loggedinanon = Anon.objects.get(username=loggedinuser)
		loggedinauthor = Author.objects.get(username=request.user.username)
		previous_view = UserViews.objects.filter(anon=loggedinanon).order_by('-view_date').first()
		pages_view = UserViews.objects.create(page_view="tower_of_bable", anon=loggedinanon, ip_address=ip, httpxforwardfor=x_forwarded_for)
		page_views.user_views.add(pages_view)
		if previous_view:
			pages_view.previous_view_id = previous_view.id
			pages_view.previous_page = previous_view.page_view
			pages_view.previous_view_date = previous_view.view_date
			pages_view.previous_view_time_between_pages = datetime.datetime.now(timezone.utc) - previous_view.view_date
		post_form = PostForm(request)
		startdate = datetime.datetime.now() - timedelta(minutes=int(loggedinanon.post_sort_from_date_char.split(',')[0]), hours=int(loggedinanon.post_sort_from_date_char.split(',')[1]), days=int(loggedinanon.post_sort_from_date_char.split(',')[2]), weeks=int(loggedinanon.post_sort_from_date_char.split(',')[3]))
		enddate = startdate - timedelta(minutes=int(loggedinanon.post_sort_depth_char.split(',')[0]), hours=int(loggedinanon.post_sort_depth_char.split(',')[1]), days=int(loggedinanon.post_sort_depth_char.split(',')[2]), weeks=int(loggedinanon.post_sort_depth_char.split(',')[3]))
		posts_by_viewcount = Post.objects.filter(latest_change_date__range=[enddate, startdate]).order_by(loggedinanon.post_sort_char)[:25]
		file_form = FileForm()
		post_sort_form = PostSortForm(request)
		post_filter_depth_form = PostFilterDepthForm(request)
		post_filter_from_date_form = PostFilterFromDateForm(request)
		
		posts_values = list(posts_by_viewcount.values('img', 'author__username', 'id', 'title', 'body', 'viewcount', 'pub_date'))
		postscount = 25
		posts_by_viewcount = posts_values

		sms_verification_form = SMSVerificationForm(request)
		email_verification_form = EmailVerificationForm(request)
		change_email_form = ChangeEmailForm(request)
		change_phone_form = ChangePhoneForm(request)

		
		

		
		the_response = render(request, 'tower_of_bable.html', { "sms_verification_form": sms_verification_form, "email_verification_form": email_verification_form, "change_email_form": change_email_form, "change_phone_form": change_phone_form,  "post_filter_depth_form": post_filter_depth_form, "post_filter_from_date_form": post_filter_from_date_form, "post_sort_form": post_sort_form, "postscount": postscount, "ip": ip, "x_forwarded_for": x_forwarded_for, "file_form": file_form, "total": total, "count": lower, "mcount": mcount, "count100": count100, "loggedinanon": loggedinanon, "posts": posts_by_viewcount, 'loginform': loginform, 'registerform': registerform, "post_form": post_form, })
	else:
		the_response = render(request, 'tower_of_bable.html', {"ip": ip, "x_forwarded_for": x_forwarded_for,  "total": total, "count": lower, "mcount": mcount, "count100": count100, 'loginform': loginform, 'registerform': registerform, })
	
	the_response.set_cookie('current', 'tower_of_bable')
	return the_response




def landingpage(request):
	#recently_modified_post = Post.objects.order_by('-latest_change_date')[:100]
	registerform = UserCreationForm()
	
		
	
	loginform = AuthenticationForm()

	
	count = 0
	count100 = 100
	mcount = 0

	
	
	page_views, created = Pageviews.objects.get_or_create(page="landingpage")
	page_views.views += 1
	page_views.save()

	translation = page_views.translation

	x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
	if x_forwarded_for:
		x_forwarded_for = x_forwarded_for.split(',')[0]
	ip = request.META.get('REMOTE_ADDR')

	total = 0
	for page in Pageviews.objects.all():
		total += page.views

	if request.user.is_authenticated:
		loggedinuser = User.objects.get(username=request.user.username)
		loggedinanon = Anon.objects.get(username=loggedinuser)
		loggedinauthor = Author.objects.get(username=request.user.username)
		previous_view = UserViews.objects.filter(anon=loggedinanon).order_by('-view_date').first()
		pages_view = UserViews.objects.create(page_view="landingpage", anon=loggedinanon, ip_address=ip, httpxforwardfor=x_forwarded_for)
		page_views.user_views.add(pages_view)
		if previous_view:
			pages_view.previous_view_id = previous_view.id
			pages_view.previous_page = previous_view.page_view
			pages_view.previous_view_date = previous_view.view_date
			pages_view.previous_view_time_between_pages = datetime.datetime.now(timezone.utc) - previous_view.view_date
		
		the_response = render(request, 'landingpage.html', { "ip": ip, "x_forwarded_for": x_forwarded_for, "loggedinanon": loggedinanon, 'loginform': loginform, 'registerform': registerform, "post_form": post_form,})
	else: 
		previous_view = UserViews.objects.filter(ip_address=ip).order_by('-view_date').first()
		pages_view = UserViews.objects.create(page_view="landingpage", ip_address=ip, httpxforwardfor=x_forwarded_for)
		page_views.user_views.add(pages_view)
		if previous_view:
			pages_view.previous_view_id = previous_view.id
			pages_view.previous_page = previous_view.page_view
			pages_view.previous_view_date = previous_view.view_date
			pages_view.previous_view_time_between_pages = datetime.datetime.now(timezone.utc) - previous_view.view_date
		begin_verification_form_start = BeginVerificationFormStart()
		begin_verification_form = BeginVerificationForm()
		the_response = render(request, 'landingpage.html', { "ip": ip, "x_forwarded_for": x_forwarded_for, "begin_verification_form_start": begin_verification_form_start, "begin_verification_form": loginform })
	
	the_response.set_cookie('current', 'landingpage')
	return the_response




def change_password(request):
	#recently_modified_post = Post.objects.order_by('-latest_change_date')[:100]
	if request.method == "POST":
		change_password_form = CustomChangePasswordForm(data=request.POST)
		if change_password_form.is_valid():
			change_password_form.save()
			update_session_auth_hash(request, request.user)
	return base_redirect(request, 0)

def change_phone(request):
	#recently_modified_post = Post.objects.order_by('-latest_change_date')[:100]
	if request.method == "POST":
		change_phone_form = ChangePhoneForm(data=request.POST)
		if change_phone_form.is_valid():
			change_phone_form.save()
			
	return base_redirect(request, 0)

def change_email(request):
	#recently_modified_post = Post.objects.order_by('-latest_change_date')[:100]
	if request.method == "POST":
		change_email_form = ChangeEmailForm(data=request.POST)
		if change_email_form.is_valid():
			change_email_form.save()
			
	return base_redirect(request, 0)

def begin_verification(request):
	#recently_modified_post = Post.objects.order_by('-latest_change_date')[:100]
	if request.method == "POST":
		begin_verification_form = BeginVerificationForm(data=request.POST)
		if begin_verification_form.is_valid():
			user = authenticate(request, username=begin_verification_form.instance.username, password=begin_verification_form.cleaned_data['password'])
			update_session_auth_hash(request, user)
		else:
			error_message = ''
			for error in begin_verification_form.errors:
				error_message += error
			
			return HttpResponse("Begin: "+ error_message)

	return base_redirect(request, 0)

def begin_verification_start(request):
	#recently_modified_post = Post.objects.order_by('-latest_change_date')[:100]
	if request.method == "POST":
		begin_verification_form = BeginVerificationFormStart(data=request.POST)
		if begin_verification_form.is_valid():
			user_anon = Anon.objects.get(user_name=begin_verification_form.cleaned_data["user_name"])
			login(request, user_anon.username)
			update_session_auth_hash(request, request.user)

			
	return base_redirect(request, 0)


def email_verification(request):
	#recently_modified_post = Post.objects.order_by('-latest_change_date')[:100]
	if request.method == "POST":
		email_verification_form = EmailVerificationForm(request, data=request.POST)
		if email_verification_form.is_valid():
			email_verification_form.save()
	return base_redirect(request, 0)


def sms_verification(request):
	#recently_modified_post = Post.objects.order_by('-latest_change_date')[:100]
	if request.method == "POST":
		sms_verification_form = SMSVerificationForm(request, data=request.POST)
		if sms_verification_form.is_valid():
			sms_verification_form.save()
	return base_redirect(request, 0)


def tower_of_bable_count(request, count):
	#recently_modified_post = Post.objects.order_by('-latest_change_date')[:100]
	registerform = UserCreationForm()
	change_password_form = CustomChangePasswordForm()
	begin_verification_form = BeginVerificationForm()
	sms_verification_form = SMSVerificationForm()
	email_verification_form = EmailVerificationForm()
	if Anon.objects.all().count():
		user = User.objects.create(username="test")
		user.set_password("thattickles")
		anon = Anon.objects.create(username=user)
		author = Author.objects.create(username="test")
	
	basic_price = Price.objects.filter(name="Donate - Predictionary.us", anon_user_id=1).first()
	if not basic_price.stripe_price_id:
		basic_price.stripe_price_id = "price_1Nf8jMIDEcA7LIBjpnt385yZ"

		basic_price.stripe_product_id = "prod_OS2pk9gZWam5Ye"
		basic_price.price = 500
		basic_price.save()


	count = int(count)
	if not count:
		return redirect('Bable:tower_of_bable')

	page_views, created = Pageviews.objects.get_or_create(page="tower_of_bable_count")
	page_views.views += 1
	page_views.save()

	total = 0
	for page in Pageviews.objects.all():
		total += page.views

	buyadvertisingform = BuyAdvertisingForm()

	x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
	if x_forwarded_for:
		x_forwarded_for = x_forwarded_for.split(',')[0]
	ip = request.META.get('REMOTE_ADDR')

	total = 0
	for page in Pageviews.objects.all():
		total += page.views
	
	
	count100 = count + 25
	mcount = 0
	if count > 25:
		mcount = count - 25
		
	loginform = AuthenticationForm()
	if request.user.is_authenticated:
		loggedinuser = User.objects.get(username=request.user.username)
		loggedinanon = Anon.objects.get(username=loggedinuser)
		loggedinauthor = Author.objects.get(username=request.user.username)
		previous_view = UserViews.objects.filter(anon=loggedinanon).order_by('-view_date').first()
		pages_view = UserViews.objects.create(page_view="tower_of_bable_count__"+str(count), anon=loggedinanon, ip_address=ip, httpxforwardfor=x_forwarded_for)
		page_views.user_views.add(pages_view)
		if previous_view:
			pages_view.previous_view_id = previous_view.id
			pages_view.previous_page = previous_view.page_view
			pages_view.previous_view_date = previous_view.view_date
			pages_view.previous_view_time_between_pages = datetime.datetime.now(timezone.utc) - previous_view.view_date
		startdate = datetime.datetime.now() - timedelta(minutes=int(loggedinanon.post_sort_from_date_char.split(',')[0]), hours=int(loggedinanon.post_sort_from_date_char.split(',')[1]), days=int(loggedinanon.post_sort_from_date_char.split(',')[2]), weeks=int(loggedinanon.post_sort_from_date_char.split(',')[3]))
		enddate = startdate - timedelta(minutes=int(loggedinanon.post_sort_depth_char.split(',')[0]), hours=int(loggedinanon.post_sort_depth_char.split(',')[1]), days=int(loggedinanon.post_sort_depth_char.split(',')[2]), weeks=int(loggedinanon.post_sort_depth_char.split(',')[3]))
		posts_by_viewcount = Post.objects.filter(latest_change_date__range=[enddate, startdate]).order_by(loggedinanon.post_sort_char)[count:count100]
		postscount = posts_by_viewcount.count()

		dic_form = DictionaryForm()
		post_form = PostForm(request)
		space_form = SpaceForm(request)
		task_form = TaskForm()
		word_form = WordForm(request)
		
		apply_votestyle_form = ApplyVotestyleForm(request)
		create_votes_form = CreateVotesForm(request)
		exclude_votes_form = ExcludeVotesForm(request)
		apply_dic_form = ApplyDictionaryForm(request)
		exclude_dic_form = ExcludeDictionaryAuthorForm()

		post_sort_form = PostSortForm(request)
		post_filter_depth_form = PostFilterDepthForm(request)
		post_filter_from_date_form = PostFilterFromDateForm(request)
		
		

		the_response = render(request, 'tower_of_bable.html', {"change_password_form": change_password_form, "basic_price": basic_price, "post_sort_form": post_sort_form, "postscount": postscount, "buyadvertisingform": buyadvertisingform, "total": total, "count": count, "mcount": mcount, "count100": count100, "posts": posts_by_viewcount, "loggedinanon": loggedinanon, 'loginform': loginform, 'registerform': registerform,  'postform': post_form, 'spaceform': space_form, "post_form": post_form, 'taskform': task_form, 
			"apply_votestyle_form": apply_votestyle_form, "create_votes_form": create_votes_form, "exclude_votes_form": exclude_votes_form, "apply_dic_form": apply_dic_form, "exclude_dic_form": exclude_dic_form})
	else:
		previous_view = UserViews.objects.filter(ip_address=ip).order_by('-view_date').first()
		pages_view = UserViews.objects.create(page_view="tower_of_bable_count__"+str(count), ip_address=ip, httpxforwardfor=x_forwarded_for)
		page_views.user_views.add(pages_view)
		if previous_view:
			pages_view.previous_view_id = previous_view.id
			pages_view.previous_page = previous_view.page_view
			pages_view.previous_view_date = previous_view.view_date
			pages_view.previous_view_time_between_pages = datetime.datetime.now(timezone.utc) - previous_view.view_date
		
		posts_by_viewcount = Post.objects.order_by('viewcount')[count:count100]
		postscount = posts_by_viewcount.count()
		the_response = render(request, 'tower_of_bable.html', {"basic_price": basic_price, "postscount": postscount, "buyadvertisingform": buyadvertisingform, "total": total, "count": count, "mcount": mcount, "count100": count100, "posts": posts_by_viewcount, 'loginform': loginform, 'registerform': registerform, })
	the_response.set_cookie('current', 'tower_of_bable_count')
	the_response.set_cookie('count', count)
	return the_response


#Import Geocoder 
import geocoder

#Assign IP address to a variable
ip = geocoder.ip("161.185.160.93")

#Obtain the city
print(ip.city)

#Obtain the coordinates: 
print(ip.latlng)


import matplotlib.pyplot as plt
import numpy as np

import plotly as py
from plotly.offline import iplot
import plotly.graph_objs as go
import plotly.io as pio
pio.renderers.default = 'iframe'
from matplotlib.figure import Figure

@login_required
def heatmap(request, keywords):
	x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
	if x_forwarded_for:
		x_forwarded_for = x_forwarded_for.split(',')[0]
	ip = request.META.get('REMOTE_ADDR')

	total = 0
	for page in Pageviews.objects.all():
		total += page.views

	loggedinauthor = Author.objects.get(username=request.user.username)
	most_recent_post = Anon.objects.get(username=request.user).posts.order_by('-creation_date').first()
	if most_recent_post:
		stat_signature = most_recent_post.zipfslawstatsignature.zipfs_law_signature.filter(keywords=keywords).first()
	many_stats = ZipfsLawStatSignature.objects.filter(body=keywords, year=timezone.now().date().year, month=timezone.now().date().month, day=timezone.now().date().day-1)


	a = list(many_stats.values('lat', 'lng', 'one_sum'))
	#b = list(many_stats.values('lng', 'one_sum'))
	#ax = plt.imshow(a, cmap='hot', interpolation='nearest')
	fig = go.Figure(a)
	#ax = fig.add_subplot(1,1,1)
	#ax.plot(a, b, '-')
	#fig.set_xlabel('Lat')
	#fig.set_ylabel('Lng')
	#fig.set_title("One Sum")
	graph_div = plotly.offline.plot(fig, auto_open = False, output_type="div")


	the_response = render(request, "tob_heatmap.html", { "graph_div":graph_div, "ip": ip, "x_forwarded_for": x_forwarded_for})
	the_response.set_cookie('current', 'tob_heatmap')
	the_response.set_cookie('keywords', keywords)
	the_response.set_cookie('count', 0)
	return the_response

@login_required
def tob_post(request, post):
	users_post = Post.objects.get(id=int(post))
	
	posts_comments = users_post.comments.order_by('-viewcount')[:25]
	users_post.viewcount += 1
	if users_post.spaces.count():
		for space in users_post.spaces.all():
			full_space = space.to_full()
			full_space.posts_viewcount += 1
			full_space.save()
	max_sponsor = users_post.max_sponsor()
	users_post.save()
	
	page_views, created = Pageviews.objects.get_or_create(page="tob_post")
	page_views.views += 1
	page_views.save()

	x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
	if x_forwarded_for:
		x_forwarded_for = x_forwarded_for.split(',')[0]
	ip = request.META.get('REMOTE_ADDR')


	registerform = UserCreationForm()
	
		
	
	loginform = AuthenticationForm()
	if request.user.is_authenticated:
		loggedinuser = User.objects.get(username=request.user.username)
		loggedinanon = Anon.objects.get(username=loggedinuser)
		loggedinauthor = Author.objects.get(username=request.user.username)

		previous_view = UserViews.objects.filter(anon=loggedinanon).order_by('-view_date').first()
		pages_view = UserViews.objects.create(page_view="tob_post__"+post, anon=loggedinanon, ip_address=ip, httpxforwardfor=x_forwarded_for)
		page_views.user_views.add(pages_view)
		if previous_view:
			pages_view.previous_view_id = previous_view.id
			pages_view.previous_page = previous_view.page_view
			pages_view.previous_view_date = previous_view.view_date
			pages_view.previous_view_time_between_pages = datetime.datetime.now(timezone.utc) - previous_view.view_date
		

		dic_form = DictionaryForm()
		post_form = PostForm(request)
		space_form = SpaceForm(request)
		task_form = TaskForm()
		word_form = WordForm(request)
	
		apply_votestyle_form = ApplyVotestyleForm(request)
		create_votes_form = CreateVotesForm(request)
		exclude_votes_form = ExcludeVotesForm(request)
		apply_dic_form = ApplyDictionaryForm(request)
		exclude_dic_form = ExcludeDictionaryAuthorForm()

		file_form = FileForm() 
		the_response = render(request, "tob_post.html", {"ip": ip, "x_forwarded_for": x_forwarded_for, "file_form": file_form, "loggedinanon": loggedinanon, "users_post": users_post, "space_form": space_form, "post_form": post_form, "task_form": task_form, "word_form": word_form, "registerform": registerform,  "loginform": loginform, 
			"apply_votestyle_form": apply_votestyle_form, "create_votes_form": create_votes_form, "exclude_votes_form": exclude_votes_form, "apply_dic_form": apply_dic_form, "exclude_dic_form": exclude_dic_form})
	else:
		previous_view = UserViews.objects.filter(ip_address=ip).order_by('-view_date').first()
		pages_view = UserViews.objects.create(page_view="tob_post__"+post, ip_address=ip, httpxforwardfor=x_forwarded_for)
		page_views.user_views.add(pages_view)
		if previous_view:
			pages_view.previous_view_id = previous_view.id
			pages_view.previous_page = previous_view.page_view
			pages_view.previous_view_date = previous_view.view_date
			pages_view.previous_view_time_between_pages = datetime.datetime.now(timezone.utc) - previous_view.view_date
		
		the_response = render(request, "tob_post.html", {"ip": ip, "x_forwarded_for": x_forwarded_for, "users_post": users_post, "registerform": registerform,  "loginform": loginform})
	the_response.set_cookie('current', 'tob_post')
	the_response.set_cookie('post', post)
	the_response.set_cookie('count', 0)
	return the_response



@login_required
def notification_redirect(request, new_notification_id):
	if request.user.is_authenticated:
		loggedinanon = Anon.objects.get(username=request.user)
		notification = loggedinanon.new_notifications.filter(id=int(new_notification_id)).first()
		
		page_views, created = Pageviews.objects.get_or_create(page="notification_redirect")
		page_views.views += 1
		page_views.save()

		x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
		if x_forwarded_for:
			x_forwarded_for = x_forwarded_for.split(',')[0]
		ip = request.META.get('REMOTE_ADDR')

		previous_view = UserViews.objects.filter(anon=loggedinanon).order_by('-view_date').first()
		pages_view = UserViews.objects.create(page_view="notification_redirect__"+str(new_notification_id), anon=loggedinanon, ip_address=ip, httpxforwardfor=x_forwarded_for)
		page_views.user_views.add(pages_view)
		if previous_view:
			pages_view.previous_view_id = previous_view.id
			pages_view.previous_page = previous_view.page_view
			pages_view.previous_view_date = previous_view.view_date
			pages_view.previous_view_time_between_pages = datetime.datetime.now(timezone.utc) - previous_view.view_date
		




		if notification.link:
			return redirect(notification.link)
		return redirect("Bable:"+"notifications_page")
	return base_redirect(request, 0)

@login_required
def notifications_page(request):
	if request.user.is_authenticated:
		loggedinanon = Anon.objects.get(username=request.user)
		
		page_views, created = Pageviews.objects.get_or_create(page="notifications_page")
		page_views.views += 1
		page_views.save()

		x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
		if x_forwarded_for:
			x_forwarded_for = x_forwarded_for.split(',')[0]
		ip = request.META.get('REMOTE_ADDR')

		previous_view = UserViews.objects.filter(anon=loggedinanon).order_by('-view_date').first()
		pages_view = UserViews.objects.create(page_view="notifications_page__"+str(count), anon=loggedinanon, ip_address=ip, httpxforwardfor=x_forwarded_for)
		page_views.user_views.add(pages_view)
		if previous_view:
			pages_view.previous_view_id = previous_view.id
			pages_view.previous_page = previous_view.page_view
			pages_view.previous_view_date = previous_view.view_date
			pages_view.previous_view_time_between_pages = datetime.datetime.now(timezone.utc) - previous_view.view_date
		

		dic_form = DictionaryForm()
		post_form = PostForm(request)
		space_form = SpaceForm(request)
		task_form = TaskForm()
		word_form = WordForm(request)
	
		apply_votestyle_form = ApplyVotestyleForm(request)
		create_votes_form = CreateVotesForm(request)
		exclude_votes_form = ExcludeVotesForm(request)
		apply_dic_form = ApplyDictionaryForm(request)
		exclude_dic_form = ExcludeDictionaryAuthorForm()

	
		file_form = FileForm() 
		the_response = render(request, "notifications_page.html", {"ip": ip, "x_forwarded_for": x_forwarded_for, "file_form": file_form, "loggedinanon": loggedinanon, "space_form": space_form, "post_form": post_form, "task_form": task_form, "word_form": word_form, "registerform": registerform,  "loginform": loginform, 
			"apply_votestyle_form": apply_votestyle_form, "create_votes_form": create_votes_form, "exclude_votes_form": exclude_votes_form, "apply_dic_form": apply_dic_form, "exclude_dic_form": exclude_dic_form})
		the_response.set_cookie('current', 'notifications_page')
		return the_response
	return base_redirect(request, 0)





from django import forms


@login_required
def change_anon_sort_char(request):
	if request.method == "POST":
		anon_sort_form = AnonSortForm(request, data=request.POST)
		if anon_sort_form.is_valid():
			anon_sort_form.save()
	return base_redirect(request, 0)

@login_required
def change_anon_filter_depth(request):
	if request.method == "POST":
		anon_sort_form = AnonFilterDepthForm(request, data=request.POST)
		if anon_sort_form.is_valid():
			anon_sort_form.save()
	return base_redirect(request, 0)

@login_required
def change_anon_filter_from_date(request):
	if request.method == "POST":
		anon_sort_form = AnonFilterFromDateForm(request, data=request.POST)
		if anon_sort_form.is_valid():
			anon_sort_form.save()
	return base_redirect(request, 0)



@login_required
def change_post_sort_char(request):
	if request.method == "POST":
		post_sort_form = PostSortForm(request, data=request.POST)
		if post_sort_form.is_valid():
			post_sort_form.save()
	return base_redirect(request, 0)

@login_required
def change_post_filter_depth(request):
	if request.method == "POST":
		post_filter_depth_form = PostFilterDepthForm(request, data=request.POST)
		if post_filter_depth_form.is_valid():
			post_filter_depth_form.save()
	return base_redirect(request, 0)

@login_required
def change_post_filter_from_date(request):
	if request.method == "POST":
		post_filter_from_date_form = PostFilterFromDateForm(request, data=request.POST)
		if post_filter_from_date_form.is_valid():
			post_filter_from_date_form.save()
	return base_redirect(request, 0)


def tob_view_users(request):

	user_anons = Anon.objects.order_by('-latest_change_date')[:25]
	count = 0 
	mcount = 0
	count100 = 25
	registerform = UserCreationForm()
	
	user_anons_count = Anon.objects.count()
	page_views, created = Pageviews.objects.get_or_create(page="tob_view_users")
	page_views.views += 1
	page_views.save()

	x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
	if x_forwarded_for:
		x_forwarded_for = x_forwarded_for.split(',')[0]
	ip = request.META.get('REMOTE_ADDR')

	total = 0
	for page in Pageviews.objects.all():
		total += page.views	
	
	
	loginform = AuthenticationForm()
	if request.user.is_authenticated:
		loggedinuser = User.objects.get(username=request.user.username)
		loggedinanon = Anon.objects.get(username=loggedinuser)
		loggedinauthor = Author.objects.get(username=request.user.username)

		previous_view = UserViews.objects.filter(anon=loggedinanon).order_by('-view_date').first()
		pages_view = UserViews.objects.create(page_view="tob_view_users", anon=loggedinanon, ip_address=ip, httpxforwardfor=x_forwarded_for)
		page_views.user_views.add(pages_view)
		if previous_view:
			pages_view.previous_view_id = previous_view.id
			pages_view.previous_page = previous_view.page_view
			pages_view.previous_view_date = previous_view.view_date
			pages_view.previous_view_time_between_pages = datetime.datetime.now(timezone.utc) - previous_view.view_date
		

		user_anons = Anon.objects.order_by(loggedinanon.anon_sort_char)[0:25]

		post_form = PostForm(request)
		anon_sort_form = AnonSortForm(request)
	
		the_response = render(request, "tob_view_users.html", {"user_anons_count": user_anons_count, "anon_sort_form": anon_sort_form, "count": count, "mcount": mcount, "count100": count100, "loggedinanon": loggedinanon, "user_anons": user_anons, "post_form": post_form, "registerform": registerform,  "loginform": loginform, })
	else:
		previous_view = UserViews.objects.filter(ip_address=ip).order_by('-view_date').first()
		pages_view = UserViews.objects.create(page_view="tob_view_users", ip_address=ip, httpxforwardfor=x_forwarded_for)
		page_views.user_views.add(pages_view)
		if previous_view:
			pages_view.previous_view_id = previous_view.id
			pages_view.previous_page = previous_view.page_view
			pages_view.previous_view_date = previous_view.view_date
			pages_view.previous_view_time_between_pages = datetime.datetime.now(timezone.utc) - previous_view.view_date
		
		the_response = render(request, "tob_view_users.html", {"user_anons_count": user_anons_count, "count": count, "mcount": mcount, "count100": count100, "user_anons": user_anons, "registerform": registerform,  "loginform": loginform})
	the_response.set_cookie('current', 'tob_view_users')
	the_response.set_cookie('count', 0)
	return the_response

def tob_view_users_count(request, count):
	count = int(count)
	count100 = count + 25
	user_anons = Anon.objects.order_by('-latest_change_date')[count:count100]
	#if request.user.is_authenticated:
	if count > 25:
		mcount = count - 25
	else:
		mcount = 0
	#	if user_anons is not None:
	registerform = UserCreationForm()
	
	user_anons_count = Anon.objects.count()
	page_views, created = Pageviews.objects.get_or_create(page="tob_view_users_count")
	page_views.views += 1
	page_views.save()

	x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
	if x_forwarded_for:
		x_forwarded_for = x_forwarded_for.split(',')[0]
	ip = request.META.get('REMOTE_ADDR')

	total = 0
	for page in Pageviews.objects.all():
		total += page.views	
	
	
	loginform = AuthenticationForm()
	if request.user.is_authenticated:
		loggedinuser = User.objects.get(username=request.user.username)
		loggedinanon = Anon.objects.get(username=loggedinuser)
		loggedinauthor = Author.objects.get(username=request.user.username)

		user_anons = Anon.objects.order_by(loggedinanon.anon_sort_char)[count:count100]

		previous_view = UserViews.objects.filter(anon=loggedinanon).order_by('-view_date').first()
		pages_view = UserViews.objects.create(page_view="tob_view_users_count__"+str(count), anon=loggedinanon, ip_address=ip, httpxforwardfor=x_forwarded_for)
		page_views.user_views.add(pages_view)
		if previous_view:
			pages_view.previous_view_id = previous_view.id
			pages_view.previous_page = previous_view.page_view
			pages_view.previous_view_date = previous_view.view_date
			pages_view.previous_view_time_between_pages = datetime.datetime.now(timezone.utc) - previous_view.view_date
		


		post_form = PostForm(request)
		anon_sort_form = AnonSortForm(request)

		the_response = render(request, "tob_view_users.html", {"user_anons_count": user_anons_count, "anon_sort_form": anon_sort_form, "count": count, "mcount": mcount, "count100": count100, "loggedinanon": loggedinanon, "user_anons": user_anons, "post_form": post_form, "registerform": registerform,  "loginform": loginform, })
	else:
		previous_view = UserViews.objects.filter(ip_address=ip).order_by('-view_date').first()
		pages_view = UserViews.objects.create(page_view="tob_view_users_count__"+str(count), ip_address=ip, httpxforwardfor=x_forwarded_for)
		page_views.user_views.add(pages_view)
		if previous_view:
			pages_view.previous_view_id = previous_view.id
			pages_view.previous_page = previous_view.page_view
			pages_view.previous_view_date = previous_view.view_date
			pages_view.previous_view_time_between_pages = datetime.datetime.now(timezone.utc) - previous_view.view_date
		
		the_response = render(request, "tob_view_users.html", {"user_anons_count": user_anons_count, "count": count, "mcount": mcount, "count100": count100, "user_anons": user_anons, "registerform": registerform,  "loginform": loginform})
	the_response.set_cookie('current', 'tob_view_users_count')
	the_response.set_cookie('count', count)
	return the_response




def tob_user_view(request, user, count=0):
	# Takes in the user object and collects lists to be displayed, totalling 100
	# Each must be checked, if any exist, HTML doc displays an IF with a message for each
	# if so, they are then ordered in the feasible ways saved for each anon
	# CHANGE SORTING TO . < function intrinsic to the object


	count = int(count)
	registerform = UserCreationForm()
	
		
	
	loginform = AuthenticationForm()
	if request.user.is_authenticated:
		loggedinuser = User.objects.get(username=request.user.username)
		loggedinanon = Anon.objects.get(username=loggedinuser)
		loggedinauthor = Author.objects.get(username=request.user.username)

	if User.objects.filter(username=user).count():
		user_themself, created = User.objects.get_or_create(username=user[0:149])
		user_author, created = Author.objects.get_or_create(username=user[0:149])
		user_anon = user_author.to_anon()
	else:
		user_themself, created = User.objects.get_or_create(username=user[0:149])
		user_author, created = Author.objects.get_or_create(username=user[0:149])
		user_anon = user_author.to_anon()
	
	

	users_posts = user_anon.posts.count()
	if users_posts:
		if request.user.is_authenticated:
			users_posts = user_anon.posts.order_by(loggedinanon.post_sort_char)[count:25]
			
		else:
			users_posts = user_anon.posts.order_by('viewcount')[count:count+25]
	if request.user.username == user or request.user.username == 'test':
		users_posts = user_anon.posts.order_by(loggedinanon.post_sort_char)[count:25]
		
	'''
	
	users_posted_comments = user_anon.posted_comments.all()
	if users_posted_comments is not None:
		if request.user.is_authenticated:
			users_posted_comments = sort_comments(users_posted_comments, loggedinanon.comment_sort, count, 25)
		else:
			users_posted_comments = sort_comments(users_posted_comments, 14, count, 25)

	'''

	'''
		Django, when calling and .order_by, sorts None into Error, rather than into None.
			THAT MUST BE FIXED - ReTaRdS, wouldn't get anywhere with creating the universe.
			So may aswell force 'migrate' to run 'migrate --run-syncdb' and 'makemigrations' beforehand.
	'''
	
	page_views, created = Pageviews.objects.get_or_create(page="tob_user_view")
	page_views.views += 1
	page_views.save()	
	
	total = 0
	for page in Pageviews.objects.all():
		total += page.views
	# Forms for entry on the view of a user of public model entry-points, 
	# each must have a respective submission point, ie. redirection url and therefore view.
	# they can be general (also redirected to by other views,) or specific (redirected from only this)

	# General
	if request.user.is_authenticated:
		post_form = PostForm(request)
		

		file_form = FileForm()
		email_form = EmailForm()
		post_sort_form = PostSortForm(request)


		comment_form = CommentForm()
	
	if request.user.is_authenticated:
		the_response = render(request, "tob_user_view.html", { "post_sort_form": post_sort_form, "email_form": email_form, "file_form": file_form, "total": total, "loggedinanon": loggedinanon, "users_posts": users_posts, "user_anon": user_anon, 
			"post_form": post_form, "comment_form": comment_form, "registerform": registerform,  "loginform": loginform, })
	else:
		the_response = render(request, "tob_user_view.html", {"total": total, "users_posts": users_posts, "users_spaces": users_spaces, "user_anon": user_anon, "registerform": registerform,  "loginform": loginform})
	the_response.set_cookie('current', 'tob_user_view_count')
	the_response.set_cookie('viewing_user', user)
	the_response.set_cookie('count', count)
	return the_response


def u(request, user):
	user_id = User.objects.get(username=user)
	return redirect('Bable:tob_user_view', user_id.username)

def tob_user_view_count(request, user, count=0):
	# Takes in the user object and collects lists to be displayed, totalling 100
	# Each must be checked, if any exist, HTML doc displays an IF with a message for each
	# if so, they are then ordered in the feasible ways saved for each anon
	# CHANGE SORTING TO . < function intrinsic to the object
	count = int(count)
	registerform = UserCreationForm()
	
	page_views, created = Pageviews.objects.get_or_create(page="tob_user_view_count")
	page_views.views += 1
	page_views.save()	
	
	
	loginform = AuthenticationForm()
	if request.user.is_authenticated:
		loggedinuser = User.objects.get(username=request.user.username)
		loggedinanon = Anon.objects.get(username=loggedinuser)
		loggedinauthor = Author.objects.get(username=request.user.username)

	if User.objects.filter(username=user).count():
		user_themself, created = User.objects.get_or_create(username=user)
		user_author, created = Author.objects.get_or_create(username=user_themself.username)
		user_anon = user_author.to_anon()
	else:
		user_themself, created = User.objects.get_or_create(username=user)
		user_author, created = Author.objects.get_or_create(username=user_themself.username)
		user_anon = user_author.to_anon()
	
	
	users_spaces = user_anon.spaces.all()
	if users_spaces is not None:
		users_spaces = user_anon.spaces.filter(Q(for_sale=True)|Q(approved_voters__username=request.user.username))
		if request.user.is_authenticated:
			users_spaces = users_spaces.order_by(loggedinanon.space_sort_char)[count:count+25]
		else:
			users_spaces = user_anon.spaces.order_by('viewcount')[count:count+25]
	


	anons_posts = Post.objects.all().filter(author=user_author)
	for post in anons_posts:
		user_anon.posts.add(post)
	


	users_posts = user_anon.posts.count()
	if users_posts:
		if request.user.is_authenticated:
			#users_posts = user_anon.posts.filter(Q(dictionaries__in=loggedinanon.purchased_dictionaries.all())|Q(dictionaries=None))
			users_posts = user_anon.posts.filter(Q(dictionaries__in=loggedinanon.purchased_dictionaries.all())|Q(dictionaries=None)).order_by(loggedinanon.post_sort_char)[count:25]
			
		else:
			users_posts = user_anon.posts.order_by('viewcount')[count:count+25]
	if request.user.username == user or request.user.username == 'test':
		users_posts = user_anon.posts.order_by(loggedinanon.post_sort_char)[count:25]
	# Dictionary contains: author, for_sale, views, 
	'''
	users_dictionaries = user_anon.dictionaries.filter(Q(for_sale=True)|Q(public=True))
	if request.user.username == user or request.user.username == 'test':
		users_dictionaries = user_anon.dictionaries
	if users_dictionaries is not None:
		if request.user.is_authenticated:
			if users_dictionaries.filter(purchase_orders__author=loggedinauthor):
				users_dictionaries = users_dictionaries.filter(purchase_orders__author=loggedinauthor)
			users_dictionaries = user_anon.dictionaries.filter(Q(for_sale=True)|Q(author=loggedinauthor))
			users_dictionaries = sort_dictionaries(users_dictionaries, loggedinanon.dictionary_sort, count, 25)
		else:
			users_dictionaries.order_by('viewcount')[count:count+25]

	users_examples = 0
	if user_anon.examples.count():
		users_examples = user_anon.examples.filter(dictionaries__the_dictionary_itself__in=loggedinanon.purchased_dictionaries.all().values_list('the_dictionary_itself'))
		if request.user.is_authenticated:
			users_examples = sort_examples(user_anon.examples.all(), loggedinanon.example_sort, count, 25)
		else:
			users_examples.order_by('viewcount')[count:count+25]

	users_posted_comments = user_anon.posted_comments.all()
	if users_posted_comments is not None:
		if request.user.is_authenticated:
			users_posted_comments = sort_comments(users_posted_comments, loggedinanon.comment_sort, count, 25)
		else:
			users_posted_comments = sort_comments(users_posted_comments, 14, count, 25)

	users_sponsors = Sponsor.objects.filter(author=user_author)
	users_sponsors_count = users_sponsors.count()
	if users_sponsors is not None:
		if request.user.is_authenticated:
			users_sponsors = sort_sponsors(users_sponsors, loggedinanon.sponsor_sort, count, 25)
		else:
			users_sponsors = users_sponsors.order_by('price_limit')[count:count+25]
	'''

	'''
		Django, when calling and .order_by, sorts None into Error, rather than into None.
			THAT MUST BE FIXED - ReTaRdS, wouldn't get anywhere with creating the universe.
			So may aswell force 'migrate' to run 'migrate --run-syncdb' and 'makemigrations' beforehand.
	'''
	
	
	total = 0
	for page in Pageviews.objects.all():
		total += page.views
	# Forms for entry on the view of a user of public model entry-points, 
	# each must have a respective submission point, ie. redirection url and therefore view.
	# they can be general (also redirected to by other views,) or specific (redirected from only this)

	# General
	if request.user.is_authenticated:
		dic_form = DictionaryForm()
		space_form = SpaceForm(request)
		post_form = PostForm(request)
		task_form = TaskForm()
		word_form = WordForm(request)
		bread_form = BreadForm()

		
		
		#apply_votestyle_form = ApplyVotestyleForm(request)
		apply_votes_form = VoteIntoVoteStyleForm()
		wallet_form = MoneroWalletForm()
		#exclude_votes_form = ExcludeVoteStyleForm(request)

		apply_votestyle_form = ApplyVotestyleForm(request)
		create_votes_form = CreateVotesForm(request)
		exclude_votes_form = ExcludeVotesForm(request)
		apply_dic_form = ApplyDictionaryForm(request)
		exclude_dic_form = ExcludeDictionaryAuthorForm()

		email_form = EmailForm()
		file_form = FileForm()
		post_sort_form = PostSortForm(request)

		#dic_names = []
		#for dic in loggedinanon.dictionaries.all: 
		#	dic_names += [dic.the_dictionary_itself]
		#word_form.fields["home_dictionary"].queryset = Dictionary_Source.objects.filter(author=loggedinauthor).values_list('the_dictionary_itself', flat=True)	# Specific
		#comment_form = CommentForm(request, value_from_object) # Make in template {% if loggedin %}
		comment_form = CommentForm(request)


	if request.user.is_authenticated:
		the_response = render(request, "tob_user_view.html", {"comment_form": comment_form, "post_sort_form": post_sort_form, "file_form": file_form, "email_form": email_form, "wallet_form": wallet_form, "total": total, "loggedinanon": loggedinanon, "users_posts": users_posts, "users_spaces": users_spaces, "user_anon": user_anon, 
			"bread_form": bread_form,"dic_form": dic_form, "space_form": space_form, "post_form": post_form, "task_form": task_form, "word_form": word_form, "apply_votes_form": apply_votes_form, "registerform": registerform,  "loginform": loginform, 
			"apply_votestyle_form": apply_votestyle_form, "create_votes_form": create_votes_form, "exclude_votes_form": exclude_votes_form, "apply_dic_form": apply_dic_form, "exclude_dic_form": exclude_dic_form})
	else:
		the_response = render(request, "tob_user_view.html", {"total": total, "users_posts": users_posts, "users_spaces": users_spaces, "user_anon": user_anon, "registerform": registerform,  "loginform": loginform})
	the_response.set_cookie('current', 'tob_user_view_count')
	the_response.set_cookie('viewing_user', user)
	the_response.set_cookie('count', count)
	return the_response


import random

'''
from web3.auto import w3
from eth_account.messages import encode_defunct
import asyncio

async def signature(request):     # noqa
    # User's signature from metamask passed through the body
    sig = request.get('signature')

    # The juicy bits. Here I try to verify the signature they sent.
    message = encode_defunct(text=request.get('message'))
    signed_address = (w3.eth.account.recover_message(message, signature=sig)).lower()

    # Same wallet address means same user. I use the cached address here.
    if get_cache_address() == signed_address:
        # Do what you will
        # You can generate the JSON access and refresh tokens here
        pass


'''

def tob_users_post(request, user, post, count=0, comment_count=0):
	if not User.objects.all().filter(username=user).count():
		user_themself = User.objects.create(username=user, password="Password-2")
	if User.objects.get(username=user):
		user_themself = User.objects.get(username=user)
		user_author, created = Author.objects.get_or_create(username=user)
		user_anon = user_author.to_anon()

		users_post = Post.objects.get(id=int(post))
		if users_post not in user_anon.posts.all():
			return HttpResponse("Not the users post.")
		users_post.viewcount += 1
		page_views, created = Pageviews.objects.get_or_create(page="tob_users_post")
		page_views.views += 1
		page_views.save()
		users_post.save()
	else:
		user_author, created = Author.objects.get_or_create(username=user)
		users_post = Post.objects.get(id=int(post))
		page_views, created = Pageviews.objects.get_or_create(page="tob_users_post")
		page_views.views += 1
		page_views.save()
		users_post.viewcount += 1
		users_post.save()


	
	registerform = UserCreationForm()
	
		
	
	count = 0
	count100 = 25
	mcount = 0

	x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
	if x_forwarded_for:
		x_forwarded_for = x_forwarded_for.split(',')[0]
	ip = request.META.get('REMOTE_ADDR')

	
	total = 0
	for page in Pageviews.objects.all():
		total += page.views

	loginform = AuthenticationForm()
	if request.user.is_authenticated:
		loggedinuser = User.objects.get(username=request.user.username)
		loggedinanon = Anon.objects.get(username=loggedinuser)
		users_post.has_viewed.add(Author.objects.get(username=request.user.username))
		
		if user == request.user.username:
			post_form = PostForm(request, instance=users_post)
		else:
			post_form = PostForm(request)
		
		comment_form = CommentForm(request)

		file_form = FileForm()
		
		post_filter_depth_form = PostFilterDepthForm(request)
		post_filter_from_date_form = PostFilterFromDateForm(request)

		comment_filter_depth_form = CommentFilterDepthForm(request)
		comment_filter_from_date_form = CommentFilterFromDateForm(request)


		

		startdate = datetime.datetime.now() - timedelta(minutes=int(loggedinanon.post_sort_from_date_char.split(',')[0]), hours=int(loggedinanon.post_sort_from_date_char.split(',')[1]), days=int(loggedinanon.post_sort_from_date_char.split(',')[2]), weeks=int(loggedinanon.post_sort_from_date_char.split(',')[3]))
		enddate = startdate - timedelta(minutes=int(loggedinanon.post_sort_depth_char.split(',')[0]), hours=int(loggedinanon.post_sort_depth_char.split(',')[1]), days=int(loggedinanon.post_sort_depth_char.split(',')[2]), weeks=int(loggedinanon.post_sort_depth_char.split(',')[3]))
		
		posts_by_viewcount = Post.objects.filter(latest_change_date__range=[enddate, startdate]).order_by(loggedinanon.post_sort_char)[count:count+25]
		posts_by_viewcount = list(posts_by_viewcount.values('img', 'url2', 'author__username', 'id', 'title', 'body', 'votes', 'viewcount', 'latest_change_date'))
		if not loggedinanon.comment_sort_from_date_char:
			loggedinanon.comment_sort_from_date_char = "0,0,0,0"
		if not loggedinanon.comment_sort_depth_char:
			loggedinanon.comment_sort_depth_char = "0,0,0,10000"
		startdate = datetime.datetime.now() - timedelta(minutes=int(loggedinanon.comment_sort_from_date_char.split(',')[0]), hours=int(loggedinanon.comment_sort_from_date_char.split(',')[1]), days=int(loggedinanon.comment_sort_from_date_char.split(',')[2]), weeks=int(loggedinanon.comment_sort_from_date_char.split(',')[3]))
		enddate = startdate - timedelta(minutes=int(loggedinanon.comment_sort_depth_char.split(',')[0]), hours=int(loggedinanon.comment_sort_depth_char.split(',')[1]), days=int(loggedinanon.comment_sort_depth_char.split(',')[2]), weeks=int(loggedinanon.comment_sort_depth_char.split(',')[3]))
		
		comments_by_viewcount = users_post.comments.filter(latest_change_date__range=[enddate, startdate]).order_by(loggedinanon.comment_sort_char)[comment_count:comment_count+100]

		loggedinanon.is_viewing = True
		loggedinanon.save()
		the_response = render(request, "tob_users_post.html", {"ip": ip, "x_forwarded_for": x_forwarded_for, "file_form": file_form, "total": total, "mcount": mcount, "count": count, "count100": count100, "posts" : posts_by_viewcount, "loggedinanon": loggedinanon, "users_post": users_post, "user_author": user_author,"post_form": post_form, "registerform": registerform,  "loginform": loginform, })
	else:
		if users_post.public:

			posts_by_viewcount = Post.objects.order_by('viewcount')[count:count+25]
			posts_by_viewcount = list(posts_by_viewcount.values('img', 'url2', 'author__username', 'id', 'title', 'body', 'votes', 'viewcount', 'latest_change_date'))
		
			
			the_response = render(request, "tob_users_post.html", {"ip": ip, "x_forwarded_for": x_forwarded_for, "total": total, "mcount": mcount, "count": count, "count100": count100, "posts" : posts_by_viewcount, "users_post": users_post, "user_anon": user_anon, "user_author": user_author,  "registerform": registerform,  "loginform": loginform})
		else:
			return HttpResponse("Not a public post.")
	the_response.set_cookie('current', 'tob_users_post')
	the_response.set_cookie('viewing_user', user)
	the_response.set_cookie('post', post)
	the_response.set_cookie('count', count)
	return the_response

def tob_users_posts(request, user, count):
	count = int(count)
	user_themself = User.objects.get(username=user)
	user_anon = Anon.objects.get(username=user_themself)
	
	registerform = UserCreationForm()
	
	page_views, created = Pageviews.objects.get_or_create(page="tob_users_posts")
	page_views.views += 1
	page_views.save()	
	
	loginform = AuthenticationForm()
	if request.user.is_authenticated:
		loggedinuser = User.objects.get(username=request.user.username)
		loggedinanon = Anon.objects.get(username=loggedinuser)

	users_posts = user_anon.posts.count()
	if users_posts:
		if request.user.is_authenticated:
			users_posts = user_anon.posts.order_by(loggedinanon.post_sort_char)[count:count+100]
		else:
			users_posts = user_anon.posts.order_by('viewcount')[count:count+100]

	x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
	if x_forwarded_for:
		x_forwarded_for = x_forwarded_for.split(',')[0]
	ip = request.META.get('REMOTE_ADDR')

	
	if request.user.is_authenticated:
		post_form = PostForm(request)
		post_sort_form = PostSortForm(request)
		
		the_response = render(request, "tob_users_posts.html", {"post_sort_form": post_sort_form, "ip": ip, "x_forwarded_for": x_forwarded_for, "loggedinanon": loggedinanon, "user_anon": user_anon, "users_posts": users_posts, "post_form": post_form, "registerform": registerform,  "loginform": loginform, })
	else:
		the_response = render(request, "tob_users_posts.html", {"ip": ip, "x_forwarded_for": x_forwarded_for, "user_anon": user_anon, "users_posts": users_posts, "registerform": registerform,  "loginform": loginform})

	the_response.set_cookie('current', 'tob_users_posts')
	the_response.set_cookie('viewing_user', user)
	the_response.set_cookie('count', count)
	return the_response


def tob_users_posts_comment(request, user, post, comment):
	user_themself = User.objects.get(username=user)
	user_anon = Anon.objects.get(username=user_themself)
	users_posts = user_anon.posts.order_by('-latest_change_date')[:100]
	
	registerform = UserCreationForm()
	
	page_views, created = Pageviews.objects.get_or_create(page="tob_users_posts_comment")
	page_views.views += 1
	page_views.save()	
	
	
	loginform = AuthenticationForm()
	if request.user.is_authenticated:
		loggedinuser = User.objects.get(username=request.user.username)
		loggedinanon = Anon.objects.get(username=loggedinuser)
	

	if request.user.is_authenticated:
		post_form = PostForm(request)
		
		the_response = render(request, "tob_users_posts.html", {"loggedinanon": loggedinanon, "users_posts": users_posts, "post_form": post_form, "registerform": registerform,  "loginform": loginform, })
	else:
		the_response = render(request, "tob_users_posts.html", {"users_posts": users_posts, "registerform": registerform,  "loginform": loginform})

	the_response.set_cookie('current', 'tob_users_posts_comment')
	the_response.set_cookie('viewing_user', user)
	the_response.set_cookie('post', post)
	the_response.set_cookie('comment', comment)
	return the_response


@login_required
def submit_email(request):
	loggedinuser = User.objects.get(username=request.user.username)
	loggedinanon = Anon.objects.get(username=loggedinuser)
	if request.method == 'POST':
		bread_form = EmailForm(request.POST)
		if bread_form.is_valid():
			loggedinanon.email = bread_form.cleaned_data['email']
			loggedinanon.save()
			loggedinanon.username.email = bread_form.cleaned_data['email']
			loggedinanon.username.save()
	loggedinanon.save()
	return base_redirect(request, 'email saved')
	

'''
# Test program
rack = ['_', 'u', 'v', 'w', 'x', 'y', 'z']
lexicon = ['apple', 'whisky', 'yutz', 'xray', 'tux', 'xyzzy', 'zebra']

for word in lexicon: 
    valid_word(word, rack)
'''

import requests
from base64 import b64encode

@login_required
def upload_file(request):
	loggedinuser = User.objects.get(username=request.user.username)
	loggedinanon = Anon.objects.get(username=loggedinuser)
	if request.method == 'POST':
		file_form = FileForm(request.POST, request.FILES)
		if file_form.is_valid() and file_form.cleaned_data['file']:
			#client = ipfshttpclient.connect()
			#datahash = client.addfile(request.FILES['file'].read())
			#print(datahash)
			userAndPass = b64encode(b"ff371d15-c2bc-4930-83c4-ce5c9c926dcc:phbzspnkD3gNP3CHkIBolc4MkziwSS8EjWY26PujQlXRDR0y9J").decode("ascii")
			headers = { 'Authorization' : 'Basic %s' %  userAndPass, "Content-Type": "application/octet-stream" }

			resp = requests.post('https://runfission.com/ipfs/', headers=headers, files={ "files": request.FILES['file'].read()})
			print(resp)
			data = resp.read()
			new_file = File.objects.create(url='https://runfission.com/ipfs/'+data['Hash']+'?filename='+data['Name'], public=file_form.cleaned_data['public'])
			if new_file.public:
				loggedinanon.public_files.add(new_file)
			else:
				loggedinanon.all_files.add(new_file)
			loggedinanon.save()
		else: return HttpResponse(file_form.errors)

	return redirect('Bable:tob_users_files', request.user.username)


@login_required
def tob_users_files(request, user):
	viewing_user = User.objects.get(username=user)
	viewing_anon = Anon.objects.get(username=viewing_user)
	loggedinuser = User.objects.get(username=request.user.username)
	loggedinanon = Anon.objects.get(username=loggedinuser)
	post_form = PostForm()
	
	file_form = FileForm()
	all_files = loggedinanon.all_files.all()
	public_files = loggedinanon.public_files.all()
	return render(request, "tob_users_files.html", { "file_form": file_form, "loggedinanon": loggedinanon, "viewing_anon": viewing_anon, "post_form": post_form, })



import math
from matplotlib import pyplot as plt
import matplotlib
from matplotlib_venn import venn2, venn3
import numpy as np
from matplotlib.figure import Figure

import plotly

import matplotlib.pyplot as plt
from matplotlib_venn import venn2, venn3

import plotly as py
from plotly.offline import iplot
import plotly.graph_objs as go
import plotly.io as pio
pio.renderers.default = 'iframe'

import scipy


def venn_to_plotly(L_sets,L_labels=None,title=None):
    
    #get number of sets
    n_sets = len(L_sets)
    
    #choose and create matplotlib venn diagramm
    if n_sets == 2:
        if L_labels and len(L_labels) == n_sets:
            v = venn2(L_sets,L_labels)
        else:
            v = venn2(L_sets)
    elif n_sets == 3:
        if L_labels and len(L_labels) == n_sets:
            v = venn3(L_sets,L_labels)
        else:
            v = venn3(L_sets)
    #supress output of venn diagramm
    plt.close()
    
    #Create empty lists to hold shapes and annotations
    L_shapes = []
    L_annotation = []
    
    #Define color list for sets
    #check for other colors: https://css-tricks.com/snippets/css/named-colors-and-hex-equivalents/
    L_color = ['FireBrick','DodgerBlue','DimGrey'] 
    
    #Create empty list to make hold of min and max values of set shapes
    L_x_max = []
    L_y_max = []
    L_x_min = []
    L_y_min = []
    
    for i in range(0,n_sets):
        
        #create circle shape for current set
        
        shape = go.layout.Shape(
                type="circle",
                xref="x",
                yref="y",
                x0= v.centers[i][0] - v.radii[i],
                y0=v.centers[i][1] - v.radii[i],
                x1= v.centers[i][0] + v.radii[i],
                y1= v.centers[i][1] + v.radii[i],
                fillcolor=L_color[i],
                line_color=L_color[i],
                opacity = 0.75
            )
        
        L_shapes.append(shape)
        
        #create set label for current set
        for text in v.set_labels:
            text.set_fontsize(15)
        for x in range(len(v.subset_labels)):
            if v.subset_labels[x] is not None:
                v.subset_labels[x].set_fontsize(15)
        anno_set_label = go.layout.Annotation(
                xref="x",
                yref="y",
                x = v.set_labels[i].get_position()[0],
                y = v.set_labels[i].get_position()[1],
                text = v.set_labels[i].get_text(),
                showarrow=False
        )
        
        L_annotation.append(anno_set_label)
        
        #get min and max values of current set shape
        L_x_max.append(v.centers[i][0] + v.radii[i])
        L_x_min.append(v.centers[i][0] - v.radii[i])
        L_y_max.append(v.centers[i][1] + v.radii[i])
        L_y_min.append(v.centers[i][1] - v.radii[i])
    
    #determine number of subsets
    n_subsets = sum([scipy.special.binom(n_sets,i+1) for i in range(0,n_sets)])
    
    for i in range(0,int(n_subsets)):
        
        #create subset label (number of common elements for current subset
        anno_subset_label = go.layout.Annotation(
                xref="x",
                yref="y",
                x = v.subset_labels[i].get_position()[0],
                y = v.subset_labels[i].get_position()[1],
                text = v.subset_labels[i].get_text(),
                showarrow=False
        )
        
        L_annotation.append(anno_subset_label)
        
        
    #define off_set for the figure range    
    off_set = 0.2
    
    #get min and max for x and y dimension to set the figure range
    x_max = max(L_x_max) + off_set
    x_min = min(L_x_min) - off_set
    y_max = max(L_y_max) + off_set
    y_min = min(L_y_min) - off_set
    
    #create plotly figure
    p_fig = go.Figure()
    
    #set xaxes range and hide ticks and ticklabels
    p_fig.update_xaxes(
        range=[x_min, x_max], 
        showticklabels=False, 
        ticklen=0
    )
    
    #set yaxes range and hide ticks and ticklabels
    p_fig.update_yaxes(
        range=[y_min, y_max], 
        scaleanchor="x", 
        scaleratio=1, 
        showticklabels=False, 
        ticklen=0
    )
    
    #set figure properties and add shapes and annotations
    p_fig.update_layout(
        plot_bgcolor='white', 
        margin = dict(b = 0, l = 10, pad = 0, r = 10, t = 40),
        width=800, 
        height=400,
        shapes= L_shapes, 
        annotations = L_annotation,
        title = dict(text = title, x=0.5, xanchor = 'center')
    )

    return p_fig



'''
def complementary_scholar(request):
	registerform = UserCreationForm()
	#
	#	
	#a = set(['a', 'b', 'c']) 
	#b = set(['c', 'd', 'e'])
	#c = set(['e', 'f', 'a'])
	#s = [a, b, c]

	# Plot it
	#matplotlib.pyplot.switch_backend('Agg')
	#h = venn3(s, ('A', 'B', 'C'))

	#h = venn_to_plotly(s)
	
	#graph_div = plotly.offline.plot(h, auto_open = False, output_type="div")
	
	#s = [a, b]
	#h = venn_to_plotly(s)

	search_1 = 0
	search_2 = 0
	#search_3 = 0
	search_1__2 = 0
	search_1_2 = 0
	#search_1_3 = 0
	#search_2__3 = 0
	#search_2_3 = 0
	#search_1__2__3 = 0
	#search_1_2_3 = 0

	#graph_div_2 = plotly.offline.plot(h, auto_open = False, output_type="div")
	
	if ('q_1' in request.GET) and request.GET['q_1'].strip():
		query_string_1 = request.GET['q_1']
		search_1 = Post.objects.filter(title__contains=query_string_1).filter(public=True).order_by('-latest_change_date')[0:10]
		

	if ('q_2' in request.GET) and request.GET['q_2'].strip():
		query_string_2 = request.GET['q_2']
		search_2 = Post.objects.filter(title__contains=query_string_2).filter(public=True).order_by('-latest_change_date')[0:10]
		
	
	if ('q_3' in request.GET) and request.GET['q_3'].strip():
		query_string_3 = request.GET['q_3']
		search_3 = Post.objects.filter(title__contains=query_string_3).filter(public=True).order_by('-latest_change_date')[0:100]
	
	if ('q_1' in request.GET) and request.GET['q_1'].strip() and ('q_2' in request.GET) and request.GET['q_2'].strip():
		query_string_1 = request.GET['q_1']
		query_string_2 = request.GET['q_2']
		search_1__2 = Post.objects.filter(title__contains=query_string_1+' '+query_string_2).filter(public=True).order_by('-latest_change_date')[0:10]
		search_1_2 = Post.objects.filter(title__contains=query_string_1).filter(title__contains=query_string_2).filter(public=True).order_by('-latest_change_date')[0:10]
	
	if ('q_1' in request.GET) and request.GET['q_1'].strip() and ('q_3' in request.GET) and request.GET['q_3'].strip():
		query_string_1 = request.GET['q_1']
		query_string_3 = request.GET['q_3']
		search_1_3 = Post.objects.filter(title__contains=query_string_1).filter(title__contains=query_string_3).filter(public=True).order_by('-latest_change_date')[0:100]
	
	if ('q_2' in request.GET) and request.GET['q_2'].strip() and ('q_3' in request.GET) and request.GET['q_3'].strip():
		query_string_2 = request.GET['q_2']
		query_string_3 = request.GET['q_3']
		search_2__3 = Post.objects.filter(title__contains=query_string_2 + ' ' + query_string_2).filter(public=True).order_by('-latest_change_date')[0:100]
		search_2_3 = Post.objects.filter(title__contains=query_string_2).filter(title__contains=query_string_3).filter(public=True).order_by('-latest_change_date')[0:100]
	
	if ('q_2' in request.GET) and request.GET['q_2'].strip() and ('q_3' in request.GET) and request.GET['q_3'].strip():
		query_string_1 = request.GET['q_1']
		query_string_2 = request.GET['q_2']
		query_string_3 = request.GET['q_3']
		search_1 = Post.objects.filter(title__contains=query_string_1).filter(public=True).order_by('-latest_change_date')[0:100]
		search_2 = Post.objects.filter(title__contains=query_string_2).filter(public=True).order_by('-latest_change_date')[0:100]
		search_3 = Post.objects.filter(title__contains=query_string_3).filter(public=True).order_by('-latest_change_date')[0:100]
		
		if search_1.count() > 3 and search_2.count() > 3 and search_3.count() > 3:
			list1 = search_1.values_list('id', flat=True)
			list2 = search_2.values_list('id', flat=True)
			list3 = search_3.values_list('id', flat=True)
			subset1 = list(set(list1).intersection(list2))
			subset2 = list(set(list1).intersection(list3))
			subset3 = list(set(list2).intersection(list3))

			if len(subset1) and len(subset2) and len(subset3):

				a = set(list1) 
				b = set(list2)
				c = set(list3)
				s = [a, b, c]

				# Plot it
				matplotlib.pyplot.switch_backend('Agg')
				h = venn3(s, ('A', 'B', 'C'))

				h = venn_to_plotly(s)
				
				graph_div = plotly.offline.plot(h, auto_open = False, output_type="div")

				#h = venn2(s, ('A', 'B', 'C'))
		if search_1__2.count() > 3 and search_2__3.count() > 3:
			a = set(search_1__2.values_list('id', flat=True)) 
			b = set(search_2__3.values_list('id', flat=True))
			s = [a, b]

			h = venn_to_plotly(s)
			
			graph_div_2 = plotly.offline.plot(h, auto_open = False, output_type="div")
		search_1__2__3 = Post.objects.filter(title__contains=query_string_1+' '+query_string_2+' '+query_string_3).filter(public=True).order_by('-latest_change_date')[0:100]
		search_1_2_3 = Post.objects.filter(title__contains=query_string_1).filter(title__contains=query_string_2).filter(title__contains=query_string_3).filter(public=True).order_by('-latest_change_date')[0:100]
	


	
	
	loginform = AuthenticationForm()
	if request.user.is_authenticated:
		loggedinuser = User.objects.get(username=request.user.username)
		loggedinanon = Anon.objects.get(username=loggedinuser)

		dic_form = DictionaryForm()
		space_form = SpaceForm(request)
		post_form = PostForm(request)
		task_form = TaskForm()
		word_form = WordForm(request)

		apply_votestyle_form = ApplyVotestyleForm(request)
		create_votes_form = CreateVotesForm(request)
		exclude_votes_form = ExcludeVotesForm(request)
		apply_dic_form = ApplyDictionaryForm(request)
		exclude_dic_form = ExcludeDictionaryAuthorForm()

		return render(request, "complementary_scholar.html", {"loggedinanon": loggedinanon, "search_1": search_1, "search_2": search_2, "search_1_2": search_1_2, "search_1__2": search_1__2, "dic_form": dic_form, "space_form": space_form, "post_form": post_form, "task_form": task_form, "word_form": word_form, "registerform": registerform, "loginform": loginform, 
			"apply_votestyle_form": apply_votestyle_form, "create_votes_form": create_votes_form, "exclude_votes_form": exclude_votes_form, "apply_dic_form": apply_dic_form, "exclude_dic_form": exclude_dic_form})
	return render(request, "complementary_scholar.html", {"search_1": search_1, "search_2": search_2, "search_1_2": search_1_2, "search_1__2": search_1__2, "registerform": registerform, "loginform": loginform, 
			})
'''


@login_required
def to_save_comment(request, user, comment_id):
	if request.user.is_authenticated:
		loggedinuser = User.objects.get(username=request.user.username)
		loggedinanon = Anon.objects.get(username=loggedinuser)

		author = Author.objects.get(username=user)
		saving_com = Comment.objects.get(id=int(comment_id))

		if saving_com in loggedinanon.saved_comments.all():
			loggedinanon.saved_comments.remove(saving_com)
		else:
			loggedinanon.saved_comments.add(saving_com)
	return base_redirect(request, 0)

@login_required
def to_save_sentence(request, user, sentence_id):
	if request.user.is_authenticated:
		loggedinuser = User.objects.get(username=request.user.username)
		loggedinanon = Anon.objects.get(username=loggedinuser)

		author = Author.objects.get(username=user)
		saving_sentence = Sentence.objects.get(id=int(sentence_id))

		if saving_sentence in loggedinanon.saved_sentences.all():
			loggedinanon.saved_sentences.remove(saving_sentence)
		else:
			loggedinanon.saved_sentences.add(saving_sentence)
	return base_redirect(request, 0)


