# Arduino Wireless Security Camera [![Build Status](https://travis-ci.org/openhomeautomation/arduino-yun-camera.svg)](https://travis-ci.org/openhomeautomation/arduino-yun-camera)

This is the code for the "Wireless Security Camera with the Arduino Yun" project. This project is about connecting a USB camera to the Arduino Yun to automatically upload pictures to Dropbox once movement is detected.

## I updated this project without SD card and with Parse
I try to use this project in just small memory.

## Tasks
1. Yun connected with Access point
2. Mac connected with Yun by SSH (root/arduino)
3. Install webcam related package (at /tmp)
   Refer to https://learn.adafruit.com/wireless-security-camera-arduino-yun/setting-up-your-arduino-yun
4. Insert SD card or conduct just in /tmp
5. Test (fswebcam test.png)
6. Check the result image by using Arduino web server
7. Sign up Parse
8. Write down Arduino sketch and download upload_picture.py in the Yun Linux


