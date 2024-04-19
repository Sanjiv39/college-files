import java.util.Scanner;

public class ExceptionHandlingArithmetic {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Handle arithmetic exception
        try {
            System.out.print("Enter numerator: ");
            int numerator = scanner.nextInt();
            System.out.print("Enter denominator: ");
            int denominator = scanner.nextInt();

            int result = divide(numerator, denominator);
            System.out.println("Result of division: " + result);
        } catch (ArithmeticException e) {
            System.out.println("ArithmeticException: " + e.getMessage());
        }

        // Handle string exception
        try {
            System.out.print("Enter a string: ");
            String inputString = scanner.next();
            int integerValue = Integer.parseInt(inputString);
            System.out.println("Integer value entered: " + integerValue);
        } catch (NumberFormatException e) {
            System.out.println("NumberFormatException: Invalid input, please enter a valid integer.");
        }

        scanner.close();
    }

    // Method to perform division
    public static int divide(int numerator, int denominator) {
        return numerator / denominator;
    }
}