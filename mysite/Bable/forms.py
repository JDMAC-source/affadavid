# Copyright Aden Handasyde 2019

from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError
from Bable.models import *
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q


class BusinessAdminForm(forms.ModelForm):
    class Meta:
        model = Storefront
        fields = ("business_admin",)
    def __init__(self, request, *args, **kwargs):
        super(BusinessAdminForm, self).__init__(*args, **kwargs)
        self.fields['business_admin'] = forms.MultipleChoiceField(choices=[(e, e) for e in Anon.objects.get(username=request.user).friends.order_by("username").values_list("username", flat=True)])


class ClickthroughForm(forms.Form):
    author = forms.CharField(required=True)
    sponsor_id = forms.CharField(required=True)


class ArcToForm(forms.ModelForm):
    class Meta:
        model = ArcTo
        fields = ("x", "y", "radius", "start_angle", "end_angle", "counter_clockwise",)
    def __init__(self, *args, **kwargs):
        super(ArcToForm, self).__init__(*args, **kwargs)

class QuadraticCurveToForm(forms.ModelForm):
    class Meta:
        model = QuadraticCurveTo
        fields = ("x", "y", "p1", "p2", )
    def __init__(self, *args, **kwargs):
        super(QuadraticCurveToForm, self).__init__(*args, **kwargs)
        
class BezierCurveToForm(forms.ModelForm):
    class Meta:
        model = BezierCurveTo
        fields = ("x1", "y1", "x2", "y2", "x3", "y3",)
    def __init__(self, *args, **kwargs):
        super(BezierCurveToForm, self).__init__(*args, **kwargs)

class MoveToForm(forms.ModelForm):
    class Meta:
        model = MoveTo
        fields = ("x", "y", )
    def __init__(self, *args, **kwargs):
        super(MoveToForm, self).__init__(*args, **kwargs)

class LineToForm(forms.ModelForm):
    class Meta:
        model = LineTo
        fields = ("x", "y",)
    def __init__(self, *args, **kwargs):
        super(LineToForm, self).__init__(*args, **kwargs)

class MovementForm(forms.ModelForm):
    class Meta:
        model = Movement
        fields = ("move_to", "line_to", "quadratic_curve_to", "arc_to", "line_width", "stroke_style", "stroke", "fill_style", "fill", "order",)
    def __init__(self, *args, **kwargs):
        super(MovementForm, self).__init__(*args, **kwargs)



class PurchasingForm(forms.ModelForm):
    class Meta:
        model = Storefront
        fields = ("products",)
    def __init__(self, *args, **kwargs):
        super(PurchasingForm, self).__init__(*args, **kwargs)
        self.fields['products'] = forms.MultipleChoiceField(choices=[(e, e) for e in self.instance.products.values_list("name", flat=True)]) 

class StorefrontForm(forms.ModelForm):
    class Meta:
        model = Storefront
        fields = ("logo", "title", "preview_text", "disclaimer", "image_1", "image_2", "image_3", "image_4", "image_5", "template_section_size_title_left","template_section_size_title_right","template_section_size_title_height", "template_section_size_disclaimer_left", "template_section_size_disclaimer_right", "template_section_size_disclaimer_height", "template_section_size_preview_left", "template_section_size_preview_right", "template_section_size_preview_height", "textblock_1","textblock_2","textblock_3","textblock_4",)
    def __init__(self, dictionary, *args, **kwargs):
        super(StorefrontForm, self).__init__(*args, **kwargs)
        self.fields['logo'] = forms.ChoiceField(choices=[(e, e) for e in dictionary.words.all().values_list("the_word_itself", flat=True)]) 


class StorefrontDicForm(forms.ModelForm):
    class Meta:
        model = Dictionary
        fields = ("the_dictionary_itself", )
    def __init__(self, user_anon, *args, **kwargs):
        super(StorefrontDicForm, self).__init__(*args, **kwargs)
        self.fields['the_dictionary_itself'] = forms.ChoiceField(choices=[(e, e) for e in user_anon.dictionaries.all().values_list("the_dictionary_itself", flat=True)]) 

class TimeAndRangePricesForm(forms.ModelForm):
    class Meta:
        model = TimeAndRangePrices
        fields = ("from_time_starting", "to_times_ending", "south_corner", "north_corner", "east_corner", "west_corner", "willing_for_price_per_kilometre", "willing_for_price_per_kilogram", "max_kilometre", "max_kilogram", "max_room_length", "max_room_height", "max_room_width")

class CourierForm(forms.ModelForm):
    class Meta:
        model = Courier
        fields = ("to_country", "to_state", "to_city", "to_address", "to_name", "update",  "leave_from_time", "leave_from_date", "estimated_arrival_time", "estimated_arrival_date", "deliver_to_instructions")
    def __init__(self, *args, **kwargs):
        super(CourierForm, self).__init__(*args, **kwargs)
        

class MembersSelectPrimationReference(forms.ModelForm):
    class Meta:
        model = Terms
        fields = ("primation_reference",)
    def __init__(self, request, terms, *args, **kwargs):
        super(MembersSelectPrimationReference, self).__init__(*args, **kwargs)
        self.instance = terms


class AddOrRemoveLegislatingTermsForm(forms.ModelForm):
    class Meta:
        model = Space
        fields = ("legislating_terms",)
    def __init__(self, request, terms, *args, **kwargs):
        super(AddOrRemoveLegislatingTermsForm, self).__init__(*args, **kwargs)
        self.instance = terms


class AddOrRemoveAdministratingTermsForm(forms.ModelForm):
    class Meta:
        model = Space
        fields = ("administrating_terms",)
    def __init__(self, request, terms, *args, **kwargs):
        super(AddOrRemoveAdministratingTermsForm, self).__init__(*args, **kwargs)
        self.instance = terms


class AddOrRemoveExecutingTermsForm(forms.ModelForm):
    class Meta:
        model = Space
        fields = ("executing_terms",)
    def __init__(self, request, terms, *args, **kwargs):
        super(AddOrRemoveExecutingTermsForm, self).__init__(*args, **kwargs)
        self.instance = terms


class AddOrRemoveAdjudicatingTermsForm(forms.ModelForm):
    class Meta:
        model = Space
        fields = ("adjudicating_terms",)
    def __init__(self, request, terms, *args, **kwargs):
        super(AddOrRemoveAdjudicatingTermsForm, self).__init__(*args, **kwargs)
        self.instance = terms


class PrimationConditionersSelectorFeedbackForm(forms.ModelForm):
    class Meta:
        model = Terms
        fields = ("conditioners",)
    def __init__(self, request, terms, *args, **kwargs):
        super(PrimationConditionersSelectorFeedbackForm, self).__init__(*args, **kwargs)
        self.instance = terms


class PrimationConditioneesSelectorFeedbackForm(forms.ModelForm):
    class Meta:
        model = Terms
        fields = ("conditionees",)
    def __init__(self, request, terms, *args, **kwargs):
        super(PrimationConditioneesSelectorFeedbackForm, self).__init__(*args, **kwargs)
        self.instance = terms

class AddOrRemoveTermsForm(forms.ModelForm):
    class Meta:
        model = Terms
        fields = ("chapter", "conditionees", "conditioners", "conditions", "accostings", "primation_fee", "primation_reference", 'delete',)
    def __init__(self, request, terms, *args, **kwargs):
        super(AddOrRemoveTermsForm, self).__init__(*args, **kwargs)
        self.instance = terms
        self.fields['conditionees'] = forms.MultipleChoiceField(choices=[(e, e) for e in terms.space.approved_voters.all().order_by('username').values_list('username', flat=True)])
        self.fields['condtioners'] = forms.MultipleChoiceField(choices=[(e, e) for e in terms.space.approved_voters.all().order_by('username').values_list('username', flat=True)])
        self.fields['primation_reference'] = forms.MultipleChoiceField(choices=[(e, e) for e in terms.space.approved_voters.all().order_by('username').values_list('username', flat=True)])


class VoteForLegislativeForm(forms.ModelForm):
    class Meta:
        model = Space
        fields = ("legislative_members",)
    def __init__(self, space, *args, **kwargs):
        super(VoteForLegislativeForm, self).__init__(*args, **kwargs)
        self.fields['legislative_members'] = forms.ChoiceField(choices=[(e, e) for e in space.approved_voters.all().order_by('username').values_list('username', flat=True)])

class VoteForAdministrativeForm(forms.ModelForm):
    class Meta:
        model = Space
        fields = ("administrative_members",)
    def __init__(self, space, *args, **kwargs):
        super(VoteForAdministrativeForm, self).__init__(*args, **kwargs)
        self.fields['administrative_members'] = forms.ChoiceField(choices=[(e, e) for e in space.approved_voters.all().order_by('username').values_list('username', flat=True)])

class VoteForExecutiveForm(forms.ModelForm):
    class Meta:
        model = Space
        fields = ("executive_members",)
    def __init__(self, space, *args, **kwargs):
        super(VoteForExecutiveForm, self).__init__(*args, **kwargs)
        self.fields['executive_members'] = forms.ChoiceField(choices=[(e, e) for e in space.approved_voters.all().order_by('username').values_list('username', flat=True)])

class VoteForJudiciaryForm(forms.ModelForm):
    class Meta:
        model = Space
        fields = ("judiciary_members",)
    def __init__(self, space, *args, **kwargs):
        super(VoteForJudiciaryForm, self).__init__(*args, **kwargs)
        self.fields['judiciary_members'] = forms.ChoiceField(choices=[(e, e) for e in space.approved_voters.all().order_by('username').values_list('username', flat=True)])

class WordLoanForm(forms.ModelForm):
    class Meta:
        model = Word_Loan
        fields = ("amount_total", "repayment_term", "repayment_rates", "words",)
    def __init__(self, request, dictionary_source, *args, **kwargs):
        super(WordLoanForm, self).__init__(*args, **kwargs)
        self.fields['words'] = forms.MultipleChoiceField(choices=[(e, e) for e in Word.objects.filter(author=Author.objects.get(username=request.user.username)).filter(home_dictionary=dictionary_source).order_by('the_word_itself').values_list('the_word_itself', flat=True)])


class DictionaryLoanForm(forms.ModelForm):
    class Meta:
        model = Dictionary_Loan
        fields = ("amount_total", "repayment_term", "repayment_rates", "dictionaries",)
    def __init__(self, request, *args, **kwargs):
        super(DictionaryLoanForm, self).__init__(*args, **kwargs)
        self.fields['dictionaries'] = forms.MultipleChoiceField(choices=[(e, e) for e in Dictionary.objects.filter(author=Author.objects.get(username=request.user.username)).order_by('the_dictionary_itself').values_list('the_dictionary_itself', flat=True)])


class LoanForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = ("amount_total", "repayment_term", "repayment_rates", "spaces",)
    def __init__(self, request, *args, **kwargs):
        super(LoanForm, self).__init__(*args, **kwargs)
        self.fields['spaces'] = forms.MultipleChoiceField(choices=[(e, e) for e in Space.objects.filter(author=Author.objects.get(username=request.user.username)).order_by('the_space_itself').values_list('the_space_itself', flat=True)])




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

# recreate with a comment model whereby you can attribute it to anyone.
# novelty.

class SponsorSortForm(forms.ModelForm):
    class Meta:
        model = Anon
        fields = ('sponsor_sort_char',)
    def __init__(self, request, *args, **kwargs):
        super(SponsorSortForm, self).__init__(*args, **kwargs)
        current_anon = Anon.objects.get(username=request.user)
        self.fields['sponsor_sort_char'].initial = current_anon.sponsor_sort_char
        self.fields['sponsor_sort_char'].label = False
        self.instance = current_anon



class ProductSortForm(forms.ModelForm):
    class Meta:
        model = Anon
        fields = ('product_sort_char',)
    def __init__(self, request, *args, **kwargs):
        super(ProductSortForm, self).__init__(*args, **kwargs)
        current_anon = Anon.objects.get(username=request.user)
        self.fields['product_sort_char'].initial = current_anon.product_sort_char
        self.fields['product_sort_char'].label = False
        self.instance = current_anon



class StorefrontSortForm(forms.ModelForm):
    class Meta:
        model = Anon
        fields = ('storefront_sort_char',)
    def __init__(self, request, *args, **kwargs):
        super(StorefrontSortForm, self).__init__(*args, **kwargs)
        current_anon = Anon.objects.get(username=request.user)
        self.fields['storefront_sort_char'].initial = current_anon.storefront_sort_char
        self.fields['storefront_sort_char'].label = False
        self.instance = current_anon



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


class SpaceSortForm(forms.ModelForm):
    class Meta:
        model = Anon
        fields = ('space_sort_char',)
    def __init__(self, request, *args, **kwargs):
        super(SpaceSortForm, self).__init__(*args, **kwargs)
        current_anon = Anon.objects.get(username=request.user)
        self.fields['space_sort_char'].initial = current_anon.space_sort_char
        self.fields['space_sort_char'].label = False
        self.instance = current_anon



class DicSortForm(forms.ModelForm):
    class Meta:
        model = Anon
        fields = ('dictionary_sort_char',)
    def __init__(self, request, *args, **kwargs):
        super(DicSortForm, self).__init__(*args, **kwargs)
        current_anon = Anon.objects.get(username=request.user)
        self.fields['dictionary_sort_char'].initial = current_anon.dictionary_sort_char
        self.fields['dictionary_sort_char'].label = False
        self.instance = current_anon


class WordSortForm(forms.ModelForm):
    class Meta:
        model = Anon
        fields = ('word_sort_char',)
    def __init__(self, request, *args, **kwargs):
        super(WordSortForm, self).__init__(*args, **kwargs)
        current_anon = Anon.objects.get(username=request.user)
        self.fields['word_sort_char'].initial = current_anon.word_sort_char
        self.fields['word_sort_char'].label = False
        self.instance = current_anon



class AttributeSortForm(forms.ModelForm):
    class Meta:
        model = Anon
        fields = ('attribute_sort_char',)
    def __init__(self, request, *args, **kwargs):
        super(AttributeSortForm, self).__init__(*args, **kwargs)
        current_anon = Anon.objects.get(username=request.user)
        self.fields['attribute_sort_char'].initial = current_anon.attribute_sort_char
        self.fields['attribute_sort_char'].label = False
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


class BreadForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ('amount',)

class BuyAdvertisingForm(forms.ModelForm):
    class Meta:
        model = Advertising
        fields = ('email', 'words_to_sponsor', 'the_sponsorship_phrase', 'img', 'url2', 'payperview', 'price_limit', 'allowable_expenditure', 'trickles')

class EmailForm(forms.ModelForm):
    class Meta:
        model = Anon
        fields = ('email',)

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ('username',)

class Comment_SourceForm(forms.ModelForm):
    class Meta:
        model = Comment_Source
        fields = ('body', 'dictionaries',) # conflation of word_sourcing is the point of not specifying. Or is it. ###Fork
    def clean(self):
        cleaned_data = super(Comment_SourceForm, self).clean()
        body = cleaned_data.get('body')
        dictionaries = cleaned_data.get('dictionaries')
        if not body:
            raise forms.ValidationError('What the fuck you trynna say?')
        if cleaned_data.get('dictionaries').count('dictionaries') > 5:
            raise forms.ValidationError("You can only have 5 dictionaries")
    def __init__(self, request, *args, **kwargs):
        super(Comment_SourceForm, self).__init__(*args, **kwargs)
        if Author.objects.get(username=request.user.username):
            self.fields['dictionaries'] = forms.ChoiceField(choices=[(e, e) for e in Dictionary_Source.objects.all().filter(author=Author.objects.get(username=request.user.username)).order_by('the_dictionary_itself').values_list('the_dictionary_itself', flat=True)])
        else:
            self.fields['dictionaries'] = None


class CommentSourceThreadForm(forms.ModelForm):
    class Meta:
        model = Comment_Source
        fields = ('id',)
    def clean(self):
        cleaned_data = super(CommentSourceThreadForm, self).clean()
        identifier = cleaned_data.get('id')
        if not identifier:
            raise forms.ValidationError('is it real, is it real?')
    def __init__(self, request, *args, **kwargs):
        super(CommentSourceThreadForm, self).__init__(*args, **kwargs)
        users_comments = Comment_Source.objects.all().filter(author=Author.objects.get(username=request.user.username)).values_list('id', flat=True)
        self.fields['identifier'] = forms.ChoiceField(choices=[(e, e) for e in users_comments])

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

class DefinitionForm(forms.ModelForm):
    class Meta:
        model = Definition
        fields = ('the_definition_itself',)
    def clean(self):
        cleaned_data = super(DefinitionForm, self).clean()
        body = cleaned_data.get('the_definition_itself')
        if not body:
            raise forms.ValidationError('You need a definition.')

#Repeat of Words with OVERTOPVISION-onedictionary_to_rule_them_all
class TranslationForm(forms.ModelForm):
    class Meta:
        model = Translation
        fields = ('the_translation_before', 'the_translation_after',)
    def clean(self):
        cleaned_data = super(TranslationForm, self).clean()
        body = cleaned_data.get('the_translation_before')
        body2 = cleaned_data.get('the_translation_after')
        if not body or body2:
            raise forms.ValidationError('You need a full translation.')

#Repeat of Words with OVERTOPVISION
class ConnexionForm(forms.ModelForm):
    class Meta:
        model = Connexion
        fields = ('the_connexion_itself',)
    def clean(self):
        cleaned_data = super(ConnexionForm, self).clean()
        body = cleaned_data.get('body')
        if not body:
            raise forms.ValidationError('You need a connexion.')

# ie. Metaphor, Spelling
class SimulacrumForm(forms.ModelForm):
    class Meta:
        model = Simulacrum
        fields = ('the_simulacrum_itself',)
    def clean(self):
        cleaned_data = super(SimulacrumForm, self).clean()
        body = cleaned_data.get('the_simulacrum_itself')
        if not body:
            raise forms.ValidationError('You need a simulacrum')

class SynonymForm(forms.ModelForm):
    class Meta:
        model = Synonym
        fields = ('the_synonym_itself',)
    def clean(self):
        cleaned_data = super(SynonymForm, self).clean()
        body = cleaned_data.get('the_synonym_itself')
        if not body:
            raise forms.ValidationError('You need a synonym.')

class AntonymForm(forms.ModelForm):
    class Meta:
        model = Antonym
        fields = ('the_antonym_itself',)
    def clean(self):
        cleaned_data = super(AntonymForm, self).clean()
        body = cleaned_data.get('the_antonym_itself')
        if not body:
            raise forms.ValidationError('You need an antonym.')

class HomonymForm(forms.ModelForm):
    class Meta:
        model = Homonym
        fields = ('the_homonym_itself',)
    def clean(self):
        cleaned_data = super(HomonymForm, self).clean()
        body = cleaned_data.get('the_homonym_itself')
        if not body:
            raise forms.ValidationError('You need a homonym.')

class AttributeForm(forms.ModelForm):
    class Meta:
        model = Attribute
        fields = ('the_attribute_itself',)
    def clean(self):
        cleaned_data = super(AttributeForm, self).clean()
        body = cleaned_data.get('the_attribute_itself')
        if not body:
            raise forms.ValidationError('You need an attribute')


# Change it so that the IPA characters is user definable, oh, they already are.
class IPA_pronunciationForm(forms.ModelForm):
    class Meta:
        model = IPA_pronunciation
        fields = ('the_IPA_itself', 'homophones')
    def clean(self):
        cleaned_data = super(IPA_pronunciationForm, self).clean()
        body = cleaned_data.get('the_IPA_itself')
        if not body:
            raise forms.ValidationError('You need an IPA.')

class ExampleForm(forms.ModelForm):
    class Meta:
        model = Example
        fields = ('the_example_itself',)
    def clean(self):
        cleaned_data = super(ExampleForm, self).clean()
        body = cleaned_data.get('the_example_itself')
        if not body:
            raise forms.ValidationError('You need an example.')

class StoryForm(forms.ModelForm):
    class Meta:
        model = Story
        fields = ('the_story_itself',)
    def clean(self):
        cleaned_data = super(StoryForm, self).clean()
        body = cleaned_data.get('the_story_itself')
        if not body:
            raise forms.ValidationError('You need a story.')

class RelationForm(forms.ModelForm):
    class Meta:
        model = Relation
        fields = ('the_relation_itself',)
    def clean(self):
        cleaned_data = super(RelationForm, self).clean()
        body = cleaned_data.get('the_relation_itself')
        if not body:
            raise forms.ValidationError('You need a relation')

class SponsorForm(forms.ModelForm):
    class Meta:
        model = Sponsor
        fields = ('the_sponsorship_phrase', 'img', 'url2', 'payperview', 'price_limit', 'allowable_expenditure', 'trickles')
    def clean(self):
        cleaned_data = super(SponsorForm, self).clean()
        the_sponsorship_phrase = cleaned_data.get('the_sponsorship_phrase')
        img = cleaned_data.get('img')
        url2 = cleaned_data.get('url2')
        price_limit = cleaned_data.get('price_limit')
        trickles = cleaned_data.get('trickles')
        allowable_expenditure = cleaned_data.get('allowable_expenditure')
        

class InsertSponsorForm(forms.ModelForm):
    class Meta:
        model = Sponsor
        fields = ('id',)
    def clean(self):
        cleaned_data = super(InsertSponsorForm, self).clean()
        identifier = cleaned_data.get('id')

    def __init__(self, request, *args, **kwargs):
        super(InsertSponsorForm, self).__init__(*args, **kwargs)
        all_sponsors = Sponsor.objects.filter(author__username=request.user.username).all()
        self.fields['identifier'] = forms.ChoiceField(choices=[(e, e) for e in all_sponsors.values_list("id", flat=True)])



class SpaceSourceForm(forms.ModelForm):
    class Meta:
        model = SpaceSource
        fields = ('the_space_itself',)
    def clean(self):
        cleaned_data = super(SpaceSourceForm, self).clean()
        body = cleaned_data.get('the_space_itself')
        if not body:
            raise forms.ValidationError('You need some Space')


class WordForm(forms.ModelForm):
    class Meta:
        model = Word
        fields = ('the_word_itself', 'home_dictionary')
        widgets = {
            'spaces': forms.TextInput(attrs={'class': 'spaces_input'}),
            'sponsors': forms.TextInput(attrs={'class': 'sponsors_input'}),
            'home_dictionary': forms.Select(attrs={'class': 'di_input'})
        }
    def clean(self):
        cleaned_data = super(WordForm, self).clean()
        body = cleaned_data.get('the_word_itself')
        body2 = cleaned_data.get('home_dictionary')
        #body3 = cleaned_data.get('attributes')
        if not body or body2: # or body3
            raise forms.ValidationError('You need a word and a dictionary')

    def __init__(self, request, *args, **kwargs):
        super(WordForm, self).__init__(*args, **kwargs)
        if Author.objects.get(username=request.user.username):
            self.fields['home_dictionary'] = forms.ChoiceField(choices=[(e, e) for e in Dictionary_Source.objects.all().filter(author=Author.objects.get(username=request.user.username)).order_by('the_dictionary_itself').values_list('the_dictionary_itself', flat=True)])
        else:
            self.fields['home_dictionary'] = None



class FontstyleForm(forms.ModelForm):
    class Meta:
        model = Fontstyle
        fields = ('css_encoding', 'duration')
    
    def __init__(self, *args, **kwargs):
        super(FontstyleForm, self).__init__(*args, **kwargs)
           



class FontForm(forms.ModelForm):
    class Meta:
        model = Word
        fields = ('fontsize', 'fontype')
        
    def clean(self):
        cleaned_data = super(FontForm, self).clean()
        
    def __init__(self, *args, **kwargs):
        super(FontForm, self).__init__(*args, **kwargs)
           


class CreateVotesForm(forms.ModelForm):
    class Meta:
        model = Votes
        fields = ('the_vote_name', 'the_vote_style', 'url2',)
    def clean(self):
        cleaned_data = super(CreateVotesForm, self).clean()
        the_vote_style = cleaned_data.get('the_vote_style')
        if not the_vote_style:
            raise forms.ValidationError('You need a thing thing in the what what')
    def __init__(self, request, *args, **kwargs):
        super(CreateVotesForm, self).__init__(*args, **kwargs)
        loggedinuser = User.objects.get(username=request.user.username)
        loggedinanon = Anon.objects.get(username=loggedinuser)
        self.fields['the_vote_style'] = forms.MultipleChoiceField(choices=[(e, e) for e in Space.objects.filter(saved_spaces=loggedinanon).order_by('the_space_itself__the_word_itself').values_list('the_space_itself__the_word_itself', flat=True)])
        

class ApplyVotestyleForm(forms.ModelForm):
    class Meta:
        model = Votes
        fields = ('the_vote_style',)
    def clean(self):
        cleaned_data = super(ApplyVotestyleForm, self).clean()
        the_vote_style = cleaned_data.get('the_vote_style')
        if not the_vote_style:
            raise forms.ValidationError('You need a thing thing in the what what')
    def __init__(self, request, *args, **kwargs):
        super(ApplyVotestyleForm, self).__init__(*args, **kwargs)
        loggedinuser = User.objects.get(username=request.user.username)
        loggedinanon = Anon.objects.get(username=loggedinuser)
        self.fields['the_vote_style'] = forms.CharField( widget=forms.TextInput(attrs={'type':'number'}))



class ExcludeVotesForm(forms.ModelForm):
    class Meta:
        model = Votes
        fields = ('the_vote_style',)
    def clean(self):
        cleaned_data = super(VotesForm, self).clean()
        the_vote_style = cleaned_data.get('the_vote_style')
        if not the_vote_style:
            raise forms.ValidationError('You need a thing thing in the what what')
    def __init__(self, request, *args, **kwargs):
        super(ExcludeVotesForm, self).__init__(*args, **kwargs)
        loggedinuser = User.objects.get(username=request.user.username)
        loggedinanon = Anon.objects.get(username=loggedinuser)
        self.fields['the_vote_style'] = forms.MultipleChoiceField(choices=[(e, e) for e in Space.objects.all().filter(purchased_spaces=loggedinanon).order_by('the_space_itself__the_word_itself').values_list('the_space_itself__the_word_itself', flat=True) and Votes.objects.all().filter(saved_votestyles=loggedinanon).order_by('the_vote_name').values_list('the_vote_name', flat=True)])



# of difference
class AnalysisForm(forms.ModelForm):
    class Meta:
        model = Analysis
        fields = ('the_critique_itself',)
    def clean(self):
        cleaned_data = super(AnalysisForm, self).clean()
        body = cleaned_data.get('the_critique_itself')
        if not body:
            raise forms.ValidationError('You need an analysis')
    def __init__(self, users_dic, *args, **kwargs):
        super(AnalysisForm, self).__init__(*args, **kwargs)
        if users_dic:
            self.fields['the_critique_itself'] = forms.MultipleChoiceField(choices=[(e, e) for e in Word.objects.all().filter(home_dictionary=users_dic.to_source()).order_by('the_word_itself').values_list('the_word_itself', flat=True)])
        else:
            self.fields['the_critique_itself'] = None


class RenditionForm(forms.ModelForm):
    class Meta:
        model = Rendition
        fields = ('the_rendition_itself',)
    def clean(self):
        cleaned_data = super(RenditionForm, self).clean()
        body = cleaned_data.get('the_rendition_itself')
        if not body:
            raise forms.ValidationError('You need a rendition')
    def __init__(self, users_dic, *args, **kwargs):
        super(RenditionForm, self).__init__(*args, **kwargs)
        if users_dic:
            self.fields['the_rendition_itself'] = forms.MultipleChoiceField(choices=[(e, e) for e in Word.objects.all().filter(home_dictionary=users_dic.to_source()).order_by('the_word_itself').values_list('the_word_itself', flat=True)])
        else:
            self.fields['the_rendition_itself'] = None

class SentenceForm(forms.ModelForm):
    class Meta:
        model = Sentence
        fields = ('the_sentence_itself',)
    def clean(self):
        cleaned_data = super(SentenceForm, self).clean()
        body = cleaned_data.get('the_sentence_itself')
        if not body:
            raise forms.ValidationError('You need a sentence')
    def __init__(self, users_dic, *args, **kwargs):
        super(SentenceForm, self).__init__(*args, **kwargs)
        if users_dic:
            print(users_dic.to_source())
            self.fields['the_sentence_itself'] = forms.MultipleChoiceField(choices=[(e, e) for e in Word.objects.all().filter(home_dictionary=users_dic.to_source()).order_by('the_word_itself').values_list('the_word_itself', flat=True)])
        else:
            self.fields['the_sentence_itself'] = None

class True_TranslationForm(forms.ModelForm):
    class Meta:
        model = True_Translation
        fields = ('the_translation_before', 'the_translation_after')
    def clean(self):
        cleaned_data = super(True_TranslationForm, self).clean()
        body = cleaned_data.get('the_translation_before')
        body2 = cleaned_data.get('the_translation_after')
        if not body or body2:
            raise forms.ValidationError('You need a both translations')
    def __init__(self, request, *args, **kwargs):
        super(True_TranslationForm, self).__init__(*args, **kwargs)
        loggedinuser = User.objects.get(username=request.user.username)
        loggedinanon = Anon.objects.get(username=loggedinuser)
        try: 
            anon_exclusions = loggedinanon.excluded_votestyles.all()
            choices = [(0,0)]
            for vote in anon_exclusions:
                choices.append(vote.to_source.the_vote_name.the_word_itself, vote.to_source.the_vote_name.the_word_itself)
            self.fields['the_translation_before'] = forms.MultipleChoiceField(choices=choices)
            self.fields['the_translation_after'] = forms.MultipleChoiceField(choices=choices)
        # try using Q()
        #self.fields['the_translation_before'] = forms.MultipleChoiceField(choices=[(e, e) for e in Word_Source.objects.filter(spacesource__votes__in=Votes.objects.get(excluded_votestyles__in=Anon.objects.get(username=User.objects.get(username=request.user.username)).excluded_votestyles.all())).order_by('the_word_itself').values_list('the_word_itself', flat=True)])
        #self.fields['the_translation_after'] = forms.MultipleChoiceField(choices=[(e, e) for e in Word.objects.filter(author=Author.objects.get(username=request.user.username)).order_by('the_word_itself').values_list('the_word_itself', flat=True)])
        except:
            self.fields['the_translation_before'] = None
            self.fields['the_translation_after'] = None

class WordgroupForm(forms.ModelForm):
    class Meta:
        model = Wordgroup
        fields = ('grouping',)
    def clean(self):
        cleaned_data = super(WordgroupForm, self).clean()
        body = cleaned_data.get('grouping')
        if not body:
            raise forms.ValidationError('You need to group something')
    def __init__(self, request, *args, **kwargs):
        super(WordgroupForm, self).__init__(*args, **kwargs)
        if Author.objects.get(username=request.user.username):
            self.fields['grouping'] = forms.MultipleChoiceField(choices=[(e, e) for e in Word.objects.all().filter(author=Author.objects.get(username=request.user.username)).order_by('the_word_itself').values_list('the_word_itself', flat=True)])
        else:
            self.fields['grouping'] = None
    

class DictionaryForm(forms.ModelForm):
    class Meta:
        model = Dictionary
        fields = ('public', 'for_sale', 'entry_fee', 'continuation_fee', 'invite_only', 'the_dictionary_itself')
    def clean(self):
        cleaned_data = super(DictionaryForm, self).clean()
        body = cleaned_data.get("id_the_dictionary_itself")
        if body is None:
            cleaned_data['id_the_dictionary_itself'] = 'name'

class ApplyDictionaryForm(forms.ModelForm):
    class Meta:
        model = Dictionary
        fields = ('the_dictionary_itself',)
    def clean(self):
        cleaned_data = super(DictionaryForm, self).clean()
        the_dictionary_itself = cleaned_data.get("the_dictionary_itself")
        if the_dictionary_itself is None:
            cleaned_data['the_dictionary_itself'] = 'name'
    def __init__(self, request, *args, **kwargs):
        super(ApplyDictionaryForm, self).__init__(*args, **kwargs)
        loggedinuser = User.objects.get(username=request.user.username)
        loggedinanon = Anon.objects.get(username=loggedinuser)
        try: 
            choices = [(0,0)]
            self.fields['the_dictionary_itself'] = forms.MultipleChoiceField(choices=[(e, e) for e in Dictionary.objects.all().filter(purchased_dictionaries=loggedinanon).order_by('the_dictionary_itself').values_list('the_dictionary_itself', flat=True)])
        except:
            choices = [(0,0)]
            self.fields['the_dictionary_itself'] = choices

class ExcludeDictionaryAuthorForm(forms.ModelForm):
    class Meta:
        model = Dictionary
        fields = ('author',)
    def clean(self):
        cleaned_data = super(DictionaryForm, self).clean()
        author = cleaned_data.get("author")
        if author is None:
            cleaned_data['author'] = 'name'
    def __init__(self, *args, **kwargs):
        super(ExcludeDictionaryAuthorForm, self).__init__(*args, **kwargs)
        self.fields['author'] = forms.CharField(max_length=120)

class DictionaryOwnerForm(forms.ModelForm):
    class Meta:
        model = Dictionary
        fields = ('public', 'for_sale', 'entry_fee', 'continuation_fee', 'invite_active', 'invite_code')
    def clean(self):
        cleaned_data = super(DictionaryOwnerForm, self).clean()
        public = cleaned_data.get('public')
        for_sale = cleaned_data.get('for_sale')
        entry_fee = cleaned_data.get('entry_fee')

class DictionaryPrereqForm(forms.ModelForm):
    class Meta:
        model = Dictionary
        fields = ('prerequisite_dics',)
    def clean(self):
        cleaned_data = super(DictionaryOwnerForm, self).clean()
        body = cleaned_data.get('prerequisite_dics')
        if body is None:
            cleaned_data['prerequisite_dics'] = False
    def __init__(self, request, *args, **kwargs):
        super(DictionaryPrereqForm, self).__init__(*args, **kwargs)
        if Author.objects.get(username=request.user.username):
            self.fields['prerequisite_dics'] = forms.MultipleChoiceField(choices=[(e, e) for e in Dictionary_Source.objects.all().filter(author=Author.objects.get(username=request.user.username)).order_by('the_dictionary_itself').values_list('the_dictionary_itself', flat=True)])
        else:
            self.fields['prerequisite_dics'] = None
    
class InviteCodeForm(forms.ModelForm):
    class Meta:
        model = Dictionary
        fields = ('invite_code',)
    def clean(self):
        cleaned_data = super(InviteCodeForm, self).clean()
        body = cleaned_data.get('invite_code')
        if body is None:
            cleaned_data['invite_code'] = False



class VoteIntoVoteStyleForm(forms.ModelForm):
    class Meta:
        model = Votes
        fields = ("the_vote_name", "the_vote_style",)
    def clean(self):
        cleaned_data = super(VoteIntoVoteStyleForm, self).clean()
        title = cleaned_data.get("the_vote_name")
        if title is None:
            cleaned_data['the_vote_name'] = 'null'
    






#class Video(models.Model):
#   the_video_itself = VideoField(default='')

#class Playlist(models.Model):
#   videos = models.ManyToManyField(Video)
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('the_task_itself', 'priority')

    def clean(self):
        cleaned_data = super(TaskForm, self).clean()
        body = cleaned_data.get('the_task_itself')
        if not body:
            raise forms.ValidationError('You need a Task')



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('dictionaries', 'body',)
    
    def clean(self):
        cleaned_data = super(CommentForm, self).clean()
        body = cleaned_data.get('body')
        if not body:
            raise forms.ValidationError('You need a comment')
        if len(cleaned_data.get('dictionaries')) > 5:
            raise forms.ValidationError("You can only have 5 dictionaries")
    def __init__(self, request, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        #self.instance == post_or_barcode
        if Author.objects.get(username=request.user.username):
            self.fields['dictionaries'] = forms.MultipleChoiceField(choices=[(e, e) for e in Dictionary.objects.all().filter(purchased_dictionaries=Anon.objects.get(username__username=request.user.username)).order_by('the_dictionary_itself').values_list('the_dictionary_itself', flat=True)])
        else:
            self.fields['dictionaries'] = None

    

class ProductForm(forms.ModelForm):
    class Meta:
        model = Price
        fields = ('name', 'stripe_price_id', 'stripe_product_id', 'price', 'url2purchase', 'description2purchase', 'description2helpsell', 'img', 'monthly',)

    

class SearchURLForm(forms.ModelForm):
    class Meta:
        model = SearchURL
        fields = ('name', 'public', 'img', 'stripe_product_id', 'stripe_price_id', 'price', 'monthly', 'cc')
        
    def clean(self):
        cleaned_data = super(SearchURLForm, self).clean()
        
    def __init__(self, *args, **kwargs):
        super(SearchURLForm, self).__init__(*args, **kwargs)
       
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









class StorefrontFilterDepthForm(forms.ModelForm):
    class Meta:
        model = Anon
        fields = ('storefront_sort_depth_char',)
    
    def clean(self):
        cleaned_data = super(StorefrontFilterDepthForm, self).clean()
   
    def __init__(self, request, *args, **kwargs):
        super(StorefrontFilterDepthForm, self).__init__(*args, **kwargs)
        current_anon = Anon.objects.get(username=request.user)
        self.fields['storefront_sort_depth_char'].initial = current_anon.storefront_sort_depth_char
        self.fields['storefront_sort_depth_char'].label = False
        self.instance = current_anon



class StorefrontFilterFromDateForm(forms.ModelForm):
    class Meta:
        model = Anon
        fields = ('storefront_sort_from_date_char',)
    
    def clean(self):
        cleaned_data = super(StorefrontFilterFromDateForm, self).clean()
   
    def __init__(self, request, *args, **kwargs):
        super(StorefrontFilterFromDateForm, self).__init__(*args, **kwargs)
        current_anon = Anon.objects.get(username=request.user)
        self.fields['storefront_sort_from_date_char'].initial = current_anon.storefront_sort_from_date_char
        self.fields['storefront_sort_from_date_char'].label = False
        self.instance = current_anon









class ProductFilterDepthForm(forms.ModelForm):
    class Meta:
        model = Anon
        fields = ('product_sort_depth_char',)
    
    def clean(self):
        cleaned_data = super(ProductFilterDepthForm, self).clean()
   
    def __init__(self, request, *args, **kwargs):
        super(ProductFilterDepthForm, self).__init__(*args, **kwargs)
        current_anon = Anon.objects.get(username=request.user)
        self.fields['product_sort_depth_char'].initial = current_anon.product_sort_depth_char
        self.fields['product_sort_depth_char'].label = False
        self.instance = current_anon



class ProductFilterFromDateForm(forms.ModelForm):
    class Meta:
        model = Anon
        fields = ('product_sort_from_date_char',)
    
    def clean(self):
        cleaned_data = super(ProductFilterFromDateForm, self).clean()
   
    def __init__(self, request, *args, **kwargs):
        super(ProductFilterFromDateForm, self).__init__(*args, **kwargs)
        current_anon = Anon.objects.get(username=request.user)
        self.fields['product_sort_from_date_char'].initial = current_anon.product_sort_from_date_char
        self.fields['product_sort_from_date_char'].label = False
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








class DictionaryFilterDepthForm(forms.ModelForm):
    class Meta:
        model = Anon
        fields = ('dictionary_sort_depth_char',)
    
    def clean(self):
        cleaned_data = super(DictionaryFilterDepthForm, self).clean()
   
    def __init__(self, request, *args, **kwargs):
        super(DictionaryFilterDepthForm, self).__init__(*args, **kwargs)
        current_anon = Anon.objects.get(username=request.user)
        self.fields['dictioanry_sort_depth_char'].initial = current_anon.dictioanry_sort_depth_char
        self.fields['dictioanry_sort_depth_char'].label = False
        self.instance = current_anon



class DictionaryFilterFromDateForm(forms.ModelForm):
    class Meta:
        model = Anon
        fields = ('dictionary_sort_from_date_char',)
    
    def clean(self):
        cleaned_data = super(DictionaryFilterFromDateForm, self).clean()
   
    def __init__(self, request, *args, **kwargs):
        super(DictionaryFilterFromDateForm, self).__init__(*args, **kwargs)
        current_anon = Anon.objects.get(username=request.user)
        self.fields['dictionary_sort_from_date_char'].initial = current_anon.dictionary_sort_from_date_char
        self.fields['dictionary_sort_from_date_char'].label = False
        self.instance = current_anon








class WordFilterDepthForm(forms.ModelForm):
    class Meta:
        model = Anon
        fields = ('word_sort_depth_char',)
    
    def clean(self):
        cleaned_data = super(WordFilterDepthForm, self).clean()
   
    def __init__(self, request, *args, **kwargs):
        super(WordFilterDepthForm, self).__init__(*args, **kwargs)
        current_anon = Anon.objects.get(username=request.user)
        self.fields['word_sort_depth_char'].initial = current_anon.word_sort_depth_char
        self.fields['word_sort_depth_char'].label = False
        self.instance = current_anon



class WordFilterFromDateForm(forms.ModelForm):
    class Meta:
        model = Anon
        fields = ('word_sort_from_date_char',)
    
    def clean(self):
        cleaned_data = super(WordFilterFromDateForm, self).clean()
   
    def __init__(self, request, *args, **kwargs):
        super(WordFilterFromDateForm, self).__init__(*args, **kwargs)
        current_anon = Anon.objects.get(username=request.user)
        self.fields['word_sort_from_date_char'].initial = current_anon.word_sort_from_date_char
        self.fields['word_sort_from_date_char'].label = False
        self.instance = current_anon








class AttributeFilterDepthForm(forms.ModelForm):
    class Meta:
        model = Anon
        fields = ('attribute_sort_depth_char',)
    
    def clean(self):
        cleaned_data = super(AttributeFilterDepthForm, self).clean()
   
    def __init__(self, request, *args, **kwargs):
        super(AttributeFilterDepthForm, self).__init__(*args, **kwargs)
        current_anon = Anon.objects.get(username=request.user)
        self.fields['attribte_sort_depth_char'].initial = current_anon.attribte_sort_depth_char
        self.fields['attribte_sort_depth_char'].label = False
        self.instance = current_anon



class AttributeFilterFromDateForm(forms.ModelForm):
    class Meta:
        model = Anon
        fields = ('attribute_sort_from_date_char',)
    
    def clean(self):
        cleaned_data = super(AttributeFilterFromDateForm, self).clean()
   
    def __init__(self, request, *args, **kwargs):
        super(AttributeFilterFromDateForm, self).__init__(*args, **kwargs)
        current_anon = Anon.objects.get(username=request.user)
        self.fields['attribute_sort_from_date_char'].initial = current_anon.attribute_sort_from_date_char
        self.fields['attribute_sort_from_date_char'].label = False
        self.instance = current_anon








class ExampleFilterDepthForm(forms.ModelForm):
    class Meta:
        model = Anon
        fields = ('example_sort_depth_char',)
    
    def clean(self):
        cleaned_data = super(ExampleFilterDepthForm, self).clean()
   
    def __init__(self, request, *args, **kwargs):
        super(ExampleFilterDepthForm, self).__init__(*args, **kwargs)
        current_anon = Anon.objects.get(username=request.user)
        self.fields['example_sort_depth_char'].initial = current_anon.example_sort_depth_char
        self.fields['example_sort_depth_char'].label = False
        self.instance = current_anon



class ExampleFilterFromDateForm(forms.ModelForm):
    class Meta:
        model = Anon
        fields = ('example_sort_from_date_char',)
    
    def clean(self):
        cleaned_data = super(ExampleFilterFromDateForm, self).clean()
   
    def __init__(self, request, *args, **kwargs):
        super(ExampleFilterFromDateForm, self).__init__(*args, **kwargs)
        current_anon = Anon.objects.get(username=request.user)
        self.fields['example_sort_from_date_char'].initial = current_anon.example_sort_from_date_char
        self.fields['example_sort_from_date_char'].label = False
        self.instance = current_anon








class SponsorFilterDepthForm(forms.ModelForm):
    class Meta:
        model = Anon
        fields = ('sponsor_sort_depth_char',)
    
    def clean(self):
        cleaned_data = super(SponsorFilterDepthForm, self).clean()
   
    def __init__(self, request, *args, **kwargs):
        super(SponsorFilterDepthForm, self).__init__(*args, **kwargs)
        current_anon = Anon.objects.get(username=request.user)
        self.fields['sponsor_sort_depth_char'].initial = current_anon.sponsor_sort_depth_char
        self.fields['sponsor_sort_depth_char'].label = False
        self.instance = current_anon



class SponsorFilterFromDateForm(forms.ModelForm):
    class Meta:
        model = Anon
        fields = ('sponsor_sort_from_date_char',)
    
    def clean(self):
        cleaned_data = super(SponsorFilterFromDateForm, self).clean()
   
    def __init__(self, request, *args, **kwargs):
        super(SponsorFilterFromDateForm, self).__init__(*args, **kwargs)
        current_anon = Anon.objects.get(username=request.user)
        self.fields['sponsor_sort_from_date_char'].initial = current_anon.sponsor_sort_from_date_char
        self.fields['sponsor_sort_from_date_char'].label = False
        self.instance = current_anon








class SpaceFilterDepthForm(forms.ModelForm):
    class Meta:
        model = Anon
        fields = ('space_sort_depth_char',)
    
    def clean(self):
        cleaned_data = super(SpaceFilterDepthForm, self).clean()
   
    def __init__(self, request, *args, **kwargs):
        super(SpaceFilterDepthForm, self).__init__(*args, **kwargs)
        current_anon = Anon.objects.get(username=request.user)
        self.fields['space_sort_depth_char'].initial = current_anon.space_sort_depth_char
        self.fields['space_sort_depth_char'].label = False
        self.instance = current_anon



class SpaceFilterFromDateForm(forms.ModelForm):
    class Meta:
        model = Anon
        fields = ('space_sort_from_date_char',)
    
    def clean(self):
        cleaned_data = super(SpaceFilterFromDateForm, self).clean()
   
    def __init__(self, request, *args, **kwargs):
        super(SpaceFilterFromDateForm, self).__init__(*args, **kwargs)
        current_anon = Anon.objects.get(username=request.user)
        self.fields['space_sort_from_date_char'].initial = current_anon.space_sort_from_date_char
        self.fields['space_sort_from_date_char'].label = False
        self.instance = current_anon








class PastVotesFilterDepthForm(forms.ModelForm):
    class Meta:
        model = Anon
        fields = ('past_votes_sort_depth_char',)
    
    def clean(self):
        cleaned_data = super(PastVotesFilterDepthForm, self).clean()
   
    def __init__(self, request, *args, **kwargs):
        super(PastVotesFilterDepthForm, self).__init__(*args, **kwargs)
        current_anon = Anon.objects.get(username=request.user)
        self.fields['past_votes_sort_depth_char'].initial = current_anon.past_votes_sort_depth_char
        self.fields['past_votes_sort_depth_char'].label = False
        self.instance = current_anon



class PastVotesFilterFromDateForm(forms.ModelForm):
    class Meta:
        model = Anon
        fields = ('past_votes_sort_from_date_char',)
    
    def clean(self):
        cleaned_data = super(PastVotesFilterFromDateForm, self).clean()
   
    def __init__(self, request, *args, **kwargs):
        super(PastVotesFilterFromDateForm, self).__init__(*args, **kwargs)
        current_anon = Anon.objects.get(username=request.user)
        self.fields['past_votes_sort_from_date_char'].initial = current_anon.past_votes_sort_from_date_char
        self.fields['past_votes_sort_from_date_char'].label = False
        self.instance = current_anon










class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'img', 'url2', 'body', 'spaces', 'dictionaries', 'cc')
        
    def clean(self):
        cleaned_data = super(PostForm, self).clean()
        body = cleaned_data.get('body')
        title = cleaned_data.get('title')
        spaces = cleaned_data.get('spaces')
        if not (body or title or spaces):
            raise forms.ValidationError('You need thiings')
        if len(cleaned_data.get('dictionaries')) > 5:
            raise forms.ValidationError("You can only have 5 dictionaries")
    def __init__(self, request, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        if Author.objects.get(username=request.user.username):
            self.fields['spaces'] = forms.MultipleChoiceField(choices=[(e, e) for e in Space.objects.all().filter(approved_voters=Author.objects.get(username=request.user.username)).order_by('the_space_itself__the_word_itself').values_list('the_space_itself__the_word_itself', flat=True)])
            loggedinanon = Anon.objects.get(username__username=request.user.username)
            for dic in loggedinanon.dictionaries.all():
                if dic not in loggedinanon.purchased_dictionaries.all():
                    loggedinanon.purchased_dictionaries.add(dic)
            self.fields['dictionaries'] = forms.MultipleChoiceField(choices=[(e, e) for e in Anon.objects.get(username__username=request.user.username).purchased_dictionaries.all().order_by('the_dictionary_itself').values_list('the_dictionary_itself', flat=True)])
        else:
            self.fields['spaces'] = None
            self.fields['dictionaries'] = None
    

class SpaceForm(forms.ModelForm):
    class Meta:
        model = Space
        fields = ('the_space_itself', 'sidebar', 'values', 'vision', 'mission', 'public', 'for_sale', 'free_sponsorships', 'anyone_can_edit', 'elected_sponsorships', 'elected_legislative', 'legislative_level', 'elected_administrative', 'administrative_level', 'elected_executive', 'executive_level', 'elected_judiciary', 'judiciary_level', 'successive', 'progressive', 'entry_fee', 'continuation_fee', 'invite_only', 'invite_active', 'invite_code')

    def clean(self):
        cleaned_data = super(SpaceForm, self).clean()
        the_space_itself = cleaned_data.get('the_space_itself')
        if not body:
            raise forms.ValidationError('You need a space.')

    def __init__(self, request, *args, **kwargs):
        super(SpaceForm, self).__init__(*args, **kwargs)
        loggedinuser = User.objects.get(username=request.user.username)
        loggedinauthor = Author.objects.get(username=request.user.username)
        loggedinanon = Anon.objects.get(username=loggedinuser)
        for word in Word.objects.all():
            word.get_approved
        self.fields['the_space_itself'] = forms.MultipleChoiceField(choices=[(e, e) for e in Word.objects.all().filter(ap_voters=loggedinauthor).order_by('the_word_itself').values_list('the_word_itself', flat=True)])
        


class NumStepForm(forms.ModelForm):
    class Meta:
        model = NumStep
        fields = ('from_variable', 'to_variable', 'duration', )

    def __init__(self, *args, **kwargs):
        super(NumStepForm, self).__init__(*args, **kwargs)




class ColourStepForm(forms.ModelForm):
    class Meta:
        model = ColourStep
        fields = ('from_red', 'from_green', 'from_blue', 'to_red', 'to_green', 'to_blue', 'duration', )

    def __init__(self, *args, **kwargs):
        super(ColourStepForm, self).__init__(*args, **kwargs)



class BaseTokenForm(forms.ModelForm):
    class Meta:
        model = BaseToken
        fields = ('type', 'word',)

    def __init__(self, *args, **kwargs):
        super(BaseTokenForm, self).__init__(*args, **kwargs)

     

class SpaceDataForm(forms.ModelForm):
    class Meta:
        model = Space
        fields = ('sidebar', )


class MoneroWalletForm(forms.ModelForm):
    class Meta:
        model = Anon
        fields = ('stripe_private_key', 'stripe_webhook_secret')

class AnonForm(forms.ModelForm):
    class Meta:
        model = Anon
        fields = ('username',)

class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ('file', 'public',)


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('receiver', 'encrypted_message')


