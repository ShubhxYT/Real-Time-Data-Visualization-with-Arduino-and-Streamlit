#include <DHT.h>
#include <Servo.h>

#define DHTPIN 9
#define DHTTYPE DHT11
DHT dht(DHTPIN, DHTTYPE);

Servo myServo;

const int trigPin = 10;
const int echoPin = 11;
long duration;
int distance;

int gas = A1;

int tds = A0;
const float VREF = 5.0;
const float ADCRANGE = 1024;
const float tdsfactor = 0.5;


void setup() {
  Serial.begin(9600);
  pinMode(gas, INPUT);
  pinMode(tds, INPUT);

  myServo.attach(12);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  dht.begin();
}

void loop() {
  

  radar();
  // Serial.println("");
  // delay(1000);
}

void gas_dth_tds(){
  int tds_read = analogRead(tds);
  float voltage = tds_read * (VREF / ADCRANGE);
  int tds_value = (voltage * tdsfactor) * 1000;

  Serial.print("tds,");
  Serial.print(tds_value);
  Serial.print(",");

  int humi = dht.readHumidity(0);
  Serial.print("Hum,");
  Serial.print(humi);
  Serial.print(",");

  int temp = dht.readTemperature();
  Serial.print("Temp,");
  Serial.print(temp);
  Serial.print(",");

  int gas_value = analogRead(gas);
  Serial.print("gas,");
  Serial.print(gas_value);
  Serial.print(",");
}

void radar() {
  for (int i = 5; i <= 165; i++) {
    gas_dth_tds();
    myServo.write(i);
    delay(90);
    distance = calculateDistance();
    Serial.print("Angle,");
    Serial.print(i);
    Serial.print(",");
    Serial.print("Distance,");
    Serial.print(distance);
    Serial.println("");
  }
  for (int i = 165; i > 15; i--) {
    gas_dth_tds();
    myServo.write(i);
    delay(90);
    distance = calculateDistance();
    Serial.print("Angle,");
    Serial.print(i);
    Serial.print(",");
    Serial.print("Distance,");
    Serial.print(distance);
    Serial.println("");
  }
}

int calculateDistance() {

  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  // Sets the trigPin on HIGH state for 10 micro seconds
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  duration = pulseIn(echoPin, HIGH);  // Reads the echoPin, returns the sound wave travel time in microseconds
  distance = duration * 0.034 / 2;
  return distance;
}
