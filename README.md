
<h1 align="center">Market Place Cotabest</h1>
<p align="center">Este projeto tem o objetivo de mostrar a manipulação de produtos e criação de um carrinho de compras. </p>


<p align="center">
 <a href="#features">Features</a> • 
 <a href="#tecnologias">Tecnologias</a> •
 <a href="#tecnologias">Comandos Úteis</a> •
 <a href="#licenc-a">Licença</a> • 
 <a href="#autor">Desenvolvedor</a>
</p>

## Features

- Definição do Core
- Implementação da app Users
- Implementação da app Cart
- Implementação da app Product
- Implementação da app Purchase
- Configuração das rotas, views, model.

## Tecnologias e libs principais

- [Python v.3.10](https://www.python.org/downloads/release/python-310/) - Python é uma linguagem de programação de alto nível, interpretada de script, imperativa, orientada a objetos, funcional, de tipagem dinâmica e forte.
- [Django](https://www.djangoproject.com/) - Django é um framework web Python de alto nível que encoraja o desenvolvimento rápido e design limpo e pragmático. Construído por desenvolvedores experientes, ele resolve grande parte do incômodo do desenvolvimento da Web, para que você possa se concentrar em escrever seu aplicativo sem precisar reinventar a roda. É gratuito e de código aberto.
- [DjangoRestFramework](https://www.django-rest-framework.org/) - O framework Django REST é um kit de ferramentas poderoso e flexível para construir APIs da Web.
- [Postman](https://www.postman.com/) - Postman é uma plataforma de API para construir e usar APIs. O Postman simplifica cada etapa do ciclo de vida da API e agiliza a colaboração para que você possa criar APIs melhores e mais rapidamente.

## Comandos Úteis

Realizar makemigrations : 
```sh
python manage.py makemigrations
```
Realizar migration :
```sh
python manage.py migration
```
Rodar projeto :
```sh
python manage.py runserserver 
```
Rodar projeto docker-compose :
```sh
docker-compose up --build 
```
Criar ambiente virtual :
```sh
python -m venv .venv
```
Gerar requirements.txt :
```sh
pip freeze > requeriments.txt
```
Instalar requirements.txt :
```sh
pip install -r requeriments.txt
```


## Como testar a API. Endpoints principais

Dentro do projeto está um arquivo chamado Cotabes.postman_collection.json que pode ser utilizado para teste.

Consultar permissões: 
```sh
GET /api/v1/permissions/
```
Consultar grupos: 
```sh
GET /api/v1/groups/
```
Criar grupo / Estrutura : 
```sh
POST /api/v1/create-group
```
```sh
Os grupos contém as permissões relativas a cada operação de acordo com o grupo como vizualizar, adicionar, alterar e deletar um usuário, carrinho, produto ou compra( Deletar uma compra está permitido para questões de estudo e teste.)

{
  "group-name": "Administradores",
  "permissions": [13,14,15,16,25,26,27,28,29,30,31,32,33,34,35,36,41,43,44,45]
}

{
  "group-name": "Comuns",
  "permissions": [25,26,27,28,32,41,43,44,45]
}
```
Registrar um usuário / Estrutura : 
```sh
POST /api/v1/register/
```
```sh
Iniciando o procedimento, a manipulação no 'maketplace' começa com um registro de usuário no sistema para obter o token de acesso. "IS_ADMIN", é uma variável criada se controlar de maneira aberta as permissões a um usuário. Caso
seja true o usuário é adicionado ao grupo de administradores e em caso de false o usuário é adicionado ao grupo comuns.

{
  "first_name": "Fulano",
  "last_name": "Silva",
  "cpf": "000.000.000-00",
  "password": "password",
  "email": "fulanosilva@gmail.com",
  "is_admin": true
}
```
Realizar login no sistema/ Obter token / Estrutura : 
```sh
POST /api/v1/token/
```
```sh
Simulando o acesso a um usuário cadastrado no sistema é necessário a obtenção do token para a manipulação do carrinho, produtos, compra e usuário.

{
  "username": "fulano_fulano",
  "password": "password"
}
``````
Retorno do login, Ex:
```sh
No token estão todas as permissões atribuídas ao usuário atráves da sua vinculação a um grupo. Essas permissões são verificadas em todoas as operações GET, POST, PUT e DELETE.
Caso utilize o postman para teste, inserir o token access em Authorization -> Bearer token

{ "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY2NDY1MTkyMCwiaWF0IjoxNjY0NjM3NTIwLCJqdGkiOiIwYTdjMWYwY2U0ZDQ0NDIzYWRhZDAwZjkyMGFhMzkyOSIsInVzZXJfaWQiOjUsInJvbGVzIjpbImF1dGguZGVsZXRlX3VzZXIiLCJhdXRoLmFkZF91c2VyIiwiYXV0aC5jaGFuZ2VfdXNlciIsImF1dGgudmlld191c2VyIl0sImlzX3N0YWZmIjpmYWxzZSwiaXNfc3VwZXJ1c2VyIjpmYWxzZSwidXNlcnMiOnsiaWQiOjUsInVzZXJuYW1lIjoibWFyY2VsYV9tYXJjZWxhIiwiaXNfc3RhZmYiOmZhbHNlLCJpc19zdXBlcnVzZXIiOmZhbHNlfSwicHJvZmlsZSI6eyJjcGYiOiI1MzE4MDc3ODAzMiJ9LCJwcmVmZXJlbmNlc191c2VyIjpudWxsfQ.IbzZ3kvcUTWVvFQ5yPJjz2m340s7rRuYrqlDF8RVnOU", 
"access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjY0NjQ0NzIwLCJpYXQiOjE2NjQ2Mzc1MjAsImp0aSI6IjBiYzViYTQzM2Q3ODRlNjY4ZmYxYjcxZDM4MmNkMjUxIiwidXNlcl9pZCI6NSwicm9sZXMiOlsiYXV0aC5kZWxldGVfdXNlciIsImF1dGguYWRkX3VzZXIiLCJhdXRoLmNoYW5nZV91c2VyIiwiYXV0aC52aWV3X3VzZXIiXSwiaXNfc3RhZmYiOmZhbHNlLCJpc19zdXBlcnVzZXIiOmZhbHNlLCJ1c2VycyI6eyJpZCI6NSwidXNlcm5hbWUiOiJtYXJjZWxhX21hcmNlbGEiLCJpc19zdGFmZiI6ZmFsc2UsImlzX3N1cGVydXNlciI6ZmFsc2V9LCJwcm9maWxlIjp7ImNwZiI6IjUzMTgwNzc4MDMyIn0sInByZWZlcmVuY2VzX3VzZXIiOm51bGx9.nzBLSSrtFdhKajwElL5TH3SP7dg3SFyqo67GKsMIhac" }
``````
Consultar todos os usuários / Estrutura / Utilizar o token retorno no login : 
```sh
GET /api/v1/users/
```
Cadastrar um usuário já logado no sistema/ Estrutura : 
```sh
POST /api/v1/user/
```
```sh
{
  "first_name": "Fulano",
  "last_name": "Silva",
  "cpf": "000.000.000-00",
  "password": "password",
  "email": "fulanosilva@gmail.com",
  "group": id_group
}
```
Atualizar um usuário / Estrutura : 
```sh
PUT /api/v1/user/<int:pk>
```
```sh
{
  "first_name": "Fulano",
  "last_name": "Silva",
  "cpf": "000.000.000-00",
  "password": "password",
  "email": "fulanosilva@gmail.com",
  "group": id_group
}
```
Deletar um usuário / Estrutura : 
```sh
DELETE /api/v1/users/<int:pk>
```

Obter todos os produtos registrados no sistema/ Estrutura : 
```sh
GET /api/v1/products/
```

Obter um produto específico/ Estrutura : 
```sh
GET /api/v1/product/<int:pk>
```

Localização de um produto atráves de algum caractere, palavra relacionado ao seu nome / Estrutura : 
```sh
GET /api/v1/search/products/
```
```sh
{
  "search": "Raç"
}
```

Obter todos os carrinhos / Estrutura : (Aberto para estudo) 
```sh
GET /api/v1/carts
```

Obter o carrinho aberto relacionado ao usuário / Estrutura : 
```sh
<int:pk> = id do usuário

GET /api/v1/cart/<int:pk>
```

Obter todos os produtos registrados no sistema / Estrutura : 
```sh
POST /api/v1/cart/
```
```sh
Ao se criar um carrinho a quantidade solicitada do produto é subtraída do valor total em estoque (max_avaibility)

[
  {
    "product_id": "6",
    "quantity": "80"
  },
  {
    "product_id": "8",
    "quantity": "256"
  }
]
```

Atualizar um carrinho / Estrutura : 

```sh
PUT /api/v1/cart/
```
```sh
Ao se criar ou atualizar um carrinho, sua quantidade é verificada de acordo com o valor minimo de cada produto.
De acordo com a regras do sistema, entendeu-se que o a quantidade solicitada do produto no carrinho vezes a quantidade de itens por pacote, não poderia ser menor que a quantidade minima unitária.
Resumindo a quantidade solicitada entende-se ser "pacote" e não "unitário"

[
  {
    "product_id": "6",
    "quantity": "75"
  },
  {
    "product_id": "8",
    "quantity": "150"
  },
  {
    "product_id": "1"
    "quantity": "18"
  }
]
```


Deletar o carrinho / Estrutura : 
```sh
<int:pk> = id do usuário

DELETE /api/v1/cart/<int:pk>
```
```sh
Ao deletar um carrinho quantidade solicitada de cada produto é somanda ao valor total em estoque (max_avaibility) relacionado ao produto.

```

Consultar uma pedido realizado / Estrutura : 
```sh
<int:pk> = id do usuário

GET /api/v1/purchase/<int:pk>
```

Realizar um pedido / Estrutura : 
```sh
<int:pk> = id do usuário

POST /api/v1/purchase/<int:pk>
```
```sh
Ao realizar um pedido, deve se existir um carrinho para o usuário. 
Não é permitido se criar um novo pedido estando um pedido já em aberto. 
Não é permitido criar um pedido sem um carrinho.
(Criado um endpoint para exclusão do pedido embora nao exista regras para isso, mas para poder se testar a regras)
```

Deletar um pedido / Estrutura : 
```sh
<int:pk> = id do usuário

DELETE /api/v1/purchase/<int:pk>
```
```sh
Ao se deletar um pedido, as quantidades não são devolvidas aos respectivos estoques do produto. (Endpoint de teste.)
```


## Observações do projeto
Endpoint de grupo e permissões abertos para que se possa consultar os ids, uma vez que não existe interface frontend.
O sistema não possui um superusuario admin, logo os regitros dos usuários são abertos sendo controlados os grupos atráves de um paramentro chamado is_admin.

## Licença
Open source

## Desenvolvedor
Romário Vieira

versão 1.0.0

