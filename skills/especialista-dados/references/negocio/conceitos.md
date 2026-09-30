# Conceitos de negócio — dicionário (SGD · Postgres · Dataflows)

> Última atualização: 2026-09-29 · Fonte: Maestro (`analytics-bi-dominio-orquestrador`: `modules/_import_sgd/etl/rotinas.py`, `etl/domains/clients_sgd.py`, `requests_sgd.py`, `occurrence.py`, `forecast.py`, `modules/produtividade_pendencia_realtime/sql/queries.sql`, `modules/genesys_sla/sql/queries.sql`, `modules/historic_tb_*/sql/*.sql`), `.dados-sync/maestro.json`, `sql-base/agente` (DICIONARIO_NEGOCIOS.md, MAPEAMENTO_BANCO_DADOS.md, catalogos/*.md), Dataflows em `fontes/dataflows/*.json` (SQL reproduzido em `references/dados/fluxo-*.md`), `references/dados/*.md` · **Arquivo curado** · Status: **Em revisão** (extraído de comentários/código — validar com o time)

**Como ler as citações**
- `orq:` = `C:\GitHub\TR\analytics-bi-dominio-orquestrador\`.
- `sqlbase:` = `C:\GitHub\TR\sql-base\`.
- `legado:<projeto>` = projeto irmão em `C:\GitHub\TR\`.
- `fluxo-X.md:N` = linha N de `dados-fluxo-X.md`, que reproduz o SQL do Dataflow X (a fonte original é `fontes/dataflows/X.json`).
- Trechos entre aspas são **literais**. "(inferido)" marca dedução minha, não escrita no código. "(via extração)" indica citação transcrita por agente de leitura e ainda não conferida linha a linha.
- Cada conceito traz, quando existe: **Definição** · **Códigos** · **Citação** · **Sybase** (view) · **Postgres** (tabela.coluna) · **Dataflow** (entidade) · **⚠️ Divergências**.

---

## 1. Organização: revenda, filial, unidade, UPG, Televendas, regional

### 1.1 Revenda (`i_revendas` / `i_controle` / `i_resale`)
- **Definição:** unidade comercial/de atendimento que "possui" o cliente e o colaborador. Pode ser unidade própria (Filial), parceira (Revenda), a UPG ou unidade interna (testes, Televendas etc.).
- **Chave:** `vw_revendas.i_controle`. No SSC é `ssc.i_revendas`; no usuário é `vw_usuarios.i_revendas`; no Postgres é `i_resale`.
- **Cliente → revenda:** não há FK direta. A ligação é pelo representante: "`geclientes.i_representantes = revendas.i_representantes` … `and revendas.ativa = 1`" (`orq:modules/_import_sgd/etl/domains/clients_sgd.py:116-118`).
- **Catálogo** (121 registros, "inclusive inativas") em `sqlbase:agente/catalogos/REVENDAS_UNIDADES_COMPLETO.md:3-6`. Códigos internos relevantes, literais:
  - "1 | Unidade de Produção e Gestão - UP&G | UPG" (:14)
  - "82 | Suporte a Clientes - Secundários" (:107)
  - "83 | Suporte a Clientes - Regional Sul | Suporte Sul" (:108)
  - "86 | Unidade de produção | UP" (:111)
  - "98 | Suporte a Clientes - Salvador | Suporte BA" (:116)
  - "102 | Suporte a Clientes - Campinas" (:125)
  - "104 | Apoio às Unidades | Apoio" (:127)
  - "112 | UPG - TeleVendas | TeleVendas" (:131)
  - "137 | Suporte a Clientes - Porto Alegre | Suporte RS" (:145)
  - "144 | Suporte a Clientes - Curitiba | Suporte PR" (:154)
  - "148 | Unidade Testes Internos | USI" (:156)
  - "155 | Suporte a Clientes - São Paulo" (:160)
  - "156 | Suporte a Clientes - Criciuma AT | SUP Criciuma - AT" (:161)
  - "157 | Suporte a Clientes - Salvador AT" (:162)
  - "163 | Suporte a Clientes - São Paulo AT | SUP SP - AT" (:171)
  - "165 Domínio Inova" (:173)
- **`ativa`:** assume 0/1/2; o significado de 2 não está documentado (`sqlbase` catálogo). O ETL filtra `ativa = 1`.
- **Sybase:** `bethadba.vw_revendas` (`i_controle`, `apelido`, `ativa`, `i_representantes`).
- **Postgres:** `DB_SGD.public.sgd_resale` (`i_resale`, `apelido`, `active`), recarga total (`clients_sgd.py:182-195`). Cópias legadas: `DB_SGD_N2.public."SGD_resales"`. A cópia do DB_SGD_N1 era "alimentada por codigo MORTO" (`orq:modules/produtividade_pendencia_realtime/sql/queries.sql:63-66`).
- **Dataflow:** `DB_SGD_ALL.sgd_resales` (acrescenta `type_resale`, `regiao_atend`, `agrupado`); `DB_RLS.rls_user`.

### 1.2 Filial × Revenda × UPG (`type_resale` / `tipo`)
- **Definição:** classificação da revenda em **Filiais** (unidades próprias TR/Domínio), **Revendas** (parceiras) e **UPG** (revenda 1).
- **Citação sql-base:** "**Filiais** (Unidades Próprias): **Códigos**: 3, 4, 13, 74, 40, 160"; "**Revendas** (Unidades Parceiras): Todos os demais valores" (`sqlbase:agente/DICIONARIO_NEGOCIOS.md:238-244`). Siglas: 3 UNSC, 4 UNCWB, 13 UNPOA, 40 UNSAO C, 74 UNRIO, 160 UNSAO I (DICIONARIO:253-258). Esta é a visão comercial (ERP/implantação).
- **⚠️ Divergência:** cada ponto do código tem sua própria lista literal de "Filiais".

| Onde | Lista "Filiais" | Tem 18? | Tem 148? | Tem 165? | Revenda 1 |
|---|---|---|---|---|---|
| `sgd_users.type_resale` (`orq:…/clients_sgd.py:408-410`) | 3,4,13,14,40,74,83,102,137,144,155,156,160,163,165 | não | não | **sim** | "UPG" |
| `sgd_client.type_resale` (`clients_sgd.py:95`) | 3,4,13,14,18,40,74,83,102,137,144,148,155,156,160,163 | **sim** | **sim** | não | Revendas |
| Dataflow `DB_SGD_ALL.sgd_resales` (`fluxo-db_sgd_all.md:298`) | 3,4,13,14,18,40,74,83,102,137,144,155,156,160,163 | sim | não | não | Revendas |
| sql-base (visão comercial) | 3,4,13,40,74,160 | — | — | — | UPG |
| Dataflow `DB_WEBCHAT.webchat_tenent` (`fluxo-db_webchat.md:728-731`) | por **tenant**: `633cd75c…` (Suporte) e `6a60bd21…` (Líderes) = Filiais; resto = Revendas | — | — | — | — |

- **Regra adicional:** o Dataflow `sgd_users` força `type_resale = 'BOT-IA'` para `i_user IN (1405244,1444989)` (`fluxo-db_sgd_all.md:1310-1312`).
- **Postgres:**
  - `DB_SGD.public.sgd_users.type_resale`
  - `DB_SGD.public.sgd_client.type_resale`
  - `DB_REPORTS_ANALITICOS.public.tb_colaboradores.tipo_resale` (herda de `sgd_users`)
- **Consumo:** `tb_demanda_lideres` usa `tipo_resale = 'Filiais'` para definir o universo de colaboradores (`orq:modules/historic_tb_interacoes_lideres_plug/sql/demanda.sql:35`). O `DB_LOGMEIN` usa `u.type_resale = 'Filiais'` e `u.i_resale <> 1` (`fluxo-db_logmein.md:32`).

### 1.3 Universo de revendas carregadas pelo ETL (REG_* + `REVENDAS_COM18`)
- **Definição:** conjunto de revendas cujos dados (SSC, clientes, usuários, pendência…) o `import-sgd-*` traz do Sybase. Não é "filial": é **regionais + revendas parceiras atendidas**.
- **Citação:** "Constantes de filtro (regionais/revendas) — LOAD-BEARING. As REGIONAIS continuam divergindo por rotina (REG_RECORD tem o 1, REG_SSC nao). Ja as REVENDAS foram unificadas em 2026-09-09: existe uma lista so (com o 18)." (`orq:modules/_import_sgd/etl/rotinas.py:36-39`)
- **Códigos:**
  - `REVENDAS_COM18` = 5,7,10,11,16,17,18,22,25,31,32,36,41,44,51,57,63,64,67,69,75,76,77,79,81,82,84,85,86,96,97,98,103,104,109,**112**,113,122,123,130,131,134,135,136,140,148,152,154,157,159,161,164 (`rotinas.py:45-46`).
  - `REG_RECORD` = "1,3,4,13,14,18,40,74,83,102,137,144,155,156,160,163,165" — "mainRecord + mainHistoric" (`rotinas.py:49`).
  - `REG_SSC` e `REG_TEMPO` = a mesma lista **sem o 1** (`rotinas.py:50-51`).
- **⚠️ Observação:** a 112 (Televendas) está em `REVENDAS_COM18`, mas as consultas de cliente e contrato a excluem explicitamente (ver 1.5).

### 1.4 Regional / região / unidade de atendimento (Sul, Campinas, AT, CTD…)
- **Definição:** agrupamento geográfico/operacional do suporte. **Não existe coluna mestre**: cada artefato deriva a regional com um CASE próprio.

| Artefato | Regra literal | Citação |
|---|---|---|
| `DB_SGD_ALL.sgd_resales.regiao_atend` | Campinas = 40,102,155,160,163; Sul = **1**,3,4,13,18,74,83,137,**144**,156; "Interno(UPG-USI)" = 1,148 (nunca atingido para o 1, porque o Sul vem antes no CASE); resto = Demais | `fluxo-db_sgd_all.md:299-302` |
| `DB_SGD_ALL.sgd_resales.agrupado` | revenda → grupo comercial: 57 "2B", 76 "Alpha", 4 "UNCWB", 13 "UNPOA", 74 "UNRIO", 40 "UNSAO - Capital", 160 "UNSAO - Interior", 3 "UNSC", 1/148 "Interno(UPG-USI)", etc. | `fluxo-db_sgd_all.md:303-332` |
| `TB_SYBASE_SGD_AGENDA.Agenda.unidade` | 102,**144** = "Regional Campinas"; 83,82,137 = "Regional Sul"; 155 "AT Campinas"; 156 "AT Criciuma"; 163 "AT SP"; 1 "CTD"; resto "Outras" | `fluxo-tb_sybase_sgd_agenda.md:73-81` |
| sql-base (comercial) | "**Região Sul** (SC + PR + RS): `IN (3, 4, 13)`"; "**Região Sudeste** (SP + RJ): `IN (40, 74, 160)`" | `sqlbase:agente/DICIONARIO_NEGOCIOS.md:332-340` |
| `DB_SGD_ALL.sgd_user_manager_historic.unity` | derivada do **nome do gerente** (ver 3.4): CAMPINAS / SUL / CONV-EXP-IMP / REVENDAS / BOT-IA | `fluxo-db_sgd_all.md:1379-1404` |
| Genesys `Skill_Filter` | skill terminada em `CAMP_S` = Campinas; `CRIC_S`/`_SUL_S` = "Regional Sul"; skills com 31/32/41/42/43/51/52/61/62, Conversao ou Performance = AT; `_DS_` = "TR BANK" | `fluxo-db_genesys.md:261-290` |
| WebChat `area_group` | tenant `633cd75c…`: fila Folha% = FOLHA; Contabilidade/Escrita/Fiscont/Fiscal/Reforma% = FISCONT; resto = AT; outro tenant = "Revendas" | `fluxo-db_webchat.md:135-149` |
| `forecast.demanda_projetada.regional`, `genesys.skill.regional` | valores vindos de planilha/cadastro (não derivados no código) | `postgres-db_sgd.md:58,77` |

- **⚠️ Divergências:**
  - a **144 (Curitiba / "Suporte PR")** é Sul no DB_SGD_ALL e "Regional Campinas" na agenda;
  - a **revenda 1** é Sul (DB_SGD_ALL), CTD (agenda) e UPG (`sgd_users`);
  - a **82 (Secundários)** é Regional Sul na agenda e não entra em regional nenhuma no DB_SGD_ALL.
- **Comentário de filtro enganoso:** "`usuarios.i_revendas in(83,102,137,144,155,156,163)/*SP,BA,SUL,Secundarios, POA, curitiba*/`" (`fluxo-tb_sybase_sgd_agenda.md:90`). Não há código BA (98) na lista.

### 1.5 Televendas e exclusões fixas
- **Definição:** a revenda **112** ("UPG - TeleVendas") é excluída de clientes e contratos.
- **Citação:** "`and revendas.i_controle <> 112 /*Televendas*/`" (`orq:…/clients_sgd.py:120` e `:164`).
- **Clientes excluídos:** "`geclientes.i_clientes not in (59827,40580,40581,40579,59879)`" (`clients_sgd.py:121,165,253`). Os Dataflows de WebChat excluem `id_client not IN (40579,96797)` (`fluxo-db_webchat.md:91,153,319,772`).
- **⚠️ Divergência:** 96797 só aparece no WebChat; 59827/40580/40581/59879 só no ETL SGD.
- **Usuário excluído:** `u.i_usuarios not in (1280525)` em `sgd_users` (`clients_sgd.py:418`). O usuário `1078032` é ignorado como "primeiro atendente" (`fluxo-db_sgd_all.md:876`).
- **Correção pontual:** "`DELETE FROM public.sgd_client where i_client = 2998 and i_resale = 86;`" (`clients_sgd.py:135`).

### 1.6 Representante
- **Definição:** `i_representantes` liga cliente/contrato à revenda. No comercial, `i_representantes_vendedor` identifica o vendedor ("Fonte: Tabela `gerepresentantes`", `sqlbase:agente/DICIONARIO_NEGOCIOS.md:485-487`).
- **Unidade do cliente no painel de pendência:** "`unidade = coalesce((select top 1 r.apelido from bethadba.vw_revendas as r WHERE geclientes.i_representantes = r.i_representantes and r.ativa = 1 and r.i_controle > 1),'')`" (`orq:modules/produtividade_pendencia_realtime/sql/queries.sql:145-148`).

---

## 2. Cliente, contrato e produto

### 2.1 Cliente (`i_clientes` / `i_client`)
- **Definição:** empresa (escritório contábil) que tem contrato Domínio e abre SSC.
- **Sybase:** `vw_geclientes` (`razaosocial`, `i_representantes`, `cancelado`, `i_responsavel_csm`, `i_gestor_csm`), `vw_gecidades`, `vw_geestados`, `vw_geclientes_observacoes`, `vw_geclientes_contatos_adicionais`.
- **Postgres:** `DB_SGD.public.sgd_client`. Colunas e regras:
  - `situation`: "`(case when geclientes.cancelado = 1 then 1 else 0 end )`" (`clients_sgd.py:96`); 1 = cancelado.
  - `date_register`: 1ª inclusão de contrato dos produtos 101,102,103,104,170,174,190; se não houver, qualquer contrato (`clients_sgd.py:69-83`).
  - `date_inactivation`: fim de prestação do último contrato com valor dos produtos 101-104,110,170 (`clients_sgd.py:97-104`).
  - `date_signature`: assinatura do contrato dos produtos 101-104,107,110,170,174,190 (`clients_sgd.py:105-111`).
  - `referential`: 'Sim' se `geclientes_observacoes.referencial = 1` (`clients_sgd.py:84-87`).
  - `i_cms_responsible`/`i_cms_manager` = CSM responsável/gestor.
- **Dataflow:** `DB_SGD_ALL.sgd_client`:
  - anula `date_inactivation` quando `situation = 0`;
  - junta a observação;
  - `exist_web_chat = 1` se o cliente tem protocolo no WebChat, via **dblink** ao DB_WEBCHAT (`fluxo-db_sgd_all.md:167-201`).
- **Cliente em implantação/comercial:** "Use `geclientes` quando partir do **ERP**. Use `view_geclientes` quando partir do **SGD**" (`sqlbase:agente/DICIONARIO_NEGOCIOS.md:82-84`).

### 2.2 Contrato (`i_contratos` / `i_contract`)
- **Definição:** contrato de um produto para um cliente (`vw_cmcontratos`).
- **Citação:** "`cmcontratos` - SEMPRE usar"; `situacao` "**0** - Ativo / outros - Inativo" (`sqlbase:agente/DICIONARIO_NEGOCIOS.md:854-855, 894-897`). "**NÃO** usar `situacao = 0` em análises históricas" (DICIONARIO:1041-1056).
- **Postgres:** `DB_SGD.public.sgd_product_client`: 1 linha por contrato (`i_contract`, `i_product`, `i_client`, datas, `situ_contract`), recarga total (`clients_sgd.py:143-175`).
- **Dataflow:** `DB_SGD_ALL.sgd_client_product.situacao` = "`CASE WHEN situ_contract = 1 THEN 'Inativo' else 'Ativo'`" (`fluxo-db_sgd_all.md:233`).
- **⚠️ Divergência de semântica:** no sql-base, 0 = ativo e **qualquer outro valor** = inativo. No Dataflow, **só 1** = inativo e o resto (inclusive 2, 3…) = ativo.
- **Histórico de usuários do contrato:** `forecast.client_user_history` (ACUMULA; ver `linhagem-por-conceito.md`).

### 2.3 Produto (`i_produtos` / `i_product`) — principais × demais
- **Produtos principais (sql-base):** "**Códigos**: 101, 102, 103, 104, 170, 211, 212, 213" (`sqlbase:agente/DICIONARIO_NEGOCIOS.md:495`).
  - Nomes: 101 Plus, 102 Start, 103 Personalizado, 104 Empresarial, 170 Premium, 211 One, 212 Pro, "**213** - Domínio Max (**este é o produto MAX**…)" (DICIONARIO:498-505).
  - "Pedido "MAX" → `i_produtos = 213`. Não é 101 (Plus) nem 211 (One)." (DICIONARIO:508)
- **Mesma lista no forecast:** "`produtos = '101,102,103,104,170,211,212,213'`" em "Buscar alterações de usuários Clientes" (`orq:modules/_import_sgd/etl/domains/forecast.py:404-406`).
- **Demais produtos (periféricos):** "**Todos os demais códigos são periféricos**" (DICIONARIO:519). Principais periféricos: 145 Domínio WEB 2.0 ("DW"), 173 Messenger, 174 Processos, 175 Kolossus Auditor, 221 Contabilidade Digital, 222 Benefícios (DICIONARIO:522-527). 220 Conta Digital ≠ 221 Contabilidade Digital (`sqlbase:agente/CATALOGO_PRODUTOS_TREINAMENTOS.md:53`).
- **⚠️ Divergências — listas "de produto" no ETL do cliente** (nenhuma inclui 211/212/213):

| Uso | Lista | Citação |
|---|---|---|
| data de cadastro | 101,102,103,104,170,174,190 | `clients_sgd.py:74` |
| fim de contrato (inativação) | 101,102,103,104,110,170 | `clients_sgd.py:98,102` |
| data de assinatura | 101,102,103,104,**107**,110,170,174,190 | `clients_sgd.py:109` |
| fallback antigo (comentado) | 220 | `clients_sgd.py:65` |
| forecast (atual) | 101,102,103,104,170,211,212,213 | `forecast.py:406` |
| forecast (versão comentada) | 101,102,103,104,170 | `forecast.py:542-573` |

  Aliases legados errados (101 = MAX, 102 = PRO, 103 = ONE, 104 = PREMIUM): "SS-1138498 comentou 211=MAX — **errado**" (`sqlbase:agente/CATALOGO_PRODUTOS_TREINAMENTOS.md:48-50`).
- **Cadastro de produtos:** `vw_ceprodutos`, filtro "`where ( permite_neg = 'S' or i_produtos = 221)`" (`forecast.py:677-679`) → `DB_SGD.public.sgd_product` → `DB_SGD_ALL.sgd_product`.
- **Regra de implantação:** "`gera_implantacao = Sim` identifica produtos que atualmente geram processo de implantação" (`sqlbase:agente/catalogos/PRODUTOS_COMPLETO.md:6`).

---

## 3. Pessoas: usuário, colaborador, alocação, cargo, hierarquia

### 3.1 Usuário interno × cliente × terceiro
- **Sybase:** `power_bi.vw_usuarios` (`i_usuarios`, `terceiro` bit, `i_revendas`, `ativo` bit, `i_clientes`, `cadastro`) (`references/dados/sybase-colunas.md:290`).
- **Usuário de cliente:** `i_clientes` preenchido → `DB_SGD.public.sgd_user_client`. Filtro: "`and not u.i_clientes is null and u.terceiro = 0`" (`clients_sgd.py:250-253`).
- **Colaborador interno (ETL):** `i_clientes is null`, usado em alocação/cargo/horário (`clients_sgd.py:359,506,565`). O `sgd_users` filtra "`u.terceiro = 0 … and admissao is not NULL`" (`clients_sgd.py:415-416`).
- **Terceiro:** `terceiro = 1` (flag do SGD). No sql-base, interno "exclui i_clientes e i_representantes_vendedor" (`sqlbase:padronizados/referencia_ajustados/atendimento_listar_usuarios_ativos_do_departamento_32_SS1136735.sql:28,116-118`). O usuário com `i_representantes_vendedor` preenchido seria o "terceiro" representante (inferido).

### 3.2 Colaborador ativo (em uma data)
- **Definição (ETL diário por dia):** para cada dia D, um usuário interno entra se:
  - `cadastro <= D`;
  - pertence ao universo de revendas;
  - **não** existe registro de auditoria, sendo o último até D, com `ativo <> 0`.
- **Citação:** "`and not exists(select 1 from bethadba.vw_usuarios_auditoria … where … and not usuarios_auditoria.ativo = 0 and usuarios_auditoria.i_usuarios_auditoria = (select max(au.i_usuarios_auditoria) … where convert(date,au.entrada,103) <=dDate …))`" (`clients_sgd.py:555-562`; idem em `:349-356` e `:496-503`).
- **⚠️ Semântica invertida (?):** lida literalmente, a regra **exclui** quem tem o último registro de auditoria "ativo". Ver pergunta P-07 em `perguntas-em-aberto.md`.
- **Inativação em `sgd_users`:** `date_inactivation` = maior `entrada` de auditoria com `ativo = 1` sem registro posterior com `ativo = 0/null`; `dismission` = '1' se houver inativação (`clients_sgd.py:395-404`).
- **Na tabela diária `tb_colaboradores`:** ativo no dia D ⇔ `data_admissao <= D <= data_inativacao`. Citação: "`delete from temp_base_cadastro where data < data_admissao; delete … where data > data_inativacao;`" (`orq:modules/historic_tb_colaboradores/sql/queries.sql:279-283`). `demissao = 1` só no próprio dia da inativação (`:285-288`).
- **⚠️ Duplicidade conhecida:** "o nosso `historic-tb-colaboradores` **duplica** — 24.796 pares `(data, id_usuario_sgd)`, **71 usuários/dia**" (`orq:CLAUDE.md:890-892`). Consumidores já usam DISTINCT: "tb_colaboradores com DISTINCT (cópias idênticas no mesmo dia)" (`demanda.sql:11`).
- **Genesys:** agente ativo = `status = 'active' AND role_genesys = 'Agent'` (`orq:modules/genesys_status_agents_realtime/sql/queries.sql:18`); no `genesys-sla`, `users_SGD.demissao = '0'` (`orq:modules/genesys_sla/sql/queries.sql:21`).
- **RLS:** considera ativo quem tem `dismission = '0' and "user" <> ''` (`fluxo-db_rls.md:33-34`).
- **Agenda tempo real:** "`usuarios.ativo = 1 /*Apenas usuários ativos*/`" (`fluxo-tb_sybase_sgd_agenda.md:104`).
- **sql-base:** "não existe uma definição única"; um critério usa `ultimo_login >= '2025-11-01'` (SS1136735.sql:110-114).

### 3.3 Alocação / área / equipe / setor
- **Definição:** equipe operacional do colaborador numa data (vigência por `apartir_de`). O código de alocação é mapeado para área/setor por CASE ou pela planilha de-para.
- **Sybase:** `vw_alocacao` (`i_alocacao`, `descricao`, `abreviatura`, `area`); `vw_usuarios_alocacao_historico` (`i_usuarios`, `i_historico`, `apartir_de`, `i_alocacao_nova`).
- **Regra de vigência (ETL):** para cada dia, `max(i_alocacao_nova)` do histórico `TOP 1 … where apartir_de <= dDate order by apartir_de desc` (`clients_sgd.py:535-542`).
- **Mapa alocação → setor (agenda tempo real), literal** (`fluxo-tb_sybase_sgd_agenda.md:51-72`):

| `i_alocacao` | Setor |
|---|---|
| 2, 3, 4, 11, 29, 30 | Técnica |
| 36 | Suporte Interno Técnico - Performance |
| 8, 10 | Apoio |
| 13, 60 | M.Aprendiz/Estagiário |
| 25, 26, 37, 38, 39 | Folha |
| 27, 28 | "Fical/Contábil" (sic) |
| 31 | AT - Imp/Exp/Imp |
| 32 | Treinamento |
| 34 | Em formação - Monitorado |
| 40, 41, 42 | Secundários |
| 43, 44 | Suporte DW |
| 52, 53, 54, 55 | Folha/Contábil |
| 48, 68, 69, 70 | Chat |
| 71 / 72 / 73 | Folha/AT Fone · Contábil/AT Fone · Folha/Contábil/AT Fone |
| 74 / 75 / 76 | Folha/AT Web · Contábil/AT Web · Folha/Contábil/AT Web |
| demais | Outros |

- **⚠️ Outro mapa, do legado `productivity-pendency-realtime`** (`legado:analytics-bi-dominio-productivity-pendency-realtime/sgd_productivity.py:22-73`, via extração), que diverge:
  - 'Técnica' = 2,3,4,68,17,29,30,31,36,40,41,42
  - 'Coordenação' = 11
  - 'Folha' = 25,26,37,38,39,52,54,70,71,73,74
  - 'Fical/Contábil' = 27,28,15,16,69,72,75,77
  - 32 'Treinamento'
  - **33 'Ausente'**
  - 34 'Formação Monitorado'
  - 8 'Apoio'
  - 48 'Atendimento - Chat'
  - 56,57 'TR Digital Banking'
  - 55,53,76 'Híbrido'
  - 78-83 'Apoio Chat/Web Folha/FisCont/AT'
  - 84 'Contábil/Folha/AT Fone'
  
  Exemplos de conflito: 31, 36, 40-42 são "Técnica" aqui, mas AT/Performance/Secundários na agenda; 11 é "Coordenação" aqui e "Técnica" na agenda. O mesmo legado define unidade por revenda: 102/155/163 'São Paulo'; 83/82/156 'Criciúma'; 137 'Porto Alegre'; 144 'Curitiba' (`sgd_productivity.py:75-85`).
- **Alocação 33:** no legado acima, 33 = **'Ausente'**. Isso explica a regra da agenda: "`on alocacao.i_alocacao = if usuarios_alocacao_historico.i_alocacao_nova = 33 then alocaco_anterior else usuarios_alocacao_historico.i_alocacao_nova end if`" (`fluxo-tb_sybase_sgd_agenda.md:98-100`). Ou seja, quando o colaborador está "Ausente" (33), a agenda usa a **alocação anterior**. Só a agenda aplica essa regra; o ETL diário (`sgd_alocation_historic`) grava o 33 como está (inferido pela leitura de `clients_sgd.py:535-542`).
- **Alocação 999:** convenção dos Dataflows para "sem alocação no dia" (`coalesce(h.i_alocation,999)`). Cadastro sintético: "`select 999,'.Sem Alocação','Sem Alocação','SEM ÁREA', 'SEM MEIO DE ACESSO'`" (`fluxo-db_sgd_all.md:104`).
- **Área / meio de acesso por alocação (planilha):** `forecast.de_para_alocacao` (aba "DeParaAreaAlocacao", `maestro.json` nota de `forecast.insertForecastDeParaAlocation`):
  - `area = '0'` vira 'DEMAIS ÁREAS' (em `sgd_alocation_reg`) ou 'NÃO RELACIONADO' (em `forecast_de_para_alocacao_area`) (`fluxo-db_sgd_all.md:98,1720`);
  - `meio_acesso_alocacao = '0'` vira 'SEM MEIO DE ACESSO' (`:99`).
- **⚠️ Divergência:** a mesma área "0" recebe dois rótulos diferentes em duas entidades do mesmo Dataflow.
- **Postgres:**
  - `DB_SGD.public.sgd_alocation_historic` (`date`, `i_user`, `i_alocation`, `from_of`): 1 linha por usuário × dia.
  - `sgd_alocation_reg`: cadastro.
  - Cópias em `DB_GENESYS.public.sgd_alocations` (com `id_user_genesys`) e `cad_alocations` (`clients_sgd.py:583-605`).
  - `tb_colaboradores.i_alocation/descricao/abreviacao`.
- **FisCont / Folha / AT** como **área de demanda:** colunas `calendar.fone_folha_seq_deman`, `fone_fiscont_seq_deman`, `fone_at_seq_deman`, `chat_*` (`postgres-db_sgd.md:87`); `goals.meta_at`, `meta_folha`, `meta_fiscont` (`:91`); `forecast.coefficient` (`calls_folha`, `calls_fiscont`, `calls_at`…) (`:52`).
- **N1 / N2** como nível de atendimento: ver 5.1. Não é código de alocação.
- **sql-base:** "Os códigos e descrições da tabela `alocacao` não estão documentados" (resultado da extração de `sqlbase:agente`).

### 3.4 Gestor / coordenador (supervisor) / gerente
- **Hierarquia:** "Gerente ↓ Coordenador ↓ Técnico" (`sqlbase:agente/DICIONARIO_NEGOCIOS.md:396-401`).
- **Função Sybase:** "`coordenador … where coordenador.i_usuarios = bethadba.f_get_gestor_suporte(usuarios.i_usuarios)`"; o gerente é o gestor do gestor: "`bethadba.f_get_gestor_suporte(bethadba.f_get_gestor_suporte(usuarios.i_usuarios))`" (`fluxo-tb_sybase_sgd_agenda.md:36-41`). Mesmo uso no painel de pendência (`orq:…/produtividade_pendencia_realtime/sql/queries.sql:131`).
- **Histórico diário:** `vw_usuarios_gestor_historico` → `DB_SGD.public.sgd_user_manager_historic` (`i_superv`, `superv`, `manager`), janela de 365 dias (`clients_sgd.py:639-719`).
- **⚠️ Regra frágil — unidade derivada do nome do gerente:** o Dataflow `DB_SGD_ALL.sgd_user_manager_historic` normaliza nomes ("Thiago Candelaria Birck (SP)" → "Thiago Candelaria Birck", "Adas Pavei Fontana (Sup SC)" → "Everton Batisti"…) e calcula `unity` pelo nome (`fluxo-db_sgd_all.md:1352-1404`):
  - CAMPINAS: Thiago/Marina
  - SUL: Eloiza
  - CONV-EXP-IMP: "Adas… (Sup SC)" e "Everton… (Int)"
  - REVENDAS: "Everton… (Upg)" e o default
  - BOT-IA: "Camila Becker Meller (CT)"
  
  O mesmo padrão aparece:
  - no `DB_LOGMEIN`: `manager ~* '^(marina|eloiza|thiago|everton)'` (`fluxo-db_logmein.md:91-103`);
  - no filtro de gerentes da agenda tempo real (`fluxo-tb_sybase_sgd_agenda.md:105-108`);
  - na 2ª parte da agenda, que fixa `Gerente = 'Camila Meller'` para o Centro de Treinamento (`:130-131`).
  
  Troca de gerente ou de grafia quebra os relatórios (inferido).
- **Em `tb_colaboradores`:** `supervisor` = coordenador; `gerente` (`orq:modules/historic_tb_colaboradores/sql/queries.sql:315-317`). Em `tb_demanda_lideres`: "`a.supervisor AS coordenador`" (`demanda.sql:236`).
- **Genesys:** `users_Genesys.supervisor/gerente/lider/lider_area` (cadastro da Genesys, `postgres-db_genesys.md:100-101`).
  - A hierarquia é montada por BFS a partir do diretor: "`_PROFUNDIDADE_MAX = 3  # diretor=0; gerente=1; coordenador=2; agente=3`" (`orq:modules/genesys_import/users.py:33`).
  - `lider`/`lider_area` são reaplicados a partir de variáveis de configuração por área (`users.py:221-229`).
- **⚠️ Duas hierarquias independentes:** SGD (`f_get_gestor_suporte` / `vw_usuarios_gestor_historico`) × Genesys (organograma a partir do diretor). Podem divergir.

### 3.5 Cargo
- **Sybase:** `vw_cargos` (`i_cargos`, `descricao`, `meta_produtividade` bit, `ativo`); `vw_usuarios_cargo_historico` (`apartir_de`).
- **Postgres:**
  - `DB_SGD.public.sgd_cargos`: recarga total (`clients_sgd.py:437-461`).
  - `sgd_user_cargo_historico`: 1 linha por usuário × dia **desde 2024-01-01** (data fixa), recarga total (`clients_sgd.py:464-517`).
  - `tb_colaboradores.id_cargo/descricao_cargo`.
- **Uso em meta:** `tb_meta_capacidade_atendimento` (cargo × setor × acesso × faixa de tempo de casa → `meta_maxima_atendimento`), juntada em `tb_demanda_lideres` por "`e.cargo = a.descricao_cargo AND a.tempo_casa_meses >= e.tempo_casa_min_meses AND … <= e.tempo_casa_max_meses AND e.descricao_meta = a.descricao`" (`demanda.sql:250-253`). `descricao_meta` = "`concat(initcap(setor), ' ', initcap(acesso))`" (`demanda.sql:45`).

### 3.6 Horário de trabalho / jornada
- `vw_usuarios_horario_trabalho_historico` → `DB_SGD.public.sgd_horario_historic`: 1 linha por usuário × dia com horários matutino/vespertino vigentes (`clients_sgd.py:321-372`).
- **⚠️** "`and dDate >='2026-08-01'`" é data fixa no SQL (`clients_sgd.py:360`), desalinhada da janela.
- **Jornada padrão nos Dataflows:** 480 min/dia com almoço 12:00-13:30 descontado (`fluxo-db_sgd_all.md:1105-1144`). "Dias trabalhados" em `tb_demanda_lideres` = "(minutos do motivo 0 - minutos dos demais motivos) / 480" (`demanda.sql:66-72`).

---

## 4. Atendimento: SSC, SS, SSQL, conversão, SR, SA/NE, SOSE, trâmite

### 4.1 SSC — Solicitação de Suporte do Cliente (N1)
- **Definição:** chamado aberto pelo cliente. "Solicitação de Suporte ao Cliente" (`sqlbase:padronizados/bis/ss_index.md:39`). Há outro arquivo que diz "Sistema de Suporte ao Cliente" (`bis_perifericos_ongoing_ssc.sql:2`).
- **Número visível:** `Code_SSC = ssc.seq_revenda` (`orq:…/requests_sgd.py:230`). `i_ssc` é a chave técnica.
- **Sybase:** `vw_ssc`, `vw_ssc_tramites`, `vw_ssc_situacoes`, `vw_ssc_origens` (subtópico), `vw_topicos_suportes`, `vw_sistemas`, `vw_modulos`.
- **Postgres:** `DB_SGD.public.sgd_ssc`: 1 linha por SSC, com os tempos já calculados no Sybase via `minutosuteis`:
  - `time_before_first_analysis`, `time_total`, `time_medium`, `time_ss`, `time_ssql`, `time_scd`, `time_phone`, `time_final_support`, `time_final_client`…
  - Carregada por `requests_sgd.sgdSearchRequests` (`requests_sgd.py:221-568`).
- **Dataflow:** `DB_SGD_ALL.sgd_ssc` (a partir de `2024-01-01`):
  - `i_alocation` do responsável no dia de entrada;
  - `first_user` = 1º trâmite em situações (2,3,5,14,38) de usuário ≠ 1078032;
  - `disregarddissatisfaction`;
  - `i_resales` do cliente (`fluxo-db_sgd_all.md:855-879`).
- **Entrada "no setor" / Web:** o Dataflow usa `COALESCE(st.i_ssc_situation, r.i_means_of_access) AS aux_i_Means_of_Access` com trâmite em situação 1 (`fluxo-db_sgd_all.md:858,868`). `tb_demanda_lideres.total_ssc` conta SSC com "`a.i_means_of_access = 1 OR EXISTS (… b.i_ssc_situation = 1)`" e comenta "SSC via Web" (`demanda.sql:79-91`).

### 4.2 SS — Solicitação de Serviço (N2)
- **Definição:** demanda interna para o N2 (desenvolvimento, GP, TI…), vinculada a SSC por `ssc.i_ss` ou `vw_ssc_ss`. A lista de SS da SSC é `ListaSSs` (`requests_sgd.py:240-246`).
- **⚠️ Nome:** o sql-base usa "SS (Solicitação de Suporte)" (resultado da extração de `sqlbase:padronizados/bis/bis_onepage_sgd_ss.sql`), enquanto a skill (`glossario.md`) diz "Solicitação de serviço".
- **Sybase:** `vw_ss` (`situacao`, `i_sistemas`), `vw_ss_tramites`, `vw_ss_situacoes`, `vw_ss_categorias`.
- **Postgres:** `DB_SGD_N2.ss.ss`, `ss.ss_tramites` (`sla_interacao`, `sla_n3`, `sla_tme`, `exists_requestsql`, `i_category`), `ss.ss_situation` (`pending`), `ss.ss_tramites_time` (minutos úteis por trâmite).
- **Situações de SS por área (painel tempo real)**, literal (`orq:…/produtividade_pendencia_realtime/sql/queries.sql:444-449`):
  - `(8,11,12,26,27)` 'DV'
  - `(6,10,29)` 'GP'
  - `(23,24,25)` 'TI'
  - `(16,17)` 'COORD'
  - `(31,32)` 'PAR'
  - `(1,2,4,7,9,15,18,25,28,33)` 'N2'
- **⚠️ Divergências:**
  - o 25 está em TI **e** em N2 (TI vence por ordem);
  - `sgd-regras-e-joins.md` lista TI = 23,24 e DV INT = 26,27.
- **⚠️ Três mapeamentos de situação de SS → pendência** (todos literais):

| Fonte | DV | DV INT | GP | TI | PAR | COORD | N1 | N2 |
|---|---|---|---|---|---|---|---|---|
| cadastro `ss.ss_situation.pending` (`orq:modules/_import_sgd/etl/domains/ss_n2.py:293-300`) | 8,12,11,26,27 | — | 6,10,29 | 23,24 | 31,32 | — | — (vazio) | 1,2,4,7,9,15,16,17,18,25,28,30,33 |
| snapshot `ss.ss_pendency` (`ss_n2.py:538-546`) | 8,11,12 | 26,27 | 6,10,29 | 23,24 | 31,32 | — | 3,5,13,14,20,21 | demais |
| painel tempo real (`produtividade_pendencia_realtime/sql/queries.sql:444-449`) | 8,11,12,26,27 | — | 6,10,29 | 23,24,25 | 31,32 | 16,17 | demais | 1,2,4,7,9,15,18,25,28,33 |

  A SS entra no snapshot "`1 as i_situation, 'Sem Análise' …, 'N2' as pending`" no dia da entrada (`ss_n2.py:491-493`). Corte "18:00:59" e `day_of_week not in (1,7)` (`ss_n2.py:496-497`).
- **Pendência "N2"** no Postgres: `ss.ss_situation.pending` = 'N2' (usado por `sgd_ss_pendency_time`, `fluxo-db_sgd_all.md:719-755`).
- `exists_requestsql` = trâmite de SS em situação 15 com descrição `'%requestsql%'` (`ss_n2.py:326-348`, via extração).
- **Encaminhamento:** `DB_SGD_ALL.sgd_ss_forwarding` = 1º trâmite em situações (8,23,27,31) e, separadamente, (6) (`fluxo-db_sgd_all.md:590-636`). Interpretação: entrada em DV/TI/DV-INT/PAR e em GP (inferido pela tabela acima).

### 4.3 SSQL, Conversão (SCD), SR
- **Definição:** demandas vinculadas à SSC que consomem "tempo de terceiros":
  - SSQL: solicitação de SQL/ajuste de base (inferido pelo nome);
  - Conversão: conversão de dados, sigla SCD nos tempos;
  - SR: sigla não definida no código lido.
- **⚠️ Possível bug (inferido):** no ramo ELSE do `TEMPO_SCD`, "`WHERE SSC_CONVERSOES.I_CONVERSOES = SSC.I_SSC`" (`requests_sgd.py:451,460`) compara o id da conversão com o id da SSC; nos ramos de SS/SSQL a comparação é `…I_SSC = SSC.I_SSC`.
- **Citação (tempos):** `TEMPO_SSQL` soma `minutosuteis` de `vw_ssql`/`vw_ssql_tramites` (situação 5 → 4/9) (`requests_sgd.py:392-426`); `TEMPO_SCD` usa `vw_conversoes`/`vw_conversao_tramites` (`:427-461`).
- **Postgres:** `sgd_ssc.time_ssql`, `time_scd`; `sgd_ssc_answer_time.timessql/timeconversao/timesr`; `sgd_pendency.i_ssql/i_sr/i_conversoes`.
- **Classificação 4 = "Conversão"** (ver 4.6).
- **sql-base:** três sentidos de "conversão" (questionário, SS de conversão, Exp/Imp) (resultado da extração de `sqlbase:agente/DICIONARIO_NEGOCIOS.md:1429-1432, 1662-1690` e `CLAUDE.md:154`).

### 4.4 SA / NE (fórum, banco `sgsai`)
- **Definição:** "SA: Solicitação de Alteração / NE: Nova Especificação" (`sqlbase:padronizados/bis/bis_onepage_sgd_ssc.sql:32-33`).
- **⚠️ Divergência de nome:** a skill (`glossario.md`) diz "Sugestão de alteração / necessidade".
- **Tipo no Dataflow:** "`when reason = 0 then 'NE' when reason = 1 then 'SA' when reason = 2 then 'SAL' when reason = 3 then 'SAIL'`" (`fluxo-db_sgd_all.md:1542-1547`).
- **⚠️ Divergência:** o sql-base usa `forum_sa.motivo` 1 = 'SAM', 2 = 'SAL', 3 = 'SAIL' e `tipo_sa` 1 = 'SA', senão 'NE'.
- **Vínculo SSC ↔ SA/NE:** trâmites em situações (9,11,12,15,16,37) com `i_forum_sa` (`requests_sgd.py:462-467`); reprovação = situação 11 (`:468-472`); "SSC desanexada da SA/Ne" no texto do trâmite (`:485`).
- **Postgres:** `sgd_sa`, `sgd_ssc_sa`, `sgd_sai_sane`, `sgd_sa_*`; `sgd_ssc.bond_sa_ne`, `disapproval`, `time_bond_sa_ne`.

### 4.5 SOSE
- **Definição:** serviço prestado/cobrado vinculado à SSC. O faturamento está em `vw_ssc_dados_faturamentos` e as situações em `vw_soses_situacoes`. O sql-base só registra SOSE como descrição de produto ("Servicos Prestados Cfe.Sose", `sqlbase:agente/catalogos/PRODUTOS_COMPLETO.md:57`). A definição é inferida.
- **Meio de acesso 5 = SOSE** (`dados-sgd-regras-e-joins.md`).
- **Postgres:** `DB_SGD.public.sgd_soses`: 1 linha por SSC com SOSE (`tipo_servico`, `valor_total`, `parcelas`, `situacao`…), recarga total. Corte fixo a partir de 2022-01-01 (`sgd-regras-e-joins.md` §Janelas).
- **Dataflow:** `DB_SGD_ALL.sgd_ssc_soses`.

### 4.6 Classificação da SSC (`i_sss_classificacoes`)
- **Literal (painel tempo real)** (`orq:…/produtividade_pendencia_realtime/sql/queries.sql:112-123`):

| Código | Classificação |
|---|---|
| 1 | TÉCNICA |
| 4 | CONVERSÃO |
| 9 | SECUNDARIOS |
| 10 | FUNCIONAL |
| 11 | RELATÓRIO |
| 12 | DOMÍNIO WEB |
| 13 | PERFORMANCE |
| 17 | ÁREA TÉCNICA - TR DIGITAL BANKING |
| 18 | FUNCIONAL - TR DIGITAL BANKING |
| **19** | **ATEND-EXTERNO** |
| outros | SEM CLASSIFICAÇÃO |

- A classificação 19 (atendimento externo) não constava de `sgd-regras-e-joins.md`. O sql-base usa `i_sss_classificacoes = 19` para "SSC em aberto / pendentes" de atendimento externo (resultado da extração de `bis_onepage_etl_ssc_pendentes.sql:18-21`).
- **Postgres:** `sgd_ssc.i_classification`; cadastro `sgd_ssc_classification` (coluna `desription`, sic).

### 4.7 Situação da SSC (`i_ssc_situacoes`) — códigos usados no ETL (comentários literais)
- "`in (3,19) /*aguardando resposta em negociação*/`" (`requests_sgd.py:342`)
- "`IN (5,10,13,17,37,38,43) /*concluido*/`" (`:518`)
- "`in(5,10,13,17,19,37,38,43) /*concluidas, prescrita*/`" (`:522`)
- "`IN(1,7,9) /* 7 - Respondido Interna */`" e "`/*1-SEM ANALISE, 9-PENDENTE DOMINIO SISTEMAS */`" (`:730,745`)
- "`IN(6) /*6-AGUARDANDO RESPOSTA INTERNA*/`" (`:764`)
- Situação 4 é usada como marco "devolvido ao técnico" no tempo pendente (`:354`) (inferido).
- **⚠️ Observação:** o 19 aparece ao mesmo tempo em "aguardando resposta" e em "concluídas, prescrita".
- **Descrição oficial:** `vw_ssc_situacoes.descricao` → `DB_SGD.public.sgd_ssc_situation` (recarga total). Use a descrição do cadastro, não a lista acima.

### 4.8 Trâmite
- **Definição:** cada movimentação do chamado (mudança de situação/resposta).
- SSC: `vw_ssc_tramites` → `DB_SGD.public.sgd_ssc_tramites` (`entry`, `i_ssc_situation`, `i_user`, `tipo_resposta`, `i_visualizado`…), janela de 3 dias. Último trâmite = `MAX(i_ssc_tramites)`.
- SS: `vw_ss_tramites` → `DB_SGD_N2.ss.ss_tramites`.
- Ocorrência: `vw_ocorrencia_tramite` → `sgd_ocorrencia_tramite`.
- **Contagens na SSC:** `total_procedures` (todos) e `total_procedures_waiting_answer` (situações 3,19) (`requests_sgd.py:339-345`).

### 4.9 Meio de acesso / retorno (`i_meios_acesso`)
- Cadastro `vw_meios_acesso` (e `vw_meios_retorno`). No Dataflow é uma tabela fixa (`DB_SGD_ALL.sgd_ssc_means_access`, JSON embutido). Códigos em `sgd-regras-e-joins.md` §Meios de acesso (1 Web, 2 Telefone, 3 Fax, 4 e-Mail, 5 SOSE, 6 Chat, 9 Ligações, 10 Chat-Plug).
- `time_phone` só é calculado para "`ssc.i_meios_acesso = 2`" (`requests_sgd.py:501`).
- O WebChat marca o protocolo como meio 10: "`10 AS i_meansOfAcess`" (`fluxo-db_webchat.md:250`).

---

## 5. Pendência, tempo e SLA

### 5.1 Pendência N1 / N2 / setor
- **⚠️ Duas regras diferentes no código hoje:**
  - **ETL batch (`sgd_pendency`)**, literal: "`n1_pendency = if ssc.situacao_pendente_nivel_um <> 0 and ssc.situacao_pendente_nivel_dois <> 1 then 1 else 0`", "`n2_pendency = if ssc.situacao_pendente_nivel_dois <> 0 then 1 else 0`", "`sector_pendency = if ssc.i_ssc_situacoes = 1 then 1`". Pertinência: "`(situacao_pendente_nivel_um = 1 OR situacao_pendente_nivel_dois = 1)`" (`orq:…/requests_sgd.py:1150-1153, 1210`).
  - **Tempo real (push `_sgdPendency`)**, alinhado ao SGSC: "Antes o flag N1 era `nivel_um<>0 AND nivel_dois<>1` (exclui N2, errado) … Agora, igual ao SGSC: N1 pendente = (situacao_pendente_geral=1 OU responsavel_um=0 OU responsavel_dois=0) E situacao_pendente_nivel_um=1; N2 pendente = situacao_pendente_nivel_dois=1 (independente do N1)" (`orq:modules/produtividade_pendencia_realtime/sql/queries.sql:67-74`; código em `:104-108`).
  
  O batch ainda usa a regra que o próprio time documentou como **errada**. Ver P-01.
- **Pendência de setor:** situação 1 = "Sem análise" (entrada no setor).
- **Postgres:** `DB_SGD.public.sgd_pendency`: **1 linha por SSC pendente × dia (snapshot D-1)**, ACUMULA. Cópias consolidadas: `DB_REPORTS_CONSOLIDADOS.public.pendencias_suporte` (`pendente_n1/n2/n3`), sem job conhecido.
- **Dias de pendência** (`requests_sgd.py:1233-1304`):
  - `pendency_days` = `COUNT(cal.day_useful_month)` entre `entry` e `date`. Como `COUNT(col)` ignora nulos, na prática conta **dias úteis** (inferido).
  - `useful_pendency_days_n1/n2` = nº de dias-snapshot (úteis) em que a SSC estava pendente N1/N2.
- **Dataflow:** `DB_SGD_ALL.sgd_ssc_pendency`; SS: `sgd_ss_pendency` (a partir de 2023-01-01), `sgd_ss_pendency_time`.

### 5.2 Tempo útil / minutos úteis / dias úteis / calendário
- **Sybase:** `bethadba.minutosuteis(1, ini, fim)`. O parâmetro 1 é provavelmente o calendário/jornada (inferido pelo sql-base). Usado em todos os tempos da SSC, SS e ocorrência.
- **Python:** `minutos_uteis.geral()` recalcula no Postgres o tempo de trâmite de ocorrência/SS: "O tempo util e calculado por minutos_uteis.geral()" (`orq:…/occurrence.py:6`).
  - Horário útil: manhã 8h-12h e tarde 13h30-18h; dia útil = seg-sex fora dos feriados de `public.calendar WHERE holiday <> ''` (`orq:modules/_import_sgd/etl/minutos_uteis.py:15-33`, via extração).
  - **TODO literal:** "a fonte so tem 24/12 e 31/12 de 2024 e 2025 — NADA para 2026+. O calculo de minutos uteis dessas vesperas ja esta errado em 2026. … o ideal e cadastrar na public.calendar, que ja e a fonte oficial de feriados." (`minutos_uteis.py:80-83`)
  - O legado realtime calcula **sem feriados** (`legado:analytics-bi-dominio-productivity-pendency-realtime/minutosUteis.py:15-16`).
- **Calendário:** `DB_SGD.public.calendar` (`day_useful_month` nulo = não útil (inferido); `holiday`; `ten` = dezena do mês; sequências de demanda por canal/área). "Nada no Maestro a escreve — é mantida por fora" (`orq:modules/import_agendas/skills.md:55`, via extração). Cópias: `DB_SGD_N2.ss.calendar`, `public."dCalendar"`.
- **Feriados:** `vw_feriados` (Sybase), usada nas agendas.
- **Dias úteis da agenda:** `sgd_schedule_three_days` começa no dia calculado por "`public.calendar com OFFSET AGD_DIAS_UTEIS (off-by-one por design)`" (`.dados-sync/maestro.json`, nota de `agendas.agenda.sgdSearchSchedulePast_3days`).
- **Corte do dia / fim de semana:** 18:00:59 e `day_of_week NOT IN (1,7)` (`sgd-regras-e-joins.md` §Pendência).

### 5.3 SLA, TME, TMA, TFM, TEM, abandono (voz e chat)
- **Voz (Genesys):**
  - `sla` = faixa de `metric_tAnswered` (8s, 30s, 60s, 90s, 2/3/5/10/20 min, > 20) e `tma_txt` = faixa de `metric_tTalk` (`fluxo-db_genesys.md:201-238`).
  - Abandono: `aband_txt` por `metric_tAbandon` ("Immediate" ≤ 8s…) (`:155-165`).
  - SLA do painel: "`sum(metric_oServiceLevel) / (sum(metric_nOffered) - AbandonedUntil_3min)`", em que AbandonedUntil_3min = `tAbandon60 + 120 + 180` (`references/powerbi/catalogo-relatorios.md:66-76`).
  - TME = `metric_tAnswered / metric_nAnswered` (`catalogo-relatorios.md:84-89`). **TME** aqui é tempo médio de **espera** (inferido pelo cálculo).
  - ⚠️ **Em revisão (P-16, ver `negocio-perguntas-em-aberto.md`):** o SLA de voz acima é calculado por faixas de `metric_tAnswered`/`metric_tTalk`, mas a Genesys Cloud tem uma métrica **oficial** própria para SLA — `oServiceLevel` (target/ratio/numerador/denominador) e `oServiceTarget` (a meta) — que a fila já calcula nativamente (ver `dados-genesys-glossario-metricas.md` §3). Não confirmado se o painel deveria usar o `oServiceLevel` nativo em vez do corte manual em `tAnswered`; perguntar ao time antes de tratar como oficial.
- **Chat (Plug):** `plug-queue-realtime` publica TME, TMA, TFM e TEM (`references/dados/fluxos-maestro.md:34`) em `DB_WEBCHAT.temp.tme_protocols`, `tma_protocols`, `tfm_protocols`, `tem_protocols` (`postgres-db_webchat.md:54-61`). Definições literais: "Tempo de Espera (metric-api/te)", "Tempo de Atendimento (metric-api/ta)", "Tempo de Espera Medio (metric-api/tem)", "Tempo de Fila Medio (metric-api/tfm)" (`orq:modules/plug_queue_realtime/sql/queries.sql:38-60`, via extração).
  - **⚠️ Observação:** no chat, a sigla TME vem da métrica "te" (tempo de espera), e o próprio chat tem uma TEM (espera média) separada.
  - Protocolo "preso" = duração ≥ 2700 s no tenant principal (`orq:modules/plug_queue_realtime/protocols.py:979-980`). Primeira resposta: `DB_WEBCHAT.webchat_first_answer.primeira_resposta` (segundos entre transferência/assunção e 1º texto do agente) (`fluxo-db_webchat.md:32-92`).
- **SS:** `ss_tramites.sla_interacao`, `sla_n3`, `sla_tme` vêm do Sybase. O Dataflow calcula `seq_interacao` e `sla_interacao_minutos` (`fluxo-db_sgd_all.md:487-500`).
- **Ocorrência:**
  - `tme_minutos`: tipo 1 = entrada → resposta do e-mail (extraídas do HTML da descrição); tipo 2 = entrada → 1º trâmite (`occurrence.py:42-77`).
  - `tma_total_minutos`: soma de minutos úteis entre trâmites, excluindo trâmites em situações (4,5,9,11) e os precedidos de 10, mais o tempo desde o último trâmite para ocorrência não encerrada (≠ 3,5,8,10,12) (`occurrence.py:78-103`).
  - `tma_sub_minutos`: tempo das subocorrências (`:104-138`).
- **Projetado:** `forecast.tme_projetado` (planilha "ProjecaoTME", por `setor`, `canal`, `seg`).

### 5.4 Fila / skill / NOT READY / presença
- **Genesys:**
  - `public.queue` ("Cadastro das filas") e `public.skills` ("Cadastro das Filas") com `area` e `regional` (`postgres-db_genesys.md:74,90`). Nome exibido = `substring(name,14)` (remove o prefixo "Latam_Brazil_Dominio_…", inferido).
  - Presença: `presenceDefinitions` + `HistoricAgentStatus` (tradução pt em `fluxo-db_genesys.md:100-122`: "Admin" → 'Apoio', "System Issues" → 'Testes / Análises', "On Queue" → 'Atendendo'…).
- **NOT READY:** `%notReady = 1 - (idle + interacting) / (foraFila + naFila + treinamento)` (`catalogo-relatorios.md:305-361`). Push `_genesysNotReady` pelo job `genesys-sla`.
- **Meta de tempo falado:** "`VAR meta = 6`" horas; "Ruim" se restante ≤ 0,1667 h, "Alerta" ≤ 1 h (`catalogo-relatorios.md:776-795`).
- **WebChat:** `initialqueue` normalizada ("Simples Nacional - Sul" → "Escrita Fiscal - Simples Nacional (SUL)"; '' → 'Transferência telefonia') (`fluxo-db_webchat.md:75-81`).

---

## 6. Agenda, ausência, ocorrência, implantação

### 6.1 Agenda / ausência
- **Definição:** lançamentos do colaborador: ausências, treinamentos, compromissos. Tipos: "Ausência, Compromisso, Reunião, Treinamento, Deslocamento, Outros" (`sqlbase:agente/MAPEAMENTO_BANCO_DADOS.md:267`, via extração).
- **Sybase:** `vw_agenda` (`i_responsaveis` = dono; `i_usuarios` = quem lançou), `vw_agenda_tipos`, `vw_agenda_motivos_ausencias`.
- **Lançamento por outra pessoa:** "`Lancto_Diferente = (case WHEN nome_do_tecnico <> responsavel_lancto then 1 else 0 end)`" (`fluxo-tb_sybase_sgd_agenda.md:26-28`).
- **Minutos no Dataflow:** limitados a 480, descontando o almoço 12:00-13:30; sem início/fim = 480 (`fluxo-db_sgd_all.md:1105-1144`).
- **Motivo 0 = tempo trabalhado:** em `tb_demanda_lideres`, os minutos com `i_absences_reason = 0` contam como trabalhados e os demais motivos subtraem (`demanda.sql:71-72`). A linha "motivo 0" é **sintetizada** pelo `import-agendas`: "480 - minutos da agenda do GESTOR com tipos (8,10,11,12,13) e motivos (7,30)" (`orq:modules/_import_dominio/…/domains_agendas/agenda.py:180-220`, via extração). A ausência é contada para os tipos 10,3,4,14,8,24 ou área 3, com teto de 480 (`agenda.py:143-173`).
- **Colaborador ativo na agenda:** "`u.cadastro <= wd.dDate`", `i_clientes` nulo, e "Usuário nunca teve auditoria (sempre ativo)" OU "Usuário tem auditoria, mas na data consultada estava ativo" (`agenda.py:97-133`). Dias úteis = sem sábado/domingo e sem `bethadba.vw_feriados` (`agenda.py:75-85`).
- **Postgres:** `DB_SGD.public.sgd_schedule` (60 d), `sgd_schedule_past_future` (−60/+90 d), `sgd_schedule_three_days` (últimos dias úteis); `DB_CTS.public.CTS_Schedule` (365 d).
- **Tempo real:** Dataflow `TB_SYBASE_SGD_AGENDA` (−2 a +6 meses; `inicio`/`fim` em `fluxo-tb_sybase_sgd_agenda.md:18-19`).
- **Projetado:** `forecast.ausencias_projetado` (abas "AusenciasSul" e "AusenciasCampinas").

### 6.2 Ocorrência
- **Definição:** registro interno entre áreas/setores (pai e subocorrências), com trâmites e SLA próprios.
- **Tipo:** "`when o.i_ocorrencia_pai is NULL then 1 else 2`" (`orq:…/occurrence.py:37-41`): 1 = ocorrência principal, 2 = subocorrência.
- **Exclusão fixa:** "`o.id NOT IN (4120)`" (`occurrence.py:141`).
- **Situação 5** = encerrada (inferido pela carga): as abertas são sempre relidas; as fechadas só dentro de 7 dias. "Janela das fechadas ampliada de 1 para 7 dias (pedido do gestor, 2026-09-22)" (`occurrence.py:149-156`).
- **Prioridade:** `sgd_ocorrencia_prioridade`, relida "só a partir de 2026-05-01 (data fixa no SQL)" (`.dados-sync/maestro.json`).
- **Votação/satisfação da subocorrência:** `tb_satisfacao_subocorrencias` (`votacao`, `motivo`) → `tb_ocorrencias_analitica.votacao/motivo` (`orq:modules/historic_tb_ocorrencias_analitica/sql/queries.sql:471-486, 704`).
- **Postgres:** `DB_SGD.public.sgd_ocorrencia*`; analítico `DB_REPORTS_ANALITICOS.public.tb_ocorrencias_analitica` (1 linha por trâmite de ocorrência, com colaborador do dia).
- **Metas:** aba "Ocorrencias" da planilha de metas → `public.goals`.

### 6.3 Implantação / treinamento (externo)
- **Sybase:** `vw_externo*` → `DB_SGD.externo.*` (Dataflow `DB_SGD_IMPLANTACAO`).
- **sql-base:**
  - `externo.tipo`: 1 = Implantação, 2 = Atendimento Externo;
  - `origem`: 1 Implantação, 2 Adendo, 3 Reativação;
  - situações `externo_situacoes`: 1 Não Iniciado, 2 Agendado, 3 Cancelado pelo Cliente, 4 Cancelado pela Unidade, 5 Em Andamento, 6 Concluído, 7 Realizado, 8 Troca de Responsável, 9 Prescrita, 10 Prorrogado, 11 Não Realizado, 12 Cancelado No Show (`sqlbase:agente/DICIONARIO_NEGOCIOS.md:597-598, 620-622, 692-703`);
  - "Concluído na implantação = 6; no treinamento = 6, 7, 9; cancelados = 3, 4, 12" (DICIONARIO:651-678).
- **⚠️ Divergência no sql-base:** "1=Aguardando" (MAPEAMENTO:42) × "1 = Não Iniciado" (DICIONARIO:692); cancelado "3, 4" × "3, 4, 12".
- **Carga:** `externo.implantacao`: "DELETE por id_externos IN (...) da janela" (`.dados-sync/maestro.json`).

---

## 7. Planejamento e metas

### 7.1 Forecast / projetado
- **Definição:** planejamento de demanda e capacidade. Maior parte vem da planilha **Forecast.xlsx** (abas ProjecaoUsuarios, ProjecaoTME, DeParaAreaAlocacao, AusenciasSul/AusenciasCampinas, FTEaprovado, ProdutividadeMedia, AjusteDemanda, DePara, DemandaProjetada — notas em `.dados-sync/maestro.json`).
- **Carga:** "TRUNCA 9 tabelas forecast.* de uma vez → nada do forecast pode rodar em paralelo" (`maestro.json`, `forecast.cleanForecast`). Roda às 03:00 e é recarregado às 12:00 (`import-sgd-meiodia`).
- **Base de usuários de clientes (driver da demanda):** `forecast.client_user_history` (produtos principais, `vlr_contrato > 0`, `forecast.py:404-500`).
- **Congelados:** `forecast.projetado` (`coeff_folha`, `coeff_fiscont`, `coeff_at`, `proj_*` por `unity`), `forecast.coefficient` e `forecast.calls`. "`forecast.criaProjetado` (forecast.projetado), `forecast.calls` (forecast.calls) e `forecast.creatForecast` (forecast.coefficient) foram REMOVIDAS … o Forecast que a consumia está aposentado. As 3 tabelas congelam como estão" (`orq:modules/_import_sgd/catalog.py:210-214`). Mesmo assim, o Dataflow `DB_SGD_ALL` ainda entrega `forecast_projetado` e `forecast_coefficient`.
- **Regra antiga do coeficiente (legado):** filas FOLHA = Dominio_12/13 (+Strategic); FISCONT = Dominio_21/23/24/25/26; SUL = skill `Dominio_CRIC_S` com usuários de `i_resale IN (3,4,13,74)` e AT 48%; CAMPINAS = `Dominio_CAMP_S` com `IN (40,160)` e AT 52% (`legado:analytics_bi_dominio-import-sgd-geral/sgd_import/…/forecast.py:134-239`, via extração).
- **Relatório "Real Time projetado":** lê planilhas "Plano 2026 - Diretoria - replan 1.xlsx" / "Teste demanda.xlsx" (`catalogo-relatorios.md:813-843`). `paineis-tempo-real` grava `temp.projetado_meia_hora` (`fluxos-maestro.md:60`).

### 7.2 Metas / goals
- **Definição:** meta mensal/período por colaborador (e-mail) e por área (AT/Folha/FisCont).
- **Fonte:** planilha de metas, abas "AT", "RegionalCampinas", "RegionalSUL", "N2", "Ocorrencias" → `DB_SGD.public.goals` (`compini`, `compfim`, `email`, `descmeta`, `valormeta`, `meta_at`, `meta_folha`, `meta_fiscont`). "TRUNCATE que abre a carga" + 5 INSERTs (`maestro.json`). Recarregada às 03:00 e às 12:00.
- **Competência:** `compini` pode ser 'AAAA-MM' (mês) ou 'AAAA-MM-DD' (dia). O Dataflow `DB_METAS.goals` expande pelo calendário nos dois formatos (`fluxo-db_metas.md:19-43`).
- **Duplicidade:** "goals: 1 valor por (dia, email) - havia repetições exatas que dobravam a linha" (`demanda.sql:12`).
- **Meta de capacidade:** `DB_REPORTS_ANALITICOS.public.tb_meta_capacidade_atendimento` (sem job conhecido).

---

## 8. Canais: voz (Genesys), chat (Plug/WebChat), IA, CTS/TRIA, LogMeIn

### 8.1 Genesys / ligação / transcrição
- Ligação = conversa (`conversation_id`) em `DB_GENESYS.public."historic_callsAgents"` (1 linha por conversa × agente/sessão, inferido).
- **Ligações para produtividade:** "`metric_nNotResponding = 0 AND direction = 'inbound'`", `count(DISTINCT conversation_id)` por agente e dia (`demanda.sql:53-62`).
- **Vínculo SSC ↔ ligação:** `vw_ssc` → `DB_SGD.public.sgd_genesys` (`conversation_id`, `cadastro_ia`, `tags`), "INSERT ... ON CONFLICT (i_ssc) DO NOTHING" (`maestro.json`); → `DB_GENESYS.public.sgd_ssc_genesys`.
- **Cliente da ligação:** `callsWithClient.i_client`; abandonadas via telefone (`RIGHT(numero_telefone,8) = RIGHT(_ani,8)`) em `temp."SGD_ClientContact"` (`fluxo-db_genesys.md:178`).
- **Usuário Genesys ↔ SGD:** por e-mail: "`UPDATE public.sgd_alocations … SET id_user_genesys = ug.id_user FROM public."users_Genesys" ug JOIN public."users_SGD" us ON trim(lower(ug.email)) = trim(lower(us.email))`" (`clients_sgd.py:600-605`).
- **Transcrição:** `historic_calls_transcript` (`genesys-import` + `genesys-transcricao-realtime`); IA: `historic_calls_ia_new` (insights).
- **Pesquisa:** `survey` → "Problema Resolvido", "Satisfação Atendente", "Detalhe Votação" (`fluxo-db_genesys.md:559-563`).

### 8.2 Chat / Plug / WebChat
- Protocolo = atendimento de chat (`DB_WEBCHAT.public.protocols`), gravado em tempo real por `plug-queue-realtime`.
- **Tenant:** `633cd75c16179f6a15cdace8` = Suporte (Filiais); `6a60bd21f29f6d8e02bf06a1` = Líderes (`fluxo-db_webchat.md:728-731`).
  - "`tennant_id = i.get('tenant') #REVENDA CHAT`" (`orq:modules/plug_queue_realtime/protocols.py:117`): **tenant = revenda do chat**. O tenant principal é regionalizado em SUDESTE/SUL/GERAL; os outros tenants recebem o nome do parceiro (2B Soluções, TOOL BUSINESS, Tekplan, J. DREL, TekNorte, TekSul, Resulta, Harv, SoftNews, TekNordeste) (`protocols.py:987-1026`).
- **Área do chat pela fila inicial (Maestro):** Assuntos Técnicos, Busca NF-e, Messenger, Processos, Honorários, Onvio e Gestta Legado viram AT; Contabilidade/Lalur, Escrita Fiscal, Fiscont CORE, Reforma Tributária e Auditor fiscal viram FISCONT; Folha, Folha CORE, Auditor Folha e Domínio Busca Convenções viram FOLHA; Top menu = TOPMENU; IA/BOT = OUTROS (`orq:modules/plug_queue_realtime/sql/queries.sql:96-136`).
  - **⚠️ Divergência:** o Dataflow usa outra regra, por prefixo de `queuegroup`, em que o resto vira AT (`fluxo-db_webchat.md:135-149`).
- **Usuário do chat ↔ SGD:** `users.i_user_sgd`. No `tb_colaboradores` a ligação é por e-mail (`queries.sql:336`).
- **Líderes/Plug:** `tb_interacoes_lideres_plug_analitico`; pedido de ajuda = `DB_ESPELHO_SQLSERVER.public.interacoes_bi` ou, na falta, apoio via Plug: "`Técnico = id_client / 1000 (regra da fonte)`" (`demanda.sql:139-152, 243`).
- **Clientes liberados:** `sgd_cli_liberados_chat` (`liberado_chat_gpt`, `liberado_tria_plug`, `liberado_chat_humano`).

### 8.3 CTS / TRIA / solução
- **CTS** = base de soluções (banco Sybase `cts`); **TRIA** = assistente de IA (`DB_CTS.tria.*`). Satisfação TRIA: "`likedislike = -1 then 'Insatisfeito' … = 1 then 'Satisfeito' else 'Não Opinou'`" (`fluxo-db_cts.md:207-209`).
- **Uso de solução pelo técnico:** `sgd_ssc_utiliza_solucao`:
  - `opcao_utilizada`: 1 'Pesquisar Resposta', 2 'Utilizar Solução', 3 'Utilizar Solução - SSC gravada';
  - `origem_resposta`: 1 SSC, 2 Solução;
  - `destino`: 1 'Gerado no Cadastro', 2 'Gerado na Visualização da SSC' (`fluxo-db_sgd_all.md:1004-1016`).
- **Pesquisa no CTS:** "`ids_telas_contabil = 0 then 'SiteCTS' else 'Contabil'`" (`fluxo-db_cts.md:134-135`).

### 8.4 IA no SGD
- `sgd_ssc_ia_chat`: análise de IA da SSC (prompt 1 = satisfação/motivo/exemplo; prompt 3 = acesso remoto), com normalização de texto no Dataflow `DB_SGD_IA` (`fluxo-db_sgd_ia.md:20-177`).
- `sgd_ssc_reescrever_ia`; `chain_ia_interacao`.
- **SSC cadastrada com IA:** `ia_register` = 1 se `cadastro_ia`, `cadastro_com_ia` ou `cadastrada_com_ia` = 1 (`requests_sgd.py:280-285`).

### 8.5 LogMeIn (acesso remoto)
- `DB_SGD.logmein.acessos` (`import-logmein`) → `DB_LOGMEIN.logmein_sessoes`, filtrado a Filiais sem UPG e gerentes por nome (`fluxo-db_logmein.md:31-103`).

---

## 9. Satisfação / insatisfação (por canal)

| Canal | Campo | Valores | Citação |
|---|---|---|---|
| SSC | `vw_ssc.satisfacao` → `sgd_ssc.satisfaction_ssc` | 1, 2 = 'Satisfeito'; 3, 4 = 'Insatisfeito'; 0 = 'Não Opinou' | `orq:…/requests_sgd.py:265-271` |
| SSC — texto de conclusão | `sgd_ssc_text_conclusion` | só satisfeitos (`satisfacao in (1,2)`); ignora '', 'OK', 'OBRIGADO', 'OBRIGADA', '.', "'OK.", 'OBRIGADO.', 'OBRIGADA.' e textos com `x00` | `requests_sgd.py:624-626` |
| SSC — motivo/contato | `sgd_ssc_dissatisfaction_historic` | situação 5 e (`permitir_contato_avaliar_insatisfacao = 1` ou motivo preenchido) | `requests_sgd.py:585-594` |
| SS | `ss.ss.i_satisfaction`, `ss_satisfaction_description` | domínio no cadastro (tabela sem job conhecido) | `fluxo-db_sgd_all.md:545-555` |
| Chat (Plug) | `protocols.rating` | '0' = Insatisfeito; '1' = Satisfeito; resto = Não Opinou | `fluxo-db_webchat.md:235-239` |
| TRIA | `tria.chat_interacoes.likedislike` | -1 Insatisfeito; 1 Satisfeito; resto Não Opinou | `fluxo-db_cts.md:207-209` |
| Voz (Genesys) | `survey` | perguntas 1-3 (Problema Resolvido, Satisfação Atendente, Detalhe). KPI do painel: "INSATISFACAO (nao satisfacao): % = insatisfeitos / TOTAL DE VOTACAO" | `fluxo-db_genesys.md:559-563`; `orq:modules/paineis_tempo_real/panels/sql/votacao_insatisfacao.sql:9-11` |
| Solução CTS | `CTS_SatisfactionSearch.Useful` | `util = 1` 'Sim' / 'Não' + comentário | `orq:modules/_import_dominio/…/dados_cts.py:539-545` |
| Ocorrência | `tb_satisfacao_subocorrencias.votacao/motivo` | entrada externa: "nenhum ETL da casa a escreve" | `orq:modules/historic_tb_ocorrencias_analitica/skills.md:159-162` |
| IA sobre SSC | `sgd_ssc_ia_chat` prompt 1 | 'Sim'/'Não'/'Indeterminado' + motivo categorizado | `fluxo-db_sgd_ia.md:23-113` |
| Implantação | `externo.pesquisar_satisfacao` | pesquisa original (3 Satisfeito, 2 Insatisfeito) × nova (1-5) | extração de `sqlbase:legado/bi_produtividade.sql:160-175` |

- **Desconsiderar insatisfação:** `public.sgd_ssc_disregard_dissatisfaction` (`type` = 'SSC' / 'SS' / 'CHAT'; `justif`, `email`) é a tabela mestre. "PRODUTOR da mestre; roda ANTES do consumidor (rotina ss)" (`maestro.json`). É replicada para DB_SGD_N2 e DB_WEBCHAT. Os Dataflows marcam `disregarddissatisfaction = 1` (`fluxo-db_sgd_all.md:857,865-866`; `fluxo-db_webchat.md:252,293`). A **origem** da tabela mestre (formulário/planilha?) não está no código lido.

---

## 10. RLS (segurança por linha)
- **Definição:** o Dataflow `DB_RLS` entrega:
  - `rls_user` (usuários SGD não demitidos + revenda), do Postgres (`fluxo-db_rls.md:24-35`);
  - `rls_username`, com flags por relatório (`rel_satisfacao`, `rel_produtividade`, `rel_demanda`, `rel_pendencia`, `rel_tempo_interno`, `rel_ausencias`, `rel_utiliza_solucao`, `rel_chat_plug`, `reescrever_ia`);
  - `rls_resale` (e-mail → `i_resales`, `tennant_id_chat`);
  - `rls_resale_tenant_id`.
  
  As três últimas vêm de **planilha Excel na web** (`Excel.Workbook, Web.Contents`), não do Maestro (`fluxo-db_rls.md:45-58`).
- **Regra (inferida):** o usuário vê as revendas listadas para o seu e-mail e só os relatórios com flag.
- **Não há RLS no Maestro nem no `_import_sgd`.** O Cockpit (`paineis-tempo-real`) tem RBAC próprio: "administrador (40) > gestor (30) > supervisor (20) > analistas (10)", default-deny por painel (`orq:modules/paineis_tempo_real/auth/rbac.py:32-33`).
