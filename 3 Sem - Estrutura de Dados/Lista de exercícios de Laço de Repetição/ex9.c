//9. Faça um programa em C para calcular a potência de um número.
#include <stdio.h>

int main() {
    int base, expoente;
    long long resultado = 1;
    printf("Digite a base: ");
    scanf("%d", &base);
    printf("Digite o expoente: ");
    scanf("%d", &expoente);
    if (expoente < 0) {
        printf("Expoente não pode ser negativo.\n");
        return 1;
    }
    for (int i = 0; i < expoente; i++) {
        resultado *= base;
    }
    printf("%d elevado a %d é: %lld\n", base, expoente, resultado);
    return 0;
}