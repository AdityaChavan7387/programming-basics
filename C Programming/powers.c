# include <stdio.h>
# include <math.h>

// In This we Will Test How Pow (Power) actually works for example x is the power of y let's test this.

int main(){
    int a, b, c;
    
    printf("Enter Value Of a :");
    scanf("%d", &a);

    printf("Enter Value Of b :");
    scanf("%d", &b);

    c = pow(a, b);

    printf("The Result Of %d raised to the power of %d is: %d\n", a, b, c);

    return 0;
}