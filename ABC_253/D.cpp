#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main()
{
    long long int n, a, b;
    cin >> n >> a >> b;
    long long int aa = n / a;
    long long int bb = n / b;

    long long int ab = n / (a * b);
    long long int SUM = (n * (n + 1)) / 2;
    long long int saa = (aa * (aa + 1)) / 2;
    long long int sbb = (bb * (bb + 1)) / 2;
    long long int sab = (ab * (ab + 1)) / 2;

    SUM -= a * saa;
    SUM -= b * sbb;
    SUM += ab * sab;
    cout << SUM << endl; 
}