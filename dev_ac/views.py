# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,render_to_response
from django.http import HttpResponseRedirect,HttpResponse
import datetime
from django.shortcuts import render

from dev_ac.models import dev_mesg  #引用数据库
# Create your views here.


def dev_heartbeat(request):
    if request.method == 'GET': #判断请求是否是GET请求
        dev_mac = request.GET.get('mac')
        if dev_mac:
            obj,created= dev_mesg.objects.update_or_create(dev_mac=dev_mac,defaults={'dev_name':'NULL'})

    return HttpResponse('status: ok')


def dev_list(request):
    page_name = '设备列表'
    # 初始化表格表头
    table_name = '接入平台设备列表'
    table_head = []
    table_head.append('设备名称')
    table_head.append('设备MAC')
    table_head.append('最后一次在线时间')

    dev_lists = dev_mesg.objects.all().order_by('dev_last_time')
    return render(request,'dev_list.html',{'username':'question','page_name':page_name,'table_name':table_name,'table_head':table_head,\
        'table_list':dev_lists})
    return render(request,'dev_list.html')
