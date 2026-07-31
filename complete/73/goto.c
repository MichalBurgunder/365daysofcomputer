// GOTO EXAMPLE
#include  <stdio.h>

// as code is execute from the top line downards, line 10 marks a point in the
// code where we can return to by invoking the 'goto' command. As a result, this
// program will run forever. You can verify this yourself uncommenting line 15
// and running the program. 

int main() {
    basic_goto: 

    // ...
    // ...some code...
    // ...
    printf("Hello there");

    goto basic_goto;

    return 0;
}


