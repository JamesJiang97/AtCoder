/*
 * @Author: your name
 * @Date: 2021-08-08 20:24:51
 * @LastEditTime: 2021-08-14 20:01:49
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: /AtCoder/beginner_213/A-Bitwise_Exclusive_Or.cpp
 */
#include <cstdio>
#include <iostream>

using namespace std;

int main()
{
    int a, b, A[7], B[7], C[7];
    a = 12, b = 6;
    int i = 0;
    while (a || b)
    {
        A[i] = a % 2;
        a /= 2;
        B[i] = b % 2;
        b /= 2;
        i++;
    }
    for (int j = 0; j < i; j++)
    {
        if (A[j] == B[j])
        {
            C[j] = 0;
        }
        else
            C[j] = 1;
    }
    int k = 1;
    int out = 0;
    for (int j = 0; j < i; j++)
    {
        out += C[j] * k;
        k *= 2;
    }
    cout << out;
}