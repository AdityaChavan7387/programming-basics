# include <stdio.h>
# include <math.h>

int main() {
    int x;
    printf("Enter a Number; ");
    scanf("%d", &x);
    if (x > 9 && x<100) {
        printf("The number is Higher Than 9 And is True.\n");
    } else {
        printf("The number is either Less Than 9 or Higher Than 100 So it is False.\n");
    }
    return 0;
}
    