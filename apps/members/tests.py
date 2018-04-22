from django.db import IntegrityError
from django.test import TestCase

from .models import Member
from .exceptions import InsufficientMemberError

class MemberTestCase(TestCase):
    
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

    def test_create_member(self):
        all_old_members = Member.objects.all().count()
        Member.objects.create(
            name='Emilio',
            email='emilio@email.com') 
        self.assertEqual(all_old_members + 1, Member.objects.all().count())

    def test_repeated_email(self):
        self.generate_isabel_member()
        self.assertRaises(IntegrityError,
            Member.objects.create,
            name='isabel',
            email='isabel@email.com')

    def test_randomly_assinging_whit_3_members_raise_exception(self):
        self.generate_3_members()
        self.assertRaises(InsufficientMemberError,
                          Member.randomly_assinging)