<style>
    * {text-align: justify;}
</style>

# Cheat sheat

## Image

Modelo de sistema de arquivos somente leitura formado em camadas.

### $ docker image
- **pull magem:tag** -> baixar a imagem do dockerhub, pode ocorrer de forma implícita durante o *run*.
- **ls** -> lista as imagens salvas localmente.
- **rm imagem:tag** -> remove uma ou mais imagens separadas por espaço, pode-se usar o nome ou id da imagem.
- **inspect imagem** -> retorna um json contendo as informalções de configuração da imagem.
  - **--format="{...}"** => argumentos, formatados como json, para buscar atributos da imagem criada.
- **tag imagem nome_tag** -> aplica uma nova tag à imagem.
- **build arquivo_descritor** -> monta um container a partir de um arquivo descritor, este que possibilita a replicação de containers.
  - **-t nome** => nome que será atribuído à imagem criada
  - **--build-arg argumentos** => atribui valores para a imagem a ser buildada, pode ser utilizado para definir condicionais durante o build.
- **push**: após adicionar uma nova tag ou buildar uma nova imagem ela pode ser enviada para um repositório local ou o próprio dockerhub.


## Container

Usa o sistema de arquivos montado pela imagem para definir processos e subprocessos. O container cria uma nova camada onde podem ser feitas as alterações (arquivos e configurações).

### $ docker container
- **run** -> executa uma imagem, caso ela não exista ele executa *docker image pull* da imagem selecionada
  - **-i** => executa em modo interativo
  - **-it** => executa em modo interativo e concede acesso ao terminal do container
  - **-d** => executa em modo deamon (background)
  - **-rm** => remove o container logo após a sua execução ser finalizada
  - **--name nome** => atribui um nome ao container que será executado
  - **-p host:container** => mapeia uma porta do docker em uma porta da máquina host
  - **-v host:container** => mapeia uma pasta do docker em uma pasta da máquina host
  - **--net *nome_rede*** => define o tipo de rede que se deseja utilizar, quando não definido ele entra no modo *bridge* por padrão.

- **start nome|id** -> inicia um container já criado através do nome ou do id dele
  - **ai** => acessa o terminal em modo interativo

## Dockerfile

- **FROM *image*** -> indica qual imagem será utilizada como base para criação da nova imagem.
- **RUN *comandos*** -> executa os comandos como se fosse no modo shell
    - É muito comum concatenar comandos para evitar que seja criado um número excessivo de camadas.
    - Uma boa prática é deixar as partes mais mutáveis no final do arquivo, deste modo as camadas internas são reaproveitadas.
- **COPY *origem_host dest_img**** -> copia um arquivo da máquina hospedeira para a imagem.
- **USER *nome*** -> define o usuário da imagem.
- **VOLUME *diretório*** -> instrui ao container a criar um volume para um diretório na imagem, simplificando o compartilhamento dos dados para backup.
- **WORKDIR *diretório*** -> define o diretório de trabalho.
- **EXPOSE *porta*** -> expões uma porta do container para acesso, esta ainda pode ser mapeada.
- **ENTRYPOINT [*diretório*]** -> processo que será executado quando o container estiver iniciando.
- **CMD [*comando*]** -> comando que será passado para o ENTRYPOINT.

## Updaload para DockerHub

1. Cadastro em hub.docker.com
2. Selecionar uma imagem e atribuir as tags adequadas à elas
    - Colocar a tag no formato *usuário/nome_imagem:tag*
    - EX: *docker image tag exemplo usuario/meu_exemplo:1.0*
3. Logar no dockerhub: *docker login --username=usuario*
4. docker image push usuario/meu_exemplo

## Network

### $ docker network
- **ls** -> listar os drivers de rede.
- **create --driver *driver_name* *nome*** --> ciar uma nova rede
  - **connect *rede* *container*** => conecta o container a uma outra rede
