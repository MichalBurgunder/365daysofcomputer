#include <iostream>
#include <cstdlib> // For rand() and RAND_MAX

using namespace std;

// void gotoExample() {
//     int step = 0;

// start:
//     switch (step) {
//         case 0:
//             std::cout << "Step 0: Start" << std::endl;
//             step = 1;
//             break;
//         case 1:
//             std::cout << "Step 1: Do something" << std::endl;
//             step = 2;
//             break;
//         case 2:
//             std::cout << "Step 2: Check condition" << std::endl;
//             if (someCondition()) {
//                 step = 1; // Goto step 1
//                 goto start;
//             } else {
//                 step = 3;
//                 goto start;
//             }
//             break;
//         case 3:
//             std::cout << "Step 3: End" << std::endl;
//             break;
//     }
// }

// bool someCondition() {
//     // Replace with your condition logic
//     return rand() % 2 == 0; // Randomly return true or false
// }

int main() {

    // while loop
    // while (true) {
    //     cout << "hello there" << endl;
    // }

    // // while loop goto variant
    // start_while:
    //     cout << "Hello there" << endl;
    //     goto start_while;



    // for loop
    for(int i = 0; i < 5; i++) {
        cout << "General Kenobi" << endl;
    }
    cout << "Out of loop" << endl; 

    // for loop goto variant
    int*i = new int(0);
    start_for:
        cout << "General Kenobi" << endl;
        *i = *i + 1;
        cout << *i << endl;
        if(*i < 5) {
            goto start_for;
        }
    delete i;
    cout << "Out of loop" << endl; 

    // for loop total unwinding
    int*i = new int(0);
    cout << "General Kenobi" << endl;
    *i = *i + 1;
    cout << "General Kenobi" << endl;
    *i = *i + 1;
    cout << "General Kenobi" << endl;
    *i = *i + 1;
    cout << "General Kenobi" << endl;
    *i = *i + 1;
    cout << "General Kenobi" << endl;
    *i = *i + 1;
    delete i;
    cout << "Out of loop" << endl; 

}

