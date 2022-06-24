# -*- coding: utf-8 -*-
"""博客构建配置文件
"""

# For Maverick
site_prefix = "/"
source_dir = "../src/"
build_dir = "../dist/"
index_page_size = 10
archives_page_size = 20
enable_jsdelivr = {

    "enabled": True,

    "repo": "Xrz324/Xrz324.github.io@master"

}

# 站点设置
site_name = "桉陌的小站"
site_build_date = "2020-01-01T00:00+08:00"
author = "XueRunze"
email = "Xrz324@outlook.com"
author_homepage = "https://Xrz324.github.io"
description = "承蒙时光不弃，与成长不期而遇"
key_words = ['桉陌', '博客', 'Blog']
language = 'zh-CN'
nav = [
    {
        "name": "首页",
        "url": "${site_prefix}",
        "target": "_self"
    },
    {
        "name": "归档",
        "url": "${site_prefix}archives/",
        "target": "_self"
    },
    {
        "name": "关于",
        "url": "${site_prefix}about/",
        "target": "_self"
    }
]

social_links = [
    {
        "name": "Twitter",
        "url": "https://twitter.com/x32400",
        "icon": ""
    },
    {
        "name": "Telegram",
        "url": "https://t.me/X32400",
        "icon": ""
    },
    {
        "name": "Coolapk",
        "url": "http://www.coolapk.com/u/1111669",
        "icon": ""
    }
]

head_addon = r'''
<meta http-equiv="x-dns-prefetch-control" content="on">
<link rel="dns-prefetch" href="//cdn.jsdelivr.net" />
'''

footer_addon = ''

body_addon = ''
