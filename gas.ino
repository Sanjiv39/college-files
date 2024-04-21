int value = 0;
int gas = A0; // Gas input
long led = 0;
void setup()
{
  Serial.begin(9600);
  pinMode(led, OUTPUT);
  pinMode(gas, INPUT);
}

void loop()
{
  value = analogRead(gas);
  if(value < 100){
  	digitalWrite(led, LOW);
    Serial.print("Gas not detected : ");
    Serial.println(value);
  }else {
  	digitalWrite(led, HIGH);
    Serial.print("Gas detected : ");
    Serial.println(value);
  }
  
  delay(500);
  
}
