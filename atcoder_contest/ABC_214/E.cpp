/*
 * @Author: your name
 * @Date: 2021-08-14 22:04:38
 * @LastEditTime: 2021-08-14 22:34:38
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: /AtCoder/beginner_214/E.cpp
 */
#include <iostream>

using namespace std;

int main()
{
    int T;
    cin >> T;
    for (int z = 0; z < T; z++)
    {
        int N, tag = 0;
        cin >> N;
        int L[N], R[N];
        for (int i = 0; i < N; i++)
        {
            cin >> L[i] >> R[i];
        }
        int B[N + 1];
        for (int i = 1; i <= N; i++)
        {
            B[i] = -1;
        }
        for (int i = 0; i < N; i++)
        {
            if (tag)
                break;
            int j;
            for (j = L[i]; j <= R[i]; j++)
            {
                if (B[j] == -1)
                {
                    B[j] = 1;
                    break;
                }
            }
            if(j>R[i]){
                tag = 1;
            }
        }
        if (tag)
        {
            cout << "No" << endl;
            continue;
        }
        cout << "Yes" << endl;
    }
}