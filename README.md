# vitals-event-generator

This project generates and emits vitals events to Kafka in real-time.

## Prerequisites

*   Python 3.6+
*   Docker
*   Kafka Broker

## Installation

1.  Clone the repository:

    ```bash
    git clone https://github.com/Gautam0610/vitals-event-generator.git
    cd vitals-event-generator
    ```

2.  Create a virtual environment (optional):

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Configuration

Set the following environment variables:

*   `KAFKA_BOOTSTRAP_SERVERS`: The Kafka bootstrap servers (e.g., `localhost:9092`).
*   `KAFKA_TOPIC`: The Kafka topic to send events to (e.g., `vitals`).

## Usage

Run the script:

```bash
python vitals_generator.py
```

## Docker

Build the Docker image:

```bash
docker build -t vitals-event-generator .
```

Run the Docker container:

```bash
docker run -e KAFKA_BOOTSTRAP_SERVERS=<kafka_bootstrap_servers> -e KAFKA_TOPIC=<kafka_topic> vitals-event-generator
```