#!/usr/bin/python
# -*- coding: UTF-8 -*-

###############################################################
# This script is used to define binary tree for Token
# Version : 1.0.0.1
# usage :
#
#
###############################################################

from calc_token import Token
from common_info import NodeIsNotToken


class Node:
    def __init__(self, token):
        if not isinstance(token, Token):
            raise NodeIsNotToken(token)
        self.token = token
        self.left = None
        self.right = None
