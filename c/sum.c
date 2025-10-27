#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    if (argc < 2) {
        fprintf(stderr, "Uso: %s <num1> <num2> ...\n", argv[0]);
        return 1;
    }
    double sum = 0.0;
    for (int i = 1; i < argc; i++) sum += strtod(argv[i], NULL);
    printf("Somma = %.6f\n", sum);
    return 0;
}
