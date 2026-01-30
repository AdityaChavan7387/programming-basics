# include<stdio.h>

void square(int n);
void _square(int* n);

int main () {

    int number = 4;
    square(number);
    printf("The Number is: %d\n", number);

    _square(&number);
    printf("The Number is: %d\n", number);
    return 0;

}

// Function that attempts to square the number but does not modify the original variable
// called by value
void square(int n) {
    n = n * n;
    printf("The Number inside square function is: %d\n", n);
}

// Function that squares the number and modifies the original variable
// called by reference using pointer
void _square(int* n) {
    *n = (*n) * (*n);
    printf("The Number inside _square function is: %d\n", *n);
}