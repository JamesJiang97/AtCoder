#include <iostream>

using namespace std;

int main(){
    unsigned long int a, b, c, d, e, f;

    cin >> a >> b >> c >> d >> e >> f;

    int X = 998244353;
    a = a % X;
    b = b % X;
    c = c % X;
    d = d % X;
    e = e % X;
    f = f % X;

    unsigned long int ab = (a*b)%X;
    unsigned long int abc = (ab*c)%X;
    unsigned long int de = (d*e)%X;
    unsigned long int def = (de*f)%X;

    unsigned long int ans = abc-def;

    cout << ans;
}