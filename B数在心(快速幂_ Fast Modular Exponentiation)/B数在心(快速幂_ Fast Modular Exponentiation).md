# BJTU1878 B数在心 
1000ms 256MB

### 题目：

相传在某个遥远的西方国度，有位强大而美丽的亚瑟王saber。

在某一天，她突发奇想，希望办成一个超大型的蒙面舞会。

她一口气邀请了N位男士和M位女士，由于蒙着面，就无法自行挑选合适的舞伴了。

那么，如何合理地分配每位女士的舞伴成为了困难的问题。

不过还好的是，亚瑟王统计了每位女士的对舞伴气质和形象的最低要求。

并且她成功地把这个标准给数值化了，并将之称为B数。

B数的计算非常简单，如果第i位男士拥有Ai枚圣晶石，那么这位男士的B数就是Ai的Ai次方mod D。

（不一定拥有的圣晶石更多就心里会有更多的B数）

现在，亚瑟王希望你可以帮她计算下最多究竟可以在蒙面舞会上配成多少对舞伴？

如果你可以给出正确的结果，那么她可以答应你女装参加这次的蒙面舞会！

### 输入数据：

第一行一个正整数 𝑇 (1≤𝑇≤10)，表示有 𝑇 组数据。

对于每组数据：

第一行为三个整数 𝑁，𝑀，𝐷 (1≤𝑁，𝑀，𝐷≤200000) ，其中 𝑁 和 𝑀 分别表示蒙面舞会一共来了多少位男士和多少位女士，𝐷 表示计算B数过程中的模数。

接下来 𝑁 行每行一个整数 𝐴𝑖 (1≤𝐴𝑖≤200000)，表示编号 𝑖 的男士拥有多少枚圣晶石。

接下来 𝑀 行每行一个整数 𝐵𝑖 (1≤𝐵𝑖≤200000) 为编号第i的女士对舞伴心里的B数的最低要求。

### 输出数据：

对于每组数据，输出一行：为一个整数，表示蒙面舞会上最多可以配成多少对舞伴。

### 样例输入：

    1
    3 27
    1
    2
    3
    1
    4
    27

### 样例输出 ：

    2

### 样例说明：

根据B数计算公式可以算出三位男士的B数分别为1，4，0。

其中B数为1，4的男士可以匹配女士的最低要求1，4，而最低要求27的女士无法获得舞伴。

### 解释：

这道题我的思路是先对男士的B数进行计算，并从小到大进行排序，对女士的最低要求也从小到大进行排序，然后对每一个B数进行对A的遍历，由于排过序,因此选出的舞伴应该正好是既满足 

<a><img src="https://latex.codecogs.com/gif.latex?B[b]&space;\leqslant&space;A[a]" title="B[b] \leqslant A[a]" /></a>

的情况下，也满足

<a><img src="https://latex.codecogs.com/gif.latex?fabs(B[b]-A[a])=&space;\underset&space;{b\leqslant&space;i\leqslant&space;M}{min}\{~fabs(B[i]-A[a])~\}" title="fabs(B[b]-A[a])= \underset {b\leqslant i\leqslant M}{min}\{~fabs(B[i]-A[a])~\}" /></a>

因为是要保证舞伴最多，因此不能有浪费的B数。

这是大致的思路。

**下面是复杂度的问题，1000ms的限制，首先这道题B数的计算很明显是让我们使用快速幂算法，这其中应用到了二进制：**

举个例子，例如计算：

<a><img src="https://latex.codecogs.com/gif.latex?3^{13}" title="3^{13}" /></a>

而计算它可以将它转化为：

<a><img src="https://latex.codecogs.com/gif.latex?3^{13}=3^{8}\times3^{4}\times3^{1}" title="3^{13}=3^{8}\times3^{4}\times3^{1}" /></a>

就能大大减少循环计算的次数，那么我们如何把任意一个幂的指数写成：

<a><img src="https://latex.codecogs.com/gif.latex?\sum2^k" title="\sum2^k" /></a>

的形式呢。

把指数13写成二进制：

<a><img src="https://latex.codecogs.com/gif.latex?1101" title="1101" /></a>

就比较明显了：

<a><img src="https://latex.codecogs.com/gif.latex?13=1\times2^3&plus;1\times2^2&plus;0\times2^1&plus;1\times2^0=8&plus;4&plus;1" title="13=1\times2^3+1\times2^2+0\times2^1+1\times2^0=8+4+1" /></a>

由此，我们得到统一的规律：

<a><img src="https://latex.codecogs.com/gif.latex?ans=x^n=x^{\sum_{i=0}^ma_i\times2^i}" title="ans=x^n=x^{\sum_{i=0}^ma_i\times2^i}" /></a>

而二进制项是否为1，由>>右移位运算符进行遍历即可。

然后就实现了这一算法，代码如下：

```cpp
long long quick_pow(long long x,long long n,long long m)
{
	long long res = 1;
	while(n > 0)
    {
		if(n & 1)	
        {
            res = res * x % m;
        }
		x = x * x % m;
		n >>= 1;
	}
	return res;
} 
```
这已经完成了一大步，接下来要有简化循环的好习惯，(别问我怎么知道的......)比如这道题的配对环节的循环，**我们将已经配对的B[i] = 200005,A[j] = 0,这样就不会再被考虑**，正是因为此，我们**下一个A的对B的遍历就不需要从i = 0开始了**，从上一次结束的地方开始就可以，因为我们排过序了。

这样我们就得到了AC代码：

```cpp
#include<iostream>
#include<string>
#include<cstring>
#include<algorithm>
#include<cmath>

using namespace std;

int T;
long long N,M,D;
long long *A;
long long *B;
int ans = 0;
int m;

long long quick_pow(long long x,long long n,long long m)
{
	long long res = 1;
	while(n > 0)
    {
		if(n & 1)	
        {
            res = res * x % m;
        }
		x = x * x % m;
		n >>= 1;
	}
	return res;
} 

int main()  
{
    cin>>T;
    while(T--)
    {
        cin>>N>>M>>D;
        m = 0;
        ans = 0;
        A = new long long[N];
        B = new long long[M];
        for(long long i = 0;i < N;i++)
        {
            cin>>A[i];
            A[i] = quick_pow(A[i],A[i],D);
        }
        sort(A,A+N);
        for(long long i = 0;i < M;i++)
        {
            cin>>B[i];
        }
        sort(B,B+M);
        
        for(long long i = 0;i < M;i++)
        {
            for(long long j = m;j < N;j++)
            {
                if(B[i] <= A[j])
                {
                    ans++;
                    B[i] = 200005;
                    A[j] = 0;
                    m = j;
                    break;
                }
            }
        }
        cout<<ans<<endl;
        delete A;
        delete B;
    }
    return 0;
}
```

这里相当于本小白复习快速幂了😂，所以写得多了些。
