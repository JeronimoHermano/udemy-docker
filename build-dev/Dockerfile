FROM python:3.6
LABEL maintener='Jerônimo Hermano'

RUN useradd www && \
    mkdir /app && \
    mkdir /log && \
    chown www /log

USER www
VOLUME /log
WORKDIR /app
# Define uma porta para expor/tornar acessível, mas esta pode ser remapeada no run
EXPOSE  8000

# Processo que será executado quando o container estiver iniciando
ENTRYPOINT [ "/usr/local/bin/python" ]
# Comando que será passado para o ENTRYPOINT
CMD [ "run.py" ]
