# include<stdio.h>

int main(){

    int age = 23;
    int *ptr = &age;
    int _age = *ptr;

    printf("Value of age: %d\n", age);
    printf("Address of age: %p\n", &age);
}