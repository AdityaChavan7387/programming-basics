# include<stdio.h>

// In Area of circle the value of pie is 3.14 and r square.

int main() {
    float radius;

    printf("Enter Radius :");
    scanf("%f", &radius);

    float Multiplication = radius * radius;
    printf("The Total Area Of circle is : %f", 3.14 * Multiplication);

    return 0;

}