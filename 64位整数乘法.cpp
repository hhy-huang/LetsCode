#include<iostream>
#include<string>
#include<cstring>
#include<algorithm>
#include<cmath>

using namespace std;
#define BIG 9223372036854775807

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
    long long a,b;

    cin>>a>>b;
    cout<<big_multi(a,b,BIG)<<endl;
    return 0;
}