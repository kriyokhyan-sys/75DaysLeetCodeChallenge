#include <stdbool.h>
#include <string.h>

bool isValid(char* s) {
    int n = strlen(s);
    if (n % 2 != 0) return false; // Odd length strings can't be valid

    char stack[n];
    int top = -1;

    for (int i = 0; i < n; i++) {
        char c = s[i];
        
        if (c == '(' || c == '[' || c == '{') {
            stack[++top] = c;
        } else {
            if (top == -1) return false;
            
            char last = stack[top--];
            if (c == ')' && last != '(') return false;
            if (c == ']' && last != '[') return false;
            if (c == '}' && last != '{') return false;
        }
    }

    return top == -1;
}