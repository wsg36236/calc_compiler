#!/usr/bin/python
# -*- coding: UTF-8 -*-

###############################################################
# This script is used to define stack
# Version : 1.0.0.1
# usage :
#
#
###############################################################


class Stack:
    def __init__(self):
        self.__array = []

    def __str__(self):
        return str(self.__array)

    def push(self, value):
        self.__array.append(value)

    def pop(self):
        return self.__array.pop()

    def size(self):
        return len(self.__array)

    def is_empty(self):
        return len(self.__array) == 0
