#COMUNICAÇÃO COM PROTOCOLO DAS COISAS MQTT
#INTERNET DAS COISAS
#DATA: 03/11/2021
#VERSÃO: 1.0

#instalalar paho-mqtt com "pip3 install paho-mqtt"

#imports
import paho.mqtt.client as mqtt
import sys
import RPi.GPIO as GPIO
import time

#Configuração do MQTT
broker = "test.mosquitto.org"
portaBroker = 1883
keepAliveBroker = 60
topicoSubscribe = "IOT03112021led"

def codigo(msgg):
    #código
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(18,GPIO.OUT)

    if msgg == "b'1'":
        print('LED on')
        GPIO.output(18,GPIO.HIGH)
    #time.sleep(1)
    else:
        print('LED off')
        GPIO.output(18,GPIO.LOW)

#função para conexão com o broker
def on_connect(client, userdata, flag, rc):
    print('[STATUS] Conectando ao Broker. Resultado: ' + str(rc))
    #inscrever no topico configurado
    client.subscribe(topicoSubscribe)
    
#função para recebimento de menagem
def on_message(client, userdata, msg):
    mensagemRecebida = str(msg.payload)
    #print('[Mensagem recebida] Topico: ' + msg.topic + '/Mensagem: ' + mensagemRecebida)
    codigo(mensagemRecebida)

#Programa Principal
try:
    print('[STATUS] Iniciando MQTT...')
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    
    #Conexão propriamente dita
    client.connect(broker, portaBroker, keepAliveBroker)
    client.loop_forever()
    

except KeyboardInterrupt:
    print('CTRL + C pressionado, encerrando a aplicação')
    sys.exit(0)
    
