# include <stdio.h>
# include <math.h>

int main() {
    int marks;
    printf("Enter your marks (0-100): ");
    scanf("%d", &marks);

    if (marks >= 0 && marks <= 30) {
        printf("Fail \n");
    } else if (marks > 30 && marks <= 100) {
        printf("Pass \n");
    } else {
        printf("Invalid marks entered. Please enter a value between 0 and 100.\n");
    }

    return 0;
}