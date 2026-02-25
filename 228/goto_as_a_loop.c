// LOOPING TO FIND A NUMBER
#include  <stdio.h>

// when programs try and find an element in an array or a list, they do so with a loop like the one below. instead of using a while loop, we use the goto statment instead, which is functionally equivalent here.
int main() {
    int i = 0;
    unsigned char arr[] = {
        0b11011000, // 216   
        0b11001011, // 203
        0b00110110, // 54
        0b00101011  // 43
    };

    char task = 0b00110110; // 54
    char result;

    goto start;
    
    start:
        result = task ^ arr[i]; // XORing every bit

        if(result == 0x00000000) {
            printf("%d\n", i);
            return 0;
        }
        i++;
    goto start;
}




