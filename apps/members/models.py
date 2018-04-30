#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

from django.db import models

from .exceptions import InsufficientMemberError


class Member(models.Model):
    """ Miembros que participan en el amigo invisible.
    el atributo assigned_member se refiere al miembro asignado al que le
    debemos hacer regalo.
    """
    name = models.CharField(max_length=16)
    email = models.EmailField(unique=True)
    assigned_member = models.OneToOneField('self',
                                           default=None,
                                           null=True,
                                           related_name='assigned',
                                           on_delete=models.SET_NULL)

    @classmethod
    def randomly_assigning(cls):
        """ Asignación aleatoria.
        Debe de haber al menos 4 miembros para poder hacer la asignación,
        """
        member_list = cls.objects.all()
        if len(member_list) < 4:
            raise InsufficientMemberError('{} miembro(s) '.format(
                str(len(member_list))))
        # limpia los registros.
        cls.clear_assigned()
        for member in member_list:
            # crea lista para evitar ser asignado a si mismo o a su
            # amigo invisible
            try:
                secret_santa = Member.objects.get(assigned_member=member)
            except Member.DoesNotExist:
                exclude_list = [member.pk]
            else:
                exclude_list = [member.pk, secret_santa.pk]
            exclude_list += cls.member_assigned()
            all_posible_members = cls.objects.all() \
                .exclude(pk__in=exclude_list)
            all_posible_members = cls.avoid_member_without_secret_santa(
                all_posible_members)
            member.assigned_member = random.choice(all_posible_members)
            member.save()

    @classmethod
    def avoid_member_without_secret_santa(cls, member_list):
        """ Cuando únicamente quedan dos miembros por assignar, uno de los
        miembros debe de ser ya amigo invisble de alguien, mientras que el
        otro todavía no ha participado, o sea, que no es amigo invisible de
        nadie y que está pendiente de asignar. En este caso debemos de elegir
        siempre el miembro que no ha participado todavía, en otro caso, al
        final de la asignación aleatoria, se nos quedará un miembro sin
        asignar.
        """
        if len(member_list) == 2:
            if member_list[0].assigned_member:
                return [member_list[1]]
            else:
                return [member_list[0]]
        else:
            return member_list

    @classmethod
    def member_assigned(cls):
        """ Todo los miembros que estan asignados
        """
        member_list = cls.objects.filter(assigned_member__isnull=False)
        return list(map(lambda x: x.assigned_member.pk, member_list))

    @classmethod
    def clear_assigned(self):
        """ Limpia todas las asignaciones.
        """
        assigned_list = Member.objects.filter(assigned_member__isnull=False)
        for member in assigned_list:
            member.assigned_member = None
            member.save()

    def __str__(self):
        return '{}'.format(self.name)
