// 7. Faça um programa em C para exibir os números ímpares de 1 a 50.
#include <stdio.h>

int main() {
    int cont = 0;
    for (int i = 1; i <= 50; i++) {
        if (i % 2 != 0) {
            printf("%d\n",i);
        }
    }
}