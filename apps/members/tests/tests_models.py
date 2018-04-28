from django.db import IntegrityError
from django.test import TestCase

from .. models import Member
from .. exceptions import InsufficientMemberError


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

    @staticmethod
    def probability(member):
        """ Probabilidad de resultados.
            Puede ser cualquier miembro, excepto uno mismo, y el miembro
            asignado a si mismo.
            Arg:    recibe una instancia de Member
            Return: Devuelve un QuerySet con todos las intancias que tienen la
                    probabilidad de ser asignada.
        """
        assigned_member = Member.objects.get(assigned_member=member.pk)
        member_probability = Member.objects.all() \
            .exclude(pk__in=[member.pk,
                             assigned_member.pk])
        return member_probability

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

    def test_randomly_assigning_whit_3_members_raise_exception(self):
        self.generate_3_members()
        self.assertRaises(InsufficientMemberError,
                          Member.randomly_assigning)

    def test_clear_assigned(self):
        self.generate_3_members()
        luisa = Member.objects.get(name='Luisa')
        rafael = Member.objects.get(name='Rafael')
        luisa.assigned_member = rafael
        luisa.save()
        Member.clear_assigned()
        self.assertEqual(0,
                         len(Member.member_assigned()))

    def test_members_are_not_assigned_at_the_start(self):
        self.generate_3_members()
        self.generate_isabel_member()
        self.assertEqual(0,
                         len(Member.member_assigned()))

    def test_of_4_members_3_member_are_not_assigned(self):
        self.generate_3_members()
        self.generate_isabel_member()
        isabel = Member.objects.get(name='Isabel')
        luisa = Member.objects.get(name='Luisa')
        isabel.assigned_member = luisa
        isabel.save()
        self.assertIn(luisa.pk,
                      Member.member_assigned())

    def test_4_members_probability(self):
        self.generate_3_members()
        self.generate_isabel_member()
        Member.randomly_assigning()

        rafael = Member.objects.get(name='Rafael')
        luisa = Member.objects.get(name='Luisa')
        ernesto = Member.objects.get(name='Ernesto')
        isabel = Member.objects.get(name='Isabel')

        isabel_probability = self.probability(isabel)
        ernesto_probability = self.probability(ernesto)
        luisa_probability = self.probability(luisa)
        rafael_probability = self.probability(rafael)

        self.assertIn(isabel.assigned_member,
                      isabel_probability)
        self.assertIn(ernesto.assigned_member,
                      ernesto_probability)
        self.assertIn(luisa.assigned_member,
                      luisa_probability)
        self.assertIn(rafael.assigned_member,
                      rafael_probability)
