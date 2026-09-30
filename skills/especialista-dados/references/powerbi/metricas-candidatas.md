# Métricas candidatas a regras de negócio (interpretação dos PBIX)

> Última atualização: 2026-09-29 · Fonte: 86 arquivos `.pbix` da pasta *Suporte Dominio* (metadados em `catalogo-pbix.md` / `.dados-sync/pbix.json`, gerados por `scripts/mapear_pbix.py`) cruzados com `dados/fluxos-powerbi.md` e `dados/sgd-regras-e-joins.md` · **Arquivo curado** (editado à mão)
> ⚠️ **Status: Em revisão.** Tudo aqui é **interpretação** do DAX/M encontrado nos relatórios, ainda não validado pelo time. Cada métrica tem um ID provisório `MC-###`; quando o time validar a definição, ela vira `REG-###` em `regras/negocio.md` (e o ID `MC` deve ser citado como origem).

## Como ler

- **Relatórios vigentes** = os da raiz das pastas (`Metas de Atendimento 2026`, `Workspace Domínio suporte N1`, `N1`, `N1/Atuais_Setembro`, `N1/RealTime`, `WebChat`, `CTD`, `APOIO…`). **Legados** = `OLD`, `SEM USO`, `Inutilizados`, `*_BK`, `* - Copy`, `*-<máquina>` (cópias de conflito do OneDrive). As divergências abaixo priorizam os vigentes; legados só aparecem quando ajudam a entender a evolução.
- **Origem** segue a cadeia *entidade do Dataflow → tabela Postgres (base) → job do Maestro*. Detalhe de cada entidade em `dados/fluxo-<dataflow>.md`.
- Unidades de tempo encontradas: Genesys em **milissegundos** (`/1000`), WebChat em **segundos**, SGD (`sgd_ssc_answer_time`, `sgd_ssc_internal_time`, `sgd_schedule.minutes`) em **minutos**.
- Padrão de exibição quase universal: tempo convertido para inteiro `HHMMSS` (`CONVERT(vHH&vMM&vSS, INTEGER)`) e formatado no visual. Não é regra de negócio, mas deve virar padrão `DAX-###` (ou ser substituído por format string dinâmica).

## Resumo das divergências mais relevantes

| # | Métrica | O que diverge | Relatórios |
|---|---|---|---|
| D1 | **Pendência %** | Soma de flags diárias ÷ SSCs **vs** SSC pendente contada **uma vez** ÷ SSCs vinculadas a ligação | `sgd_pendencia` × `Metas 2026/Pendência e tempo resposta` |
| D2 | **Produtividade (entregas/dia)** | 5 fórmulas diferentes: o que é "ligação atendida" (`_nHandle`, `_nAnswered`, `conversation_id` distinto, menos transferidas < 90 s ou não), SSC "atendida" × "aberta" × "cadastrada+assumida" | `Metas 2026/Produtividade`, `Produtividade - Quartis`, `sgd_produtividade`, `sgd_demanda_cliente_canal`, `_genesysSGD_Productivity`, `Demanda dos Times Lideres` |
| D3 | **Dias trabalhados** | Divisor 480 min × 432 min (a partir de 2026-08-01) × sempre 480; ajuste de atestado ×0,5 sobre *compensação de banco de horas* × ×0,4 sobre *atestado* | `Metas 2026/Produtividade`, `Produtividade - Quartis`, `Horario colaboradores`, `Forecast 2026`, `sgd_produtividade`, `webchat_geral_novo` |
| D4 | **TME fone** | `tWait/nWait` (tempo de espera) × `tAnswered/nAnswered` (ASA) com **o mesmo nome** `qualificat_tWaiting_decimal` / "TME" | `genesys_calls`, `geral_metrics`, `_genesysQueueSLA`, `Forecast 2026` |
| D5 | **TMA fone** | `(tTalkComplete+tHeldComplete)/nº conversas` × `(tTalk+tHeld)/nº` × `tHandle/nº` × `tHandle/nHandle` (fila) | `genesys_calls`, `Metas 2026/Pendência…`, `Forecast 2026` |
| D6 | **% Insatisfação SSC** | `DISTINCTCOUNT` × `COUNTROWS`; data de conclusão (`USERELATIONSHIP dateconclusion`) × relacionamento ativo; "descontados" subtraídos sem cruzar com insatisfeito | `Metas 2026/Pendência…`, `geral_metrics`, `sgd_satisfacao`, `sgd_demanda_cliente_canal`, `Metas 2026/Produtividade`, `Ocorrências` |
| D7 | **Absorção da IA no chat** | `IA ÷ total` × `IA ÷ (total sem bot)` × `(IA horário comercial + abandono em fila) ÷ (…)` | `web_chat_resolucao_satisfacao(_BK)`, `Forecast 2026` |
| D8 | **% Abandono fone** | `nAbandon/nOffered` (skill) × `_tAbandon/_nOffered` (fila, usa campo de **tempo** no numerador) | `genesys_calls` |
| D9 | **SSC Web (demanda)** | meio de acesso `=1` × `IN (1,3,4,5)` × `descricao="Web"` + filtro `Filiais` | `geral_metrics`, `sgd_demanda`, `atendimentos-digital`, `Forecast 2026` |
| D10 | **Faixas de meta** | "Parcial" < 100 % × < 99,8 % | `Metas 2026/Produtividade` × `Produtividade - Quartis` |

---

## 1. Pendência

### MC-001 · % Pendência N1 / N2 (pendência-dia)
- **Definição inferida:** proporção de SSCs que estavam pendentes (N1 ou N1+N2) em cada dia, somando as marcações diárias.
- **DAX de referência** (`N1/sgd_pendencia`, também presente sem uso em `Metas 2026/Pendência e tempo resposta`):
  ```dax
  PendencyN1_% = IF(DISTINCTCOUNT(sgd_ssc[i_ssc])>0, SUM(sgd_ssc_pendency[n1_pendency])/DISTINCTCOUNT(sgd_ssc[i_ssc]), SUM(sgd_ssc_pendency[n1_pendency])/1)
  PendencyN2_% = (SUM(sgd_ssc_pendency[n1_pendency])+SUM(sgd_ssc_pendency[n2_pendency]))/DISTINCTCOUNT(sgd_ssc[i_ssc])
  Pendency_N1_N2 = SWITCH(TRUE(), MAX('pendencyLevel'[Cod])=1,[PendencyN1_%], MAX('pendencyLevel'[Cod])=2,[PendencyN2_%])
  ```
- **Origem:** `DB_SGD_ALL.sgd_ssc_pendency` ← `DB_SGD.public.sgd_pendency` (import-sgd-diario, acumula + update) e `DB_SGD_ALL.sgd_ssc` ← `public.sgd_ssc`. Flags `n1_pendency`/`n2_pendency` = regra de `sgd-regras-e-joins.md` §4 (níveis um/dois, corte 18:00:59, sem fim de semana).
- **Observação:** o "N2 %" soma N1+N2 — ou seja, "N2" aqui significa *pendência total*. A tabela `pendencyLevel` é uma tabela manual (Enter data) usada como seletor.
- **Perguntas:** (1) Pendência N2 deve incluir N1? (2) Uma SSC pendente por 5 dias conta 5 vezes? (3) O denominador é SSCs *abertas* no período ou *ativas*?

### MC-002 · % Pendência única (SSC contada uma vez) — versão Metas 2026
- **Definição inferida:** das SSCs vinculadas a ligações (fone), quantas **entraram em pendência pela primeira vez** dentro do período selecionado.
- **DAX** (`Metas de Atendimento 2026/Pendência e tempo resposta`, medidas usadas nos visuais):
  ```dax
  Soma Pendencia por SSC Unica =
  VAR SelectedDates = VALUES('calendar'[date_int])
  RETURN SUMX(CALCULATETABLE(VALUES(sgd_ssc_pendency[i_ssc]), REMOVEFILTERS('calendar')),
         VAR FirstDates = CALCULATE(MIN(sgd_ssc_pendency[date]), REMOVEFILTERS('calendar'), sgd_ssc_pendency[n1_pendency] >= 1)
         RETURN IF(FirstDates IN SelectedDates, 1, 0))
  Contagem de SSCs (filtrada) = CALCULATE(DISTINCTCOUNT(sgd_ssc_vs_genesys[i_ssc]), TREATAS(VALUES(sgd_ssc[i_ssc]), sgd_ssc_vs_genesys[i_ssc]), REMOVEFILTERS(sgd_ssc_pendency[n1_pendency]), REMOVEFILTERS(sgd_ssc_pendency[n2_pendency]))
  PendencyN1_% liga = DIVIDE([Soma Pendencia por SSC Unica], [Contagem de SSCs (filtrada)])
  ```
  (N2: mesma lógica com `n1_pendency + n2_pendency >= 1`.)
- **Origem:** `sgd_ssc_pendency` + `DB_SGD_ALL.sgd_ssc_vs_genesys` ← `DB_SGD.public.sgd_genesys` (SSC × conversa Genesys).
- **⚠️ Divergência D1** com MC-001: numerador (dias × SSC única) e denominador (todas as SSCs × só SSCs com ligação) diferentes. Os números **não são comparáveis**.
- **Perguntas:** a meta 2026 de pendência vale só para SSCs de telefone? Qual é o valor-meta (não há medida de meta de pendência nos PBIX)?

### MC-003 · Pendência em tempo real (N1 / N2 / Sem Análise)
- **Definição:** foto atual das SSCs pendentes, por nível, com a SSC "Sem Análise" mais antiga e prioridade.
- **DAX** (`N1/RealTime/SGD/_pendenciasN1`, push dataset): `n1 = SUM(RealTimeData[n1_pendency])`, `i_ssc (Sem analise) = CALCULATE(DISTINCTCOUNT(RealTimeData[i_ssc]), RealTimeData[situacao]="Sem Análise")`, `Ultimo Sem Análise = CALCULATE(MIN(RealTimeData[ulti_tramite])-0.125, …)` (−3 h de fuso aplicado no DAX), `Prioridade Calculada` = SSCs com `prioridade="Sim"` na última carga.
- **Origem:** push dataset alimentado pelo job `produtividade-pendencia-realtime` (Sybase direto).
- **Classificação "Domínio/Inova"** (medida `Dominio-Inova`, repetida como coluna em `sgd_demanda`, `sgd_tempo_resposta` e `_pendenciasN2`): lista fixa de sistema/módulo/tópico → "Domínio/Inova" / "Inova" / "Demais". **Candidata a regra própria (MC-004)** — hoje está copiada em 5 lugares.
- **Perguntas:** o −0,125 (3 h) é correção de fuso do job? A lista Domínio/Inova tem dono?

## 2. Tempo de resposta e tempo interno da SSC

### MC-010 · Tempo médio de resposta ao cliente (SSC)
- **Definição inferida:** tempo em que a SSC ficou com o suporte aguardando resposta (minutos úteis), com duas opções do usuário: **descontar o 1º trâmite** (tempo sem análise) e **descontar o tempo com N2/terceiros** (SS, SSQL, conversão, SR). Exibido como soma ou média por SSC.
- **DAX** (`Metas 2026/Pendência…` e `N1/sgd_tempo_resposta`):
  ```dax
  -- reportOption=1 (descontar 1º trâmite) e pendencyLevel=1 (descontar N2):
  CALCULATE(SUM([TimeWithoutAnalysis]) + SUM([TimeSupport]) - (SUM([TimeSS])+SUM([TimeSSQL])+SUM([TimeConversao])+SUM([TimeSR])), [FirstProcedure]="Não")
  + CALCULATE(SUM([TimeSupport]) - (SUM([TimeSS])+SUM([TimeSSQL])+SUM([TimeConversao])+SUM([TimeSR])), [FirstProcedure]="Sim")
  TimeMediumDecimal = SWITCH(MAX(reportType[Cod]), 1, [TimeGereral]/60, 2, [TimeGereral]/COUNT(sgd_ssc_answer_time[i_ssc])/60)
  ```
- **Origem:** `DB_SGD_ALL.sgd_ssc_answer_time` ← `DB_SGD.public.sgd_ssc_answer_time` (acumula; calculado pelo Maestro, provavelmente via `relatoriotemporespostaanalitico`/`minutosuteis`).
- **Observação:** a opção "descontar 1º trâmite" na verdade **inclui** `TimeWithoutAnalysis` para os trâmites que não são o primeiro e o exclui do primeiro — o nome do seletor pode confundir. Média é por **linha** (`COUNT`), não por SSC distinta.
- **Perguntas:** qual combinação de seletores é a oficial para a meta? Média por trâmite ou por SSC?

### MC-011 · Tempo da 1ª resposta após "troca de responsável"
- **DAX:** coluna `sgd_ssc_tramites[Tempo_Apos_18]` = minutos úteis (seg–sex, 08:00–18:00) entre o trâmite anterior com **situação 18** (troca de responsável, `sgd-regras-e-joins.md`) e o trâmite atual; `Primeira_Resposta = AVERAGE(sgd_ssc_tramites[Tempo_Apos_18])`.
- **Relatório:** `Metas 2026/Pendência e tempo resposta`.
- **Divergência:** janela útil 08–18 fixa no DAX, sem feriados (o Postgres tem `public.calendar` com dias úteis). **Pergunta:** usar `calendar.day_useful_year`?

### MC-012 · Decomposição do tempo de vida da SSC (`sgd_tempo_resposta`)
- `T_Suporte = (Σtime_total − Σbond_attachment_sa_ne)/SSCs/60` (desconta tempo anexada a SA/NE), `T_SS` (tempo com SS normalizado a no máx. `time_total`), `T_First` (antes da 1ª análise), `T_Tecnico = time_total − first − SS − SA/NE`, `T_Cliente = média(time_final_support) − média(time_total)`; todas por **data de conclusão**.
- **Origem:** colunas de tempo de `DB_SGD_ALL.sgd_ssc` ← `public.sgd_ssc`.
- **⚠️** aqui o resultado é dividido por 60 e depois de novo por 60 na formatação — sugere `time_total` em **segundos**, enquanto `sgd_ssc_answer_time` está em minutos. **Pergunta:** confirmar unidades das colunas `time_*` de `sgd_ssc`.

### MC-013 · Tempo interno (resposta interna entre setores)
- `TimeInternalDecimal = Σ sgd_ssc_internal_time[timeanswer] / nº / 60` (horas). `sgd_tempo_resposta` tem seletor soma/média; `Time Líderes` usa só média.
- **Origem:** `DB_SGD_ALL.sgd_ssc_internal_time` ← `public.sgd_ssc_internal_time` (situações 6→7, aguardando/respondido interna).

## 3. Satisfação / insatisfação

### MC-020 · % Insatisfação SSC (N1)
- **Definição inferida:** SSCs concluídas no período com voto "Insatisfeito" ÷ SSCs concluídas com voto (satisfeito ou insatisfeito). Versão "Excluded" retira as insatisfações desconsideradas (`disregarddissatisfaction = 1`).
- **DAX de referência** (`Metas 2026/Pendência…`):
  ```dax
  NumSSC_Voted = CALCULATE(DISTINCTCOUNT(sgd_ssc[i_ssc]), USERELATIONSHIP(Calendar[Date], sgd_ssc[dateconclusion]), sgd_ssc[satisfaction_ssc] <> BLANK())
  NumSSC_Dissatisfied = CALCULATE(DISTINCTCOUNT(sgd_ssc[i_ssc]), USERELATIONSHIP(Calendar[Date], sgd_ssc[dateconclusion]), sgd_ssc[satisfaction_ssc] = "Insatisfeito")
  NumSSC_Excluded = CALCULATE(DISTINCTCOUNT(sgd_ssc[i_ssc]), USERELATIONSHIP(Calendar[Date], sgd_ssc[dateconclusion]), sgd_ssc[disregarddissatisfaction] = 1)
  Dissatisfied_%_Excluded = IF([NumSSC_Dissatisfied]-[NumSSC_Excluded] <= 0, 0, ([NumSSC_Dissatisfied]-[NumSSC_Excluded])/[NumSSC_Voted])
  ```
- **Origem:** `DB_SGD_ALL.sgd_ssc` (`satisfaction_ssc` texto derivado de `satisfacao` 1–2 = Satisfeito, 3–4 = Insatisfeito, 0 = não opinou — `sgd-regras-e-joins.md`; `disregarddissatisfaction` ← `public.sgd_ssc_disregard_dissatisfaction`).
- **⚠️ Divergências (D6):**
  - `geral_metrics`: `COUNTROWS` em vez de `DISTINCTCOUNT`.
  - `sgd_satisfacao`: **sem** `USERELATIONSHIP` → filtra pela relação ativa (provavelmente data de entrada), não pela conclusão.
  - `Metas 2026/Produtividade`: `CONTAINSSTRING(satisfaction_ssc,"satisfeito")` e sem data de conclusão; medida `%` devolve **texto**.
  - `Ocorrências`: `COUNT(satisfaction_ssc)` via relação por técnico.
  - Em todas, "Excluded" subtrai `disregarddissatisfaction=1` **sem exigir** que a SSC seja insatisfeita e **não retira** do denominador.
- **Meta (MC-021):** `Meta insatisfação ssc` = **4 %** se o técnico é majoritariamente Web, **2 %** se Fone (dias de alocação por `i_alocation`: fone 26, 28, 52, 54, 71…; web 25, 27, 29, 53, 55). Faixas de resultado:
  | Canal | Não atingiu | Parcial | Atingiu | Excedeu | Excedeu muito |
  |---|---|---|---|---|---|
  | Fone | > 4 % | > 2 % | > 1,7 % | > 1,4 % | ≤ 1,4 % |
  | Web | > 6 % | > 4 % | > 3,7 % | > 2,9 % | ≤ 2,9 % |
  **Perguntas:** a meta "Atingiu" do fone é 2 % (medida `Meta`) ou 1,7–2 % (faixa)? Os códigos de alocação estão completos?

### MC-022 · % Insatisfação Chat
- **Definição:** protocolos encerrados no período com `rating = "Insatisfeito"` ÷ protocolos com voto (`rating <> "Não Opinou"`), por `closed_date`. Versão "Excluded" igual à SSC.
- **Origem:** `DB_WEBCHAT.webchat_protocols` (← `public.protocols`, `protocols_history`, `disregard_dissatisfaction`).
- **Meta:** `Meta insatisfação chat = 5 %`; faixas: Não atingiu > 6,09 %, Parcial > 5,09 %, Atingiu > 3,99 %, Excedeu > 2,99 %, Excedeu muito ≤ 2,99 %.
- **Divergência:** `web_chat_resolucao_satisfacao` usa `webchat_protocols_faturamento_detalhes` e conta `protocol_number` (versão _BK contava `_id`); separa "IA" (`origem_dados="IA"`).
- **% votação chat** (`chatVoted_%`) = votados ÷ encerrados.

### MC-023 · % Insatisfação N2 (SS)
- `N2_Insatisfacao = DISTINCTCOUNT(sgd_ss[i_ss] com satisfacao="Insatisfeito") ÷ DISTINCTCOUNT(sgd_ss[i_ss])` (`geral_metrics`). **⚠️** denominador = **todas** as SS, não só as votadas (diferente de SSC/chat). Origem `DB_SGD_ALL.sgd_ss` ← `DB_SGD_N2.ss.ss`.

### MC-024 · Satisfação em outros contextos (não padronizados)
- **TRIA (chat IA interno):** `%_Dissatisfaction = insatisfeitos ÷ todas as interações` (não só votadas) — `TRIA_GPT`.
- **Pedidos de apoio a líderes (Plug):** `% Satisfação = Satisfeitos ÷ Avaliados`, com `rating "1"` = satisfeito, `"0"` = insatisfeito — `Demanda dos Times Lideres` (Projetos_Andamento).
- **Subocorrências:** `%_insatisfacao = insatisfeitos (planilha SatisfacaoSubocorrencias.xlsx) ÷ total de ocorrências` — `Ocorrências`.
- **Pergunta geral:** padronizar "insatisfação = insatisfeitos ÷ votados" para todos os canais?

## 4. Produtividade e metas individuais

### MC-030 · Produtividade de atendimento (entregas por dia trabalhado) — versão Metas 2026
- **Definição inferida:** entregas do técnico = ligações atendidas (menos as transferidas em até 90 s) + SSCs + protocolos de chat; em modo "média" divide pelos dias efetivamente trabalhados (ajustados por atestado).
- **DAX** (`Metas de Atendimento 2026/Produtividade`, idêntico em `Produtividade - Quartis` e `Produtividade por cargo` com variações):
  ```dax
  callsL_90secondsTransferred = CALCULATE(DISTINCTCOUNT(genesys_historicCallsAgents[conversation_id]), genesys_historicCallsAgents[is_L90_transferred] = 1)
  Answered - transferede <90 = SUM(genesys_callsAgentsHalfHour[_nHandle]) - [callsL_90secondsTransferred]
  SGD/CUIC Davi 2025 SUM = SWITCH(TRUE(), MAX('Tipo de relatório'[Cod])=1, IF([SGD Day Works 40 atestado]>0, [Answered - transferede <90] + DISTINCTCOUNT(sgd_ssc[i_ssc]) + DISTINCTCOUNT(webchat_protocols[_id]), 0),
                                          MAX('Tipo de relatório'[Cod])=2, IF([SGD Day Works 40 atestado]>0, ([Answered - transferede <90] + DISTINCTCOUNT(sgd_ssc[i_ssc]) + DISTINCTCOUNT(webchat_protocols[_id])) / [SGD Day Works 40 atestado], 0))
  ```
- **Origem:** `DB_GENESYS.genesys_callsAgentsHalfHour` (← `public.calls_agents_halfhour`), `genesys_historicCallsAgents` (← `public.historic_callsagents`), `DB_SGD_ALL.sgd_ssc`, `DB_WEBCHAT.webchat_protocols`, `DB_SGD_ALL.sgd_schedule` (← `public.sgd_schedule`, import-agendas).
- **⚠️ Divergências (D2):**
  | Relatório | Ligações | SSC | Chat | Divisor |
  |---|---|---|---|---|
  | Metas 2026/Produtividade | `_nHandle` − transf. ≤ 90 s (flag `is_L90_transferred`) | distintas | distintos | dias ajustados (MC-040) |
  | Produtividade - Quartis | idem, mas ≤ 90 s calculado `tTalk+tHeld ≤ 90000 ∧ nTransferred=1 ∧ Inbound` | distintas | distintos | dias com ajuste ×0,4 atestado, divisor 480 |
  | sgd_produtividade | `_nHandle` inbound (sem descontar transferidas) | "atendidas" distintas | distintos | dias /480 |
  | sgd_demanda_cliente_canal | `DISTINCTCOUNT(conversation_id)` | "abertas" | distintos | dias /480 |
  | _genesysSGD_Productivity (tempo real) | ligações − transferidas | novas web | protocolos Plug | — |
  | Demanda dos Times Lideres | `tb_demanda_lideres[ligacoes]` | `total_ssc` | `atendimento_chat` | `dias_trabalhados` da tabela |
  | webchat_geral_novo | — | — | distintos | dias /480 |
- **Perguntas:** (1) qual é a definição oficial de "ligação atendida" (`_nHandle`, `_nAnswered`, conversa distinta)? (2) desconta transferidas até 90 s sempre? (3) SSC conta todas as do responsável ou só as cadastradas/assumidas (ver MC-031)?

### MC-031 · SSCs cadastradas × assumidas
- `SSCs cadastradas` = SSCs cujo `first_user` é o técnico; `SSCs assumidas` = SSCs onde `i_user <> first_user`; `%sscXAnswered = (cadastradas+assumidas) ÷ (_nHandle − _nTransferred)` — `Metas 2026/Produtividade`. **Pergunta:** "registro de SSC por ligação atendida" é uma meta?

### MC-032 · % sobre a meta e faixas de resultado
- **DAX:** `Meta 2025 SUM (atingiu) = SUM(goals[valormeta])` (ou ÷ dias no modo média); `% sobre meta = [SGD/CUIC Davi 2025 SUM] / [Meta 2025 SUM (atingiu)]`; `Meta excedeu = meta × 1,21`; `Meta excedeu muito = meta × 1,41`.
- **Faixas:** < 70 % Não atingiu · < 100 % Parcial · < 120 % Atingiu · < 140 % Excedeu · ≥ 140 % Excedeu muito.
- **⚠️ D10:** em `Produtividade - Quartis` "Parcial" vai até **99,8 %**. Quartis: Q4 < 90 %, Q3 90–100 %; `Produtividade por cargo`: > 100 %, 90–100 %, < 90 %.
- **Origem:** `DB_METAS.goals` ← `DB_SGD.public.goals` + `public.calendar`.
- **Perguntas:** as faixas 1,21/1,41 (medida) e 1,2/1,4 (texto) são a mesma regra? Qual limite de "Parcial" vale?

### MC-033 · Meta ajustada por capacidade (Forecast)
- `Meta ajustada final goals` = meta da área × fator `MAX(1, atendimento possível real ÷ meta)` por área (AT/Folha/Fiscont); `% produtividade ajust goals = total atendido ÷ meta ajustada` — `Forecast 2026 - Replan`. **Pergunta:** é a meta oficial de área?

### MC-034 · Demanda de apoio aos líderes
- `% sobre Meta Unificada = Σ Produtividade_Realizada ÷ Σ valormeta`; `%_Ajuda = Σ pedido_ajuda ÷ Σ Produtividade_Realizada`; `Ajuda_dia_Trabalhado = Σ total_lider ÷ Σ dias_trabalhados` — origem `DB_REPORTS_CONSOLIDADOS.tb_demanda_lideres` (job `historic-tb-interacoes-lideres-plug`).
- Plug (versão em andamento): `Taxa da IA % = Resolvidas pela IA ÷ Dúvidas`, onde a `tag` do protocolo define o desfecho ("Comunicação entre cliente e IA" = resolvido pela IA; "Atendimento IA + Humano" = escalado ao líder; "Início Atendimento com IA (BOT)" = parou no início). Origem `DB_REPORTS_ANALITICOS.tb_interacoes_lideres_plug_analitico`.

## 5. Dias trabalhados, ausências e agenda

### MC-040 · Dias trabalhados (FTE-dia) a partir da agenda
- **Definição inferida:** minutos de jornada (agenda tipo 0) menos minutos de ausência (tipo > 0), divididos pela jornada diária.
- **DAX** (`Metas 2026/Produtividade`, `Horario colaboradores`, `Forecast 2026`):
  ```dax
  Days Work = VAR v3 = CALCULATE(SUM(sgd_schedule[minutos ajustado]), sgd_schedule[i_type] = 0)
              VAR v4 = CALCULATE(SUM(sgd_schedule[minutos ajustado]), sgd_schedule[i_type] > 0)
              VAR vDivisor = IF(MIN(sgd_schedule[date]) >= DATE(2026,8,1), 432, 480)
              RETURN (v3 - v4) / vDivisor
  SGD Day Works 40 atestado = [Days Work] - [SGD Day Works para Atestado]
  ```
- **⚠️ D3:**
  - divisor **432 min (7h12) a partir de 2026-08-01** só em Metas/Produtividade, Horario e Forecast; `Produtividade - Quartis`, `sgd_produtividade`, `sgd_ausencias`, `webchat_geral_novo`, `sgd_demanda_cliente_canal` usam **480 sempre** e `minutes` (não `minutos ajustado`).
  - "para Atestado": Metas/Produtividade = dias em **compensação de banco de horas** × **0,5**; Quartis = dias em **atestado** × **0,4** (o nome "40 atestado" sugere que a regra original é a de Quartis).
  - `MIN(date) >= 2026-08-01` avalia o período inteiro: um período que cruza agosto/2026 usa 480 para tudo.
- **Origem:** `DB_SGD_ALL.sgd_schedule` ← `public.sgd_schedule` (import-agendas, janela 60 dias), `sgd_schedule_absences_reason`.
- **Perguntas:** qual a jornada oficial e desde quando? Qual ajuste de atestado/compensação vale?

### MC-041 · Dias de ausência e % ausências
- `daysOut = Σ minutes (i_type > 0) / 480`; `% ausências = daysOut ÷ COUNT(sgd_alocation_historic[i_user])` (`sgd_ausencias`). Forecast separa ausências lançadas por grupo de motivo (Afastamentos, Atestados, Folgas, Falhas, Férias, Treinamento, Reuniões, Parcial chat) — listas fixas de `sgd_schedule_absences_reason[description]`. **Candidata a regra:** tabela oficial motivo → grupo (hoje há ao menos 3 listas diferentes, ex.: "Compensação banco de horas" é Folga no Forecast e "ausência" em outra medida).

### MC-042 · Antecedência do lançamento na agenda
- `Diferença = DATEDIFF(data_inicio, dataLancamento, DAY)` — `Data do lançamento na agenda técnica` (live connection). **Pergunta:** existe prazo mínimo de lançamento?

## 6. Telefonia (Genesys)

### MC-050 · SLA de fila
- **Definição:** ligações atendidas dentro do nível de serviço ÷ (oferecidas − abandonadas em até 3 min).
- **DAX** (idêntico em `genesys_calls` e no push `_genesysQueueSLA`):
  ```dax
  AbandonedUntil_3min = SUM(metric_tAbandon60) + SUM(metric_tAbandon120) + SUM(metric_tAbandon180)
  SLA = SUM(metric_oServiceLevel) / (SUM(metric_nOffered) - [AbandonedUntil_3min])
  ```
- **Origem:** `DB_GENESYS.genesys_qualificationsSkills` ← `public.historic_qualifications` (genesys-import; tempo real: job `genesys-sla`).
- **Perguntas:** qual o limiar de `oServiceLevel` (segundos) configurado no Genesys? Abandono "curto" é 3 min mesmo?

### MC-051 · TME fone (tempo médio de espera)
- **⚠️ D4:** duas definições com o mesmo nome:
  - `tWait / nWait` (espera de quem esperou) — `genesys_calls` (`qualificat_TME`), `Forecast 2026` (`TME Real`);
  - `tAnswered / nAnswered` (ASA — velocidade média de atendimento) — `geral_metrics` (medida chamada `qualificat_tWaiting_decimal`!), `_genesysQueueSLA` (`TME`), `Forecast` (`TME Real Acumulado`, comparado à `Meta TME 2025`).
- **Meta TME 2025 (Forecast):** por mês e área, em HHMMSS (ex.: jan Folha/Fiscont 00:02:00, AT 00:04:00; demais meses em geral 2–3 min; fev Folha 00:05:00). **Pergunta:** a meta de TME é sobre ASA ou sobre espera? A tabela de metas mensais deveria sair do DAX para uma tabela.

### MC-052 · TMA fone (tempo médio de atendimento)
- **⚠️ D5:**
  | Relatório | Fórmula |
  |---|---|
  | genesys_calls (`Agent_TMA`) | `(tTalkComplete + tHeldComplete) / nº conversas` |
  | Metas 2026/Pendência… (`Agent_TMA`) | `(tTalk + tHeld) / nº conversas` |
  | genesys_calls (`Agent_TMA_handle`) | `tHandle / nº conversas` (inclui ACW) |
  | genesys_calls / Forecast (`qualificat_TMA`) | `tHandle / nHandle` (visão fila) |
- **Pergunta:** o TMA oficial inclui pós-atendimento (ACW)?

### MC-053 · % Abandono fone
- `qualificat_%Abandono = nAbandon / nOffered` (skill) — padrão. **⚠️ D8:** `genesys_queuePerformance_HalfHour[%_abandono] = SUM(_tAbandon)/SUM(_nOffered)` usa campo de **tempo** no numerador (provável erro). Tempo real: `%Abandonadas = nAbandon/nOffered`.

### MC-054 · % NotReady (indisponibilidade do agente)
- **Definição:** 1 − (tempo em interação + ocioso) ÷ tempo conectado, onde conectado = fora da fila (disponível, ocupado, ausente, pausa, refeição, reunião) + na fila + treinamento. Negativos viram 0.
- **Origem:** `DB_GENESYS.genesys_agentAvailable` (← `public.agentavailable`); tempo real: push `_genesysNotReady` (`Acompanhamento Tempo Real Fone_v2.1`).
- Consistente entre `genesys_calls`, `genesys_notReady` e tempo real (só muda o tratamento de conectado = 0: BLANK × 0).
- **Metas de tempo em status (tempo real, `_genesysStatusAgents`):** Conversando ≤ 15 min bom / ≤ 30 alerta; Disponível fora da fila ≤ 1,5 min / ≤ 3; Testes/Análises e Intervalo ≤ 12 / ≤ 15; Treinamento ≤ 1h45 / ≤ 2h; Chamada externa ≤ 25 / ≤ 30; Ausente ≤ 12. `novo_indicador_tempo_falado`: meta de **6 h** de interação/dia (restante ≤ 10 min = Ruim?). **Pergunta:** são metas oficiais de aderência?

### MC-055 · Qualidade de voz (MOS) e identificação
- MOS: < 3,5 Crítico, 3,5–4,2 Aceitável, ≥ 4,2 Excelente; `% crítico = conversas críticas ÷ total` (atendidas e abandonadas).
- `%NãoIdentifi` = ligações (atendidas inbound + abandonadas) sem cliente SGD (`sgd_iclient = 0`) ÷ total.
- `%_ssc_genesys = SSCs vinculadas a ligação ÷ SUM(_tAnswered)` — **⚠️** denominador é campo de tempo (provável erro; deveria ser `_nAnswered`).

## 7. Chat (Plug / WebChat)

### MC-060 · TME / TMA / 1ª resposta / tempo entre mensagens do chat
- `TME_Decimal = Σ webchat_historic[seconds] / COUNT(_id)`; Forecast filtra `actor = "queue"` (espera em fila) — nos demais não há filtro de ator explícito na medida (depende da entidade/visual). **Pergunta:** TME deve sempre filtrar `actor="queue"`?
- `TMA_Decimal_total_novo = Σ total_seconds / nº protocolos` (`webchat_historic_total`), média por usuário quando ator = "suporte".
- 1ª resposta: `Σ primeira_resposta / COUNT(protocol_number)` (`webchat_first_answer`).
- Entre mensagens: `Σ seconds / COUNT(protocol_number)` (`webchat_historic_messages`).
- Tempo real (push `_tempo*Chat`): `SUM(tempo)/COUNT(id)`; `TEF_Maior` = maior espera em fila.
- **Origem:** `DB_WEBCHAT.webchat_historic*`, `webchat_first_answer` ← `public.protocols`, `protocols_history`, `protocols_sequence_message`.

### MC-061 · % NotReady chat
- `1 − tempo Online ÷ tempo conectado` (`webchat_historic_status` ← `public.users_historicstatus`). Mesmo conceito de MC-054.

### MC-062 · Absorção da IA / bot no chat
- **⚠️ D7:**
  - `_BK`: `_%absorção_ia = protocolos IA ÷ total`.
  - atual (`web_chat_resolucao_satisfacao`, `Forecast`): `(IA em horário comercial + abandono em fila) ÷ (IA horário comercial + IA→humano sem abandono + abandono em fila + humano sem abandono)`; o usuário IA "horário comercial" é identificado por **id fixo** de usuário de chat no DAX.
  - Forecast também: `_%absorção_ia = IA ÷ (total sem bot)` e `% bot real` = protocolos da conta de e-mail do bot ÷ total.
- **Origem:** `DB_WEBCHAT.webchat_protocols_faturamento_detalhes` ← `public.vw_protocolos_all` (não mapeado no Maestro); `origem`/`origem_dados` (bot, IA, humano, humano+IA, abandono, abandono_fila).
- **Perguntas:** abandono em fila conta como "absorvido pela IA"? Os ids fixos devem virar coluna/flag no fluxo?

### MC-063 · Abandono e transferência no chat
- `%_abandono = protocolos com motivo_encerramento_ia = "Abandono" ÷ protocolos` (`webchat_geral_novo`); `%_transf_telefonica = initialqueue "Transferência telefonia" ÷ protocolos`.

### MC-064 · Cadastro de SSC a partir do chat
- `Cad % = SSC com meio de acesso 6 (Chat) ÷ protocolos`; `%_ia = SSC com ia_register=1 ÷ SSC chat` (`webchat_geral_novo`). `sgd_demanda_cliente_canal`: chat = `i_aux_means_access = "6"` excluindo usuário UPG fixo; chat IA = `"11"` (código 11 não está na tabela de meios de acesso de `sgd-regras-e-joins.md` — **pergunta**).

### MC-065 · Efetividade / continuidade do chat
- `Efetividade bruta` (coluna) marca SSC "Efetiva"/"Inefetiva"; `ajustada` considera efetiva quando a área da SSC difere da área do 1º usuário; `Inefetividade - cadastro = inefetivas ÷ protocolos` e `- ligações = inefetivas ÷ _nAnswered` — `Continuidade chat`. **Pergunta:** definição de SSC efetiva?

### MC-066 · Faturamento Plug
- `tot_bot / tot_hum / tot_IA / tot_hum+IA = Σ total protocol` por `origem`; `mensalidade = 46.800,00` fixa no DAX (`web_chat_faturamento`). **Pergunta:** valor contratual deve estar no modelo?

## 8. Demanda e canais

### MC-070 · Demanda por canal (SSC web, ligações, chat) e realizado × projetado
- `geral_metrics`: web = SSC com `i_means_access = 1` por `date_entry`; ligações = `Σ metric_nOffered`; chat = protocolos por `created_date`; `_perc_* = (realizado − projetado) ÷ projetado` com `forecast_demanda_projetada` (← `forecast.demanda_projetada`).
- **⚠️ D9:** SSC web = `IN (1,3,4,5)` (web, fax, e-mail, SOSE) em `sgd_demanda`; `descricao="Web"` + `type_resale="Filiais"` em `atendimentos-digital` e Forecast; ligações = `nOffered` (demanda) × `DISTINCTCOUNT(conversation_id)` (`sgd_demanda_cliente_canal`) × `_nOffered` de `queuePerformance` (`atendimentos-digital`).
- **Perguntas:** demanda web inclui e-mail/fax/SOSE? Demanda considera só Filiais?

### MC-071 · Demanda por usuário do cliente
- `demand_user = COUNT(SSC) ÷ usuários do cliente no último dia ÷ nº meses` (`sgd_demanda`, `forecast_client_user_history` ← `forecast.client_user_history`). Forecast: `Demanda por Usuário Real = nOffered ÷ Σ totusers`.

### MC-072 · % SSC com SS e resolução na 1ª resposta
- `%_ss = SSC com existe_ss = "1" ÷ SSCs` (`sgd_demanda`); `Metas/Produtividade`: `%_abertSS = SSC com lista_ss <> "" ÷ SSCs` — duas colunas para o mesmo conceito.
- `%_primeiraResposta = SSCs de telefone com ≤ 1 trâmite na situação 3 ÷ SSCs de telefone`.

### MC-073 · Mix de atendimento digital × humano (`atendimentos-digital`)
- Pesos fixos: consultas à Central de Soluções ÷ **8**, YouTube ÷ **10**, Instagram ÷ **10**, ChatBot ÷ **2** (ChatBot = 0 fixo); humano = chat + SSC web Filiais + ligações oferecidas. **Pergunta:** origem dos pesos (equivalência de atendimento)?

## 9. Forecast e capacidade (`Forecast 2026 - Replan`)

- **MC-080 · FTE líquido** = FTE aprovado − (férias + rotatividade + ausências programadas) (percentuais de `forecast.ausencias_projetado`).
- **MC-081 · Capacidade** = FTE líquido × produtividade média (`forecast.produtividade_media`); **Atendidas previstas** = mín(demanda projetada, capacidade) por dia; **Absorção** = atendidas previstas ÷ demanda.
- **MC-082 · TME projetado** = busca em faixas de absorção na tabela `forecast.tme_projetado` (ini ≤ absorção ≤ fim; ano 2024 para datas < 2026, depois 2026; canal Chat separado).
- **MC-083 · Balanço de pessoas** = FTE líquido com ausências lançadas na agenda − FTE necessário (+ ajuste de híbridos); rateado por regional pela proporção de FTE.
- **MC-084 · Saldo híbridos** = ligações de outras áreas atendidas pela área − ligações da área atendidas por outras (Folha/Fiscont/AT; SP × Sul).
- Fontes: `DB_SGD_ALL.forecast_*` (← schema `forecast` do DB_SGD) + planilhas SharePoint (`Plano 2026 - Diretoria - replan 1.xlsx`, `SUPREMA - Cópia.xlsx`). **Pergunta:** as planilhas são a fonte oficial do plano ou devem ir para o schema `forecast`?

## 10. Ocorrências (`N1/Ocorrências`)

- **MC-090 · TME ocorrência** = média de `tme_minutos` (tempo até 1º trâmite); **TMA** = média de `tma_total_minutos`; tratativa = TMA − TME. Versões v2 recalculam em segundos úteis 08–18 a partir dos trâmites "Em análise". **⚠️** a medida `TME` divide por 1440 e trata como horas (inconsistente com `TME_Espera_Util`, que usa minutos).
- **MC-091 · % Ocorrência** = ocorrências ÷ (ocorrências + SSCs) (limitado a 100 %).
- **MC-092 · Meta de realização por simultaneidade** = % realizado ≥ meta aplicável, onde meta = 90 % (1 técnico), 40 % (2), 20 % (3), 15 % (4), 10 % (≥ 5 técnicos ativos no período).
- Origem `DB_OCORRENCIAS.sgd_ocorrencia*` (← `public.sgd_ocorrencia*`). Regras de `sgd-regras-e-joins.md` (id 4120 excluído; situações 4, 5, 9, 11 fora do TMA) **não aparecem no DAX** — verificar se já são aplicadas no fluxo.

## 11. Uso de ferramentas e IA

- **MC-100 · % SSC com IA** = SSCs com `ia_register = 1` ÷ SSCs (`cadastro_ticket`, `ferramentas_sscs`). **% com Card** = registros com `origem_resposta = "Solução"` ÷ SSCs; **% Manual** = restante. `sgd_utiliza_solucoes`: `%_utiliza` (qualquer resposta pronta), `%_utiliza_solucao`, `%_utiliza_ssc` — origem `sgd_ssc_pesquisa_resposta_utiliza_solucao` ← `public.sgd_ssc_utiliza_solucao`. **⚠️** numerador `COUNT` (linhas) × denominador `DISTINCTCOUNT` (SSC): pode passar de 100 %.
- **MC-101 · Reescrever com IA:** `% Utilizou resposta = sim ÷ usos`, `% Alterou resposta` (`sgd_utilizou_reescrever_IA` ← `public.sgd_ssc_reescrever_ia`); configuração de saudação/pesquisa = % de usuários com configuração completa na última data.
- **MC-102 · % Saudações padrão (fone)** = ligações com `analise_saudacao = "Sim"` ÷ ligações (`genesys_historicCalls_ia` ← `public.historic_calls_ia(_new)`).
- **MC-103 · TRIA curadoria:** `corretas` = "Resposta Certa" ou "Pediu Mais Informações" sem motivo; `erradas` = interações com usuário ≠ 0 − corretas (`DB_CTS.tria_interactions`).
- **MC-104 · Acessos remotos:** `% Calling Card = sessões Calling Card ÷ sessões`; `% Instalação CC` = miniaplicativo com "CC" nas ferramentas ÷ sessões LogMeIn (`DB_LOGMEIN.logmein_sessoes`).
- **MC-105 · Central de Soluções:** acessos (`cts_sol_access_count`) — **⚠️** `ssc-solutions-top10` usa `COUNTROWS`, a versão _BK usava `DISTINCTCOUNT(i_access_count)`; pesquisas por origem (`id_origem_pesquisa = 2` = CTS).

## 12. Disponibilidade de ferramentas (`incidentes_estrategico`)

- **MC-110 · % Disponibilidade** = (expediente em minutos − minutos de indisponibilidade) ÷ expediente, só dias úteis; por plataforma (BI, Chat, Distribuidor, IA, SGD, Central de Soluções, LogMeIn, Telefonia, Internet). Expediente = `calendar[ExpedienteSGD]` (chat usa `ExpedienteMinutosChat`). Fonte: planilhas SharePoint de incidentes (Forms/Lists) — não passam pelo Maestro.
- **Pergunta:** expediente oficial por plataforma? Incidentes fora do expediente contam?

## 13. Colaboradores

- **MC-120 · Quantidade de colaboradores** = e-mails distintos em `tb_colaboradores` na **última data disponível** do período (snapshot), com filtros de horário de entrada; faixas de tempo de casa: até 3 m, 6 m, 1 a, 2 a, 5 a, acima (mesma faixa em `Demanda dos Times Lideres` e Forecast; `Metas/Produtividade` usa 0–6, 6–12, 12–24, 24+). Origem `DB_REPORTS_ANALITICOS.tb_colaboradores` (job `historic-tb-colaboradores`) — é a fonte recomendada em `sgd-regras-e-joins.md` §5.
- **Pergunta:** padronizar as faixas de tempo de casa?

---

## Padrões técnicos recorrentes (candidatos a `DAX-###` / `FON-###`)

1. **Listas fixas de pessoas no DAX** (gestores → regional/área, gerentes de filial) em colunas calculadas de `IA Chat 1`, `reescrever_ia`, `dados chattt`/`webchat_geral_novo`, `Forecast`. Quebram a cada mudança de equipe → usar `sgd_user_manager_historic`/`tb_colaboradores`.
2. **Ids e e-mails fixos** (usuário de chat IA, conta do bot, usuário UPG 1405244) no DAX → mover para coluna/flag no Dataflow.
3. **Data de referência:** satisfação e tempos usam `USERELATIONSHIP` com a data de conclusão; demanda usa data de entrada/criação. Documentar a data oficial por métrica.
4. **Seletores manuais** (`reportType`, `reportOption`, `pendencyLevel`, `Tipo de relatório`) como tabelas "Enter data" repetidas em cada PBIX → candidato a tabela de parâmetros padrão (field parameters).
5. **Tabela calendário:** `DB_SGD_ALL.calendar` (dias úteis `day_useful_year`) convive com janelas 08–18 fixas no DAX sem feriados.
6. **Fontes fora do padrão:** `incidentes_estrategico` lê Postgres `DB_GENESYS` direto (SQL nativo) + ~12 planilhas SharePoint; `sgd_agenda` usa ODBC direto (Sybase) além do Dataflow `TB_SYBASE_SGD_AGENDA`; Forecast/Horário/Time Líderes dependem de planilhas SharePoint.
7. **Tema:** 68 de 86 arquivos seguem o tema oficial TR Clario; 11 usam uma variante antiga (6/8 cores em comum) e 7 usam só o tema base do Power BI (lista em `catalogo-pbix.md`).

---

## Tipos de BI encontrados

Formato da ficha de `tipos-de-bi.md` (conteúdo proposto; aquele arquivo **não** foi editado). Público inferido pelas páginas, RLS e filtros. Cópias/legados agrupados na ficha do vigente.

### Metas de Atendimento 2026 — Pendência e tempo resposta
- **Objetivo / público:** acompanhar as metas 2026 de pendência (SSC única), tempo de resposta SSC/chat, TMA web e insatisfação — gestores/coordenadores; RLS por e-mail em `genesys_users`.
- **Relatório(s):** `Metas de Atendimento 2026/Pendência e tempo resposta.pbix` · **Workspace:** não identificado (Import publicado)
- **Atualização:** D-1 (Dataflow)
- **Fonte oficial:** `DB_SGD_ALL.sgd_ssc_pendency`, `sgd_ssc_answer_time`, `sgd_ssc_tramites`, `sgd_ssc_vs_genesys`; `DB_WEBCHAT.webchat_first_answer`, `webchat_historic_messages`
- **Métricas:** MC-002, MC-010, MC-011, MC-020/021, MC-022, MC-052, MC-060
- **Dimensões / filtros padrão:** período, gestor/técnico, módulo/tópico, seletores "descontar 1º trâmite" e "descontar tempo N2"
- **Tema:** Padrão TR Clario (COR-001)

### Metas de Atendimento 2026 — Produtividade (+ Workspace: Produtividade - Quartis, Produtividade por cargo)
- **Objetivo / público:** produtividade individual contra a meta (`goals`), quartis de desempenho, SS × SSC, ligações atendidas × SSC registradas — gestão; RLS `Rolemail_user` em `genesys_users`.
- **Atualização:** D-1 (Dataflow)
- **Fonte oficial:** `DB_GENESYS.genesys_callsAgentsHalfHour`, `genesys_historicCallsAgents`; `DB_SGD_ALL.sgd_ssc`, `sgd_schedule`; `DB_WEBCHAT.webchat_protocols`; `DB_METAS.goals`
- **Métricas:** MC-030, MC-031, MC-032, MC-040
- **Dimensões:** gerente, supervisor, técnico, cargo, faixa de tempo de casa, tipo de relatório (soma/média)
- **Tema:** Padrão TR Clario

### Forecast 2026 - Replan
- **Objetivo / público:** planejamento de capacidade (projetado × realizado, FTE, balanço de pessoas, TME projetado × real, saldo de híbridos) — diretoria/planejamento.
- **Atualização:** D-1 (Dataflow) + planilhas SharePoint do plano
- **Fonte oficial:** `DB_SGD_ALL.forecast_*`, `sgd_schedule_past_future`; `DB_GENESYS.genesys_qualificationsSkills`, `genesys_callsAgentsHalfHour`; `DB_WEBCHAT.webchat_protocols_faturamento_detalhes`; planilhas `Plano 2026…`, `SUPREMA…`
- **Métricas:** MC-080 a MC-084, MC-051 (meta TME), MC-033, MC-062, MC-070
- **Tema:** Padrão TR Clario

### Pendências SGD (histórico) — `N1/sgd_pendencia` (legados `OLD/sgd_pendencias`)
- **Objetivo / público:** % pendência N1/N2 por classificação, gestor e nível — técnicos/gestores com RLS por revenda/usuário (`DB_RLS`).
- **Atualização:** D-1 · **Fonte:** `DB_SGD_ALL.sgd_ssc_pendency` + `sgd_ssc`
- **Métricas:** MC-001 · **Tema:** Padrão TR Clario

### Pendências em tempo real — `N1/RealTime/SGD/_pendenciasN1`, `_pendenciasN2`, `N2/RealTime/_pendencyN2`, `_EntrySS_byDay` (legado `OLD/sgd_pendencias_n1`)
- **Objetivo / público:** fila de SSC/SS pendentes agora (sem análise, prioridade, mais antiga, Inova, por regional/unidade/agenda) — coordenação/aquário.
- **Atualização:** tempo real (push) · **Fonte:** push datasets do workspace de tempo real (job `produtividade-pendencia-realtime`)
- **Métricas:** MC-003, MC-004 · **Tema:** `_pendenciasN1/N2` seguem o TR Clario; `_pendencyN2` (tema base) e `_EntrySS_byDay` (variante antiga) não

### Tempo de resposta SSC — `N1/sgd_tempo_resposta` (legado `OLD/sgd_tempo_interno`)
- **Objetivo / público:** tempo de resposta, tempo de vida e tempo interno por analista/unidade/classificação — gestores; RLS.
- **Atualização:** D-1 · **Fonte:** `DB_SGD_ALL.sgd_ssc_answer_time`, `sgd_ssc_internal_time`, `sgd_ssc`
- **Métricas:** MC-010, MC-012, MC-013 · **Tema:** Padrão TR Clario

### Satisfação SSC — `N1/sgd_satisfacao`
- **Objetivo / público:** % insatisfação e votação por técnico/tempo de casa/cliente, textos de insatisfação, encaminhamentos de SS — gestores; RLS.
- **Atualização:** D-1 · **Fonte:** `DB_SGD_ALL.sgd_ssc`, `sgd_ssc_dissatisfaction_historic`, `sgd_ssc_reason_dissatisfaction`, `sgd_ss_forwarding`
- **Métricas:** MC-020 · **Tema:** Padrão TR Clario

### Demanda SGD — `N1/sgd_demanda`, `N1/sgd_demanda_cliente_canal`
- **Objetivo / público:** volume de SSC por tópico/classificação/cliente, SSC × SS, demanda por usuário, Domínio/Inova; canal (fone/chat/soluções), indicações de IA (reforma tributária, erro 8) — gestão/produto; RLS.
- **Atualização:** D-1 · **Fonte:** `DB_SGD_ALL.sgd_ssc`, `sgd_ssc_tramites`, `forecast_client_user_history`, `sgd_client*`; `DB_GENESYS.genesys_historicCalls_ia`; `DB_WEBCHAT.webchat_protocols_ia`
- **Métricas:** MC-070, MC-071, MC-072, MC-064, MC-030 (versão canal) · **Tema:** Padrão TR Clario

### Produtividade SGD (versão 2025/26) — `N1/sgd_produtividade`
- **Objetivo / público:** produtividade por técnico, por fila Genesys e por fila/TAG Plug — gestores; RLS.
- **Atualização:** D-1 · **Fonte:** `genesys_callsAgentsHalfHour`, `sgd_ssc`, `webchat_protocols`, `sgd_schedule`
- **Métricas:** MC-030 (variante), MC-040 (480) · **Tema:** Padrão TR Clario

### Produtividade em tempo real — `N1/RealTime/_genesysSGD_Productivity`
- **Objetivo / público:** ligações, SSCs novas e tramitadas, Plug do dia (aquário/dash) — coordenação.
- **Atualização:** tempo real (push, job `produtividade-pendencia-realtime`) · **Métricas:** MC-030 (variante) · **Tema:** tema base (fora do padrão)

### Telefonia histórica — `N1/genesys_calls`, `N1/genesys_notReady`, `N1/geral_metrics`
- **Objetivo / público:** ligações por regional/cliente, mapa de calor, TME/TMA/SLA/abandono, distribuição, MOS, NotReady e ociosidade; `geral_metrics` = visão geral por regional com projetado × realizado — gestão de atendimento.
- **Atualização:** D-1 · **Fonte:** `DB_GENESYS.genesys_qualificationsSkills`, `genesys_historicCallsAgents`, `genesys_historicCallsAbandoned`, `genesys_queuePerformance_HalfHour`, `genesys_agentAvailable`, `genesys_historicAgentStatus`; `DB_SGD_ALL.forecast_demanda_projetada`
- **Métricas:** MC-050 a MC-055, MC-070, MC-023 · **Tema:** Padrão TR Clario

### Telefonia em tempo real — `_genesysQueue`, `_genesysQueueDetails`, `_genesysQueueSLA`, `_genesysStatusAgents`, `_genesysNotReady`, `Acompanhamento Tempo Real Fone_v2.1`
- **Objetivo / público:** filas e clientes em espera, SLA por fila/área, status e tempo em status dos técnicos, NotReady e meta de horário de pico — coordenação/aquário.
- **Atualização:** tempo real (push; jobs `genesys-queue-realtime`, `genesys-sla`) · **Workspace:** Dashboard - Real Time (onde identificado)
- **Métricas:** MC-050, MC-051 (ASA), MC-053, MC-054 · **Tema:** `_genesysQueue*` e `_genesysStatusAgents` seguem o TR Clario; `_genesysNotReady` e `Acompanhamento Tempo Real Fone_v2.1` usam tema base (fora do padrão)

### Chat geral — `WebChat/webchat_geral_novo` (cópia `N1/Atuais_Setembro/webchat_geral_novo`; legados em `SEM USO`, `N1/dados chattt`)
- **Objetivo / público:** demanda por fila/regional/30 min, TME, TMA, 1ª resposta, entre mensagens, satisfação e listagem de votos, produtividade, NotReady chat, migração, Plug × SGD, adesão de clientes, abandono da IA — gestão do chat; RLS por usuário/revenda/tenant.
- **Atualização:** D-1 · **Fonte:** `DB_WEBCHAT.*` (protocols, historic, first_answer, historic_messages, historic_status, historic_total, queues, users), `DB_SGD_IA.sgd_ssc_ia_chat`, `DB_SGD_ALL.sgd_ssc`
- **Métricas:** MC-022, MC-060 a MC-064, MC-030 (chat) · **Tema:** Padrão TR Clario

### Chat tempo real — `WebChat/_tempoAtendimentoChat`, `_tempoEmFilaChat`, `_tempoEntreMensagemChat`, `_tempoEsperaChat`, `_tempoFirstMensagemChat`
- **Objetivo / público:** tempos do chat em andamento e fila atual — coordenação. **Atualização:** tempo real (push, job `plug-queue-realtime` provável) · **Métricas:** MC-060 · **Tema:** variante antiga do tema (6/8 cores) — fora do padrão

### Chat IA: resolução e satisfação — `CTD/web_chat_resolucao_satisfacao` (+ `_BK`), `APOIO/web_chat_faturamento`, `(raiz)/IA Chat 1`
- **Objetivo / público:** absorção da IA, insatisfação geral e da IA, motivos, faturamento do Plug por origem; IA Chat 1 = qualificação de SSCs de chat por motivo/acesso remoto (planilha) — produto/diretoria.
- **Atualização:** D-1 (+ planilha em IA Chat 1) · **Fonte:** `DB_WEBCHAT.webchat_protocols_faturamento(_detalhes)`, `webchat_tenent`, `webchat_motivo_insatisf`
- **Métricas:** MC-062, MC-022, MC-066 · **Tema:** TR Clario, exceto `IA Chat 1` (tema base)

### Continuidade do chat — `N1/Atuais_Setembro/Continuidade chat`
- **Objetivo / público:** efetividade (simples/ajustada) das SSCs geradas no chat, por colaborador/assunto. **Fonte:** `sgd_ssc`, `sgd_alocation_historic`, `webchat_protocols`, `genesys_callsAgentsHalfHour` · **Métricas:** MC-065

### Ocorrências — `N1/Ocorrências`
- **Objetivo / público:** volume, TME/TMA, trâmites, criticidade, insatisfação de subocorrências e metas de realização por técnico/área — gestão de ocorrências; RLS por e-mail.
- **Atualização:** D-1 + planilha de votação · **Fonte:** `DB_OCORRENCIAS.*`, `DB_SGD_ALL.sgd_ssc`, `sgd_user_manager_historic`
- **Métricas:** MC-090 a MC-092, MC-024 · **Tema:** tema base (fora do padrão)

### Uso de ferramentas / IA no SSC — `APOIO/ferramentas_sscs` (cópia em Atuais_Setembro), `APOIO/cadastro_ticket`, `N1/sgd_utiliza_solucoes`, `APOIO/reescrever_ia`, `APOIO/saudacao_fone`, `APOIO/assuntos_transcricao`
- **Objetivo / público:** adoção de IA/cards/respostas prontas no cadastro de SSC, reescrita com IA, saudação padrão no fone, assuntos por transcrição — qualidade/produto e gestores.
- **Atualização:** D-1 · **Fonte:** `sgd_ssc` (`ia_register`), `sgd_ssc_pesquisa_resposta_utiliza_solucao`, `DB_SGD_IA.sgd_utilizou_reescrever_IA`, `DB_CTS.cts_config_saudacao`, `DB_GENESYS.genesys_historicCalls_ia`, `sgd_ssc_vs_genesys`
- **Métricas:** MC-100 a MC-102 · **Tema:** Padrão TR Clario

### Central de Soluções / TRIA — `CTD/TRIA_GPT` (cópia em Atuais_Setembro), `CTD/ssc-solutions-top10` (+ `_BK`), `CTD/pesquisa_solucoes`, `CTD/Soluções History` (+ `_OLD`), `CTD/atendimentos-digital`
- **Objetivo / público:** curadoria e satisfação da TRIA, top 10 SSC × soluções, termos pesquisados, tempo gasto/alterações em soluções, mix digital × humano — time CTD.
- **Atualização:** D-1 · **Fonte:** `DB_CTS.*` (tria_interactions, cts_sol_*), `sgd_ssc`, `webchat_protocols`, `genesys_queuePerformance_HalfHour`
- **Métricas:** MC-103, MC-105, MC-073, MC-024 · **Tema:** TR Clario, exceto `TRIA_GPT` e `Soluções History` (variante antiga)

### Disponibilidade de ferramentas — `APOIO/incidentes_estrategico` (+ `- Copy`, `-<máquina>`)
- **Objetivo / público:** incidentes e % de disponibilidade por plataforma (BI, chat, distribuidor, IA, SGD, telefonia/internet, Calling Card) — gestão/tecnologia.
- **Atualização:** Import de planilhas SharePoint + Postgres `DB_GENESYS` direto · **Métricas:** MC-110 · **Tema:** Padrão TR Clario

### Pessoas e escala — `N1/Horario colaboradores`, `N1/sgd_ausencias`, `N1/sgd_agenda`, `N1/Data do lançamento na agenda técnica`, `N1/sgd_hierarquia`, `N1/rev_valida_consultor`, `APOIO/acessos_remotos`, `APOIO/demanda_genesys_estratégico`, `CTD/info_clientes`
- **Objetivo / público:** quadro por horário de entrada e tempo de casa × plano; ausências; agenda do dia (tempo real via Sybase); antecedência de lançamento; hierarquia atual; liberação de revendas; uso de LogMeIn/Calling Card; requisições de telefonia; qualidade do cadastro de usuários de clientes — gestão/WFM.
- **Fonte:** `DB_REPORTS_ANALITICOS.tb_colaboradores`, `sgd_schedule*`, `TB_SYBASE_SGD_AGENDA.Agenda`, `DB_RLS.*`, `DB_LOGMEIN.logmein_sessoes`, planilhas
- **Métricas:** MC-120, MC-040, MC-041, MC-042, MC-104 · **Tema:** TR Clario, exceto `Horario colaboradores` (tema base)

### Líderes — `Metas 2026/Demanda dos Times Lideres` (+ `N1/…`, versão Plug em `Projetos_Andamento`), `N1/Time Líderes - 2026` (+ 2025)
- **Objetivo / público:** pedidos de apoio aos líderes por faixa de tempo de casa, desfecho das dúvidas no Plug (IA/escalado), vínculos de líderes em SSC e posts do Teams — liderança; RLS em `tb_demanda_lideres`.
- **Fonte:** `DB_REPORTS_CONSOLIDADOS.tb_demanda_lideres`, `DB_REPORTS_ANALITICOS.tb_interacoes_lideres_plug_analitico`, `sgd_ssc_internal_time`, planilha `Cadência de Post_Teams.xlsx`
- **Métricas:** MC-034, MC-013, MC-024

### Outros
- `N1/sgd_implantacoes` (+ 2 cópias de conflito): horas de treinamento de implantação e dados de DW via `Folder.Files` — `DB_SGD_IMPLANTACAO.*`.
- `(raiz)/Painel Geral`: página de navegação (sem dados). `APOIO/DiárioBordo_Jhonattan`: registro pessoal de tempo (planilha).

---

## Perguntas gerais para o time

1. Quais relatórios são **oficiais** para cada meta 2026 (os de `Metas de Atendimento 2026` substituem `sgd_pendencia`, `sgd_produtividade`, `sgd_satisfacao`)?
2. Definições únicas de: ligação atendida, SSC contabilizada, dia trabalhado (jornada 480 × 432 min), TME e TMA de fone e chat.
3. Insatisfação: sempre "insatisfeitos ÷ votados", pela data de conclusão, descontando desconsideradas só entre as insatisfeitas?
4. Pendência: métrica diária (MC-001) ou SSC única (MC-002)? Vale para todos os canais?
5. Listas fixas (gestores, motivos de ausência, alocações, Domínio/Inova, ids do bot) podem ir para tabelas no Postgres/Dataflow?
6. Os legados (`OLD`, `SEM USO`, `_BK`, cópias de conflito) podem ser arquivados para não serem usados como referência?
