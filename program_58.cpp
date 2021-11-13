// Name: Martin Czarnecki
// Email: martin.czarnecki99@myhunter.cuny.edu
// Date: November 13, 2021

#include <iostream>

int main(){

    int userInputNum, i, j;
    char userInputChr;

    std::cout << "Please enter a number: ";
    std::cin >> userInputNum;
    std::cout << "Please enter a character: ";
    std::cin >> userInputChr;

    for(i = 1; i <= userInputNum; i++){
        for(j = 1; j <= i; j++){
            std::cout << userInputChr;
        }
        std::cout << std::endl;
    }

    for(i = 1; i <= userInputNum; i++){
        for(j = 1; j <= userInputNum; j++){
            std::cout << userInputChr;
        }
        std::cout << std::endl;
    }

    return 0;
}