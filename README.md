# Flask Authentication API — Aprendendo Flask

Este projeto faz parte do meu processo de aprendizado com **Python, Flask e desenvolvimento de APIs REST**.  
O foco principal é a **implementação de um sistema de autenticação de usuários**, com **controle de acesso**, **sessões**, **criptografia de senhas** e **perfis de usuário (roles)**.

A aplicação simula uma API real, permitindo **login, logout, cadastro, leitura, atualização e exclusão de usuários**, seguindo boas práticas de backend e integração com banco de dados relacional.

---

## Objetivo do projeto

Com este projeto, busquei aprender na prática:

- Autenticação e autorização de usuários em APIs REST
- Gerenciamento de sessão e cookies
- Proteção de rotas com controle de acesso
- Criptografia de senhas antes do armazenamento no banco
- Implementação de **roles de usuário (user e admin)**
- Integração do Flask com banco de dados relacional usando ORM

---

## Funcionalidades da API

- Cadastro de usuários com **senha criptografada**
- Login de usuários
- Logout (encerramento de sessão)
- Controle de sessão com cookies
- Proteção de rotas usando `login_required`
- Sistema de permissões baseado em roles:
  - **User**: acesso restrito às próprias informações
  - **Admin**: permissões administrativas
- CRUD completo de usuários:
  - Criar usuário
  - Buscar usuário por ID
  - Atualizar dados do usuário
  - Deletar usuário
- Comunicação via JSON
- Rotas REST organizadas e bem definidas

---

## Segurança

- As senhas **não são armazenadas em texto puro**
- Criptografia aplicada antes da persistência no banco de dados
- Validação de credenciais no processo de login
- Controle de acesso baseado em autenticação e role do usuário

---

## Pontos importantes do projeto

- API REST desenvolvida com Flask
- Autenticação e gerenciamento de sessão usando **Flask-Login**
- Uso de **cookies de sessão** para manter o usuário autenticado
- Integração com banco de dados MySQL via **SQLAlchemy**
- Uso de ORM para abstração das consultas SQL
- Implementação de autorização baseada em roles
- Testes manuais das rotas com Postman
- Projeto estruturado para aprendizado de backend real

---

## Tecnologias e versões utilizadas

- **Python 3.12**
- **Flask 3.0.3**
- **Werkzeug 3.0.3**
- **Flask-SQLAlchemy 3.1.1**
- **Flask-Login 0.6.3**
- **PyMySQL 1.1.0**
- **Cryptography 41.0.7**
- **MySQL** — banco de dados relacional
- **Postman** — testes manuais da API
- **Git** — controle de versão
- **GitHub** — hospedagem do projeto
- **Virtual Environment (venv)** — isolamento do ambiente

---

## Status do projeto

Projeto em desenvolvimento contínuo, utilizado como base de estudo para:

- Backend com Flask  
- APIs REST  
- Autenticação e autorização  
- Segurança de aplicações web  
- Boas práticas de desenvolvimento backend  
