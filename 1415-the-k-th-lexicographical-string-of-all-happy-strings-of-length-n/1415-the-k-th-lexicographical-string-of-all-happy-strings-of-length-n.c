#include <stdlib.h>
#include <string.h>

void backtrack(int n, int* k, char* current, int index, char** result) {
    if (*result != NULL) return;

    if (index == n) {
        (*k)--;
        if (*k == 0) {
            *result = strdup(current);
        }
        return;
    }

    for (char c = 'a'; c <= 'c'; c++) {
        if (index == 0 || current[index - 1] != c) {
            current[index] = c;
            current[index + 1] = '\0';
            backtrack(n, k, current, index + 1, result);
        }
    }
}

char* getHappyString(int n, int k) {
    char current[11] = {0};
    char* result = NULL;
    int temp_k = k;
    
    backtrack(n, &temp_k, current, 0, &result);
    
    return result ? result : "";
}