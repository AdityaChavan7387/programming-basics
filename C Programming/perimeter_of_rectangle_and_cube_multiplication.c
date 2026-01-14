# include <stdio.h>

// perimeter of rectangle formula is p = 2 * (a + b)

int main () {
    float a , b , perimeter;
    
    printf("Enter Perimeter for a side :");
    scanf("%f", &a);
     
    printf("Enter Perimeter for b side :");
    scanf("%f", &b);

    perimeter = 2 * (a + b);
    printf("The perimeter of Rectangle is : %f \n", perimeter);

    int c , cube;

    printf("Enter c value :");
    scanf("%d", &c);
    
    cube = c * c * c;
    printf("The Total Cube is : %d", cube);

    return 0;

}