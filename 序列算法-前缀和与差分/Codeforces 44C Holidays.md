# Codeforces 44C Holidays

## 题目：

School holidays come in Berland. The holidays are going to continue for n n n days. The students of school № N N N are having the time of their lives and the IT teacher Marina Sergeyevna, who has spent all the summer busy checking the BSE (Berland State Examination) results, has finally taken a vacation break! Some people are in charge of the daily watering of flowers in shifts according to the schedule. However when Marina Sergeyevna was making the schedule, she was so tired from work and so lost in dreams of the oncoming vacation that she perhaps made several mistakes. In fact, it is possible that according to the schedule, on some days during the holidays the flowers will not be watered or will be watered multiple times. Help Marina Sergeyevna to find a mistake.

n天假期，安排m个人来浇花，第i个人负责[a[i],b[i]]天，问花是否可以每天都被浇水且不重复。 可以的话输出“OK”，不可以的话输出最早出问题的那天的天号以及那天花被浇了多少次水。

1≤n,m≤100 1≤a[i]≤b[i]≤n b[i]≤a[i+1]

## 输入格式：

The first input line contains two numbers n n n and m m m ( 1<=n,m<=100 1<=n,m<=100 1<=n,m<=100 ) — the number of days in Berland holidays and the number of people in charge of the watering respectively. The next m m m lines contain the description of the duty schedule. Each line contains two integers ai a_{i} ai​ and bi b_{i} bi​ ( 1<=ai<=bi<=n 1<=a_{i}<=b_{i}<=n 1<=ai​<=bi​<=n ), meaning that the i i i -th person in charge should water the flowers from the ai a_{i} ai​ -th to the bi b_{i} bi​ -th day inclusively, once a day. The duty shifts are described sequentially, i.e. bi<=ai+1 b_{i}<=a_{i+1} bi​<=ai+1​ for all i i i from 1 1 1 to n−1 n-1 n−1 inclusively.

## 输出格式：

Print "OK" (without quotes), if the schedule does not contain mistakes. Otherwise you have to find the minimal number of a day when the flowers will not be watered or will be watered multiple times, and output two integers — the day number and the number of times the flowers will be watered that day.

## 样例：

输入1：

    10 5
    1 2
    3 3
    4 6
    7 7
    8 10

输出：

    OK

输入2：

    10 5
    1 2
    2 3
    4 5
    7 8
    9 10

输出：

    2 2

输入3：

    10 5
    1 2
    3 3
    5 7
    7 7
    7 10

输出：

    4 0

## 分析：

体面上分析出这是一道区间和的问题，那首选就是差分前缀和了，~~模拟也可以，就是费脑子~~change差分数组最一开始均为0，然后`a[i]`和`b[i]`为左端点和右端点。

最后再对sum遍历判断即可。

代码：

```cpp
#include<iostream>
#include<string>
#include<cstring>
#include<algorithm>
#include<cmath>
#include<vector>

using namespace std;

int main()
{
    int n,m;
    int a[105] = {0};
    int b[105] = {0};
    int change[105] = {0};
    int sum[105] = {0};
    bool judge = false;

    cin>>n>>m;
    for(int i = 1;i <= m;i++)
    {
        cin>>a[i]>>b[i];
    }
    for(int i = 1;i <= m;i++)
    {
        change[a[i]]++;
        change[b[i] + 1]--;
    }
    for(int i = 1;i <= n;i++)
    {
        sum[i] = sum[i - 1] + change[i];
        if(sum[i] != 1)
        {
            cout<<i<<" "<<sum[i];
            judge = true;
            break;
        }
    }
    if(!judge)
    {
        cout<<"OK"<<endl;
    }
    return 0;
}

```

