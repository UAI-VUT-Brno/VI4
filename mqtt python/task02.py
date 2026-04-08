import getpass
from xmlrpc import client
import paho.mqtt.client as mqtt

# TODO: vyjděte z předchozího kódu a vytvořte MQTT subscribera
# který se připojí k mqtt topicu "quality-check/duff" a bude vypisovat přijaté zprávy

# TODO: pro připojení ke klientovi (v inicialiazci Clienta) použijte unikátní klientské ID, např. vytvořené pomocí vašeho username a časové známky (timestampu) pomocí time.time()

# TODO: v on_connect callbacku se přihlašte k odběru topicu pomocí metody klienta subscribe(...)

# TODO: použijte metodu Clienta *on_message* pro nastavení callbacku, který bude zpracovávat přijaté zprávy

# TODO: následně zprávy jednoduše vypište na konzoli (stačí payload zprávy, nemusíte vypisovat další informace)
