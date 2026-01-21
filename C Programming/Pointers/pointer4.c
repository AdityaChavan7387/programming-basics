#include<stdio.h>

int main(){

    int x;
    int *ptr;

    ptr = &x; // Assigning the address of x to pointer ptr
    *ptr = 10; // Assigning value 10 to the location pointed to by ptr
    (*ptr)++; // Incrementing the value at the address pointed to by ptr

    printf("Value of x: %d\n", x); // Output the value of x
    printf("Value via pointer ptr: %d\n", *ptr); // Output the value via pointer ptr


    return 0;
}