from django import forms
from django.db import models

from .models import App, ApplicationLog, NetworkLog, Incident
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('password', 'email', 'first_name', 'last_name')

class AppForm(forms.ModelForm):

    class Meta:
        model = App
        #fields = ('login', 'recharge', 'wallet', 'earn', 'gem',)
        fields = ('login', 'recharge', 'wallet', 'earn', 'gem','remark',)

    remark = forms.CharField(
        max_length=254,
        widget=forms.TextInput(attrs={'class': "input-sm"}),
    )


class ApplicationLogForm(forms.ModelForm):

    class Meta:
        model = ApplicationLog
        fields = ('info', 'warn', 'cs','error','remark')

    remark = forms.CharField(
        max_length=254,
        widget=forms.TextInput(attrs={'class': "input-sm"}),
    )


class NetworkLogForm(forms.ModelForm):
    class Meta:
        model = NetworkLog
        fields = ('WAN_in', 'WAN_out','port15_in','port15_out','port16_in','port16_out','p2p_in','p2p_out','wfd_in','wfd_out','remark')

    remark = forms.CharField(
        max_length=254,
        widget=forms.TextInput(attrs={'class': "input-sm"}),
    )


class IncidentForm(forms.ModelForm):
    class Meta:
        model = Incident
        fields = ('title','description','escalated_to', 'document', 'category')

    description = forms.CharField(widget=forms.Textarea(attrs={'width':"100%", 'cols' : "100%", 'rows': "4", }))

    title = forms.CharField(
        max_length=254,
        widget=forms.TextInput(attrs={'width':"100%", 'cols' : "100%", 'class': "input-sm"}),
    )
