from string import *
from re import *
from datetime import *
from collections import *
from heapq import *
from bisect import *
from copy import *
from math import *
from random import *
from statistics import *
from itertools import *
from functools import *
from operator import *
from io import *
from sys import *
from json import *
from builtins import *
import string
import re
import datetime
import collections
import heapq
import bisect
import copy
import math
import random
import statistics
import itertools
import functools
import operator
import io
import sys
import json
from typing import *

# @leet start
class Solution:
    def isValid(self, s: str) -> bool:
        set1 = set(['[', '(', '{'])
        set2 = set([']', ')', '}'])
        mapping = {']': '[', '}': '{', ')': '('}

        stackk = ['#']
        for item in s:
            if item in set1:
                stackk.append(item)
            elif item in set2:
                if mapping[item] == stackk[-1]:
                    stackk.pop()
                else:
                    return False
            elif item == '#':
                stackk.append(item)
        if stackk == ['#']:
            return True
        else:
            return False
                    
# @leet end
