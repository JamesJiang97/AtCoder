#include <cstdio>
#include <iostream>
#include <algorithm>

using namespace std;

struct S
{
    int key;
    int score;
};

bool compare(const S &x, const S &y)
{
    return x.score < y.score;
}

int main()
{
    int n;
    cin >> n;
    S A[n];
    for (int i = 0; i < n; i++)
    {
        A[i].key = i + 1;
        cin >> A[i].score;
    }
    sort(A, A + n, compare);
    cout << A[n - 2].key;
}
