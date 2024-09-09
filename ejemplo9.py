from confluent_kafka import Producer

# Configurar el productor (puerto y servidor de Kafka)
conf = {'bootstrap.servers': ""}  # Cambia por tu servidor de Kafka

# Crear productor
producer = Producer(**conf)

# Definir función de callback
def acked(err, msg):
    if err is not None:
        print(f"Error al enviar el mensaje: {err}")
    else:
        print(f"Mensaje enviado a {msg.topic()} [{msg.partition()}]")

# Enviar un mensaje a un tópico llamado 'mi-topico'
topic = 'mi-topico'
producer.produce(topic, key="clave", value="Hola Kafka!", callback=acked)

# Esperar a que se envíen todos los mensajes
producer.flush()
