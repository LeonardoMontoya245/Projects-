#include <iostream>
#include <cmath>
#include <limits>

using namespace std;

void displayOp() {
    cout << "\nReal Calculator in C++" << endl;
    cout << "------------------------" << endl;
    cout << "Available operations:" << endl;
    cout << "+ : Addition" << endl;
    cout << "- : Subtraction" << endl;
    cout << "* : Multiplication" << endl;
    cout << "/ : Division" << endl;
    cout << "^ : Power" << endl;
    cout << "% : Modulus (integers only)" << endl;
    cout << "sqrt : Square root" << endl;
    cout << "log : Logarithm (base 10)" << endl;
    cout << "sin : Sine (radians)" << endl;
    cout << "cos : Cosine (radians)" << endl;
    cout << "tan : Tangent (radians)" << endl;
    cout << "exit : Exit the program" << endl;
    cout << "------------------------" << endl;
}

int main() {
    string operation;
    double number1, number2;

    while (true) {
        displayOp();
        cout << "Enter operation: ";
        cin >> operation;

        if (operation == "exit") {
            cout << "Exiting the calculator. Goodbye!" << endl;
            break;
        }

        if (operation == "sqrt" || operation == "log" || 
            operation == "sin" || operation == "cos" || operation == "tan") {
            
            cout << "Enter the number: ";
            cin >> number1;

            if (operation == "sqrt") {
                if (number1 < 0) cout << "ERROR: Square root of negative number is not allowed." << endl;
                else cout << "Result: " << sqrt(number1) << endl;
            } 
            else if (operation == "log") {
                if (number1 <= 0) cout << "ERROR: Logarithm of non-positive number is not allowed." << endl;
                else cout << "Result: " << log10(number1) << endl;
            } 
            else if (operation == "sin") cout << "Result: " << sin(number1) << endl;
            else if (operation == "cos") cout << "Result: " << cos(number1) << endl;
            else if (operation == "tan") cout << "Result: " << tan(number1) << endl;
        } 
        else if (operation == "+" || operation == "-" || operation == "*" || 
                 operation == "/" || operation == "^" || operation == "%") {
            
            cout << "Enter the first number: ";
            cin >> number1;
            cout << "Enter the second number: ";
            cin >> number2;

            if (operation == "+") cout << "Result: " << number1 + number2 << endl;
            else if (operation == "-") cout << "Result: " << number1 - number2 << endl;
            else if (operation == "*") cout << "Result: " << number1 * number2 << endl;
            else if (operation == "/") {
                if (number2 == 0) cout << "ERROR: Division by zero is not allowed." << endl;
                else cout << "Result: " << number1 / number2 << endl;
            } 
            else if (operation == "^") cout << "Result: " << pow(number1, number2) << endl;
            else if (operation == "%") {
                int a = static_cast<int>(number1);
                int b = static_cast<int>(number2);
                if (b == 0) cout << "ERROR: Modulus by zero is not allowed." << endl;
                else cout << "Result: " << a % b << endl;
            }
        } 
        else {
            cout << "ERROR: Invalid operation. Please try again." << endl;
        }
    }

    return 0;
}
