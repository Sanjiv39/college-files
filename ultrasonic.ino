int signal = 4; // transmitter
int echo = 11;  // receiver

void setup()
{
  pinMode(signal, OUTPUT);
  pinMode(echo, INPUT);
  Serial.begin(9600);
}

void loop()
{
  // reset transmitter initially
  digitalWrite(signal, LOW);
  delayMicroseconds(2);

  // send high signal via transmitter
  digitalWrite(signal, HIGH);
  delayMicroseconds(10);
  digitalWrite(signal, LOW);

  // recieve the received signal
  long distance = pulseIn(echo, HIGH) * 0.0344 / 2;
  Serial.print("Duration ");
  Serial.print(distance);
  Serial.print("cm\n");
  delay(3000);
}