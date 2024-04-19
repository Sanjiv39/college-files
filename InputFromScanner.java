import java.util.Scanner;

public class InputFromScanner {
    public static void main(String[] args) {
        // Create a Scanner object to read input from the console
        Scanner scanner = new Scanner(System.in);

        // Prompt the user to enter their name
        System.out.print("Enter your name: ");

        // Read the input entered by the user
        String name = scanner.nextLine();

        // Display a greeting message with the entered name
        System.out.println("Hello, " + name + "!");

        // Close the scanner
        scanner.close();
    }
}