import psycopg2
import redis
import json
import os
from bottle import Bottle, request


class Sender(Bottle):
    def __init__(self):
        super().__init__()
        self.route('/', method='POST', callback=self.send)

        redis_host = os.getenv('REDIS_HOST', 'queue')
        self.fila = redis.StrictRedis(host=redis_host, port=6379, db=0)

        db_host = os.getenv('DB_HOST', 'db')
        db_user = os.getenv('DB_USER', 'postgres')
        db_name = os.getenv('DB_NAME', 'email_sender')

        DSN = f'dbname={db_name} user={db_user} host={db_host}'
        self.conn = psycopg2.connect(DSN)

    def register_message(self, assunto, mensagem):
        # insere mensagem no BD
        SQL = 'insert into emails (assunto, mensagem) values (%s, %s)'
        cur = self.conn.cursor()
        cur.execute(SQL, (assunto, mensagem))
        self.conn.commit()
        cur.close()

        # envia mensagem para o redis
        msg = {'assunto':assunto, 'mensagem':mensagem}
        self.fila.rpush('sender', json.dumps(msg))

        print('E-mail registrado!')

    def send(self):
        assunto = request.forms.get('assunto')
        mensagem = request.forms.get('mensagem')

        self.register_message(assunto, mensagem)

        return 'Mensagem enviada para fila!\nAssunto:\"{}\"\nMensagem:\n{}'.format(
            assunto,
            mensagem
        )


if __name__ == "__main__":
    sender = Sender()
    sender.run(host='0.0.0.0', port=8080, debug=True)
