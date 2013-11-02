# -*- coding: utf-8 -*-
#: settings for liquidluck

#: site information
#: all variables can be accessed in template with ``site`` namespace.
#: for instance: {{site.name}}
site = {
    "name": "Chinese Hacking",  # your site name
    "url": "defm03.github.io",  # your site url
    # "prefix": "blog",
}

#: this config defined information of your site
#: 1. where the resources  2. how should the site be generated
config = {
    "source": "content",
    "output": "deploy",
    "static": "deploy/static",
    "static_prefix": "/static/",
    "permalink": "{{date.year}}/{{filename}}.html",
    "relative_url": False,
    "perpage": 30,
    "feedcount": 20,
    "timezone": "+01:00",
}


author = {
    "default": "defm03",
    "vars": {
        "defm03": {
            "name": 'Yang Wen-li',
            "website": "http://defm03.github.io",
            "email": "defm03@outlook.jp"
        }
    }
}

#: active readers
reader = {
    "active": [
        "liquidluck.readers.markdown.MarkdownReader",
        # uncomment to activate rST reader
        # "liquidluck.readers.restructuredtext.RestructuredTextReader",
    ],
    "vars": {}
}

#: active writers
writer = {
    "active": [
        "liquidluck.writers.core.PostWriter",
        "liquidluck.writers.core.PageWriter",
        "liquidluck.writers.core.ArchiveWriter",
        "liquidluck.writers.core.ArchiveFeedWriter",
        "liquidluck.writers.core.FileWriter",
        "liquidluck.writers.core.StaticWriter",
        "liquidluck.writers.core.YearWriter",
        "liquidluck.writers.core.CategoryWriter",
        "liquidluck.writers.core.CategoryFeedWriter",
        "liquidluck.writers.core.TagWriter",
        "liquidluck.writers.core.TagCloudWriter",
    ],
    "vars": {
        # uncomment if you want to reset archive page
        "archive_output": "archive.html",
    }
}

#: theme variables
theme = {
    "name": "cb3f20",

    # theme variables are defined by theme creator
    # you can access theme in template with ``theme`` namespace
    # for instance: {{theme.disqus}}
    "vars": {
        #"disqus": "your_short_name",
        "analytics": "UA-21475122-1",

        'navigation': [
        #    {'title': 'Home', 'link': '/'},
        #    {'title': 'Life', 'link': 'https://twitter.com/defm03'},
        #    {'title': 'Worl', 'link': 'https://github.com/defm03'}
            ['/', 'Home'],
            ['https://twitter.com/defm03', 'Twitter'],
            ['https://github.com/defm03', 'GitHub']
        ]
    }
}

#: template variables
template = {
    "vars": {},
    "filters": {},
}
