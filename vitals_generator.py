import json
import time
import random
from datetime import datetime
from kafka import KafkaProducer

# Configuration
KAFKA_BOOTSTRAP_SERVERS = 'localhost:9092'  # Replace with your Kafka brokers
KAFKA_TOPIC = 'vitals'  # Replace with your Kafka topic

def generate_vitals_event():
    """Generates a sample vitals event."""
    vitals = {
        'timestamp': datetime.utcnow().isoformat(),
        'patient_id': random.randint(1000, 9999),
        'heart_rate': random.randint(60, 100),
        'blood_pressure': f"{random.randint(110, 140)}/{random.randint(70, 90)}",
        'temperature': round(random.uniform(36.5, 37.5), 1),
        'spo2': random.randint(95, 100)
    }
    return vitals

def main():
    """Emits vitals events to Kafka."""
    producer = KafkaProducer(
        bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )

    try:
        while True:
            event = generate_vitals_event()
            producer.send(KAFKA_TOPIC, event)
            print(f"Sent event: {event}")
            time.sleep(1)  # Send an event every 1 second
    except KeyboardInterrupt:
        print("Stopping the vitals event generator.")
    finally:
        producer.close()

if __name__ == "__main__":
    main()