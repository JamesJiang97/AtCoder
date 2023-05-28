#include <bits/stdc++.h>


using namespace std;

struct Card
{
    int X;
    int Y;
    int key;
};

bool compareX(const Card &x, const Card &y)
{
    return x.X < y.X;
}

bool compareY(const Card &x, const Card &y)
{
    return x.Y < y.Y;
}

bool compareK(const Card &x, const Card &y)
{
    return x.key < y.key;
}

int main()
{
    int H, W, N;
    cin >> H >> W >> N;
    Card C[N];
    for (int i = 0; i < N; i++)
    {
        cin >> C[i].X >> C[i].Y;
        C[i].key = i + 1;
    }
    sort(C, C + N, compareX);
    int n = 1;
    for (int i = 0; i < N; i++)
    {
        if (C[i].X > n)
        {
            int temp = C[i].X - n;
            for (int j = i; j < n; j++)
            {
                C[j].X -= temp;
            }
        }
        n = C[i].X + 1;
    }
    sort(C, C + N, compareY);
    n = 1;
    for (int i = 0; i < N; i++)
    {
        if (C[i].Y > n)
        {
            int temp = C[i].Y - n;

            for (int j = i; j < n; j++)
            {
                C[j].Y -= temp;
            }
        }
        n = C[i].Y + 1;
    }
    sort(C, C + N, compareK);
    for (int i = 0; i < N; i++)
    {
        cout << C[i].X << " " << C[i].Y << endl;
    }
    
}
