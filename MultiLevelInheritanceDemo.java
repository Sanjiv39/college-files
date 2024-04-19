class GrandParent {
    void displayGrandParent() {
        System.out.println("This is the grandparent class.");
    }
}

class Parent extends GrandParent {
    void displayParent() {
        System.out.println("This is the parent class.");
    }
}

class Child extends Parent {
    void displayChild() {
        System.out.println("This is the child class.");
    }
}

public class MultiLevelInheritanceDemo {
    public static void main(String[] args) {
        GrandParent grandParent = new GrandParent();
        Parent parent = new Parent();
        Child child = new Child();

        // Calling methods from the grandparent class
        grandParent.displayGrandParent();

        // Calling methods from the parent class
        parent.displayGrandParent(); // Inherited method from the grandparent class
        parent.displayParent();

        // Calling methods from the child class
        child.displayGrandParent(); // Inherited method from the grandparent class via parent class
        child.displayParent(); // Inherited method from the parent class
        child.displayChild();
    }
}