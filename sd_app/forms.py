import datetime
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import UserProfile, Transaction

# Widget to display a dropdown menu of states for transaction form.
class DateInput(forms.DateInput):
    input_type = 'date'

# Creates a form for the user to register a new user account.
class NewUserForm(UserCreationForm):
    #email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
        labels = {  'username': 'Username', 'password1': 'Password', 
                    'password2': 'Confirm Password'}    
    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)		
        if commit:
            user.save()
        return user

# Create a form for the user to update their profile information.
class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile 
        fields = ('full_name', 'address_1', 'address_2', 'city', 'state', 'zipcode')      

class BuyForm(forms.ModelForm):
   
    def clean(self):
        cleaned_data = super(BuyForm, self).clean()
        reservation_date = cleaned_data['reservation_date']
        converted_date = datetime.datetime.strptime(reservation_date, '%Y-%m-%d').date()
        # print("today: ", datetime.date.today())
        # print("reservation_date: ", reservation_date)
        # print("converted_date: ", converted_date)
        if converted_date < datetime.date.today():
            raise forms.ValidationError("Reservation date must be in the future.")
        
        return cleaned_data

    class Meta:
        model = Transaction
        fields = ('number_of_people', 'reservation_date', 'reservation_time', 'user_phone_number', 'user_email', 'preferred_payment_method')
        widgets = {'reservation_date': DateInput()}
