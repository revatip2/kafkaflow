# word-count-data-streaming

This program reads a text file and performs word count using Python, Kafka, and MongoDB. It reads the given `sample.txt` file, counts the occurrence of each word, and stores the word counts in a MongoDB database. The program utilizes Kafka for streaming data and connects to MongoDB for data storage.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)

## Introduction

Word count is a common task in data processing and analysis. This program provides a streaming approach to perform word count using Python, Kafka, and MongoDB. It reads a given text file, counts the occurrence of each word, and stores the word counts in a MongoDB database for further analysis or visualization.

## Installation

Before running the program, ensure that you have the following prerequisites installed in your local environment:

- Kafka and ZooKeeper
- Python
- Kafka-Python package (`kafka-python`)
- PyMongo package (`pymongo`)
- MongoDB

1. Install the required Python packages by running the following commands in your terminal:

`pip install kafka-python`
`pip install pymongo`


2. Start Kafka and ZooKeeper by running the following commands in separate terminal windows:
   
`bin/zookeeper-server-start.sh config/zookeeper.properties`
`bin/kafka-server-start.sh config/server.properties`


4. Create a Kafka topic named `input-topic` by running the following command:

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

This command reads the lines from `sample.txt` and sends them to the `input-topic` Kafka topic.

4. To verify that the word counts are being written to the MongoDB collection, run the following command in the mongo shell:
   
`db.counts.find().pretty()`

## Configuration

The program requires the following configurations:

- **Kafka Configuration**: Make sure that the Kafka server is running on `localhost:9092` or update the `bootstrap_servers` parameter in the Python code (`word_count.py`) accordingly. Open the `word_count.py` file and modify the following line:

  ```python
  producer = KafkaProducer(bootstrap_servers=['localhost:9092'])
  consumer = KafkaConsumer('input-topic', bootstrap_servers=['localhost:9092'])

Update the bootstrap_servers parameter to match your Kafka server address if it is hosted elsewhere.

- **MongoDB Configuration**: Ensure that MongoDB is running on `localhost:27017` or update the MongoDB connection URL in the Python code (`word_count.py`) if your MongoDB server is hosted elsewhere. Open the `word_count.py` file and modify the following line:

   ```python
   client = MongoClient('mongodb://localhost:27017/')
   
Update the connection URL to match your MongoDB server address if it is hosted elsewhere. For example, if your MongoDB server is running on a different IP address or port, update the connection URL accordingly. Here's an example of how to modify the connection URL:

`client = MongoClient('mongodb://<your-mongodb-server-address>:<port>/')`

Replace <your-mongodb-server-address> with the IP address or hostname of your MongoDB server, and <port> with the corresponding port number.

Feel free to modify the configurations as per your environment setup.
