#include <iostream>
#include <unistd.h>

using namespace std;

// # when compiling this program and anaylzing the output program with lldb, we get the text saved in mem_dump.txt
int main()
{
  cout << "This is data written directly into RAM" << endl;

 while (true) {
    int i = 9;
 }

  cout << "...done! Exiting";
  return 0;
}