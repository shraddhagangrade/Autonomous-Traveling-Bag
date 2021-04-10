# AutonomousTravelBag



1-SIM7000E NB-IoT/LTE/GPRS/GPS Expansion Shield :
        Used for tracking the pin point cordinates, in case of theft and also
        aids to maintain minimum distance between user and bag. 


2-LSM303-Triple-axis Accelerometer+Magnetometer (Compass) Board :
        Direction decision - LSM303 readings compared with mobile device magnetometer readings to derive an 
        offset(a range until which it will not change the direction)
        in which it has to traverse which is of approx 30° calculated (Bn-Mn)°


3-38KHz IR obstacle detector :
        Obstacle detection/avoidance through a pre trained path.


4-HC-05 (IEEE 802.15.1): 
        Bluetooth Wireless coneectivity (range ~ 10 mtr), If out of connectivity 
        sends a signal to the user and tries to move towards SIM7000E cordinates.
 

5-URM37 V4.0 Ultrasonic Sensor (range ~ (5~500cm)):
        Provides obstacle avoidance similar to IR.

6-L293D motor shield :
        • 4 bi-directional DC motors with 8-bit speed selection(0-255).
        • 2 stepper motors (unipolar or bipolar) with single coil, double coil, interleaved or micro-stepping.
        •  2 servo motors

7-Nvidia Jetson Nano : 
        powerful computer that lets you run multiple neural networks in parallel for applications like image classification,
        object detection, segmentation, and speech processing. All in an easy-to-use platform that runs in as little as 5 watts.

