#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.urls import path

from .views import create, randomly_assigning

urlpatterns = [
    path('create', create, name='create_member'),
    path('randomly_assigning', randomly_assigning, name='randomly_assigning')]
