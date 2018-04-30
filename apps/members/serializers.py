#!/usr/bin/env python
# -*- coding: utf-8 -*-
from rest_framework import serializers
from .models import Member


class MemberSerializer(serializers.ModelSerializer):
    """ Serealizador para crear miembros
    """

    class Meta:
        model = Member
        fields = ('id', 'name', 'email')


class AssignedMemberSerializer(serializers.ModelSerializer):
    """ Serializador para mostrar el miembro asociado.
    """

    class Meta:
        model = Member
        fields = ('assigned_member',)
