from django import forms
from datetime import date




VISA_CHOICES = (
    (1, 'F1 - OPT'),
    (2, 'F1 - CPT'),
    (3, 'H-1B'),
    (4, 'H-4'),
    (5, 'TN'),
    (6, 'Other'),
)


class RecruiterScreenForm(forms.Form):
    today = date.today()
    day = today.strftime("%d")
    year = today.strftime("%Y")
    month = today.strftime("%m")

    todays_date = str(year + '-' + month + '-' + day)

    screen_date = forms.DateField(label='Todays Date', initial=todays_date, widget=forms.SelectDateWidget)
    candidatename = forms.CharField(max_length=100,widget= forms.TextInput(attrs={'placeholder':'Richard Eby'}))

    email = forms.CharField(required=False, widget= forms.EmailInput(attrs={'placeholder':'reby@wayfair.com'}))

    experience = forms.CharField(required=False, widget=forms.Textarea(attrs={'placeholder':'Enter Work Experience'}))

    leadership = forms.CharField(required=False, widget=forms.Textarea(attrs={'placeholder':'Enter Leadership Experience'}))

    motivation = forms.CharField(required=False, widget=forms.Textarea(attrs={'placeholder':'Enter Motivation'}))

    compensation = forms.CharField(required=False, widget=forms.Textarea(attrs={'placeholder':'Enter Comp Details'}))

    visa1 = forms.ChoiceField(choices=VISA_CHOICES)

    visa2 = forms.CharField(required=False, max_length=100, widget=forms.Textarea(attrs={'placeholder':'Other Visa'}))

    additional_comments = forms.CharField(required=False, widget=forms.Textarea(attrs={'placeholder':'Any Additional Comments'}))