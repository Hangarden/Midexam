from django import forms
from usermgmt.models import Music

class MusicForm(forms.ModelForm):
    class Meta:
        model = Music
        fields = '__all__'
        #field = ['salutation', 'first_name', 'last_name', 'email']
