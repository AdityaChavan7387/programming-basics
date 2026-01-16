# include<stdio.h>

void printNamaste();
void printBonjour();

int main()
{
    printf("Enter f for french & i for indian: ");
    char choice;
    scanf(" %c", &choice);

    if(choice == 'i'){
        printNamaste();
    }
    else if(choice == 'f'){
        printBonjour();
    }
    else{
        printf("Invalid choice\n");
    }
    return 0;
}

void printNamaste()
{
    printf("Namaste\n");
}

void printBonjour()
{
    printf("Bonjour\n");
}
