const int ldr = A0; // LDR input
const int led = 0;
int val = 0;

void setup()
{
    pinMode(ldr, INPUT);
    pinMode(led, OUTPUT);
    Serial.begin(9600);
}

void loop()
{
    val = analogRead(ldr); // Reads the LDR value (0-1023)

    if (val < 400)
    {
        digitalWrite(led, HIGH);
        Serial.println("Light not detected!");
    }
    else
    {
        digitalWrite(led, LOW);
        Serial.println("Light detected!");
    }

    delay(500);
}
