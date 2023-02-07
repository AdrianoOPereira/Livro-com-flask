void setup() {
  Serial.begin(9600);
  pinMode(4, OUTPUT);
}


void loop() {
  if (Serial.available() > 0){
    int dado = Serial.read();
    if (dado == '1')digitalWrite(4, HIGH);
    else if (dado == '0')digitalWrite(4, LOW);      
  } 
}
