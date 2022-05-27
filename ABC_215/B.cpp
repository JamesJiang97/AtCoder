#include <iostream>

using namespace std;

int main()
{
    long long N;
    cin >> N;
    long long l = 1;
    for(int i = 0; i < 70; i++){
        if(l == N){
            cout <<  i << endl;
            break;
        }else if(l > N) {
            cout << i-1 << endl;
            break;
        }
        l *= 2;
    }
}