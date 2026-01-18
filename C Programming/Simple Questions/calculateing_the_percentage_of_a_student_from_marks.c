#include <stdio.h>

float calculatePercentage(float science, float math, float sanskrit) {
    float total = science + math + sanskrit;
    return (total / 300) * 100;   // assuming each subject is out of 100
}

int main() {
    float science, math, sanskrit;

    printf("Enter marks in Science: ");
    scanf("%f", &science);

    printf("Enter marks in Math: ");
    scanf("%f", &math);

    printf("Enter marks in Sanskrit: ");
    scanf("%f", &sanskrit);

    printf("Percentage: %.2f%%\n", calculatePercentage(science, math, sanskrit));

    return 0;
}
