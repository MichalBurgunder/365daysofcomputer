#include <iostream>

using namespace std;

int ackermann(int x, int y) {
    if(x == 0){ 
        return y + 1;
    }
     
    if (y == 0) {
        return ackermann(x-1,1);
    }
        
    return ackermann(x-1, ackermann(x,y-1));
}

int main() {
    cout << ackermann(4,2) << endl;
}