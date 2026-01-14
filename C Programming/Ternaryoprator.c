# include <stdio.h>
# include <math.h>

int main() {
    int x;
    printf("Enter a Marks; ");
    scanf("%d", &x);
    x>30 && x<100 ? printf("The Marks Higher Than 30 And The Student Passed.\n") : printf("The Marks Are Less Than 30 And The Student Failed.\n"); 
    return 0;
}