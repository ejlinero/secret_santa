from django.db import models
from .exceptions import InsufficientMemberError


class Member(models.Model):
    name = models.CharField(max_length=16)
    email = models.EmailField(unique=True)
    assigned_member = models.OneToOneField('self', 
                                            default=None, 
                                            null=True,
                                            related_name='assigned',
                                            on_delete=models.SET_NULL)

    @classmethod
    def randomly_assinging(cls):
        member_list = cls.objects.all()
        if len(member_list) < 4:
            raise InsufficientMemberError('{} miembro(s) '.format(
                str(len(member_list))))

    @classmethod
    def member_not_assingned_id_list(cls):
        member_list = cls.objects.filter(assigned_member__isnull=True) \
            .values('id')
        return list(member_list)

    def __str__(self):
        return self.name
