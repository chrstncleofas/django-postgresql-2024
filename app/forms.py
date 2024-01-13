from django import forms
from .models import Reservation


class ReservationForm(forms.ModelForm):
  class Meta:
    model = Reservation
    fields = [
      'fname',
      'lname',
      'address',
      'city',
      'province',
      'postal',
      'email',
      'phone',
      'arrival_date',
      'arrival_time',
      'departure_date',
      'departure_time',
      'number_person',
      'message'
    ]

    labels = {
      'fname': 'First Name',
      'lname': 'Last Name',
      'address': 'Address',
      'city': 'City',
      'province': 'Province',
      'postal': 'Postal  No.',
      'email': 'Email',
      'phone': 'Phone',
      'arrival_date': 'Arrival Date',
      'arrival_time': 'Arrival Time',
      'departure_date': 'Departure Date',
      'departure_time': 'Departure Time',
      'number_person': 'Number person',
      'message': 'Message',
    }
    widgets = {
      'fname': forms.TextInput(attrs={'class': 'form-control'}),
      'lname': forms.TextInput(attrs={'class': 'form-control'}),
      'address': forms.TextInput(attrs={'class': 'form-control'}),
      'city': forms.TextInput(attrs={'class': 'form-control'}),
      'province': forms.TextInput(attrs={'class': 'form-control'}),
      'postal': forms.TextInput(attrs={'class': 'form-control'}),
      'email': forms.EmailInput(attrs={'class': 'form-control'}),
      'phone': forms.NumberInput(attrs={'class': 'form-control'}),
      'arrival_date': forms.TextInput(attrs={'class': 'form-control'}),
      'arrival_time': forms.TextInput(attrs={'class': 'form-control'}),
      'departure_date': forms.TextInput(attrs={'class': 'form-control'}),
      'departure_time': forms.TextInput(attrs={'class': 'form-control'}),
      'number_person': forms.TextInput(attrs={'class': 'form-control'}),
      'message': forms.TextInput(attrs={'class': 'form-control'}),
    }
