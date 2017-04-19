from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from django.contrib.auth.models import Permission, User
from django.contrib.auth.decorators import login_required
from django.forms.models import inlineformset_factory
from django.core.exceptions import PermissionDenied

from .models import ContinuingEducationLog, UserProfile
from .forms import CELogForm, UserForm, UserProfileForm


def auth_error(request):
	return render(request, 'compliance/auth_error.html')

@login_required()
def home(request):
	return render(request, 'compliance/home.html')


@login_required()
def user_edit(request, username):
	if request.user.is_authenticated():
		user = get_object_or_404(UserProfile, user=request.user)
		if (request.method == "POST"):
			
			form = UserProfileForm(request.POST, instance=user)
			if (form.is_valid()):
				user = form.save(commit=False)
				user.username = request.user
				user.save()
				return redirect('user_profile', username=user.username)
		else:
			form = UserProfileForm(instance=user)
		return render(request, 'compliance/user_edit.html', {'form': form})
	else:
		return redirect('auth_error')


@login_required()
def user_list(request):
	if request.user.is_authenticated():
		users = User.objects.all()

		return render(request, 'compliance/user_list.html', {'users': users})
	else:
		return redirect('auth_error')


@login_required()
def get_user_profile(request, username):
	if request.user.is_authenticated():
		user = User.objects.get(username=request.user)
		profile = UserProfile.objects.get(user=user)
		return render(request, 'compliance/user_profile.html', {
			'user':user,
			'profile':profile
		})
	else:
		return redirect('auth_error')


@login_required()
def ce_list(request):
	if request.user.is_authenticated():

		logs = ContinuingEducationLog.objects.filter(name=request.user, date_completed__lte=timezone.now()).order_by('date_completed')
		return render(request, 'compliance/ce_list.html', {'logs': logs})
	else:
		return redirect('auth_error')


@login_required()
def ce_draft_list(request):
	if request.user.is_authenticated():
		logs = ContinuingEducationLog.objects.filter(name=request.user, date_completed__isnull=True).order_by('required_CE')
		return render(request, 'compliance/ce_draft_list.html', {'logs': logs})
	else:
		return redirect('auth_error')


@login_required()
def ce_log_detail(request, pk):
	if request.user.is_authenticated():
		log = get_object_or_404(ContinuingEducationLog, name=request.user, pk=pk)
		return render (request, 'compliance/ce_log_detail.html', {'log': log})
	else:
		return redirect('auth_error')


@login_required()
def ce_log_new(request):
	if request.user.is_authenticated():
		if (request.method == "POST"):
			form = CELogForm(request.POST)
			if (form.is_valid()):
				log = form.save(commit=False)
				log.name = request.user
				log.submit_date = timezone.now()
				log.save()
				return redirect('ce_log_detail', pk=log.pk)
		else:
			form = CELogForm()
		return render(request, 'compliance/ce_log_edit.html', {'form': form})
	else:
		return redirect('auth_error')


@login_required()
def ce_log_edit(request, pk):
	if request.user.is_authenticated():
		log = get_object_or_404(ContinuingEducationLog, name=request.user, pk=pk)
		if (request.method == "POST"):
			form = CELogForm(request.POST, instance=log)
			if (form.is_valid()):
				log = form.save(commit=False)
				log.name = request.user
				log.submit_date = timezone.now()
				log.save()
				return redirect('ce_log_detail', pk=log.pk)
		else:
			form = CELogForm(instance=log)
		return render(request, 'compliance/ce_log_edit.html', {'form': form})
	else:
		return redirect('auth_error')


@login_required()
def ce_log_remove(request, pk):
	if request.user.is_authenticated():
		log = get_object_or_404(ContinuingEducationLog, name=request.user, pk=pk)
		log.delete()
		return redirect('ce_list')
	else:
		return redirect('auth_error')