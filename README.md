# 🚀 TW Todos - Gerenciador de Tarefas com Django

O **TW Todos** é uma aplicação web de gerenciamento de tarefas desenvolvida com o framework **Django**. O projeto foi construído para colocar em prática conceitos de desenvolvimento backend, segurança de dados e estilização responsiva.

## 📋 Funcionalidades

- **Autenticação Completa:** Sistema de registro de usuários, login e logout, garantindo que cada usuário tenha sua lista privada.
- **Gerenciamento de Tarefas (CRUD):** Criar, visualizar, editar e excluir tarefas de forma intuitiva.
- **Status de Conclusão:** Marcar tarefas como finalizadas com um único clique.
- **Interface Responsiva:** Desenvolvida com Bootstrap para funcionar perfeitamente em dispositivos móveis e desktop.

---

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python 3.14+
- **Framework Web:** Django 5.1+
- **Frontend:** Bootstrap 5 (via `django-bootstrap5`)
- **Segurança e Ambiente:** - `python-decouple`: Gerenciamento de variáveis de ambiente (SECRET_KEY).
    - `dj-database-url`: Configuração dinâmica de banco de dados.
- **Banco de Dados:** SQLite (Desenvolvimento).

---

## 🏗️ Estrutura do Projeto

O projeto utiliza **Class-Based Views (CBVs)**, seguindo as melhores práticas do Django para um código limpo e reutilizável:

* `TodoListView`: Exibe a lista de tarefas do usuário logado.
* `TodoCreateView`: Formulário para novas tarefas.
* `TodoUpdateView` / `TodoDeleteView`: Edição e remoção.
* `TodoCompleteView`: Lógica rápida para alteração de status da tarefa.
   ```bash
   git clone [https://github.com/JoaoMMA/twtodos.git](https://github.com/JoaoMMA/twtodos.git)
   cd twtodos
