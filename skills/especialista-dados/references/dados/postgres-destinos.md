# Destinos Postgres do ETL (SGD · CTS · Agendas)

> Última atualização: 2026-09-30 · Fonte: Maestro v1.9.9 (`analytics-bi-dominio-orquestrador`) — `modules/_import_sgd/catalog.py` e `modules/_import_dominio/catalog.py`
> **Gerado automaticamente** por `scripts/mapear_maestro.py` — não editar à mão (regras e contexto de negócio ficam em `dados-sgd-regras-e-joins.md`).

Regra de ouro do Maestro: o fluxo `ss` grava em **DB_SGD_N2** (schema `ss`); o Genesys grava em **DB_GENESYS**; o resto do ETL do SGD grava em **DB_SGD**; o import-cts grava em **DB_CTS**. Tipos de carga: *recarga total*, *substitui janela de N dia(s)* (delta), *ACUMULA* (insert sem limpeza), *UPDATE/UPSERT*.

## DB_CTS

| Tabela destino | Carga | Função ETL | Rotinas | Job | Origem |
|---|---|---|---|---|---|
| `public.CTS_HistoryOfResponsible` | UPSERT (MERGE por chave) | `cts.dados_cts.sgdSearchHistoricoCTS` | A | import-cts | Sybase cts |
| `public.CTS_HistoryOfResponsibleFinally` | recarga TOTAL | `cts.dados_cts.sgdSearchHistoricoCTS` | A | import-cts | Sybase cts |
| `public.CTS_ModulosSolucoes` | recarga TOTAL | `cts.dados_cts.sgdSearchModuleSolutions` | A | import-cts | Sybase cts |
| `public.CTS_SatisfactionSearch` | substitui janela de 1 dia(s) | `cts.dados_cts.sgdSatisfacaoSolucoes` | B | import-cts | Sybase cts |
| `public.CTS_Schedule` | substitui janela de 365 dia(s) | `cts.agenda.sgdSearchSchedule` | A | import-cts | Sybase sgd |
| `public.CTS_SearchContent` | INSERT sem limpeza (ACUMULA) | `cts.dados_cts.sgdSearchPesquisasRealizadas` | A | import-cts | Sybase cts |
| `public.CTS_Solutions_Video_URL` | INSERT so do que mudou | `cts.dados_cts.sgdVerificaUrlCTS` | B | import-cts | Sybase cts |
| `public.CTS_Users` | recarga TOTAL | `cts.cadastros.sgdSearchUsersCTSclientes` | A | import-cts | Sybase sgd |
| `public.SGD_Client` | recarga TOTAL | `cts.cadastros.sgdSearchClients` | A | import-cts | Sybase sgd |
| `public.User_SGD_CTS` | recarga TOTAL | `cts.cadastros.sgdSearchUsersCTS` | A | import-cts | Sybase sgd |
| `public.cts_access_count` | substitui janela de 10 dia(s) | `cts.dados_cts.sgdSearchAcessCount` | A | import-cts | Sybase cts |
| `public.cts_dados_digital` | recarga TOTAL | `cts.excel_digital.InsertDadosExcel` | A | import-cts | Excel: digital |
| `public.cts_gpt_saudacao` | INSERT sem limpeza (ACUMULA) | `cts.dados_cts.ctsConfigSaudacoes` | semanal | import-cts | Sybase cts |
| `public.cts_solucoes` | substitui janela de 5 dia(s) | `cts.dados_cts.sgdSearchSolutions` | A | import-cts | Sybase cts |
| `public.cts_solucoes_historico` | substitui janela de 30 dia(s) | `cts.dados_cts.ctsSolucoesHistorico` | C | import-cts | Sybase cts |
| `public.cts_solucoes_revisoes` | substitui janela de 30 dia(s) | `cts.dados_cts.ctsSolucoesRevisoes` | C | import-cts | Sybase cts |
| `public.cts_solucoes_revisoes_motivos` | recarga TOTAL | `cts.dados_cts.ctsRevisaoMotivos` | A | import-cts | Sybase cts |
| `public.cts_solucoes_usuarios` | recarga TOTAL | `cts.cadastros.sgdSearchResponsibleCTS` | A | import-cts | Sybase sgd |
| `public.sgd_absences_type` | recarga TOTAL | `cts.agenda.sgdDataAgendaTypes` | A | import-cts | Sybase sgd |
| `public.sgd_absencesreason` | recarga TOTAL | `cts.agenda.sgdDataAbsencesReason` | A | import-cts | Sybase sgd |
| `public.sgd_avaliacao_tria` | INSERT sem limpeza (ACUMULA) | `cts.requisicoes.sgdAvaliacoesTria` | A | import-cts | Sybase sgd |
| `public.sgd_classification` | recarga TOTAL | `cts.requisicoes.sgdSearchClassifications` | A | import-cts | Sybase sgd |
| `public.sgd_request` | substitui janela de 180 dia(s) | `cts.requisicoes.sgdSsc` | A | import-cts | Sybase sgd |
| `temp_import.CTS_HistoryOfResponsible` | recarga TOTAL | `cts.dados_cts.sgdSearchHistoricoCTS` | A | import-cts | Sybase cts |
| `temp_import.CTS_SatisfactionSearch` | recarga TOTAL | `cts.dados_cts.sgdSatisfacaoSolucoes` | B | import-cts | Sybase cts |
| `temp_import.CTS_Solutions_VideoURL` | recarga TOTAL | `cts.dados_cts.sgdVerificaUrlCTS` | B | import-cts | Sybase cts |
| `tria.chat_interacoes` | INSERT sem limpeza (ACUMULA) | `cts.chat_interacoes.sgdInteracoesChat` | A | import-cts | Sybase cts |

## DB_GENESYS

| Tabela destino | Carga | Função ETL | Rotinas | Job | Origem |
|---|---|---|---|---|---|
| `public.cad_alocations` | recarga TOTAL | `clients_sgd.sgdSearchAlocations` | historico | import-sgd-diario | Sybase sgd |
| `public.sgd_alocations` | recarga TOTAL | `clients_sgd.sgdSearchAlocations` | historico | import-sgd-diario | Sybase sgd |
| `public.sgd_ssc_genesys` | recarga TOTAL | `requests_sgd.sgdSearchSSC_GENESYStoSGD` | daily | import-sgd-diario | Postgres |

## DB_SGD

| Tabela destino | Carga | Função ETL | Rotinas | Job | Origem |
|---|---|---|---|---|---|
| `externo.categoria` | recarga TOTAL | `externo.sgdCategoria` | implantacao | import-sgd-diario | Sybase sgd |
| `externo.forma_treinamento` | recarga TOTAL | `externo.sgdFormasTreinamentos` | implantacao | import-sgd-diario | Sybase sgd |
| `externo.implantacao` | substitui janela de 10 dia(s) | `externo.sgdImplantacao` | implantacao | import-sgd-diario | Sybase sgd |
| `externo.local_treinamento` | recarga TOTAL | `externo.sgdLocalTreinamento` | implantacao | import-sgd-diario | Sybase sgd |
| `externo.motivo_treinamento` | recarga TOTAL | `externo.sgdMotivoTreinamento` | implantacao | import-sgd-diario | Sybase sgd |
| `externo.programacao` | substitui janela de 5 dia(s) | `externo.sgdProgramacao` | implantacao | import-sgd-diario | Sybase sgd |
| `externo.situacoes` | recarga TOTAL | `externo.sgdSituacoes` | implantacao | import-sgd-diario | Sybase sgd |
| `externo.treinamento` | recarga TOTAL | `externo.sgdCadTreinamentos` | implantacao | import-sgd-diario | Sybase sgd |
| `externo.treinamento_conteudo` | recarga TOTAL | `externo.sgdCadConteudoTreinamentos` | implantacao | import-sgd-diario | Sybase sgd |
| `externo.treinamento_programacao` | substitui janela de 5 dia(s) | `externo.sgdTreinamentosProgramacao` | implantacao | import-sgd-diario | Sybase sgd |
| `externo.treinamento_programacao_usuario` | recarga TOTAL | `externo.sgdTreinamentosProgramacaoUsuarios` | implantacao | import-sgd-diario | Sybase sgd |
| `forecast.ajuste_demanda` | recarga TOTAL | `forecast.cleanForecast` | sa_ne_genesys_forecast, meiodia | import-sgd-diario, import-sgd-meiodia | Postgres |
| `forecast.ajuste_demanda` | recarga TOTAL | `forecast.insertForecastAjusteDemanda` | sa_ne_genesys_forecast, meiodia | import-sgd-diario, import-sgd-meiodia | Excel: forecast |
| `forecast.ausencias_projetado` | recarga TOTAL | `forecast.cleanForecast` | sa_ne_genesys_forecast, meiodia | import-sgd-diario, import-sgd-meiodia | Postgres |
| `forecast.ausencias_projetado` | recarga TOTAL | `forecast.insertForecastAusenciasProjetado` | sa_ne_genesys_forecast, meiodia | import-sgd-diario, import-sgd-meiodia | Excel: forecast |
| `forecast.client_user_history` | INSERT sem limpeza (ACUMULA) | `forecast.sgdUsersAlter` | sa_ne_genesys_forecast | import-sgd-diario | Sybase sgd |
| `forecast.de_para_alocacao` | recarga TOTAL | `forecast.cleanForecast` | sa_ne_genesys_forecast, meiodia | import-sgd-diario, import-sgd-meiodia | Postgres |
| `forecast.de_para_alocacao` | recarga TOTAL | `forecast.insertForecastDeParaAlocation` | sa_ne_genesys_forecast, meiodia | import-sgd-diario, import-sgd-meiodia | Excel: forecast |
| `forecast.de_para_calendar` | recarga TOTAL | `forecast.cleanForecast` | sa_ne_genesys_forecast, meiodia | import-sgd-diario, import-sgd-meiodia | Postgres |
| `forecast.de_para_calendar` | recarga TOTAL | `forecast.deParaCalendar` | sa_ne_genesys_forecast, meiodia | import-sgd-diario, import-sgd-meiodia | Excel: forecast |
| `forecast.demanda_projetada` | recarga TOTAL | `forecast.criaDemandaProjetada` | sa_ne_genesys_forecast | import-sgd-diario | Excel: forecast |
| `forecast.fte_aprovado` | recarga TOTAL | `forecast.cleanForecast` | sa_ne_genesys_forecast, meiodia | import-sgd-diario, import-sgd-meiodia | Postgres |
| `forecast.fte_aprovado` | recarga TOTAL | `forecast.insertForecastFTEAprovado` | sa_ne_genesys_forecast, meiodia | import-sgd-diario, import-sgd-meiodia | Excel: forecast |
| `forecast.produtividade_media` | recarga TOTAL | `forecast.cleanForecast` | sa_ne_genesys_forecast, meiodia | import-sgd-diario, import-sgd-meiodia | Postgres |
| `forecast.produtividade_media` | recarga TOTAL | `forecast.insertForecastMediaProdutividade` | sa_ne_genesys_forecast, meiodia | import-sgd-diario, import-sgd-meiodia | Excel: forecast |
| `forecast.tme_projetado` | recarga TOTAL | `forecast.cleanForecast` | sa_ne_genesys_forecast, meiodia | import-sgd-diario, import-sgd-meiodia | Postgres |
| `forecast.tme_projetado` | recarga TOTAL | `forecast.insertForecastProjTME` | sa_ne_genesys_forecast, meiodia | import-sgd-diario, import-sgd-meiodia | Excel: forecast |
| `forecast.users` | recarga TOTAL | `forecast.cleanForecast` | sa_ne_genesys_forecast, meiodia | import-sgd-diario, import-sgd-meiodia | Postgres |
| `forecast.users` | recarga TOTAL | `forecast.insertForecastUsers` | sa_ne_genesys_forecast, meiodia | import-sgd-diario, import-sgd-meiodia | Excel: forecast |
| `public.chain_ia_interacao` | substitui janela de 1 dia(s) | `misc_cadastros.search_chain_ia` | chain_ia | import-sgd-diario | Sybase sgd |
| `public.goals` | recarga TOTAL | `excel.limpa_GoalsOfExcel` | metas | import-sgd-diario, import-sgd-meiodia | Postgres |
| `public.goals` | INSERT sem limpeza (ACUMULA) | `excel.InsertGoalsOfExcel_AT` | metas | import-sgd-diario, import-sgd-meiodia | Excel: metas |
| `public.goals` | INSERT sem limpeza (ACUMULA) | `excel.InsertGoalsOfExcel_Campinas` | metas | import-sgd-diario, import-sgd-meiodia | Excel: metas |
| `public.goals` | INSERT sem limpeza (ACUMULA) | `excel.InsertGoalsOfExcel_SUL` | metas | import-sgd-diario, import-sgd-meiodia | Excel: metas |
| `public.goals` | INSERT sem limpeza (ACUMULA) | `excel.InsertGoalsOfExcel_N2` | metas | import-sgd-diario, import-sgd-meiodia | Excel: metas |
| `public.goals` | INSERT sem limpeza (ACUMULA) | `excel.InsertGoalsOfExcel_Ocorrencias` | metas | import-sgd-diario, import-sgd-meiodia | Excel: metas |
| `public.sgd_alocation_historic` | substitui janela de 60 dia(s) | `clients_sgd.sgdSearchAlocations` | historico | import-sgd-diario | Sybase sgd |
| `public.sgd_alocation_reg` | recarga TOTAL | `clients_sgd.sgdSearchCadAlocations` | daily | import-sgd-diario | Sybase sgd |
| `public.sgd_cargos` | recarga TOTAL | `clients_sgd.insertCargos` | daily | import-sgd-diario | Sybase sgd |
| `public.sgd_client` | recarga TOTAL | `clients_sgd.sgdSearchClients` | daily | import-sgd-diario | Sybase sgd |
| `public.sgd_client_contact` | recarga TOTAL | `clients_sgd.sgdDateClientesContacts` | daily | import-sgd-diario | Sybase sgd |
| `public.sgd_client_observ` | recarga TOTAL | `clients_sgd.sgdObservation` | observacoes | import-sgd-observacoes | Sybase sgd |
| `public.sgd_genesys` | substitui janela de 5 dia(s) | `requests_sgd.sgdSearchSSC_GENESYS` | daily | import-sgd-diario | Sybase sgd |
| `public.sgd_horario_historic` | substitui janela de 15 dia(s) | `clients_sgd.sgdSearchHorarios` | historico | import-sgd-diario | Sybase sgd |
| `public.sgd_ocorrencia` | substitui por situação (não por data) | `occurrence.search_occurrence` | ocorrencias | import-sgd-diario | Sybase sgd |
| `public.sgd_ocorrencia` | UPDATE no lugar | `occurrence.search_occurrence_tramite` | ocorrencias | import-sgd-diario | Postgres |
| `public.sgd_ocorrencia_area` | recarga TOTAL | `occurrence.search_occurrence_area` | ocorrencias | import-sgd-diario | Sybase sgd |
| `public.sgd_ocorrencia_categoria` | recarga TOTAL | `occurrence.search_occurrence_category` | ocorrencias | import-sgd-diario | Sybase sgd |
| `public.sgd_ocorrencia_prioridade` | recarga TOTAL | `occurrence.search_occurrence_priority` | ocorrencias | import-sgd-diario | Sybase sgd |
| `public.sgd_ocorrencia_sane` | recarga TOTAL | `occurrence.search_occurrence_sane` | ocorrencias | import-sgd-diario | Sybase sgd |
| `public.sgd_ocorrencia_setor` | recarga TOTAL | `occurrence.search_occurrence_setor` | ocorrencias | import-sgd-diario | Sybase sgd |
| `public.sgd_ocorrencia_situacao` | recarga TOTAL | `occurrence.search_occurrence_situation` | ocorrencias | import-sgd-diario | Sybase sgd |
| `public.sgd_ocorrencia_ss` | recarga TOTAL | `occurrence.search_occurrence_ss` | ocorrencias | import-sgd-diario | Sybase sgd |
| `public.sgd_ocorrencia_ssc` | recarga TOTAL | `occurrence.search_occurrence_ssc` | ocorrencias | import-sgd-diario | Sybase sgd |
| `public.sgd_ocorrencia_tramite` | substitui janela de 1 dia(s) | `occurrence.search_occurrence_tramite` | ocorrencias | import-sgd-diario | Sybase sgd |
| `public.sgd_ocorrencia_tramite_time` | recarga TOTAL | `occurrence.sgdOccurrenceTime` | ocorrencias | import-sgd-diario | Postgres |
| `public.sgd_pendency` | INSERT sem limpeza (ACUMULA) | `requests_sgd.sgdSscPendency` | pendency | import-sgd-diario | Sybase sgd |
| `public.sgd_pendency` | UPDATE no lugar | `requests_sgd.sgdSscPendencyDiasUteis` | pendency, dias_uteis | import-sgd-diario | Postgres |
| `public.sgd_preferencia_pesquisa` | INSERT sem limpeza (ACUMULA) | `cts.cadastros.sgdSearchPreferenciasPesquisas` | semanal | import-cts | Sybase sgd |
| `public.sgd_product` | recarga TOTAL | `forecast.sgdProduct` | daily | import-sgd-diario | Sybase sgd |
| `public.sgd_product_client` | recarga TOTAL | `clients_sgd.sgdSearchProduct` | historico | import-sgd-diario | Sybase sgd |
| `public.sgd_resale` | recarga TOTAL | `clients_sgd.sgdSearchResales` | daily | import-sgd-diario | Sybase sgd |
| `public.sgd_sa` | substitui janela de 1 dia(s) | `sgsai.saNeRequest` | sa_ne_genesys_forecast | import-sgd-diario | Sybase sgsai |
| `public.sgd_sa_classification` | recarga TOTAL | `sgsai.saClassification` | sa_ne_genesys_forecast | import-sgd-diario | Sybase sgsai |
| `public.sgd_sa_disapproval_reason` | recarga TOTAL | `sgsai.saDisapprovalReason` | sa_ne_genesys_forecast | import-sgd-diario | Sybase sgsai |
| `public.sgd_sa_module` | recarga TOTAL | `requests_sgd.sgdModule` | daily | import-sgd-diario | Sybase sgd |
| `public.sgd_sa_priority` | INSERT sem limpeza (ACUMULA) | `sgsai.saPriority` | sa_ne_genesys_forecast | import-sgd-diario | Sybase sgsai |
| `public.sgd_sa_situations` | recarga TOTAL | `sgsai.saSituations` | sa_ne_genesys_forecast | import-sgd-diario | Sybase sgsai |
| `public.sgd_sa_system` | recarga TOTAL | `requests_sgd.sgdSystem` | daily | import-sgd-diario | Sybase sgd |
| `public.sgd_sai_sane` | recarga TOTAL | `sgsai.saiSaNe` | sa_ne_genesys_forecast | import-sgd-diario | Sybase sgsai |
| `public.sgd_schedule` | substitui janela de 60 dia(s) | `agendas.agenda.sgdSearchSchedulePastNEW` | agendas | import-agendas | Sybase sgd |
| `public.sgd_schedule_absences_reason` | recarga TOTAL | `misc_cadastros.sgdDataAbsencesReason` | daily | import-sgd-diario | Sybase sgd |
| `public.sgd_schedule_absences_type` | recarga TOTAL | `misc_cadastros.sgdDataAgendaTypes` | daily | import-sgd-diario | Sybase sgd |
| `public.sgd_schedule_past_future` | substitui janela de 60 dia(s) | `agendas.agenda.sgdSearchSchedulePastNEW` | agendas | import-agendas | Sybase sgd |
| `public.sgd_schedule_past_future` | substitui janela de 90 dia(s) | `agendas.agenda.sgdSearchScheduleFutureNew` | agendas | import-agendas | Sybase sgd |
| `public.sgd_schedule_three_days` | janela dos ultimos dias uteis | `agendas.agenda.sgdSearchSchedulePast_3days` | agendas | import-agendas | Sybase sgd |
| `public.sgd_soses` | recarga TOTAL | `requests_sgd.sgdSSCsSoses` | historico | import-sgd-diario | Sybase sgd |
| `public.sgd_ssc` | substitui janela de 5 dia(s) | `requests_sgd.sgdSearchRequests` | daily | import-sgd-diario | Sybase sgd |
| `public.sgd_ssc_answer_time` | INSERT sem limpeza (ACUMULA) | `requests_sgd.sgdSscTimeAnswered` | daily | import-sgd-diario | Sybase sgd |
| `public.sgd_ssc_classification` | recarga TOTAL | `requests_sgd.sgdSearchClassifications` | daily | import-sgd-diario | Sybase sgd |
| `public.sgd_ssc_disregard_dissatisfaction` | recarga TOTAL | `disregard.disregardDissatisfaction` | daily | import-sgd-diario | Postgres |
| `public.sgd_ssc_dissatisfaction_historic` | substitui janela de 30 dia(s) | `requests_sgd.sgdSearchRequestsReasonDissatisfaction` | historico | import-sgd-diario | Sybase sgd |
| `public.sgd_ssc_ia_chat` | substitui janela de 5 dia(s) | `requests_sgd.sgdSearchSSC_IA_CHAT` | daily | import-sgd-diario | Sybase sgd |
| `public.sgd_ssc_internal_time` | substitui janela de 5 dia(s) | `requests_sgd.sgdSscTimeInternal` | daily | import-sgd-diario | Sybase sgd |
| `public.sgd_ssc_reescrever_ia` | substitui janela de 5 dia(s) | `requests_sgd.utilizaReescreverIA` | historico | import-sgd-diario | Sybase sgd |
| `public.sgd_ssc_sa` | recarga TOTAL | `sgsai.saNeRequest` | sa_ne_genesys_forecast | import-sgd-diario | Sybase sgsai |
| `public.sgd_ssc_situation` | recarga TOTAL | `requests_sgd.sgdDataSscSituation` | daily | import-sgd-diario | Sybase sgd |
| `public.sgd_ssc_text_conclusion` | substitui janela de 5 dia(s) | `requests_sgd.sgdSearchTextConclusion` | historico | import-sgd-diario | Sybase sgd |
| `public.sgd_ssc_tramites` | substitui janela de 3 dia(s) | `requests_sgd.sgdSscTramites` | historico | import-sgd-diario | Sybase sgd |
| `public.sgd_ssc_utiliza_solucao` | substitui janela de 5 dia(s) | `requests_sgd.pesquisaSolucao` | historico | import-sgd-diario | Sybase sgd |
| `public.sgd_user_cargo_historico` | recarga TOTAL | `clients_sgd.insertHistoricoCargos` | daily | import-sgd-diario | Sybase sgd |
| `public.sgd_user_client` | recarga TOTAL | `clients_sgd.sgdSearchUsersClient` | daily | import-sgd-diario | Sybase sgd |
| `public.sgd_user_manager_historic` | substitui janela de 365 dia(s) | `clients_sgd.sgdSearchAlterManager` | historico | import-sgd-diario | Sybase sgd |
| `public.sgd_users` | recarga TOTAL | `clients_sgd.insertUsersSGD` | daily | import-sgd-diario | Sybase sgd |
| `suporte.dados_teams_sul` | UPSERT (ON CONFLICT DO UPDATE) | `excel.main_teams_sul` | — | — | Excel: teams sul |

## DB_SGD_N2

| Tabela destino | Carga | Função ETL | Rotinas | Job | Origem |
|---|---|---|---|---|---|
| `public.sgd_ssc_disregard_dissatisfaction` | recarga TOTAL | `disregard.disregardDissatisfaction` | daily | import-sgd-diario | Postgres |
| `ss.ss` | substitui janela de SS_DIAS dia(s) (default 31) | `ss_n2.sgdSearchRequests` | ss | import-sgd-diario | Sybase sgd |
| `ss.ss_category` | recarga TOTAL | `ss_n2.sgdSearchCategorias` | ss | import-sgd-diario | Sybase sgd |
| `ss.ss_classification` | recarga TOTAL | `ss_n2.sgdSearchClassifications` | ss | import-sgd-diario | Sybase sgd |
| `ss.ss_conclusion_text` | substitui janela de 5 dia(s) | `ss_n2.sgdSearchTextConclusion` | ss | import-sgd-diario | Sybase sgd |
| `ss.ss_disregard_dissatisfaction` | recarga TOTAL | `disregard.disregardDissatisfactionSS` | ss | import-sgd-diario | Postgres |
| `ss.ss_module` | recarga TOTAL | `ss_n2.sgdSearchModulos` | ss | import-sgd-diario | Sybase sgd |
| `ss.ss_pendency` | INSERT sem limpeza (ACUMULA) | `ss_n2.sgdSsPendencyPostgres` | ss | import-sgd-diario | Postgres |
| `ss.ss_situation` | recarga TOTAL | `ss_n2.sgdSituationSS` | ss | import-sgd-diario | Sybase sgd |
| `ss.ss_sub_topic` | recarga TOTAL | `ss_n2.sgdSearchSubTopicos` | ss | import-sgd-diario | Sybase sgd |
| `ss.ss_system` | recarga TOTAL | `ss_n2.sgdSearchSistemas` | ss | import-sgd-diario | Sybase sgd |
| `ss.ss_topic` | recarga TOTAL | `ss_n2.sgdSearchTopicos` | ss | import-sgd-diario | Sybase sgd |
| `ss.ss_tramites` | substitui janela de 5 dia(s) | `ss_n2.sgdSsTramites` | ss | import-sgd-diario | Sybase sgd |
| `ss.ss_tramites_time` | recarga TOTAL | `ss_n2.sgdSSTimeN2` | ss | import-sgd-diario | Postgres |

## DB_WEBCHAT

| Tabela destino | Carga | Função ETL | Rotinas | Job | Origem |
|---|---|---|---|---|---|
| `public.disregard_dissatisfaction` | recarga TOTAL | `disregard.disregardDissatisfaction` | daily | import-sgd-diario | Postgres |

