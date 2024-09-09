from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers='http://ip172-18-0-14-crf1tpaim2rg008r8io0-2181.direct.labs.play-with-docker.com/')
producer.send('mi_tema', b'Hola, mundo!')
producer.flush()
