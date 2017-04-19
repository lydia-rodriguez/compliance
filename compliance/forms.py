from django import forms
from .models import ContinuingEducationLog, UserProfile
from django.contrib.auth.models import User

class CELogForm(forms.ModelForm):
	class Meta:
		model = ContinuingEducationLog
		fields = ('required_CE', 'oversight_entity', 'repeat', 'hours', 'date_completed', 'top_items_learned',)


class UserForm(forms.Form):
	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'email',)
		
		def __init__(self, *args, **kwargs):
			user = kwargs.pop('user')
			super(UserForm, self).__init__(*args, **kwargs)

		
class UserProfileForm(forms.ModelForm):
	class Meta:
		
		model = UserProfile
		fields = ('extension', 'title', 'address', 'city', 'state', 'zip', 'home_phone', 'mobile_phone', 
		'birth_date', 'emergency_contact_first_name', 'emergency_contact_last_name', 'emergency_contact_phone', 
		'emergency_contact_doctor', 'emergency_contact_doctor_phone',)
		
		def __init__(self, *args, **kwargs):
			user = kwargs.pop('user')
			super(UserProfileForm, self).__init__(*args, **kwargs)
