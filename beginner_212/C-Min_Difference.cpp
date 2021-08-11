#include <cstdio>
#include <algorithm>

using namespace std;

bool compare(int a, int b){
    return a > b;
}

int main(){
    int N, M;
    scanf("%d %d", &N, &M);
    int A[N], B[M];
    for(int i = 0; i < N; i++){
        scanf("%d", &A[i]);
    }
    for(int i = 0; i < M; i++){
        scanf("%d", &B[i]);
    }
    sort(A, A+N, compare);
    sort(B, B+M, compare);
    int min = 2147483647;
    for(int i = 0; i < N; i++){
        for(int j = 0; j < M; j++){
            int temp = abs(A[i] - B[j]);
            if(temp < min){
                min = temp;
            }
            if(temp > min){
                break;
            }
        }
    }
    printf("%d\n", min);
}