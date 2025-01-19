#include <stdio.h>
#include <limits.h>
#include <math.h>
#include <stdint.h>

int max() {
    // Usando a função pow() da biblioteca math.h
    // return (int)pow(2, 8 * sizeof(int)) - 1;

    // Fazendo um deslocamento de bits
    return (int)((1U << (8 * sizeof(int) - 1)) - 1);
}
/*int32_t c() {
    return (int32_t)((1U << (8 * sizeof(int32_t) - 1)) - 1);
}*/