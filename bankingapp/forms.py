from django import forms
from .models import Branch, District

class AccountForm(forms.Form):
    name = forms.CharField(max_length=100)
    dob = forms.DateField()
    age = forms.IntegerField()
    gender = forms.ChoiceField(choices=[('M', 'Male'), ('F', 'Female')])
    phone_number = forms.CharField(max_length=20)
    mail_id = forms.EmailField()
    address = forms.CharField(widget=forms.Textarea)
    district = forms.ModelChoiceField(queryset=District.objects.all())
    branch = forms.ModelChoiceField(queryset=Branch.objects.all())
    account_type = forms.ChoiceField(choices=[('savings', 'Savings Account'), ('current', 'Current Account')])
    materials_provide = forms.MultipleChoiceField(choices=[('debit', 'Debit Card'), ('credit', 'Credit Card'), ('cheque', 'Cheque Book')], widget=forms.CheckboxSelectMultiple)
