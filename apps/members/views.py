#!/usr/bin/env python
# -*- coding: utf-8 -*-
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Member
from .serializers import MemberSerializer
from .exceptions import InsufficientMemberError


@api_view(['POST'])
def create(request):
    """Crea un nuevo miembro"""
    serializer = MemberSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def randomly_assigning(request):
    try:
        Member.randomly_assigning()
        return Response(status=status.HTTP_200_OK)
    except InsufficientMemberError:
        return Response(status=status.HTTP_428_PRECONDITION_REQUIRED)

