from tmq.kafka.consumer.group import KafkaConsumer

test_consumer = KafkaConsumer('test20180606')
msg = test_consumer.poll()

print msg
