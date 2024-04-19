import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class FactorialCalculatorGUI extends JFrame implements ActionListener {
    private JTextField numberField, resultField;
    private JButton calculateButton;

    public FactorialCalculatorGUI() {
        // Set up the frame
        setTitle("Factorial Calculator");
        setSize(300, 150);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null); // Center the frame

        // Create components
        JLabel numberLabel = new JLabel("Enter a number:");
        numberField = new JTextField(10);
        JLabel resultLabel = new JLabel("Factorial:");
        resultField = new JTextField(10);
        resultField.setEditable(false); // Make the result field read-only
        calculateButton = new JButton("Calculate");

        // Add action listener to the button
        calculateButton.addActionListener(this);

        // Create panel and add components
        JPanel panel = new JPanel();
        panel.setLayout(new GridLayout(3, 2));
        panel.add(numberLabel);
        panel.add(numberField);
        panel.add(resultLabel);
        panel.add(resultField);
        panel.add(calculateButton);

        // Add panel to frame
        add(panel);

        // Display the frame
        setVisible(true);
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        if (e.getSource() == calculateButton) {
            String input = numberField.getText();
            try {
                int number = Integer.parseInt(input);
                long factorial = calculateFactorial(number);
                resultField.setText(String.valueOf(factorial));
            } catch (NumberFormatException ex) {
                JOptionPane.showMessageDialog(this, "Invalid input. Please enter an integer.");
            }
        }
    }

    // Method to calculate factorial
    private long calculateFactorial(int number) {
        if (number < 0) {
            throw new IllegalArgumentException("Number must be non-negative");
        }
        long factorial = 1;
        for (int i = 2; i <= number; i++) {
            factorial *= i;
        }
        return factorial;
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> new FactorialCalculatorGUI());
    }
}