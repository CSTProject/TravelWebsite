from django import forms

class FForm(forms.Form):
	origin = forms.CharField()
	destination = forms.CharField()
	date = forms.CharField()
	adults = forms.CharField()
	childs = forms.CharField()
	infants = forms.CharField()
	