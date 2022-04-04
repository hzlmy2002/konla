from django import forms
# Written by Minyi Lei

class selectionForm(forms.Form):
    whole=forms.IntegerField(min_value=0,max_value=1,required=True)
    partial=forms.IntegerField(min_value=0,max_value=1,required=True)
    keywords=forms.IntegerField(min_value=0,max_value=1,required=True)
    refs=forms.IntegerField(min_value=0,max_value=1,required=True)
    metadata=forms.IntegerField(min_value=0,max_value=1,required=True)
    metrics=forms.IntegerField(min_value=0,max_value=1,required=True)
