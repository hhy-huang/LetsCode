#include<iostream>
#include<string>
#include<cstring>
#include<algorithm>
#include<cmath>

using namespace std;
#define BIG 9223372036854775807

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
    long long a,b;

    cin>>a>>b;
    cout<<quick_pow(a,b,BIG)<<endl;
    return 0;
}
