#include <Adafruit_Sensor.h>
#include <DHT.h>
#include <DHT_U.h>
#include <Wire.h>
#include <Adafruit_BMP085.h>
#include <SoftwareSerial.h>

#define DHTPIN            2         // Pin which is connected to the DHT sensor.
// Type of sensor being used
#define DHTTYPE           DHT22     // DHT 22 (AM2302)
// OBJECT DECLARATIONS
DHT_Unified dht(DHTPIN, DHTTYPE);
Adafruit_BMP085 bmp;
//CONSTANTS
const int co2SensorIn = A0;  // CO2 sensor analog pin
const int smokeSensorIn = A2; // CO sensor analog pin
const int AOUTpin=1;//the AOUT pin of the co sensor goes into analog pin A0 of the arduino
const int DOUTpin=8;//the DOUT pin of the co sensor goes into digital pin D8 of the arduino
const int ledPin=13;//the anode of the LED connects to digital pin D13 of the arduino
// VARIABLES
uint32_t delayMS;
String data;
float temp, humi, pres, smoke, coConcentration;
int co2SensorValue, voltage_diference, coSensorValue, voltage_diferenceCO;
float voltage, co2Concentration, voltageCO;
int limit;
// Initial setup
 SoftwareSerial s(7, 6);
void setup() 
{
  // Serial data with 115200 BAUD
  Serial.begin(9600);
  Serial1.begin(9600); 
 
  s.begin(9600);
  // Initialize device.
  dht.begin();
  Serial.println("DHTxx Unified Sensor Example");

  sensor_t sensor;
  dht.temperature().getSensor(&sensor);

}
// Running program
void loop() {
  //****************TEMPERATURE READINGS*****************//
  // Get temperature event and print its value.
  sensors_event_t event;  
  dht.temperature().getEvent(&event);
  if (isnan(event.temperature)) 
  {
    Serial.println("Error reading temperature!");
  }
  else 
  {
      event.temperature;
    temp=event.temperature;
    temp = (temp * 1.8) + 32;
  }
  //****************HUMIDITY READINGS*******************//
  
  // Get humidity event and print its value.
  dht.humidity().getEvent(&event);
  if (isnan(event.relative_humidity)) 
  {
    Serial.println("Error reading humidity!");
  }
  else 
  {
      event.relative_humidity;
    humi=event.relative_humidity;
  }
  //****************PRESSURE READINGS******************//
  pres = bmp.readPressure();
  pres = pres - 130;
  //****************CHANGE TO SMOKE*****************//
  smoke = analogRead(smokeSensorIn);
  
  //****************CO2 READINGS*********************//
  //Read voltage
  co2SensorValue = analogRead(co2SensorIn);
  // The analog signal is converted to a voltage
  voltage = co2SensorValue*(5000/1024.0);
  if(voltage == 0)
  {
    Serial.println("Fault");
  }
  else if(voltage < 400)
  {
    Serial.println("preheating");
  }
  else 
  {
    voltage_diference=voltage-400;
    co2Concentration=voltage_diference*50.0/16.0; // <-------- EDIT THIS LINE FOR USABLE CO2 VALUES
  }
  //****************CO READINGS**********************//
  coSensorValue = analogRead(AOUTpin);//reads the analaog value from the hydrogen sensor's AOUT pin
  limit= digitalRead(DOUTpin);//reads the digital value from the hydrogen sensor's DOUT pin
  
  voltageCO = coSensorValue*(5000/1024.0);
  if(voltageCO == 0)
  {
    Serial.println("Fault");
  }
  else if(voltageCO < 400)
  {
    Serial.println("preheating");
  }
  else 
  {
    voltage_diferenceCO=voltageCO-600;
    coConcentration=voltage_diferenceCO*50.0/46.0; 
    if (coConcentration<0)
    {
      coConcentration = 0;
    }
  }
  // DATA to be sent to webpage
  data = "<" +String("Temperature=")+String(temp)
  +String("&Humidity=")+String(humi)
  +String("&Pressure=")+String(pres)
  +String("&Smoke=")+String(smoke)
  +String("&Co2=")+String(co2Concentration)
  +String("&Co=")+String(coConcentration)+">";
  Serial.println();
  Serial.println(data);
  //Serial.print("i got here!");
  s.println(data);
  s.println();
  
  // Delay between measurements.
  delay(800);
}
