#include <Arduino.h>
#include <ESP8266WiFi.h>
#include <WiFiClient.h>
#include <Ticker.h> 

#define WIFISSID "YOUR WIFI SSID"
#define PASSWD  "YOUR WIFI PASSWD"
String Key = "微信获取Key进行替换";

const char *host = "www.rykj.xyz";
String comdata = "";
String KeyMark = "<key>"+Key+"</key>";

Ticker flipper;
WiFiClient client;

void flip() {
   client.print(KeyMark);
}

void setup()
{
    Serial.begin(115200);
    Serial.println("Connecting...\n");
    WiFi.mode(WIFI_STA);
    WiFi.begin(WIFISSID,PASSWD); // change it to your ussid and password
    while (WiFi.status() != WL_CONNECTED)
    {
        delay(500);
        Serial.print(".");
    }
    if (!client.connect("www.rykj.xyz", 443))
    {
        Serial.println("Connection to host failed");
        delay(1000);
        return;
    }
    else{
          client.print(KeyMark);
      }
    flipper.attach(180, flip);//每隔0.5秒执行一次回调函数
}

void loop()
{
  while (Serial.available() > 0)  
    {
        comdata += char(Serial.read());
        delay(2);
    }
    while (client.available() > 0)
        {
          char c = client.read();
          Serial.write(c);
        }
    if (comdata.length() > 0)
    {
        String SendMsg = comdata + KeyMark;
        Serial.println(SendMsg);
        client.print(SendMsg);
        comdata = "";
    }

}
  
