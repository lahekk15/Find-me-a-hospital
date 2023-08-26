# forms.py
from django import forms

class ReportForm(forms.Form):
    name = forms.CharField(max_length=50)
    aadhaar_number = forms.CharField(max_length=12)
    pincode = forms.CharField(max_length=10)
    mobile_number = forms.CharField(max_length=15)
    severity = forms.ChoiceField(choices=[("Low", "Low"), ("Medium", "Medium"), ("High", "High")])
    report_image = forms.ImageField()
