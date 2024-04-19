// Define interfaces for the different behaviors
interface Interface1 {
    void method1();
}

interface Interface2 {
    void method2();
}

// Implement the interfaces in a single class
class MyClass implements Interface1, Interface2 {
    @Override
    public void method1() {
        System.out.println("Method 1 implementation");
    }

    @Override
    public void method2() {
        System.out.println("Method 2 implementation");
    }
}

public class MultipleInheritanceInterface {
    public static void main(String[] args) {
        // Create an object of the class implementing the interfaces
        MyClass obj = new MyClass();

        // Call methods defined in each interface
        obj.method1();
        obj.method2();
    }
}