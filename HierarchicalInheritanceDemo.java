class Animal {
    void eat() {
        System.out.println("Animal is eating...");
    }
}

class Dog extends Animal {
    void bark() {
        System.out.println("Dog is barking...");
    }
}

class Cat extends Animal {
    void meow() {
        System.out.println("Cat is meowing...");
    }
}

public class HierarchicalInheritanceDemo {
    public static void main(String[] args) {
        Dog dog = new Dog();
        Cat cat = new Cat();

        // Calling methods from the Dog class
        System.out.println("Dog actions:");
        dog.eat(); // Inherited method from the Animal class
        dog.bark();

        // Calling methods from the Cat class
        System.out.println("\nCat actions:");
        cat.eat(); // Inherited method from the Animal class
        cat.meow();
    }
}