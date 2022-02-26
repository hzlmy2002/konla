import re
from django import forms

class selectionForm(forms.Form):
    whole=forms.IntegerField(min_value=0,max_value=1,required=True)
    partial=forms.IntegerField(min_value=0,max_value=1,required=True)
    keywords=forms.IntegerField(min_value=0,max_value=1,required=True)
    refs=forms.IntegerField(min_value=0,max_value=1,required=True)
    meta=forms.IntegerField(min_value=0,max_value=1,required=True)
    metrics=forms.IntegerField(min_value=0,max_value=1,required=True)
