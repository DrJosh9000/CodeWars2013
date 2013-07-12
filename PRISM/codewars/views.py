from datetime import datetime
from django import forms
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from models import War, Team

class BackdoorLoginForm(forms.Form):
	team_name = forms.CharField(max_length=50)
	password = forms.CharField(max_length=50, widget=forms.PasswordInput)
	def clean_password(self):
		pword = self.cleaned_data['password']
		if pword.upper() == 'TEAANDBEX':
			return pword
		else:
			raise forms.ValidationError('Incorrect password!')

def war_gogo_or_404():
	war = get_object_or_404(War,year=2013)
	if war.gogo:
		return war
	else:
		raise Http404
		
def round_gogo_or_404(war, url):
	thisround = war.round_set.filter(url=url)[0]
	if thisround and thisround.gogo:
		return thisround
	else:
		raise Http404

def index(request):
	war = get_object_or_404(War,year=2013)
	return render_to_response('codewars2013/index.html', 
	{ 
		'rounds': war.round_set.filter(gogo=True) if war.gogo else []
	})

def time(request):
	war = war_gogo_or_404()
	thisround = round_gogo_or_404(war, '/time')
	return render_to_response('codewars2013/time.html', {})
	
def chemtrails(request):
	war = war_gogo_or_404()
	thisround = round_gogo_or_404(war, '/chemtrails')
	return render_to_response('codewars2013/chemtrails.html', {})

def illuminati(request):
	war = war_gogo_or_404()
	thisround = round_gogo_or_404(war, '/illuminati')
	return render_to_response('codewars2013/illuminati.html', {})

def backdoor(request):
	war = war_gogo_or_404()
	thisround = round_gogo_or_404(war, '/time') #First round should be gogo
	if request.method == 'POST': 
		form = BackdoorLoginForm(request.POST) 
		if form.is_valid(): 
			team = Team(war=war, 
				name=form.cleaned_data['team_name'], 
				passed_open_round_at=datetime.now(), 
				confirmed=False)
			team.save()
			return render_to_response('codewars2013/success.html', {})
	else:
		form = BackdoorLoginForm() 
	return render_to_response('codewars2013/backdoor.html', {
		'form': form,
	}, context_instance=RequestContext(request))
	
def leaderboard(request):
	war = war_gogo_or_404()
	return render_to_response('codewars2013/leaderboard.html', 
	{
		'teams_confirmed': war.team_set.filter(confirmed=True),
		'other_comments': war.other_comments,
	})
	
def credits(request):
	return render_to_response('codewars2013/credits.html', {})