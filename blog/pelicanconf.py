#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Sam Whitney'
SITENAME = 'bad ideas'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Trello: MK2 VR6 Tasks', 'https://trello.com/b/lalq28zE/mk2-jetta-vr6-swap-tasks'),
         ('Trello: MK2 VR6 Parts & Tools', 'https://trello.com/b/aZhuJZH4/mk2-jetta-vr6-swap-parts-tools'),)

# Social widget
SOCIAL = (('Instagram', 'https://instagram.com/wamshitney/'),
          ('GitHub', 'https://github.com/swhi3635'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

THEME = 'pelican-sober'
PELICAN_SOBER_ABOUT = 'A collection of personal projects that usually involve poor financial decisions and other mistakes.'
