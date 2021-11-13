// Name: Martin Czarnecki
// Email: martin.czarnecki99@myhunter.cuny.edu
// Date: November 13, 2021

#include <iostream>
#include <string.h>

int main(){

    int userInputTemp;

    std::cout << "Enter the temperature: ";
    std::cin >> userInputTemp;

    if(userInputTemp <= 32){ std::cout << "It's freezing!"; }
    else if(userInputTemp  < 68){ std::cout << "It's cold!"; }
    else if(userInputTemp < 73){ std::cout << "It's warm!"; }
    else{ std::cout << "It's hot!"; }
    
    return 0;
}