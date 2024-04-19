import java.util.Scanner;

public class AreaCalculator {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Calculate area of rectangle
        System.out.println("Rectangle:");
        System.out.print("Enter length: ");
        double length = scanner.nextDouble();
        System.out.print("Enter width: ");
        double width = scanner.nextDouble();
        double rectangleArea = calculateRectangleArea(length, width);
        System.out.println("Area of rectangle: " + rectangleArea);

        // Calculate area of circle
        System.out.println("\nCircle:");
        System.out.print("Enter radius: ");
        double radius = scanner.nextDouble();
        double circleArea = calculateCircleArea(radius);
        System.out.println("Area of circle: " + circleArea);

        scanner.close();
    }

    public static double calculateRectangleArea(double length, double width) {
        return length * width;
    }

    public static double calculateCircleArea(double radius) {
        return Math.PI * radius * radius;
    }
}