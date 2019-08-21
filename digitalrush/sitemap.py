# -*- coding: utf-8 -*-
from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'monthly'

    def items(self):
        return ['main', 'development', 'promotion', 'prices', 'contacts', 'landing', 'card', 'catalog', 'online_store', 'seo', 'smm', 'context']

    def location(self, item):
        return reverse(item)