# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import socket

from django.shortcuts import render
from django.http import HttpResponse

def homePageView(request):
    text = 'We are serving from ' + display()
    return HttpResponse(text)

def display():
    return(socket.gethostname())
# Create your views here.
