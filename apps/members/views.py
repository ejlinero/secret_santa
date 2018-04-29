#!/usr/bin/env python
# -*- coding: utf-8 -*-
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Member
from .serializers import MemberSerializer


@api_view(['POST'])
def create(request):
    serializer = MemberSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
