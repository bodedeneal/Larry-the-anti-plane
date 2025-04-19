# Servo and LCD Control Project

This project demonstrates how to control a servo motor and an LCD screen using a Raspberry Pi. The project is divided into two parts:
1. **Servo Motor Control**: A Python script to control the angle of a servo motor via GPIO pins.
2. **LCD Display**: A Python script to display custom text on a 16x2 LCD screen connected to the Raspberry Pi.

## Features
- Control the angle of a servo motor using GPIO pins on a Raspberry Pi.
- Display custom messages on an LCD screen using the I2C interface.

## Hardware Requirements
- Raspberry Pi (any model with GPIO pins, e.g., Raspberry Pi 4 or Raspberry Pi Zero).
- Servo motor (e.g., SG90 or MG90S).
- 16x2 LCD screen with I2C interface (or without, if you're comfortable with extra wiring).
- Jumper wires and (optional) a breadboard.
- External power supply for high-power servos (optional).

## Software Requirements
- Python 3.
- Required Python libraries (see `requirements.txt` for details).

## Setup and Usage

### **1. Clone the Repository**
```bash
git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>
```

### **2. Install Dependencies**
Use `pip` to install the required Python libraries:
```bash
pip install -r requirements.txt
```

### **3. Run the Servo Control Script**
To control the servo motor, connect the servo to the Raspberry Pi as described in the [Servo Motor Wiring](#servo-motor-wiring) section and run:
```bash
python servo_control.py
```

### **4. Run the LCD Display Script**
To display text on the LCD, connect the LCD to the Raspberry Pi as described in the [LCD Wiring](#lcd-wiring) section and run:
```bash
python lcd_display.py
```

---

## Wiring Details

### **Servo Motor Wiring**
- **Signal (Orange/White)**: Connect to GPIO18 (or any other GPIO pin you specify in the script).
- **Power (Red)**: Connect to the 5V pin on the Raspberry Pi (or external power supply).
- **Ground (Black/Brown)**: Connect to a GND pin on the Raspberry Pi.

### **LCD Wiring (I2C Interface)**
- **GND**: Connect to a GND pin on the Raspberry Pi.
- **VCC**: Connect to the 5V pin on the Raspberry Pi.
- **SDA**: Connect to GPIO2 (SDA).
- **SCL**: Connect to GPIO3 (SCL).

---

## File Overview
- `servo_control.py`: Python script for controlling the servo motor.
- `lcd_display.py`: Python script for displaying text on the LCD screen.
- `requirements.txt`: List of all Python dependencies needed for the project.
- `README.md`: Project documentation.

---

## Contributing
Feel free to fork this repository and submit pull requests with improvements or enhancements!

---

## License
This project is licensed under the MIT License.
