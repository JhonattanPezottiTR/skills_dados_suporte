# Linhagem de dados: Sybase → ETL → Postgres → Power BI

> Última atualização: 2026-09-30 · Fonte: Maestro v1.9.9 (`analytics-bi-dominio-orquestrador`) — catálogos ETL + `origens.py` + `spec.yaml` + PBIP
> **Gerado automaticamente** por `scripts/mapear_maestro.py` — não editar à mão (regras e contexto de negócio ficam em `dados-sgd-regras-e-joins.md`).

## 1. ETL batch (tabela a tabela)

| Origem (views Sybase / outra) | Função ETL | Destino Postgres | Carga |
|---|---|---|---|
| `bethadba.vw_cts_solucoes_historico_responsaveis` | `cts.dados_cts.sgdSearchHistoricoCTS` | `DB_CTS·public.CTS_HistoryOfResponsible` | UPSERT (MERGE por chave) |
| `bethadba.vw_cts_solucoes_historico_responsaveis` | `cts.dados_cts.sgdSearchHistoricoCTS` | `DB_CTS·public.CTS_HistoryOfResponsibleFinally` | recarga TOTAL |
| `bethadba.vw_cts_modulos_solucoes` | `cts.dados_cts.sgdSearchModuleSolutions` | `DB_CTS·public.CTS_ModulosSolucoes` | recarga TOTAL |
| `bethadba.vw_cts_pesquisa_satisfacoes` | `cts.dados_cts.sgdSatisfacaoSolucoes` | `DB_CTS·public.CTS_SatisfactionSearch` | substitui janela de 1 dia(s) |
| `bethadba.f_get_gestor_suporte`, `bethadba.vw_agenda`, `bethadba.vw_agenda_tipos`, `bethadba.vw_feriados`, `bethadba.vw_setores`, `bethadba.vw_usuarios_auditoria`, `bethadba.vw_usuarios_dados`, `power_bi.vw_usuarios` | `cts.agenda.sgdSearchSchedule` | `DB_CTS·public.CTS_Schedule` | substitui janela de 365 dia(s) |
| `bethadba.vw_cts_pesquisa_conteudos` | `cts.dados_cts.sgdSearchPesquisasRealizadas` | `DB_CTS·public.CTS_SearchContent` | INSERT sem limpeza (ACUMULA) |
| `bethadba.vw_cts_solucoes` | `cts.dados_cts.sgdVerificaUrlCTS` | `DB_CTS·public.CTS_Solutions_Video_URL` | INSERT so do que mudou |
| `power_bi.vw_usuarios` | `cts.cadastros.sgdSearchUsersCTSclientes` | `DB_CTS·public.CTS_Users` | recarga TOTAL |
| `bethadba.vw_cmcontratos`, `bethadba.vw_gecidades`, `bethadba.vw_geclientes`, `bethadba.vw_geclientes_observacoes`, `bethadba.vw_geestados`, `bethadba.vw_revendas` | `cts.cadastros.sgdSearchClients` | `DB_CTS·public.SGD_Client` | recarga TOTAL |
| `bethadba.vw_setores`, `bethadba.vw_usuarios_dados`, `power_bi.vw_usuarios` | `cts.cadastros.sgdSearchUsersCTS` | `DB_CTS·public.User_SGD_CTS` | recarga TOTAL |
| `bethadba.vw_cts_contagem_acessos` | `cts.dados_cts.sgdSearchAcessCount` | `DB_CTS·public.cts_access_count` | substitui janela de 10 dia(s) |
| Excel: digital | `cts.excel_digital.InsertDadosExcel` | `DB_CTS·public.cts_dados_digital` | recarga TOTAL |
| `bethadba.vw_cts_gpt_sugestao` | `cts.dados_cts.ctsConfigSaudacoes` | `DB_CTS·public.cts_gpt_saudacao` | INSERT sem limpeza (ACUMULA) |
| `bethadba.vw_cts_solucoes`, `bethadba.vw_modulos`, `bethadba.vw_sistemas`, `bethadba.vw_ssc_origens`, `bethadba.vw_sss_classificacoes`, `bethadba.vw_topicos_suportes` | `cts.dados_cts.sgdSearchSolutions` | `DB_CTS·public.cts_solucoes` | substitui janela de 5 dia(s) |
| `bethadba.vw_modulos`, `bethadba.vw_sistemas`, `bethadba.vw_topicos_suportes`, `cts.bethadba.vw_cts_solucoes_historico` | `cts.dados_cts.ctsSolucoesHistorico` | `DB_CTS·public.cts_solucoes_historico` | substitui janela de 30 dia(s) |
| `cts.bethadba.vw_cts_solucoes_revisoes` | `cts.dados_cts.ctsSolucoesRevisoes` | `DB_CTS·public.cts_solucoes_revisoes` | substitui janela de 30 dia(s) |
| `cts.bethadba.vw_cts_solucoes_revisao_motivos` | `cts.dados_cts.ctsRevisaoMotivos` | `DB_CTS·public.cts_solucoes_revisoes_motivos` | recarga TOTAL |
| `bethadba.vw_setores`, `bethadba.vw_usuarios_dados`, `power_bi.vw_usuarios` | `cts.cadastros.sgdSearchResponsibleCTS` | `DB_CTS·public.cts_solucoes_usuarios` | recarga TOTAL |
| `bethadba.vw_agenda_tipos` | `cts.agenda.sgdDataAgendaTypes` | `DB_CTS·public.sgd_absences_type` | recarga TOTAL |
| `bethadba.vw_agenda_motivos_ausencias` | `cts.agenda.sgdDataAbsencesReason` | `DB_CTS·public.sgd_absencesreason` | recarga TOTAL |
| `bethadba.vw_modulos`, `bethadba.vw_ssc`, `bethadba.vw_ssc_avaliacao_tria` | `cts.requisicoes.sgdAvaliacoesTria` | `DB_CTS·public.sgd_avaliacao_tria` | INSERT sem limpeza (ACUMULA) |
| `bethadba.vw_sss_classificacoes` | `cts.requisicoes.sgdSearchClassifications` | `DB_CTS·public.sgd_classification` | recarga TOTAL |
| `bethadba.vw_ssc` | `cts.requisicoes.sgdSsc` | `DB_CTS·public.sgd_request` | substitui janela de 180 dia(s) |
| `bethadba.vw_cts_solucoes_historico_responsaveis` | `cts.dados_cts.sgdSearchHistoricoCTS` | `DB_CTS·temp_import.CTS_HistoryOfResponsible` | recarga TOTAL |
| `bethadba.vw_cts_pesquisa_satisfacoes` | `cts.dados_cts.sgdSatisfacaoSolucoes` | `DB_CTS·temp_import.CTS_SatisfactionSearch` | recarga TOTAL |
| `bethadba.vw_cts_solucoes` | `cts.dados_cts.sgdVerificaUrlCTS` | `DB_CTS·temp_import.CTS_Solutions_VideoURL` | recarga TOTAL |
| `bethadba.vw_cts_chat_interacoes` | `cts.chat_interacoes.sgdInteracoesChat` | `DB_CTS·tria.chat_interacoes` | INSERT sem limpeza (ACUMULA) |
| `bethadba.vw_usuarios_alocacao_historico`, `bethadba.vw_usuarios_auditoria`, `power_bi.vw_usuarios` | `clients_sgd.sgdSearchAlocations` | `DB_GENESYS·public.cad_alocations` | recarga TOTAL |
| `bethadba.vw_usuarios_alocacao_historico`, `bethadba.vw_usuarios_auditoria`, `power_bi.vw_usuarios` | `clients_sgd.sgdSearchAlocations` | `DB_GENESYS·public.sgd_alocations` | recarga TOTAL |
| Postgres | `requests_sgd.sgdSearchSSC_GENESYStoSGD` | `DB_GENESYS·public.sgd_ssc_genesys` | recarga TOTAL |
| `bethadba.vw_externo_categoria` | `externo.sgdCategoria` | `DB_SGD·externo.categoria` | recarga TOTAL |
| `bethadba.vw_externo_forma_treinamento` | `externo.sgdFormasTreinamentos` | `DB_SGD·externo.forma_treinamento` | recarga TOTAL |
| `sgd.bethadba.vw_externo` | `externo.sgdImplantacao` | `DB_SGD·externo.implantacao` | substitui janela de 10 dia(s) |
| `bethadba.vw_externo_local_treinamento` | `externo.sgdLocalTreinamento` | `DB_SGD·externo.local_treinamento` | recarga TOTAL |
| `bethadba.vw_externo_treinamento_motivo` | `externo.sgdMotivoTreinamento` | `DB_SGD·externo.motivo_treinamento` | recarga TOTAL |
| `sgd.bethadba.vw_externo_programacao` | `externo.sgdProgramacao` | `DB_SGD·externo.programacao` | substitui janela de 5 dia(s) |
| `bethadba.vw_externo_situacoes` | `externo.sgdSituacoes` | `DB_SGD·externo.situacoes` | recarga TOTAL |
| `bethadba.vw_externo_treinamento` | `externo.sgdCadTreinamentos` | `DB_SGD·externo.treinamento` | recarga TOTAL |
| `bethadba.vw_externo_treinamento_conteudo` | `externo.sgdCadConteudoTreinamentos` | `DB_SGD·externo.treinamento_conteudo` | recarga TOTAL |
| `sgd.bethadba.vw_externo_treinamento_programacao` | `externo.sgdTreinamentosProgramacao` | `DB_SGD·externo.treinamento_programacao` | substitui janela de 5 dia(s) |
| `bethadba.vw_externo_treinamento_programacao_usuario` | `externo.sgdTreinamentosProgramacaoUsuarios` | `DB_SGD·externo.treinamento_programacao_usuario` | recarga TOTAL |
| Postgres | `forecast.cleanForecast` | `DB_SGD·forecast.ajuste_demanda` | recarga TOTAL |
| Excel: forecast | `forecast.insertForecastAjusteDemanda` | `DB_SGD·forecast.ajuste_demanda` | recarga TOTAL |
| Postgres | `forecast.cleanForecast` | `DB_SGD·forecast.ausencias_projetado` | recarga TOTAL |
| Excel: forecast | `forecast.insertForecastAusenciasProjetado` | `DB_SGD·forecast.ausencias_projetado` | recarga TOTAL |
| `bethadba.vw_cmcontratos`, `bethadba.vw_cmcontratos_hist_usuarios`, `bethadba.vw_geclientes` | `forecast.sgdUsersAlter` | `DB_SGD·forecast.client_user_history` | INSERT sem limpeza (ACUMULA) |
| Postgres | `forecast.cleanForecast` | `DB_SGD·forecast.de_para_alocacao` | recarga TOTAL |
| Excel: forecast | `forecast.insertForecastDeParaAlocation` | `DB_SGD·forecast.de_para_alocacao` | recarga TOTAL |
| Postgres | `forecast.cleanForecast` | `DB_SGD·forecast.de_para_calendar` | recarga TOTAL |
| Excel: forecast | `forecast.deParaCalendar` | `DB_SGD·forecast.de_para_calendar` | recarga TOTAL |
| Excel: forecast | `forecast.criaDemandaProjetada` | `DB_SGD·forecast.demanda_projetada` | recarga TOTAL |
| Postgres | `forecast.cleanForecast` | `DB_SGD·forecast.fte_aprovado` | recarga TOTAL |
| Excel: forecast | `forecast.insertForecastFTEAprovado` | `DB_SGD·forecast.fte_aprovado` | recarga TOTAL |
| Postgres | `forecast.cleanForecast` | `DB_SGD·forecast.produtividade_media` | recarga TOTAL |
| Excel: forecast | `forecast.insertForecastMediaProdutividade` | `DB_SGD·forecast.produtividade_media` | recarga TOTAL |
| Postgres | `forecast.cleanForecast` | `DB_SGD·forecast.tme_projetado` | recarga TOTAL |
| Excel: forecast | `forecast.insertForecastProjTME` | `DB_SGD·forecast.tme_projetado` | recarga TOTAL |
| Postgres | `forecast.cleanForecast` | `DB_SGD·forecast.users` | recarga TOTAL |
| Excel: forecast | `forecast.insertForecastUsers` | `DB_SGD·forecast.users` | recarga TOTAL |
| `bethadba.vw_chat_open_arena_interacao` | `misc_cadastros.search_chain_ia` | `DB_SGD·public.chain_ia_interacao` | substitui janela de 1 dia(s) |
| Postgres | `excel.limpa_GoalsOfExcel` | `DB_SGD·public.goals` | recarga TOTAL |
| Excel: metas | `excel.InsertGoalsOfExcel_AT` | `DB_SGD·public.goals` | INSERT sem limpeza (ACUMULA) |
| Excel: metas | `excel.InsertGoalsOfExcel_Campinas` | `DB_SGD·public.goals` | INSERT sem limpeza (ACUMULA) |
| Excel: metas | `excel.InsertGoalsOfExcel_SUL` | `DB_SGD·public.goals` | INSERT sem limpeza (ACUMULA) |
| Excel: metas | `excel.InsertGoalsOfExcel_N2` | `DB_SGD·public.goals` | INSERT sem limpeza (ACUMULA) |
| Excel: metas | `excel.InsertGoalsOfExcel_Ocorrencias` | `DB_SGD·public.goals` | INSERT sem limpeza (ACUMULA) |
| `bethadba.vw_usuarios_alocacao_historico`, `bethadba.vw_usuarios_auditoria`, `power_bi.vw_usuarios` | `clients_sgd.sgdSearchAlocations` | `DB_SGD·public.sgd_alocation_historic` | substitui janela de 60 dia(s) |
| `bethadba.vw_alocacao` | `clients_sgd.sgdSearchCadAlocations` | `DB_SGD·public.sgd_alocation_reg` | recarga TOTAL |
| `bethadba.vw_cargos` | `clients_sgd.insertCargos` | `DB_SGD·public.sgd_cargos` | recarga TOTAL |
| `bethadba.vw_cmcontratos`, `bethadba.vw_gecidades`, `bethadba.vw_geclientes`, `bethadba.vw_geclientes_observacoes`, `bethadba.vw_geestados`, `bethadba.vw_revendas` | `clients_sgd.sgdSearchClients` | `DB_SGD·public.sgd_client` | recarga TOTAL |
| `bethadba.vw_geclientes`, `bethadba.vw_geclientes_contatos_adicionais`, `bethadba.vw_revendas` | `clients_sgd.sgdDateClientesContacts` | `DB_SGD·public.sgd_client_contact` | recarga TOTAL |
| `bethadba.vw_geclientes_observacoes` | `clients_sgd.sgdObservation` | `DB_SGD·public.sgd_client_observ` | recarga TOTAL |
| `bethadba.vw_ssc` | `requests_sgd.sgdSearchSSC_GENESYS` | `DB_SGD·public.sgd_genesys` | substitui janela de 5 dia(s) |
| `bethadba.vw_usuarios_auditoria`, `bethadba.vw_usuarios_horario_trabalho_historico`, `power_bi.vw_usuarios` | `clients_sgd.sgdSearchHorarios` | `DB_SGD·public.sgd_horario_historic` | substitui janela de 15 dia(s) |
| `bethadba.minutosuteis`, `bethadba.minutosuteis`, `bethadba.vw_ocorrencia`, `bethadba.vw_ocorrencia`, `bethadba.vw_ocorrencia_tramite`, `bethadba.vw_ocorrencia_tramite` | `occurrence.search_occurrence` | `DB_SGD·public.sgd_ocorrencia` | substitui por situação (não por data) |
| `bethadba.vw_ocorrencia_anotacao`, `bethadba.vw_ocorrencia_tramite` | `occurrence.search_occurrence_tramite` | `DB_SGD·public.sgd_ocorrencia` | UPDATE no lugar |
| `bethadba.vw_ocorrencia_area` | `occurrence.search_occurrence_area` | `DB_SGD·public.sgd_ocorrencia_area` | recarga TOTAL |
| `bethadba.vw_ocorrencia_categoria` | `occurrence.search_occurrence_category` | `DB_SGD·public.sgd_ocorrencia_categoria` | recarga TOTAL |
| `bethadba.vw_ocorrencia`, `bethadba.vw_ocorrencia_prioridade` | `occurrence.search_occurrence_priority` | `DB_SGD·public.sgd_ocorrencia_prioridade` | recarga TOTAL |
| `bethadba.vw_ocorrencia_sane` | `occurrence.search_occurrence_sane` | `DB_SGD·public.sgd_ocorrencia_sane` | recarga TOTAL |
| `bethadba.vw_ocorrencia_setor` | `occurrence.search_occurrence_setor` | `DB_SGD·public.sgd_ocorrencia_setor` | recarga TOTAL |
| `bethadba.vw_ocorrencia_situacao` | `occurrence.search_occurrence_situation` | `DB_SGD·public.sgd_ocorrencia_situacao` | recarga TOTAL |
| `bethadba.vw_ocorrencia_ss` | `occurrence.search_occurrence_ss` | `DB_SGD·public.sgd_ocorrencia_ss` | recarga TOTAL |
| `bethadba.vw_ocorrencia_ssc` | `occurrence.search_occurrence_ssc` | `DB_SGD·public.sgd_ocorrencia_ssc` | recarga TOTAL |
| `bethadba.vw_ocorrencia_anotacao`, `bethadba.vw_ocorrencia_tramite` | `occurrence.search_occurrence_tramite` | `DB_SGD·public.sgd_ocorrencia_tramite` | substitui janela de 1 dia(s) |
| Postgres | `occurrence.sgdOccurrenceTime` | `DB_SGD·public.sgd_ocorrencia_tramite_time` | recarga TOTAL |
| `bethadba.vw_modulos`, `bethadba.vw_sistemas`, `bethadba.vw_ssc`, `bethadba.vw_ssc_origens`, `bethadba.vw_ssc_tramites`, `bethadba.vw_topicos_suportes` | `requests_sgd.sgdSscPendency` | `DB_SGD·public.sgd_pendency` | INSERT sem limpeza (ACUMULA) |
| Postgres | `requests_sgd.sgdSscPendencyDiasUteis` | `DB_SGD·public.sgd_pendency` | UPDATE no lugar |
| `bethadba.vw_modulos`, `bethadba.vw_preferencias_pesquisas`, `bethadba.vw_sistemas`, `bethadba.vw_ssc_situacoes`, `bethadba.vw_sss_classificacoes`, `power_bi.vw_usuarios` | `cts.cadastros.sgdSearchPreferenciasPesquisas` | `DB_SGD·public.sgd_preferencia_pesquisa` | INSERT sem limpeza (ACUMULA) |
| `bethadba.vw_ceprodutos` | `forecast.sgdProduct` | `DB_SGD·public.sgd_product` | recarga TOTAL |
| `bethadba.vw_cmcontratos`, `bethadba.vw_geclientes`, `bethadba.vw_revendas` | `clients_sgd.sgdSearchProduct` | `DB_SGD·public.sgd_product_client` | recarga TOTAL |
| `bethadba.vw_revendas` | `clients_sgd.sgdSearchResales` | `DB_SGD·public.sgd_resale` | recarga TOTAL |
| `bethadba.vw_ssc`, `sgsai.bethadba.vw_forum_sa` | `sgsai.saNeRequest` | `DB_SGD·public.sgd_sa` | substitui janela de 1 dia(s) |
| `bethadba.vw_forum_sa_classificacoes` | `sgsai.saClassification` | `DB_SGD·public.sgd_sa_classification` | recarga TOTAL |
| `bethadba.vw_forum_sa_motivos_reprovacao` | `sgsai.saDisapprovalReason` | `DB_SGD·public.sgd_sa_disapproval_reason` | recarga TOTAL |
| `bethadba.vw_modulos` | `requests_sgd.sgdModule` | `DB_SGD·public.sgd_sa_module` | recarga TOTAL |
| `bethadba.vw_forum_sa_prioridades` | `sgsai.saPriority` | `DB_SGD·public.sgd_sa_priority` | INSERT sem limpeza (ACUMULA) |
| `bethadba.vw_forum_sa_situacoes` | `sgsai.saSituations` | `DB_SGD·public.sgd_sa_situations` | recarga TOTAL |
| `bethadba.vw_sistemas` | `requests_sgd.sgdSystem` | `DB_SGD·public.sgd_sa_system` | recarga TOTAL |
| `bethadba.vw_forum_sa_sai` | `sgsai.saiSaNe` | `DB_SGD·public.sgd_sai_sane` | recarga TOTAL |
| `bethadba.f_get_gestor_suporte`, `bethadba.vw_agenda`, `bethadba.vw_agenda_tipos`, `bethadba.vw_feriados`, `bethadba.vw_usuarios_auditoria`, `power_bi.vw_usuarios` | `agendas.agenda.sgdSearchSchedulePastNEW` | `DB_SGD·public.sgd_schedule` | substitui janela de 60 dia(s) |
| `bethadba.vw_agenda_motivos_ausencias` | `misc_cadastros.sgdDataAbsencesReason` | `DB_SGD·public.sgd_schedule_absences_reason` | recarga TOTAL |
| `bethadba.vw_agenda_tipos` | `misc_cadastros.sgdDataAgendaTypes` | `DB_SGD·public.sgd_schedule_absences_type` | recarga TOTAL |
| `bethadba.f_get_gestor_suporte`, `bethadba.vw_agenda`, `bethadba.vw_agenda_tipos`, `bethadba.vw_feriados`, `bethadba.vw_usuarios_auditoria`, `power_bi.vw_usuarios` | `agendas.agenda.sgdSearchSchedulePastNEW` | `DB_SGD·public.sgd_schedule_past_future` | substitui janela de 60 dia(s) |
| `bethadba.f_get_gestor_suporte`, `bethadba.vw_agenda`, `bethadba.vw_agenda_tipos`, `bethadba.vw_feriados`, `bethadba.vw_usuarios_auditoria`, `power_bi.vw_usuarios` | `agendas.agenda.sgdSearchScheduleFutureNew` | `DB_SGD·public.sgd_schedule_past_future` | substitui janela de 90 dia(s) |
| `bethadba.f_get_gestor_suporte`, `bethadba.vw_agenda`, `bethadba.vw_agenda_tipos`, `bethadba.vw_feriados`, `bethadba.vw_usuarios_auditoria`, `power_bi.vw_usuarios` | `agendas.agenda.sgdSearchSchedulePast_3days` | `DB_SGD·public.sgd_schedule_three_days` | janela dos ultimos dias uteis |
| `bethadba.vw_dado_relatorio_sose`, `bethadba.vw_soses_situacoes`, `bethadba.vw_ssc`, `bethadba.vw_ssc_dados_faturamentos`, `bethadba.vw_ssc_tipos_servicos_soses`, `bethadba.vw_ssc_tramites` | `requests_sgd.sgdSSCsSoses` | `DB_SGD·public.sgd_soses` | recarga TOTAL |
| `bethadba.minutosuteis`, `bethadba.minutosuteis`, `bethadba.vw_conversao_tramites`, `bethadba.vw_conversoes`, `bethadba.vw_modulos`, `bethadba.vw_sistemas`, `bethadba.vw_ss`, `bethadba.vw_ss_tramites`, `bethadba.vw_ssc`, `bethadba.vw_ssc_conversoes`, `bethadba.vw_ssc_origens`, `bethadba.vw_ssc_ss`, `bethadba.vw_ssc_ssql`, `bethadba.vw_ssc_tramites`, `bethadba.vw_ssql`, `bethadba.vw_ssql_tramites`, `bethadba.vw_topicos_suportes` | `requests_sgd.sgdSearchRequests` | `DB_SGD·public.sgd_ssc` | substitui janela de 5 dia(s) |
| `bethadba.relatoriotemporespostaanalitico`, `bethadba.vw_ssc`, `power_bi.vw_usuarios` | `requests_sgd.sgdSscTimeAnswered` | `DB_SGD·public.sgd_ssc_answer_time` | INSERT sem limpeza (ACUMULA) |
| `bethadba.vw_sss_classificacoes` | `requests_sgd.sgdSearchClassifications` | `DB_SGD·public.sgd_ssc_classification` | recarga TOTAL |
| Postgres | `disregard.disregardDissatisfaction` | `DB_SGD·public.sgd_ssc_disregard_dissatisfaction` | recarga TOTAL |
| `bethadba.vw_ssc` | `requests_sgd.sgdSearchRequestsReasonDissatisfaction` | `DB_SGD·public.sgd_ssc_dissatisfaction_historic` | substitui janela de 30 dia(s) |
| `bethadba.vw_completion_ai_ssc_chat` | `requests_sgd.sgdSearchSSC_IA_CHAT` | `DB_SGD·public.sgd_ssc_ia_chat` | substitui janela de 5 dia(s) |
| `bethadba.minutosuteis`, `bethadba.vw_meios_acesso`, `bethadba.vw_modulos`, `bethadba.vw_revendas`, `bethadba.vw_sistemas`, `bethadba.vw_ssc`, `bethadba.vw_ssc_categorias`, `bethadba.vw_ssc_origens`, `bethadba.vw_ssc_tramites`, `bethadba.vw_sss_classificacoes`, `bethadba.vw_topicos_suportes`, `power_bi.vw_usuarios` | `requests_sgd.sgdSscTimeInternal` | `DB_SGD·public.sgd_ssc_internal_time` | substitui janela de 5 dia(s) |
| `bethadba.removerhtmleacentuacao`, `bethadba.vw_confg_fluxo_acao_open_arena_interacao`, `bethadba.vw_configuracao_fluxo_acao_open_arena` | `requests_sgd.utilizaReescreverIA` | `DB_SGD·public.sgd_ssc_reescrever_ia` | substitui janela de 5 dia(s) |
| `bethadba.vw_ssc`, `sgsai.bethadba.vw_forum_sa` | `sgsai.saNeRequest` | `DB_SGD·public.sgd_ssc_sa` | recarga TOTAL |
| `bethadba.vw_ssc_situacoes` | `requests_sgd.sgdDataSscSituation` | `DB_SGD·public.sgd_ssc_situation` | recarga TOTAL |
| `bethadba.removerhtml`, `bethadba.vw_ssc`, `bethadba.vw_ssc_tramites` | `requests_sgd.sgdSearchTextConclusion` | `DB_SGD·public.sgd_ssc_text_conclusion` | substitui janela de 5 dia(s) |
| `bethadba.vw_ssc`, `bethadba.vw_ssc_tramites` | `requests_sgd.sgdSscTramites` | `DB_SGD·public.sgd_ssc_tramites` | substitui janela de 3 dia(s) |
| `bethadba.vw_ssc_pesquisa_resposta_utiliza_solucao` | `requests_sgd.pesquisaSolucao` | `DB_SGD·public.sgd_ssc_utiliza_solucao` | substitui janela de 5 dia(s) |
| `bethadba.vw_usuarios_auditoria`, `bethadba.vw_usuarios_cargo_historico`, `power_bi.vw_usuarios` | `clients_sgd.insertHistoricoCargos` | `DB_SGD·public.sgd_user_cargo_historico` | recarga TOTAL |
| `bethadba.vw_usuarios_dados`, `bethadba.vw_usuarios_informacoes_adicionais`, `power_bi.vw_usuarios` | `clients_sgd.sgdSearchUsersClient` | `DB_SGD·public.sgd_user_client` | recarga TOTAL |
| `bethadba.vw_usuarios_auditoria`, `bethadba.vw_usuarios_gestor_historico`, `power_bi.vw_usuarios` | `clients_sgd.sgdSearchAlterManager` | `DB_SGD·public.sgd_user_manager_historic` | substitui janela de 365 dia(s) |
| `bethadba.vw_revendas`, `bethadba.vw_usuarios_auditoria`, `bethadba.vw_usuarios_dados`, `power_bi.vw_usuarios` | `clients_sgd.insertUsersSGD` | `DB_SGD·public.sgd_users` | recarga TOTAL |
| Excel: teams sul | `excel.main_teams_sul` | `DB_SGD·suporte.dados_teams_sul` | UPSERT (ON CONFLICT DO UPDATE) |
| Postgres | `disregard.disregardDissatisfaction` | `DB_SGD_N2·public.sgd_ssc_disregard_dissatisfaction` | recarga TOTAL |
| `bethadba.vw_ss` | `ss_n2.sgdSearchRequests` | `DB_SGD_N2·ss.ss` | substitui janela de SS_DIAS dia(s) (default 31) |
| `bethadba.vw_ss_categorias` | `ss_n2.sgdSearchCategorias` | `DB_SGD_N2·ss.ss_category` | recarga TOTAL |
| `bethadba.vw_sss_classificacoes` | `ss_n2.sgdSearchClassifications` | `DB_SGD_N2·ss.ss_classification` | recarga TOTAL |
| `bethadba.removerhtml`, `bethadba.vw_ss_tramites` | `ss_n2.sgdSearchTextConclusion` | `DB_SGD_N2·ss.ss_conclusion_text` | substitui janela de 5 dia(s) |
| Postgres | `disregard.disregardDissatisfactionSS` | `DB_SGD_N2·ss.ss_disregard_dissatisfaction` | recarga TOTAL |
| `bethadba.vw_modulos` | `ss_n2.sgdSearchModulos` | `DB_SGD_N2·ss.ss_module` | recarga TOTAL |
| Postgres | `ss_n2.sgdSsPendencyPostgres` | `DB_SGD_N2·ss.ss_pendency` | INSERT sem limpeza (ACUMULA) |
| `bethadba.vw_ss_situacoes` | `ss_n2.sgdSituationSS` | `DB_SGD_N2·ss.ss_situation` | recarga TOTAL |
| `bethadba.vw_ssc_origens` | `ss_n2.sgdSearchSubTopicos` | `DB_SGD_N2·ss.ss_sub_topic` | recarga TOTAL |
| `bethadba.vw_sistemas` | `ss_n2.sgdSearchSistemas` | `DB_SGD_N2·ss.ss_system` | recarga TOTAL |
| `bethadba.vw_topicos_suportes` | `ss_n2.sgdSearchTopicos` | `DB_SGD_N2·ss.ss_topic` | recarga TOTAL |
| `bethadba.vw_ss_tramites` | `ss_n2.sgdSsTramites` | `DB_SGD_N2·ss.ss_tramites` | substitui janela de 5 dia(s) |
| Postgres | `ss_n2.sgdSSTimeN2` | `DB_SGD_N2·ss.ss_tramites_time` | recarga TOTAL |
| Postgres | `disregard.disregardDissatisfaction` | `DB_WEBCHAT·public.disregard_dissatisfaction` | recarga TOTAL |

## 2. Tempo real (push para Power BI)

| Job | Variável de push | Dataset (workspace "Dashboard - Real Time") | Relatórios |
|---|---|---|---|
| `genesys-queue-realtime` | `POWERBI_QUEUES_DETAILS_PUSH_URL` | _genesysQueue (detalhe) | — |
| `genesys-queue-realtime` | `POWERBI_QUEUES_PUSH_URL` | _genesysQueue | _genesysQueue |
| `genesys-sla` | `POWERBI_URL_NOTREADY` | _genesysNotReady | Acompanhamento Tempo Real Fone_v2.1 |
| `genesys-sla` | `POWERBI_URL_SLA` | _genesysQueueSLA | _genesysQueueSLA |
| `genesys-status-agents-realtime` | `POWERBI_PUSH_URL` | ? | — |
| `plug-queue-realtime` | `POWERBI_PUSH_URL_CHAT_FILA` | ? | — |
| `plug-queue-realtime` | `POWERBI_PUSH_URL_TEM` | ? | — |
| `plug-queue-realtime` | `POWERBI_PUSH_URL_TFM` | ? | — |
| `plug-queue-realtime` | `POWERBI_PUSH_URL_TMA` | ? | — |
| `plug-queue-realtime` | `POWERBI_PUSH_URL_TME` | ? | — |
| `plug-status-realtime` | `POWERBI_PUSH_URL` | ? | — |
| `produtividade-pendencia-realtime` | `POWERBI_PUSH_URL_DEMAND` | ? | — |
| `produtividade-pendencia-realtime` | `POWERBI_PUSH_URL_ENTRY_N2` | ? | — |
| `produtividade-pendencia-realtime` | `POWERBI_PUSH_URL_PENDENCY` | _sgdPendency | _sgdPendency |
| `produtividade-pendencia-realtime` | `POWERBI_PUSH_URL_PENDENCY_N2` | ? | — |
| `produtividade-pendencia-realtime` | `POWERBI_PUSH_URL_PRODUCTIVITY` | _genesysSGD_Productivity | _genesysSGD_Productivity |

> Datasets marcados com `?` ainda não foram associados a um relatório PBIP. A associação variável → dataset é inferida (nomes/colunas) e deve ser confirmada.
