# include<stdio.h>

int main() {
    int var = 3000;

    // pointer to var
    int *ptr = &var;

    // pointer to pointer ptr
    int **pptr = &ptr;

    // Displaying the value of var using pptr
    printf("Value of var = %d\n", var);
    printf("Value of var using single pointer ptr = %d\n", *ptr);
    printf("Value of var using double pointer pptr = %d\n", **pptr);

    return 0;
}
