#include <cstdio>

using namespace std;

int main(){
    int a, b;
    scanf("%d %d", &a, &b);
    if(a > 0 && b > 0){
        printf("Alloy\n");
    } else if(a == 0){
        printf("Silver\n");
    } else {
        printf("Gold\n");
    }
}