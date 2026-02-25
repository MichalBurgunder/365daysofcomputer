// ACKERMANN FUNCTION DEMONSTRATION IN C++

#include <iostream>

using namespace std;

// an implementation of the ackermann function in C++. Even with a performance increase of almost 100 times compared to python, the ackermannn function still takes a chile to run. 
int ackermann(int x, int y) {
    if(x == 0){ 
        return y + 1;
    } else if (y == 0) {
        return ackermann(x-1,1);
    }
    return ackermann(x-1, ackermann(x,y-1));
}

int main() {
    int x1 = 4;
    int x2 = 2;

    cout << ackermann(x1,x2) << endl;
}