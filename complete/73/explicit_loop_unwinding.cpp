// EXPLICIT LOOP UNWINDING
#include <iostream>

using namespace std;

// to see how the for loop simplifies any source code, we unwind the loop (1) to one using he goto statement (2) and one that doesn't use a loop at all. To run the code, only leave 1 segmenet uncommented.
int main() {

    // 1. for loop
    for(int i = 0; i < 5; i++) {
        cout << "General Kenobi" << endl;
    }
    cout << "Out of loop" << endl; 

    // 2. for loop goto variant
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

    // 3. for loop total unwinding
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

