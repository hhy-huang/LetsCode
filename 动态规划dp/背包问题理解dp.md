# 动态规划dp

这个算法以普通的背包问题引入。

它其实是将大块问题分解成小问题，并使得每一个小问题的解决都可依赖其它小问题解决后的结果来进行。

## 首先描述一下背包问题：

容量为10的背包，有5种物品，**每种物品只有一个**，其重量分别为5，4，3，2，1，其价值分别为1，2，3，4，5。设计算法，实现背包内物品价值最大。

对于这个大问题，把它分解为：设物品标号为[1],[2],[3],[4],[5]。然后计算当存在物品分别为[1],[1][2],[1][2][3]...时、背包容量分别为1、2、3、4...9、10时背包内价值的最大值。下面展示一下思维过程：

*当只有物品[1]时：([1]的重量为5，价值为1，下面以此类推)*

    size:  1 2 3 4 5 6 7 8 9 10
    price: 0 0 0 0 1 1 1 1 1 1

*当只有物品[1]、[2]时：*

    size:  1 2 3 4 5 6 7 8 9 10
    price: 0 0 0 2 2 2 2 2 3 3

*当只有物品[1]、[2]、[3]时：*

    size:  1 2 3 4 5 6 7 8 9 10
    price: 0 0 3 3 3 3 5 5 5 5

*当只有物品[1]、[2]、[3]、[4]时：*

    size:  1 2 3 4 5 6 7 8 9 10
    price: 0 4 4 4 7 7 7 7 9 9

*当只有物品[1]、[2]、[3]、[4]、[5]，即全部都有时：*

    size:  1 2 3 4 5 6  7  8  9  10
    price: 5 5 9 9 9 12 12 12 12 12

但是每一个最大价格的计算是怎么依赖前面问题的结果的呢？

假设上面的矩阵为：

<center><a href="https://www.codecogs.com/eqnedit.php?latex=dp[6][11]" target="_blank"><img src="https://latex.codecogs.com/png.latex?dp[6][11]" title="dp[6][11]" /></a></center>

那么在计算dp[i][j]时，进行如下计算和判断:（j >= w[i] )

<center><a href="https://www.codecogs.com/eqnedit.php?latex=dp[i][j]&space;=max&space;\begin{cases}&space;dp[i-1][j]&&space;\\&space;dp[i-1][j-w[i]]&space;&plus;&space;v[i]&&space;\end{cases}" target="_blank"><img src="https://latex.codecogs.com/png.latex?dp[i][j]&space;=max&space;\begin{cases}&space;dp[i-1][j]&&space;\\&space;dp[i-1][j-w[i]]&space;&plus;&space;v[i]&&space;\end{cases}" title="dp[i][j] =max \begin{cases} dp[i-1][j]& \\ dp[i-1][j-w[i]] + v[i]& \end{cases}" /></a></center>

就是比较来确定在增加了一个物体后，背包内能否再在这基础上放入物品。而这个背包价值的最大值就是这个矩阵中元素的最大值。

代码如下：
```cpp
int dp[6][11] = {0};
int v[6] = {0,1,2,3,4,5};
int w[6] = {0,5,4,3,2,1};
int n = 5, m = 10;
for(int i = 1;i <= n;i++)
{
    for(int j = m;j > 0;j--)
    {
        if(j >= w[i])
        {
            dp[i][j] = max(dp[i-1][j], dp[i-1][j - w[i]] + v[i]);//减去当前产品的质量之后剩余多少
        }
        else
        {
            dp[i][j] = dp[i-1][j];
        }
    }
}
```

## 对于完全背包问题

容量为10的背包，有5种物品，**每种物品数量无限**，其重量分别为5，4，3，2，1，其价值分别为1，2，3，4，5。 设计算法，实现背包内物品价值最大。

区别就是限制不再是物品个数了，而只是背包容量。修改的也只是矩阵列的循环方式。

代码如下：

```cpp
int dp[6][11] = {0};
int v[6] = {0,1,2,3,4,5};
int w[6] = {0,5,4,3,2,1};
int n = 5, m = 10;
for(int i = 1;i <= n;i++)
{
    for(int j = w[i];j <= m;j++)
    {
        if(j >= w[i])
        {
            dp[i][j] = max(dp[i-1][j], dp[i-1][j - w[i]] + v[i]);
        }
        else
        {
            dp[i][j] = dp[i-1][j];
        }
    }
}
```

## 对于多重背包问题

容量为10的背包，有5种物品，**每种物品数量分别为1，2，1，2，1**，其重量分别为5，4，3，2，1，其价值分别为1，2，3，4，5。设计算法，实现背包内物品价值最大。

按照背包的思路，每一个物品的限制不同，所以再增加一个循环限制即可。

```cpp
int dp[6][11] = {0};
int v[6] = {0,1,2,3,4,5};
int w[6] = {0,5,4,3,2,1};
int n[6] = {0,1,2,1,2,1};
int n = 5, m = 10;
for(int i = 1;i <= n;i++)
{
    for(int k = 1;k <= n[i];k++)
    {
        for(int j = m;j > 0;j--)
        {
            if(j >= w[i])
            {
                dp[i][j] = max(dp[i-1][j], dp[i-1][j - w[i]] + v[i]);
            }
            else
            {
                dp[i][j] = dp[i-1][j];
            }
        }
    }
}
```

<!--
algorithm: dp
contributor: hhy
-->
