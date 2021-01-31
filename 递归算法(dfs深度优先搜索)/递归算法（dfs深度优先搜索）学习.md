# 递归算法（dfs深度优先搜索）

递归算法一般用于问题可抽象为以下公式的情况：

<a><img src="https://latex.codecogs.com/png.latex?\bg_white&space;\begin{cases}&space;F(n)&space;=&space;G(n,F(n-1))&space;&&space;\text{&space;}&space;n>0&space;\\&space;F(n)&space;=&space;a&space;&&space;\text{&space;}&space;n&space;=&space;0&space;\end{cases}" title="\begin{cases} F(n) = G(n,F(n-1)) & \text{ } n>0 \\ F(n) = a & \text{ } n = 0 \end{cases}" /></a>

**背景问题**：给你一个长度为3的环形数组，请你往里面填数字1--20，要求不能重复，而且相邻两个数的和为质数。 请输出所有的可能方案。

这种问题的首先想到的是用for循环堆叠，这样的思路很清晰，但是却很冗长并且不适宜解决数据更大的问题。

对于长度为3，用3个for循环来解决，代码如下：

```cpp
bool vis[20];
int ans = 0;
int a[20];

bool isprime(int x)
{
    for(int i = 2;i <= sqrt(x);i++)
    {
        if(x % i == 0)
        {
            return false;
        }
    }
    return true;
}

int main()
{
    for(int i = 1;i <= 20;i++)
    {
        if(vis[i])
        {
            continue;
        }
        vis[i] = true;
        a[1] = i;
        for(int j = 1;j <= 20;j++)
        {
            if(vis[j])
            {
                continue;
            }
            if(!isprime(a[1] + j))
            {
                continue;
            }
            vis[j] = true;
            a[2] = j;
            for(int k = 1;k <= 20;k++)
            {
                if(vis[k])
                {
                    continue;
                }
                if(!isprime(a[2] + k) || !isprime(a[1] + k))
                {
                    continue;
                }
                ans++;
            }
            vis[j] = false;
        }
        vis[i] = false;
    }
    return 0;
}
```

现在把这些步骤写为递归，通过分析，写的每一个循环都要遵从以下的步骤：

    1.排除非法情况
    2.记录相关信息
    3.下一层操作
    4.消除vis

这也是深搜模板的套路，先判断是否达到目标，若达到了目标，判断当前的状态是否计入答案，没达到就枚举可能的状态，记录本轮的选择，进入下一状态。

下面给出上述问题的递归（dfs）操作：

```cpp
bool vis[20];
int ans = 0;
int a[20];
int n;

bool isprime(int x)
{
    for(int i = 2;i <= sqrt(x);i++)
    {
        if(x % i == 0)
        {
            return false;
        }
    }
    return true;
}

void dfs(int now)
{
    if(now == n + 1)
    {
        if(isprime(a[n] + a[1]))
        {
            ans++;
        }
        return;
    }
    for(int i = 1;i <= 20;i++)
    {
        if(!vis[i])
        {
            if(now > 1 && !isprime(a[now - 1] + i))
            {
                continue;
            }
            vis[i] = true;
            a[now] = i;
            dfs(now + 1);//循环n次
            vis[i] = false;
        }
    }
}
```
可以类比斐波那契数列的操作，因为要进行n次的for循环操作，因此搜索终止的条件就是`now == n + 1` ，并且对于每一次的搜索的for循环的操作都是一样的，先用`vis[i]`判断是否用过这个数，并且在`now > 1`的情况下，上一个符合要求的数在这一循环也要符合要求（指和为质数）。然后记录信息，继续向深里循环，最后记得处理干净，即`vis[i] = false`。

这样就完成了深搜的操作，感觉重要的还是把原过程搞清楚，不然写递推会一塌糊涂，不要忘记操作就行。
