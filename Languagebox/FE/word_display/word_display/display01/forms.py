from django import forms


class inputform(forms.Form):
    len1=forms.IntegerField(min_value=3,max_value=20,label="enter the length")