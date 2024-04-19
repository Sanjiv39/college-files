class MyClass {
    // Data members
    private int number;
    private String name;

    // Constructor
    public MyClass(int number, String name) {
        this.number = number;
        this.name = name;
    }

    // Member function to display data members
    public void display() {
        System.out.println("Number: " + number);
        System.out.println("Name: " + name);
    }
}

public class AccessClassMembers {
    public static void main(String[] args) {
        // Creating an object of MyClass
        MyClass obj = new MyClass(123, "John");

        // Accessing data members
        System.out.println("Accessing data members:");

        // Accessing member function
        System.out.println("\nAccessing member function:");
        obj.display();
    }
}