public class CompileTimePolymorphism {
    // Method with one parameter
    public void display(int num) {
        System.out.println("Method with one parameter: " + num);
    }

    // Method with two parameters of different types
    public void display(String str) {
        System.out.println("Method with one parameter: " + str);
    }

    // Method with two parameters of the same type but different order
    public void display(int num, String str) {
        System.out.println("Method with two parameters: " + num + " and " + str);
    }

    // Method with two parameters of different types
    public void display(String str, int num) {
        System.out.println("Method with two parameters: " + str + " and " + num);
    }

    public static void main(String[] args) {
        CompileTimePolymorphism obj = new CompileTimePolymorphism();

        // Call each overloaded method
        obj.display(5);
        obj.display("Hello");
        obj.display(10, "World");
        obj.display("Java", 8);
    }
}