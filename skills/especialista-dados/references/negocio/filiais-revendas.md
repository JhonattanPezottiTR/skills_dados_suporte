# Filiais, revendas, regionais e grupos: como o fluxo `DB_SGD_ALL.sgd_resales` monta o retorno

> Última atualização: 2026-09-29 · Fonte: SQL da entidade `sgd_resales` do Dataflow `DB_SGD_ALL` (workspace Dominio FLOWS, lido pela API; ver `dados-fluxo-db_sgd_all.md` §`sgd_resales`), `negocio-conceitos.md` §1 (citações do Maestro `clients_sgd.py`/`rotinas.py` e do `sql-base`) · **Arquivo curado** · Status: **Em revisão** (as listas são literais do SQL; o significado oficial precisa ser validado pelo time)

## 1. A consulta (Dataflow `DB_SGD_ALL` → entidade `sgd_resales`)

- **Origem:** Postgres `DB_SGD.public.sgd_resale`, uma linha por revenda.
- **Carga:** recarga total pelo job `import-sgd-diario` a partir do Sybase `bethadba.vw_revendas`, com `i_controle` → `i_resale` e `apelido` → `name_resale`.
- **Colunas vindas da tabela:** `i_resale`, `name_resale` (apelido) e `active` (0/1/2; o ETL usa `ativa = 1`).
- **Colunas calculadas no próprio SQL do fluxo**, com três CASE independentes:

### 1.1 `type_resale` (tipo): Filiais × Revendas
```sql
CASE WHEN i_resale IN (3,4,13,14,18,40,74,83,102,137,144,155,156,160,163) THEN 'Filiais' ELSE 'Revendas' END
```
- São **15 códigos = Filiais**. Tudo o mais é "Revendas", **inclusive a 1 (UPG), a 148 (Testes Internos) e a 165 (Domínio Inova)**.

### 1.2 `regiao_atend` (região de atendimento)
```sql
CASE WHEN i_resale IN (40,102,155,160,163)             THEN 'Campinas'
     WHEN i_resale IN (1,3,4,13,18,74,83,137,144,156)  THEN 'Sul'
     WHEN i_resale IN (1,148)                          THEN 'Interno(UPG-USI)'
     ELSE 'Demais' END
```
- O CASE é avaliado **em ordem**. A revenda **1** cai em **Sul**, e o ramo "Interno(UPG-USI)" só é atingido pela **148**.
- Os códigos **14** e **155/160/163** são Filiais. A 14 **não tem região**: cai em "Demais".

### 1.3 `agrupado` (grupo comercial / parceiro)
| Grupo | Revendas | | Grupo | Revendas |
|---|---|---|---|---|
| 2B | 57 | | Soft News - GO + CE + DF | 7, 37, 131, 140 |
| Alpha | 76 | | Teknordeste PB + RN | 161, 27 |
| Atlas | 17 | | Teknorte | 64 |
| Campos | 41 | | Tekplan RS + PA | 134, 36 |
| Designer + R&S | 166, 85, 10 | | Teksul + Sibrum | 84, 16 |
| Gtek SM + XAP | 31, 67 | | Tekvale | 51 |
| Harv | 109 | | Tool - POO + BHZ | 63, 75 |
| Implantta - AL + SE + PE | 5, 81 | | **UNCWB** | 4 |
| J.DREL - MT + AM + ES | 25, 54, 77, 103 | | **UNPOA** | 13 |
| Modulo | 22 | | **UNRIO** | 74 |
| Moretto | 18 | | **UNSAO - Capital** | 40 |
| Novo Oeste | 32 | | **UNSAO - Interior** | 160 |
| PC + PC Minas | 69, 152 | | **UNSC** | 3 |
| | | | **Interno(UPG-USI)** | 1, 148 |

- Qualquer código fora dessa lista recebe `''` (vazio), e não "Outros".
- Os grupos `UN*` são as unidades comerciais próprias: UNSC = 3, UNCWB = 4, UNPOA = 13, UNRIO = 74, UNSAO = 40/160. Elas batem com as **Filiais da visão comercial** do `sql-base` (3, 4, 13, 40, 74, 160).
- A **18 (Moretto)** é "Filiais" em `type_resale`, mas aparece como parceira em `agrupado`.

## 2. Nomes das revendas internas relevantes (catálogo `sql-base`)
| Código | Nome |
|---|---|
| 1 | Unidade de Produção e Gestão – UP&G (**UPG**) |
| 82 | Suporte a Clientes – Secundários |
| 83 | Suporte a Clientes – Regional Sul |
| 86 | Unidade de produção (UP) |
| 98 | Suporte a Clientes – Salvador |
| 102 | Suporte a Clientes – Campinas |
| 104 | Apoio às Unidades |
| 112 | UPG – **TeleVendas** (excluída de clientes e contratos) |
| 137 | Suporte a Clientes – Porto Alegre |
| 144 | Suporte a Clientes – Curitiba |
| 148 | Unidade Testes Internos (**USI**) |
| 155 | Suporte a Clientes – São Paulo |
| 156 | Suporte a Clientes – Criciúma AT |
| 157 | Suporte a Clientes – Salvador AT |
| 163 | Suporte a Clientes – São Paulo AT |
| 165 | Domínio Inova |

## 3. ⚠️ Cada lugar classifica de um jeito (não misture sem avisar)
| Onde | "Filiais" | Diferença para o fluxo `sgd_resales` |
|---|---|---|
| **Fluxo `DB_SGD_ALL.sgd_resales`** (referência deste arquivo) | 3,4,13,14,18,40,74,83,102,137,144,155,156,160,163 | — |
| `DB_SGD.sgd_users.type_resale` (colaborador; usado por `tb_colaboradores`) | mesma lista **sem 18**, **com 165**; a revenda 1 = **"UPG"** | não tem 18, tem 165, e a 1 vira "UPG" |
| `DB_SGD.sgd_client.type_resale` (cliente) | mesma lista **com 148** | tem 148 |
| Dataflow `sgd_users` | acrescenta `'BOT-IA'` para os usuários 1405244 e 1444989 | tipo extra |
| Agenda em tempo real (`TB_SYBASE_SGD_AGENDA.unidade`) | 102/**144** = Regional Campinas; 83/82/137 = Regional Sul; 155 = AT Campinas; 156 = AT Criciúma; 163 = AT SP; 1 = CTD | a **144 é Campinas** aqui e **Sul** no fluxo; a 1 é CTD |
| `sql-base` (visão comercial/ERP) | 3,4,13,40,74,160 | só as unidades comerciais UN* |
| ETL do SGD (`REG_*`, `REVENDAS_COM18`) | **não é lista de filiais**: define **quais revendas são importadas** | — |

## 4. Como usar num BI (padrão até o time validar)
1. **Dimensão de revenda = entidade `DB_SGD_ALL.sgd_resales`** (tabela `dRevenda`):
   - chave `i_resale`;
   - atributos `name_resale` → *Revenda*, `type_resale` → *Tipo*, `regiao_atend` → *Região de atendimento* e `agrupado` → *Grupo*;
   - `active` fica oculta.
2. **Relacionamento:** fato[`i_resale`] → `dRevenda[i_resale]`, 1:N, direção única. Isso vale para qualquer fato do SGD que tenha `i_resale` (SSC, usuários, clientes).
3. **Tipo do cliente ou do colaborador:**
   - Se a pergunta for sobre o **colaborador** (produtividade, demanda de líderes, `tb_colaboradores`), o time usa `sgd_users.type_resale`, porque é o que os relatórios de líderes filtram (`tipo_resale = 'Filiais'`).
   - Se for sobre o **cliente**, use `sgd_client.type_resale`.
   - Diga ao usuário qual das duas classificações foi usada.
4. **Região:**
   - `regiao_atend` do fluxo é a padrão para BI analítico;
   - para agenda e escala em tempo real, use a `unidade` do próprio fluxo de agenda;
   - **avise** que a 144 e a 1 divergem entre as duas.
5. **Sempre sinalize "Em revisão"** quando o número depender dessas listas, e aponte a pergunta em `negocio-perguntas-em-aberto.md`: qual é a lista oficial de filiais e o de-para revenda → regional.

## 5. Perguntas para o time (resumo)
- A lista oficial de Filiais é a do fluxo (15 códigos), a de usuários (com 165 e sem 18) ou a comercial (6 códigos)?
- A 144 (Curitiba) é da regional Sul ou de Campinas?
- A revenda 1 (UPG) deve aparecer como Sul, Interno, CTD ou UPG?
- A 14 é filial sem região ("Demais")?
- A 18 é filial ou parceira (Moretto)?
- O que significa `active = 2`?
