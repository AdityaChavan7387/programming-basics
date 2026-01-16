# include<stdio.h>

//declaration of function/ prototype

void printHello();

int main(){

    //function call
    printHello();
    printHello();
    return 0;
}

//function definition
void printHello(){
    printf("Hello, World!\n");
    printf("Welcome to C programming.\n");
}