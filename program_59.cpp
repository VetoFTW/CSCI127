// Name: Martin Czarnecki
// Email: martin.czarnecki99@myhunter.cuny.edu
// Date: November 13, 2021

#include <iostream>

int main(){

    double userInputMonthlyBudget, userInputWeeklySpending;

    std::cout << "Enter your monthly budget for food and coffee: ";
    std::cin >> userInputMonthlyBudget;
    std::cout << "How much are you spending in a week for coffee: ";
    std::cin >> userInputWeeklySpending;

    for(int i = 1; i <= 4; i++){
        std::cout << "Budget left after week " + std::to_string(i) + "    " + std::to_string(userInputMonthlyBudget - (userInputWeeklySpending * i)) << std::endl;
    }

    return 0;
}