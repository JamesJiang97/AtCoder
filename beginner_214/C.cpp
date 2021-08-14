/*
 * @Author: your name
 * @Date: 2021-08-14 21:13:54
 * @LastEditTime: 2021-08-14 21:50:17
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: /AtCoder/beginner_214/C.cpp
 */
#include <iostream>

using namespace std;

int main()
{
    int N;
    cin >> N;
    int S[N], T[N];
    for(int i = 0; i < N; i++){
        cin >> S[i];
    }
    for(int i = 0; i < N; i++){
        cin >> T[i];
    }
    for (int i = 0; i < N; i++)
    {
        int j = i;
        while (1)
        {
            if (T[j] + S[j] < T[(j + 1) % N])
            {
                T[(j + 1)%N] = T[j] + S[j];
                j = (j+1)%N;
            }else break;
        }
    }
    for(int i = 0; i < N; i++){
        cout<< T[i] << endl;
    }
}