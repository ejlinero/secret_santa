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
            # asignado
            if member.assigned_member:
                exclude_list = [member.pk, member.assigned_member.pk]
            else:
                exclude_list = [member.pk]
            exclude_list += cls.member_assigned()
            all_posible_members = cls.objects.all() \
                .exclude(pk__in=exclude_list)
            member.assigned_member = random.choice(all_posible_members)
            member.save()

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