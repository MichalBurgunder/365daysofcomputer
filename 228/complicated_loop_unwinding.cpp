#include <iostream>
#include <cstdlib> // For rand() and RAND_MAX

using namespace std;


int main() {
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