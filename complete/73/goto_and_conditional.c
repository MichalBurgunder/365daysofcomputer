// GOTO WITH CONDTIONAL DEMONSTRATION
#include  <stdio.h>

int main() {
    int i = 6;

    goto six;
    goto notsix;

    if(i == 6) {
        goto six;
    } else {
        goto notsix;
    }
    
    six:
    printf("It's 6\n");
    return 0;
    notsix:
    printf("It's not 6\n");
    return 0;
}


