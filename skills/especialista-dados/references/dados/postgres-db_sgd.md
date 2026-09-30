# Postgres · DB_SGD — estrutura

> Última atualização: 2026-09-29 · Fonte: catálogo `pg_catalog` lido por `scripts/catalogo_postgres.py` (sessão READ ONLY, sem leitura de dados) · **Gerado automaticamente** — não editar à mão.
> Linhas = estimativa do planner (`reltuples`), não contagem exata. Quem carrega cada tabela: `dados-postgres-destinos.md` / `dados-fluxos-maestro.md`.

| Schema | Tabelas | Views |
|---|---|---|
| `externo` | 11 | 0 |
| `forecast` | 13 | 0 |
| `genesys` | 3 | 0 |
| `logmein` | 1 | 0 |
| `public` | 63 | 1 |
| `suporte` | 1 | 0 |
| `temp` | 11 | 0 |

## Schema `externo`

- **`externo.categoria`** (tabela, ~0 linhas)
  `id_categoria` integer, `desc_categoria` character varying
- **`externo.forma_treinamento`** (tabela, ~0 linhas)
  `id_forma_treinamento` integer, `desc_forma_treinamento` character varying
- **`externo.implantacao`** (tabela, ~219.6 mil linhas)
  `id_externos` integer, `id_revendas` integer, `tipo` integer, `entrada` character varying, `atualizacao` character varying, `id_clientes` integer, `i_usuarios` integer, `i_responsaveis` integer, `i_situacoes` integer, `i_contratos` integer, `tempo_treinamento` integer, `tempo_treinamento_realizadas` integer, `prazo_limite_iniciar` character varying, `prazo_limite_concluir` character varying, `quantidade_dias_produto` integer, `numero_usuarios` integer, `i_produtos` integer, `i_cm_contratos` integer, `prazo_limte_concluir_antiga` character varying, `tempo_original` integer, `id_forma_treinamento` integer, `id_adendos` integer, `servidor` integer, `i_usuarios_coordenador` integer, `i_usuarios_pos_venda` integer, `i_usuarios_tecnico` integer, `i_usuarios_assistente` integer, `i_produtos_anterior` integer, `configuracao` integer, `modelo_treinamento` integer, `i_responsaveis_cliente_implantacao` integer, `prazo_limite_concluir_passagem_bastao` character varying, `i_pos_venda` integer, `origem` integer
- **`externo.local_treinamento`** (tabela, ~8 linhas)
  `id_local` integer, `desc_local` character varying
- **`externo.motivo_treinamento`** (tabela, ~0 linhas)
  `id_motivo` integer, `id_situacao` integer, `desc_motivo` character varying
- **`externo.programacao`** (tabela, ~1 mi linhas)
  `id_programacoes` integer, `id_externos` integer, `descricao` character varying, `dt_inicio` character varying, `duracao` integer, `id_usuarios_resp` integer, `id_situacoes` integer, `tempo_treinamento` integer, `instrucoes` character varying, `id_local_treinamento` integer, `id_categorias` integer, `id_usuarios_cadastro` integer
- **`externo.situacoes`** (tabela, ~0 linhas)
  `id_situacao` integer, `desc_situacao` character varying, `id_situacao_grupo` integer
- **`externo.treinamento`** (tabela, ~341 linhas)
  `id_treinamento` integer, `sigla` character varying, `id_tipo` integer, `desc_treinamento` character varying, `id_situacao` integer, `id_sistemas` integer, `id_modulos` integer
- **`externo.treinamento_conteudo`** (tabela, ~1.4 mil linhas)
  `id_conteudo` integer, `id_treinamento` integer, `ordem` integer, `descricao` character varying, `detalhamento` character varying, `tempo` integer, `id_situacao` integer, `concluido` integer
- **`externo.treinamento_programacao`** (tabela, ~7.8 mi linhas)
  `id_treinamento_programacao` integer, `id_externo` integer, `id_programacoes` integer, `id_treinamento` integer, `id_conteudo` integer, `id_situacao` integer, `concluido` integer, `prazo` character varying, `i_produtos` integer, `entrada` character varying
- **`externo.treinamento_programacao_usuario`** (tabela, ~2 mi linhas)
  `id_programacao_usuarios` integer, `id_programacoes` integer, `id_treinamento` integer, `i_usuarios` integer, `i_programacao_categoria` integer, `i_categorias` integer

## Schema `forecast`

- **`forecast.ajuste_demanda`** (tabela, ~313 linhas)
  `ini` character varying(10), `fim` character varying(10), `vlr_ajuste` numeric, `area` character varying, `gerente` character varying
- **`forecast.ausencias_projetado`** (tabela, ~5.5 mil linhas)
  `ini` character varying(10), `fim` character varying(10), `area` character varying, `total` numeric, `tipo` character varying, `reg` character varying
- **`forecast.calls`** (tabela, ~0 linhas)
  `date` character varying(10), `offered` numeric, `answered` numeric, `queue` character varying, `skill` character varying
- **`forecast.client_user_history`** (tabela, ~76.4 mi linhas)
  `firstdaymonth` character varying(10), `i_client` numeric, `i_contrat` numeric, `dateregister` character varying(10), `totusers` numeric, `i_product` numeric
- **`forecast.coefficient`** (tabela, ~2.7 mil linhas)
  `date` character varying(10), `calls_folha` character varying, `calls_fiscont` character varying, `calls_funcional` character varying, `coeff_geral` character varying, `perc_folha` character varying, `coeff_folha` character varying, `perc_fiscont` character varying, `coeff_fiscont` character varying, `calls_at` character varying, `coeff_at` character varying, `unity` text
- **`forecast.de_para_alocacao`** (tabela, ~96 linhas)
  `i_alocation` integer, `alocation` character varying, `area` character varying, `meio_acesso_alocacao` character varying
- **`forecast.de_para_calendar`** (tabela, ~865 linhas)
  `date_projet` character varying(10), `date_origem` character varying(10)
- **`forecast.demanda_projetada`** (tabela, ~1.1 mil linhas)
  `_data` character varying(10), `regional` character varying, `area` character varying, `demanda_fone` numeric, `demanda_web` numeric, `demanda_chat` numeric
- **`forecast.fte_aprovado`** (tabela, ~0 linhas)
  `ini` character varying(10), `fim` character varying(10), `aprovado` integer, `area` character varying, `gerente` character varying
- **`forecast.produtividade_media`** (tabela, ~0 linhas)
  `ini` character varying(10), `fim` character varying(10), `medprodut` integer, `area` character varying, `gerente` character varying
- **`forecast.projetado`** (tabela, ~692 linhas)
  `date_projet` character varying(10), `date_origem` character varying, `unity` character varying, `coeff_folha` character varying, `coeff_fiscont` character varying, `coeff_at` character varying, `tot_users` integer, `proj_folha` integer, `proj_fiscont` integer, `proj_at` integer
- **`forecast.tme_projetado`** (tabela, ~3.5 mil linhas)
  `year` integer, `ini` character varying, `fim` character varying, `seg` integer, `setor` character varying, `canal` character varying
- **`forecast.users`** (tabela, ~0 linhas)
  `date_month` character varying(10), `tot_sc` integer, `tot_sp` integer

## Schema `genesys`

- **`genesys.historic_qualifications`** (tabela, ~271.6 mil linhas)
  `skill_id_1` text, `skill_id_2` text, `date_interval` character varying(10), `time_interval` character varying(5), `metric_nOffered` numeric, `metric_nAnswered` numeric, `metric_tAnswered` numeric, `metric_tAnsweredMax` numeric, `metric_tAnsweredMin` numeric, `metric_nAbandon` numeric, `metric_tAbandon` numeric, `metric_tAbandonMax` numeric, `metric_tAbandonMin` numeric, `metric_tFlowOut` numeric, `metric_oServiceLevel` numeric, `metric_oServiceTarget` numeric, `metric_nHandle` numeric, `metric_tHandle` numeric, `metric_tHandleMax` numeric, `metric_tHandleMin` numeric, `metric_nTalkComplete` numeric, `metric_tTalkComplete` numeric, `metric_tTalkCompleteMax` numeric, `metric_tTalkCompleteMin` numeric, `metric_tHeldComplete` numeric, `metric_nAcw` numeric, `metric_tAcw` numeric, `metric_tAcwMax` numeric, `metric_tAcwMin` numeric, `metric_nTransferred` numeric, `metric_nOverSla` numeric, `metric_tShortAbandon` numeric, `metric_nWait` numeric, `metric_tWait` numeric, `metric_tWaitMax` numeric, `metric_tWaitMin` numeric, `metric_nOutboundAttempted` numeric, `metric_tVoicemail` numeric, `metric_tAbandon60` numeric, `metric_tAbandon120` numeric, `metric_tAbandon180` numeric, `metric_tAbandon300` numeric, `metric_tAbandon600` numeric, `metric_tAbandonMore600` numeric
- **`genesys.queue`** (tabela, ~4 linhas)
  `id_queue` text, `name_queue` text, `area` text
- **`genesys.skill`** (tabela, ~45 linhas)
  `id_skill` text, `name_skill` text, `area` text, `regional` text

## Schema `logmein`

- **`logmein.acessos`** (tabela, ~1.8 mi linhas)
  `start_time` character varying, `end_time` character varying, `last_action_time` character varying, `technician_name` character varying, `technician_id` character varying, `session_id` character varying, `session_type` character varying, `status` character varying, `name` character varying, `custom_field_1` character varying, `custom_field_2` character varying, `custom_field_3` character varying, `custom_field_4` character varying, `custom_field_5` character varying, `tracking_id` character varying, `customer_ip` character varying, `device_id` character varying, `incident_tools_used` character varying, `resolved_unresolved` character varying, `channel_id` character varying, `channel_name` character varying, `calling_card` character varying, `connecting_time` character varying, `waiting_time` character varying, `total_time` character varying, `active_time` character varying, `work_time` character varying, `hold_time` character varying, `time_in_transfer` character varying, `rebooting_time` character varying, `reconnecting_time` character varying, `platform` character varying, `email` character varying, `time_logmein` character varying, `livre_1` character varying, `livre_2` character varying

## Schema `public`

- **`public.calendar`** (tabela, ~1.8 mil linhas)
  `date` date, `day` integer, `day_name` character varying, `month` integer, `month_name` character varying, `day_of_week` integer, `day_of_year` integer, `holiday` character varying, `ten` integer, `ten_name` character(2), `day_useful_month` integer, `day_useful_year` integer, `year` integer, `fone_folha_seq_deman` integer, `fone_fiscont_seq_deman` integer, `fone_at_seq_deman` integer, `chat_folha_seq_deman` integer, `chat_fiscont_seq_deman` integer, `chat_at_seq_deman` integer
- **`public.chain_ia_interacao`** (tabela, ~21.8 mil linhas · PK (id))
  `id` integer, `login_usuario` character varying(100), `nome_usuario` character varying(255), `i_usuarios_gestor` integer, `i_revendas` integer, `i_chain_ai_chat` integer, `prompt_usuario` text, `resposta_copiada` character varying(3), `data_interacao` date, `horario_interacao` time without time zone
- **`public.goals`** (tabela, ~259.7 mil linhas)
  `compini` character varying(10), `compfim` character varying(10), `email` character varying(100), `descmeta` character varying(50), `valormeta` numeric(10,2), `meta_at` numeric(10,2), `meta_folha` numeric(10,2), `meta_fiscont` numeric(10,2)
- **`public.sgd_alocation_historic`** (tabela, ~3.4 mi linhas)
  `date` character varying(10), `i_user` integer, `i_alocation` integer, `from_of` character varying(10)
- **`public.sgd_alocation_reg`** (tabela, ~96 linhas)
  `i_alocation` integer, `description` character varying(100), `abbreviation` character varying(50), `area` integer
- **`public.sgd_cargos`** (tabela, ~160 linhas)
  `i_cargo` integer, `descricao` character varying, `ativo` integer
- **`public.sgd_client`** (tabela, ~248.7 mil linhas)
  `i_client` integer, `name_client` character varying(100), `date_register` character varying(10), `referential` character varying(3), `cep` character varying(8), `city` character varying(60), `initial_state` character varying(2), `desc_state` character varying(30), `phone` character varying(50), `i_resale` integer, `name_resale` character varying(30), `type_resale` character varying(20), `situation` integer, `date_inactivation` character varying(10), `date_signature` character varying(10), `i_cms_responsible` integer, `i_cms_manager` integer
- **`public.sgd_client_contact`** (tabela, ~481.6 mil linhas)
  `i_contact` integer, `i_client` integer, `phone_number` character varying, `name` character varying
- **`public.sgd_client_observ`** (tabela, ~22.9 mil linhas)
  `i_client` integer, `observation` text
- **`public.sgd_genesys`** (tabela, ~1.3 mi linhas)
  `i_ssc` integer, `cadastro_ia` integer, `id_transcricao_anexo` integer, `id_ligacao` integer, `tags` character varying, `conversation_id` character varying(50)
- **`public.sgd_horario_historic`** (tabela, ~29.7 mil linhas)
  `date` character varying(10), `i_user` integer, `i_responsavel_lancto` integer, `horario_inicio_matutino` character varying(10), `horario_fim_matutino` character varying(10), `horario_inicio_vespertino` character varying(10), `horario_fim_vespertino` character varying(10), `vigencia` character varying(10)
- **`public.sgd_ocorrencia`** (tabela, ~26.6 mil linhas)
  `i_ocorrencia` integer, `date_entry` character varying(10), `date_time` timestamp without time zone, `i_area_origem` integer, `i_area_destino` integer, `i_responsavel` integer, `i_usuario` integer, `i_clientes` integer, `i_revendas` integer, `i_situacao` integer, `i_categoria` integer, `i_setor_origem` integer, `i_setor_destino` integer, `i_ocorrencia_pai` character varying, `ultimo_tramite` timestamp without time zone, `tipo` integer, `entrada_email` character varying, `resposta_email` character varying, `tme_minutos` integer, `tma_total_minutos` integer, `tma_sub_minutos` integer
- **`public.sgd_ocorrencia_area`** (tabela, ~74 linhas)
  `i_area` integer, `description` character varying(60), `i_setor` integer
- **`public.sgd_ocorrencia_categoria`** (tabela, ~384 linhas)
  `i_categoria` integer, `description` character varying(60), `i_area` integer, `i_setor` integer
- **`public.sgd_ocorrencia_prioridade`** (tabela, ~4 mil linhas)
  `id_ocorrencia` integer, `id_prioridade` integer, `nome_prioridade` character varying(250)
- **`public.sgd_ocorrencia_sane`** (tabela, ~2.8 mil linhas)
  `i_ocorrencia` integer, `i_sane` integer
- **`public.sgd_ocorrencia_setor`** (tabela, ~0 linhas)
  `i_setor` integer, `description` character varying(60)
- **`public.sgd_ocorrencia_situacao`** (tabela, ~13 linhas)
  `i_situacao` integer, `description` character varying(60)
- **`public.sgd_ocorrencia_ss`** (tabela, ~3 mil linhas)
  `i_ocorrencia` integer, `i_ss` integer
- **`public.sgd_ocorrencia_ssc`** (tabela, ~24.5 mil linhas)
  `i_ocorrencia` integer, `i_ssc` integer
- **`public.sgd_ocorrencia_tramite`** (tabela, ~192.7 mil linhas)
  `i_tram` integer, `date_tram` character varying(19), `i_user` integer, `i_ocorrencia` integer, `i_situacao` integer
- **`public.sgd_ocorrencia_tramite_time`** (tabela, ~251.5 mil linhas)
  `i_ocorrencia` integer, `i_tram` integer, `tempo` integer
- **`public.sgd_pendency`** (tabela, ~6.2 mi linhas)
  `i_ssc` integer, `date` character varying(10), `i_user` integer, `i_ssc_tramites` integer, `i_ssc_situation` integer, `i_ss` integer, `i_ssql` integer, `i_sr` integer, `i_conversoes` integer, `n1_pendency` integer, `n2_pendency` integer, `sector_pendency` integer, `i_clientes` integer, `i_meios_acesso` integer, `i_meios_retorno` integer, `i_sss_classificacoes` integer, `system` character varying(40), `module` character varying(40), `topic` character varying(120), `entry` character varying(10), `pendency_days` integer, `useful_pendency_days_n1` integer, `useful_pendency_days_n2` integer, `subtopic` character varying
- **`public.sgd_preferencia_pesquisa`** (tabela, ~436 mil linhas)
  `data_consulta` character varying(10), `i_usuario` numeric, `sistema_config` character varying, `modulo_config` character varying, `situacao_config` character varying, `classificacao_config` character varying
- **`public.sgd_product`** (tabela, ~61 linhas)
  `i_product` numeric, `description` character varying
- **`public.sgd_product_client`** (tabela, ~449.3 mil linhas)
  `i_contract` numeric, `i_product` numeric, `date_register` character varying(10), `i_client` numeric, `date_ass_cont` character varying(10), `date_ini_serv` character varying(10), `date_fim_serv` character varying(10), `situ_contract` numeric
- **`public.sgd_resale`** (tabela, ~121 linhas)
  `i_resale` integer, `apelido` character varying, `active` integer
- **`public.sgd_sa`** (tabela, ~433.1 mil linhas)
  `i_sa` integer, `date_entry` character varying(10), `subject` character varying, `description` text, `justification` text, `i_sa_classification` integer, `i_status` integer, `i_resales` integer, `i_system` integer, `i_module` integer, `type_sa` integer, `reason` integer, `client` character varying, `i_user` integer, `i_sa_disapproval_reason` integer
- **`public.sgd_sa_classification`** (tabela, ~0 linhas)
  `i_sa_classification` integer, `description` character varying
- **`public.sgd_sa_disapproval_reason`** (tabela, ~0 linhas)
  `i_sa_disapproval_reason` integer, `description` character varying
- **`public.sgd_sa_module`** (tabela, ~410 linhas)
  `i_system` integer, `i_module` integer, `description` character varying
- **`public.sgd_sa_priority`** (tabela, ~486 linhas)
  `i_sa` integer, `entry` character varying(10), `i_user` integer, `description` character varying
- **`public.sgd_sa_situations`** (tabela, ~0 linhas)
  `i_sa_situation` integer, `description` character varying
- **`public.sgd_sa_system`** (tabela, ~0 linhas)
  `i_system` integer, `description` character varying
- **`public.sgd_sai_sane`** (tabela, ~201.6 mil linhas)
  `i_sai` integer, `i_sa_ne` integer
- **`public.sgd_schedule`** (tabela, ~4.6 mi linhas)
  `date` character varying(10), `i_user` integer, `i_type` integer, `responsible` character varying, `i_absences_reason` integer, `minutes` bigint, `description` character varying, `data_hora_ini` character varying(19), `data_hora_fim` character varying(19)
- **`public.sgd_schedule_absences_reason`** (tabela, ~0 linhas)
  `i_absences_reason` integer, `description` character varying(60), `active` character varying(6), `i_schedule_type` integer
- **`public.sgd_schedule_absences_type`** (tabela, ~0 linhas)
  `i_schedule_type` integer, `description` character varying(64), `area` integer
- **`public.sgd_schedule_past_future`** (tabela, ~2.3 mi linhas)
  `date` character varying(10), `i_user` integer, `i_type` integer, `responsible` character varying, `i_absences_reason` integer, `minutes` bigint, `description` character varying, `data_hora_ini` character varying(19), `data_hora_fim` character varying(19)
- **`public.sgd_schedule_three_days`** (tabela, ~4.6 mi linhas)
  `date` character varying(10), `i_user` integer, `i_type` integer, `responsible` character varying, `i_absences_reason` integer, `minutes` bigint, `description` character varying, `data_hora_ini` character varying(19), `data_hora_fim` character varying(19)
- **`public.sgd_soses`** (tabela, ~43.1 mil linhas)
  `i_ssc` integer, `tipo_servico` character varying(200), `duracao` integer, `valor_total` numeric, `parcelas` integer, `vencimento` character varying(10), `autorizacao` character varying(10), `exclusao` character varying(10), `entregue` integer, `prazo_anterior` integer, `situacao` character varying, `data_emissao` character varying(10)
- **`public.sgd_ssc`** (tabela, ~20.8 mi linhas)
  `code_ssc` integer, `i_ssc` integer, `date_entry` character varying(10), `date_time` timestamp without time zone, `i_classification` integer, `system` character varying(40), `module` character varying(40), `topic` character varying, `subtopic` character varying, `i_means_of_access` integer, `lista_ss` character varying, `i_clientes` integer, `i_user` integer, `total_procedures_waiting_answer` integer, `total_procedures` integer, `time_before_first_analysis` integer, `time_total` integer, `time_medium` integer, `dateconclusion` character varying(10), `time_ss` integer, `time_ssql` integer, `bond_sa_ne` integer, `disapproval` character varying(10), `time_bond_sa_ne` integer, `time_phone` integer, `time_final_support` integer, `time_final_client` integer, `time_last_procedure_without_analysis` integer, `number_procedure_conclusion` integer, `satisfaction_ssc` character varying(12), `i_ssc_satisfaction_reason` integer, `i_user_resales` integer, `number_procedure_attachement` integer, `bond_attachment_sa_ne` integer, `time_scd` integer, `priority` integer, `no_acess_system` integer, `dtime` character varying(5), `ia_register` integer
- **`public.sgd_ssc_answer_time`** (tabela, ~16.9 mi linhas)
  `i_ssc` integer, `i_user` integer, `datewithoutanalysis` timestamp without time zone, `datewaitinganswer` timestamp without time zone, `timesupport` integer, `timess` integer, `timessql` integer, `timeconversao` integer, `timesr` integer, `timewithoutanalysis` integer, `firstprocedure` character varying(5), `i_client` integer
- **`public.sgd_ssc_classification`** (tabela, ~0 linhas)
  `i_classification` integer, `desription` character varying(60)
- **`public.sgd_ssc_contact_dissatisfaction`** (tabela, ~0 linhas)
  `i_response` integer, `i_ssc` character varying, `email` character varying, `contact` character varying, `detail` character varying, `date_incl` timestamp without time zone
- **`public.sgd_ssc_disregard_dissatisfaction`** (tabela, ~631 linhas)
  `i_response` integer, `i_ssc_ss_chat` character varying, `type` character varying, `justif` character varying, `date_incl` timestamp without time zone, `email` character varying
- **`public.sgd_ssc_dissatisfaction_historic`** (tabela, ~54.5 mil linhas)
  `i_ssc` integer, `text_dissatisfaction` character varying, `allow_contact` character varying(10), `conclusion_date` character(10)
- **`public.sgd_ssc_ia_chat`** (tabela, ~743.7 mil linhas · PK (i_seq))
  `i_seq` integer, `id_prompt` integer, `i_ssc` integer, `entrada` character varying, `completion` text
- **`public.sgd_ssc_internal_time`** (tabela, ~1.2 mi linhas)
  `i_ssc` integer, `i_ssc_tramites` integer, `datewaitinganswer` timestamp without time zone, `dateanswered` timestamp without time zone, `category` character varying(100), `i_userrequest` integer, `i_userresponsible` integer, `timeanswer` integer
- **`public.sgd_ssc_reason_dissatisfaction`** (tabela, ~5 linhas)
  `i_ssc_satisfaction_reason` integer, `description` character varying(100)
- **`public.sgd_ssc_reescrever_ia`** (tabela, ~73 mil linhas)
  `seq` integer, `data_entrada` character varying, `utilizou_resposta` integer, `alterou_resposta` integer, `i_usuario` integer, `prompt_usuario` character varying, `retorno_ia` character varying
- **`public.sgd_ssc_sa`** (tabela, ~1.5 mi linhas)
  `i_ssc` integer, `i_resale` integer, `i_sa_ne` integer
- **`public.sgd_ssc_situation`** (tabela, ~0 linhas)
  `i_ssc_situation` integer, `description` character varying(80)
- **`public.sgd_ssc_ss`** (tabela, ~1.2 mi linhas)
  `ssc` integer, `ss` integer
- **`public.sgd_ssc_text_conclusion`** (tabela, ~353.4 mil linhas)
  `i_ssc` numeric(10,0), `conclusion_date` character varying, `description` text
- **`public.sgd_ssc_tramites`** (tabela, ~65.8 mi linhas)
  `i_ssc` integer, `i_ssc_tramites` integer, `entry` timestamp without time zone, `i_ssc_situation` integer, `i_user` integer, `tipo_resposta` character varying, `i_visualizado` character varying, `data_visualizacao` character varying, `existe_texto_web` character varying
- **`public.sgd_ssc_utiliza_solucao`** (tabela, ~4.4 mi linhas)
  `seq` integer, `i_ssc` integer, `i_user` integer, `opcao_utilizada` integer, `origem_resposta` integer, `destino` integer, `alterou_texto` integer, `data_hora` character varying
- **`public.sgd_user_cargo_historico`** (tabela, ~3.1 mi linhas)
  `data_dia` character varying(10), `i_usuario` integer, `i_cargo_historico` integer, `a_partir_de` character varying(10)
- **`public.sgd_user_client`** (tabela, ~928.4 mil linhas)
  `i_client` integer, `i_user` integer, `name_user` character varying, `email_user` character varying, `date_entry` character varying(10), `situation` character varying(7), `cpf` character varying, `date_nasc` character varying(10), `escolaridade` character varying, `curso` character varying, `forma_trabalho` character varying, `total_dias` integer
- **`public.sgd_user_client_cursos`** (tabela, ~3.6 mil linhas)
  `i_user` integer, `cursos` character varying
- **`public.sgd_user_manager_historic`** (tabela, ~2.1 mi linhas)
  `date` character varying(10), `i_historic` integer, `i_user` integer, `from_of` character varying(10), `i_superv` integer, `superv` character varying, `manager` character varying, `responsible_alter` character varying, `date_alter` character varying(10)
- **`public.sgd_users`** (tabela, ~11.7 mil linhas)
  `i_user` integer, `user` character varying, `email` character varying, `admission` character varying, `date_inactivation` character varying, `dismission` character varying, `name` character varying, `resale` character varying, `i_resale` integer, `type_resale` character varying
- **`public.validacaoImportacao`** (tabela, ~1 linhas)
  `idConf` integer, `maxSSC` integer, `maxdatahoratramite` character varying, `conexao` character varying, `ultimaatualizacao` character varying
- **`public.vw_sgd_ssc_id_genesys`** (view, — linhas)
  `i_ssc` integer, `conversation_id` character varying(50), `system` character varying(40), `module` character varying(40), `topic` character varying, `subtopic` character varying

## Schema `suporte`

- **`suporte.dados_teams_sul`** (tabela, ~49.3 mil linhas · PK (auxiliar))
  `auxiliar` text, `data` timestamp without time zone, `equipe_teams` text, `canal_teams` text, `email_ajuda` text, `email_lider` text, `email_lider_respondeu` text, `assunto` text, `descricao` text, `link_conversa` text, `quem_pediu_ajuda` text, `quem_respondeu` text, `adaptacao_apoio` text, `email_lider_adapt` text, `tempo_reacao` text, `tempo_reacao_novo` text

## Schema `temp`

- **`temp._Productivity`** (tabela, ~1.4 mil linhas)
  `code_user` integer, `email` character varying(150), `alocacao` character varying(100), `setor` character varying(100), `unidade` character varying(100), `qtde_novas` integer, `qtde_novas_web` integer, `qtde_tramitadas` integer, `ligacoes` integer
- **`temp._callsWithClient`** (tabela, ~11.6 mil linhas)
  `conversation_id` character varying, `i_client` integer, `ani` character varying
- **`temp._calls_agents_halfHour`** (tabela, ~3.1 mil linhas)
  `date_interval` text, `id_user` text, `time_interval` text, `_nAnswered` numeric, `_tAnswered` numeric, `_tAnsweredMax` numeric, `_tAnsweredMin` numeric, `_nHandle` numeric, `_tHandle` numeric, `_tHandleMax` numeric, `_tHandleMin` numeric, `_nTalkComplete` numeric, `_tTalkComplete` numeric, `_tTalkCompleteMax` numeric, `_tTalkCompleteMin` numeric, `_tHeldComplete` numeric, `_nAcw` numeric, `_tAcw` numeric, `_tAcwMax` numeric, `_tAcwMin` numeric, `_nDialing` numeric, `_tDialing` numeric, `_tDialingMax` numeric, `_tDialingMin` numeric, `_nContacting` numeric, `_tContacting` numeric, `_tContactingMax` numeric, `_tContactingMin` numeric, `_nTransferred` numeric, `_nOutbound` numeric, `_nNotResponding` numeric, `_tNotResponding` numeric, `_tNotRespondingMax` numeric, `_tNotRespondingMin` numeric, `_nAlert` numeric, `_tAlert` numeric, `_tAlertMax` numeric, `_tAlertMin` numeric, `_nMonitoring` numeric, `_tMonitoring` numeric, `_tMonitoringMax` numeric, `_tMonitoringMin` numeric, `_nBlindTransferred` numeric, `_nConsultTransferred` numeric
- **`temp._sgdDemanda`** (tabela, ~0 linhas)
  `i_ssc` integer, `entrada` timestamp without time zone, `situacao` character varying(100), `n1_pendency` integer, `n2_pendency` integer, `prioridade` character varying(40), `meio_acesso` character varying(40), `meio_retorno` character varying(40), `classificacao` character varying(40), `sitema` character varying(50), `modulo` character varying(50), `topico` character varying(100), `subtopico` character varying(100), `i_clientes` integer, `razao_cliente` character varying(500), `tecnico` character varying(100), `alocacao` character varying(100), `coordenador` character varying(100), `assunto` character varying, `i_user` integer, `i_revendas` integer
- **`temp._sgdPendency`** (tabela, ~1.7 mil linhas)
  `i_ssc` text, `entrada` text, `situacao` text, `i_ss` text, `i_ssql` text, `i_sr` text, `i_conversoes` text, `n1_pendency` text, `n2_pendency` text, `prioridade` text, `meio_acesso` text, `meio_retorno` text, `classificacao` text, `sistema` text, `modulo` text, `topico` text, `i_clientes` text, `tecnico` text, `alocacao` text, `coordenador` text, `DataHora` text, `assunto` text, `ulti_tramite` text, `link` text, `agenda` text, `unidade` text, `qtd_tramite_respondido_cliente` text, `qtd_tramite_aguardando_suporte` text, `qtd_tramite_troca_responsavel` text, `entrada_ultima_interacao_valida` text, `situacao_ultima_interacao_valida` text, `minutos_pendente_com_suporte` text, `numero_ssc` text, `minutos_uteis_desde_ultimo_tramite` integer, `minutos_uteis_desde_ultima_interacao_valida` integer, `qtd_dias_corridos_desde_entrada` integer, `gerente` text, `meses_empresa_tecnico` integer, `hora_consulta` timestamp without time zone
- **`temp._users_Genesys`** (tabela, ~531 linhas · PK (id_user))
  `id_user` text, `email` text, `name` text, `status` text, `supervisor` text, `jabber_id` text, `department` text, `gerente` text
- **`temp.analise_ssc`** (tabela, ~22.8 mil linhas)
  `cliente` numeric, `ssc` numeric, `problema` numeric
- **`temp.analise_ssc_sgd`** (tabela, ~22.8 mil linhas)
  `cliente` numeric, `ssc` numeric, `assunto` text, `descricao` text
- **`temp.protocols`** (tabela, ~2 mil linhas)
  `_id` character varying(25), `protocol_number` character varying(25), `i_userchat` character varying(25), `initialqueue` character varying, `createdatdate` character varying(25), `interval` character varying(5), `rating` character varying(15), `ratingdesc` character varying, `duration` integer, `closedate` character varying(25), `id_client` integer, `closure_motive` character varying, `cli_name_contact` character varying, `cli_user_onvio` character varying, `i_ssc` integer
- **`temp.sgd_user_manager_historic`** (tabela, ~4.2 mil linhas)
  `i_historic` integer, `i_user` integer, `from_of` character varying(10), `manager` character varying, `responsible_alter` character varying, `date_alter` character varying(10)
- **`temp.users_chat`** (tabela, ~0 linhas)
  `i_userchat` character varying(25), `email` character varying, `username` character varying, `name` character varying, `status` character varying, `role` character varying, `createddate` character varying(25), `updatedate` character varying(25), `i_user_sgd` character varying
