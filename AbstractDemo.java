// Abstract class
abstract class Shape {
    // Abstract method
    abstract double calculateArea();
    
    // Concrete method
    void display() {
        System.out.println("This is a shape.");
    }
}

// Concrete subclass extending the abstract class
class Circle extends Shape {
    // Implementation of abstract method
    double radius;

    Circle(double radius) {
        this.radius = radius;
    }

    @Override
    double calculateArea() {
        return Math.PI * radius * radius;
    }
}

// Concrete subclass extending the abstract class
class Rectangle extends Shape {
    // Implementation of abstract method
    double length;
    double width;

    Rectangle(double length, double width) {
        this.length = length;
        this.width = width;
    }

    @Override
    double calculateArea() {
        return length * width;
    }
}

public class AbstractDemo {
    public static void main(String[] args) {
        // Creating objects of concrete subclasses
        Circle circle = new Circle(5);
        Rectangle rectangle = new Rectangle(4, 6);

        // Calling abstract method and concrete method
        System.out.println("Area of circle: " + circle.calculateArea());
        circle.display();

        System.out.println("Area of rectangle: " + rectangle.calculateArea());
        rectangle.display();
    }
}