#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = u'Ethan Rosenthal'
SITENAME = u'Data Piques'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'

THEME='blue-penguin'

STATIC_PATHS = ['assets','CNAME']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Set the article URL
ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

RELATIVE_URLS = True
# ARTICLE_URL = '{slug}.html'
# PAGE_URL = '{slug}.html'
# PAGE_SAVE_AS = '{slug}.html'
# TAG_URL = 'tag-{slug}.html'
# TAG_SAVE_AS = 'tag-{slug}.html'
# TAGS_URL = 'tags.html'
# TAGS_SAVE_AS = 'tags.html'
# ARCHIVES_URL = 'archives.html'
# ARCHIVES_SAVE_AS = 'archives.html'

# Plugins
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['summary','liquid_tags.notebook','render_math']

# This header file is automatically generated by the notebook plugin
if not os.path.exists('_nb_header.html'):
    import warnings
    warnings.warn("_nb_header.html not found.  "
                  "Rerun make html to finalize build.")
else:
    EXTRA_HEADER = open('_nb_header.html').read().decode('utf-8')

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

PAGINATION_PATTERNS = (
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
)

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Title menu options
MENUITEMS = [('Archives', '/archives.html'),
             ('About', '/pages/about.html'),
             ('Website', 'http://www.ethanrosenthal.com')]
DISPLAY_PAGES_ON_MENU = False
