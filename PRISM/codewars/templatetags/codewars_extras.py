from django import template
import random

register = template.Library()

@register.simple_tag
def nope():
	return random.choice(
		['<img src="/media/cw2013/hypnotoad.gif" alt="ALL GLORY TO THE HYPNOTOAD" />',
		 '<img src="/media/cw2013/nope.jpg" alt="NOPE." />']
	)
