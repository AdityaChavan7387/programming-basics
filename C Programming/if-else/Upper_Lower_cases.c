# include<stdio.h>

int main() {
    char ch;
    printf("Enter a character: ");
    scanf("%c", &ch);

    if (ch >= 'A' && ch <= 'Z') {
        printf("The character '%c' is an Uppercase letter.\n", ch);
    } else if (ch >= 'a' && ch <= 'z') {
        printf("The character '%c' is a Lowercase letter.\n", ch);
    } else {
        printf("The character '%c' is neither an Uppercase nor a Lowercase letter.\n", ch);
    }

    return 0;
}