import java.util.Scanner;

public class FinallyBlockDemo {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        try {
            System.out.print("Enter a number: ");
            int number = scanner.nextInt();
            int result = 100 / number;
            System.out.println("Result of 100 divided by " + number + " is: " + result);
        } catch (ArithmeticException e) {
            System.out.println("ArithmeticException: Division by zero is not allowed.");
        } finally {
            // This block will always execute regardless of whether an exception occurs or not
            System.out.println("Finally block executed.");
            scanner.close();
        }
    }
}