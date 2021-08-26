from django import forms


# Form for users seeking a caregiver 
class NewListingForm(forms.Form):
    title = forms.CharField(max_length=65) 
    category = forms.CharField(max_length=30)
    location = forms.CharField(max_length=30)
    pay = forms.IntegerField(max_value=6)
    dates = forms.CharField(max_length=30)
    description = forms.CharField(widget=forms.Textarea())
    
    
# Form for contractors seeking work 
class NewInterestForm(forms.Form):
    name = forms.CharField(max_length=30)
    email = forms.CharField(max_length=40)
    message = forms.Textarea()


# Form to create a public event
class NewEventForm(forms.Form):
    title = forms.CharField(max_length=65)
    location = forms.CharField(max_length=30)
    date = forms.CharField(max_length=30)
    description = forms.CharField(widget=forms.Textarea())
