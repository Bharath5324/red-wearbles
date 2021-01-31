#include <Hash.h> //using sha1 hash
#include <SPI.h> // SPI library- Serial Peripheral Interface Protocol
#include <MFRC522.h> // RFID library (https://github.com/miguelbalboa/rfid)
#include <NTPClient.h>
#include "FirebaseESP8266.h"
#include <ESP8266WiFi.h>
#include <WiFiUdp.h>

#define FIREBASE_HOST "https://nodemcu-1206.firebaseio.com/"      
#define FIREBASE_AUTH "YtEadYbnayiO7jIrytZo1z7eWaBJ3EjuQ8uUcFEk"            
#define WIFI_SSID "Tenda_2B1C00"                                  
#define WIFI_PASSWORD "Rex@mra81"

#define SS_PIN D4 //Slave Select
#define RST_PIN D2 // Reset Pin

WiFiUDP ntpUDP;
NTPClient timeClient(ntpUDP, "pool.ntp.org");

//Week Days
String weekDays[7]={"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"};

//Month names
String months[12]={"January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"};


MFRC522 mfrc522(SS_PIN, RST_PIN); // Set up mfrc522 on the Arduino
FirebaseData firebaseData;
FirebaseJson json;

void setup() {
  SPI.begin(); // open SPI connection
  mfrc522.PCD_Init();// Initialize Proximity Coupling Device (PCD)--to emit and capture EM waves
  Serial.begin(9600); // open serial connection
  
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);                                  
  Serial.print("Connecting to ");
  Serial.print(WIFI_SSID);
  while (WiFi.status() != WL_CONNECTED) {
    Serial.print(".");
    delay(500);
  }
 
  Serial.println();
  Serial.print("Connected");
  Serial.print("IP Address: ");
  Serial.println(WiFi.localIP());                               //prints local IP address
  Firebase.begin(FIREBASE_HOST, FIREBASE_AUTH);  // connect to the firebase
  // Initialize a NTPClient to get time
  timeClient.begin();
  // Set offset time in seconds to adjust for your timezone, for example:
  // GMT +1 = 3600
  // GMT +8 = 28800
  // GMT -1 = -3600
  // GMT 0 = 0
  timeClient.setTimeOffset(19800);//UTC to IST
 
}
 
void loop() {
  if (mfrc522.PICC_IsNewCardPresent()) { // (true, if RFID tag/card is present ) PICC = Proximity Integrated Circuit Card
    if(mfrc522.PICC_ReadCardSerial()) { // true, if RFID tag/card was read
      Serial.print("RFID TAG ID:");
      String id;
      for (byte i = 0; i < mfrc522.uid.size; ++i) { // read id (in parts)
          id= id + (mfrc522.uid.uidByte[i]); // 11 bit id
      }
      String resultid = sha1(id);//Encrypting id using SHA1 Algorithm
      Serial.println(" " + resultid); // Print out of encrypted id is complete.
      delay(1000);
      
      timeClient.update();
      unsigned long epochTime = timeClient.getEpochTime();
      
      struct tm *ptm = gmtime ((time_t *)&epochTime); 

      int monthDay = ptm->tm_mday;
      int currentMonth = ptm->tm_mon+1;
      int currentYear = ptm->tm_year+1900;
      //Print complete date:
      String currentDateandTime = String(currentYear) + "-" + String(currentMonth) + "-" + String(monthDay) + "  " + String(timeClient.getFormattedTime());
      Serial.print("Current date and time : ");
      Serial.println(currentDateandTime);

      Serial.println("");
      
      json.set("chipid",resultid);
      json.set("readerid","H101");
      json.set("timestamp",currentDateandTime);
      if (Firebase.pushJSON(firebaseData, "/rfid", json)){

  Serial.println(firebaseData.dataPath());

  Serial.println(firebaseData.pushName());

  Serial.println(firebaseData.dataPath() + "/"+ firebaseData.pushName());

} else {
  Serial.println(firebaseData.errorReason());
}

//  }
    }
  }
}
