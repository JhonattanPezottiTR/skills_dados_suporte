# Perguntas em aberto, divergências e propostas de correção

> Última atualização: 2026-09-29 · Fonte: comparação entre o Maestro (`orq:` = `C:\GitHub\TR\analytics-bi-dominio-orquestrador\`), os projetos legados irmãos (`legado:<projeto>`), `sqlbase:` (`C:\GitHub\TR\sql-base\`), os Dataflows (`references/dados/fluxo-*.md`) e os arquivos da skill · **Arquivo curado** · Status: **Em revisão** (extraído de comentários/código — validar com o time)

**Como usar este arquivo**
- Enquanto um item estiver aberto, a skill **deve avisar** que a regra está em revisão ao usá-la.
- Quando o time responder, a resposta vira regra `REG-###` em `regras-negocio.md` e o item é marcado como resolvido aqui.
- Prioridade: 🔴 afeta número publicado · 🟠 afeta escolha de fonte · 🟡 documentação.

---

## A. Regras de negócio divergentes

**P-01 🔴 Pendência N1: duas regras em produção**
- **Batch** (`sgd_pendency`): "`n1_pendency = if ssc.situacao_pendente_nivel_um <> 0 and ssc.situacao_pendente_nivel_dois <> 1`" (`orq:modules/_import_sgd/etl/domains/requests_sgd.py:1150-1151`).
- **Realtime:** "Antes o flag N1 era `nivel_um<>0 AND nivel_dois<>1` (exclui N2, errado) … Agora, igual ao SGSC: N1 pendente = (situacao_pendente_geral=1 OU responsavel_um=0 OU responsavel_dois=0) E situacao_pendente_nivel_um=1; N2 … independente do N1" (`orq:modules/produtividade_pendencia_realtime/sql/queries.sql:67-74`).
- **Pergunta:** a regra do SGSC também deve valer para o histórico `sgd_pendency` e para o Dataflow `sgd_ssc_pendency`? Enquanto isso não for decidido, o painel realtime e os relatórios históricos de pendência N1 **não batem**.
- **Proposta** para `dados-sgd-regras-e-joins.md` §Pendência: documentar as duas regras e qual fonte usa cada uma.

**P-02 🔴 Lista de "Filiais" diferente em cada ponto**
- `sgd_users.type_resale` inclui 165 e exclui 18/148 (`orq:…/clients_sgd.py:408-410`).
- `sgd_client.type_resale` inclui 18/148 e exclui 165 (`clients_sgd.py:95`).
- Dataflow `sgd_resales` inclui 18 e exclui 148/165 (`fluxo-db_sgd_all.md:298`).
- sql-base: "Filiais … 3, 4, 13, 74, 40, 160" (`sqlbase:agente/DICIONARIO_NEGOCIOS.md:238-244`).
- **Perguntas:**
  - Qual é a lista oficial de Filiais para o suporte?
  - A 18 é filial ou revenda (18 = "Moretto" no `agrupado`, `fluxo-db_sgd_all.md:314`)?
  - A 148 (USI, testes internos) deve contar como filial?
  - A 165 (Domínio Inova) é filial?
- **Impacto:** `tb_demanda_lideres` usa o `tipo_resale` de `sgd_users`.

**P-03 🟠 Regional de cada revenda (144, 1, 82)**
- **144 (Curitiba / Suporte PR):** "Sul" no DB_SGD_ALL (`fluxo-db_sgd_all.md:300`) × "Regional Campinas" na agenda tempo real (`fluxo-tb_sybase_sgd_agenda.md:74`) × "Curitiba" no legado realtime.
- **Revenda 1:** "Sul" (DB_SGD_ALL, que nunca chega a "Interno(UPG-USI)" pela ordem do CASE) × "CTD" (agenda) × "UPG" (`sgd_users`).
- **82 (Secundários):** "Regional Sul" na agenda × "Demais" no DB_SGD_ALL × "Criciúma" no legado.
- **Pergunta:** qual é o de-para oficial revenda → regional (Sul, Campinas, SP, AT…)? Recomendo uma tabela única no Postgres para substituir os CASEs.

**P-04 🟠 Unidade/regional derivada do NOME do gerente**
- `DB_SGD_ALL.sgd_user_manager_historic.unity` (`fluxo-db_sgd_all.md:1379-1404`), `DB_LOGMEIN` (`fluxo-db_logmein.md:91-103`) e o filtro `Gerente IN (…)` da agenda (`fluxo-tb_sybase_sgd_agenda.md:105-108`) dependem de nomes de pessoas fixos no SQL.
- **Pergunta:** existe cadastro gerente → unidade que possa substituir? O que acontece quando entra ou sai um gerente?

**P-05 🔴 Carga duplicada de `sgd_pendency`?**
- O legado `analytics_bi_dominio-import-sgd-pendencias` grava o **mesmo** snapshot D-1 em `public.sgd_pendency` com INSERT puro (`legado:analytics_bi_dominio-import-sgd-pendencias/sgd_pendency.py:91-95`, via extração). A rotina `pendency` do Maestro faz o mesmo.
- **Pergunta:** o agendador antigo desse projeto foi desligado? Se não, as linhas duplicam e `useful_pendency_days_n1/n2` (COUNT de snapshots) fica inflado.

**P-06 🟠 Situação de SS → área de pendência (3 mapas)**
- Os três mapas: `ss_n2.py:293-300` (cadastro `pending`), `ss_n2.py:538-546` (`ss_pendency`) e `produtividade_pendencia_realtime/sql/queries.sql:444-449`. Tabela comparativa em `conceitos.md` §4.2.
- Divergências:
  - o 25 é TI no realtime e N2 no resto;
  - 16/17 são COORD no realtime e N2 no batch;
  - 26/27 são "DV INT" só no `ss_pendency`;
  - 3,5,13,14,20,21 são N1 só no `ss_pendency`.
- **Pergunta:** qual é o mapa oficial? `sgd-regras-e-joins.md` §SS lista TI = 23,24 e "COORD (só no realtime)", o que confirma a divergência.

**P-07 🔴 Semântica de `vw_usuarios_auditoria.ativo`**
- O filtro "colaborador ativo no dia" é "`not exists(… not usuarios_auditoria.ativo = 0 and … = max(i_usuarios_auditoria) … <= dDate)`" (`orq:…/clients_sgd.py:555-562`). Lido literalmente, ele **exclui** quem tem o último registro com `ativo ≠ 0`.
- A inativação em `sgd_users` usa "`ativo = 1`" como **evento de inativação** (`clients_sgd.py:395-404`).
- **Pergunta:** em `vw_usuarios_auditoria`, `ativo = 1` significa "foi inativado" (registro de auditoria da ação) ou "está ativo"? A resposta define a regra oficial de colaborador ativo. Hoje há três versões: auditoria (ETL), admissão/inativação (`tb_colaboradores`) e `ativo = 1` (agenda/realtime).

**P-08 🟠 Mapa alocação → setor/área**
- Existem pelo menos três mapas:
  - CASE da agenda (`fluxo-tb_sybase_sgd_agenda.md:51-72`);
  - CASE da produtividade (`orq:…/produtividade_pendencia_realtime/sql/queries.sql:612-663` e legado `sgd_productivity.py:22-73`);
  - planilha `forecast.de_para_alocacao`.
- Conflitos:
  - 11 = "Técnica" na agenda e "Coordenação" na produtividade;
  - 31 = "AT - Imp/Exp/Imp" × "Técnica";
  - 33 = alocação anterior (agenda) × "Ausente" (produtividade).
- **Pergunta:** a planilha `de_para_alocacao` é a fonte oficial? Se for, os CASEs devem ler dela.

**P-09 🟠 Produtos principais**
- sql-base: 101, 102, 103, 104, 170, 211, 212, 213 (DICIONARIO:495).
- O forecast usa a mesma lista (`forecast.py:406`).
- `sgd_client` usa 101-104,170,174,190 (cadastro), 101-104,110,170 (inativação) e 101-104,107,110,170,174,190 (assinatura) (`clients_sgd.py:74,98,109`).
- O CTS usa 101-104,110,170.
- **Perguntas:** as datas de cadastro/inativação do cliente devem considerar 211/212/213 (One/Pro/Max)? 174 (Processos) e 190 são "principais" para esse fim? Sem 211-213, um cliente só-Max pode aparecer sem data de cadastro/inativação (inferido).

**P-10 🟡 Situação do contrato**
- sql-base: `situacao` 0 = Ativo, "outros - Inativo".
- Dataflow `sgd_client_product`: "`WHEN situ_contract = 1 THEN 'Inativo' else 'Ativo'`" (`fluxo-db_sgd_all.md:233`).
- **Pergunta:** quais valores existem em `situ_contract` e o que significam?

**P-11 🟡 SA/NE: nomes e códigos — ✅ nomes resolvidos em 2026-09-30 (REG-001)**
- O usuário confirmou: SA = Solicitação de Alteração · NE = Notificação de Erro · SAL = Solicitação de Alteração Legal · SAIL = Solicitação de Implementação Legal. Ver `regras-negocio.md` REG-001 e `glossario.md`.
- **Ainda em aberto:** os **códigos numéricos** continuam divergentes entre fontes — `reason` 0 NE / 1 SA / 2 SAL / 3 SAIL (Dataflow) × `motivo` 1 SAM / 2 SAL / 3 SAIL (sql-base). Não confirmado qual de-para numérico é o oficial (o sql-base usa "SAM" em vez de "SA" no código 1 — sigla adicional a esclarecer).

**P-12 🟡 Siglas sem definição no código**
- SR, SSQL (inferido: solicitação de SQL), SCD (conversão), TFM/TEM (há definição no plug: "Tempo de Fila Medio", "Tempo de Espera Medio").
- DV, GP, TI, PAR, COORD (áreas de SS).
- `forecast.users.tot_sc`/`tot_sp`.
- Colunas `*_seq_deman` do calendário.
- **Pergunta:** o time pode confirmar as siglas?

**P-13 🟡 Situações de SSC com dois significados**
- O 19 aparece em "aguardando resposta em negociação" (3,19) e em "concluidas, prescrita" (5,10,13,17,19,…) (`requests_sgd.py:342,522`).
- **Pergunta:** o 19 é "em negociação" (aberta) ou final? Isso afeta o `time_final_support` e a janela de releitura da SSC.

**P-14 🟡 Meio de acesso "Web" no Dataflow**
- `COALESCE(st.i_ssc_situation, r.i_means_of_access) AS aux_i_Means_of_Access` usa a **situação** do trâmite (1) como se fosse **meio de acesso** (`fluxo-db_sgd_all.md:858,868`). O legado demanda-líderes fazia o mesmo e o extrator marcou como problema (`legado:analytics_bi_dominio-etl-tb-demanda-lideres/sql/etl.sql:209`).
- O Maestro reescreveu como "SSC via Web" = meio 1 **OU** trâmite em situação 1 (`orq:modules/historic_tb_interacoes_lideres_plug/sql/demanda.sql:79-91`).
- **Pergunta:** a regra "SSC que passou por Sem Análise conta como Web" é intencional?

**P-16 🟠 SLA de voz: faixa manual de `tAnswered` × métrica nativa `oServiceLevel`**
- `negocio-conceitos.md` §5.3 documenta o SLA de voz do painel como um cálculo manual sobre faixas de `metric_tAnswered`/`metric_tTalk` e `sum(metric_oServiceLevel) / (sum(metric_nOffered) - AbandonedUntil_3min)` (`catalogo-relatorios.md:66-76`).
- A Genesys Cloud já expõe `oServiceLevel` (target/ratio/numerador/denominador) e `oServiceTarget` (meta) como métricas nativas de SLA por fila — ver `dados-genesys-glossario-metricas.md`.
- **Pergunta:** o SLA publicado deveria usar o `oServiceLevel`/`oServiceTarget` nativos da fila em vez (ou além) do cálculo manual por faixa de `tAnswered`? O `AbandonedUntil_3min` (soma de `tAbandon60+120+180`) é uma regra de negócio do time ou uma tentativa de reproduzir algo que a Genesys já calcula sozinha?
- **Impacto:** se os dois métodos derem números diferentes, o SLA publicado pode não bater com o relatório nativo da Genesys Cloud.

**P-15 🟡 Satisfação da SSC 1-4**
- O código trata 1/2 = Satisfeito e 3/4 = Insatisfeito (`requests_sgd.py:265-271`).
- **Pergunta:** a escala tem graus (muito satisfeito…)? O sql-base diz "escala não documentada".

## B. Lacunas de carga (tabela usada em Dataflow sem job conhecido)

Base: "não mapeado no Maestro" em `dados-fluxos-powerbi.md`. **Pergunta para cada uma:** quem grava, como e com que frequência?

| # | Tabela | Consumida por | Observação |
|---|---|---|---|
| L-01 🔴 | `DB_SGD.public.calendar` | pendência (dias úteis), agendas, minutos úteis, metas, forecast, `tb_colaboradores` | "Nada no Maestro a escreve — é mantida por fora" (`orq:modules/import_agendas/skills.md:55`, via extração). Feriados 2026+ precisam estar lá: TODO em `orq:modules/_import_sgd/etl/minutos_uteis.py:80-83` |
| L-02 | `DB_SGD.forecast.projetado`, `forecast.coefficient` | `DB_SGD_ALL.forecast_projetado`, `forecast_coefficient` | **congeladas** por decisão ("As 3 tabelas congelam como estão", `orq:modules/_import_sgd/catalog.py:210-214`). Proposta: remover as entidades do fluxo ou marcar como históricas |
| L-03 | `DB_SGD.public.sgd_ssc_ss`, `sgd_ssc_reason_dissatisfaction` | `DB_SGD_ALL.sgd_ssc_ss`, `sgd_ssc_reason_dissatisfaction` | sem função no catálogo |
| L-04 | `DB_SGD_N2.ss.ss_dissatisfied_reason`, `ss.ss_satisfaction_description`, `ss.ultimo_backup_bkn` | `DB_SGD_ALL.sgd_ss*`, `sgd_bkn_last_backup` | `ultimo_backup_bkn` tem ~7,7 mi linhas com `data_record` → há carga ativa em algum lugar |
| L-05 🔴 | `DB_REPORTS_CONSOLIDADOS`: `produtividade_n1`, `produtividade_n2`, `pendencias_suporte`, `sla_pendency_time_snapshot`, `tempo_tramite_interno`, `jornada_fte(_etapas)`, `chains_ia`, `backup_nuvem` | `DB_REPORTS_CONSOLIDADOS.*` | todas com PK/`data_importacao` → ETL externo ao Maestro (outro servidor? outro repositório?) |
| L-06 | `DB_REPORTS_ANALITICOS.tb_meta_capacidade_atendimento`, `tb_satisfacao_subocorrencias` | `tb_demanda_lideres`, `tb_ocorrencias_analitica`, Dataflow | "entrada externa ao Maestro … nenhum ETL da casa a escreve" |
| L-07 🟠 | `DB_WEBCHAT`: `protocols_history`, `protocols_sequence_message`, `protocols_all`, `vw_protocolos_all`, `users`, `users_historicstatus`, `tenant_id`, `sgd_cli_liberados_chat` | `DB_WEBCHAT.*` (quase todo o fluxo) | carga batch **planejada, não implementada** (`orq:docs/PLANO-WEBCHAT.md`). Quem alimenta hoje? |
| L-08 | `DB_GENESYS`: `survey_question`, `survey_question_option`, `historic_calls_ia` (antiga), `temp."SGD_ClientContact"` | `genesys_survey`, `genesys_historicCalls_ia`, `genesys_historicCallsAbandoned` | `temp."SGD_ClientContact"` (cliente pelo telefone) não tem produtor conhecido |
| L-09 | `DB_CTS`: `tria.authentication`, `tria.chat_sit_motv`, `public.vw_rel_cts_gpt_saudacao`, base `tria.public.dashboard` | `DB_CTS.*` | — |
| L-10 🟠 | `DB_SGD.suporte.dados_teams_sul` | `DB_SUL_INTERNO.dados_teams_sul` | função **órfã**: "não é chamada por nenhuma rotina (era assim na fonte)" (`.dados-sync/maestro.json`). O dado pode estar parado |
| L-11 | `DB_ESPELHO_SQLSERVER.public.interacoes_bi` | `tb_demanda_lideres.pedido_ajuda` | origem do espelho SQL Server não documentada |
| L-12 | origem da mestre `DB_SGD.public.sgd_ssc_disregard_dissatisfaction` | flags `disregarddissatisfaction` | o ETL só replica; quem insere (formulário/app)? |
| L-13 | planilhas RLS (`DB_RLS.rls_username`, `rls_resale`, `rls_resale_tenant_id`) | RLS dos relatórios | quem mantém e onde fica a planilha? |

## C. Qualidade / bugs vistos no código (confirmar e decidir)

- **Q-01 🟠 `TEMPO_SCD` (conversão):** o ramo ELSE compara `SSC_CONVERSOES.I_CONVERSOES = SSC.I_SSC` (`requests_sgd.py:451,460`). Possível bug; nos ramos de SS/SSQL a comparação é por `I_SSC`. (inferido)
- **Q-02 🟠 Horários:** `sgd_horario_historic` tem data fixa `dDate >='2026-08-01'` (`clients_sgd.py:360`). Não há histórico anterior de horário em `tb_colaboradores`.
- **Q-03 Prioridade de ocorrência:** trunca tudo, mas relê só a partir de 2026-05-01. O histórico anterior some.
- **Q-04 🟠 Agenda:** "`sgdSearchSchedulePastNEW` apaga `public.sgd_schedule` com `date >= inicio` **sem teto superior** e reinsere só o passado" (`orq:modules/import_agendas/skills.md:46-49`, via extração). A tabela `sgd_schedule` não deve ser usada para o futuro; use `sgd_schedule_past_future`.
- **Q-05 🟠 `tb_colaboradores` duplica** cerca de 71 usuários/dia (`orq:CLAUDE.md:890-892`). Nas medidas, use DISTINCT ou dedupe.
- **Q-06 `tb_ocorrencias_analitica`:** perde ~17% dos trâmites em D-30 e tem 40% de fan-out (aceito pelo time; `orq:modules/historic_tb_ocorrencias_analitica/skills.md:121-143`, via extração).
- **Q-07 `sgd_genesys`:** ON CONFLICT DO NOTHING. Tags e IA posteriores da SSC nunca são atualizadas. (inferido)
- **Q-08 Feriados:** `minutos_uteis` (Python) não tem vésperas de 2026+ (TODO literal); o realtime não tem feriado nenhum.
- **Q-09 🟠 Duplicação em reexecução:** `sgd_ssc_answer_time`, `sgd_pendency`, `sgd_sa_priority`, `forecast.client_user_history`, `ss.ss_pendency` e as tabelas AC do import-cts.
  - O README fala em "Oito tabelas" e o skills.md em cinco (divergência de documentação; via extração).
  - O job recusa repetir sem `forcar`.
- **Q-10 Nota desatualizada no catálogo:** `maestro.json`/`catalog.py` dizem "DELETE WHERE i_situacao NOT IN (5)" para `sgd_ocorrencia`; o código atual também apaga as fechadas dos últimos 7 dias (`occurrence.py:149-164`).
- **Q-11 `cleanForecast`:** o comentário diz "TRUNCA 9 tabelas"; o código trunca 8 (via extração).
- **Q-12 Disregard:** "cada execucao bem-sucedida DOBRAVA os backslashes do `justif`" (`orq:modules/_import_sgd/etl/domains/disregard.py:64-72`, via extração). Há limpeza pendente de uma linha.
- **Q-13 Chain IA:** falha por encoding sem `cp1252` (`rotinas.py:284-286`, via extração).
- **Q-14 Genesys:** `metric_oMediaCount`/`oExternalMediaCount` gravam sempre 0 (TODO reg. 0221, via extração).

## D. Propostas de correção para outros arquivos da skill (não editados aqui)

1. **`dados-sgd-regras-e-joins.md`** — ✅ **resolvido em 2026-09-30** (documentação; nenhum dos itens abaixo exigiu decisão de negócio, só registrar o que já se sabia):
   - §Universo de regionais carregadas (ex-§Filiais): renomeado; segue apontando para P-02 (a pergunta "qual é a lista oficial de Filiais" continua aberta).
   - §Pendência: as duas regras de N1 (batch × SGSC) documentadas lado a lado; P-01 continua aberta (qual delas é a oficial).
   - §SS por área: os três mapas e suas divergências explicitados; P-06 continua aberta (qual é o oficial).
   - §Classificações: **19 = ATEND-EXTERNO** acrescentado.
   - §Alocação → área: 33 = "Ausente", 999 = "sem alocação" acrescentados, com nota do mapa divergente da produtividade; P-08 continua aberta.
   - §Produtos e §Ocorrências: **ainda não feitos** — ficam para uma próxima rodada (não bloqueiam o restante).
2. **`references/glossario.md`** — ✅ **resolvido em 2026-09-30:** SA/NE e SS com a divergência de nomes registrada (P-11 permanece aberta quanto à definição correta); TFM/TEM/TME do chat acrescentados, com alerta de que "TME" tem outro significado em outros relatórios.
3. **`.dados-sync/maestro.json` / `scripts/mapear_maestro.py`** (gerado; ajuste no gerador, não à mão):
   - O `uso_sybase` lista tabelas físicas (`bethadba.ssc`, `bethadba.usuarios`, `dba.revendas`…) para `produtividade-pendencia-realtime` e `genesys-sla`. É **falso positivo**: os nomes vêm dos **comentários de de-para** no topo de `orq:modules/produtividade_pendencia_realtime/sql/queries.sql:13-35` e `orq:modules/genesys_sla/sql/queries.sql:26-33`. O SQL efetivo já usa `vw_*`/`POWER_BI.vw_usuarios` ("O login de BI so tem SELECT nas views `vw_*`; apontar para a tabela fisica da erro de permissao em producao (foi o que derrubou o genesys-sla)", `queries.sql:7-8`).
   - Proposta: o gerador deve ignorar linhas de comentário `--`. ✅ Já corrigido em versão anterior (`mapear_maestro.py` usa `sem_comentarios()`).
   - Nota desatualizada de `sgd_ocorrencia` (Q-10) — ainda não corrigida.
4. **`dados-fluxos-powerbi.md`** (gerado) — ✅ **resolvido em 2026-09-30:** `scripts/mapear_fluxos.py` ganhou o dicionário `NOTAS_CONHECIDAS`; `forecast.projetado` e `forecast.coefficient` agora aparecem como "congelada (decisão... catalog.py:210-214)" e `public.calendar` como "mantida manualmente por fora do Maestro", em vez de "não mapeado no Maestro".
5. **`dados-linhagem.md`** §2: as associações "?" de push podem ser completadas pelo README do `produtividade-pendencia-realtime`. PENDENCY = SSC N1; PENDENCY_N2 = SS; ENTRY_N2 = SS do dia; PRODUCTIVITY; DEMAND (`orq:modules/produtividade_pendencia_realtime/README.md:10-14`, via extração) — ainda não feito.

## E. Alertas de segurança observados (sem reproduzir segredos)

- **S-01 🔴 Senha em texto aberto nos Dataflows:** as definições exportadas `fontes/dataflows/DB_SGD_ALL.json` (entidade `sgd_client`) e `fontes/dataflows/DB_WEBCHAT.json` (entidade `webchat_protocols`) contêm uma connection string de `dblink` com usuário e senha em texto aberto. Nos `.md` da skill já aparece mascarada (`***`).
  - Recomendação: rotacionar a senha e trocar o dblink inline por foreign server + user mapping, ou por uma view.
  - Avaliar tirar esses `.json` do versionamento ou mascará-los na sincronização.
- **S-02 🟠 DSN com senha montada por concatenação no Maestro:** "TODO(seguranca reg. 0065): o bloco ETL_DBLINK é preenchido por concatenação de string (as 3 DSNs libpq embutem a senha …)" (`orq:modules/historic_tb_colaboradores/sql/queries.sql:8-10`). A dívida é conhecida e o código não loga a DSN.
- **S-03 🟠 Chaves de push do Power BI:** "devem ser tratadas como expostas e rotacionadas" (`orq:CLAUDE.md:843-844`, via extração).
- **S-04:** os templates de URL de solução do CTS estão hardcoded no legado `cts-import` (`sgd_dadosCTS.py:9-10`, via extração). É só URL pública de aplicação, sem credencial; valores omitidos aqui.

## F. Lacunas desta extração

- Os 4 agentes de extração (Maestro `_import_sgd`, demais módulos, legados, `sql-base\agente`) concluíram. Os `spec.yaml` não foram lidos um a um: os horários vêm de `fluxos-maestro.md` e dos skills/README.
- Citações "via extração" foram transcritas pelos agentes e não conferidas linha a linha por mim. As de `clients_sgd.py`, `requests_sgd.py`, `occurrence.py`, `rotinas.py`, `historic_tb_*`, `produtividade_pendencia_realtime/sql/queries.sql` e `genesys_sla/sql/queries.sql` foram lidas diretamente.
- O `sql-base\agente` cobre sobretudo implantação, contratos e pós-venda. Não traz definição para SSQL, SR, pendência, SLA, fila, forecast, metas, CTS, chat, Genesys nem RLS.
