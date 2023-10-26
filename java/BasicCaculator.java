// A basic calculator program in Java
import java.util.Scanner;

public class Calculator {

public static void main(String[] args) {
// Create a scanner object to read user input
Scanner scanner = new Scanner(System.in);

// Prompt the user to enter two numbers
System.out.println("Enter the first number:");
double num1 = scanner.nextDouble();
System.out.println("Enter the second number:");
double num2 = scanner.nextDouble();

// Prompt the user to enter an operator (+, -, , /)
System.out.println("Enter an operator (+, -,, /):");
char operator = scanner.next().charAt(0);

// Declare a v
ariable to store the result
double result;

// Perform the calculation based on the operator
switch (operator) {
case '+':
result = num1 + num2;
break;
case '-':
result = num1 - num2;
break;
case '':
result = num1 num2;
break;
case '/':
// Check if the second number is zero
if (num2 == 0) {
// Display an error message and exit the program
System.out.println("Cannot divide by zero");
return;
}
result = num1 / num2;
break;
default:
// Display an error message and exit the program
System.out.println("Invalid operator");
return;
}

// Display the result
System.out.println(num1 + " " + operator + " " +
num2 + " = " + result);
}
}
