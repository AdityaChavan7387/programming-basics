# include<stdio.h>

int main() {
    int n;

    do {
        printf("Enter a number: ");
       scanf("%d", &n);
       printf("You entered: %d\n", n);

         if (n % 2 != 0) {
              break;
         }
    } while (1);

    printf("Odd number entered, exiting loop.\n");
    return 0;
    
}