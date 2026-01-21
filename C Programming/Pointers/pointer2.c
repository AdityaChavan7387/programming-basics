#include<stdio.h>

int main(){

    int x;
    int *ptr;

    ptr = &x; // Assigning the address of x to pointer ptr
    *ptr = 4; // Assigning value 42 to the location pointed by ptr

    printf("Value of x: %d\n", x); // Output the value of x
    printf("Value via pointer ptr: %d\n", *ptr); // Output the value via pointer


    return 0;
}