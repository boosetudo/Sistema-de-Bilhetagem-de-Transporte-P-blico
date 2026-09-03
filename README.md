## Sobre o projeto

O projeto consiste no desenvolvimento de um sistema de bilhetagem para a cidade fictícia de **TechVille**, capaz de gerenciar usuários de diferentes categorias, seus saldos, recargas e compras de passagens.

O sistema trabalha com três categorias de usuários:

* **Padrão:** paga o valor integral da passagem;
* **Estudante/idoso:** paga 50% do valor da passagem;
* **Social:** paga 20% do valor da passagem.

O valor da tarifa pode ser configurado no início do programa, permitindo que o sistema seja reutilizado em diferentes cidades.

## Funcionalidades

O sistema possui um menu interativo com as seguintes opções:

1. **Cadastrar usuário**

   * Cadastro do nome completo;
   * Possibilidade de utilização de nome social;
   * Cadastro do CPF;
   * Seleção da categoria do usuário.

2. **Visualizar saldo**

   * Consulta do saldo disponível no cartão.

3. **Fazer recarga**

   * Adição de créditos ao cartão;
   * Exibição do saldo anterior e do novo saldo.

4. **Comprar passagem(ns)**

   * Verificação da quantidade de passagens que o saldo permite comprar;
   * Verificação de saldo suficiente;
   * Desconto automático do valor das passagens.

5. **Gerar relatório**

   * Acesso restrito aos administradores;
   * Quantidade de usuários por categoria;
   * Total de recargas;
   * Número de recargas;
   * Quantidade de passagens compradas;
   * Saldo restante por categoria.

6. **Fechar sistema**

A estrutura do menu e suas funcionalidades estão implementadas diretamente no código-fonte.

## Tarifas

O programa utiliza uma tarifa-base configurável. No código entregue, o valor inicial definido é de **R$ 4,80**.

| Categoria       |  Tarifa |
| --------------- | ------: |
| Padrão          | R$ 4,80 |
| Estudante/idoso | R$ 2,40 |
| Social          | R$ 0,96 |

Os valores das categorias com desconto são calculados automaticamente a partir da tarifa-base.

## Relatório administrativo

O sistema possui uma área destinada aos administradores, protegida por autenticação, onde são apresentadas informações agregadas sobre o funcionamento do sistema.

Entre os dados apresentados estão:

* Usuários registrados por categoria;
* Saldo total por categoria;
* Total de passagens compradas por categoria;
* Número de recargas realizadas por categoria.

Esses dados são contabilizados durante a utilização do sistema.

## Tecnologias

* **Python**
* Entrada e saída de dados pelo terminal
* Estruturas condicionais (`if`, `elif`, `else`)
* Estruturas de repetição (`while`)
* Variáveis e operações aritméticas
* Formatação de strings com *f-strings*

## Como executar

Clone o repositório:

```bash
git clone https://github.com/boosetudo/Sistema-de-Bilhetagem-de-Transporte-P-blico.git
```

Entre na pasta do projeto:

```bash
cd Sistema-de-Bilhetagem-de-Transporte-P-blico
```

Execute o programa:

```bash
python3 AntonioCarneiro.py
```

O sistema será iniciado diretamente no terminal e apresentará o menu principal.

## Contexto acadêmico

**Disciplina:** MI de Algoritmos
**Problema:** 1
**Tema:** Sistema de Bilhetagem de Transporte Público
**Linguagem:** Python
**Ano:** 2025.1

O problema propunha a construção de um algoritmo em fluxograma, seu código-fonte em Python e um relatório descrevendo o desenvolvimento do sistema.

## Autoria

Projeto desenvolvido individualmente como atividade acadêmica da MI de Algoritmos.

O código-fonte contém a declaração de autoria e não plágio exigida pela atividade.
