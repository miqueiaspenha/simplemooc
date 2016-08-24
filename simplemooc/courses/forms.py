from django import forms

class ContactCourse(forms.Form):

	name = forms.CharField(label='Nome', max_length=100)
	email = forms.EmailField(label='Email')
	msg = forms.CharField(label='Mensagem', widget=forms.Textarea)