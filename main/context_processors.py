# -*- coding: utf-8 -*-
from .forms import ClientForm


def prices(request):
    form = ClientForm(request.POST or None)
    return locals()