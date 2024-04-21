const int input = A0; // Temperature input
const int led = 0;
int val = 0;

void setup()
{
    pinMode(input, INPUT);
    pinMode(led, OUTPUT);
    Serial.begin(9600);
}

void loop()
{
    val = map(((analogRead(input) - 20) * 3.04), 0, 1023, 40, 125);
    Serial.print("Temperature : ");
    Serial.print(val);
    Serial.println(" C");
    delay(1000);
}
