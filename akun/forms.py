from django import forms

from .models import NewAkun
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class FormAkun(UserCreationForm):
    class Meta:
        model = NewAkun
        fields = ['email','nama','no_hp','password1','password2']
        
    def clean(self):
        cd = self.cleaned_data
        if cd.get('password1') != cd.get('password2'):
            self.add_error('password2', "Konfirmasi password tidak sama!")
        if NewAkun.objects.filter(email=cd.get('email')).exists():
            self.add_error('email', "Email ini sudah pernah digunakan!")
        return cd
    
    def __init__(self, *args, **kwargs):
            super(FormAkun, self).__init__(*args, **kwargs)
            self.fields['email'].widget.attrs.update({'placeholder': 'Masukkan Email ','class':'form-control',})
            self.fields['nama'].widget.attrs.update({'placeholder': 'Masukkan Nama Anda ','class':'form-control',})
            self.fields['no_hp'].widget.attrs.update({'placeholder': 'Masukkan No. Handphone','class':'form-control',})
            self.fields['password1'].widget.attrs.update({'placeholder': 'Masukkan Password ','class':'form-control',})
            self.fields['password2'].widget.attrs.update({'placeholder': 'Konfirmasi Password ','class':'form-control',})
