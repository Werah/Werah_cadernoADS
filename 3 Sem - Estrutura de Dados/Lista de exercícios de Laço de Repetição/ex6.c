#include <stdio.h>

int main() {
    int soma = 0;
    for (int i = 1; i <= 100; i++) {
        if (i % 2 == 0) {
            soma += i;
        }
    }
    printf("A soma dos números pares de 1 a 100 é: %d", soma);
}