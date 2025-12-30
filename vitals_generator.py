import json
import time
import random
from datetime import datetime
from kafka import KafkaProducer

# Configuration
KAFKA_BOOTSTRAP_SERVERS = 'localhost:9092'  # Replace with your Kafka brokers
KAFKA_TOPIC = 'vitals'  # Replace with your Kafka topic
BATCH_SIZE_BYTES = 1024  # 1KB batch size

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

    batch = []
    current_batch_size = 0

    try:
        while True:
            event = generate_vitals_event()
            event_string = json.dumps(event)
            event_size = len(event_string.encode('utf-8'))

            if current_batch_size + event_size > BATCH_SIZE_BYTES:
                # Send the batch
                if batch:
                    producer.send(KAFKA_TOPIC, batch)
                    print(f"Sent batch of {len(batch)} events")
                # Start a new batch
                batch = [event]
                current_batch_size = event_size
            else:
                # Add to the current batch
                batch.append(event)
                current_batch_size += event_size

            time.sleep(1)  # Send an event every 1 second
    except KeyboardInterrupt:
        print("Stopping the vitals event generator.")
        # Send any remaining events
        if batch:
            producer.send(KAFKA_TOPIC, batch)
            print(f"Sent remaining batch of {len(batch)} events")
    finally:
        producer.close()

if __name__ == "__main__":
    main()