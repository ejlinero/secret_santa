#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .base import BaseTestCase
from ..models import Member
from ..serializers import MemberSerializer


class MemberSerializerTest(BaseTestCase):

    def test_serializers_a_members(self):
        self.generate_isabel_member()
        members = Member.objects.get(id=1)
        serializer = MemberSerializer(members)
        result_json = {'id': 1,
                       'name': 'Isabel',
                       'email': 'isabel@email.com',
                       'assigned_member': None}
        self.assertEqual(result_json, serializer.data)
