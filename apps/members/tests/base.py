#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.test import TestCase

from ..models import Member


class BaseTestCase(TestCase):

    @staticmethod
    def generate_3_members():
        Member.objects.create(
            name='Rafael',
            email='rafael@email.com')
        Member.objects.create(
            name='Luisa',
            email='luisa@email.com')
        Member.objects.create(
            name='Ernesto',
            email='ernesto@email.com')

    @staticmethod
    def generate_isabel_member():
        Member.objects.create(
            name='Isabel',
            email='isabel@email.com')

    @staticmethod
    def probability(member):
        """ Probabilidad de resultados.
            Puede ser cualquier miembro, excepto uno mismo, y el miembro
            asignado a si mismo.
            Arg:    recibe una instancia de Member
            Return: Devuelve un QuerySet con todos las instancias que tienen la
                    probabilidad de ser asignada.
        """
        try:
            secret_santa = Member.objects.get(assigned_member=member.pk)
        except Member.DoesNotExist:
            exclude_list = [member.pk]
            secret_santa = 'No tiene'
        else:
            exclude_list = [member.pk, secret_santa.pk]
        member_probability = Member.objects.all().exclude(pk__in=exclude_list)
        return member_probability