#include <cstdio>

using namespace std;

int main(){
    int X[4], x, mod = 10;
    scanf("%d", &x);
    for(int i = 3; i >=0; i--){
        X[i] = x % mod;
        x /= mod;
    }
    if(X[0] == X[1] && X[1] == X[2] && X[2]== X[3]){
        printf("Weak");
        return 0;
    }
    for(int i = 0; i < 3; i++){
        if(X[i+1] != (X[i]+1)%10){
            printf("Strong");
            return 0;
        }
    }
    printf("Weak");
}