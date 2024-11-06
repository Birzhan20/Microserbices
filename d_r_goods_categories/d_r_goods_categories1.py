import uuid
import nest_asyncio
import g4f
import redis
import json
from confluent_kafka import Consumer, Producer, KafkaError, KafkaException
import logging

nest_asyncio.apply()

kafka_config = {
    'bootstrap.servers': 'kafka:9093',
    'group.id': 'd_r_goods_categories',
    'auto.offset.reset': 'earliest',
    'enable.auto.commit': False,
    'acks': 'all'
}

redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

producer = Producer(kafka_config)
consumer = Consumer(kafka_config)

consumer.subscribe(['d-r-goods-index', 'd-r-goods-seo', 'd-r-categories-index', 'd-r-categories-seo'])

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def process_message(text: str, category: str) -> str:
    try:
        if category == 'd-r-goods-index':
            prompt = f"������ ���������� ������������� � google ����-�������� �� ����� 200 ���� ��� ���������� � ������������ �� ������������� ����� ���������� Mytrade.kz �� ������ ����� ������: �{text}�"
        elif category == 'd-r-goods-seo':
            prompt = f"������ ���������� seo-����� �� ����� 500 ���� � ����������� ����� �� ������������� ����� ���������� Mytrade.kz ���������� �� �������� � ������� ��� � �������, ������� ��� ����� � ������ �{text}�. ������� ��������� �������. ��������� ������ ��������� ������� ����, � ������� ����� ����� �������������� ���������� �� ����� ���������� Mytrade.kz � �������, �������, ������ ������� ������������. � ������ �� ��������� ��������� ��� ��������, �� ��������� ����� '���-������', �� ��������� ������, �� ��������� �������� ����� �� ����� ������, �� ��������� ������, �� ��������� ������ �����. ����� ������ ���� ��������� �������"
        elif category == 'd-r-categories-index':
            prompt = f"������ ���������� ������������� � google ����-�������� �� ����� 200 ���� ��� ��������� ������������� ����� ���������� Mytrade.kz �{text}�. ������ ������ ����� ������������ ����� ������, �������, ����� ��� ����� � ������ � ������ ���������"
        elif category == 'd-r-categories-seo':
            prompt = f"������ ���������� seo-����� �� 500 ���� � ����������� ���������� ���������� � �������, �������, ������ ������������ � ��������� �{text}� �� ������������� ����� ���������� Mytrade.kz. �������� � ������� ���������� ���������� � ��������� �{text}� �� �������� � ������� ��� �� ����� ����. ��������� ������ � �������� �������������� �� ����� ���������� Mytrade.kz ���� ������������� �� ��������� �{text}�. ��������� ������ ��������� ������� ����, � ������� ������� ���� � �������� �������, �������� ��� ����� � ������ ������������ �� ������ ��������� �� ����� ���������� Mytrade.kz. � ������ �� ��������� ��������� ��� ��������, �� ��������� ����� '���-������', �� ��������� ������, �� ��������� �������� ����� �� ����� ������, �� ��������� ������, �� ��������� ������ �����. ����� ������ ���� ��������� �������"
        else:
            return "unknown category"

        response = g4f.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            stream=False
        )

        return response.strip('"')
    except Exception as e:
        logger.error(f"������ ��� ��������� ������: {str(e)}")
        return f"Error {str(e)}"


def handle_message(message):
    try:
        message_value = message.value().decode('utf-8')
        data = json.loads(message_value)

        message_id = data.get("message_id")
        text = data.get("text", "")
        category = data.get("category", "")

        if not text or not message_id:
            logger.warning(f"None, ignore...")
            return

        if redis_client.exists(message_id):
            logger.info(f"Message {message_id} has already been processed. skip it")
            return

        meta_description = process_message(text, category)

        result = {
            'message_id': str(uuid.uuid4()),
            'meta': meta_description,
            'category': category
        }

        producer.produce('d-r-result', json.dumps(result).encode('utf-8'))
        producer.flush()

        consumer.commit()

    except KafkaException as e:
        logger.error(f"Error Kafka: {str(e)}")
    except Exception as e:
        logger.error(f"Error of processing message: {str(e)}")


def consume_messages():
    logger.info("Starting consume messages...")

    while True:
        try:
            msg = consumer.poll(timeout=1.0)

            if msg is None:
                continue

            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    logger.info(f"The end of partitions has been reached {msg.partition}")
                else:
                    logger.error(f"Error Kafka: {msg.error()}")
            else:
                handle_message(msg)

        except KeyboardInterrupt:
            logger.info("Completing the consumption of messages...")
            break
        except Exception as e:
            logger.error(f"Error: {str(e)}")


if __name__ == '__main__':
    try:
        consume_messages()
    except Exception as e:
        logger.error(f"Error: {str(e)}")
    finally:
        consumer.close()
