#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .base import BaseTestCase
from ..models import Member
from ..serializers import MemberSerializer, AssignedMemberSerializer


class MemberSerializerTest(BaseTestCase):

    def setUp(self):
        self.generate_isabel_member()
        self.members = Member.objects.get(id=1)

    def test_serializers_a_members(self):
        serializer = MemberSerializer(self.members)
        result_json = {'id': 1,
                       'name': 'Isabel',
                       'email': 'isabel@email.com'}
        self.assertEqual(result_json, serializer.data)

    def test_serializers_a_assinged_member_is_none(self):
        serializer = AssignedMemberSerializer(self.members)
        result_json = {'assigned_member': None}
        self.assertEqual(result_json, serializer.data)

    def test_serializers_a_assinged_member_is_member(self):
        self.generate_3_members()
        rafael = Member.objects.get(name='Rafael')
        self.members.assigned_member = rafael
        self.members.save()
        serializer = AssignedMemberSerializer(self.members)
        result_json = {'assigned_member': rafael.pk}
        self.assertEqual(result_json, serializer.data)
