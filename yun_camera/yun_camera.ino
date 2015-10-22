// Sketch to upload pictures to Dropbox when motion is detected
#include <Bridge.h>
#include <Process.h>

// Picture process
Process picture;

unsigned long time = 0;

void setup() {
  
  // Bridge
  Bridge.begin();
  
}

void wifiCheck() {
  Process wifiCheck;  // initialize a new process

  Serial.println();

  wifiCheck.runShellCommand("/usr/bin/pretty-wifi-info.lua");  // command you want to run

  // while there's any characters coming back from the
  // process, print them to the serial monitor:
  while (wifiCheck.available() > 0) {
    char c = wifiCheck.read();
    Serial.print(c);
  }

  Serial.println();

}

int idx = 10;
  
void loop(void) 
{
  
  //if (digitalRead(pir_pin) == true) {
  if (millis() > time + 10*1000) {
    wifiCheck();
    time = millis();
    
    // Take picture
    picture.runShellCommand("fswebcam -r 1280x720 /www/nice295/_pic.jpg --crop 300x400 /www/nice295/pic.jpg");
    while(picture.running());
    
    // Upload to Dropbox
    picture.runShellCommand("python /www/nice295/upload_picture.py " + String(idx) + " /www/nice295/pic.jpg");
    while(picture.running());

    Serial.print("Success to upload pic.jpg");
    Serial.println();    

    idx++;
  }
}
