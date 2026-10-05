# Order Delivery API

API REST para gerenciamento de pedidos de delivery, desenvolvida em Python com Flask e MongoDB.

O projeto foi criado com foco em **arquitetura de software, separação de responsabilidades, testes unitários e integração com banco de dados NoSQL**.

## 🚀 Tecnologias

* Python
* Flask
* MongoDB
* PyMongo
* Pytest
* Pylint

## 📌 Funcionalidades

A API permite:

* Criar pedidos
* Buscar um pedido pelo ID
* Atualizar informações de um pedido
* Persistir pedidos no MongoDB
* Tratar erros da aplicação
* Validar respostas através de testes automatizados

## 🏗️ Arquitetura

O projeto utiliza uma estrutura baseada em separação de responsabilidades:

```text
src/
├── errors/
│   ├── errors_handler.py
│   └── types/
│
├── main/
│   ├── composer/
│   ├── http_types/
│   └── routes/
│
├── models/
│   └── repositories/
│       └── interfaces/
│
└── use_cases/
```

O fluxo principal da aplicação segue a ideia:

```text
HTTP Request
     ↓
Route
     ↓
Composer
     ↓
Use Case
     ↓
Repository
     ↓
MongoDB
     ↓
HttpResponse
     ↓
JSON Response
```

Essa organização facilita a manutenção, os testes e a substituição de componentes da aplicação.

## 📡 Endpoints

### Criar pedido

```http
POST /delivery/order
```

Exemplo de requisição:

```json
{
    "customer_name": "João",
    "product": "Hambúrguer",
    "quantity": 2
}
```

### Buscar pedido

```http
GET /delivery/order/<order_id>
```

Exemplo:

```http
GET /delivery/order/68e2c8c9f123456789
```

Resposta:

```json
{
    "data": {
        "type": "order",
        "count": 1,
        "attributes": {
            "_id": "68e2c8c9f123456789",
            "customer_name": "João",
            "product": "Hambúrguer",
            "quantity": 2
        }
    }
}
```

### Atualizar pedido

```http
PATCH /delivery/order/<order_id>
```

Exemplo:

```json
{
    "status": "delivered"
}
```

## 🗄️ MongoDB

A aplicação utiliza o MongoDB para armazenar os pedidos.

Antes de executar a aplicação, é necessário ter uma instância do MongoDB disponível.

A conexão com o banco é centralizada através do módulo de conexão da aplicação, evitando que cada repository precise criar sua própria conexão.

## ⚙️ Instalação

Clone o projeto:

```bash
git clone <repository-url>
```

Entre no diretório:

```bash
cd order-com-mongodb
```

Crie um ambiente virtual:

```bash
python3 -m venv venv
```

Ative o ambiente virtual:

```bash
source venv/bin/activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

## ▶️ Executando a aplicação

Com o ambiente virtual ativado:

```bash
python3 run.py
```

A API ficará disponível localmente em:

```text
http://localhost:5000
```

## 🧪 Testes

Para executar os testes:

```bash
pytest -v
```

Para visualizar os testes com mais detalhes:

```bash
pytest -s -v
```

Os testes são utilizados para validar principalmente as regras dos casos de uso e o comportamento dos repositories.

## 🛡️ Tratamento de erros

A aplicação possui uma camada própria para tratamento de exceções.

Por exemplo, quando um pedido não é encontrado, o caso de uso gera uma exceção específica:

```python
raise HttpNotFoundError("order not found")
```

Essa exceção é posteriormente processada pelo `error_handler`, permitindo que a API retorne uma resposta HTTP adequada.

## 🎯 Objetivo do projeto

Este projeto tem como objetivo colocar em prática conceitos de desenvolvimento de APIs REST utilizando Python, incluindo:

* Arquitetura em camadas
* Repository Pattern
* Separação entre regras de negócio e infraestrutura
* Injeção de dependências
* Tratamento de exceções
* MongoDB
* Testes unitários
* Desenvolvimento de APIs REST

## 📚 Próximos passos

Algumas melhorias que podem ser implementadas futuramente:

* Autenticação de usuários
* Validação dos dados recebidos
* Paginação de pedidos
* Filtros por status
* Documentação com Swagger/OpenAPI
* Docker
* Testes de integração
* CI/CD

## 👨‍💻 Autor

**João Vitor Abreu**

Backend Developer | Python | Go

* GitHub: https://github.com/abreu-developer
* LinkedIn: https://www.linkedin.com/in/vitorabreudev
* Portfólio: https://vitorabreuportifolio.lovable.app
