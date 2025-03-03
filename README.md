

---

# Simple IOT Platform Built Using Django  

This is a simple yet powerful IoT platform built using Django, allowing users to register, log in, and manage their ESP32 devices. The platform provides an intuitive dashboard where users can control their devices remotely and monitor their status in real time.  

## Features  
- **User Authentication**: Secure login and registration system.  
- **Device Management**: Users can add, activate, deactivate, and delete ESP32 devices.  
- **Remote LED Control**: Toggle multiple LEDs on ESP32 devices through the web interface.  
- **Real-time Monitoring**: View the status of connected devices on the dashboard.  
- **API Key Generation**: Each device is assigned a unique API key for secure communication.  

## How It Works  
1. **User Registration & Login**: Users create an account and log in.  
2. **Device Addition**: Users can register their ESP32 devices by providing a name.  
3. **Dashboard Overview**: Displays active and inactive devices with key metrics.  
4. **Control Panel**: Users can toggle LEDs and check device status in real time.  
5. **Secure API Access**: Devices communicate securely using API keys.  

## Tech Stack  
- **Backend**: Django  
- **Frontend**: HTML, CSS, JavaScript  
- **Database**: SQLite (can be replaced with PostgreSQL or MySQL)  
- **IoT Hardware**: ESP32  

## Installation  
1. Clone the repository:  
   ```bash
   git clone https://github.com/ApyCoder1/Simple-IOT-Platform-Built-Using-Django/
  
   ```  
2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```  
3. Run migrations:  
   ```bash
   python manage.py migrate
   ```  
4. Start the development server:  
   ```bash
   python manage.py runserver 0.0.0.0:8000
   ```  
5. Open `http://127.0.0.1:8000/` in your browser.  

## Future Enhancements  
- MQTT support for real-time communication.  
- Graphical data visualization for device logs.  
- Mobile app integration for remote control.  

---
