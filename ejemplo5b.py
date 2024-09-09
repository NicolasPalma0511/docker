from kafka import KafkaConsumer

# Configura el consumidor
consumer = KafkaConsumer(
    'mi_topico',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='mi_grupo',
    value_deserializer=lambda x: x.decode('utf-8')
)

print("Esperando mensajes...")
for message in consumer:
    print(f"Recibido: {message.value}")
