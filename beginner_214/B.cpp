/*
 * @Author: your name
 * @Date: 2021-08-14 21:04:12
 * @LastEditTime: 2021-08-14 21:13:14
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: /AtCoder/beginner_214/B.cpp
 */
#include <iostream>

using namespace std;

int main()
{
    int S, T;
    cin >> S >> T;
    int N = 0;
    for (int i = 0; i <= S; i++)
    {
        for (int j = 0; j <= S; j++)
        {
            if (i + j > S)
                break;
            for (int k = 0; k <= S; k++)
            {
                if (i + j + k > S)
                    break;
                if (i + j + k <= S && i * j * k <= T)
                {
                    N++;
                }
            }
        }
    }
    cout << N << endl;
}