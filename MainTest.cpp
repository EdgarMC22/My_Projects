#include <iostream>
#include <iomanip>
#include <vector>
#include <fstream>
#include <string>

#include "MyInfixCalculator_e272m757.h"

using namespace std;

int main(int argc, char* argv[])
{
    
    string str;
    cout << "Enter an equation to be solved: "; 
    cin >> str; 
    MyInfixCalculator infix_calculator;
    
    double a = infix_calculator.calculate(str);
    std::cout.precision(3);
    cout << std::fixed << a << endl;
    

    return 0;
}
