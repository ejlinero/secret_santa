#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.urls import path

from .views import create

urlpatterns = [
    path('create', create, name='create_member')]
