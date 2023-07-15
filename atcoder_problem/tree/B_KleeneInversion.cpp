#include <iostream>
#include <string>
#include <vector>

using namespace std;

long long int MOD = 1000000007;

int main()
{
    int n, k;
    long long int ans = 0;
    cin >> n >> k;
    vector<int> A(n);

    for (int i = 0; i < n; i++)
    {
        cin >> A[i];
    }

    for (int i = 0; i < n; i++)
    {
        int aft = 0, all = 0;
        for (int j = i; j < n; j++){
            if(A[i] > A[j]) aft++;
        }
        for (int k = 0; k < n; k++)
        {
            if(A[i] > A[k]) all++;
        }

        ans += aft * k % MOD;
        ans %= MOD;
        ans += (((k - 1) * k) / 2 % MOD) * (all % MOD);
        ans %= MOD;

    }
    cout << ans << endl;
}