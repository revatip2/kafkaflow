# word-count-data-streaming

This program reads a text file and performs word count using Python, Kafka, and MongoDB. It reads the given `sample.txt` file, counts the occurrence of each word, and stores the word counts in a MongoDB database. The program utilizes Kafka for streaming data and connects to MongoDB for data storage.

## Prerequisites

Before running the program, ensure that you have the following components installed and set up in your local environment:

- Kafka and ZooKeeper
- Python
- Kafka-Python package (`kafka-python`)
- PyMongo package (`pymongo`)
- MongoDB

## Installation

1. Install the required Python packages by running the following commands in your terminal:

`pip install kafka-python`
`pip install pymongo`


2. Start Kafka and ZooKeeper by running the following commands in separate terminal windows:
`bin/zookeeper-server-start.sh config/zookeeper.properties`
`bin/kafka-server-start.sh config/server.properties`


3. Create a Kafka topic named `input-topic` by running the following command:

`bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic input-topic`

4. Create a MongoDB database named `word_count` and a collection named `counts` using the mongo shell:
   
`mongosh
use word_count
db.createCollection("counts")`


## Usage

1. Copy the provided Python code into a file named `word_count.py`.

2. Open a new terminal window, navigate to the directory where you saved `word_count.py`, and run the following command to execute the Python code:
   
`python word_count.py`

3. In another terminal window, navigate to the directory where the `input.txt` file is located, and run the following command to produce input data:

`cat input.txt | bin/kafka-console-producer.sh --broker-list localhost:9092 --topic input-topic`

This command reads the lines from `input.txt` and sends them to the `input-topic` Kafka topic.

4. To verify that the word counts are being written to the MongoDB collection, run the following command in the mongo shell:
   
`db.counts.find().pretty()`
