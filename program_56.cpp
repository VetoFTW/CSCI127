// Name: Martin Czarnecki
// Email: martin.czarnecki99@myhunter.cuny.edu
// Date: November 13, 2021

#include <iostream>
#include <string.h>

int main(){

    int userInputNumber;
    std::string userInputString;

    std::cout << "Please enter a number: ";
    std::cin >> userInputNumber;
    std::cout << "Please type a word: ";
    std::cin >> userInputString;

    for(userInputNumber; userInputNumber > 0; userInputNumber -= 1){
        std::cout << std::to_string(userInputNumber) + "," << std::endl;
    }

    std::cout << "Time for " + userInputString + "!";

    return 0;
}