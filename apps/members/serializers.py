#!/usr/bin/env python
# -*- coding: utf-8 -*-
from rest_framework import serializers
from .models import Member


class MemberSerializer(serializers.ModelSerializer):

    class Meta:
        model = Member
        fields = ('id', 'name', 'email')


class AssignedMemberSerializer(serializers.ModelSerializer):

    class Meta:
        model = Member
        fields = ('assigned_member',)