// LOOP UNWINDING

#include <iostream>
#include <cstdlib> // For rand() and RAND_MAX

using namespace std;

// main_unwinded is the function that is technically equivalent to main(), although because we are using goto statements to jump from one code location to another, it is very difficult to understand. See the main() function for a more intuitive implementation using loops.
int main_unwinded() {
    int small_number_1;
    int small_number_2;

    srand(time(0));
    first_while_loop:
        int i = rand();
        if (i < 200000) {
            small_number_1 = i;
            goto second_while_loop;
        } else {
            goto first_while_loop;
        }
    

    second_while_loop:
        int a = rand();
        if(a > 200000) {
            goto first_while_loop;
        }
        small_number_2 = a;
        
    cout << "The small number 1 is " << small_number_1 << endl;
    cout << "The small number 2 is " << small_number_2 << endl;
}


// random_small_numbers() is the heart of the mechanism, while main() serves as a abstraction layer to separate concerns
std::pair<int, int> random_small_numbers() {
    int i;
    int a;

    srand(time(0));
    while(true) {
        i = rand();
        if(i < 200000) {
            a = rand();
            if(a < 200000) {
                return std::make_pair(i, a);
            }
        }
    }
}

int main() {
    std::pair <int, int> numbers = random_small_numbers();

    cout << "The small number 1 is " << numbers.first << endl;
    cout << "The small number 2 is " << numbers.second << endl;
}