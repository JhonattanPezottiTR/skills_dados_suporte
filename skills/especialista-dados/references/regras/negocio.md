# Regras de negócio, nomenclatura e fontes do time

> Última atualização: 2026-09-29 · Fonte: regras ensinadas pelo time de BI · Formato: ver `regras-formato.md`

**Prioridade máxima:** as regras deste arquivo prevalecem sobre qualquer boa prática genérica.

## Índice

| ID | Título | Status | Atualizada em |
|---|---|---|---|
| REG-001 | Significado de SA / NE / SAL / SAIL | Ativa | 2026-09-30 |
| REG-002 | "Cliente" sempre filtra `terceiro = 0` | Ativa | 2026-09-30 |
| REG-003 | "Produto" sem qualificação = produtos principais | Ativa | 2026-09-30 |
| FON-001 | DB_GENESYS: métricas seguem a Analytics API da Genesys Cloud | Em revisão | 2026-09-30 |

---

## Regras de negócio (REG)

### REG-001 · Significado de SA / NE / SAL / SAIL
- **Status:** Ativa
- **Criada em:** 2026-09-30 · **Atualizada em:** 2026-09-30
- **Origem:** conversa com o usuário (2026-09-30), resolvendo a divergência P-11 registrada em `negocio-perguntas-em-aberto.md`
- **Escopo:** qualquer SSC/trâmite do SGD com o campo `reason`/`motivo` (SA/NE/SAL/SAIL) — DB_SGD_ALL, sql-base, relatórios de SSC
- **Regra:**
  - **SA** = Solicitação de Alteração
  - **NE** = Notificação de Erro
  - **SAL** = Solicitação de Alteração Legal
  - **SAIL** = Solicitação de Implementação Legal
- **Justificativa:** o glossário anterior da skill e o sql-base tinham definições divergentes/incompletas (glossário antigo: "Sugestão de alteração / necessidade"; sql-base: "NE = Nova Especificação"; SAL/SAIL sem definição). O usuário confirmou o significado oficial.
- **Como aplicar:** usar esses quatro nomes sempre que o texto publicado (relatório, resposta, documentação) mencionar SA/NE/SAL/SAIL. Os **códigos** numéricos ainda divergem entre fontes (Dataflow `reason`: 0=NE/1=SA/2=SAL/3=SAIL; sql-base `motivo`: 1=SAM/2=SAL/3=SAIL) — isso não foi resolvido por esta regra, só o **nome** de cada sigla. Para de-para numérico, seguir `dados-sgd-regras-e-joins.md` e sinalizar se os códigos não baterem.
- **Exemplo válido:**
  ```texto
  "NE (Notificação de Erro) é diferente de SA (Solicitação de Alteração):
  NE reporta um problema no sistema, SA pede uma mudança de comportamento."
  ```
- **Exemplo inválido:**
  ```texto
  "NE = Nova Especificação" (definição antiga do sql-base, substituída por esta regra)
  ```
- **Relacionadas:** resolve P-11 (`negocio-perguntas-em-aberto.md`); `glossario.md` (verbete SA/NE).

### REG-002 · "Cliente" sempre filtra `terceiro = 0`
- **Status:** Ativa
- **Criada em:** 2026-09-30 · **Atualizada em:** 2026-09-30
- **Origem:** conversa com o usuário (2026-09-30)
- **Escopo:** qualquer query, medida ou resposta que fale de **clientes** (usuários de cliente, contagem de clientes, base de clientes) usando `power_bi.vw_usuarios`/`sgd_user_client`/tabelas derivadas com o campo `terceiro`
- **Regra:** sempre que o filtro/joins/medida se referir a **clientes**, o campo `terceiro` tem que ser `0`. Isso já era usado no ETL (`i_clientes is not null and terceiro = 0`, `clients_sgd.py:250-253`) — a regra torna isso explícito e obrigatório para qualquer SQL/DAX novo que a skill gerar, mesmo fora do ETL existente.
- **Justificativa:** `terceiro = 1` marca representante/terceiro, não o cliente em si; incluir `terceiro = 1` no filtro de "clientes" conta representantes como se fossem clientes, inflando a base.
- **Como aplicar:** ao montar SQL/DAX/medida que filtre ou agregue por "cliente", sempre incluir `terceiro = 0` junto do filtro de `i_clientes`/`i_client` (mesmo se o pedido do usuário não mencionar `terceiro`). Ver `negocio-conceitos.md` §3.1 para o detalhe de onde o campo `terceiro` aparece em cada camada (Sybase → Postgres → Dataflow).
- **Exemplo válido:**
  ```sql
  where u.i_clientes is not null and u.terceiro = 0
  ```
- **Exemplo inválido:**
  ```sql
  where u.i_clientes is not null
  -- (sem o filtro de terceiro, mistura representante/terceiro com cliente)
  ```
- **Relacionadas:** `negocio-conceitos.md` §3.1 (Usuário interno × cliente × terceiro); RG-01/RG-14 (nunca inventar/distorcer dado).

### REG-003 · "Produto" sem qualificação = produtos principais
- **Status:** Ativa
- **Criada em:** 2026-09-30 · **Atualizada em:** 2026-09-30
- **Origem:** conversa com o usuário (2026-09-30)
- **Escopo:** qualquer pergunta, query, medida ou BI que mencione "produto"/"produtos" do SGD sem citar um produto específico
- **Regra:** toda menção genérica a "produto" (sem nomear um produto específico) deve ser entendida como os **produtos principais** — códigos `101, 102, 103, 104, 170, 211, 212, 213` (Plus, Start, Personalizado, Empresarial, Premium, One, Pro, Domínio Max) — **exceto** quando o pedido citar explicitamente outro produto (ex.: "Domínio WEB 2.0", "Messenger", código periférico específico), caso em que vale só o produto citado.
- **Justificativa:** é a mesma lista já documentada como "produtos principais" no sql-base (`DICIONARIO_NEGOCIOS.md:495`) e usada no forecast (`forecast.py:404-406`); tratar "produto" de forma genérica sem essa lista mistura produtos periféricos (ex. 145, 173, 221) na análise e distorce contagens/receita.
- **Como aplicar:** ao montar SQL/DAX/medida/resposta sobre "produto" sem nome específico, filtrar/considerar só os 8 códigos de produtos principais. Se o usuário citar um produto periférico específico (por nome ou código), usar somente aquele — não misturar com a lista de principais.
- **Exemplo válido:**
  ```sql
  where i_produtos in (101,102,103,104,170,211,212,213)  -- "produto" genérico
  ```
- **Exemplo inválido:**
  ```sql
  where i_produtos = 145  -- respondendo "produto" genérico com um periférico (Domínio WEB 2.0)
  ```
- **Relacionadas:** `negocio-conceitos.md` §2.3 (Produto — principais × demais); P-09 (`negocio-perguntas-em-aberto.md`).

## Nomenclatura (NOM)

*(vazio)*

## Fontes de dados e fluxos (FON)

O mapa técnico das fontes (bases, tabelas, jobs, Dataflows, linhagem) fica nos arquivos `dados-*` (gerados). Aqui entram só as **regras** sobre fontes definidas pelo time, por exemplo "o BI X deve usar a entidade Y".

Os códigos de negócio extraídos do código (situações, pendência, satisfação...) estão em `dados-sgd-regras-e-joins.md` com status **Em revisão**. Quando o time validar, cada um vira uma regra `REG-###` aqui.

### FON-001 · DB_GENESYS: métricas seguem a Analytics API da Genesys Cloud
- **Status:** Em revisão (extraído da documentação oficial Genesys Cloud e do código do Maestro, não confirmado pelo time)
- **Criada em:** 2026-09-30 · **Atualizada em:** 2026-09-30
- **Origem:** cruzamento entre `dados-fluxo-db_genesys.md` (colunas reais), `dados-fluxos-maestro.md` (endpoints `genesys_import`) e a documentação oficial developer.genesys.cloud/help.genesys.cloud
- **Escopo:** qualquer pergunta, query ou BI sobre as bases `DB_GENESYS`/`DB_GENESYS_TRANSCRIPTIONS`
- **Regra:** toda coluna `metric_*`/`_n*`/`_t*`/`_o*` do DB_GENESYS corresponde 1:1 a uma métrica oficial da **Genesys Cloud Analytics API** (convenção `n`=contador, `t`=timer em ms, `o`=observação). O significado de cada uma está em `genesys-glossario-metricas.md` — nunca redefinir ou inventar um significado diferente do documentado ali.
- **Justificativa:** os nomes vêm direto da API da Genesys (via `conversations/aggregates/query` e `conversations/details/query`, `genesys_import`); tratá-los como colunas "do time" gera divergência com a doc oficial e com qualquer relatório nativo da Genesys.
- **Como aplicar:** ao responder algo sobre DB_GENESYS, consultar `genesys-glossario-metricas.md` pelo nome da coluna. Se a linha estiver marcada **Confirmado**, usar a definição direto. Se estiver **Em revisão**, usar a definição só como hipótese e avisar o usuário explicitamente que não foi confirmada na documentação oficial.
- **Exemplo válido:**
  ```texto
  "TMA aqui é a coluna metric_tHandle, que na Genesys é a métrica oficial tHandle
  (fala + hold + ACW). Confirmado na doc oficial."
  ```
- **Exemplo inválido:**
  ```texto
  "TMA é metric_tHandle, que deve ser tTalk + tAcw" (inventa uma composição
  diferente da documentada, sem citar a fonte)
  ```
- **Relacionadas:** ver também a divergência de SLA de voz (`oServiceLevel` oficial × faixas de `tAnswered` usadas hoje em `negocio-conceitos.md`), registrada em `negocio-perguntas-em-aberto.md`.

## Padrões SQL do time (SQL)

*(vazio)*

## Padrões DAX do time (DAX)

*(vazio)*
