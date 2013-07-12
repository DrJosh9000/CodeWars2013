from PRISM.codewars.models import War, Team, Round
from django.contrib import admin

class RoundInline(admin.TabularInline):
	model = Round
	extra = 3
	
class TeamInline(admin.TabularInline):
	model = Team
	extra = 2

class WarAdmin(admin.ModelAdmin):
	inlines = [ RoundInline, TeamInline, ]

admin.site.register(War, WarAdmin)
admin.site.register(Team)
admin.site.register(Round)

