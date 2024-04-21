int status = 0;
int pir = 1; // PIR input
long led = 0;
void setup()
{
    pinMode(led, OUTPUT);
    pinMode(pir, INPUT);
    Serial.begin(9600);
}

void loop()
{
    status = digitalRead(pir);
    if (status == 1)
    {
        digitalWrite(led, HIGH);
        Serial.println("Object Detected");
    }
    else
    {
        digitalWrite(led, LOW);
        Serial.println("Object not Detected");
    };
    delay(1000);
}
