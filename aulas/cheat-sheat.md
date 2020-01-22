# Cheat sheat

## Image

Modelo de sistema de arquivos somente leitura formado em camadas.

### $ docker image
- **pull magem:tag** -> baixar a imagem do dockerhub, pode ocorrer de forma implícita durante o *run*.
- **ls** -> lista as imagens salvas localmente.
- **rm imagem:tag** -> remove uma ou mais imagens separadas por espaço, pode-se usar o nome ou id da imagem.
- **inspect imagem** -> retorna um json contendo as informalções de configuração da imagem.
- **tag imagem nome_tag** -> aplica uma nova tag à imagem.
- **build arquivo_descritor** -> monta um container a partir de um arquivo descritor, este que possibilita a replicação de containers.
  - **-t nome** => nome que será atribuído à imagem criada
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

- **start nome|id** -> inicia um container já criado através do nome ou do id dele
  - **ai** => acessa o terminal em modo interativo

## Dockerfile
