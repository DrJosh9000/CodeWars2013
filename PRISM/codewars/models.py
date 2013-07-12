from django.db import models

class War(models.Model):
	year = models.IntegerField()
	gogo = models.BooleanField()
	other_comments = models.TextField()
	def __unicode__(self):
		return 'CodeWars %d' % self.year

class Team(models.Model):
	war = models.ForeignKey(War)
	name = models.CharField(max_length=50)
	passed_open_round_at = models.DateTimeField()
	confirmed = models.BooleanField()
	def __unicode__(self):
		return self.name

class Round(models.Model):
	war = models.ForeignKey(War)
	name = models.CharField(max_length=50)
	gogo = models.BooleanField()
	url = models.CharField(max_length=50)
	def __unicode__(self):
		return '%s - %s' % (self.war, self.name)