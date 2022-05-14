#include <iostream>
#include <string>

using namespace std;

int main()
{
    string A = "Hello,World!", B;
    getline(cin, B);
    if(A == B){
        cout << "AC" << endl;
    }else cout << "WA" << endl;
}