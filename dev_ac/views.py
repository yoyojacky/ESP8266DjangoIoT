# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,render_to_response
from django.http import HttpResponseRedirect,HttpResponse
import datetime
from django.shortcuts import render

# Create your views here.



def dev_list(request):


    return render(request,'dev_list.html')



def dev_heartbeat(request):

    return HttpResponse('status: ok')
