#include <WiFi.h>
#include <HTTPClient.h>
#include <ArduinoJson.h>  // JSON Parsing Library

const char* ssid = "ApyCoder";
const char* password = "Asif12345";
const char* serverURL = "http://10.129.101.93:8000/led-status/";  // Server URL

#define LED1_PIN 10  
#define LED2_PIN 9  
#define LED3_PIN 8  
#define LED4_PIN 7  

bool lastLedState[4] = {LOW, LOW, LOW, LOW};  // Store last LED states

String apiKey = "KWPBjA6IPaNdLnGgApil";  // Replace Your Device API key for authentication

void setup() {
    Serial.begin(115200);
    
    // Initialize LED pins
    pinMode(LED1_PIN, OUTPUT);
    pinMode(LED2_PIN, OUTPUT);
    pinMode(LED3_PIN, OUTPUT);
    pinMode(LED4_PIN, OUTPUT);

    // Set LEDs to LOW initially
    digitalWrite(LED1_PIN, LOW);
    digitalWrite(LED2_PIN, LOW);
    digitalWrite(LED3_PIN, LOW);
    digitalWrite(LED4_PIN, LOW);

    // Connect to WiFi
    Serial.print("Connecting to WiFi...");
    WiFi.begin(ssid, password);
    
    while (WiFi.status() != WL_CONNECTED) {
        delay(500);
        Serial.print(".");
    }
    Serial.println("\nConnected to WiFi!");
}

void loop() {
    // Check WiFi connection
    if (WiFi.status() != WL_CONNECTED) {
        Serial.println("WiFi Disconnected! Reconnecting...");
        WiFi.reconnect();
        delay(1000);
        return;
    }

    // Make HTTP GET request with only API key
    String requestUrl = String(serverURL) + "?api_key=" + apiKey;
    HTTPClient http;
    http.begin(requestUrl);
    int httpResponseCode = http.GET();

    // If request is successful
    if (httpResponseCode == 200) {
        String payload = http.getString();
        Serial.println("Server Response: " + payload);

        // Parse JSON using ArduinoJson
        StaticJsonDocument<200> doc;
        DeserializationError error = deserializeJson(doc, payload);
        
        if (!error) {
            int ledStates[4] = {
                doc["led1_status"], 
                doc["led2_status"], 
                doc["led3_status"], 
                doc["led4_status"]
            };

            // Debug: Print LED states
            Serial.print("LED States: ");
            for (int i = 0; i < 4; i++) {
                Serial.print(ledStates[i]);
                Serial.print(" ");
            }
            Serial.println();

            // Check if LED states have changed and update the LEDs
            for (int i = 0; i < 4; i++) {
                int pin = (i == 0) ? LED1_PIN : (i == 1) ? LED2_PIN : (i == 2) ? LED3_PIN : LED4_PIN;
                if (ledStates[i] != lastLedState[i]) {
                    Serial.print("Changing LED ");
                    Serial.print(i + 1);
                    Serial.print(" to ");
                    Serial.println(ledStates[i] ? "ON" : "OFF");
                    
                    // Update the LED pin based on the state
                    digitalWrite(pin, ledStates[i] ? HIGH : LOW);
                    lastLedState[i] = ledStates[i];  // Update the last state
                }
            }
        } else {
            Serial.println("JSON Parsing Error!");
        }
    } else {
        Serial.print("HTTP Error: ");
        Serial.println(httpResponseCode);
    }
    
    http.end();

    // Add delay for stability
    delay(1000);  // Increase delay to 1 second for stability
}
