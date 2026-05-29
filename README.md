# Programação Orientada a Objetos - Lista de Exercícios II Parte I

## 📚 Informações Gerais

**Universidade:** Universidade Federal do Amazonas — UFAM  
**Curso:** Sistemas de Informação  
**Disciplina:** Programação Orientada a Objetos  
**Professor:** Alternei Brito  
**Autora:** Nádia Maria Leão Xavier
**Ano:** 2026


## 📁 Estrutura do Repositório

```
ListaDeExerciciosII-Parte-1/
├── SistemaEducacional/
│   ├── models/
│   │   ├── __init__.py
│   │   ├── midia.py
│   │   ├── video.py
│   │   ├── podcast.py
│   │   └── texto_narrado.py
│   ├── services/
│   │   ├── __init__.py
│   │   └── plataforma.py
│   └── main.py
│
├── SistemaDeEmpresa/
│   ├── models/
│   │   ├── __init__.py
│   │   ├── funcionario.py
│   │   ├── funcionario_assalariado.py
│   │   ├── funcionario_horista.py
│   │   └── funcionario_comissionado.py
│   ├── services/
│   │   ├── __init__.py
│   │   └── empresa.py
│   └── main.py
│
├── SistemaDeNotificacoes/
│   ├── models/
│   │   ├── __init__.py
│   │   ├── notificador.py
│   │   ├── notificador_email.py
│   │   ├── notificador_sms.py
│   │   └── notificador_app.py
│   ├── services/
│   │   ├── __init__.py
│   │   └── central_notificacoes.py
│   └── main.py
│
├── SistemaDeImpressao/
│   ├── models/
│   │   ├── __init__.py
│   │   ├── imprimivel.py
│   │   ├── boleto.py
│   │   ├── etiqueta.py
│   │   └── relatorio_simples.py
│   ├── services/
│   │   ├── __init__.py
│   │   └── processador.py
│   └── main.py
│
├── SistemaDeArmazenamento/
│   ├── models/
│   │   ├── __init__.py
│   │   ├── armazenador.py
│   │   ├── armazenador_arquivo.py
│   │   ├── armazenador_banco.py
│   │   ├── salvavel.py
│   │   └── armazenador_nuvem.py
│   ├── services/
│   │   ├── __init__.py
│   │   └── executores.py
│   └── main.py
│
└── README.md
```

---

## 🧩 Exercícios

### 1️⃣ Sistema Educacional de Mídias
📂 [`SistemaEducacional/`](./SistemaEducacional/)

Plataforma educacional que gerencia diferentes tipos de mídia de forma polimórfica.

**Hierarquia:**
```
Midia (ABC)
├── Video         → resolucao
├── Podcast       → apresentador
└── TextoNarrado  → idioma
```

**Conceitos:** `ABC`, `@abstractmethod`, herança, polimorfismo em `reproduzir()`.

---

### 2️⃣ Sistema de Funcionários
📂 [`SistemaDeEmpresa/`](./SistemaDeEmpresa/)

Folha de pagamento com diferentes regimes de contratação.

**Hierarquia:**
```
Funcionario (ABC)
├── FuncionarioAssalariado   → salario_mensal
├── FuncionarioHorista       → horas_trabalhadas × valor_hora
└── FuncionarioComissionado  → total_vendas × (percentual_comissao / 100)
```

**Conceitos:** `@abstractmethod` em `calcular_pagamento()`, polimorfismo, encapsulamento.

---

### 3️⃣ Sistema de Notificações
📂 [`SistemaNotificacoes/`](./SistemaNotificações/)

Sistema multi-canal de notificações usando ABC.

**Hierarquia:**
```
Notificador (ABC)
├── NotificadorEmail
├── NotificadorSMS
└── NotificadorApp

CentralNotificacoes → agrega notificadores e dispara para todos
```

**Conceitos:** ABC como contrato de interface, polimorfismo, extensibilidade.

---

### 4️⃣ Sistema de Impressão
📂 [`SistemaDeImpressao/`](./SistemaDeImpressao/)

Demonstra tipagem estrutural com `typing.Protocol`.

**Estrutura:**
```
Imprimivel (Protocol)  → contrato: imprimir()

Boleto                 → implementa imprimir() sem herdar
Etiqueta               → implementa imprimir() sem herdar
RelatorioSimples       → implementa imprimir() sem herdar
```

**Conceitos:** `typing.Protocol`, duck typing formal, desacoplamento estrutural.

---

### 5️⃣ Sistema de Armazenamento
📂 [`SistemaDeArmazenamento/`](SistemaDeArmazemento/)

Exercício comparativo entre ABC e Protocol no mesmo problema.

**Estrutura:**
```
── Parte A: ABC ─────────────────────────────
Armazenador (ABC)
├── ArmazenadorArquivo
└── ArmazenadorBanco

── Parte B: Protocol ────────────────────────
Salvavel (Protocol)
└── ArmazenadorNuvem  (sem herança explícita)

── Parte C: Funções ─────────────────────────
executar_salvamento_formal()   → exige herança de Armazenador
executar_salvamento_flexivel() → aceita qualquer Salvavel
```

**Conceitos:** ABC vs Protocol, tipagem nominal vs estrutural.

---
## ▶️ Instruções para Execução e Reprodução

### Pré-requisitos
Antes de executar, certifique-se de ter instalado:
- **Python 3.8 ou superior**

Para verificar sua versão do Python:
```bash
python --version
```

---

### Como obter o projeto

**Opção 1 — Clonar via Git:**
```bash
git clone https://github.com/nadileao/ListaDeExerciciosII-Parte-1.git
cd ListaDeExerciciosII-Parte-1
```

**Opção 2 — Baixar manualmente:**
- Clique em **Code** → **Download ZIP**
- Extraia o arquivo
- Abra a pasta no terminal

---

### Como executar cada sistema

Entre na pasta do sistema desejado e execute o `main.py`:

```bash
# Sistema 1 — Mídias Educacionais
cd SistemaEducacional
python main.py

# Sistema 2 — Funcionários
cd SistemaFuncionarios
python main.py

# Sistema 3 — Notificações
cd SistemaNotificacoes
python main.py

# Sistema 4 — Impressão
cd SistemaImpressao
python main.py

# Sistema 5 — Armazenamento
cd SistemaArmazenamento
python main.py
```

---
