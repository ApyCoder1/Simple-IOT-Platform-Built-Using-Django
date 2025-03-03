

---

# Simple IOT Platform Built Using Django  

This is a simple yet powerful IoT platform built using Django, allowing users to register, log in, and manage their ESP32 devices. The platform provides an intuitive dashboard where users can control their devices remotely and monitor their status in real time.  

## Features  
- **User Authentication**: Secure login and registration system.
- ![image](https://github.com/user-attachments/assets/21a42dc8-c569-4b11-bd28-85d4c98e3adf)

- **Device Management**: Users can add, activate, deactivate, and delete ESP32 devices.
- ![image](https://github.com/user-attachments/assets/780c794a-149a-40ba-8c49-c1b03a2d566f)

- **Remote LED Control**: Toggle multiple LEDs on ESP32 devices through the web interface.
- ![image](https://github.com/user-attachments/assets/dc74722b-a760-41b5-8777-9edd2240e334)
- ![image](https://github.com/user-attachments/assets/9f8d5e60-4197-4347-baa8-b8486b454e6f)

 
- **Real-time Monitoring**: View the status of connected devices on the dashboard.
- ![image](https://github.com/user-attachments/assets/ba668edd-1d35-49be-a1ba-9c12fb089f2e)
 
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
- **Database**: SQLite 
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
