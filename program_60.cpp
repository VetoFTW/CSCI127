// Name: Martin Czarnecki
// Email: martin.czarnecki99@myhunter.cuny.edu
// Date: November 13, 2021

#include <iostream>

int main(){

    int n, x, b = 16;

    std::cout << "Enter a number:  ";
    std::cin >> n;

    if(n < 0){
        std::cout << 1;
        x = 32 + n;
    } else{
        std::cout << 0;
        x = n;
    }

    while(b > 0.5){
        
        if(x >= b){
            std::cout << 1;
        }else{
            std::cout << 0;
        }

        x = x % b;
        b = b / 2;
    }

    std::cout << std::endl;

    return 0;
}