# include <stdio.h>
# include <math.h>

int main() {
    int x;
    printf("Enter a Marks; ");
    scanf("%d", &x);
    if (x > 30 && x<100) {
        printf("The Marks Higher Than 30 And The Student Passed.\n");
    } else {
        printf("The Marks Are Less Than 30 And The Student Failed.\n");
    }
    int age;
    printf("Enter Your Age; ");
    scanf("%d", &age);
    if (age >= 18) {
        printf("You are Eligible for Voting.\n");
    } else {
        printf("You are Not Eligible for Voting.\n");
    }
    return 0;
}