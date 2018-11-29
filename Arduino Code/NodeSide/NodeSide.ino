
#include <ESP8266WiFi.h>
#include <WiFiClient.h> 
#include <ESP8266WebServer.h>
#include <ESP8266HTTPClient.h>
#include <SoftwareSerial.h>

SoftwareSerial s(D6, D5); // RX, TX
#define LED D0

/* Set these to your desired credentials. */
const char *ssid = "Conrad";  
const char *password = "conradworks";
String station, test;
const byte numChars = 126;
char receivedChars[numChars];
boolean newData = false;
int flag;
//const char *ssid = "ATT9S957g2";  //ENTER YOUR WIFI SETTINGS
//const char *password = "5a9w3x7=4b79";
//Web/Server address to read/write from 
const char *host = "https://go-environment.appspot.com/";   

String passed;
//=======================================================================
//                    Power on setup
//=======================================================================
 
void setup() {
  ESP.wdtDisable();
  delay(1000);
  Serial.begin(9600);
  //Serial1.begin(9600);
  s.begin(9600);
  pinMode(LED, OUTPUT);
  ESP.eraseConfig();
  WiFi.disconnect();
  WiFi.setAutoConnect(false);
  WiFi.setAutoReconnect(false);
  //WiFi.softAP(softAp_ssid.c_str());
  WiFi.mode(WIFI_OFF);        //Prevents reconnection issue (taking too long to connect)
  delay(1000);
  WiFi.mode(WIFI_STA);        //This line hides the viewing of ESP as wifi hotspot
  
  
  WiFi.begin(ssid, password);  
  Serial.println("");
 
  Serial.print("Connecting");
  // Wait for connection
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
 
  //If connection successful show IP address in serial monitor
  Serial.println("");
  Serial.print("Connected to ");
  Serial.println(ssid);
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());  
}
 String postData;
//=======================================================================
//                    Main Program Loop
//=======================================================================
void loop() {
  //disable watchdog on the nodeMCU to prevent random disconnections
  ESP.wdtDisable();
  HTTPClient http;    
  
  flag = 0;
  
  if (s.available()) 
  {
    flag=1;
  }
  recvWithStartEndMarkers();

}


void httpPostData()
{
    digitalWrite(LED, HIGH);
    HTTPClient http; 
    http.begin("http://go-environment.herokuapp.com/_stuff");
    http.addHeader("Content-Type", "application/x-www-form-urlencoded");         //Specify content-type header
    
    int httpCode = http.POST(receivedChars);   //Send the request
    String payload = http.getString();    //Get the response payload
   
    Serial.println(httpCode);   //Print HTTP return code
    Serial.println(payload);    //Print request response payload
   
    http.end();  //Close connection

    digitalWrite(LED, LOW);
    flag=0;
    ESP.wdtDisable();
}

void recvWithStartEndMarkers() 
{
    ESP.wdtDisable();
    static boolean recvInProgress = false;
    static byte ndx = 0;
    char startMarker = '<';
    char endMarker = '>';
    char rc;
 
    while (s.available() > 0 && newData == false) {
        rc = s.read();

        if (recvInProgress == true) {
            if (rc != endMarker) {
                receivedChars[ndx] = rc;
                ndx++;
                if (ndx >= numChars) {
                    ndx = numChars - 1;
                }
                break;
            }
            else {
                receivedChars[ndx] = '\0'; // terminate the string
                recvInProgress = false;
                ndx = 0;
                newData = true;
            }
        }

        else if (rc == startMarker) {
            recvInProgress = true;
        }
    }
    flag = 1;
    showNewData();
}

void showNewData() 
{
    if (newData == true) {

        httpPostData();
        newData = false;
    }
}

void oldway()
{
  if (s.available()) 
  {

    postData=s.readString();

    flag=1;
  }
}


