public class StringConcatenation {
    public static void main(String[] args) {
        String str1 = "Hello";
        String str2 = "World";
        
        // Concatenating strings using the + operator
        String result1 = str1 + " " + str2;
        System.out.println("Result 1: " + result1);
        
        // Concatenating strings using the concat() method
        String result2 = str1.concat(" ").concat(str2);
        System.out.println("Result 2: " + result2);
    }
}