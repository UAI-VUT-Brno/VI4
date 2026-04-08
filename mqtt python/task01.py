import getpass
from xmlrpc import client
import paho.mqtt.client as mqtt

# TODO: ideálně do konstant (ať to neschováváme do argumentů si uložte host a port, 
# TODO: dále username a password pro připojení k MQTT brokeru
# TODO: password načtěte pomocí knihovny getpass funkce getpass, aby se nezobrazoval při zadávání

def on_connect(client, userdata, flags, reason_code, properties=None):
    pass
    # TODO: vypište informaci o připojení, použijte reason code


def main():
    pass
    # TODO: vytvořte klienta (třída Client) a nastavte callback API na verzi 2
    # TODO: nastavte u něj přihlašovací údaje
    # TODO: nastavte callback (delegate) on_connect
    # TODO: připojte se k brokeru
    # TODO: spusťte smyčku loop forever, která bude zpracovávat příchozí zprávy a udržovat připojení



if __name__ == "__main__":
    main()