void setup()
{
    pinMode(0, OUTPUT);
    pinMode(1, OUTPUT);
    pinMode(2, OUTPUT);
}

void turn_on(int pin, bool allOf = true)
{
    if (allOf)
    {
        for (int i = 0; i < 3; i++)
        {
            digitalWrite(i, LOW);
        }
    }
    digitalWrite(pin, HIGH);
}

void patterns()
{
    for (int i = 0; i < 2; i++)
    {
        for (int i = 0; i < 3; i++)
        {
            turn_on(i);
            delay(1000);
        }
    }
    for (int i = 0; i < 5; i++)
    {
        for (int i = 0; i < 3; i++)
        {
            turn_on(i);
            turn_on((i + 1) % 3, false);
            delay(300);
        }
    }
    for (int i = 0; i < 20; i++)
    {
        for (int i = 0; i < 3; i++)
        {
            turn_on(i);
            delay(100);
        }
    }
}

void loop()
{
    patterns();
    delay(1000);
}
