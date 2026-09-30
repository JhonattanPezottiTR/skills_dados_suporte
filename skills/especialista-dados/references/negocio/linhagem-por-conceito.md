# Linhagem por conceito — Sybase → carga → Postgres → Dataflow → relatório

> Última atualização: 2026-09-29 · Fonte: Maestro (`orq:modules/_import_sgd/catalog.py`, `etl/rotinas.py`, `etl/domains/*.py`, `modules/historic_tb_*/sql/*.sql`, `modules/*/skills.md`, `modules/produtividade_pendencia_realtime/sql/queries.sql`), `.dados-sync/maestro.json` (notas de carga), `references/dados/{linhagem,postgres-destinos,fluxos-maestro,fluxos-powerbi,fluxo-*}.md`, `references/powerbi/{catalogo-relatorios,servico-powerbi}.md`, projetos legados irmãos · **Arquivo curado** · Status: **Em revisão** (extraído de comentários/código — validar com o time)

**Legenda**
- **Carga (o COMO):**
  - `T` = TRUNCATE+INSERT (recarga total, em geral numa transação);
  - `Dn` = DELETE da janela de n dias + INSERT;
  - `ID` = DELETE dos ids relidos + INSERT (upsert por id);
  - `AC` = INSERT sem limpeza (acumula; **duplica se rodar 2× no dia**);
  - `UP` = UPDATE no lugar;
  - `UPSERT` = ON CONFLICT / MERGE;
  - `PG` = derivada de outra tabela Postgres (SQL ou dblink).
- **Jobs e agendas** (cron, America/Sao_Paulo; `dados-fluxos-maestro.md`):

| Job | Agenda |
|---|---|
| `import-sgd-diario` | 03:00 |
| `import-sgd-meiodia` | 12:00 |
| `import-sgd-observacoes` | sábado 08:00 |
| `import-agendas` | 03:05 |
| `genesys-import` | 03:15 |
| `import-cts` | 05:30 |
| `historic-tb-colaboradores` | 06:11 |
| `import-logmein` | 06:40 |
| `historic-tb-interacoes-lideres-plug` | 07:20 |
| `historic-tb-ocorrencias-analitica` | 08:00 |

  Os realtime rodam em janela (07:55–18:30 etc.).
- **Rotinas do `import-sgd-diario`:** `daily` roda primeiro; em seguida, em paralelo, `ss`, `historico`, `ocorrencias`, `pendency`, `chain_ia`, `sa_ne_genesys_forecast`, `implantacao` e `metas` (`orq:modules/_import_sgd/etl/rotinas.py:550-560`, via extração). "`daily` é **pré-requisito** de `ss` e `historico`" (`rotinas.py:20`).
- **Universo de revendas** das consultas Sybase = `REG_*` + `REVENDAS_COM18` (ver `conceitos.md` §1.3).
- ⚠️ O `enabled` do `spec.yaml` pode estar `false` e ser sobrescrito na tela do Maestro (`fluxos-maestro.md:6`).

---

## 1. SSC (chamado N1)

| Etapa | Detalhe |
|---|---|
| **Sybase** | `bethadba.vw_ssc` (i_ssc, seq_revenda, entrada, ultimo_tramite, i_ssc_situacoes, i_sss_classificacoes, i_meios_acesso, i_clientes, i_responsaveis, i_revendas, i_ss, i_ssql, i_sr, i_conversoes, i_forum_sa, satisfacao, prioridade…) + `vw_ssc_tramites`, `vw_sistemas`, `vw_modulos`, `vw_topicos_suportes`, `vw_ssc_origens`, `vw_ss*`, `vw_ssql*`, `vw_conversoes`, `vw_conversao_tramites`, `vw_ssc_ss`, `vw_ssc_ssql`, `vw_ssc_conversoes`, UDF `bethadba.minutosuteis` |
| **Carga** | `import-sgd-diario` · rotina `daily` · `requests_sgd.sgdSearchRequests`. **ID**: "`DELETE FROM public.sgd_ssc WHERE i_ssc IN(…)`" + INSERT (`orq:…/requests_sgd.py:554-562`). Relê as SSC com entrada nos últimos 5 dias **ou** com situação (3,5,10,13,17,19,37,38,43) e `ultimo_tramite` nos últimos 5 dias (`requests_sgd.py:537-539`). O parâmetro se chama `ninety_days`, mas recebe 5 dias (`rotinas.py:163`, via extração). |
| **Postgres** | `DB_SGD.public.sgd_ssc`: 1 linha por SSC, com os tempos (minutos úteis) já calculados, `satisfaction_ssc`, `ia_register`, `dtime` (meia hora) |
| **Dataflow** | `DB_SGD_ALL.sgd_ssc` (entrada ≥ 2024-01-01; junta `sgd_client`, `sgd_alocation_historic`, `sgd_ssc_tramites`, `sgd_ssc_disregard_dissatisfaction`) |
| **Relatórios** | datasets do Dominio FLOWS `Satisfaction`, `Productivity`, `Response Time` (inferido pelo nome, `servico-powerbi.md:37-44`); `tb_demanda_lideres.total_ssc` |

**Tabelas-satélite da SSC**

| Tabela | Sybase | Função | Carga | Dataflow |
|---|---|---|---|---|
| `sgd_ssc_tramites` | `vw_ssc_tramites` | `sgdSscTramites` (rotina historico) | D3 | `DB_SGD_ALL.sgd_ssc_tramites` |
| `sgd_ssc_answer_time` | proc `bethadba.relatoriotemporespostaanalitico` | `sgdSscTimeAnswered` (daily) | **AC** D-1 (duplica em reexecução) | `sgd_ssc_answer_time` |
| `sgd_ssc_internal_time` | trâmites 6 → (1,7,9) | `sgdSscTimeInternal` | D5 | `sgd_ssc_internal_time` |
| `sgd_ssc_text_conclusion` | trâmite situação 5, satisfeitos | `sgdSearchTextConclusion` | D5 | `sgd_ssc_text_conclusion` |
| `sgd_ssc_dissatisfaction_historic` | `vw_ssc` situação 5 | `sgdSearchRequestsReasonDissatisfaction` | D30 | idem |
| `sgd_ssc_situation` / `sgd_ssc_classification` | `vw_ssc_situacoes` / `vw_sss_classificacoes` | cadastros | T | idem |
| `sgd_ssc_utiliza_solucao` | `vw_ssc_pesquisa_resposta_utiliza_solucao` | `pesquisaSolucao` | D5 | `sgd_ssc_pesquisa_resposta_utiliza_solucao` |
| `sgd_ssc_ia_chat` | `vw_completion_ai_ssc_chat` | `sgdSearchSSC_IA_CHAT` | D5 | `DB_SGD_IA.sgd_ssc_ia_chat` |
| `sgd_ssc_reescrever_ia` | `vw_confg_fluxo_acao_open_arena_interacao` (i_confg_fluxo_acao=1) | `utilizaReescreverIA` | D5 | `DB_SGD_IA.sgd_utilizou_reescrever_IA` |
| `sgd_genesys` | `vw_ssc.codigo_ligacao_genesys` | `sgdSearchSSC_GENESYS` | "INSERT ... ON CONFLICT (i_ssc) DO NOTHING" (nunca atualiza) | `sgd_ssc_vs_genesys` |
| `DB_GENESYS.sgd_ssc_genesys` | PG: view `DB_SGD.public.vw_sgd_ssc_id_genesys` | `sgdSearchSSC_GENESYStoSGD` | T | — |
| `sgd_soses` | `vw_ssc_dados_faturamentos`, `vw_ssc_tipos_servicos_soses`, `vw_soses_situacoes`, `vw_dado_relatorio_sose` | `sgdSSCsSoses` | T (entrada ≥ 2022-01-01) | `sgd_ssc_soses` |
| `sgd_ssc_sa` | sgsai `vw_forum_sa` + `vw_ssc.i_forum_sa` | `sgsai.saNeRequest` | T | `sgd_ssc_sa` |
| `sgd_ssc_ss` | — | **não mapeado** (sem job) | ? | `sgd_ssc_ss` |
| `sgd_ssc_reason_dissatisfaction` | — | **não mapeado** | ? | `sgd_ssc_reason_dissatisfaction` |
| `DB_CTS.sgd_request` | `vw_ssc` (todas as revendas) | `cts.requisicoes.sgdSsc` (import-cts) | D180 | — |

## 2. Pendência de SSC (N1/N2/setor)

| Caminho | Sybase | Carga | Postgres | Consumo |
|---|---|---|---|---|
| **Batch D-1** | `vw_ssc` com `situacao_pendente_nivel_um/dois`, último trâmite via `vw_ssc_tramites` | `import-sgd-diario` · rotina `pendency` · `sgdSscPendency` = **AC** (foto de ontem, `dDate = '{yestarday}'`); depois `sgdSscPendencyDiasUteis` = **UP** dos dias úteis via `public.calendar` (1 dia por chamada; rotina `dias_uteis` = backfill de 490 dias sob demanda) | `DB_SGD.public.sgd_pendency`: 1 linha por **SSC pendente × dia** | `DB_SGD_ALL.sgd_ssc_pendency`; dataset `Pendency` (inferido) |
| **Tempo real** | `vw_ssc` + UDFs `f_get_gestor_suporte`, `f_get_tempo_pendente_SSC`, `minutosUteis` | `produtividade-pendencia-realtime` (07:55–18:30, ~60 s): T por ciclo | `DB_SGD.temp."_sgdPendency"` (snapshot) + push | push `_sgdPendency` → relatório `_sgdPendency`; Cockpit `sgd_pendencia` |
| **Consolidado** | ? | **não mapeado no Maestro** | `DB_REPORTS_CONSOLIDADOS.public.pendencias_suporte` (`pendente_n1/n2/n3`, `data_insercao/atualizacao`) | `DB_REPORTS_CONSOLIDADOS.pendencias_suporte` |

⚠️ O batch e o realtime usam **regras N1 diferentes** (ver `conceitos.md` §5.1 e P-01). O legado `analytics_bi_dominio-import-sgd-pendencias` grava o **mesmo** snapshot na mesma tabela; se ainda estiver agendado, duplica (P-05).

## 3. SS (N2) e pendência de SS

| Etapa | Detalhe |
|---|---|
| **Sybase** | `vw_ss` (situacao, i_sistemas, ultimo_tramite), `vw_ss_tramites` (sla_interacao, sla_n3, sla_tme…), `vw_ss_situacoes`, `vw_ss_categorias`, cadastros `vw_sistemas`/`vw_modulos`/`vw_topicos_suportes`/`vw_ssc_origens`/`vw_sss_classificacoes` |
| **Carga** | `import-sgd-diario` · rotina `ss` (**depois** da `daily`, que produz o disregard). Tarefas: `ss_n2.sgdSearchRequests` = **ID**, janela `SS_DIAS` (default 31; "absorveu a antiga rotina ss_backfill"); `sgdSsTramites` = D5; `sgdSearchTextConclusion` = D5; cadastros = T; `sgdSSTimeN2` = PG T (minutos úteis por trâmite, Python); `sgdSsPendencyPostgres` = **AC** (PG, lê `ss.ss`, `ss.calendar`, `ss.ss_tramites`, `ss.ss_situation`) |
| **Postgres** | `DB_SGD_N2.ss.ss` (1 linha por SS), `ss.ss_tramites` (1 por trâmite), `ss.ss_tramites_time`, `ss.ss_pendency` (1 por SS × dia), `ss.ss_situation.pending` |
| **Dataflow** | `DB_SGD_ALL.sgd_ss`, `sgd_ss_tramite`, `sgd_ss_forwarding`, `sgd_ss_pendency` (≥ 2023-01-01), `sgd_ss_pendency_time` (SQL longo de agrupamento de interações N2), `sgd_ss_situation`, `sgd_ss_category`, `sgd_ss_classification`, `sgd_ss_dissatisfied_*` |
| **Tempo real** | push `POWER_BI_PUSH_URL_PENDENCY_N2` / `ENTRY_N2` (`produtividade-pendencia-realtime`) |
| **Snapshot SLA** | `DB_REPORTS_CONSOLIDADOS.public.sla_pendency_time_snapshot` (PK data_snapshot, i_ss, sequential_iteraction). Mesmo formato de `sgd_ss_pendency_time` + `data_snapshot`/`processado_em`. **Não mapeado no Maestro.** Hipótese (inferido): foto diária da entidade do fluxo |
| **Produtividade N2** | `DB_REPORTS_CONSOLIDADOS.public.produtividade_n2` (1 linha por trâmite de SS: tipo, unidade, sistema…, situacao_tramite, responsavel_tramite) e `tempo_tramite_interno`. **Não mapeados** |
| Sem job | `ss.ss_dissatisfied_reason`, `ss.ss_satisfaction_description`, `ss.ultimo_backup_bkn` (→ `DB_SGD_ALL.sgd_bkn_last_backup`) |

## 4. Cliente, contrato, produto, revenda

| Conceito | Sybase | Carga (função · rotina · como) | Postgres (grão) | Dataflow |
|---|---|---|---|---|
| Cliente | `vw_geclientes`, `vw_revendas` (join por `i_representantes`, `ativa=1`, ≠112), `vw_cmcontratos`, `vw_gecidades`, `vw_geestados`, `vw_geclientes_observacoes` | `clients_sgd.sgdSearchClients` · daily · **T** + "DELETE pontual (i_client=2998/i_resale=86)" | `DB_SGD.public.sgd_client` (1/cliente) | `DB_SGD_ALL.sgd_client` (+ observação, + `exist_web_chat` via dblink DB_WEBCHAT) |
| Observação | `vw_geclientes_observacoes` | `sgdObservation` · `import-sgd-observacoes` (sábado) · **T** "~1-2 h", "view sem data de alteração" | `sgd_client_observ` | dentro de `sgd_client` |
| Contatos/telefones | `vw_geclientes`, `vw_geclientes_contatos_adicionais` | `sgdDateClientesContacts` · daily · T | `sgd_client_contact` (1/telefone) | `sgd_client_phone`; usado para achar o cliente de ligação abandonada (`temp."SGD_ClientContact"`, sem job) |
| Contrato × produto | `vw_cmcontratos` × `vw_geclientes` × `vw_revendas` | `sgdSearchProduct` · historico · T | `sgd_product_client` (1/contrato) | `sgd_client_product` |
| Produto | `vw_ceprodutos` (`permite_neg='S' or i_produtos=221`) | `forecast.sgdProduct` · daily · T | `sgd_product` | `sgd_product` |
| Usuários do cliente | `power_bi.vw_usuarios` (`i_clientes` não nulo, `terceiro=0`) + `vw_usuarios_informacoes_adicionais`, `vw_usuarios_dados` | `sgdSearchUsersClient` · daily · T | `sgd_user_client` | `sgd_client_user` |
| Usuários contratados por mês | `vw_cmcontratos`, `vw_cmcontratos_hist_usuarios`, `vw_geclientes` (produtos 101-104,170,211-213; `vlr_contrato > 0`) | `forecast.sgdUsersAlter` · sa_ne_genesys_forecast · **AC** | `DB_SGD.forecast.client_user_history` (~76 mi linhas) | `forecast_client_user_history` |
| Revenda | `vw_revendas` | `sgdSearchResales` · daily · T | `sgd_resale` | `DB_SGD_ALL.sgd_resales` (CASEs de tipo/região/agrupado); `DB_RLS.rls_user` |
| Clientes liberados no chat | ? | **não mapeado** | `DB_WEBCHAT.public.sgd_cli_liberados_chat` | `DB_WEBCHAT.sgd_clients_control_chat` |
| Backup nuvem | ? | **não mapeado** | `DB_REPORTS_CONSOLIDADOS.public.backup_nuvem` (PK i_clientes) | `backup_nuvem` |

Cópia CTS: `DB_CTS.public."SGD_Client"` (`cts.cadastros.sgdSearchClients`, T), com outra lista de produtos para data de cadastro (101,102,103,104,110,170; `legado:analytics_bi_dominio-cts-import/sgd_cadastros.py:22`, via extração).

## 5. Colaborador (usuário interno) e suas dimensões históricas

| Conceito | Sybase | Carga | Postgres (grão) | Dataflow |
|---|---|---|---|---|
| Usuário SGD | `power_bi.vw_usuarios` (`terceiro=0`, `admissao not null`, ≠1280525) + `vw_usuarios_dados`, `vw_usuarios_auditoria`, `vw_revendas` | `clients_sgd.insertUsersSGD` · daily · **T** | `DB_SGD.public.sgd_users` (1/usuário; `type_resale` Filiais/UPG/Revendas) | `DB_SGD_ALL.sgd_users` (BOT-IA), `DB_RLS.rls_user`, `DB_LOGMEIN` |
| Alocação (histórico) | `vw_usuarios_alocacao_historico` (+ auditoria para ativo) | `sgdSearchAlocations` · historico · **D60** numa transação; depois T em `DB_GENESYS.public.sgd_alocations` / `cad_alocations` + UPDATE `id_user_genesys` por e-mail (`users_Genesys` × `users_SGD`) | `sgd_alocation_historic` (1 por usuário × dia) | `DB_SGD_ALL.sgd_alocation_historic` (≥ 2024-01-01) e junções em quase todo fluxo (`coalesce(…,999)`); `DB_GENESYS.*` via `sgd_alocations`; `DB_WEBCHAT.webchat_protocols` via **dblink** |
| Cadastro de alocação | `vw_alocacao` | `sgdSearchCadAlocations` · daily · T ("lida pela rotina historico → precisa rodar antes") | `sgd_alocation_reg` | `DB_SGD_ALL.sgd_alocation_reg` (+ área/meio de acesso de `forecast.de_para_alocacao`, + linha 999) |
| Área por alocação | planilha Forecast.xlsx, aba DeParaAreaAlocacao | `forecast.insertForecastDeParaAlocation` · sa_ne_genesys_forecast + meiodia · T (após `cleanForecast`) | `forecast.de_para_alocacao` | `forecast_de_para_alocacao_area`, `sgd_alocation_reg`; `genesys-sla` copia para `DB_GENESYS.temp.sgd_alocation_reg` |
| Alocação (realtime voz) | `vw_usuarios_alocacao_historico` (RANK último), `vw_alocacao` | `genesys-sla` · `sync_allocation` a cada ~5 ciclos · T atômico | `DB_GENESYS.temp.alocation`, `temp.sgd_alocation_reg` | lidos por `genesys-status-agents-realtime` |
| Gestor (coord./gerente) | `vw_usuarios_gestor_historico` + `power_bi.vw_usuarios` | `sgdSearchAlterManager` · historico · **D365** | `sgd_user_manager_historic` (1 por usuário × dia: `i_superv`, `superv`, `manager`) | `DB_SGD_ALL.sgd_user_manager_historic` (normaliza nomes + `unity` pelo nome do gerente + linha sintética de D-1) |
| Cargo | `vw_cargos`; `vw_usuarios_cargo_historico` | `insertCargos` (T) e `insertHistoricoCargos` (T, 1 linha/dia desde 2024-01-01) · daily | `sgd_cargos`, `sgd_user_cargo_historico` | `sgd_cargos`, `sgd_user_position_historic` |
| Horário | `vw_usuarios_horario_trabalho_historico` | `sgdSearchHorarios` · historico · D15 (**SQL fixo ≥ 2026-08-01**) | `sgd_horario_historic` | `sgd_users_horario_historic` |
| Usuário Genesys | API Genesys (BFS do organograma) | `genesys-import` · T | `DB_GENESYS.public."users_Genesys"` ("Tabela que salva os usuários da nossa divisão dentro da Genesys") | `DB_GENESYS.genesys_users` |
| Usuário SGD na Genesys | Sybase (por e-mail cadastrado na Genesys) | `genesys-import` · T | `DB_GENESYS.public."users_SGD"` | usado no UPDATE de `sgd_alocations` |
| Usuário do chat | API Plug | **não mapeado** (planejado `import-webchat-plug`, `orq:docs/PLANO-WEBCHAT.md`) | `DB_WEBCHAT.public.users` (`i_user_sgd`) | `DB_WEBCHAT.webchat_users` |

### 5.1 `tb_colaboradores` (tabela derivada)
- **Origem:** somente Postgres, via **dblink** a partir de DB_SGD (`calendar`, `sgd_users`, `sgd_alocation_historic`, `sgd_alocation_reg`, `sgd_cargos`, `sgd_resale`, `sgd_user_cargo_historico`, `sgd_user_manager_historic`, `sgd_horario_historic`), DB_GENESYS (`users_Genesys`) e DB_WEBCHAT (`users`) (`orq:modules/historic_tb_colaboradores/sql/queries.sql:24-247`).
- **Como:**
  - produto cartesiano calendário × `sgd_users`;
  - remove dias fora de [admissão, inativação];
  - junta por (data, i_user) às tabelas históricas, por e-mail ao Genesys (exato) e ao WebChat (`trim(lower)`);
  - "`delete from public.tb_colaboradores … where a.data = b.data`" + INSERT (`queries.sql:340-416`);
  - backfill: `DELETE … WHERE data BETWEEN %s AND %s`.
- **Job:** `historic-tb-colaboradores`, 06:11, janela D-1.
- **Postgres:** `DB_REPORTS_ANALITICOS.public.tb_colaboradores`, 1 linha por (data, id_usuario_sgd), ~4,9 mi linhas. **Duplica** cerca de 71 usuários/dia (`orq:CLAUDE.md:890-892`).
- **Consumo:**
  - Dataflow `DB_REPORTS_ANALITICOS.tb_colaboradores`;
  - `tb_ocorrencias_analitica`;
  - `tb_demanda_lideres`;
  - `tb_interacoes_lideres_plug_analitico`;
  - `plug-status-realtime` (coordenador pelo `id_chat`).

## 6. Agenda / ausência

| Caminho | Sybase | Carga | Postgres | Dataflow |
|---|---|---|---|---|
| Passado | `vw_agenda`, `vw_agenda_tipos`, `vw_feriados`, `vw_usuarios_auditoria`, `power_bi.vw_usuarios`, UDF `f_get_gestor_suporte` | `import-agendas` (03:05) · `sgdSearchSchedulePastNEW` · D60. ⚠️ "o DELETE nao tem teto superior — apaga o futuro e reinsere so o passado" | `DB_SGD.public.sgd_schedule` (1 por dia × usuário × tipo × motivo, em minutos) | `DB_SGD_ALL.sgd_schedule` (recalcula minutos com teto de 480 e almoço) |
| Passado + futuro | idem | `sgdSearchSchedulePastNEW` (D60) e depois `sgdSearchScheduleFutureNew` ("faixa >= CURRENT_DATE", +90 d), sequenciais | `sgd_schedule_past_future` | `sgd_schedule_past_future` |
| Últimos dias úteis | idem + `public.calendar` | `sgdSearchSchedulePast_3days` ("OFFSET AGD_DIAS_UTEIS (off-by-one por design)") | `sgd_schedule_three_days` | `sgd_schedule_three_days` |
| Cadastros | `vw_agenda_tipos`, `vw_agenda_motivos_ausencias` | `misc_cadastros.*` · daily · T | `sgd_schedule_absences_type/_reason` | idem |
| **Tempo real** | `vw_agenda`, `vw_agenda_tipos`, `vw_agenda_motivos_ausencias`, `vw_alocacao`, `vw_usuarios_alocacao_historico`, `vw_usuarios_dados`, `vw_setores`, `power_bi.vw_usuarios`, `f_get_gestor_suporte` | leitura direta no Sybase pelo Dataflow (sem Maestro); -2 a +6 meses | — | `TB_SYBASE_SGD_AGENDA.Agenda` (setor por alocação, unidade por revenda, filtro de gerentes por nome) |
| CTS | idem (UPG + "Centro de Treinamento") | `import-cts` · `cts.agenda.sgdSearchSchedule` · D365 ("consulta mais cara do modulo") | `DB_CTS.public.CTS_Schedule` | — |
| Projetado | planilha Forecast, abas AusenciasSul/AusenciasCampinas | `forecast.insertForecastAusenciasProjetado` (2×) · T | `forecast.ausencias_projetado` | `forecast_proj_ausencias` |

- **Derivado:** "dias trabalhados" = (motivo 0 − demais)/480 em `tb_demanda_lideres`.
- **Nota:** o `import-sgd-geral` deixou de carregar a agenda: "essa carga passou a ser responsabilidade de outro app" (`orq:modules/_import_sgd/etl/domains/misc_cadastros.py:10-14`, via extração). O "outro app" é o `import-agendas` (inferido).

## 7. Ocorrência

| Etapa | Detalhe |
|---|---|
| **Sybase** | `vw_ocorrencia`, `vw_ocorrencia_tramite`, `vw_ocorrencia_anotacao`, `vw_ocorrencia_area/categoria/setor/situacao/prioridade/sane/ss/ssc`, UDF `minutosuteis` |
| **Carga** | `import-sgd-diario` · rotina `ocorrencias` (espera ~10 min "para nao concorrer com a carga do proprio SGD"). `search_occurrence`: "`DELETE FROM public.sgd_ocorrencia WHERE i_situacao NOT IN (5) OR (i_situacao = 5 AND ultimo_tramite::date >= CURRENT_DATE - INTERVAL '7 days')`" + INSERT (`orq:…/occurrence.py:162-170`); exclui `id 4120`. `search_occurrence_tramite`: D1 (UNION tramite + anotação) + 6 UPDATEs de correção em `sgd_ocorrencia`. Cadastros T; `search_occurrence_priority`: T, mas só entrada ≥ 2026-05-01. `sgdOccurrenceTime`: PG T (minutos úteis em Python) |
| **Postgres** | `DB_SGD.public.sgd_ocorrencia` (1/ocorrência; tipo 1 = pai, 2 = sub; `tme_minutos`, `tma_total_minutos`, `tma_sub_minutos`), `sgd_ocorrencia_tramite` (1/trâmite), `sgd_ocorrencia_tramite_time`, domínios |
| **Dataflow** | `DB_OCORRENCIAS.*` (10 entidades, cópia 1:1) |
| **Derivada** | `DB_REPORTS_ANALITICOS.public.tb_ocorrencias_analitica`: `historic-tb-ocorrencias-analitica` (08:00; nasce `enabled:false`), dblink DB_SGD + `tb_colaboradores` + `tb_satisfacao_subocorrencias`. DELETE da janela por período `date_tram >= %s AND < fim+1` + INSERT, guarda anti-wipe, janela D-30. 1 linha por trâmite de ocorrência (chave real `(i_ocorrencia, i_tram)`), 69 colunas. "A janela descarta trâmites por construção … 17% em D-30" (aceito). Dataflow `DB_REPORTS_ANALITICOS.tb_ocorrencias_analitica` |
| **Metas** | aba "Ocorrencias" → `public.goals` |

## 8. Implantação / treinamento (externo)

- **Sybase:** `vw_externo`, `vw_externo_programacao`, `vw_externo_treinamento*`, `vw_externo_situacoes`, `vw_externo_categoria`, `vw_externo_local_treinamento`, `vw_externo_forma_treinamento`, `vw_externo_treinamento_motivo`.
- **Carga:** rotina `implantacao`:
  - `externo.implantacao` = **ID** ("DELETE por id_externos IN (...) da janela", entrada ou atualização ≥ D-10);
  - `programacao` e `treinamento_programacao` = D5;
  - demais = T.
- **Postgres:** `DB_SGD.externo.*` (implantação ~220 mil; programação ~1 mi; treinamento_programacao ~7,8 mi).
- **Dataflow:** `DB_SGD_IMPLANTACAO.*` (11 entidades; o fluxo não é modificado desde 2024-10-17).

## 9. SA / NE (sgsai)

- **Sybase sgsai:** `vw_forum_sa` (atualizacao D-1), `vw_forum_sa_classificacoes`, `vw_forum_sa_situacoes`, `vw_forum_sa_motivos_reprovacao`, `vw_forum_sa_prioridades`, `vw_forum_sa_sai`.
- **Carga:** rotina `sa_ne_genesys_forecast`, que é uma "cadeia sequencial obrigatória (SA/NE → Genesys → Forecast)". O passo Genesys foi removido: "um schema `genesys` que NÃO existe no DB_GENESYS. Nunca funcionaram" (`orq:modules/_import_sgd/catalog.py:275-280`, via extração).
  - `sgd_sa`: ID
  - `sgd_ssc_sa`: T
  - `sgd_sa_priority`: **AC**
  - `sgd_sai_sane`: T
  - cadastros: T
- **Postgres:** `DB_SGD.public.sgd_sa*`, `sgd_sai_sane`.
- **Dataflow:** `DB_SGD_ALL.sgd_sa`, `sgd_sa_description`, `sgd_sa_*`, `sgd_sai_vs_sane`.

## 10. Forecast / projetado

- **Fonte:** planilha Forecast.xlsx (abas por tabela) + Sybase para `client_user_history`.
- **Carga:** `forecast.cleanForecast` trunca as tabelas `forecast.*` ("TRUNCA 9 tabelas" segundo `maestro.json`; **8** segundo o código, `forecast.py:22-33`, via extração) e reinserir a partir das abas. Roda às 03:00 (sa_ne_genesys_forecast) e às 12:00 (`import-sgd-meiodia`).
- **Postgres:** `DB_SGD.forecast.{users, tme_projetado, de_para_alocacao, ausencias_projetado, fte_aprovado, produtividade_media, ajuste_demanda, de_para_calendar, demanda_projetada, client_user_history}`.
- **Dataflow:** `DB_SGD_ALL.forecast_*` (expande ini/fim pelo `public.calendar`).
- **Congeladas** (sem carga desde a remoção): `forecast.projetado`, `forecast.coefficient`, `forecast.calls`. Continuam no Dataflow (`forecast_projetado`, `forecast_coefficient`).
- **Planejado da diretoria:** `DB_GENESYS.temp.projetado_meia_hora` / `temp.projetado_pessoas`. Carga única de CSV "Real Time Projetado" (`orq:modules/paineis_tempo_real/tools/importar_projetado.py:1-40`, via extração). O relatório **Real Time projetado** lê planilhas direto do SharePoint/Web.

## 11. Metas (goals) e meta de capacidade

- **Fonte:** planilha de metas, abas AT, RegionalCampinas, RegionalSUL (com meta_at/folha/fiscont), N2 e Ocorrencias.
- **Carga:** `excel.limpa_GoalsOfExcel` (TRUNCATE) + 5 × `InsertGoalsOfExcel_*` (INSERT), às 03:00 e às 12:00 ("a planilha de metas é atualizada durante a manhã e o painel precisa dela ao meio-dia", `catalog.py:372-374`, via extração).
- **Postgres:** `DB_SGD.public.goals` (1 linha por e-mail × competência × descmeta; ~260 mil).
- **Dataflow:** `DB_METAS.goals` (expande por dia com `public.calendar`, para os formatos AAAA-MM e AAAA-MM-DD).
- **Consumo:** `tb_demanda_lideres.valormeta` (1 valor por dia × e-mail, o maior).
- **Meta de capacidade:** `DB_REPORTS_ANALITICOS.public.tb_meta_capacidade_atendimento` (PK id_meta_atendimento; cargo × setor × acesso × faixa de tempo de casa). **Não mapeada no Maestro** → Dataflow `DB_REPORTS_ANALITICOS.tb_meta_capacidade_atendimento` e `tb_demanda_lideres.meta_maxima_atendimento`.

## 12. Demanda dos líderes (tabelas derivadas)

| Tabela | Fontes | Como | Grão | Consumo |
|---|---|---|---|---|
| `DB_REPORTS_CONSOLIDADOS.public.tb_demanda_lideres` | `tb_colaboradores` (Filiais), `tb_meta_capacidade_atendimento`, `DB_GENESYS."historic_callsAgents"` (inbound, `nNotResponding=0`), `DB_SGD.sgd_schedule` (dias trabalhados), `sgd_ssc` (SSC Web), `goals`, `DB_ESPELHO_SQLSERVER.public.interacoes_bi` (pedido de ajuda), `DB_WEBCHAT.protocols` (chat) e `protocols_all` (apoio Plug) | `historic-tb-interacoes-lideres-plug` (07:20, dias=3): extração em Python, TEMP tables e "DEMANDA_DELETE_PERIODO" + INSERT final (`orq:modules/historic_tb_interacoes_lideres_plug/sql/demanda.sql`) | "Uma linha por colaborador "Filiais" por dia" (`demanda.sql:4`) | Dataflow `DB_REPORTS_CONSOLIDADOS.tb_demanda_lideres`; dataset `Controle Mensal - Líderes` (inferido) |
| `DB_REPORTS_ANALITICOS.public.tb_interacoes_lideres_plug_analitico` | `DB_WEBCHAT.protocols_all` × `tenant_id` (tenant "TR Atendimento Líderes"), `sgd_sa_module`/`sgd_sa_system`, `tb_colaboradores` | mesmo job; DELETE período [ini, fim+1) + INSERT; guardas anti-fan-out/anti-wipe | 1 por interação de líder no Plug. Líder = `i_userchat`; técnico = `id_client / 1000` | Dataflow `DB_REPORTS_ANALITICOS.tb_interacoes_lideres_plug_analitico` |
| `DB_SGD.suporte.dados_teams_sul` | 3 planilhas "Dados demanda time líderes 2025 {AT, Fiscont, Folha}" | `excel.main_teams_sul` = UPSERT ON CONFLICT (auxiliar) — **ÓRFÃ** (nenhuma rotina chama) | 1 por pedido de ajuda no Teams | `DB_SUL_INTERNO.dados_teams_sul` |

## 13. Voz (Genesys)

| Postgres `DB_GENESYS.public.*` | Carga | Dataflow `DB_GENESYS.*` |
|---|---|---|
| `historic_callsAgents` (conversa × agente), `historic_callsAbandoned`, `calls_agents_halfHour`, `queue_Performance`, `historic_qualifications`, `agentAvailable`, `HistoricAgentStatus` | `genesys-import` (03:15, ontem): DELETE+INSERT da janela ("executar duas vezes no mesmo dia é seguro"); `historic_callsAgents` também é reescrita no dia por `produtividade-pendencia-realtime` (DELETE+INSERT do dia) | `genesys_historicCallsAgents`, `…Abandoned`, `callsAgentsHalfHour`, `queuePerformance_HalfHour`, `qualificationsSkills`, `agentAvailable`, `historicAgentStatus` |
| `queue`, `skills` | UPSERT (filas antigas mantidas de propósito) | `genesys_queue`, `genesys_skill`, `genesys_areaSkillQueue` |
| `users_Genesys`, `users_SGD` | T | `genesys_users` |
| `survey` | NOT EXISTS (`genesys-import`) + novos (realtime) | `genesys_survey` (com `survey_question*`, **sem job**) |
| `callsWithClient` | 30 dias | dentro de `genesys_historicCallsAgents` |
| `historic_calls_transcript` | NOT EXISTS (`genesys-import` + `genesys-transcricao-realtime`) | `DB_GENESYS_TRANSCRIPTIONS.genesys_calls_transcription` |
| `historic_calls_ia_new` | `insights-realtime` (IA) | `genesys_historicCalls_ia`; `historic_calls_ia` (antiga, **sem job**) |
| `sgd_alocations` | vem do `import-sgd-diario` (ver §5) | junções de alocação |

- **Tempo real:** `genesys-sla` (push `_genesysQueueSLA`, `_genesysNotReady` → relatórios `_genesysQueueSLA` e "Acompanhamento Tempo Real Fone_v2.1"); `genesys-queue-realtime` (push `_genesysQueue`); `genesys-status-agents-realtime`.

## 14. Chat (Plug / WebChat)

- **Tempo real:** `plug-queue-realtime` grava `DB_WEBCHAT.public.protocols` (DELETE do dia + INSERT), `protocols_transcription` (ON CONFLICT DO NOTHING) e `temp.{tme,tma,tem,tfm}_protocols`, com push TME/TMA/TEM/TFM/CHAT_FILA.
- **Status:** `plug-status-realtime` grava `DB_GENESYS.temp."plugRealTimeStatus"`.
- **Transcrição:** `plug-transcricao-realtime`.
- **Sem job no Maestro:** `protocols_history`, `protocols_sequence_message` (~112 mi), `protocols_all`, `users`, `users_historicstatus`, `tenant_id`, `sgd_cli_liberados_chat`, view `vw_protocolos_all`. Carga batch **planejada, não implementada** (`orq:docs/PLANO-WEBCHAT.md:8-14`, via extração).
- **IA:** `protocols_ia` ← `insights-realtime`.
- **Dataflow:** `DB_WEBCHAT.*` (14 entidades). `webchat_protocols` junta alocação do DB_SGD por **dblink** e o disregard `type='CHAT'`.

## 15. CTS / TRIA

- **Sybase cts:** `vw_cts_*`, `vw_cts_chat_interacoes`; e sgd `vw_ssc_avaliacao_tria`.
- **Carga:** `import-cts` (05:30; grupos A → barreira → B → espera de 2 h → C). Tipos de carga:
  - UPSERT: `CTS_HistoryOfResponsible`
  - D1: `CTS_SatisfactionSearch`
  - D5: `cts_solucoes`
  - D10: `cts_access_count`
  - D30: histórico/revisões
  - D180: `sgd_request`
  - **AC:** `CTS_SearchContent`, `cts_gpt_saudacao`, `sgd_avaliacao_tria`, `tria.chat_interacoes`, `DB_SGD.sgd_preferencia_pesquisa`
- **Dataflow:** `DB_CTS.*`.
- **Sem job:** `tria.authentication`, `tria.chat_sit_motv`, `public.vw_rel_cts_gpt_saudacao`, base `tria.public.dashboard`.

## 16. IA no SGD / chains
- `vw_chat_open_arena_interacao` → `misc_cadastros.search_chain_ia` (rotina chain_ia, D1 numa transação; falha por encoding sem `cp1252`) → `DB_SGD.public.chain_ia_interacao` → `DB_SGD_ALL/DB_SGD_IA.sgd_chain_ia_interacao`.
- `DB_REPORTS_CONSOLIDADOS.public.chains_ia` (**sem job**) → `chains_ia_usuarios`.

## 17. LogMeIn
- API LogMeIn Rescue → `import-logmein` (06:40): DELETE `start_time` da janela D-1 + INSERT → `DB_SGD.logmein.acessos` → `DB_LOGMEIN.logmein_sessoes` (junta `sgd_alocation_historic`, `sgd_users`, `sgd_user_manager_historic`).

## 18. Calendário e dimensões de tempo
- `DB_SGD.public.calendar` — **mantida por fora do Maestro** ("Nada no Maestro a escreve", `orq:modules/import_agendas/skills.md:55`, via extração).
  - Usada por `sgd_pendency` (UP de dias úteis), `import-agendas` (três dias), `minutos_uteis` (feriados), `tb_colaboradores` (esqueleto de dias), `DB_METAS.goals` e `forecast_*`.
  - Dataflow `DB_SGD_ALL.calendar`.
- Cópias: `DB_SGD_N2.ss.calendar` (usada por `ss_pendency`), `DB_SGD_N2.public."dCalendar"`, `public."dTime"`.

## 19. RLS
- Revendas: `DB_SGD.public.sgd_users` + `sgd_resale` → `DB_RLS.rls_user`.
- Permissões: planilhas Web (`rls_username`, `rls_resale`, `rls_resale_tenant_id`), sem Maestro.
