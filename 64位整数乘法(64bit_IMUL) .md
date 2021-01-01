# 64位整数乘法

64位整数乘法即两个10的18次幂的整数相乘，由于不存在128位的整数类型，因此需要进行其它的处理方式。

类似于快速幂的思想，对于：

<a><img src="https://latex.codecogs.com/png.latex?a\times&space;b&space;~mod~&space;m" title="a\times b ~mod~ m" /></a>

对***b***同样表示成若干指数不重复的2的次幂的和：

<a><img src="https://latex.codecogs.com/png.latex?b&space;=&space;c_{k-1}2^{k-1}&space;&plus;&space;c_{k-2}2^{k-2}&space;&plus;..&plus;c_02^0" title="b = c_{k-1}a^{k-1} + c_{k-2}a^{k-2} +..+c_0a^0" /></a>

在这样的展开式中，我们把***a*** 乘进去再取模,并且由于 ***c***非0即1:

<a><img src="https://latex.codecogs.com/png.latex?ans&space;=&space;\{c_{k-1}(a\cdot&space;2^{k-1})mod~m&plus;c_{k-2}(a\cdot&space;2^{k-2})mod~m~&plus;..&plus;c_{0}(a\cdot&space;2^{0})mod~m~\}mod~m" title="ans = \{c_{k-1}(a\cdot 2^{k-1})mod~m+c_{k-2}(a\cdot 2^{k-2})mod~m~+..+c_{0}(a\cdot 2^{0})mod~m~\}mod~m" /></a>

在计算每一项时，都是在前一项求得结果的基础上乘2再取模就可以得到，这样每一层的计算结果都不会爆64位的范围。

代码：

```cpp
#include<iostream>
#include<string>
#include<cstring>
#include<algorithm>
#include<cmath>

using namespace std;

long long big_multi(long long a,long long b,long long m)
{
    long long ans = 0;
    while(b)
    {
        if(b & 1)
        {
            ans = (ans + a) % m;//b的拆项
        }
        a = a * 2 % m;
        b >>= 1;
    }
    return ans;
}

int main()
{
    long long a,b,m;

    cin>>a>>b>>m;
    cout<<big_multi(a,b,m)<<endl;
    return 0;
}
```
