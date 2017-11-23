# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class dev_mesg(models.Model):
    dev_name = models.CharField('设备名称',max_length=200,null=True)
    dev_mac = models.CharField('设备MAC地址',max_length=32,null=True)
    dev_last_time=models.DateTimeField('最后一次在线时间',auto_now = True,null=True)
    
    def __str__(self):
        return self.dev_mac
