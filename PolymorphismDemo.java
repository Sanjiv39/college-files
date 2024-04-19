// Parent class
class Animal {
    // Method to make sound
    public void makeSound() {
        System.out.println("Animal makes a sound");
    }
}

// Subclass Dog
class Dog extends Animal {
    // Overriding the makeSound method of the parent class
    @Override
    public void makeSound() {
        System.out.println("Dog barks");
    }
}

// Subclass Cat
class Cat extends Animal {
    // Overriding the makeSound method of the parent class
    @Override
    public void makeSound() {
        System.out.println("Cat meows");
    }
}

public class PolymorphismDemo {
    public static void main(String[] args) {
        // Creating objects of different classes
        Animal animal1 = new Animal();
        Animal animal2 = new Dog(); // Upcasting
        Animal animal3 = new Cat(); // Upcasting

        // Calling makeSound method of each object
        animal1.makeSound(); // Calls method from Animal class
        animal2.makeSound(); // Calls method from Dog class
        animal3.makeSound(); // Calls method from Cat class
    }
}