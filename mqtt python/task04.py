import json
import time
from datetime import datetime, timezone
import getpass
import paho.mqtt.client as mqtt

MQTT_HOST = "broker.uai.fme.vutbr.cz"
MQTT_PORT = 1883

MQTT_USERNAME = input("Username: ").strip()
MQTT_PASSWORD = getpass.getpass("Password: ")

TOPIC = "sometopic/somewhere/"


def now():
    return datetime.now(timezone.utc).isoformat()


def main():
    client = mqtt.Client(
        callback_api_version=mqtt.CallbackAPIVersion.VERSION2,
        client_id=CLIENT_ID,
        protocol=mqtt.MQTTv311,
    )

    client.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)

    client.connect(MQTT_HOST, MQTT_PORT, keepalive=60)
    client.loop_start()

    try:
        while True:
            payload = {
                "msg": "ahoj",
                "ts": now()
            }

            data = json.dumps(payload, ensure_ascii=False)
            client.publish(TOPIC, data, qos=1)

            print("SENT:", data)
            time.sleep(2)

    except KeyboardInterrupt:
        print("Stopped")
    finally:
        client.loop_stop()
        client.disconnect()


if __name__ == "__main__":
    main()