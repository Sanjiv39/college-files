// Define the interface for banks
interface Bank {
    double getInterestRate();
}

// Implement the interface for each bank
class BankA implements Bank {
    @Override
    public double getInterestRate() {
        return 3.5; // Example interest rate for Bank A
    }
}

class BankB implements Bank {
    @Override
    public double getInterestRate() {
        return 4.0; // Example interest rate for Bank B
    }
}

class BankC implements Bank {
    @Override
    public double getInterestRate() {
        return 4.5; // Example interest rate for Bank C
    }
}

class BankD implements Bank {
    @Override
    public double getInterestRate() {
        return 5.0; // Example interest rate for Bank D
    }
}

class BankE implements Bank {
    @Override
    public double getInterestRate() {
        return 5.5; // Example interest rate for Bank E
    }
}

public class BankInterestRates {
    public static void main(String[] args) {
        // Create objects for each bank
        BankA bankA = new BankA();
        BankB bankB = new BankB();
        BankC bankC = new BankC();
        BankD bankD = new BankD();
        BankE bankE = new BankE();

        // Display interest rates for each bank
        System.out.println("Bank A interest rate: " + bankA.getInterestRate() + "%");
        System.out.println("Bank B interest rate: " + bankB.getInterestRate() + "%");
        System.out.println("Bank C interest rate: " + bankC.getInterestRate() + "%");
        System.out.println("Bank D interest rate: " + bankD.getInterestRate() + "%");
        System.out.println("Bank E interest rate: " + bankE.getInterestRate() + "%");
    }
}