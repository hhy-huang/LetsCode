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
    def dfs(self, x):
        if x == len(self.numm) - 1:
            self.res.append(list(self.numm))
            return

        for i in range(x, len(self.numm)):
            self.numm[i], self.numm[x] = self.numm[x], self.numm[i]
            self.dfs(x + 1)
            self.numm[i], self.numm[x] = self.numm[x], self.numm[i]

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.numm = nums
        self.res = []
        self.dfs(0)
        print(self.res)

        return self.res

# @leet end
