# 🚀 Mini API Motoboy

API desenvolvida em Python com FastAPI para gerenciamento de pedidos e motoboys, simulando o fluxo real de entregas (estilo iFood), com foco em lógica de negócio e organização backend.

---

## 🏪 Aplicação no Mundo Real

Este projeto foi pensado para atender pequenos e médios negócios que possuem entregadores próprios (motoboys), como lanchonetes, pizzarias e restaurantes locais.

A API permite organizar o fluxo de pedidos de forma eficiente, garantindo uma melhor distribuição das entregas com base na disponibilidade dos motoboys.

Com o controle de status (livre/ocupado), é possível priorizar automaticamente os entregadores disponíveis, evitando sobrecarga e melhorando o tempo de resposta nas entregas.

Essa abordagem simula uma logística semelhante a grandes plataformas de delivery, porém adaptada para uma realidade mais simples e acessível.

---

## 📌 Funcionalidades

### 📦 Pedidos

* Criar pedido

* Listar pedidos

* Buscar pedido por ID

* Deletar pedido

* Atualização de status:

  * Aceitar pedido
  * Marcar como preparo
  * Marcar como pronto
  * Cancelar pedido
  * Aguardar motoboy
  * Iniciar rota
  * Finalizar entrega
  * Falha na entrega

---

### 🛵 Motoboys

* Criar motoboy

* Listar motoboys

* Buscar motoboy por ID

* Deletar motoboy

* Controle de status:

  * Ativar/Desativar
  * Livre/Ocupado

---

## 🔄 Fluxo do Pedido

```text
PENDENTE
→ ACEITO
→ PREPARO
→ PRONTO
→ AGUARDANDO_MOTOBOY
→ EM_ROTA
→ ENTREGUE
        ↘
         FALHA_ENTREGA
```

---

## 🧠 Regras de Negócio

* Pedido só pode iniciar rota se tiver motoboy atribuído
* Motoboy não pode pegar mais de um pedido ao mesmo tempo
* Pedido não pode pular etapas do fluxo
* Motoboy volta a ficar livre após entrega ou falha
* Controle de prioridade baseado em motoboys disponíveis

---

## 🛠️ Tecnologias

* Python
* FastAPI
* SQLAlchemy
* SQLite

O uso do SQLAlchemy permite uma fácil adaptação para outros bancos de dados como PostgreSQL, MySQL ou Oracle, sem necessidade de grandes mudanças no código, garantindo flexibilidade e escalabilidade para o projeto.

---

## ⚠️ Sobre Interface

Este projeto é focado exclusivamente no backend.

Não possui interface gráfica (frontend) no momento, sendo totalmente acessado via requisições HTTP.

Caso necessário, pode ser integrado facilmente com:

* aplicações web (React, Vue, etc.)
* aplicativos mobile
* ou ferramentas como Postman/Insomnia

---

## ▶️ Como rodar o projeto

```bash
# Clonar repositório
git clone https://github.com/seu-usuario/seu-repo.git

# Entrar na pasta
cd seu-repo

# Criar ambiente virtual
python -m venv venv

# Ativar ambiente (Windows)
venv\Scripts\activate

# Instalar dependências
pip install -r requirements.txt

# Rodar servidor
uvicorn main:app --reload
```

---

## 📄 Documentação da API

Após rodar o projeto, acesse:

```
http://127.0.0.1:8000/docs
```

Interface interativa gerada automaticamente pelo FastAPI (Swagger UI).

---

## 💡 Diferenciais do Projeto

* Uso de Enum para controle de status
* Separação em camadas (Router, Service, Repository)
* Regras de negócio bem definidas
* Simulação de fluxo real de entregas
* Controle de disponibilidade de motoboys

---

## 🎯 Objetivo

Projeto desenvolvido para prática de desenvolvimento backend, com foco em:

* lógica de negócio
* organização de código
* construção de APIs REST
* simulação de cenários reais

---

## 📌 Autor

Desenvolvido por Isaias-Morais
