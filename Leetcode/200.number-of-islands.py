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
    def dfs(self, grid, i, j, m, n):
        if i < 0 or i >= m or j < 0 or j >= n:
            return
        if grid[i][j] == "2" or grid[i][j] == "0":
            return

        grid[i][j] = "2"
        self.dfs(grid, i - 1, j, m, n)
        self.dfs(grid, i + 1, j, m, n)
        self.dfs(grid, i, j - 1, m, n)
        self.dfs(grid, i, j + 1, m, n)

    def numIslands(self, grid: List[List[str]]) -> int:
        self.res = 0
        m = len(grid)
        n = len(grid[0]) 
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    self.res += 1
                    self.dfs(grid, i, j, m, n)
        return self.res

# @leet end
