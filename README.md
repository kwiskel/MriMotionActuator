# MriMotionActuator

ECE 492 Capstone Project - University of Alberta

NodeRed:
https://nodered.org/docs/user-guide/

Steps:

1. Plug in Raspberry Pi
2. From personal computer open chrome: http://192.168.1.71:1880/
3. Login with username: raspberrypi and password: raspberrypi - admin account
4. Flow credentials key: mrimotionactuator
5. Create an SSH key to allow push to remote github repo, passphrase: mrimotionactuator

Settings that should be enabled in NodeRed: - see settings.js file

To Setup Raspberry Pi:
follow this: https://nodered.org/docs/getting-started/raspberrypi
and enable autostart on boot by running: sudo systemctl enable nodered.service
