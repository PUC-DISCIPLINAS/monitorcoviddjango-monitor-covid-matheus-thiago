# kv-grpc-matheus-thiago
## Autores

* [Matheus Felipe Ferreira Martins](https://github.com/MatheusFFM)
* [Thiago Jorge Queiroz Silva](https://github.com/ThiagoQueirozSilva)

## Sobre o sistema

Este trabalho se trata de um monitor de covid feito com o framework web mvc django. Será exibido nesta aplicação uma tabela com diversos países demonstando
os casos de COVID-19 confirmados, os casos recuperados e as mortes causadas pela doença em cada país. Também é possível criar países e adicionar os casos para cada país
por meio do admin django.

## Execução

```bash
#Checkando se possui django
$ python -m django --version.

#Installando o django
$ python -m pip install Django.

# Clonar o repositório
$ git clone https://github.com/PUC-DISCIPLINAS/monitorcoviddjango-monitor-covid-matheus-thiago.git

# Entrar na pasta de código
$ cd covid/covidmvc
```

### Iniciando django

```bash
# Executar a aplicação
$ python manage.py runserver
```

Retorna que a aplicação foi iniciada com sucesso. Para interromper seu funcionamento pressione Ctrl + C.

## Aplicação
Após executada entre no link: http://127.0.0.1:8000/ no seu navegador.

Será exibida uma tabela com os países e seus casos de COVID-19 e um botão "Admin" onde os dados da aplicação poderão ser manipulados.

### Admin
Ao clickar no botão "Admin" será requisitado um login e uma senha.

```bash
#Usuário
...
#Senha
...
```

Feito o login poderão ser manipuladas as tabelas de países e de casos de cada país
