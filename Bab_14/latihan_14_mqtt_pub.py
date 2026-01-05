# Credit: Fikom UIT
import paho.mqtt.client as mqtt
import time
import random

BROKER = "broker.hivemq.com"
PORT = 1883
TOPIC = "fikom/iot/suhu"

def run_publisher():
    client = mqtt.Client()
    
    print(f"Menghubungkan ke {BROKER}...")
    client.connect(BROKER, PORT, 60)
    
    try:
        while True:
            # Simulasi Data
            suhu = random.randint(20, 35)
            payload = f"{suhu} C"
            
            client.publish(TOPIC, payload)
            print(f"Published to {TOPIC}: {payload}")
            
            time.sleep(2)
            
    except KeyboardInterrupt:
        print("Stopped.")
    finally:
        client.disconnect()

if __name__ == "__main__":
    run_publisher()
