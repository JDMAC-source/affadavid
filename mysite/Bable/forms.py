# Copyright Aden Handasyde 2019

from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError
from Bable.models import *
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.db.models import Q




class UserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "password1", "password2",)

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        if commit:
            user.save()
        return user

class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    title = forms.CharField(required=True)
    message = forms.CharField(required=True, widget=forms.Textarea)



class ChangeEmailForm(forms.ModelForm):
    class Meta:
        model = Anon
        fields = ('email', 'phone',)
    
    def __init__(self, request, *args, **kwargs):
        current_anon = Anon.objects.get(username=request.user)
        self.instance = current_anon

    def clean(self):
        cleaned_data = super(BeginVerificationForm, self).clean()
        email = cleaned_data.get('email')
        phone = cleaned_data.get('phone')
        if not phone == self.instance.phone:
            raise forms.ValidationError('Check phone number is correct')
        else:
            self.instance.email = email
            self.instance.save()


class ChangePhoneForm(forms.ModelForm):
    class Meta:
        model = Anon
        fields = ('email', 'phone',)
    
    def __init__(self, request, *args, **kwargs):
        current_anon = Anon.objects.get(username=request.user)
        self.instance = current_anon

    def clean(self):
        cleaned_data = super(BeginVerificationForm, self).clean()
        email = cleaned_data.get('email')
        phone = cleaned_data.get('phone')
        if not email == self.instance.email:
            raise forms.ValidationError('Check email is correct')
        else:
            self.instance.phone = phone
            self.instance.save()


class BeginVerificationForm(forms.ModelForm):
    class Meta:
        model = Anon
        fields = ('email', 'phone',)
    
    def __init__(self, request, *args, **kwargs):
        current_anon = Anon.objects.get(username=request.user)
        self.instance = current_anon

    def clean(self):
        cleaned_data = super(BeginVerificationForm, self).clean()
        email = cleaned_data.get('email')
        phone = cleaned_data.get('phone')
        if not email == self.instance.email and not phone == self.instance.phone:
            raise forms.ValidationError('Check your email and phone number are correct')



# recreate with a comment model whereby you can attribute it to anyone.
# novelty.


class AnonSortForm(forms.ModelForm):
    class Meta:
        model = Anon
        fields = ('anon_sort_char',)
    def __init__(self, request, *args, **kwargs):
        super(AnonSortForm, self).__init__(*args, **kwargs)
        current_anon = Anon.objects.get(username=request.user)
        self.fields['anon_sort_char'].initial = current_anon.anon_sort_char
        self.fields['anon_sort_char'].label = False
        self.instance = current_anon



class PostSortForm(forms.ModelForm):
    class Meta:
        model = Anon
        fields = ('post_sort_char',)
    def __init__(self, request, *args, **kwargs):
        super(PostSortForm, self).__init__(*args, **kwargs)
        current_anon = Anon.objects.get(username=request.user)
        self.fields['post_sort_char'].initial = current_anon.post_sort_char
        self.fields['post_sort_char'].label = False
        self.instance = current_anon



class EmailForm(forms.ModelForm):
    class Meta:
        model = Anon
        fields = ('email',)

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ('username',)


class CommentThreadForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('id',)
    def clean(self):
        cleaned_data = super(CommentThreadForm, self).clean()
        identifier = cleaned_data.get('id')
        if not identifier:
            raise forms.ValidationError('is it real, is it real?')
    def __init__(self, request, *args, **kwargs):
        super(CommentThreadForm, self).__init__(*args, **kwargs)
        users_comments = Comment.objects.get(author=Author.objects.get(username=request.user.username)).values_list('id', flat=True)
        self.fields['identifier'] = forms.ChoiceField(choices=[(e, e) for e in users_comments])


#Repeat of Words with OVERTOPVISION



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
    
    def clean(self):
        cleaned_data = super(CommentForm, self).clean()
        body = cleaned_data.get('body')
        if not body:
            raise forms.ValidationError('You need a comment')
        
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        
        

    

       
class PostFilterDepthForm(forms.ModelForm):
    class Meta:
        model = Anon
        fields = ('post_sort_depth_char',)
    
    def clean(self):
        cleaned_data = super(PostFilterDepthForm, self).clean()
   
    def __init__(self, request, *args, **kwargs):
        super(PostFilterDepthForm, self).__init__(*args, **kwargs)
        current_anon = Anon.objects.get(username=request.user)
        self.fields['post_sort_depth_char'].initial = current_anon.post_sort_depth_char
        self.fields['post_sort_depth_char'].label = False
        self.instance = current_anon



class PostFilterFromDateForm(forms.ModelForm):
    class Meta:
        model = Anon
        fields = ('post_sort_from_date_char',)
    
    def clean(self):
        cleaned_data = super(PostFilterFromDateForm, self).clean()
   
    def __init__(self, request, *args, **kwargs):
        super(PostFilterFromDateForm, self).__init__(*args, **kwargs)
        current_anon = Anon.objects.get(username=request.user)
        self.fields['post_sort_from_date_char'].initial = current_anon.post_sort_from_date_char
        self.fields['post_sort_from_date_char'].label = False
        self.instance = current_anon




class CustomPasswordChangeForm(PasswordChangeForm):
        class Meta:
            model = User
            fields = ['old_password', 'new_password1', 'new_password2']



class CommentFilterDepthForm(forms.ModelForm):
    class Meta:
        model = Anon
        fields = ('comment_sort_depth_char',)
    
    def clean(self):
        cleaned_data = super(CommentFilterDepthForm, self).clean()
   
    def __init__(self, request, *args, **kwargs):
        super(CommentFilterDepthForm, self).__init__(*args, **kwargs)
        current_anon = Anon.objects.get(username=request.user)
        self.fields['comment_sort_depth_char'].initial = current_anon.comment_sort_depth_char
        self.fields['comment_sort_depth_char'].label = False
        self.instance = current_anon



class CommentFilterFromDateForm(forms.ModelForm):
    class Meta:
        model = Anon
        fields = ('comment_sort_from_date_char',)
    
    def clean(self):
        cleaned_data = super(CommentFilterFromDateForm, self).clean()
   
    def __init__(self, request, *args, **kwargs):
        super(CommentFilterFromDateForm, self).__init__(*args, **kwargs)
        current_anon = Anon.objects.get(username=request.user)
        self.fields['comment_sort_from_date_char'].initial = current_anon.comment_sort_from_date_char
        self.fields['comment_sort_from_date_char'].label = False
        self.instance = current_anon













class AnonFilterDepthForm(forms.ModelForm):
    class Meta:
        model = Anon
        fields = ('anon_sort_depth_char',)
    
    def clean(self):
        cleaned_data = super(AnonFilterDepthForm, self).clean()
   
    def __init__(self, request, *args, **kwargs):
        super(AnonFilterDepthForm, self).__init__(*args, **kwargs)
        current_anon = Anon.objects.get(username=request.user)
        self.fields['anon_sort_depth_char'].initial = current_anon.anon_sort_depth_char
        self.fields['anon_sort_depth_char'].label = False
        self.instance = current_anon



class AnonFilterFromDateForm(forms.ModelForm):
    class Meta:
        model = Anon
        fields = ('anon_sort_from_date_char',)
    
    def clean(self):
        cleaned_data = super(AnonFilterFromDateForm, self).clean()
   
    def __init__(self, request, *args, **kwargs):
        super(AnonFilterFromDateForm, self).__init__(*args, **kwargs)
        current_anon = Anon.objects.get(username=request.user)
        self.fields['anon_sort_from_date_char'].initial = current_anon.anon_sort_from_date_char
        self.fields['anon_sort_from_date_char'].label = False
        self.instance = current_anon










class PastCredibilityFilterDepthForm(forms.ModelForm):
    class Meta:
        model = Anon
        fields = ('past_credibility_sort_depth_char',)
    
    def clean(self):
        cleaned_data = super(PastCredibilityFilterDepthForm, self).clean()
   
    def __init__(self, request, *args, **kwargs):
        super(PastCredibilityFilterDepthForm, self).__init__(*args, **kwargs)
        current_anon = Anon.objects.get(username=request.user)
        self.fields['past_credibility_sort_depth_char'].initial = current_anon.past_credibility_sort_depth_char
        self.fields['past_credibility_sort_depth_char'].label = False
        self.instance = current_anon



class PastCredibilityFilterFromDateForm(forms.ModelForm):
    class Meta:
        model = Anon
        fields = ('past_credibility_sort_from_date_char',)
    
    def clean(self):
        cleaned_data = super(PastCredibilityFilterFromDateForm, self).clean()
   
    def __init__(self, request, *args, **kwargs):
        super(PastCredibilityFilterFromDateForm, self).__init__(*args, **kwargs)
        current_anon = Anon.objects.get(username=request.user)
        self.fields['past_credibility_sort_from_date_char'].initial = current_anon.past_credibility_sort_from_date_char
        self.fields['past_credibility_sort_from_date_char'].label = False
        self.instance = current_anon




class PastAccuracyFilterDepthForm(forms.ModelForm):
    class Meta:
        model = Anon
        fields = ('past_accuracy_sort_depth_char',)
    
    def clean(self):
        cleaned_data = super(PastAccuracyFilterDepthForm, self).clean()
   
    def __init__(self, request, *args, **kwargs):
        super(PastAccuracyFilterDepthForm, self).__init__(*args, **kwargs)
        current_anon = Anon.objects.get(username=request.user)
        self.fields['past_accuracy_sort_depth_char'].initial = current_anon.past_accuracy_sort_depth_char
        self.fields['past_accuracy_sort_depth_char'].label = False
        self.instance = current_anon



class PastAccuracyFilterFromDateForm(forms.ModelForm):
    class Meta:
        model = Anon
        fields = ('past_accuracy_sort_from_date_char',)
    
    def clean(self):
        cleaned_data = super(PastAccuracyFilterFromDateForm, self).clean()
   
    def __init__(self, request, *args, **kwargs):
        super(PastAccuracyFilterFromDateForm, self).__init__(*args, **kwargs)
        current_anon = Anon.objects.get(username=request.user)
        self.fields['past_accuracy_sort_from_date_char'].initial = current_anon.past_accuracy_sort_from_date_char
        self.fields['past_accuracy_sort_from_date_char'].label = False
        self.instance = current_anon




class PastSentenceBeforeEditViewsFilterDepthForm(forms.ModelForm):
    class Meta:
        model = Anon
        fields = ('past_sentence_before_edit_views_sort_depth_char',)
    
    def clean(self):
        cleaned_data = super(PastSentenceBeforeEditViewsFilterDepthForm, self).clean()
   
    def __init__(self, request, *args, **kwargs):
        super(PastSentenceBeforeEditViewsFilterDepthForm, self).__init__(*args, **kwargs)
        current_anon = Anon.objects.get(username=request.user)
        self.fields['past_sentence_before_edit_views_sort_depth_char'].initial = current_anon.past_sentence_before_edit_views_sort_depth_char
        self.fields['past_sentence_before_edit_views_sort_depth_char'].label = False
        self.instance = current_anon



class PastSentenceBeforeEditViewsFilterFromDateForm(forms.ModelForm):
    class Meta:
        model = Anon
        fields = ('past_sentence_before_edit_views_sort_from_date_char',)
    
    def clean(self):
        cleaned_data = super(PastSentenceBeforeEditViewsFilterFromDateForm, self).clean()
   
    def __init__(self, request, *args, **kwargs):
        super(PastSentenceBeforeEditViewsFilterFromDateForm, self).__init__(*args, **kwargs)
        current_anon = Anon.objects.get(username=request.user)
        self.fields['past_sentence_before_edit_views_sort_from_date_char'].initial = current_anon.past_sentence_before_edit_views_sort_from_date_char
        self.fields['past_sentence_before_edit_views_sort_from_date_char'].label = False
        self.instance = current_anon



class PastSentenceAfterEditViewsFilterDepthForm(forms.ModelForm):
    class Meta:
        model = Anon
        fields = ('past_sentence_after_edit_views_sort_depth_char',)
    
    def clean(self):
        cleaned_data = super(PastSentenceAfterEditViewsFilterDepthForm, self).clean()
   
    def __init__(self, request, *args, **kwargs):
        super(PastSentenceAfterEditViewsFilterDepthForm, self).__init__(*args, **kwargs)
        current_anon = Anon.objects.get(username=request.user)
        self.fields['past_sentence_after_edit_views_sort_depth_char'].initial = current_anon.past_sentence_after_edit_views_sort_depth_char
        self.fields['past_sentence_after_edit_views_sort_depth_char'].label = False
        self.instance = current_anon



class PastSentenceAfterEditViewsFilterFromDateForm(forms.ModelForm):
    class Meta:
        model = Anon
        fields = ('past_sentence_after_edit_views_sort_from_date_char',)
    
    def clean(self):
        cleaned_data = super(PastSentenceAfterEditViewsFilterFromDateForm, self).clean()
   
    def __init__(self, request, *args, **kwargs):
        super(PastSentenceAfterEditViewsFilterFromDateForm, self).__init__(*args, **kwargs)
        current_anon = Anon.objects.get(username=request.user)
        self.fields['past_sentence_after_edit_views_sort_from_date_char'].initial = current_anon.past_sentence_after_edit_views_sort_from_date_char
        self.fields['past_sentence_after_edit_views_sort_from_date_char'].label = False
        self.instance = current_anon




class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body', 'img')
        
    def clean(self):
        cleaned_data = super(PostForm, self).clean()
        body = cleaned_data.get('body')
        title = cleaned_data.get('title')
        if not (body or title):
            raise forms.ValidationError('You need thiings')
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        

class AnonForm(forms.ModelForm):
    class Meta:
        model = Anon
        fields = ('username',)

class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ('file', 'public',)


