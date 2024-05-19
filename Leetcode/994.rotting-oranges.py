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
    def orangesRotting(self, grid: List[List[int]]) -> int:
        self.res = 0
        m = len(grid)
        n = len(grid[0])
        q = []

        bcount = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    bcount += 1
                elif grid[i][j] == 2:
                    q.append((i, j))
        while bcount > 0 and len(q) > 0:
            temp = len(q)
            self.res += 1
            for i in range(temp):
                a, b = q.pop(0)
                if a + 1 < m and grid[a + 1][b] == 1:
                    bcount -= 1
                    grid[a + 1][b] = 2
                    q.append((a + 1, b))
                if a - 1 >= 0 and grid[a - 1][b] == 1:
                    bcount -= 1
                    grid[a - 1][b] = 2
                    q.append((a - 1, b))
                if b + 1 < n and grid[a][b + 1] == 1:
                    bcount -= 1
                    grid[a][b + 1] = 2
                    q.append((a, b + 1))
                if b - 1 >= 0 and grid[a][b - 1] == 1:
                    bcount -= 1
                    grid[a][b - 1] = 2
                    q.append((a, b - 1))
        if bcount != 0:
            return -1
        else:
            return self.res

# @leet end
