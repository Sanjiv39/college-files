
// Define pin numbers for LED output
#define LED0 2
#define LED1 3
#define LED2 4
#define LED3 5

void setup()
{
    // Initialize LED pins as output
    pinMode(LED0, OUTPUT);
    pinMode(LED1, OUTPUT);
    pinMode(LED2, OUTPUT);
    pinMode(LED3, OUTPUT);
}

void loop()
{
    // Count from 15 (binary 1111) to 0 (binary 0000)
    for (int count = 15; count >= 0; count--)
    {
        // Extract individual bits of the count value
        int bit3 = (count >> 3) & 1;
        int bit2 = (count >> 2) & 1;
        int bit1 = (count >> 1) & 1;
        int bit0 = count & 1;

        // Display the bits on LEDs
        digitalWrite(LED0, bit0);
        digitalWrite(LED1, bit1);
        digitalWrite(LED2, bit2);
        digitalWrite(LED3, bit3);

        // Delay to observe the output
        delay(500);
    }
}
