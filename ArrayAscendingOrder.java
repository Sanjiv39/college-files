import java.util.Arrays;

public class ArrayAscendingOrder {
    public static void main(String[] args) {
        int[] array = {5, 2, 9, 1, 7};

        // Print the original array
        System.out.println("Original array:");
        printArray(array);

        // Sort the array in ascending order
        Arrays.sort(array);

        // Print the sorted array
        System.out.println("\nArray in ascending order:");
        printArray(array);
    }

    // Method to print an array
    public static void printArray(int[] arr) {
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + " ");
        }
        System.out.println();
    }
}