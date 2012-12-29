#!/usr/bin/env python
# -*- coding: utf-8 -*- #

# Calculated settings are maintained within the mtol module#
import sys
sys.path.append('.')
import mtol

AUTHOR = u'Linden Mackenzie-Tolhurst'
SITENAME = u'Linden Mackenzie-Tolhurst'
SITEURL = ''

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Blogroll
LINKS =  (('Pelican', 'http://docs.notmyidea.org/alexis/pelican/'),
          ('Python.org', 'http://python.org'),
          ('Jinja2', 'http://jinja.pocoo.org'),
          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Direct templates
# -- only direct render files which have a base template in our custom implementation

THEME = mtol.THEME
DIRECT_TEMPLATES = mtol.DIRECT_TEMPLATES
