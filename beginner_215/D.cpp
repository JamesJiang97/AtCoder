#include <iostream>
#include <cmath>

using namespace std;

int gcd(int x, int y)
{
    if (x % y == 0)
    {
        return y;
    }
    else
    {
        return gcd(y, x % y);
    }
}

int main()
{
    int N, M;
    cin >> N >> M;
    int A[N];
    for (int i = 0; i < N; i++)
    {
        cin >> A[i];
    }
    int B[M];
    int count = 0;
    for (int i = 1; i <= M; i++)
    {
        int tag = 1;
        for (int j = 0; j < N; j++)
        {
            if (gcd(A[j], i) != 1)
            {
                tag = 0;
                break;
            }
        }
        if (tag)
        {
            B[count] = i;
            count++;
        }
    }
    cout << count << endl;
    for (int i = 0; i < count; i++)
    {
        cout << B[i] << endl;
    }
}