# Atcoder Regular Contest 113 B-A^B^C

https://atcoder.jp/contests/arc113/tasks/arc113_b

## Problem Statement：

Given positive integers A,B,C, find the digit at the ones place in the decimal notation of $A^{B^C}$.

## Constraints:

1 <= A,B,C <= $10^9$
A,B,C are integers.

## Inputs:

Input is given from Standard Input in the following format:

    A B C

## Outputs:

Print the digit at the one's place in the decimal notation of $A^{B^C}$

## Sample Input:

    3141592 6535897 9323846

## Sample Output:

    2

## 分析：

数据很大，思路首先是使用快速幂，然后思考一下，输出的是结果%10的结果，而这个结果只与A的个位有关。

然后```A % 10```的幂也是循环的，发现对于0、1、5、6这样的值直接输出就可以，因为不管```B^C```为多少，都不会改变。然后4、9这样值循环大小为2，其余的为4。把循环大小作为```B^C```的模，这样能最好得优化。

**坑**：```B^C```取模后会=0，这种情况要让他们恢复相应的循环的大小，因为A的0次幂肯定是0嘛。。要做这样一个判断。

代码：
```cpp
#include<iostream>
#include<iostream>
#include<string>
#include<cstring>
#include<algorithm>
#include<cmath>
#include<vector>
#include<cstdio>

using namespace std;

long long a,b,c;
long long A;


long long quick_pow(long long base,long long pow)
{
    long long temp = 0;
    if(A == 4 || A == 9)
    {
        temp = 2;
    }
    else
    {
        temp = 4;
    }
    long long ans = 1;
    while(pow)
    {
        if(pow & 1)
        {
            ans = ans * base % temp;
        }
        base = base * base % temp;//caculate the x^n
        pow >>= 1;
    }
    if(ans == 0)
    {
        if(A == 4 || A == 9)
        {
            ans = 2;
        }
        else
        {
            ans = 4;
        }
    }
    return ans;
}

long long quick_pow2(long long base, long long p, long long m)
{
    long long ans = 1 % m;
    while(p)
    {
        if(p & 1)
        {
            ans = ans * base % m;
        }
        base = base * base % m;
        p >>= 1;
    }
    return ans;
}

int main()
{
    cin>>a>>b>>c;
    A = a % 10;
    if(A == 0 || A == 5 || A == 6 || A == 1)
    {
        cout<<A<<endl;
    }
    else
    {
        long long p = quick_pow(b, c);
        cout<<quick_pow2(a, p, 10)<<endl;
    }
    return 0;
}
```
