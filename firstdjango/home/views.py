# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('warren')

def details(request):
    return HttpResponse('detail')
