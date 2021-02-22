# BFS广度优先搜素

bfs相对于dfs来说，并不是一条路走到黑，不撞南墙不回头，而是对于每一层的所有情况都遍历一次才进入下一层。也就是说bfs更侧重于每一层的可能性，而不是每个选择的可能性。

对于二叉树的遍历来说，遍历完一层才会进入下一层。

c++中实现方法往往是使用一个队列，先将起点元素push进去，然后再去遍历该元素的子元素，再将它pop出去，将他们的子元素依次push到队列中，再重复相同的过程，这样就能实现只有遍历完父节点才能去索引子节点。

这种算法通常用来保证结果的完整性，用于解决问题答案大多聚集在浅层的问题。

对于如下例题：

## 马的遍历：

有一个n*m的棋盘(1< n,m<=400)，在某个点上有一个马,要求你计算出马到达棋盘 上任意一个点最少要 走几步。

输入：一行四个数据，棋盘的大小和马的坐标。

输出：一个n*m的矩阵，代表马到达某个点最少要走几步(左对齐，宽5格，不能到达则输 出-1。

样例：

输入：

    3 3 1 1

输出

    0 3 2 
    3 -1 1
    2 1 4

除了实现方法不同，处理方法与dfs是类似的，都要去判断坐标的合法性，然后进行下一步的遍历，注意遍历的终点是序列中的元素为空（表示均已遍历完）。
```cpp
#include<iostream>
#include<iostream>
#include<string>
#include<cstring>
#include<algorithm>
#include<cmath>
#include<vector>
#include<cstdio>
#include<queue>

using namespace std;

class node
{
public:
    int x;
    int y;
};

int n,m;
int x,y;
int dx[8] = {2, 1, -1, -2, -2, -1, 1, 2};
int dy[8] = {-1, -2, -2, -1, 1, 2, 2, 1};
int dist[500][500];
bool vis[500][500];
queue<node> q;

int main()
{
    cin>>n>>m>>x>>y;
    x--;
    y--;
    for(int i = 0;i < n;i++)
    {
        for(int j = 0;j < m;j++)
        {
            dist[i][j] = -1;
        }
    }
    dist[x][y] = 0;
    memset(vis, false, sizeof(vis));
    node temp;
    temp.x = x;
    temp.y = y;
    vis[x][y] = true;

    q.push(temp);
    
    while(!q.empty())
    {
        node now = q.front();
        q.pop();
        int nx = now.x;
        int ny = now.y;
        for(int i = 0;i < 8;i++)
        {
            int newx = nx + dx[i];
            int newy = ny + dy[i];
            if(newx < 0 || newx >= n || newy < 0 || newy >= m)
            {
                continue;
            }
            else
            {
                if(vis[newx][newy])
                {
                    continue;
                }
                temp.x = newx;
                temp.y = newy;
                q.push(temp);
                vis[newx][newy] = true;
                dist[newx][newy] = dist[nx][ny] + 1;
            }
        }
    }
    for(int i = 0;i< n;i++)
    {
        for(int j = 0;j < m;j++)
        {
            cout<<dist[i][j]<<" ";
        }
        cout<<endl;
    }
    return 0;
}
```
