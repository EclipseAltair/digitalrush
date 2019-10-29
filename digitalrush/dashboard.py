"""
This file was generated with the customdashboard management command and
contains the class for the main dashboard.

To activate your index dashboard add the following to your settings.py::
    GRAPPELLI_INDEX_DASHBOARD = 'digitalrush.dashboard.CustomIndexDashboard'
"""

from django.utils.translation import ugettext_lazy as _
from django.urls import reverse

from grappelli.dashboard import modules, Dashboard
from grappelli.dashboard.utils import get_admin_site_name


class CustomIndexDashboard(Dashboard):
    """
    Custom index dashboard for www.
    """

    def init_with_context(self, context):
        site_name = get_admin_site_name(context)

        self.children.append(modules.Group(
            _('Услуги'),
            column=1,
            collapsible=True,
            children=[
                modules.AppList(
                    _('Разработка'),
                    column=1,
                    collapsible=False,
                    models=('landing.models.*','card.models.*','catalog.models.*','online_store.models.*'),
                ),
                modules.AppList(
                    _('Продвижение'),
                    column=1,
                    collapsible=False,
                    models=('seo.models.*','smm.models.*','context.models.*'),
                )
            ]
        ))

        self.children.append(modules.Group(
            _('Администрирование'),
            column=2,
            collapsible=True,
            children = [
                modules.AppList(
                    _('Администрация'),
                    column=2,
                    collapsible=False,
                    models=('django.contrib.*',),
                ),
                modules.AppList(
                    _('Главная'),
                    column=2,
                    collapsible=False,
                    models=('main.models.*',),
                )
            ]
        ))
