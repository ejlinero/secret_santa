#!/usr/bin/env python
# -*- coding:utf-8 -*-


class InsufficientMemberError(Exception):
    """ Excepción para cunado no existen los suficientes miembros para
    generar parejas aleatoriamente.
    """

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)
