# Tabelas Postgres de negócio — fichas

> Última atualização: 2026-09-29 · Fonte: `references/dados/postgres-{db_sgd,db_sgd_n2,db_genesys,db_webchat,db_reports_analiticos,db_reports_consolidados}.md` (colunas reais do `pg_catalog`), `references/dados/{postgres-destinos,fluxos-powerbi}.md`, código do Maestro (`orq:modules/_import_sgd/etl/domains/*.py`, `modules/historic_tb_*/sql/*.sql`), `.dados-sync/maestro.json` · **Arquivo curado** · Status: **Em revisão** (extraído de comentários/código — validar com o time)

- **Formato de cada ficha:** Significado · **Grão** (1 linha = ?) · Chaves · Colunas de negócio · Quem grava / como / frequência · Quem consome.
- **Volumes:** estimativa do planner (`reltuples`).
- **Datas:** muitas colunas de data são `varchar(10)` 'AAAA-MM-DD'. Faça cast (`::date`) e compare como data; comparação de texto só é segura no formato ISO.
- Linhagem completa em `linhagem-por-conceito.md`; conceitos em `conceitos.md`.

---

## DB_SGD · public

### `public.sgd_ssc`: SSC (chamado N1), ~20,8 mi
- **Grão:** 1 linha por SSC (`i_ssc`). `code_ssc` = `seq_revenda`, o número exibido.
- **Colunas de negócio:**
  - `date_entry`/`date_time` = abertura; `dtime` = faixa de meia hora (HH:00/HH:30)
  - `i_classification` = classificação (1 Técnica, 4 Conversão, 19 Atend.-Externo…)
  - `system`/`module`/`topic`/`subtopic` = textos já resolvidos
  - `i_means_of_access` = meio de acesso (1 Web, 2 Telefone…)
  - `lista_ss` = SS vinculadas (lista)
  - `i_clientes`
  - `i_user` = técnico responsável (`i_responsaveis`)
  - `i_user_resales` = usuário do cliente que abriu
- **Tempos** (minutos úteis, `bethadba.minutosuteis`):
  - `time_before_first_analysis`
  - `time_total` (pendente com o técnico)
  - `time_medium` (= total / nº de trâmites "aguardando resposta")
  - `time_ss`, `time_ssql`, `time_scd` (conversão)
  - `time_phone` (só meio 2)
  - `time_final_support`, `time_final_client`, `time_last_procedure_without_analysis`
  - `time_bond_sa_ne`
- **Contagens:** `total_procedures`, `total_procedures_waiting_answer` (situações 3,19), `number_procedure_conclusion`.
- **SA/NE:** `bond_sa_ne` (id SA/NE vinculada), `disapproval` (data de reprovação, situação 11).
- **Satisfação:** `satisfaction_ssc` ('Satisfeito' / 'Insatisfeito' / 'Não Opinou' / ''), `i_ssc_satisfaction_reason`.
- **Flags:** `priority`, `no_acess_system`, `ia_register` (1 = cadastrada com IA).
- **Quem grava:** `import-sgd-diario` (03:00) · `requests_sgd.sgdSearchRequests`. DELETE dos `i_ssc` relidos + INSERT; relê entrada D-5 ou `ultimo_tramite` D-5 nas situações finais.
- **⚠️ Limites:**
  - A SSC não é relida se mudar fora das situações (3,5,10,13,17,19,37,38,43) depois de 5 dias. Os tempos de SSC antigas "congelam" (inferido).
  - Não tem coluna de situação atual nem revenda; a revenda vem do cliente no Dataflow.
- **Consome:** `DB_SGD_ALL.sgd_ssc`, `sgd_ssc_answer_time`, `sgd_ssc_internal_time`; `tb_demanda_lideres` (SSC Web); `tb_ocorrencias_analitica`; view `public.vw_sgd_ssc_id_genesys`.

### `public.sgd_ssc_tramites`: trâmites de SSC, ~65,8 mi
- **Grão:** 1 linha por trâmite (`i_ssc`, `i_ssc_tramites`).
- **Colunas:**
  - `entry` (timestamp)
  - `i_ssc_situation` (situação do trâmite)
  - `i_user`
  - `tipo_resposta`, `i_visualizado`, `data_visualizacao`
  - `existe_texto_web`: '1' = situação 2 com "contato efetuado pelo time web"; '2' = contato do time chat (via extração de `requests_sgd.py:685-697`).
- **Grava:** `import-sgd-diario` · rotina historico · D3.
- **Consome:** `DB_SGD_ALL.sgd_ssc_tramites`; primeiro atendente e entrada Web no `sgd_ssc` do fluxo; `tb_demanda_lideres`.

### `public.sgd_pendency`: foto diária de SSC pendente, ~6,2 mi
- **Grão:** 1 linha por **SSC pendente × `date`** (D-1 do dia da carga).
- **Colunas:**
  - `n1_pendency`, `n2_pendency`, `sector_pendency` (1/0)
  - `i_ssc_situation`, `i_ssc_tramites` (último trâmite)
  - `i_user` (responsável)
  - `i_ss`, `i_ssql`, `i_sr`, `i_conversoes`
  - `i_meios_acesso`, `i_meios_retorno`, `i_sss_classificacoes`
  - `system`/`module`/`topic`/`subtopic`
  - `entry` (entrada da SSC)
  - `pendency_days` e `useful_pendency_days_n1/n2` (via UPDATE)
- **Grava:** `import-sgd-diario` · rotina pendency. INSERT (**acumula; duplica se rodar 2×**) + UPDATE de dias úteis via `public.calendar`.
- **⚠️ Regra N1** = "`nivel_um <> 0 and nivel_dois <> 1`", que o realtime considera errada (P-01).
- **Consome:** `DB_SGD_ALL.sgd_ssc_pendency`.

### `public.sgd_ssc_answer_time`: tempo de resposta analítico, ~16,9 mi
- **Grão:** 1 linha por SSC × usuário × evento, retornada pela procedure `relatoriotemporespostaanalitico` do dia D-1 (grão exato não documentado; inferido).
- **Colunas:** `timesupport`, `timess`, `timessql`, `timeconversao`, `timesr`, `timewithoutanalysis`, `firstprocedure` ('Sim' quando é o 1º trâmite), `datewithoutanalysis`, `datewaitinganswer`.
- **Grava:** daily · **AC** (duplica em reexecução).
- **Consome:** `DB_SGD_ALL.sgd_ssc_answer_time`.

### `public.sgd_ssc_internal_time`: tempo de resposta interna, ~1,2 mi
- **Grão:** 1 linha por pedido interno (trâmite situação 6 "AGUARDANDO RESPOSTA INTERNA" → próxima 1/7/9).
- **Colunas:** `category`, `i_userrequest`, `i_userresponsible`, `timeanswer` (minutos úteis).
- **Grava:** daily · D5.
- **Consome:** `DB_SGD_ALL.sgd_ssc_internal_time`; dataset `Internal Time` (inferido).

### `public.sgd_client`: cliente, ~249 mil
- **Grão:** 1 linha por cliente das revendas carregadas (exceto Televendas 112 e 5 clientes fixos).
- **Colunas:**
  - `i_client`, `name_client`
  - `date_register` (1º contrato dos produtos 101-104,170,174,190)
  - `date_signature`
  - `date_inactivation` (fim do último contrato com valor dos produtos 101-104,110,170)
  - `situation` (1 = cancelado)
  - `referential` ('Sim'/'Não')
  - `cep`, `city`, `initial_state`, `desc_state`, `phone`
  - `i_resale`, `name_resale`, `type_resale` (Filiais/Revendas, lista própria com 18 e 148)
  - `i_cms_responsible`, `i_cms_manager` (CSM)
- **Grava:** daily · T + DELETE pontual.
- **Consome:** `DB_SGD_ALL.sgd_client`, `sgd_ssc` (revenda da SSC); `tb_ocorrencias_analitica` (nome/cidade/estado).

### `public.sgd_product_client`: contratos, ~449 mil
- **Grão:** 1 linha por contrato (`i_contract`).
- **Colunas:** `i_product`, `i_client`, `date_register`, `date_ass_cont`, `date_ini_serv`, `date_fim_serv`, `situ_contract` (0 = ativo, segundo o sql-base; o Dataflow trata só 1 como Inativo).
- **Grava:** historico · T.
- **Consome:** `DB_SGD_ALL.sgd_client_product`.

### `public.sgd_product`: produtos, 61
- **Grão:** 1 linha por produto negociável (`permite_neg='S'`) ou produto 221.
- **Colunas:** `i_product`, `description`.
- **Grava:** daily · T.

### `public.sgd_resale`: revendas, 121
- **Colunas:** `i_resale`, `apelido`, `active`.
- **Grava:** daily · T. Não tem tipo nem região: o CASE está no Dataflow `sgd_resales`.

### `public.sgd_users`: usuários internos SGD, ~11,7 mil
- **Grão:** 1 linha por usuário interno (`terceiro=0`, com admissão, das revendas carregadas).
- **Colunas:**
  - `i_user`, `user` (login), `email` (lower), `name`
  - `admission`
  - `date_inactivation` (última auditoria "ativo=1" sem reversão), `dismission` ('0'/'1')
  - `resale`, `i_resale`, `type_resale` (Filiais/UPG/Revendas, lista com 165 e sem 18/148)
- **Grava:** daily · T.
- **Consome:**
  - `tb_colaboradores` (base)
  - `DB_SGD_ALL.sgd_users`, `sgd_client` (nome do CSM)
  - `DB_RLS.rls_user`
  - `DB_LOGMEIN`
- Cópia antiga: `DB_WEBCHAT.public.sgd_users` (sem job; inferido).

### `public.sgd_alocation_historic`: alocação por dia, ~3,4 mi
- **Grão:** 1 linha por usuário interno ativo × `date`.
- **Colunas:** `i_alocation` (vigente), `from_of` (a partir de).
- **Grava:** historico · D60 (transação).
- **Consome:**
  - quase todos os fluxos (`coalesce(i_alocation,999)`)
  - `tb_colaboradores`
  - réplica em `DB_GENESYS.public.sgd_alocations` (+ `id_user_genesys`)
  - dblink do `webchat_protocols`
- **⚠️** 60 dias de janela: alterações retroativas mais antigas não são refletidas (inferido).

### `public.sgd_alocation_reg`: cadastro de alocação, 96
- **Colunas:** `i_alocation`, `description`, `abbreviation`, `area` (int do SGD).
- **Grava:** daily · T. A área de negócio usada nos relatórios vem de `forecast.de_para_alocacao`.

### `public.sgd_user_manager_historic`: coordenador/gerente por dia, ~2,1 mi
- **Grão:** usuário × `date`.
- **Colunas:**
  - `i_historic`, `from_of`
  - `i_superv` + `superv` (gestor imediato = coordenador)
  - `manager` (gestor do gestor = gerente)
  - `responsible_alter`, `date_alter`
- **Grava:** historico · D365.
- **Consome:**
  - `DB_SGD_ALL.sgd_user_manager_historic` (normaliza nomes e deriva `unity`)
  - `tb_colaboradores.supervisor/gerente`
  - `DB_LOGMEIN`

### `public.sgd_user_cargo_historico` (~3,1 mi) / `public.sgd_cargos` (160)
- **Grão:** usuário × `data_dia` desde 2024-01-01.
- **Colunas:** `i_cargo_historico` (= i_cargos), `a_partir_de`. Cadastro: `i_cargo`, `descricao`, `ativo`.
- **Grava:** daily · T (as duas).
- **Consome:** `tb_colaboradores.id_cargo/descricao_cargo`; `DB_SGD_ALL.sgd_user_position_historic`, `sgd_cargos`.

### `public.sgd_horario_historic`: jornada vigente por dia, ~30 mil
- **Colunas:** `horario_inicio/fim_matutino/vespertino`, `vigencia`, `i_responsavel_lancto`.
- **Grava:** historico · D15. ⚠️ O SQL tem data fixa ≥ 2026-08-01, então **não há histórico anterior**.

### `public.sgd_schedule` (~4,6 mi) / `sgd_schedule_past_future` (~2,3 mi) / `sgd_schedule_three_days` (~4,6 mi)
- **Grão:** 1 linha por data × usuário × tipo (`i_type`) × motivo (`i_absences_reason`), com `minutes`.
- **Colunas:** `responsible`, `description`, `data_hora_ini/fim`.
- **Motivo 0:** linha sintética de tempo trabalhado ("480 - minutos da agenda do GESTOR…", ver `conceitos.md` §6.1).
- **Grava:** `import-agendas` (03:05): passado D60 / futuro +90 / últimos dias úteis.
- **⚠️** O D60 apaga o futuro de `sgd_schedule` (dívida documentada).
- **Consome:** `DB_SGD_ALL.sgd_schedule*` (recalcula minutos); `tb_demanda_lideres.dias_trabalhados`; `tb_ocorrencias_analitica` (temps não usadas).

### `public.sgd_ocorrencia`: ocorrência, ~26,6 mil
- **Grão:** 1 linha por ocorrência (`i_ocorrencia`). `tipo` 1 = principal, 2 = subocorrência (`i_ocorrencia_pai`).
- **Colunas:**
  - áreas/setores de origem e destino, `i_categoria`, `i_situacao` (5 = fechada, inferido)
  - `i_responsavel`, `i_usuario`, `i_clientes`, `i_revendas`, `ultimo_tramite`
  - `entrada_email`/`resposta_email` (extraídos do HTML)
  - `tme_minutos`, `tma_total_minutos`, `tma_sub_minutos`
- **Grava:** rotina ocorrencias: DELETE abertas + fechadas dos últimos 7 dias, depois INSERT; 6 UPDATEs corretivos.
- **Consome:** `DB_OCORRENCIAS.sgd_ocorrencia`; `tb_ocorrencias_analitica`.

### `public.sgd_ocorrencia_tramite` (~193 mil) / `_tramite_time` (~252 mil)
- **Grão:** 1 linha por trâmite (`i_tram`). `date_tram` é varchar(19) com data e hora.
- **Tempo:** `tempo` = minutos úteis até o próximo trâmite (Python).
- **Grava:** D1 (UNION trâmite + anotação) / T (PG).

### `public.goals`: metas, ~260 mil
- **Grão:** 1 linha por e-mail × competência (`compini`..`compfim`, 'AAAA-MM' ou 'AAAA-MM-DD') × `descmeta`.
- **Colunas:** `valormeta`; `meta_at`, `meta_folha`, `meta_fiscont` (aba RegionalSUL).
- **Grava:** `import-sgd-diario` e `import-sgd-meiodia` (TRUNCATE + 5 abas).
- **Consome:** `DB_METAS.goals` (expande por dia); `tb_demanda_lideres.valormeta`.
- **⚠️** Há linhas repetidas exatas (`demanda.sql:12`).

### `public.calendar`: calendário, ~1,8 mil
- **Grão:** 1 linha por data.
- **Colunas:**
  - `day_of_week` (1 = domingo, 7 = sábado; inferido de `NOT IN (1,7)`)
  - `holiday` (≠ '' = feriado)
  - `day_useful_month`/`day_useful_year` (nº do dia útil; nulo = não útil, inferido)
  - `ten`/`ten_name` (dezena)
  - `fone_/chat_{folha,fiscont,at}_seq_deman` (sequência de demanda por área e canal; semântica não documentada)
- **Grava:** **ninguém no Maestro** ("mantida por fora").
- **Consome:** `sgd_pendency` (dias úteis), `import-agendas`, `minutos_uteis` (feriados), `tb_colaboradores`, `DB_METAS`, `forecast_*`, `DB_SGD_ALL.calendar`.

### `public.sgd_genesys`: SSC × ligação Genesys, ~1,3 mi
- **Grão:** 1 linha por SSC com ligação.
- **Colunas:** `conversation_id`, `id_ligacao`, `id_transcricao_anexo`, `cadastro_ia`, `tags`.
- **Grava:** daily. ON CONFLICT (i_ssc) DO NOTHING: nunca atualiza a linha.
- **Consome:** `DB_SGD_ALL.sgd_ssc_vs_genesys`; view `vw_sgd_ssc_id_genesys` → `DB_GENESYS.sgd_ssc_genesys`.

### `public.sgd_ssc_disregard_dissatisfaction`: insatisfações desconsideradas (mestre), ~631
- **Grão:** 1 linha por item desconsiderado.
- **Colunas:** `i_response`, `i_ssc_ss_chat` (id da SSC, SS ou protocolo), `type` ('SSC'/'SS'/'CHAT'), `justif`, `date_incl`, `email`.
- **Grava:** a mestre em si (origem não identificada no código lido: formulário?). `disregard.disregardDissatisfaction` deduplica e replica (T) para DB_SGD_N2 e `DB_WEBCHAT.public.disregard_dissatisfaction`. O consumidor SS vai para `ss.ss_disregard_dissatisfaction`.
- **Consome:** flags `disregarddissatisfaction` em `sgd_ssc`, `sgd_ss` e `webchat_protocols`.

### `forecast.*` (DB_SGD)
- **`client_user_history`** (~76 mi): 1 linha por mês × cliente × contrato × produto principal. `totusers` = usuários contratados (entradas − saídas); o Dataflow troca 0 por 1. **AC** diário.
- **`de_para_alocacao`** (96): alocação → `area`, `meio_acesso_alocacao`. Planilha, T.
- **`demanda_projetada`:** `_data` × `regional` × `area` com demanda fone/web/chat. Planilha, T.
- **`tme_projetado`:** `year`, `ini`, `fim`, `seg`, `setor`, `canal`. Planilha, T.
- **`fte_aprovado`, `produtividade_media`, `ajuste_demanda`:** `ini`/`fim` (mês) × `area` × `gerente`. Planilha, T.
- **`ausencias_projetado`:** `ini`/`fim` × `area` × `tipo` × `reg` (Sul/Campinas). Planilha, T.
- **`users`:** `date_month`, `tot_sc`, `tot_sp`. SC/SP não documentados (inferido: Santa Catarina / São Paulo?).
- **Congeladas:** `projetado`, `coefficient`, `calls`.

### `suporte.dados_teams_sul`: pedidos de ajuda (Teams Sul), ~49 mil
- **PK:** `auxiliar`.
- **Colunas:** `equipe_teams`, `canal_teams`, `email_ajuda`, `email_lider`, `quem_pediu_ajuda`, `quem_respondeu`, `tempo_reacao`…
- **Grava:** `excel.main_teams_sul` (UPSERT), mas **órfã** (nenhuma rotina a chama). O dado pode estar parado.
- **Consome:** `DB_SUL_INTERNO.dados_teams_sul`.

## DB_SGD_N2 · ss

### `ss.ss`: SS (N2), ~499 mil
- **Grão:** 1 linha por SS.
- **Colunas:** `date_entry`, `i_classification`, `i_system`/`i_module`/`i_topc`/`i_subtopic`, `i_satisfaction`, `i_dissatisfied_reason`, `i_userreasales`, `i_resales`, `i_situacao` (situação atual), `last_update`.
- **Grava:** rotina ss · ID janela 31 d por `ultimo_tramite`.
- **Consome:** `DB_SGD_ALL.sgd_ss`, `sgd_ss_forwarding`, `sgd_ss_pendency`.

### `ss.ss_tramites` (~3,8 mi) / `ss.ss_tramites_time` (~4,3 mi)
- **Grão:** 1 por trâmite (`i_ss`, `i_ss_tram`).
- **Colunas:** `situation`, `i_user`, `typeforwarding`, `dateanalysisforwarding`, `i_userforwarding`, `exists_requestsql`, `i_category`, `sla_interacao`/`sla_n3`/`sla_tme` (texto de intervalo).
- **Tempo:** `time` = minutos úteis do trâmite.
- **Grava:** D5 / T (PG).

### `ss.ss_pendency`: foto diária de SS pendente, ~2,6 mi
- **Grão:** SS × `ddate` (+ `ddatetime`).
- **Colunas:** `i_ss_situation`, `description_situation`, `pending` (DV / DV INT / GP / TI / PAR / N1 / N2).
- **Grava:** rotina ss · **AC** (PG).
- **Consome:** `DB_SGD_ALL.sgd_ss_pendency` (≥ 2023-01-01).
- Tabelas legadas no `public` do DB_SGD_N2 (`SGD_SS_Pendency*`) não têm job.

### `ss.ss_situation` (38)
- **Colunas:** `i_situation`, `description`, `pending` (área dona da pendência; mapa diferente do `ss_pendency`, ver `conceitos.md` §4.2).

## DB_REPORTS_ANALITICOS · public

### `tb_colaboradores`: colaborador por dia, ~4,9 mi
- **Grão:** (data, id_usuario_sgd). Há duplicatas conhecidas (~71 usuários/dia).
- **Colunas:**
  - `ususrio_sgd` (sic), `email`, `nome`
  - `data_admissao`, `tempo_casa_dias/meses/anos`
  - `data_inativacao`/`demissao` (preenchidas só no dia da inativação)
  - `resale`, `id_resale`, `tipo_resale`, `descricao_resale`
  - `id_usuario_genesys`, `status_genesys`, `jabber_id`
  - `i_alocation`, `desde`, `descricao`/`abreviacao` (alocação)
  - `id_cargo`, `descricao_cargo`
  - `id_supervisor`/`supervisor` (coordenador), `gerente`
  - `id_chat`, `atibuicao_chat` (sic), `tenant_id`
  - horários matutino/vespertino
- **Grava:** `historic-tb-colaboradores` (06:11): DELETE por data + INSERT (dblink).
- **Consome:** Dataflow `DB_REPORTS_ANALITICOS.tb_colaboradores`, `tb_ocorrencias_analitica`, `tb_demanda_lideres`, `tb_interacoes_lideres_plug_analitico`, `plug-status-realtime`.
- **Uso recomendado:** partir desta tabela para indicadores de colaborador por dia (`sgd-regras-e-joins.md` §5).

### `tb_ocorrencias_analitica`: trâmite de ocorrência enriquecido, ~229 mil
- **Grão:** 1 linha por trâmite (chave real `(i_ocorrencia, i_tram)`), com "40% da tabela é fan-out de join" (via extração do skills.md do módulo).
- **Colunas:**
  - `ordem_tramite`, `tempo_tramite_seg` (segundos corridos, não úteis)
  - `id_situacao_tramite`/`descricao_situacao_tramite`
  - `votacao`/`motivo` (satisfação da subocorrência)
  - todas as colunas de `sgd_ocorrencia`, descrições de área/setor/categoria/prioridade
  - cliente (nome, cidade, estado)
  - cadastro do colaborador do dia (`tb_colaboradores`)
- **Grava:** `historic-tb-ocorrencias-analitica` (08:00, D-30): DELETE por período + INSERT, com guarda anti-wipe.
- **Consome:** Dataflow `DB_REPORTS_ANALITICOS.tb_ocorrencias_analitica`.

### `tb_interacoes_lideres_plug_analitico`: interação de líder no Plug, ~429 mil
- **Grão:** 1 linha por interação (`_id`) do tenant "TR Atendimento Líderes".
- **Colunas:** `lider`/`coordenador_lider`/`gerente_lider`, `tecnico`/`coordenador_tecnico`/`gerente_tecnico` (técnico = `id_client / 1000`), `modulo`/`descricao_modulo`/`descricao_sistema`, `rating`, `id_motiv_insatisf`, `issc`.
- **Grava:** `historic-tb-interacoes-lideres-plug` (07:20, 3 dias).
- **⚠️** "Só ~45% das interações acham o líder" (via extração).

### `tb_meta_capacidade_atendimento`: meta de capacidade, 120
- **Grão:** cargo × `setor` × `acesso` × faixa `tempo_casa_min/max_meses`, com `meta_maxima_atendimento`.
- **Grava:** **não mapeado** (manual/planilha?).
- **Consome:** `tb_demanda_lideres`; Dataflow.

### `tb_satisfacao_subocorrencias` (~1,6 mil)
- **Colunas:** `subocorrencia`, `votacao`, `motivo`.
- **Grava:** "entrada externa ao Maestro … nenhum ETL da casa a escreve".

## DB_REPORTS_CONSOLIDADOS · public

### `tb_demanda_lideres`: consolidado diário por colaborador Filiais, ~663 mil
- **Grão:** data × colaborador (`email`).
- **Colunas:**
  - `area`/`abreviacao_area` (alocação), `cargo`, `coordenador`, `gerente`, `anos_empresa`
  - `ligacoes` (inbound atendidas)
  - `dias_trabalhados` (fração de 480 min)
  - `total_ssc` (SSC Web)
  - `meta_maxima_atendimento`, `valormeta`
  - `pedido_ajuda`, `total_lider`, `atendimento_chat`
- **Grava:** `historic-tb-interacoes-lideres-plug` (07:20): DELETE por período + INSERT.
- **Consome:** Dataflow `DB_REPORTS_CONSOLIDADOS.tb_demanda_lideres`.
- **⚠️** "Reprocessar dias antigos traz o valor **atual** da origem" (via extração).

### Tabelas **sem job conhecido** (fonte a confirmar)
- **`produtividade_n1`** (~1,9 mi, PK id): 1 linha por trâmite de SSC/SS (`tipo`, `unidade`, `sistema`, `modulo`, `classificacao`, `topico`, `numero_ss`, `numero_ssc`, `numero_tramite`, `situacao_tramite`, `data_tramite`, `responsavel_tr`, `data_importacao`).
- **`produtividade_n2`** (~391 mil): idem para SS (`responsavel_tramite` texto).
- **`pendencias_suporte`** (~5,6 mil, PK id): SSC/SS com `pendente_n1/n2/n3` e datas de pendência, `data_insercao`/`data_atualizacao`. É um estado atual, com upsert (inferido).
- **`sla_pendency_time_snapshot`** (~389 mil, PK `data_snapshot, i_ss, sequential_iteraction`): foto do tempo por interação N2.
- **`tempo_tramite_interno`** (~99 mil): pedidos internos de SS com analista solicitante/respondente, categoria e `tempo_resposta_interna`.
- **`jornada_fte`** / **`jornada_fte_etapas`:** fluxo de vagas/FTE (formulário: `data_resposta`, `acao`, `tipo_vaga`, `etapa`, `sla_etapa`…).
- **`chains_ia`** (~432 mil): uso de chains de IA.
- **`backup_nuvem`** (~53 mil, PK i_clientes): último backup completo por cliente.

## DB_GENESYS · public (principais)

| Tabela | Grão / significado | Grava |
|---|---|---|
| `historic_callsAgents` (~7,8 mi, 11 GB) | 1 linha por conversa × agente/sessão. Métricas `metric_t*`/`n*` em ms; `direction`, `queue_id`, `skill_id_1/2`, `survey_id` | `genesys-import` (D-1, DELETE+INSERT) + `produtividade-pendencia-realtime` (dia corrente) |
| `historic_callsAbandoned` | 1 por ligação abandonada (`metric_tAbandon`, `_ani`) | `genesys-import` |
| `historic_qualifications` | skill × intervalo (SLA: `metric_oServiceLevel`, `nOffered`, `nAbandon`, `tAbandon60..More600`) | `genesys-import` + `genesys-sla` |
| `agentAvailable` (~40 mi) | agente × dia × meia hora, com tempo em cada status | `genesys-import` |
| `HistoricAgentStatus` (~16,6 mi) | intervalos de presença | `genesys-import` |
| `queue` / `skills` | cadastro de filas/skills (`area`, `regional`, `region`); filas antigas mantidas | `genesys-import` (UPSERT) |
| `users_Genesys` / `users_SGD` | agentes da divisão / usuários SGD casados por e-mail | `genesys-import` (T) |
| `sgd_alocations` / `cad_alocations` | réplica da alocação diária SGD + `id_user_genesys` | `import-sgd-diario` |
| `survey` | respostas (`survey_id`, `question_id`, `answer_id`) | `genesys-import` / realtime |
| `callsWithClient` | conversa × cliente SGD | `genesys-import` (30 d) |

## DB_WEBCHAT · public (principais)

| Tabela | Grão / significado | Grava |
|---|---|---|
| `protocols` (~2,6 mi) | 1 linha por protocolo de chat: `initialqueue`, `rating` ('0'/'1'), `ratingdesc`, `id_motv_insatisf`, `duration`, `id_client`, `i_ssc`, `tenant_id`, `grupo_atend` | `plug-queue-realtime` (DELETE dia + INSERT) |
| `protocols_history` (~5,8 mi) | trechos do protocolo por fila/ator (`queuegroup`, `actor`, `seconds`, `transfer`) | **sem job** |
| `protocols_sequence_message` (~112 mi) | mensagens/eventos (`type`, `actor`, `integrated_id`, `details`) | **sem job** |
| `protocols_all` (~2,2 mi) / view `vw_protocolos_all` | protocolos de todas as origens (IA/humano/bot) para faturamento | **sem job** |
| `users` / `users_historicstatus` | atendentes do chat (`i_user_sgd`, `tenant_id`) / histórico de status | **sem job** |
| `tenant_id` (17) | tenants (Suporte, Líderes, revendas parceiras) | **sem job** |
| `protocols_ia` | classificação por IA | `insights-realtime` |
