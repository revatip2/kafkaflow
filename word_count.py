from kafka import KafkaProducer, KafkaConsumer
from pymongo import MongoClient
import re

# Create a Kafka producer to read data from the text file and produce messages to a Kafka topic

producer = KafkaProducer(bootstrap_servers=['localhost:9092'])
with open('input.txt', 'r') as f:
   for line in f:
       producer.send('input-topic', line.strip().encode('utf-8'))
     
# Create a Kafka consumer to consume messages from the input topic

consumer = KafkaConsumer('input-topic', bootstrap_servers=['localhost:9092'])

# Perform word count and write the result to MongoDB

word_counts = {}
for message in consumer:
   line = message.value.decode('utf-8').lower()
   words = re.findall(r'\w+', line)
   for word in words:
       if word in word_counts:
           word_counts[word] += 1
       else:
           word_counts[word] = 1
         
   # Write the word count data to MongoDB
  
   client = MongoClient('mongodb://localhost:27017/')
   db = client['word_count']
   collection = db['counts']
   for word, count in word_counts.items():
       collection.update_one(
           {"word": word},
           {"$inc": {"count": count}},
           upsert=True
       )
   result = list(collection.find({}, {"_id": 1, "word": 1, "count": 1}))
   print(result)
   collection.insert_one(word_counts)


