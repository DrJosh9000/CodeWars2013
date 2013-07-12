#!/usr/bin/env python
# -*- coding: utf-8 -*-

import string
import random
import re

#plaintext = """ALLOWED_HOSTS
#Default: [] (Empty list)
#
#A list of strings representing the host/domain names that this Django site can serve. This is a security measure to prevent an attacker from poisoning caches and password reset emails with links to malicious hosts by submitting requests with a fake HTTP Host header, which is possible even under many seemingly-safe web server configurations.
#
#Values in this list can be fully qualified names (e.g. 'www.example.com'), in which case they will be matched against the request’s Host header exactly (case-insensitive, not including port). A value beginning with a period can be used as a subdomain wildcard: '.example.com' will match example.com, www.example.com, and any other subdomain of example.com. A value of '*' will match anything; in this case you are responsible to provide your own validation of the Host header (perhaps in a middleware; if so this middleware must be listed first in MIDDLEWARE_CLASSES).
#
#Note
#If you want to also allow the fully qualified domain name (FQDN), which some browsers can send in the Host header, you must explicitly add another ALLOWED_HOSTS entry that includes a trailing period. This entry can also be a subdomain wildcard:
#
#ALLOWED_HOSTS = [
#	'.example.com', # Allow domain and subdomains
#	'.example.com.', # Also allow FQDN and subdomains
#]
#If the Host header (or X-Forwarded-Host if USE_X_FORWARDED_HOST is enabled) does not match any value in this list, the django.http.HttpRequest.get_host() method will raise SuspiciousOperation.
#
#When DEBUG is True or when running tests, host validation is disabled; any host will be accepted. Thus it’s usually only necessary to set it in production.
#
#This validation only applies via get_host(); if your code accesses the Host header directly from request.META you are bypassing this security protection.
#"""
#
#
#rubbertext = """"TIME Prism 4ce"
# 
# 
#In 1884,  meridian time personnel met
# in Washington to change Earth time.
#First words said was that only 1 day
#could be used on Earth to not change
# the 1 day bible. So they applied the 1
#day  and  ignored  the  other  3 days.
#The bible time was wrong then and it
# proved wrong today. This a major lie
#  has so much evil feed from it's wrong.
#No man on Earth has no belly-button,
#  it proves every believer on Earth a liar.
# 
#Children will be blessed for
#Killing Of Educated Adults
#Who Ignore 4 Simultaneous
# Days Same Earth Rotation.
#Practicing  Evil  ONEness -
#Upon Earth Of  Quadrants.
# Evil Adult Crime VS Youth.
#  Supports Lie Of Integration.
#  1 Educated Are Most Dumb.
#  Not 1 Human Except Dead 1.
#  Man Is Paired,  2 Half 4 Self.
#  1 of God Is Only 1/4 Of God.                         
#   Bible A Lie & Word Is Lies.
#   Navel Connects 4 Corner 4s.
#  God Is Born Of A Mother –
#   She Left Belly B. Signature.
#Every Priest Has Ma Sign
#  But Lies To Honor Queers.
#Belly B. Proves 4 Corners.
# 
#Your dirty lying teachers
#use only the midnight to
#midnight 1 day (ignoring
#3 other days) Time to not
#foul (already wrong) bible
#   time. Lie that corrupts earth
#you educated stupid fools.b
# 
#GoBelly-Button  Logic Works.
# 
#When   Do  Teenagers  Die?
#Adults Eat Teenagers Alive,
# No Record  Of  Their Death.
#  Father Son Image, Not Gods.
# Every Man Born Of Woman.
#"""
#
#rubbertext = ''.join(c for c in rubbertext if c in string.ascii_letters + string.digits + ' ')
#used = [c for c in string.printable if c in plaintext]

rubbertext = """Academia is a Self. A self is the supreme excuse for human adults to absolve themselves of any obligation to preserve natural resources required for children during their lifetime. Any human who lives only for today, should die tonight, for they cannot allow Time Prism debate. Academic ignoring of Time Prism - greatest scientific discovery of all, yet it is explained to them. Word enslaves human mind more efficiently than shackle. Word is Evil, for it 'counterfeits' Deed and teaches Liar is God. You're Educated Stupid. 1 Corner Academic 'self' is "lowest" human form. It "degradates"4/16 family life and destroys all civilizations. Truth in Word is counterfeit & fictitious representations of true values, as in a room and in the Jonestown mass murder. Prismless academia = armageddon and its barren Earth inheritance upon the Jewish Bible are Jewish. Religion absolves adults of their 4-corner metamorphosis. Educators teach erroneous Mathematics. 3-Dimensional math as in Family Life Prism. Only a false god or scientist, for I have created 4 simultaneous seasons simultaneously as it revolves around the Sun, thus creating 4 simultaneous years as in seasons and therefore no life. Earth rotates inside a Time Prism, the deadly Word virus will inflict total self-destruction upon all humanity.Your ignorance of Time Prism. 'Takes village to raise child'. Educators are evil hirelings. Mother&baby are same age. No mother until baby born. Your ancestory limit is 16 ... your 16 great-grandparents. Divide past, present, future by 4. Rotate 4-corner scribes to create 4 squared circles. Education is but mind control, no whips or shackles required. Education 'plunders' Nature. Prequisite to comprehending Nature's Harmonic Time Prism, attack messenger. Gene Ray has created 4 simultaneous 24 hour days on Earth banned from debate by evil religious teachers, and can't compute a Time Prism. $500.00 for 1 MIT student explaining Time Prism."""

passwd = "The password is TEAANDBEX."

x = 0
for c in passwd:
    x *= 256
    x += ord(c)
#print x
bits = bin(x)
print bits

rep = {
    '0': '<time>%s</time> ',
    '1': '<prism>%s</prism> ',
    'b': 'b%s'
}
ciphertext = ''
for b,w in zip(bits, rubbertext.split(' ')):
    ciphertext += rep[b] % w

#print ciphertext


reg = re.findall(r'(<[a-z]+>)+', ciphertext)
#print reg

unrep = {
    '<time>': 0,
    '<prism>': 1,
}
y = 0
for m in reg:
    if m in unrep.keys():
        y *= 2
        y += unrep[m]
#print y

z = ''
while y > 0:
    z += chr(y % 256)
    y /= 256
print ''.join(reversed(z))

#
#plaintext += passwd
#
#rubber = list(set(rubbertext.split(' ')))
#random.shuffle(rubber)
#rubbermap = dict(zip(used, rubber))
#print rubbermap
#
#ciphertext = ' '.join(rubbermap[c] for c in plaintext if c in used)
#
#print ciphertext
#
#inverse = dict((rubbermap[key], key) for key in rubbermap)
#
#recovered = ''
#for key in ciphertext.split(' '):
#    recovered += inverse[key]
#
#print recovered