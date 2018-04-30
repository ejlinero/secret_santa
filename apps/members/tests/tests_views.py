#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status

from .base import BaseTestCase
from ..models import Member
from ..serializers import MemberSerializer, AssignedMemberSerializer


client = Client()


class CreateNewMemberTest(TestCase):

    def setUp(self):
        self.valid_member = {
            'name': 'Joaquin',
            'email': 'joaquin@email.com'
        }
        self.invalid_email = {
            'name': 'Joaquin2',
            'email': 'joaquin'
        }
        self.invalid_name = {
            'name': '',
            'email': 'joaquin@email.com'
        }

    def test_create_valid_member(self):
        members_initial = Member.objects.all().count()
        response = client.post(
            reverse('create_member'),
            data=json.dumps(self.valid_member),
            content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(members_initial + 1, Member.objects.all().count())

    def test_invalid_name_member(self):
        members_initial = Member.objects.all().count()
        response = client.post(
            reverse('create_member'),
            data=json.dumps(self.invalid_name),
            content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(members_initial, Member.objects.all().count())

    def test_invalid_email_member(self):
        members_initial = Member.objects.all().count()
        response = client.post(
            reverse('create_member'),
            data=json.dumps(self.invalid_email),
            content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(members_initial, Member.objects.all().count())


class RandomlyAssigningTest(BaseTestCase):

    def setUp(self):
        self.generate_3_members()

    def test_randomly_assigning_whit_3_members_return_http_400(self):
        response = client.post(
            reverse('randomly_assigning'),
            data=json.dumps({'key':'value'}),
            content_type='application/json')
        self.assertEqual(response.status_code,
                         status.HTTP_428_PRECONDITION_REQUIRED)

    def test_randomly_assigning_whit_4_members_return_http_200(self):
        self.generate_isabel_member()
        response = client.post(
            reverse('randomly_assigning'),
            data=json.dumps({'value':'value'}),
            content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetAssignedMemberTest(BaseTestCase):

    def setUp(self):
        self.generate_isabel_member()
        self.isabel = Member.objects.get(pk=1)

    def test_get_assigned_member(self):
        response = client.get(
            reverse('get_assigned_member', kwargs={'pk': 1}))
        serializer = AssignedMemberSerializer(self.isabel)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_assigned_member_after_assigning(self):
        self.generate_3_members()
        rafael = Member.objects.get(name='Rafael')
        self.isabel.assigned_member = rafael
        self.isabel.save()

        response = client.get(
            reverse('get_assigned_member', kwargs={'pk': 1}))
        serializer = AssignedMemberSerializer(self.isabel)

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_member_not_found(self):
        response = client.get(
            reverse('get_assigned_member', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


