#include <stdio.h>
int main(){
    int a;
    while (scanf("%x", &a) != EOF){
        printf("%d\n", a);
    }
    return 0;
}