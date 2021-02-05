# 洛谷：P6207 [USACO06OCT] Cows on Skates G

## 题目：

Farmer John 把农场划分为了一个 r 行 c 列的矩阵，并发现奶牛们无法通过其中一些区域。此刻，Bessie 位于坐标为 (1,1) 的区域，并想到坐标为 (r,c) 的牛棚享用晚餐。她知道，以她所在的区域为起点，每次移动至相邻的四个区域之一，总有一些路径可以到达牛棚。

这样的路径可能有无数种，请你输出任意一种，并保证所需移动次数不超过 100000。
## 输入：

第一行两个整数 r,c。

接下来 r 行，每行 c 个字符，表示 Bessie 能否通过相应位置的区域。字符只可能是 . 或 *。

    . 表示 Bessie 可以通过该区域。
    * 表示 Bessie 无法通过该区域。



## 输出：

若干行，每行包含两个用空格隔开的整数，表示 Bessie 依次通过的区域的坐标。

显然，输出的第一行是 1 1 ，最后一行是 r c。

相邻的两个坐标所表示的区域必须相邻。

## 样例：

输入：

    5 8
    ..*...**
    *.*.*.**
    *...*...
    *.*.*.*.
    ....*.*.

输出：

    1 1
    1 2
    2 2
    3 2
    3 3
    3 4
    2 4
    1 4
    1 5
    1 6
    2 6
    3 6
    3 7
    3 8
    4 8
    5 8

## 分析：

与一般的地图搜索题模式一样，但是这里涉及到了在满足要求时，输出满足要求时的状态集合。

对于一个一般函数来说return后就可以跳出了，然后在主函数中输出状态集合。但是现在时在递归函数中，跳出了递归的的这一个函数，上一层还会有函数继续循环递归，状态方程在到达主函数的输出行时已经改变了。

所以return出来输出不可行，所以直接在dfs函数中进行输出，输出完直接`exit()`，结束运行。

代码：

```cpp
#include<iostream>
#include<string>
#include<cstring>
#include<algorithm>
#include<cmath>
#include<vector>

using namespace std;

int r,c;
char map[400][400] = {'*'};
string s;
int change_x[4] = {-1, 0, 1, 0};
int change_y[4] = {0, 1, 0, -1};
int ans[4000000][2];
int q = 0;

void dfs(int x, int y)
{
    if(x == r - 1 && y == c - 1)
    {
        for(int i = 0;i <= q;i++)
        {
            cout<<ans[i][0] + 1<<" "<<ans[i][1] + 1<<endl;
        }
        exit(0);
    }
    for(int i = 0;i < 4;i++)
    {
        int new_x = x + change_x[i];
        int new_y = y + change_y[i];

        if(new_x >= 0 && new_x < r && new_y >= 0 && new_y < c && map[new_x][new_y] == '.')
        {
            q++;
            ans[q][0] = new_x;
            ans[q][1] = new_y;
            map[new_x][new_y] = '*';
            dfs(new_x,new_y);
            q--;
        }
    }
}

int main()
{
    cin>>r>>c;

    for(int i = 0;i < r;i++)
    {
       cin>>s;
       for(int j = 0;j < c;j++)
       {
           map[i][j] = s[j];
       }
    }
    ans[0][0] = 0;
    ans[0][1] = 0;
    map[0][0] = '*';
    dfs(0,0);
    return 0;
}
```
