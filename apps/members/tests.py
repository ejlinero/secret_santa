from django.test import TestCase

from .models import Member

class MemberTestCase(TestCase):

	def test_create_member(self):
		all_old_members = Member.objects.all().count()
		Member.objects.create(
			name='Emilio',
			email='emilio@email.com') 
		self.assertEqual(all_old_members + 1, Member.objects.all().count())

