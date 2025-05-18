# Copyright Aden Handasyde 2019
from django.conf.urls import include
from django.urls import re_path as url
from . import views
from . import models
from django.contrib import admin
from django.urls import path

# ^^^^ Use for cleaning up dodgy datatables

from rest_framework import routers
# ^^^^ Use for cleaning up dodgy datatables

# Each has a sort
# Needs a page-number
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt import views as jwt_views
app_name='Bable'
# path('admin/', admin.site.urls),
router = routers.DefaultRouter()
router.register(r'author', views.AuthorViewSet)
#router.register(r'post', views.PostViewSet)
	
# Each has a sort
# Needs a page-number
urlpatterns = [
	path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
	path('i18n/', include('django.conf.urls.i18n')),
	path('posts/', views.ListCreatePostAPIView.as_view()),
	

	# path('admin/', admin.site.urls),
	path('logout/', views.logout_user, name='logout_user'),
	path('login/', views.login_view, name='login_view'),
	path('feedback/', views.feedback, name='feedback'),
	path('create_feedback/', views.create_feedback, name='create_feedback'),
	path('select_feedback_on_display/', views.thanks, name='thanks'),
	path('about/', views.about, name='about'),
	path('management/', views.management, name='management'),
	path('register/', views.register_view, name='register_view'),
	path('pages/', views.tower_of_bable, name='tower_of_bable'),
	
	path('landingpage/', views.landingpage, name='landingpage'),
	
	path('change_password/', views.change_password, name='change_password'),
	path('search/<search_id>/count/<count>/', views.search, name='search'),
	path('index/count/<count>/', views.tower_of_bable_count, name='tower_of_bable_count'),
	path('users/', views.tob_view_users, name='tob_view_users'),
	path('users/count/<count>/', views.tob_view_users_count, name='tob_view_users_count'),
	path('change_anon_sort_char/', views.change_anon_sort_char, name='change_anon_sort_char'),
	path('change_post_sort_char/', views.change_post_sort_char, name='change_post_sort_char'),
	path('change_post_filter_from_date/', views.change_post_filter_from_date, name='change_post_filter_from_date'),
	path('change_post_filter_depth/', views.change_post_filter_depth, name='change_post_filter_depth'),
	path('user/<user>/', views.tob_user_view, name='tob_user_view'),
	path('user/<user>/count/<count>/', views.tob_user_view_count, name='tob_user_view_count'),
	path('user/<user>/posts/count/<count>/', views.tob_users_posts, name='tob_users_posts'),
	path('user/<user>/post/<post_title>/count/<count>/', views.tob_users_post, name='tob_users_post'),
	path('user/<user>/post/<post_title>/comment/<comment_id>/count/<count>', views.tob_users_posts_comment, name='tob_users_posts_comment'),
	path('logout_user/', views.logout_user, name='logout_user'),
	path('create_post/', views.create_post, name='create_post'),
	path('edit_post/<post_id>/', views.edit_post, name='edit_post'),
	path('delete_own_comment/<comment_id>/', views.delete_own_comment, name='delete_own_comment'),
	path('delete_own_post/<user>/<post_id>/', views.delete_own_post, name='delete_own_post'),
	path('to_save_sentence/<user>/<sentence_id>/', views.to_save_sentence, name='to_save_sentence'),
	path('to_save_comment/<user>/<comment_id>/', views.to_save_comment, name='to_save_comment'),
	path('tob_post/<post>/', views.tob_post, name='tob_post'),
	path('tob_email/<token_id>/<count>/', views.tob_email, name='tob_email'),
	path('submit_email/', views.submit_email, name='submit_email'),
	path('roadmap/', views.roadmap, name='roadmap'),
	path('upload_file/', views.upload_file, name='upload_file'),
	path('tob_users_files/<user>/', views.tob_users_files, name='tob_users_files'),
    path('u/<user>/', views.u, name='u'),
]