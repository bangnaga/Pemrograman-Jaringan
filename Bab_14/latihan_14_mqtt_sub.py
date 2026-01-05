# Credit: Fikom UIT
import paho.mqtt.client as mqtt

# Broker Publik Gratisan
BROKER = "broker.hivemq.com"
PORT = 1883
TOPIC = "fikom/iot/suhu"

def on_connect(client, userdata, flags, rc):
    print(f"Terhubung ke Broker! (Code: {rc})")
    # Langsung subscribe saat koneksi jadi
    client.subscribe(TOPIC)
    print(f"Subscribed to {TOPIC}")

def on_message(client, userdata, msg):
    print(f"[DATA MASUK] {msg.topic}: {msg.payload.decode()}")

def run_subscriber():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    
    print(f"Menghubungkan ke {BROKER}...")
    try:
        client.connect(BROKER, PORT, 60)
        # Loop forever (blocking) untuk menangani network events
        client.loop_forever()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    run_subscriber()
