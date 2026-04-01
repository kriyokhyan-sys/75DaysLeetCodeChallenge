#include <stdlib.h>
#include <string.h>

int evalRPN(char** tokens, int tokensSize) {
    int* stack = (int*)malloc(sizeof(int) * tokensSize);
    int top = -1;

    for (int i = 0; i < tokensSize; i++) {
        char* s = tokens[i];

        if ((strlen(s) == 1) && (s[0] == '+' || s[0] == '-' || s[0] == '*' || s[0] == '/')) {
            long b = stack[top--];
            long a = stack[top--];
            
            if (s[0] == '+') stack[++top] = (int)(a + b);
            else if (s[0] == '-') stack[++top] = (int)(a - b);
            else if (s[0] == '*') stack[++top] = (int)(a * b);
            else if (s[0] == '/') stack[++top] = (int)(a / b);
        } else {
            stack[++top] = atoi(s);
        }
    }

    int result = stack[0];
    free(stack);
    return result;
}