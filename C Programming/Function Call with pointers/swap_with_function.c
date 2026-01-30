#include <stdio.h>

// Function prototypes
void swap(int a, int b);        // Call by value
void _swap(int* a, int* b);    // Call by reference

int main() {
    int x = 5;
    int y = 10;

    // Call by value
    swap(x, y);
    // x and y will NOT change here
    printf("Inside main after swap: x = %d, y = %d\n", x, y);

    // Call by reference
    _swap(&x, &y);
    // x and y WILL change here
    printf("Inside main after _swap: x = %d, y = %d\n", x, y);

    return 0;
}

/*
   CALL BY VALUE
   Here copies of x and y are sent.
   Original values in main do NOT change.
*/
void swap(int a, int b) {
    int temp = a;
    a = b;
    b = temp;

    printf("Inside swap function: a = %d, b = %d\n", a, b);
}

/*
   CALL BY REFERENCE
   Here addresses of x and y are sent.
   So original values in main WILL change.
*/
void _swap(int* a, int* b) {
    int temp = *a;   // get value at address a
    *a = *b;        // put value of b into a
    *b = temp;      // put temp into b

    printf("Inside _swap function: a = %d, b = %d\n", *a, *b);
}
