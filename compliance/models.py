from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class ContinuingEducationLog(models.Model):

	RENEWAL_CHOICES = (
			('Biannually', 'Biannually'),
			('Yearly', 'Yearly'),
			('Every 2 years', 'Every 2 years'),
			('Every 3 years', 'Every 3 years'),
			('Every 4 years', 'Every 4 years'),
			('Every 5 years', 'Every 5 years'),
			('Other', 'Other'),
		)
		
	name = models.ForeignKey('auth.User')
	required_CE = models.CharField(max_length=200)
	oversight_entity = models.CharField(max_length=200)
	repeat = models.CharField(max_length=200, choices=RENEWAL_CHOICES)
	hours = models.CharField(max_length=200)
	date_completed = models.DateField(blank=True, null=True)
	top_items_learned = models.TextField(blank=True)
	
	def submit(self):
		self.submit_date = timezone.now()
		self.save()
		
	def __str__(self):
		return self.required_CE


class UserProfile(models.Model):
	user = models.OneToOneField(User, related_name='user', on_delete=models.CASCADE)
	extension = models.CharField(max_length=8)
	title = models.CharField(max_length=200)
	address = models.CharField(max_length=300, blank=True)
	city = models.CharField(max_length=50, blank=True)
	state = models.CharField(max_length=25, blank=True)
	zip = models.CharField(max_length=10, blank=True)
	home_phone = models.CharField(max_length=15, blank=True)
	mobile_phone = models.CharField(max_length=15, blank=True)
	birth_date = models.DateField(null=True, blank=True)
	emergency_contact_first_name = models.CharField(max_length=100, blank=True)
	emergency_contact_last_name = models.CharField(max_length=100, blank=True)
	emergency_contact_phone = models.CharField(max_length=15, blank=True)
	emergency_contact_doctor = models.CharField(max_length=100, blank=True)
	emergency_contact_doctor_phone = models.CharField(max_length=15, blank=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


def create_profile(sender, **kwargs):
    user = kwargs["instance"]
    if kwargs["created"]:
        user_profile = UserProfile(user=user)
        user_profile.save()
post_save.connect(create_profile, sender=User)

