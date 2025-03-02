//10. Escreva um programa em C para imprimir uma pirâmide de números:
//
//          1 
//         2 2 
//        3 3 3 
//       4 4 4 4 
//      5 5 5 5 5 
//     6 6 6 6 6 6 
//    7 7 7 7 7 7 7 
//   8 8 8 8 8 8 8 8 
//  9 9 9 9 9 9 9 9 9

#include <stdio.h>

int main() {
    int linhas = 9;
    for (int i = 1; i <= linhas; i++) {
        for (int espaco = 1; espaco <= linhas - i; espaco++) {
            printf(" ");
        }
        for (int j = 1; j <= i; j++) {
            printf("%d ", i);
        }
        printf("\n");
    }
    return 0;
}