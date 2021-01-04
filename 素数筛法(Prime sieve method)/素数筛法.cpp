#include<iostream>
#include<string>
#include<cstring>
#include<algorithm>
#include<cmath>

using namespace std;

//原始筛选法->适用于单个元素的检验
bool isprime_A(int n)
{
    for(int i = 2;i < sqrt(n);i++)
    {
        if(n % i == 0)
        {
            return false;
        }
    }
    return true;
}

//埃拉托斯特尼(Eratosthenes)筛法->适用于一定范围的元素的筛选
bool is_prime[1000];//布尔数组来标记是否为素数
int prime[1000] = {0};    //存放素数
int q = 0;

void isprime_B(int b) //要筛选素数的区间右端点
{
    memset(is_prime,true,sizeof(is_prime[0]));//先假设都为素数
    for(int i = 2;i <= sqrt(b);i++)
    {
        if(is_prime[i])
        {
            prime[q++] = i;
            for(int j = i*2;j <= b;j += i)//素数的倍数一定不是素数
            {
                is_prime[j] = false;
            }
        }
    }

}

//欧拉筛法->适用于一定范围的元素的筛选，时间复杂度O(n)
bool is_prime_Euler[1000];
int prime2[1000] = {0};

void isprime_C(int b)
{
    int k = 0,j = 0;

    memset(is_prime_Euler,true,sizeof(is_prime_Euler[0]));
    for(int i = 2;i <= b;i++)
    {
        if(is_prime_Euler[i])
        {
            prime2[j++] = i;
        }
        //接下来进行筛的操作
        while(1)
        {
            if(i*prime2[k] > b)
            {
                break;
            }
            is_prime_Euler[i*prime2[k]] = false;//最小质因数的倍数一定不是素数
            if(i % prime2[k] == 0)//确保是最小质因数
            {
                break;
            }
            k++;
        }
        k = 0;
    }
}


int main()
{
    int a,b;
    if(isprime_A(a))
    {
        cout<<"YES"<<endl;
    }
    else
    {
        cout<<"NO"<<endl;
    }

    isprime_B(b);
    for(int i = 0;;i++)
    {
        if(prime[i] == 0)
        {
            break;
        }
        cout<<prime[i]<<" ";
    }
    cout<<endl;
    isprime_C(b);
    for(int i = 0;;i++)
    {
        if(prime2[i] == 0)
        {
            break;
        }
        cout<<prime2[i]<<" ";
    }
    cout<<endl;
    return 0;
}
