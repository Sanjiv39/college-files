public class PrimeNumberAddition {
    public static void main(String[] args) {
        int count = 0; // Count of prime numbers found
        int sum = 0;   // Sum of prime numbers

        int number = 2; // Starting number to check for primality

        while (count < 10) {
            if (isPrime(number)) {
                sum += number;
                count++;
            }
            number++;
        }

        System.out.println("Sum of the first 10 prime numbers: " + sum);
    }

    // Function to check if a number is prime
    public static boolean isPrime(int n) {
        if (n <= 1) {
            return false;
        }
        if (n <= 3) {
            return true;
        }
        if (n % 2 == 0 || n % 3 == 0) {
            return false;
        }
        for (int i = 5; i * i <= n; i += 6) {
            if (n % i == 0 || n % (i + 2) == 0) {
                return false;
            }
        }
        return true;
    }
}