#include<iostream>
#include<string>
#include<cstring>
#include<algorithm>
#include<cmath>

using namespace std; 

long long quick_pow(long long base,long long pow,long long m)
{
    long long ans = 1 % m;
    while(pow)
    {
        if(pow & 1)
        {
            ans = ans * base % m;
        }
        base = base * base % m;//caculate the x^n
        pow >>= 1;
    }
    return ans;
}

int main()
{
    long long a,b,m;

    cin>>a>>b>>m;
    cout<<quick_pow(a,b,m)<<endl;
    return 0;
}
/*
Algorithm:     快速幂
Contributor:   hhy-huang
*/
