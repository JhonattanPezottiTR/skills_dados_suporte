# Formato padrão de regras

> Última atualização: 2026-09-29 · Fonte: definição interna do time de BI

Toda regra ensinada pelo time é registrada neste formato, para que a IA entenda **o quê**, **por quê** e **como aplicar** — sem ambiguidade.

## Prefixos de ID

| Prefixo | Categoria | Arquivo |
|---|---|---|
| `REG-###` | Regra de negócio (KPI, cálculo, filtro, definição) | `regras-negocio.md` |
| `COR-###` | Cores, tema e padrão visual | `powerbi-tema-cores.md` |
| `NOM-###` | Nomenclatura (tabelas, colunas, medidas, arquivos) | `regras-negocio.md` |
| `FON-###` | Fontes de dados, bases, fluxos (Dataflows/Pipelines) | `regras-negocio.md` |
| `SQL-###` | Padrão SQL específico do time | `regras-negocio.md` |
| `DAX-###` | Padrão DAX específico do time | `regras-negocio.md` |

IDs são **sequenciais e nunca reutilizados**. Regra revogada fica com status `Revogada` (não é apagada).

## Modelo

```markdown
### REG-001 · <Título curto>
- **Status:** Ativa | Em revisão | Revogada (substituída por REG-xxx)
- **Criada em:** AAAA-MM-DD · **Atualizada em:** AAAA-MM-DD
- **Origem:** conversa com <área/pessoa> | documento <nome> | reunião <data>
- **Escopo:** onde se aplica (relatório X, todos os modelos, tabela Y...)
- **Regra:** enunciado objetivo e verificável.
- **Justificativa:** por que existe.
- **Como aplicar:** instrução prática para a IA.
- **Exemplo válido:**
  ```sql / dax / texto
  ...
  ```
- **Exemplo inválido:**
  ```
  ...
  ```
- **Relacionadas:** REG-xxx, COR-xxx
```

## Princípios
1. Uma regra = uma ideia. Se tiver "e", provavelmente são duas.
2. Verificável: deve ser possível dizer se uma resposta cumpre ou não.
3. Sempre com exemplo válido e inválido quando houver código.
4. Datas no formato ISO (AAAA-MM-DD).
