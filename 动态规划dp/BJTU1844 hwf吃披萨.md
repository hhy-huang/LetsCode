# BJTU1844 hwf吃披萨

## 题目：

hwf 是一个非常喜欢吃披萨的人。某天，天上掉下了一张披萨，被 hwf 和高老师看到了。高老师把披萨分成了 𝑛 份, 第 𝑖 份的角度为 𝑎𝑖。为了公平起见，他们决定由 hwf 把 𝑛 份披萨分成两堆，然后高老师肯定会挑一堆角度和多的，hwf 拿剩下的一堆。hwf 想吃到尽可能多的披萨，但是 hwf 的心思已经全在吃披萨上了。

快帮助 hwf，告诉他最多能吃到多少披萨吧！

## 输入数据：

第一行为一个整数 𝑡 (1≤𝑡≤500)，表示数据的组数。接下来对于每组数据：第一行有一个整数 𝑛 (2≤𝑛≤360)，表示披萨被分成的份数。
第二行有 𝑛 个整数 𝑎1,𝑎2,…,𝑎𝑛 (1≤𝑎𝑖<360)，分别表示第 𝑖 份披萨的角度。

保证 ∑𝑛𝑖=1𝑎𝑖=360

## 样例

输入：

    2
    4
    10 130 170 50
    3
    200 60 100

输出：

    180
    160

## 解释:

在理解完题意后，**可以把它抽象为一个01背包的dp问题**，题意是hwf得到的角度和在不超过180度的情况下找它的最大值，这熟悉的描述方式就是dp了。

然后180就相当于它背包的limitation，然后物品的weight和value值都是它的角度，模型就出来了。

下面是AC代码：

```cpp
#include<iostream>
#include<string>
#include<cstring>
#include<algorithm>
#include<cmath>

using namespace std;

int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        int n;
        int a[500] = {0};
        int dp[500] = {0};

        cin>>n;
        for(int i = 1;i <= n;i++)
        {
            cin>>a[i];
        }
        for(int i = 1;i <= n;i++)
        {
            for(int j = 180;j >= a[i];j--)
            {
                dp[j] = max(dp[j],dp[j-a[i]]+a[i]);
            }
        }
        cout<<dp[180]<<endl;
    }
    return 0;
}

```
