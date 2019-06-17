# coding: utf-8
# @Author : baoming
# @Email : 8685066@qq.com
__DATE__ = '2019/6/1 19:14'

import xadmin
from xadmin import views
import models

class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = "个人博客管理后台"
    site_footer = "blog"




class Tagadmin(object):
    list_display = ["name","get_article_nums"]
    search_fields = ['name', ]
    list_filter = ["name", ]

class Articleadmin(object):
    list_display = ["author","title","update_date"]
    search_fields = ["author","title","update_date",]
    list_filter = ["author","title","update_date",]
    style_fields = {"body": "ueditor"}


xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
xadmin.site.register(models.Tag,Tagadmin)
xadmin.site.register(models.Article,Articleadmin)