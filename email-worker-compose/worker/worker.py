import redis
import json
import os
from time import sleep
from random import randint

if __name__ == "__main__":
    redis_host = os.getenv('REDIS_HOST', 'queue')
    r = redis.Redis(host=redis_host, port=6379, db=0)

    print('Aguardando e-mails...')

    while True:
        mensage = json.loads(r.blpop('sender')[1])

        # Envio de e-mail simulado
        print('Enviando mensagem:', mensage['assunto'])
        sleep(randint(15, 54))
        print('Mensagem "', mensage['assunto'], '" enviada')
