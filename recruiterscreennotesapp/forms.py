from django import forms
from datetime import date




VISA_CHOICES = (
    (1, 'US Citizen'),
    (2, 'Green Card Holder'),
    (3, 'F1 - OPT'),
    (4, 'F1 - CPT'),
    (5, 'H-1B'),
    (6, 'H-4'),
    (7, 'TN'),
    (8, 'Other'),
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

    visa2 = forms.ChoiceField(choices=VISA_CHOICES)

    visa1 = forms.CharField(required=False, max_length=100, widget=forms.Textarea(attrs={'placeholder':'''Does the candidate have the unrestricted right to work indefinitely in the United States? What is the candidate's current status?"'''}))

    visa3 = forms.CharField(required=False, max_length=100, widget=forms.Textarea(attrs={'placeholder':'''If sponsorship is required, when does the candidate's current U.S. Immigration status expire?'''}))

    visa4 = forms.CharField(required=False, max_length=100, widget=forms.Textarea(attrs={'placeholder':'''If in H-1B status, how much time does he or she have remaining towards the 6 year limit?'''}))

    visa5 = forms.CharField(required=False, max_length=100, widget=forms.Textarea(attrs={'placeholder':'''If on OPT, is the candidate eligible for a STEM extension? If so, what is the expected expiration date of their STEM extension?'''}))

    visa6 = forms.CharField(required=False, max_length=100, widget=forms.Textarea(attrs={'placeholder':'''Is the candidate in the green card process? Does he or she have a certified PERM? Does he or she have an approved I-140, and have 180 days passed since approval?'''}))

    additional_comments = forms.CharField(required=False, widget=forms.Textarea(attrs={'placeholder':'Any Additional Comments'}))