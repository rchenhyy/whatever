# coding=utf-8
import logging
from tmq.kafka.producer.kafka import KafkaProducer

test_producer = KafkaProducer()

msg = {
    "product": "toutiao",
    "sub_product": "xigua",
    "item_id": 999999999,
    "group_id": 999999999,
    "title": "测试",
    "content": "测试测试测试测试哈哈哈哈哈哈哈，明天就要高考了",
    "source": "陈嘉华",
    "url_source": "陈嘉华",
    "visibility_level": 1,
    "create_time": 1528349052.876066,
    "update_time": 1528349052.876066,
    "img": [{
        "key": "test007",
        "md5": "test",
        "url": "test"
    }],
    "video": [{
        "key": "",
        "md5": "",
        "url": "",
        "duration": 99
    }],
    "audio": [{
        "key": "",
        "md5": "",
        "url": "",
        "duration": 99
    }],
    "i18n": {
        "display_regions": "",
        "language": ""
    },
    "user": {
        "id": 123456789,
        "username": "unknown"
    },
    "trace": {
        "publish_ip": "10.2.195.167",
        "publish_port": 9999
    },
    "ext": {

    }
}

test_producer.send(topic='test20180606', value=msg)
logging.info("Message sent!")
