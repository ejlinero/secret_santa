from django.db import models
from .exceptions import InsufficientMemberError


class Member(models.Model):
    name = models.CharField(max_length=16)
    email = models.EmailField(unique=True)

    @classmethod
    def randomly_assinging(cls):
        member_list = cls.objects.all()
        if len(member_list) < 4:
            raise InsufficientMemberError('pass')

    def __str__(self):
        return self.name