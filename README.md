# <English/PT-BR>
# Dice API

This repository contains a small, open-source component of a larger personal project. Its purpose is to provide simple dice-rolling functionality through a RESTful API. Although part of a bigger project, this module is made available to the community for learning and use.

The API is built using **Flask** and packaged with **Poetry** for dependency management. It supports standard dice as well as RPG-style dice with modifiers.

## Features

* Roll standard dice with a specified number of sides and quantity.
* Roll RPG-style dice with optional modifiers.
* JSON responses suitable for integration with other projects.

## Installation

1. **Clone the repository**

```bash
git clone https://github.com/Dum2601/dice_rolling_API.git
cd dice-api
```

2. **Install dependencies using Poetry**

```bash
poetry install
```

3. **Activate the virtual environment**

```bash
poetry shell
```

## Running the API

Run the Flask server using:

```bash
flask run
```

By default, the API will be available at `http://127.0.0.1:5000`.

---

## API Endpoints

### 1. Standard Dice

**Endpoint:** `/die`
**Method:** `GET`

| Parameter | Type | Default | Description             |
| --------- | ---- | ------- | ----------------------- |
| sides     | int  | 6       | Number of sides per die |
| quantity  | int  | 1       | Number of dice to roll  |

**Example Request:**

```text
http://127.0.0.1:5000/die?sides=6&quantity=3
```

**Example Response:**

```json
[
  { "die_value": 4 },
  { "die_value": 2 },
  { "die_value": 6 }
]
```

---

### 2. RPG Dice

**Endpoint:** `/rpg-dice`
**Method:** `GET`

| Parameter | Type   | Default | Description                                      |
| --------- | ------ | ------- | ------------------------------------------------ |
| sides     | int    | 6       | Number of sides per die                          |
| quantity  | int    | 1       | Number of dice to roll                           |
| modifiers | string | ""      | Comma-separated integers to add to each die roll |

**Example Request:**

```text
http://127.0.0.1:5000/rpg-dice?sides=8&quantity=2&modifiers=1,2
```

**Example Response:**

```json
[
  {
    "die_value": 2,
    "modifiers_sum": 3,
    "total": 5
  },
  {
    "die_value": 1,
    "modifiers_sum": 3,
    "total": 4
  }
]
```

---

## Notes

* This project is part of a larger personal project but is provided open-source for the community.
* The software is licensed under the MIT License.

---

## License

MIT License © 2026 Douglas Barbosa

---

# Dice API

Este repositório contém um pequeno componente open-source de um projeto pessoal maior. Seu objetivo é fornecer funcionalidade simples de lançamento de dados através de uma API RESTful. Embora faça parte de um projeto maior, este módulo é disponibilizado à comunidade para aprendizado e uso.

A API é construída usando **Flask** e gerenciada com **Poetry** para controle de dependências. Ela suporta dados padrão, bem como dados de RPG com modificadores.

## Funcionalidades

* Lançar dados padrão com um número específico de lados e quantidade.
* Lançar dados de RPG com modificadores opcionais.
* Respostas em JSON adequadas para integração com outros projetos.

## Instalação

1. **Clone o repositório**

```bash
git clone https://github.com/Dum2601/dice_rolling_API.git
cd dice-api
```

2. **Instale as dependências usando Poetry**

```bash
poetry install
```

3. **Ative o ambiente virtual**

```bash
poetry shell
```

## Executando a API

Execute o servidor Flask usando:

```bash
flask run
```

Por padrão, a API estará disponível em `http://127.0.0.1:5000`.

---

## Endpoints da API

### 1. Dados Padrão

**Endpoint:** `/die`
**Método:** `GET`

| Parâmetro | Tipo | Padrão | Descrição                    |
| --------- | ---- | ------ | ---------------------------- |
| sides     | int  | 6      | Número de lados por dado     |
| quantity  | int  | 1      | Quantidade de dados a lançar |

**Exemplo de Requisição:**

```text
http://127.0.0.1:5000/die?sides=6&quantity=3
```

**Exemplo de Resposta:**

```json
[
  { "die_value": 4 },
  { "die_value": 2 },
  { "die_value": 6 }
]
```

---

### 2. Dados de RPG

**Endpoint:** `/rpg-dice`
**Método:** `GET`

| Parâmetro | Tipo   | Padrão | Descrição                                                           |
| --------- | ------ | ------ | ------------------------------------------------------------------- |
| sides     | int    | 6      | Número de lados por dado                                            |
| quantity  | int    | 1      | Quantidade de dados a lançar                                        |
| modifiers | string | ""     | Inteiros separados por vírgula para somar ao resultado de cada dado |

**Exemplo de Requisição:**

```text
http://127.0.0.1:5000/rpg-dice?sides=8&quantity=2&modifiers=1,2
```

**Exemplo de Resposta:**

```json
[
  {
    "die_value": 2,
    "modifiers_sum": 3,
    "total": 5
  },
  {
    "die_value": 1,
    "modifiers_sum": 3,
    "total": 4
  }
]
```

---

## Observações

* Este projeto faz parte de um projeto pessoal maior, mas é disponibilizado open-source para a comunidade.
* O software está licenciado sob a Licença MIT.

---

## Licença

MIT License © 2026 Douglas Barbosa
