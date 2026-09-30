# Postgres · DB_GENESYS — estrutura

> Última atualização: 2026-09-29 · Fonte: catálogo `pg_catalog` lido por `scripts/catalogo_postgres.py` (sessão READ ONLY, sem leitura de dados) · **Gerado automaticamente** — não editar à mão.
> Linhas = estimativa do planner (`reltuples`), não contagem exata. Quem carrega cada tabela: `dados-postgres-destinos.md` / `dados-fluxos-maestro.md`.

| Schema | Tabelas | Views |
|---|---|---|
| `microsoft` | 1 | 0 |
| `public` | 47 | 3 |
| `telegram` | 1 | 0 |
| `temp` | 23 | 0 |

## Schema `microsoft`

- **`microsoft.token`** (tabela, ~543 linhas)
  `token` character varying(8000), `last_update` character varying

## Schema `public`

- **`public.FormsDetailUnavailability`** (tabela, ~0 linhas)
  `ddate_ocurrence` date, `detail` character varying(500), `email` character varying(500), `ddate_detail` date
- **`public.HistoricAgentAvailable_NotUsed`** (tabela, ~109.2 mil linhas)
  `user_id` text, `ddate` text, `dtime` text, `tsystempresence` numeric, `tagentroutingstatus` numeric, `torganizationpresence` numeric, `q_tsystempresence` text, `q_tagentroutingstatus` text, `q_torganizationpresence` text
- **`public.HistoricAgentStatus`** (tabela, ~16.6 mi linhas)
  `dDateStart` date, `dTime` text, `id_user` text, `id_presenceDef` text, `nameSystemPresence` text, `nameSecondPresence` text, `dTimeStart` text, `dTimeEnd` text, `duration` integer
- **`public.HistoricAgentStatusLista`** (tabela, ~9.9 mi linhas)
  `id_user` text, `id_presenceDef` text, `dDateStart` date, `dDateEnd` date, `dTimeStart` text, `dTimeEnd` text, `dIntervalStart` text, `dIntervalEnd` text, `dTime_total` numeric, `startDateTime` text, `endDateTime` text
- **`public.TTEC_calls2022`** (tabela, ~670.7 mil linhas)
  `date_interval` character varying, `time_interval` character varying, `_nAnswered` integer, `_nHandle` integer, `_tHandle` integer, `_nTransferred` integer, `i_usuarios` integer, `i_meios_acessos` integer
- **`public.Users_SGD_CUIC`** (tabela, ~819 linhas)
  `i_usuarios` integer, `AgentSkillID` integer, `usuario` character varying, `AgentEnterpriseName` character varying, `nome` character varying, `email` character varying, `NomeGestor` character varying, `NomeGerente` character varying, `unidade` character varying, `admissao` text, `Situation` character varying
- **`public._parametros`** (tabela, ~2 linhas)
  `hora_in_atualiza` text, `hora_fim_atualiza` text, `status` boolean, `id` integer
- **`public.agentAvailable`** (tabela, ~40.4 mi linhas)
  `user_id` text, `ddate` text, `dtime` text, `interacting` numeric, `available` numeric, `busy` numeric, `on_queue` numeric, `idle` numeric, `offline` numeric, `away` numeric, `break` numeric, `meal` numeric, `meeting` numeric, `training` numeric, `not_responding` numeric
- **`public.analytics_login`** (tabela, ~1.2 mil linhas · PK (id_seq_login))
  `id_seq_login` integer, `user_sgd` text, `horario_login` timestamp without time zone
- **`public.analytics_relatorios_gerados`** (tabela, ~1.9 mil linhas · PK (id))
  `id` integer, `user_sgd` character varying(100), `data_hora` timestamp without time zone, `data_inicio` date, `data_fim` date, `tipo_relatorio` character varying(50), `filtros_regioes` text, `filtros_areas` text, `filtros_filas` text, `tipo_ligacao` character varying(20), `todas_filas` boolean, `nome_arquivo` character varying(255), `total_registros` integer, `observacoes` text
- **`public.cad_alocations`** (tabela, ~96 linhas)
  `i_alocation` integer, `descricao` character varying(100), `abreviatura` character varying(50), `area` integer
- **`public.callsWithClient`** (tabela, ~21.3 mi linhas)
  `conversation_id` character varying, `i_client` integer, `name_contact` character varying
- **`public.calls_agents_halfHour`** (tabela, ~6.3 mi linhas)
  `date_interval` text, `id_user` text, `time_interval` text, `_nAnswered` numeric, `_tAnswered` numeric, `_tAnsweredMax` numeric, `_tAnsweredMin` numeric, `_nHandle` numeric, `_tHandle` numeric, `_tHandleMax` numeric, `_tHandleMin` numeric, `_nTalkComplete` numeric, `_tTalkComplete` numeric, `_tTalkCompleteMax` numeric, `_tTalkCompleteMin` numeric, `_tHeldComplete` numeric, `_nAcw` numeric, `_tAcw` numeric, `_tAcwMax` numeric, `_tAcwMin` numeric, `_nDialing` numeric, `_tDialing` numeric, `_tDialingMax` numeric, `_tDialingMin` numeric, `_nContacting` numeric, `_tContacting` numeric, `_tContactingMax` numeric, `_tContactingMin` numeric, `_nTransferred` numeric, `_nOutbound` numeric, `_nNotResponding` numeric, `_tNotResponding` numeric, `_tNotRespondingMax` numeric, `_tNotRespondingMin` numeric, `_nAlert` numeric, `_tAlert` numeric, `_tAlertMax` numeric, `_tAlertMin` numeric, `_nMonitoring` numeric, `_tMonitoring` numeric, `_tMonitoringMax` numeric, `_tMonitoringMin` numeric, `_nBlindTransferred` numeric, `_nConsultTransferred` numeric, `direction` text, `_queue` text
- **`public.dCalendar`** (tabela, ~1.1 mil linhas)
  `Date` date, `Day` integer, `DayName` character varying, `Month` integer, `MonthName` character varying, `DayOfWeek` integer, `DayOfYear` integer, `Holiday` character varying, `Ten` integer, `TenName` character(2), `DayUsefulOfMonth` integer, `DayUsefulOfYear` integer, `Year` integer
- **`public.dTime`** (tabela, ~48 linhas)
  `dTime` text
- **`public.historic_callsAbandoned`** (tabela, ~797.5 mil linhas)
  `conversation_id` text, `metric_tAbandon` numeric, `dateTime_start` timestamp without time zone, `dateTime_end` timestamp without time zone, `dtime_start` text, `dtime_end` text, `queue_id` text, `skill_id_1` text, `skill_id_2` text, `_ani` text, `removed_skill` text, `session_id` text, `_mos` numeric
- **`public.historic_callsAgents`** (tabela, ~7.8 mi linhas)
  `conversation_id` text, `user_id` text, `metric_tAcd` numeric, `metric_tAcw` numeric, `metric_tTalkComplete` numeric, `metric_tIvr` numeric, `metric_tHeldComplete` numeric, `metric_tAlert` numeric, `metric_tAbandon` numeric, `metric_nTransferred` numeric, `metric_tTalk` numeric, `metric_tHeld` numeric, `metric_nOutboundAttempted` numeric, `metric_tContacting` numeric, `metric_tDialing` numeric, `metric_tHandle` numeric, `metric_nBlindTransferred` numeric, `metric_nConsult` numeric, `metric_nConsultTransferred` numeric, `metric_oMediaCount` numeric, `metric_oExternalMediaCount` numeric, `metric_tVoicemail` numeric, `metric_tMonitoring` numeric, `metric_tFlowOut` numeric, `metric_nOffered` numeric, `metric_tAnswered` numeric, `metric_nNotResponding` numeric, `metric_tNotResponding` numeric, `dateTime_start` timestamp without time zone, `dateTime_end` timestamp without time zone, `dtime_start` text, `dtime_end` text, `queue_id` text, `skill_id_1` text, `skill_id_2` text, `bullseye` numeric, `direction` text, `purpose` text, `disconnecttype` text, `wrapupcode` text, `_ani` text, `_dnis` text, `removed_skill` text, `session_id` text, `_mos` numeric, `survey_id` text, `disconnecttype_out` character varying(40)
- **`public.historic_callsTranfers`** (tabela, ~2 mil linhas)
  `conversation_id` text, `queue_name` text, `dateTime_start` timestamp without time zone, `dateTime_end` timestamp without time zone, `_user` text, `disconnect` text, `rona` integer
- **`public.historic_callsTranfers_OLD`** (tabela, ~41.7 mil linhas)
  `conversation_id` text, `queue_name` text, `dateTime_start` timestamp without time zone, `dateTime_end` timestamp without time zone
- **`public.historic_calls_ia`** (tabela, ~1.2 mi linhas)
  `conversation_id` text, `session_id` text, `resumo` text, `problema_1` text, `problema_2` text, `frustacoes` text, `dificuldades` text, `analise_especifica` text, `analise_saudacao` text, `analise_telefonia` text
- **`public.historic_calls_ia_new`** (tabela, ~605.9 mil linhas)
  `conversation_id` text, `session_id` text, `qtd_duvidas_ligacoes` text, `justificativa_qtd_duvidas_ligacoes` text, `categoria_duvidas1` text, `categoria_duvidas2` text, `categoria_duvidas3` text, `categoria_duvidas4` text, `categoria_duvidas5` text, `categoria_duvidas6` text, `cliente_recorrente` text, `cliente_novo` text, `resistencia_cliente_finalizar_ligacao` text, `justificativa_resistencia` text, `resolvido_em_linha` text, `resumo_conversa` text, `tema_novo` text, `cliente_insistencia_acesso_remoto` text, `tentativa_e_erro` text, `justificativa_tentativa_e_erro` text, `acompanha_acesso_remoto` text, `resumo_breve` text, `problema_principal` text, `problemas_secundarios` text, `frustracao_cliente` text, `dificuldades_atendimento` text, `classificacao_especifica` text, `saudacao_agent` text, `qualidade_chamada` text, `anomalia_qualidade_atendimento` text, `anomalia_justificativa_ia` text, `tipos_de_anomalia` text, `tipo_anomalia_analista` text, `tipos_de_desconsiderado` text, `nivel_confianca` text, `justificativa_confianca` text, `mencao_pesquisa` text
- **`public.historic_calls_ia_resumos`** (tabela, ~3.8 mil linhas)
  `hora_insercao` timestamp without time zone, `origem` text, `resumo` text
- **`public.historic_calls_ia_resumos_new`** (tabela, ~3.9 mil linhas)
  `hora_insercao` timestamp without time zone, `origem` text, `resumo` text
- **`public.historic_calls_transcript`** (tabela, ~4.7 mi linhas)
  `conversation_id` text, `session_id` text, `transcript` text
- **`public.historic_qualifications`** (tabela, ~553.3 mil linhas)
  `skill_id_1` text, `skill_id_2` text, `date_interval` character varying(10), `time_interval` character varying(5), `metric_nOffered` numeric, `metric_nAnswered` numeric, `metric_tAnswered` numeric, `metric_tAnsweredMax` numeric, `metric_tAnsweredMin` numeric, `metric_nAbandon` numeric, `metric_tAbandon` numeric, `metric_tAbandonMax` numeric, `metric_tAbandonMin` numeric, `metric_tFlowOut` numeric, `metric_oServiceLevel` numeric, `metric_oServiceTarget` numeric, `metric_nHandle` numeric, `metric_tHandle` numeric, `metric_tHandleMax` numeric, `metric_tHandleMin` numeric, `metric_nTalkComplete` numeric, `metric_tTalkComplete` numeric, `metric_tTalkCompleteMax` numeric, `metric_tTalkCompleteMin` numeric, `metric_tHeldComplete` numeric, `metric_nAcw` numeric, `metric_tAcw` numeric, `metric_tAcwMax` numeric, `metric_tAcwMin` numeric, `metric_nTransferred` numeric, `metric_nOverSla` numeric, `metric_tShortAbandon` numeric, `metric_nWait` numeric, `metric_tWait` numeric, `metric_tWaitMax` numeric, `metric_tWaitMin` numeric, `metric_nOutboundAttempted` numeric, `metric_tVoicemail` numeric, `metric_tAbandon60` numeric, `metric_tAbandon120` numeric, `metric_tAbandon180` numeric, `metric_tAbandon300` numeric, `metric_tAbandon600` numeric, `metric_tAbandonMore600` numeric
- **`public.historic_qualifications_gran1`** (tabela, ~5.6 mi linhas)
  `skill_id_1` text, `skill_id_2` text, `date_interval` character varying(10), `time_interval` character varying(5), `metric_nOffered` numeric, `metric_nAnswered` numeric, `metric_tAnswered` numeric, `metric_tAnsweredMax` numeric, `metric_tAnsweredMin` numeric, `metric_nAbandon` numeric, `metric_tAbandon` numeric, `metric_tAbandonMax` numeric, `metric_tAbandonMin` numeric, `metric_tFlowOut` numeric, `metric_oServiceLevel` numeric, `metric_oServiceTarget` numeric, `metric_nHandle` numeric, `metric_tHandle` numeric, `metric_tHandleMax` numeric, `metric_tHandleMin` numeric, `metric_nTalkComplete` numeric, `metric_tTalkComplete` numeric, `metric_tTalkCompleteMax` numeric, `metric_tTalkCompleteMin` numeric, `metric_tHeldComplete` numeric, `metric_nAcw` numeric, `metric_tAcw` numeric, `metric_tAcwMax` numeric, `metric_tAcwMin` numeric, `metric_nTransferred` numeric, `metric_nOverSla` numeric, `metric_tShortAbandon` numeric, `metric_nWait` numeric, `metric_tWait` numeric, `metric_tWaitMax` numeric, `metric_tWaitMin` numeric, `metric_nOutboundAttempted` numeric, `metric_tVoicemail` numeric, `metric_tAbandon60` numeric, `metric_tAbandon120` numeric, `metric_tAbandon180` numeric, `metric_tAbandon300` numeric, `metric_tAbandon600` numeric, `metric_tAbandonMore600` numeric, `time_gran5` text, `time_gran10` text, `time_gran15` text, `time_gran20` text, `time_gran30` text
- **`public.presenceDefinitions`** (tabela, ~20 linhas · PK (id_SystemPresence))
  `id_SystemPresence` text, `nameSystemPresence` text, `nameSecondPresence` text, `primaryStatus` boolean
- **`public.queue`** (tabela, ~154 linhas · PK (id_queue)) — Cadastro das filas
  `id_queue` text, `name_queue` text, `area` text, `description` text, `region` text
- **`public.queue_Performance`** (tabela, ~521.2 mil linhas)
  `date_interval` text, `id_queue` text, `time_interval` text, `_nOffered` numeric, `_tAnswered` numeric, `_tAbandon` numeric, `_nOutbound` numeric, `_tFlowOut` numeric, `_nConnected` numeric, `_oServiceLevel` numeric, `_tWait` numeric, `_tWaitMax` numeric, `_tWaitMin` numeric, `_tHandle` numeric, `_tHandleMin` numeric, `_tHandleMax` numeric, `_tTalkComplete` numeric, `_tTalkCompleteMax` numeric, `_tTalkCompleteMin` numeric, `_tHeldComplete` numeric, `_tAcw` numeric, `_tAcd` numeric, `_tAcMax` numeric, `_tAcdMin` numeric, `_tDialing` numeric, `_tContacting` numeric, `_nTransferred` numeric, `_nBlindTransferred` numeric, `_nConsult` numeric, `_nConsultTransferred` numeric, `_oExternalMediaCount` numeric, `_oMediaCount` numeric, `_nOverSla` numeric, `_tShortAbandon` numeric, `_nOutboundAttempted` numeric, `_tVoicemail` numeric, `_nError` numeric
- **`public.queue_performance_gran1`** (tabela, ~2 mi linhas)
  `date_interval` text, `id_queue` text, `time_interval` text, `_nOffered` numeric, `_tAnswered` numeric, `_tAbandon` numeric, `_nOutbound` numeric, `_tFlowOut` numeric, `_nConnected` numeric, `_oServiceLevel` numeric, `_tWait` numeric, `_tWaitMax` numeric, `_tWaitMin` numeric, `_tHandle` numeric, `_tHandleMin` numeric, `_tHandleMax` numeric, `_tTalkComplete` numeric, `_tTalkCompleteMax` numeric, `_tTalkCompleteMin` numeric, `_tHeldComplete` numeric, `_tAcw` numeric, `_tAcd` numeric, `_tAcMax` numeric, `_tAcdMin` numeric, `_tDialing` numeric, `_tContacting` numeric, `_nTransferred` numeric, `_nBlindTransferred` numeric, `_nConsult` numeric, `_nConsultTransferred` numeric, `_oExternalMediaCount` numeric, `_oMediaCount` numeric, `_nOverSla` numeric, `_tShortAbandon` numeric, `_nOutboundAttempted` numeric, `_tVoicemail` numeric, `_nError` numeric, `time_gran5` text, `time_gran10` text, `time_gran15` text, `time_gran20` text, `time_gran25` text, `time_gran30` text
- **`public.queues_InUser`** (tabela, ~8.8 mil linhas)
  `id_user` text, `id_queue` text, `bullseyeRouting` integer
- **`public.sgd_alocations`** (tabela, ~3.4 mi linhas)
  `ddate` character varying(10), `i_user` integer, `i_alocation` integer, `apartir_de` character varying(10), `id_user_genesys` text
- **`public.sgd_genesys`** (tabela externa, — linhas)
  `i_ssc` integer, `cadastro_ia` integer, `id_transcricao_anexo` integer, `id_ligacao` integer, `tags` character varying, `conversation_id` character varying(50)
- **`public.sgd_ssc`** (tabela externa, — linhas)
  `code_ssc` integer, `i_ssc` integer, `date_entry` character varying(10), `date_time` timestamp without time zone, `i_classification` integer, `system` character varying(40), `module` character varying(40), `topic` character varying, `subtopic` character varying, `i_means_of_access` integer, `lista_ss` character varying, `i_clientes` integer, `i_user` integer, `total_procedures_waiting_answer` integer, `total_procedures` integer, `time_before_first_analysis` integer, `time_total` integer, `time_medium` integer, `dateconclusion` character varying(10), `time_ss` integer, `time_ssql` integer, `bond_sa_ne` integer, `disapproval` character varying(10), `time_bond_sa_ne` integer, `time_phone` integer, `time_final_support` integer, `time_final_client` integer, `time_last_procedure_without_analysis` integer, `number_procedure_conclusion` integer, `satisfaction_ssc` character varying(12), `i_ssc_satisfaction_reason` integer, `i_user_resales` integer, `number_procedure_attachement` integer, `bond_attachment_sa_ne` integer, `time_scd` integer, `priority` integer, `no_acess_system` integer, `dtime` character varying(5), `ia_register` integer
- **`public.sgd_ssc_genesys`** (tabela, ~1.3 mi linhas)
  `ssc_i_ssc` integer, `conversation_id` character varying, `ssc_system` character varying, `ssc_module` character varying, `ssc_topic` character varying, `ssc_subtopic` character varying
- **`public.skills`** (tabela, ~151 linhas · PK (id_skill)) — Cadastro das Filas
  `id_skill` text, `name_skill` text, `area` text, `regional` text
- **`public.skills_InUser`** (tabela, ~6 mil linhas) — Filas que estão alocadas nos usuários
  `id_user` text, `id_skill` text
- **`public.survey`** (tabela, ~131.4 mil linhas)
  `survey_id` text, `user_id` text, `question_id` text, `answer_id` text
- **`public.survey_question`** (tabela, ~3 linhas)
  `question_id` text, `question` text, `question_resume` text, `question_order` integer
- **`public.survey_question_option`** (tabela, ~5 linhas)
  `question_id` text, `answer_id` text, `answer` text
- **`public.users_Genesys`** (tabela, ~1.1 mil linhas) — Tabela que salva os usuários da nossa divisão dentro da Genesys.
  `id_user` text, `email` text, `name` text, `status` text, `supervisor` text, `jabber_id` text, `department` text, `gerente` text, `role_genesys` text, `lider` boolean, `lider_area` text
- **`public.users_Plug`** (tabela, ~554 linhas · PK (i_user_plug))
  `i_user_plug` character varying(50), `i_user_sgd` integer, `name` character varying(255), `email` character varying(255), `username` character varying(255), `perfil` character varying(100), `supervisor` character varying(255), `gerente` character varying(255), `status` character varying(20), `tenant_id` character varying(50), `updated_at` timestamp without time zone
- **`public.users_SGD`** (tabela, ~1.1 mil linhas · PK (i_usuarios)) — Tabela que salva os usuários do SGD com base nos e-mails cadastrados na central Genesys
  `i_usuarios` numeric, `usuario` text, `email` text, `admissao` text, `demissao` text, `nome` text
- **`public.validacaoImportacao`** (tabela, ~0 linhas)
  `idConf` integer, `maxSSC` integer, `maxdatahoratramite` character varying, `conexao` character varying, `ultimaatualizacao` character varying
- **`public.vw_analytics_relatorio_ligacoes`** (view, — linhas)
  `ID Conversa` text, `Data` date, `Data/Hora Completa` timestamp without time zone, `Área` text, `Nome da Fila` text, `Região` text, `id_queue` text, `direction` text, `Tipo de Ligação` text, `DNIS` text, `ANI` text, `Tipo de desconexão` text, `Agente` text, `Coordenador` text, `Gerente` text, `Teve Transferência` text, `Início Ligação` time without time zone, `Fim da Ligação` time without time zone, `T.Segundos de espera na Fila` numeric, `T.Segundos da Interação` numeric, `T.Segundos cliente na espera durante Atendimento` numeric, `Resumo da Ligação` text, `Problema Principal` text, `Seq SSC` integer, `Módulo` character varying, `Tópico` character varying, `Transcrição` text
- **`public.vw_analytics_relatorio_ligacoes_new`** (view, — linhas)
  `ID Conversa` text, `Data` date, `Data/Hora Completa` timestamp without time zone, `Área` text, `Nome da Fila` text, `Região` text, `id_queue` text, `direction` text, `Tipo de Ligação` text, `DNIS` text, `ANI` text, `Tipo de desconexão` text, `Agente` text, `Coordenador` text, `Gerente` text, `Teve Transferência` text, `Início Ligação` time without time zone, `Fim da Ligação` time without time zone, `T.Segundos de espera na Fila` numeric, `T.Segundos da Interação` numeric, `T.Segundos cliente na espera durante Atendimento` numeric, `IA Qtd Duvidas Ligacoes` text, `IA Justificativa Qtd Duvidas Ligacoes` text, `IA Categoria Duvidas 1` text, `IA Categoria Duvidas 2` text, `IA Categoria Duvidas 3` text, `IA Categoria Duvidas 4` text, `IA Categoria Duvidas 5` text, `IA Categoria Duvidas 6` text, `IA Cliente Recorrente` text, `IA Cliente Novo` text, `IA Resistencia Cliente Finalizar Ligacao` text, `IA Justificativa Resistencia` text, `IA Resolvido Em Linha` text, `IA Resumo Conversa` text, `IA Tema Novo` text, `IA Cliente Insistencia Acesso Remoto` text, `IA Tentativa e Erro` text, `IA Justificativa Tentativa e Erro` text, `IA Acompanha Acesso Remoto` text, `IA Resumo Breve` text, `IA Problema Principal` text, `IA Problemas Secundarios` text, `IA Frustracao Cliente` text, `IA Dificuldades Atendimento` text, `IA Classificacao Especifica` text, `IA Saudacao Agent` text, `IA Qualidade Chamada` text, `IA Anomalia Qualidade Atendimento` text, `IA Anomalia Justificativa IA` text, `IA Tipos de Anomalia` text, `IA Tipo Anomalia Analista` text, `IA Tipos de Desconsiderado` text, `IA Nivel Confianca` text, `IA Justificativa Confianca` text, `Mencao à Pesquisa` integer, `Seq SSC` integer, `Módulo` character varying, `Tópico` character varying, `GENESYS Problema Resolvido` text, `GENESYS Satisfação Atendente` text, `GENESYS Detalhe da Votação` text, `Transcrição` text
- **`public.vw_ligacoes_problemas_geral`** (view, — linhas)
  `total` bigint, `name` text, `supervisor` text, `data_ligacao` date
- **`public.vw_sgd_ssc`** (tabela externa, — linhas)
  `i_ssc` integer, `code_ssc` integer, `system` character varying(40), `module` character varying(40), `topic` character varying, `subtopic` character varying
- **`public.vw_sgd_ssc_id_genesys`** (tabela externa, — linhas)
  `i_ssc` integer, `conversation_id` character varying(50), `system` character varying(40), `module` character varying(40), `topic` character varying, `subtopic` character varying
- **`public.wrapupcodes`** (tabela, ~83 linhas · PK (id)) — Cadastro de WrapUpCodes
  `id` text, `name` text, `dateCreated` text, `createdBy` text, `dateModified` text, `modifiedBy` text

## Schema `telegram`

- **`telegram.notifica_teste`** (tabela, ~5 linhas)
  `id` integer, `descricao` character varying

## Schema `temp`

- **`temp.SGD_ClientContact`** (tabela, ~472.6 mil linhas)
  `i_contatos` integer, `i_clientes` integer, `numero_telefone` character varying, `nome` character varying, `ultimo_digitos` character varying(10)
- **`temp.agentAvailable`** (tabela, ~15.9 mil linhas)
  `user_id` text, `ddate` text, `dtime` text, `interacting` numeric, `available` numeric, `busy` numeric, `on_queue` numeric, `idle` numeric, `offline` numeric, `away` numeric, `break` numeric, `meal` numeric, `meeting` numeric, `training` numeric, `not_responding` numeric
- **`temp.alocation`** (tabela, ~480 linhas)
  `email` text, `alocation` text
- **`temp.disconnecttype`** (tabela, ~9 linhas)
  `id_type` text, `desc_type` text
- **`temp.historic_callsAgents`** (tabela, ~5.4 mil linhas)
  `conversation_id` text, `user_id` text, `metric_tAcd` numeric, `metric_tAcw` numeric, `metric_tTalkComplete` numeric, `metric_tIvr` numeric, `metric_tHeldComplete` numeric, `metric_tAlert` numeric, `metric_tAbandon` numeric, `metric_nTransferred` numeric, `metric_tTalk` numeric, `metric_tHeld` numeric, `metric_nOutboundAttempted` numeric, `metric_tContacting` numeric, `metric_tDialing` numeric, `metric_tHandle` numeric, `metric_nBlindTransferred` numeric, `metric_nConsult` numeric, `metric_nConsultTransferred` numeric, `metric_oMediaCount` numeric, `metric_oExternalMediaCount` numeric, `metric_tVoicemail` numeric, `metric_tMonitoring` numeric, `metric_tFlowOut` numeric, `metric_nOffered` numeric, `metric_tAnswered` numeric, `metric_nNotResponding` numeric, `metric_tNotResponding` numeric, `dateTime_start` timestamp without time zone, `dateTime_end` timestamp without time zone, `dtime_start` text, `dtime_end` text, `queue_id` text, `skill_id_1` text, `skill_id_2` text, `bullseye` numeric, `direction` text, `purpose` text, `disconnecttype` text, `wrapupcode` text, `_ani` text, `_dnis` text, `removed_skill` text, `_record` timestamp without time zone, `session_id` text, `_mos` numeric, `survey_id` text
- **`temp.historic_callsTranfers`** (tabela, ~1.1 mil linhas)
  `conversation_id` text, `queue_name` text, `dateTime_start` timestamp without time zone, `dateTime_end` timestamp without time zone
- **`temp.historic_qualifications`** (tabela, ~412 linhas)
  `skill_id_1` text, `skill_id_2` text, `date_interval` character varying(10), `time_interval` character varying(5), `metric_nOffered` numeric, `metric_nAnswered` numeric, `metric_tAnswered` numeric, `metric_tAnsweredMax` numeric, `metric_tAnsweredMin` numeric, `metric_nAbandon` numeric, `metric_tAbandon` numeric, `metric_tAbandonMax` numeric, `metric_tAbandonMin` numeric, `metric_tFlowOut` numeric, `metric_oServiceLevel` numeric, `metric_oServiceTarget` numeric, `metric_nHandle` numeric, `metric_tHandle` numeric, `metric_tHandleMax` numeric, `metric_tHandleMin` numeric, `metric_nTalkComplete` numeric, `metric_tTalkComplete` numeric, `metric_tTalkCompleteMax` numeric, `metric_tTalkCompleteMin` numeric, `metric_tHeldComplete` numeric, `metric_nAcw` numeric, `metric_tAcw` numeric, `metric_tAcwMax` numeric, `metric_tAcwMin` numeric, `metric_nTransferred` numeric, `metric_nOverSla` numeric, `metric_tShortAbandon` numeric, `metric_nWait` numeric, `metric_tWait` numeric, `metric_tWaitMax` numeric, `metric_tWaitMin` numeric, `metric_nOutboundAttempted` numeric, `metric_tVoicemail` numeric, `metric_tAbandon60` numeric, `metric_tAbandon120` numeric, `metric_tAbandon180` numeric, `metric_tAbandon300` numeric, `metric_tAbandon600` numeric, `metric_tAbandonMore600` numeric
- **`temp.newRealTimeStatus`** (tabela, ~0 linhas)
  `user_id` character varying, `routingstatus` character varying, `presence` character varying, `hora_consulta` character varying, `temporoutingstatus` character varying
- **`temp.notifica_agents_ligacoes`** (tabela, ~1.8 mil linhas)
  `conversation_id` text, `user_id` text
- **`temp.plugRealTimeStatus`** (tabela, ~0 linhas)
  `i_user_plug` character varying(50), `i_user_sgd` character varying(20), `name` character varying(255), `email` character varying(255), `perfil` character varying(100), `status` character varying(100), `online` boolean, `time_in_status_minutes` integer, `hora_consulta` timestamp without time zone
- **`temp.projetado_meia_hora`** (tabela, ~12.6 mil linhas)
  `data` date, `area` text, `demanda_acum` integer, `meia_hora` text, `demanda_proj` integer, `tme_proj` time without time zone, `tme_acu` time without time zone
- **`temp.projetado_pessoas`** (tabela, ~12.6 mil linhas)
  `data` date, `area` text, `meia_hora` text, `fte_presente` numeric(10,2), `indisponibilidade_proj` numeric(6,2)
- **`temp.queues_InUser`** (tabela, ~5.3 mil linhas)
  `id_user` text, `id_queue` text, `bullseyeRouting` integer
- **`temp.realTime_status`** (tabela, ~8.9 mil linhas)
  `user_id` character varying, `presence_id` character varying, `tempo_status` character varying, `hora_consulta` character varying, `routingstatus` character varying, `temporoutingstatus` character varying
- **`temp.realtime_queues`** (tabela, ~0 linhas)
  `id_queue` text, `skill_1` text, `skill_2` text, `_time` text, `phone` text, `phone_10` text, `total` text
- **`temp.realtime_queues_metrics`** (tabela, ~0 linhas)
  `id_queue` text, `active_users` text, `member_users` text, `off_queue_users` text, `on_queue_users` text
- **`temp.realtime_queues_teste`** (tabela, ~92 linhas)
  `id_queue` text, `skill_1` text, `skill_2` text, `_time` text, `phone` text, `phone_10` text, `total` integer
- **`temp.sgd_alocation_reg`** (tabela, ~96 linhas)
  `i_alocation` integer, `alocation` character varying, `area` character varying, `meio_acesso_alocacao` character varying
- **`temp.sgd_client`** (tabela, ~241.5 mil linhas)
  `I_clientes` integer, `NameClient` character varying(100), `I_representantes` integer, `I_revenda` integer, `ResaleSmallName` character varying(20), `DateRegister` character varying(10), `Referencial` character varying(3), `Cep` character varying(8), `City` character varying(60), `InitialsState` character varying(2), `State` character varying(30), `numberOfUsers` integer, `Phone` character varying(50), `DateIniPrestServ` character varying(10), `DateAssin` character varying(10), `Situation` integer
- **`temp.tb_genesys_grupos`** (tabela, ~304 linhas · PK (id_grupo))
  `id_grupo` character varying, `nome_grupo` character varying, `tipo_grupo` character varying, `data_carga` timestamp without time zone
- **`temp.tb_genesys_usuario_fila`** (tabela, ~6.7 mil linhas · PK (id_usuario, id_fila))
  `id_usuario` character varying, `id_fila` character varying, `data_carga` timestamp without time zone
- **`temp.tb_genesys_usuario_grupo`** (tabela, ~1 mil linhas · PK (id_usuario, id_grupo))
  `id_usuario` character varying, `id_grupo` character varying, `data_carga` timestamp without time zone
- **`temp.users_incall`** (tabela, ~0 linhas)
  `id_user` text, `id_queue` text
