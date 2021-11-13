// Name: Martin Czarnecki
// Email: martin.czarnecki99@myhunter.cuny.edu
// Date: November 12, 2021

#include <iostream>
#include <iomanip>
using namespace std;

int main(){

    double userInput;
    double cryptoConversion[] = {31901.19, 1901.54, 0.179733};

    cout << "Enter amount in cryptocurrency: ";
    cin >> userInput;

    cout << fixed << setprecision(2) << userInput << " BTC in USD: " << userInput * cryptoConversion[0] << "\n";
    cout << fixed << setprecision(2) << userInput << " ETH in USD: " << userInput * cryptoConversion[1] << "\n";
    cout << fixed << setprecision(2) << userInput << " DOGE in USD: " << userInput * cryptoConversion[2] << "\n";

    return 0;
}