import java.util.Scanner;

class Student {
    private String name;
    private int age;
    private String grade;

    public void setName(String name) {
        this.name = name;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public void setGrade(String grade) {
        this.grade = grade;
    }

    public void displayRecord() {
        System.out.println("Name: " + name);
        System.out.println("Age: " + age);
        System.out.println("Grade: " + grade);
    }
}

public class StudentRecord {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Student student = new Student();

        System.out.println("Enter student details:");
        System.out.print("Name: ");
        String name = scanner.nextLine();
        student.setName(name);

        System.out.print("Age: ");
        int age = scanner.nextInt();
        student.setAge(age);

        scanner.nextLine(); // Consume newline left-over
        System.out.print("Grade: ");
        String grade = scanner.nextLine();
        student.setGrade(grade);

        System.out.println("\nStudent record:");
        student.displayRecord();

        scanner.close();
    }
}