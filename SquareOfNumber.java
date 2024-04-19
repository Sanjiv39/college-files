public class SquareOfNumber {
    public static void main(String[] args) {
        // Check if there is exactly one command-line argument
        if (args.length != 1) {
            System.out.println("Usage: java SquareOfNumber <number>");
            return;
        }

        // Parse the command-line argument as an integer
        int number;
        try {
            number = Integer.parseInt(args[0]);
        } catch (NumberFormatException e) {
            System.out.println("Invalid input. Please provide a valid integer.");
            return;
        }

        // Calculate the square of the number
        int square = number * number;

        // Print the result
        System.out.println("Square of " + number + " is: " + square);
    }
}