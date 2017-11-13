# coding=utf-8

from django import forms
from .models import TVShow, Like


#création du formulaire:

class TVShowForm(forms.ModelForm):

    class Meta:
        """ Assigning the order of the fields"""
        model = TVShow
        fields = ("title", "director","actors", "gender", )

class LikeForm(forms.ModelForm):

    class Meta:
        model=Like
        fields=('add',)


