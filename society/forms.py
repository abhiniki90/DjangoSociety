from django import forms
from .models import UserProfile

class ImageForm(forms.ModelForm):
	about_me = forms.CharField(required=False)
	birth_date = forms.DateField(required=False)
	first_name = forms.CharField(required=False)
	last_name = forms.CharField(required=False)
	username = forms.CharField(required=False)
	image = forms.ImageField(required=False)
	class Meta:
		model = UserProfile
		fields= ('about_me', 'birth_date', 'fav_movies', 'first_name', 'last_name', 'username', 'image')
