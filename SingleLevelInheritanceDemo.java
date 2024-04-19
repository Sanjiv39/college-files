class Parent {
    void displayParent() {
        System.out.println("This is the parent class.");
    }
}

class Child extends Parent {
    void displayChild() {
        System.out.println("This is the child class.");
    }
}

public class SingleLevelInheritanceDemo {
    public static void main(String[] args) {
        Parent parent = new Parent();
        Child child = new Child();

        // Calling methods from the parent class
        parent.displayParent();

        // Calling methods from the child class
        child.displayParent(); // Inherited method from the parent class
        child.displayChild();
    }
}