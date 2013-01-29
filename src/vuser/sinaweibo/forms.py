# -*- coding: utf-8 -*-
'''
Created on 2013-1-15

@author: tonycao
'''
from django import forms


class UserForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput,label='')