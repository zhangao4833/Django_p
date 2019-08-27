# -*- coding: utf-8 -*-
from xadmin import views
import xadmin
class BaseSetting:
    enable_themes = True  # 开启主题功能
    use_bootswatch = True

xadmin.site.register(views.BaseAdminView, BaseSetting)