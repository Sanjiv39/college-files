public class Print2DArray {
    public static void main(String[] args) {
        int[][] matrix = {
            {1, 2, 3},
            {4, 5, 6},
            {7, 8, 9}
        };

        // Iterate over each row
        for (int i = 0; i < matrix.length; i++) {
            // Iterate over each column in the current row
            for (int j = 0; j < matrix[i].length; j++) {
                // Print the element at current row and column
                System.out.print(matrix[i][j] + " ");
            }
            // Move to the next line after printing all elements in the row
            System.out.println();
        }
    }
}