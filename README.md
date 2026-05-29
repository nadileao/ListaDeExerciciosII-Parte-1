# Programação Orientada a Objetos - Lista de Exercícios II Parte I

## 🎓 Dados Acadêmicos

Informação| Detalhes
Universidade| Universidade Federal do Amazonas — UFAM
Instituto| ICET — Instituto de Ciências Exatas e Tecnologia
Curso| Sistemas de Informação
Disciplina| Programação Orientada a Objetos
Professor| Alternei Brito
Desenvolvido por| Nádia Maria Leão Xavier
Período| 2026.1
Linguagem| Python 3

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
│   ├── utils/
│   │   ├── __init__.py
│   │   └── formatador.py
│   └── main.py
├── SistemaFuncionarios/
│   ├── models/
│   ├── services/
│   ├── utils/
│   └── main.py
├── SistemaNotificacoes/
│   ├── models/
│   ├── services/
│   ├── utils/
│   └── main.py
├── SistemaImpressao/
│   ├── models/
│   ├── services/
│   ├── utils/
│   └── main.py
├── SistemaArmazenamento/
│   ├── models/
│   ├── services/
│   ├── utils/
│   └── main.py
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
📂 [`SistemaFuncionarios/`](./SistemaFuncionarios/)

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
📂 [`SistemaNotificacoes/`](./SistemaNotificacoes/)

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
📂 [`SistemaImpressao/`](./SistemaImpressao/)

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
📂 [`SistemaArmazenamento/`](./SistemaArmazenamento/)

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

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Uso |
|------------|-----|
| **Python 3.8+** | Linguagem principal |
| **`abc.ABC` / `@abstractmethod`** | Classes e métodos abstratos |
| **`typing.Protocol`** | Tipagem estrutural |

---

## 📋 Como Executar

```bash
# Clone o repositório
git clone <url-do-repositorio>

# Execute cada sistema
cd SistemaEducacional && python main.py
cd SistemaFuncionarios && python main.py
cd SistemaNotificacoes && python main.py
cd SistemaImpressao && python main.py
cd SistemaArmazenamento && python main.py
```

> **Requisito:** Python 3.8 ou superior.
```
