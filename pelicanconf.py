#!/usr/bin/env python
# -*- coding: utf-8 -*- #

# Add the root directory to pythonpath so that we can include our own modules
import sys, os.path
sys.path.append(os.path.dirname(__file__))

# Helper methods for these settings are defined in the mtol module
from mtol import *

# The author of the website
AUTHOR = u'Linden Mackenzie-Tolhurst'
# The name of the website
SITENAME = u'Linden Mackenzie-Tolhurst'
# The domain of the website (defined in the publishconf module)
SITEURL = ''

# The base directory
BASEDIR = os.path.dirname(__file__)
# The theme directory
THEME = BASEDIR+'/theme'
# The pages directory
PAGES = BASEDIR+'/pages'

# The page files to be directly rendered
# TEMPLATE_PAGES = pages(PAGES)
TEMPLATE_PAGES = {
    PAGES+'/index.html': 'index.html',
}
TEMPLATE_PAGES[PAGES+'/README.md'] = 'README.md'
TEMPLATE_PAGES[BASEDIR+'/CNAME'] = 'CNAME'

# The templates within the theme to be directly rendered -- of which we want
# none to be as we are going to mirror the site structure 1:1 using /pages
DIRECT_TEMPLATES = []

# Timezone
TIMEZONE = 'Australia/Melbourne'
DEFAULT_LANG = u'en'

# Disable feeds
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
