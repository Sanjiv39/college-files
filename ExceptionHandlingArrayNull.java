import java.util.Scanner;

public class ExceptionHandlingArrayNull {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Handle string exception
        try {
            System.out.print("Enter a string: ");
            String inputString = scanner.nextLine();
            System.out.println("Length of the input string: " + inputString.length());
        } catch (NullPointerException e) {
            System.out.println("NullPointerException: String is null.");
        }

        // Handle array exception
        try {
            int[] numbers = {1, 2, 3, 4, 5};
            System.out.print("Enter an index to access the array: ");
            int index = scanner.nextInt();
            System.out.println("Element at index " + index + ": " + numbers[index]);
        } catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("ArrayIndexOutOfBoundsException: Invalid index.");
        }

        scanner.close();
    }
}
