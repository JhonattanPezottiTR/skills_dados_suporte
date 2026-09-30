# Fluxos de dados (Dataflows Power BI) — índice

> Última atualização: 2026-09-30 · Fonte: exports `model.json` dos Dataflows (pasta `Fluxos`) lidos por `scripts/mapear_fluxos.py` · **Gerado automaticamente** — não editar à mão.

## Como escolher a fonte ao criar um BI

1. **Já existe entidade no fluxo com os campos?** Use o Dataflow (a entidade abaixo) — é a fonte padrão dos relatórios, já tratada e com refresh agendado.
2. **Precisa de dado em tempo real do SGD** (ex.: agenda do dia)? Só o fluxo que lê **Sybase direto** é tempo real — hoje o `TB_SYBASE_SGD_AGENDA`. O resto lê réplicas no Postgres (atualizadas pelos jobs do Maestro, em geral D-1 ou intradiário — ver coluna *Carregada por*).
3. **Nenhum fluxo atende?** Escreva o SELECT direto na tabela Postgres de origem (colunas em `dados-postgres-<base>.md`) e avalie criar uma entidade nova no fluxo em vez de consulta avulsa no relatório.
4. SQL novo no Sybase: **somente** objetos de `dados-sybase-sgd-catalogo.md` (views `vw_*`).

## Resumo por dataflow

| Dataflow | Origem | Base(s) | Entidades | Última modificação |
|---|---|---|---|---|
| [DB_CTS](dados-fluxo-db_cts.md) | Postgres | DB_CTS, tria | 11 | 2026-06-04 |
| [DB_GENESYS](dados-fluxo-db_genesys.md) | Json.Document, Table.FromRows, Postgres | DB_GENESYS | 16 | 2026-09-28 |
| [DB_GENESYS_TRANSCRIPTIONS](dados-fluxo-db_genesys_transcriptions.md) | Postgres | DB_GENESYS | 1 | 2025-05-05 |
| [DB_LOGMEIN](dados-fluxo-db_logmein.md) | Postgres | DB_SGD | 1 | 2026-02-11 |
| [DB_METAS](dados-fluxo-db_metas.md) | Postgres | DB_SGD | 1 | 2026-01-05 |
| [DB_OCORRENCIAS](dados-fluxo-db_ocorrencias.md) | Postgres | DB_SGD | 10 | 2026-09-09 |
| [DB_REPORTS_ANALITICOS](dados-fluxo-db_reports_analiticos.md) | Postgres | DB_REPORTS_ANALITICOS | 4 | 2026-08-28 |
| [DB_REPORTS_CONSOLIDADOS](dados-fluxo-db_reports_consolidados.md) | Postgres | DB_REPORTS_CONSOLIDADOS | 10 | 2026-07-20 |
| [DB_RLS](dados-fluxo-db_rls.md) | Excel.Workbook, Web.Contents, Postgres | DB_SGD | 4 | 2025-12-23 |
| [DB_SGD_ALL](dados-fluxo-db_sgd_all.md) | Json.Document, Table.FromRows, Postgres | DB_SGD, DB_SGD_N2 | 71 | 2026-09-09 |
| [DB_SGD_IA](dados-fluxo-db_sgd_ia.md) | Postgres | DB_SGD | 3 | 2026-06-03 |
| [DB_SGD_IMPLANTACAO](dados-fluxo-db_sgd_implantacao.md) | Postgres | DB_SGD | 11 | 2024-10-17 |
| [DB_SUL_INTERNO](dados-fluxo-db_sul_interno.md) | Postgres | DB_SGD | 1 | 2025-10-21 |
| [DB_WEBCHAT](dados-fluxo-db_webchat.md) | Json.Document, Table.FromRows, Postgres | DB_WEBCHAT | 14 | 2026-09-23 |
| [TB_SYBASE_SGD_AGENDA](dados-fluxo-tb_sybase_sgd_agenda.md) | Sybase (SGD direto) | sgd | 1 | 2026-09-09 |

## Tabela de origem → entidade do fluxo

Use para responder "de qual tabela vem este campo" e "qual entidade do fluxo usar".

| Tabela de origem | Motor · base | Carregada por (Maestro) | Entidade(s) do fluxo |
|---|---|---|---|
| `bethadba.f_get_gestor_suporte` | Sybase · sgd | — (leitura direta, tempo real) | `TB_SYBASE_SGD_AGENDA.Agenda` |
| `bethadba.vw_agenda` | Sybase · sgd | — (leitura direta, tempo real) | `TB_SYBASE_SGD_AGENDA.Agenda` |
| `bethadba.vw_agenda_motivos_ausencias` | Sybase · sgd | — (leitura direta, tempo real) | `TB_SYBASE_SGD_AGENDA.Agenda` |
| `bethadba.vw_agenda_tipos` | Sybase · sgd | — (leitura direta, tempo real) | `TB_SYBASE_SGD_AGENDA.Agenda` |
| `bethadba.vw_alocacao` | Sybase · sgd | — (leitura direta, tempo real) | `TB_SYBASE_SGD_AGENDA.Agenda` |
| `bethadba.vw_setores` | Sybase · sgd | — (leitura direta, tempo real) | `TB_SYBASE_SGD_AGENDA.Agenda` |
| `bethadba.vw_usuarios_alocacao_historico` | Sybase · sgd | — (leitura direta, tempo real) | `TB_SYBASE_SGD_AGENDA.Agenda` |
| `bethadba.vw_usuarios_dados` | Sybase · sgd | — (leitura direta, tempo real) | `TB_SYBASE_SGD_AGENDA.Agenda` |
| `externo.categoria` | Postgres · DB_SGD | import-sgd-diario (recarga TOTAL) | `DB_SGD_IMPLANTACAO.sgd_externo_categoria` |
| `externo.forma_treinamento` | Postgres · DB_SGD | import-sgd-diario (recarga TOTAL) | `DB_SGD_IMPLANTACAO.sgd_externo_forma_treinamento` |
| `externo.implantacao` | Postgres · DB_SGD | import-sgd-diario (substitui janela de 10 dia(s)) | `DB_SGD_IMPLANTACAO.sgd_externo_implantacoes` |
| `externo.local_treinamento` | Postgres · DB_SGD | import-sgd-diario (recarga TOTAL) | `DB_SGD_IMPLANTACAO.sgd_externo_local_treinamento` |
| `externo.motivo_treinamento` | Postgres · DB_SGD | import-sgd-diario (recarga TOTAL) | `DB_SGD_IMPLANTACAO.sgd_externo_motivo_treinamento` |
| `externo.programacao` | Postgres · DB_SGD | import-sgd-diario (substitui janela de 5 dia(s)) | `DB_SGD_IMPLANTACAO.sgd_externo_programacao` |
| `externo.situacoes` | Postgres · DB_SGD | import-sgd-diario (recarga TOTAL) | `DB_SGD_IMPLANTACAO.sgd_externo_situacao` |
| `externo.treinamento` | Postgres · DB_SGD | import-sgd-diario (recarga TOTAL) | `DB_SGD_IMPLANTACAO.sgd_externo_treinamentos` |
| `externo.treinamento_conteudo` | Postgres · DB_SGD | import-sgd-diario (recarga TOTAL) | `DB_SGD_IMPLANTACAO.sgd_externo_treinamento_conteudo` |
| `externo.treinamento_programacao` | Postgres · DB_SGD | import-sgd-diario (substitui janela de 5 dia(s)) | `DB_SGD_IMPLANTACAO.sgd_externo_treinamento_programacao` |
| `externo.treinamento_programacao_usuario` | Postgres · DB_SGD | import-sgd-diario (recarga TOTAL) | `DB_SGD_IMPLANTACAO.sgd_externo_treinamento_programacao_usuarios` |
| `forecast.ajuste_demanda` | Postgres · DB_SGD | import-sgd-diario, import-sgd-meiodia (recarga TOTAL) | `DB_SGD_ALL.forecast_ajuste_demanda` |
| `forecast.ausencias_projetado` | Postgres · DB_SGD | import-sgd-diario, import-sgd-meiodia (recarga TOTAL) | `DB_SGD_ALL.forecast_proj_ausencias` |
| `forecast.client_user_history` | Postgres · DB_SGD | import-sgd-diario (INSERT sem limpeza (ACUMULA)) | `DB_SGD_ALL.forecast_client_user_history` |
| `forecast.coefficient` | Postgres · DB_SGD | congelada (decisão: "As 3 tabelas congelam como estão", orq:modules/_import_sgd/catalog.py:210-214) — não é escrita por nenhum job ativo | `DB_SGD_ALL.forecast_coefficient` |
| `forecast.de_para_alocacao` | Postgres · DB_SGD | import-sgd-diario, import-sgd-meiodia (recarga TOTAL) | `DB_SGD_ALL.forecast_de_para_alocacao_area`, `DB_SGD_ALL.sgd_alocation_reg` |
| `forecast.de_para_calendar` | Postgres · DB_SGD | import-sgd-diario, import-sgd-meiodia (recarga TOTAL) | `DB_SGD_ALL.forecast_de_para_calendar` |
| `forecast.demanda_projetada` | Postgres · DB_SGD | import-sgd-diario (recarga TOTAL) | `DB_SGD_ALL.forecast_demanda_projetada` |
| `forecast.fte_aprovado` | Postgres · DB_SGD | import-sgd-diario, import-sgd-meiodia (recarga TOTAL) | `DB_SGD_ALL.forecast_FTE_aprovado` |
| `forecast.produtividade_media` | Postgres · DB_SGD | import-sgd-diario, import-sgd-meiodia (recarga TOTAL) | `DB_SGD_ALL.forecast_avg_produtividade` |
| `forecast.projetado` | Postgres · DB_SGD | congelada (decisão: "As 3 tabelas congelam como estão", orq:modules/_import_sgd/catalog.py:210-214) — não é escrita por nenhum job ativo | `DB_SGD_ALL.forecast_projetado` |
| `forecast.tme_projetado` | Postgres · DB_SGD | import-sgd-diario, import-sgd-meiodia (recarga TOTAL) | `DB_SGD_ALL.forecast_proj_tme` |
| `forecast.users` | Postgres · DB_SGD | import-sgd-diario, import-sgd-meiodia (recarga TOTAL) | `DB_SGD_ALL.forecast_users_proj` |
| `power_bi.vw_usuarios` | Sybase · sgd | — (leitura direta, tempo real) | `TB_SYBASE_SGD_AGENDA.Agenda` |
| `public.agentavailable` | Postgres · DB_GENESYS | genesys-import | `DB_GENESYS.genesys_agentAvailable` |
| `public.backup_nuvem` | Postgres · DB_REPORTS_CONSOLIDADOS | não mapeado no Maestro | `DB_REPORTS_CONSOLIDADOS.backup_nuvem` |
| `public.calendar` | Postgres · DB_SGD | mantida manualmente por fora do Maestro (orq:modules/import_agendas/skills.md:55) | `DB_METAS.goals`, `DB_SGD_ALL.calendar`, `DB_SGD_ALL.forecast_FTE_aprovado`, `DB_SGD_ALL.forecast_ajuste_demanda`, `DB_SGD_ALL.forecast_avg_produtividade`, `DB_SGD_ALL.forecast_proj_ausencias` |
| `public.calls_agents_halfhour` | Postgres · DB_GENESYS | genesys-import | `DB_GENESYS.genesys_callsAgentsHalfHour` |
| `public.callswithclient` | Postgres · DB_GENESYS | genesys-import | `DB_GENESYS.genesys_historicCallsAgents` |
| `public.chain_ia_interacao` | Postgres · DB_SGD | import-sgd-diario (substitui janela de 1 dia(s)) | `DB_SGD_ALL.sgd_chain_ia_interacao`, `DB_SGD_IA.sgd_chain_ia_interacao` |
| `public.chains_ia` | Postgres · DB_REPORTS_CONSOLIDADOS | não mapeado no Maestro | `DB_REPORTS_CONSOLIDADOS.chains_ia_usuarios` |
| `public.cts_access_count` | Postgres · DB_CTS | import-cts (substitui janela de 10 dia(s)) | `DB_CTS.cts_sol_access_count` |
| `public.cts_dados_digital` | Postgres · DB_CTS | import-cts (recarga TOTAL) | `DB_CTS.cts_dados_digital` |
| `public.cts_searchcontent` | Postgres · DB_CTS | import-cts (INSERT sem limpeza (ACUMULA)) | `DB_CTS.cts_sol_pesquisas` |
| `public.cts_solucoes` | Postgres · DB_CTS | import-cts (substitui janela de 5 dia(s)) | `DB_CTS.cts_sol_cadastro` |
| `public.cts_solucoes_historico` | Postgres · DB_CTS | import-cts (substitui janela de 30 dia(s)) | `DB_CTS.cts_sol_historico` |
| `public.cts_solucoes_revisoes` | Postgres · DB_CTS | import-cts (substitui janela de 30 dia(s)) | `DB_CTS.cts_sol_revisoes` |
| `public.cts_solucoes_revisoes_motivos` | Postgres · DB_CTS | import-cts (recarga TOTAL) | `DB_CTS.cts_sol_revisoes_motivos` |
| `public.cts_solucoes_usuarios` | Postgres · DB_CTS | import-cts (recarga TOTAL) | `DB_CTS.cts_usuarios` |
| `public.dashboard` | Postgres · tria | não mapeado no Maestro | `DB_CTS.tria_plug` |
| `public.disregard_dissatisfaction` | Postgres · DB_WEBCHAT | import-sgd-diario (recarga TOTAL) | `DB_WEBCHAT.webchat_protocols` |
| `public.goals` | Postgres · DB_SGD | import-sgd-diario, import-sgd-meiodia (INSERT sem limpeza (ACUMULA)); import-sgd-diario, import-sgd-meiodia (recarga TOTAL) | `DB_METAS.goals` |
| `public.historic_calls_ia` | Postgres · DB_GENESYS | não mapeado no Maestro | `DB_GENESYS.genesys_historicCalls_ia` |
| `public.historic_calls_ia_new` | Postgres · DB_GENESYS | insights-realtime/insights-resumos (lib _insights) | `DB_GENESYS.genesys_historicCallsAgents`, `DB_GENESYS.genesys_historicCalls_ia` |
| `public.historic_calls_transcript` | Postgres · DB_GENESYS | genesys-import; genesys-transcricao-realtime | `DB_GENESYS_TRANSCRIPTIONS.genesys_calls_transcription` |
| `public.historic_callsabandoned` | Postgres · DB_GENESYS | genesys-import | `DB_GENESYS.genesys_historicCallsAbandoned` |
| `public.historic_callsagents` | Postgres · DB_GENESYS | genesys-import; produtividade-pendencia-realtime | `DB_GENESYS.genesys_historicCallsAgents`, `DB_GENESYS.genesys_survey` |
| `public.historic_callstranfers` | Postgres · DB_GENESYS | genesys-import | `DB_GENESYS.genesys_historicCallsTransfer` |
| `public.historic_qualifications` | Postgres · DB_GENESYS | genesys-import; genesys-sla | `DB_GENESYS.genesys_qualificationsSkills` |
| `public.historicagentstatus` | Postgres · DB_GENESYS | genesys-import | `DB_GENESYS.genesys_historicAgentStatus` |
| `public.jornada_fte` | Postgres · DB_REPORTS_CONSOLIDADOS | não mapeado no Maestro | `DB_REPORTS_CONSOLIDADOS.jornada_fte` |
| `public.jornada_fte_etapas` | Postgres · DB_REPORTS_CONSOLIDADOS | não mapeado no Maestro | `DB_REPORTS_CONSOLIDADOS.jornada_fte_etapas` |
| `public.pendencias_suporte` | Postgres · DB_REPORTS_CONSOLIDADOS | não mapeado no Maestro | `DB_REPORTS_CONSOLIDADOS.pendencias_suporte` |
| `public.presencedefinitions` | Postgres · DB_GENESYS | genesys-import | `DB_GENESYS.genesys_presenceDefinitions` |
| `public.produtividade_n1` | Postgres · DB_REPORTS_CONSOLIDADOS | não mapeado no Maestro | `DB_REPORTS_CONSOLIDADOS.produtividade_n1` |
| `public.produtividade_n2` | Postgres · DB_REPORTS_CONSOLIDADOS | não mapeado no Maestro | `DB_REPORTS_CONSOLIDADOS.produtividade_n2` |
| `public.protocols` | Postgres · DB_SGD | plug-queue-realtime | `DB_SGD_ALL.sgd_client` |
| `public.protocols` | Postgres · DB_WEBCHAT | plug-queue-realtime | `DB_WEBCHAT.webchat_first_answer`, `DB_WEBCHAT.webchat_historic`, `DB_WEBCHAT.webchat_historic_messages`, `DB_WEBCHAT.webchat_historic_total`, `DB_WEBCHAT.webchat_protocols`, `DB_WEBCHAT.webchat_queues` |
| `public.protocols_all` | Postgres · DB_WEBCHAT | não mapeado no Maestro | `DB_WEBCHAT.webchat_protocols_faturamento` |
| `public.protocols_history` | Postgres · DB_WEBCHAT | não mapeado no Maestro | `DB_WEBCHAT.webchat_historic`, `DB_WEBCHAT.webchat_protocols` |
| `public.protocols_ia` | Postgres · DB_WEBCHAT | insights-realtime/insights-resumos (lib _insights) | `DB_WEBCHAT.webchat_historic`, `DB_WEBCHAT.webchat_protocols`, `DB_WEBCHAT.webchat_protocols_ia` |
| `public.protocols_sequence_message` | Postgres · DB_WEBCHAT | não mapeado no Maestro | `DB_WEBCHAT.webchat_first_answer`, `DB_WEBCHAT.webchat_historic_messages`, `DB_WEBCHAT.webchat_historic_total` |
| `public.queue` | Postgres · DB_GENESYS | genesys-import | `DB_GENESYS.genesys_areaSkillQueue`, `DB_GENESYS.genesys_historicCallsAbandoned`, `DB_GENESYS.genesys_historicCallsAgents`, `DB_GENESYS.genesys_qualificationsSkills`, `DB_GENESYS.genesys_queue` |
| `public.queue_performance` | Postgres · DB_GENESYS | genesys-import | `DB_GENESYS.genesys_queuePerformance_HalfHour` |
| `public.sgd_alocation_historic` | Postgres · DB_SGD | import-sgd-diario (substitui janela de 60 dia(s)) | `DB_LOGMEIN.logmein_sessoes`, `DB_SGD_ALL.sgd_alocation_historic`, `DB_SGD_ALL.sgd_config_pref_pesquisas`, `DB_SGD_ALL.sgd_schedule`, `DB_SGD_ALL.sgd_schedule_three_days`, `DB_SGD_ALL.sgd_ssc`, `DB_SGD_ALL.sgd_user_manager_historic`, `DB_SGD_IA.sgd_utilizou_reescrever_IA` |
| `public.sgd_alocation_historic` | Postgres · DB_WEBCHAT | import-sgd-diario/meiodia/observacoes/consultas (lib _import_sgd) | `DB_WEBCHAT.webchat_protocols` |
| `public.sgd_alocation_reg` | Postgres · DB_SGD | import-sgd-diario (recarga TOTAL) | `DB_SGD_ALL.sgd_alocation_reg` |
| `public.sgd_alocations` | Postgres · DB_GENESYS | import-sgd-diario (recarga TOTAL) | `DB_GENESYS.genesys_agentAvailable`, `DB_GENESYS.genesys_callsAgentsHalfHour`, `DB_GENESYS.genesys_historicAgentStatus`, `DB_GENESYS.genesys_historicCallsAgents` |
| `public.sgd_cargos` | Postgres · DB_SGD | import-sgd-diario (recarga TOTAL) | `DB_SGD_ALL.sgd_cargos` |
| `public.sgd_cli_liberados_chat` | Postgres · DB_WEBCHAT | não mapeado no Maestro | `DB_WEBCHAT.sgd_clients_control_chat` |
| `public.sgd_client` | Postgres · DB_SGD | import-sgd-diario (recarga TOTAL) | `DB_SGD_ALL.sgd_client`, `DB_SGD_ALL.sgd_ssc` |
| `public.sgd_client_contact` | Postgres · DB_SGD | import-sgd-diario (recarga TOTAL) | `DB_SGD_ALL.sgd_client_phone` |
| `public.sgd_client_observ` | Postgres · DB_SGD | import-sgd-observacoes (recarga TOTAL) | `DB_SGD_ALL.sgd_client` |
| `public.sgd_genesys` | Postgres · DB_SGD | import-sgd-diario (substitui janela de 5 dia(s)) | `DB_SGD_ALL.sgd_ssc_vs_genesys` |
| `public.sgd_horario_historic` | Postgres · DB_SGD | import-sgd-diario (substitui janela de 15 dia(s)) | `DB_SGD_ALL.sgd_users_horario_historic` |
| `public.sgd_ocorrencia` | Postgres · DB_SGD | import-sgd-diario (UPDATE no lugar); import-sgd-diario (substitui por situação (não por data)) | `DB_OCORRENCIAS.sgd_ocorrencia` |
| `public.sgd_ocorrencia_area` | Postgres · DB_SGD | import-sgd-diario (recarga TOTAL) | `DB_OCORRENCIAS.sgd_ocorrencia_area` |
| `public.sgd_ocorrencia_categoria` | Postgres · DB_SGD | import-sgd-diario (recarga TOTAL) | `DB_OCORRENCIAS.sgd_ocorrencia_categoria` |
| `public.sgd_ocorrencia_prioridade` | Postgres · DB_SGD | import-sgd-diario (recarga TOTAL) | `DB_OCORRENCIAS.sgd_ocorrencia_prioridade` |
| `public.sgd_ocorrencia_sane` | Postgres · DB_SGD | import-sgd-diario (recarga TOTAL) | `DB_OCORRENCIAS.sgd_ocorrencia_sane` |
| `public.sgd_ocorrencia_setor` | Postgres · DB_SGD | import-sgd-diario (recarga TOTAL) | `DB_OCORRENCIAS.sgd_ocorrencia_setor` |
| `public.sgd_ocorrencia_situacao` | Postgres · DB_SGD | import-sgd-diario (recarga TOTAL) | `DB_OCORRENCIAS.sgd_ocorrencia_situacao` |
| `public.sgd_ocorrencia_ss` | Postgres · DB_SGD | import-sgd-diario (recarga TOTAL) | `DB_OCORRENCIAS.sgd_ocorrencia_ss` |
| `public.sgd_ocorrencia_ssc` | Postgres · DB_SGD | import-sgd-diario (recarga TOTAL) | `DB_OCORRENCIAS.sgd_ocorrencia_ssc` |
| `public.sgd_ocorrencia_tramite` | Postgres · DB_SGD | import-sgd-diario (substitui janela de 1 dia(s)) | `DB_OCORRENCIAS.sgd_ocorrencia_tramite` |
| `public.sgd_pendency` | Postgres · DB_SGD | import-sgd-diario (INSERT sem limpeza (ACUMULA)); import-sgd-diario (UPDATE no lugar) | `DB_SGD_ALL.sgd_ssc_pendency` |
| `public.sgd_preferencia_pesquisa` | Postgres · DB_SGD | import-cts (INSERT sem limpeza (ACUMULA)) | `DB_SGD_ALL.sgd_config_pref_pesquisas` |
| `public.sgd_product` | Postgres · DB_SGD | import-sgd-diario (recarga TOTAL) | `DB_SGD_ALL.sgd_product` |
| `public.sgd_product_client` | Postgres · DB_SGD | import-sgd-diario (recarga TOTAL) | `DB_SGD_ALL.sgd_client_product` |
| `public.sgd_resale` | Postgres · DB_SGD | import-sgd-diario (recarga TOTAL) | `DB_RLS.rls_user`, `DB_SGD_ALL.sgd_resales` |
| `public.sgd_sa` | Postgres · DB_SGD | import-sgd-diario (substitui janela de 1 dia(s)) | `DB_SGD_ALL.sgd_sa`, `DB_SGD_ALL.sgd_sa_description` |
| `public.sgd_sa_classification` | Postgres · DB_SGD | import-sgd-diario (recarga TOTAL) | `DB_SGD_ALL.sgd_sa_classification` |
| `public.sgd_sa_disapproval_reason` | Postgres · DB_SGD | import-sgd-diario (recarga TOTAL) | `DB_SGD_ALL.sgd_sa_disapproval_reason` |
| `public.sgd_sa_module` | Postgres · DB_SGD | import-sgd-diario (recarga TOTAL) | `DB_SGD_ALL.sgd_sa_module`, `DB_SGD_IMPLANTACAO.sgd_externo_treinamentos` |
| `public.sgd_sa_priority` | Postgres · DB_SGD | import-sgd-diario (INSERT sem limpeza (ACUMULA)) | `DB_SGD_ALL.sgd_sa_priority` |
| `public.sgd_sa_situations` | Postgres · DB_SGD | import-sgd-diario (recarga TOTAL) | `DB_SGD_ALL.sgd_sa_situations` |
| `public.sgd_sa_system` | Postgres · DB_SGD | import-sgd-diario (recarga TOTAL) | `DB_SGD_ALL.sgd_sa_system`, `DB_SGD_IMPLANTACAO.sgd_externo_treinamentos` |
| `public.sgd_sai_sane` | Postgres · DB_SGD | import-sgd-diario (recarga TOTAL) | `DB_SGD_ALL.sgd_sai_vs_sane` |
| `public.sgd_schedule` | Postgres · DB_SGD | import-agendas (substitui janela de 60 dia(s)) | `DB_SGD_ALL.sgd_schedule` |
| `public.sgd_schedule_absences_reason` | Postgres · DB_SGD | import-sgd-diario (recarga TOTAL) | `DB_SGD_ALL.sgd_schedule_absences_reason` |
| `public.sgd_schedule_absences_type` | Postgres · DB_SGD | import-sgd-diario (recarga TOTAL) | `DB_SGD_ALL.sgd_schedule_absences_type` |
| `public.sgd_schedule_past_future` | Postgres · DB_SGD | import-agendas (substitui janela de 60 dia(s)); import-agendas (substitui janela de 90 dia(s)) | `DB_SGD_ALL.sgd_schedule_past_future` |
| `public.sgd_schedule_three_days` | Postgres · DB_SGD | import-agendas (janela dos ultimos dias uteis) | `DB_SGD_ALL.sgd_schedule_three_days` |
| `public.sgd_soses` | Postgres · DB_SGD | import-sgd-diario (recarga TOTAL) | `DB_SGD_ALL.sgd_ssc_soses` |
| `public.sgd_ssc` | Postgres · DB_SGD | import-sgd-diario (substitui janela de 5 dia(s)) | `DB_SGD_ALL.sgd_ssc`, `DB_SGD_ALL.sgd_ssc_answer_time`, `DB_SGD_ALL.sgd_ssc_internal_time` |
| `public.sgd_ssc_answer_time` | Postgres · DB_SGD | import-sgd-diario (INSERT sem limpeza (ACUMULA)) | `DB_SGD_ALL.sgd_ssc_answer_time` |
| `public.sgd_ssc_classification` | Postgres · DB_SGD | import-sgd-diario (recarga TOTAL) | `DB_SGD_ALL.sgd_ssc_classification` |
| `public.sgd_ssc_disregard_dissatisfaction` | Postgres · DB_SGD | import-sgd-diario (recarga TOTAL) | `DB_SGD_ALL.sgd_ssc`, `DB_SGD_ALL.sgd_ssc_disregard_dissatisfaction` |
| `public.sgd_ssc_dissatisfaction_historic` | Postgres · DB_SGD | import-sgd-diario (substitui janela de 30 dia(s)) | `DB_SGD_ALL.sgd_ssc_dissatisfaction_historic` |
| `public.sgd_ssc_ia_chat` | Postgres · DB_SGD | import-sgd-diario (substitui janela de 5 dia(s)) | `DB_SGD_IA.sgd_ssc_ia_chat` |
| `public.sgd_ssc_internal_time` | Postgres · DB_SGD | import-sgd-diario (substitui janela de 5 dia(s)) | `DB_SGD_ALL.sgd_ssc_internal_time` |
| `public.sgd_ssc_reason_dissatisfaction` | Postgres · DB_SGD | não mapeado no Maestro | `DB_SGD_ALL.sgd_ssc_reason_dissatisfaction` |
| `public.sgd_ssc_reescrever_ia` | Postgres · DB_SGD | import-sgd-diario (substitui janela de 5 dia(s)) | `DB_SGD_IA.sgd_utilizou_reescrever_IA` |
| `public.sgd_ssc_sa` | Postgres · DB_SGD | import-sgd-diario (recarga TOTAL) | `DB_SGD_ALL.sgd_ssc_sa` |
| `public.sgd_ssc_situation` | Postgres · DB_SGD | import-sgd-diario (recarga TOTAL) | `DB_SGD_ALL.sgd_ssc_situation` |
| `public.sgd_ssc_ss` | Postgres · DB_SGD | não mapeado no Maestro | `DB_SGD_ALL.sgd_ssc_ss` |
| `public.sgd_ssc_text_conclusion` | Postgres · DB_SGD | import-sgd-diario (substitui janela de 5 dia(s)) | `DB_SGD_ALL.sgd_ssc_text_conclusion` |
| `public.sgd_ssc_tramites` | Postgres · DB_SGD | import-sgd-diario (substitui janela de 3 dia(s)) | `DB_SGD_ALL.sgd_ssc`, `DB_SGD_ALL.sgd_ssc_tramites` |
| `public.sgd_ssc_utiliza_solucao` | Postgres · DB_SGD | import-sgd-diario (substitui janela de 5 dia(s)) | `DB_SGD_ALL.sgd_ssc_pesquisa_resposta_utiliza_solucao` |
| `public.sgd_user_cargo_historico` | Postgres · DB_SGD | import-sgd-diario (recarga TOTAL) | `DB_SGD_ALL.sgd_user_position_historic` |
| `public.sgd_user_client` | Postgres · DB_SGD | import-sgd-diario (recarga TOTAL) | `DB_SGD_ALL.sgd_client_user` |
| `public.sgd_user_manager_historic` | Postgres · DB_SGD | import-sgd-diario (substitui janela de 365 dia(s)) | `DB_SGD_ALL.sgd_user_manager_historic` |
| `public.sgd_users` | Postgres · DB_SGD | import-sgd-diario (recarga TOTAL) | `DB_LOGMEIN.logmein_sessoes`, `DB_RLS.rls_user`, `DB_SGD_ALL.sgd_client`, `DB_SGD_ALL.sgd_users` |
| `public.skills` | Postgres · DB_GENESYS | genesys-import | `DB_GENESYS.genesys_areaSkillQueue`, `DB_GENESYS.genesys_historicCallsAbandoned`, `DB_GENESYS.genesys_historicCallsAgents`, `DB_GENESYS.genesys_qualificationsSkills`, `DB_GENESYS.genesys_skill` |
| `public.sla_pendency_time_snapshot` | Postgres · DB_REPORTS_CONSOLIDADOS | não mapeado no Maestro | `DB_REPORTS_CONSOLIDADOS.sla_pendency_time_snapshot` |
| `public.survey` | Postgres · DB_GENESYS | genesys-import; produtividade-pendencia-realtime | `DB_GENESYS.genesys_survey` |
| `public.survey_question` | Postgres · DB_GENESYS | não mapeado no Maestro | `DB_GENESYS.genesys_survey` |
| `public.survey_question_option` | Postgres · DB_GENESYS | não mapeado no Maestro | `DB_GENESYS.genesys_survey` |
| `public.tb_colaboradores` | Postgres · DB_REPORTS_ANALITICOS | historic-tb-colaboradores | `DB_REPORTS_ANALITICOS.tb_colaboradores` |
| `public.tb_demanda_lideres` | Postgres · DB_REPORTS_CONSOLIDADOS | historic-tb-interacoes-lideres-plug | `DB_REPORTS_CONSOLIDADOS.tb_demanda_lideres` |
| `public.tb_interacoes_lideres_plug_analitico` | Postgres · DB_REPORTS_ANALITICOS | historic-tb-interacoes-lideres-plug | `DB_REPORTS_ANALITICOS.tb_interacoes_lideres_plug_analitico` |
| `public.tb_meta_capacidade_atendimento` | Postgres · DB_REPORTS_ANALITICOS | não mapeado no Maestro | `DB_REPORTS_ANALITICOS.tb_meta_capacidade_atendimento` |
| `public.tb_ocorrencias_analitica` | Postgres · DB_REPORTS_ANALITICOS | historic-tb-ocorrencias-analitica | `DB_REPORTS_ANALITICOS.tb_ocorrencias_analitica` |
| `public.tempo_tramite_interno` | Postgres · DB_REPORTS_CONSOLIDADOS | não mapeado no Maestro | `DB_REPORTS_CONSOLIDADOS.tempo_tramite_interno` |
| `public.tenant_id` | Postgres · DB_WEBCHAT | não mapeado no Maestro | `DB_WEBCHAT.webchat_queues`, `DB_WEBCHAT.webchat_tenent` |
| `public.users` | Postgres · DB_WEBCHAT | não mapeado no Maestro | `DB_WEBCHAT.webchat_historic_status`, `DB_WEBCHAT.webchat_protocols`, `DB_WEBCHAT.webchat_users` |
| `public.users_genesys` | Postgres · DB_GENESYS | genesys-import | `DB_GENESYS.genesys_historicCallsTransfer`, `DB_GENESYS.genesys_users` |
| `public.users_historicstatus` | Postgres · DB_WEBCHAT | não mapeado no Maestro | `DB_WEBCHAT.webchat_historic_status` |
| `public.vw_protocolos_all` | Postgres · DB_WEBCHAT | não mapeado no Maestro | `DB_WEBCHAT.webchat_protocols_faturamento_detalhes` |
| `public.vw_rel_cts_gpt_saudacao` | Postgres · DB_CTS | não mapeado no Maestro | `DB_CTS.cts_config_saudacao` |
| `ss.date_entry` | Postgres · DB_SGD_N2 | não mapeado no Maestro | `DB_SGD_ALL.sgd_ss` |
| `ss.html` | Postgres · DB_SGD_N2 | não mapeado no Maestro | `DB_SGD_ALL.sgd_ss` |
| `ss.i_classification` | Postgres · DB_SGD_N2 | não mapeado no Maestro | `DB_SGD_ALL.sgd_ss`, `DB_SGD_ALL.sgd_ss_forwarding`, `DB_SGD_ALL.sgd_ss_pendency` |
| `ss.i_dissatisfied_reason` | Postgres · DB_SGD_N2 | não mapeado no Maestro | `DB_SGD_ALL.sgd_ss` |
| `ss.i_module` | Postgres · DB_SGD_N2 | não mapeado no Maestro | `DB_SGD_ALL.sgd_ss` |
| `ss.i_resales` | Postgres · DB_SGD_N2 | não mapeado no Maestro | `DB_SGD_ALL.sgd_ss`, `DB_SGD_ALL.sgd_ss_forwarding` |
| `ss.i_satisfaction` | Postgres · DB_SGD_N2 | não mapeado no Maestro | `DB_SGD_ALL.sgd_ss` |
| `ss.i_situacao` | Postgres · DB_SGD_N2 | não mapeado no Maestro | `DB_SGD_ALL.sgd_ss` |
| `ss.i_ss` | Postgres · DB_SGD_N2 | não mapeado no Maestro | `DB_SGD_ALL.sgd_ss`, `DB_SGD_ALL.sgd_ss_forwarding`, `DB_SGD_ALL.sgd_ss_pendency` |
| `ss.i_subtopic` | Postgres · DB_SGD_N2 | não mapeado no Maestro | `DB_SGD_ALL.sgd_ss` |
| `ss.i_system` | Postgres · DB_SGD_N2 | não mapeado no Maestro | `DB_SGD_ALL.sgd_ss` |
| `ss.i_topc` | Postgres · DB_SGD_N2 | não mapeado no Maestro | `DB_SGD_ALL.sgd_ss` |
| `ss.i_userreasales` | Postgres · DB_SGD_N2 | não mapeado no Maestro | `DB_SGD_ALL.sgd_ss` |
| `ss.last_update` | Postgres · DB_SGD_N2 | não mapeado no Maestro | `DB_SGD_ALL.sgd_ss` |
| `ss.ss` | Postgres · DB_SGD_N2 | import-sgd-diario (substitui janela de SS_DIAS dia(s) (default 31)) | `DB_SGD_ALL.sgd_ss`, `DB_SGD_ALL.sgd_ss_forwarding`, `DB_SGD_ALL.sgd_ss_pendency` |
| `ss.ss_category` | Postgres · DB_SGD_N2 | import-sgd-diario (recarga TOTAL) | `DB_SGD_ALL.sgd_ss_category` |
| `ss.ss_classification` | Postgres · DB_SGD_N2 | import-sgd-diario (recarga TOTAL) | `DB_SGD_ALL.sgd_ss`, `DB_SGD_ALL.sgd_ss_classification` |
| `ss.ss_conclusion_text` | Postgres · DB_SGD_N2 | import-sgd-diario (substitui janela de 5 dia(s)) | `DB_SGD_ALL.sgd_ss_dissatisfied_conclusion_text` |
| `ss.ss_disregard_dissatisfaction` | Postgres · DB_SGD_N2 | import-sgd-diario (recarga TOTAL) | `DB_SGD_ALL.sgd_ss` |
| `ss.ss_dissatisfied_reason` | Postgres · DB_SGD_N2 | não mapeado no Maestro | `DB_SGD_ALL.sgd_ss_dissatisfied_reason` |
| `ss.ss_module` | Postgres · DB_SGD_N2 | import-sgd-diario (recarga TOTAL) | `DB_SGD_ALL.sgd_ss` |
| `ss.ss_pendency` | Postgres · DB_SGD_N2 | import-sgd-diario (INSERT sem limpeza (ACUMULA)) | `DB_SGD_ALL.sgd_ss_pendency` |
| `ss.ss_satisfaction_description` | Postgres · DB_SGD_N2 | não mapeado no Maestro | `DB_SGD_ALL.sgd_ss_dissatisfied_description` |
| `ss.ss_situation` | Postgres · DB_SGD_N2 | import-sgd-diario (recarga TOTAL) | `DB_SGD_ALL.sgd_ss_forwarding`, `DB_SGD_ALL.sgd_ss_pendency_time`, `DB_SGD_ALL.sgd_ss_situation` |
| `ss.ss_sub_topic` | Postgres · DB_SGD_N2 | import-sgd-diario (recarga TOTAL) | `DB_SGD_ALL.sgd_ss` |
| `ss.ss_system` | Postgres · DB_SGD_N2 | import-sgd-diario (recarga TOTAL) | `DB_SGD_ALL.sgd_ss` |
| `ss.ss_topic` | Postgres · DB_SGD_N2 | import-sgd-diario (recarga TOTAL) | `DB_SGD_ALL.sgd_ss` |
| `ss.ss_tramites` | Postgres · DB_SGD_N2 | import-sgd-diario (substitui janela de 5 dia(s)) | `DB_SGD_ALL.sgd_ss`, `DB_SGD_ALL.sgd_ss_forwarding`, `DB_SGD_ALL.sgd_ss_pendency_time`, `DB_SGD_ALL.sgd_ss_tramite` |
| `ss.ss_tramites_time` | Postgres · DB_SGD_N2 | import-sgd-diario (recarga TOTAL) | `DB_SGD_ALL.sgd_ss`, `DB_SGD_ALL.sgd_ss_pendency_time`, `DB_SGD_ALL.sgd_ss_tramite` |
| `ss.ultimo_backup_bkn` | Postgres · DB_SGD_N2 | não mapeado no Maestro | `DB_SGD_ALL.sgd_bkn_last_backup` |
| `suporte.dados_teams_sul` | Postgres · DB_SGD | excel.main_teams_sul (UPSERT (ON CONFLICT DO UPDATE)) | `DB_SUL_INTERNO.dados_teams_sul` |
| `temp.sgd_clientcontact` | Postgres · DB_GENESYS | não mapeado no Maestro | `DB_GENESYS.genesys_historicCallsAbandoned` |
| `tria.authentication` | Postgres · DB_CTS | não mapeado no Maestro | `DB_CTS.tria_interactions` |
| `tria.chat_interacoes` | Postgres · DB_CTS | import-cts (INSERT sem limpeza (ACUMULA)) | `DB_CTS.tria_interactions` |
| `tria.chat_sit_motv` | Postgres · DB_CTS | não mapeado no Maestro | `DB_CTS.tria_situ_motv` |
