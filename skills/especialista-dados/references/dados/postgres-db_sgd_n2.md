# Postgres · DB_SGD_N2 — estrutura

> Última atualização: 2026-09-29 · Fonte: catálogo `pg_catalog` lido por `scripts/catalogo_postgres.py` (sessão READ ONLY, sem leitura de dados) · **Gerado automaticamente** — não editar à mão.
> Linhas = estimativa do planner (`reltuples`), não contagem exata. Quem carrega cada tabela: `dados-postgres-destinos.md` / `dados-fluxos-maestro.md`.

| Schema | Tabelas | Views |
|---|---|---|
| `public` | 37 | 0 |
| `ss` | 17 | 0 |

## Schema `public`

- **`public.BKN_ultimoBackup`** (tabela, ~0 linhas)
  `i_client` numeric, `backup` character varying, `days` numeric
- **`public.ClienteProduto`** (tabela, ~267.6 mil linhas)
  `data` character varying, `i_client` numeric, `i_produto` numeric
- **`public.SGD_SCD_Pendency`** (tabela, ~3.6 mil linhas)
  `i_conversoes` integer, `ddate` character varying, `i_user` integer, `i_tramites` integer, `i_situation` integer, `description_situation` character varying
- **`public.SGD_SS_Pendency`** (tabela, ~2.3 mi linhas)
  `i_ss` integer, `ddate` character varying, `ddatetime` character varying, `i_user` integer, `i_ss_tramites` integer, `i_ss_situation` integer, `description_situation` character varying, `pending` character varying(50)
- **`public.SGD_SS_Pendency_BK`** (tabela, ~32.3 mil linhas)
  `i_ss` integer, `ddate` character varying, `ddatetime` character varying, `i_user` integer, `i_ss_tramites` integer, `i_ss_situation` integer, `description_situation` character varying, `pending` character varying(50), `i_classification` integer, `system` character varying(50), `module` character varying(50), `topc` character varying(200)
- **`public.SGD_SS_Pendency_BK2`** (tabela, ~491.2 mil linhas)
  `i_ss` integer, `ddate` character varying, `ddatetime` character varying, `i_user` integer, `i_ss_tramites` integer, `i_ss_situation` integer, `description_situation` character varying, `pending` character varying(50)
- **`public.SGD_SS_Pendency_OLD`** (tabela, ~76 mil linhas)
  `i_ss` integer, `ddate` character varying, `ddatetime` character varying, `i_user` integer, `i_ss_tramites` integer, `i_ss_situation` integer, `description_situation` character varying, `pending` character varying(50), `i_classification` integer, `system` character varying(50), `module` character varying(50), `topc` character varying(200)
- **`public.SGD_agendaMotivos`** (tabela, ~0 linhas)
  `i_agenda_motivos_ausencias` integer, `descricao` character varying(60), `ativo` character varying(6), `i_agenda_tipos` integer
- **`public.SGD_agendaTipos`** (tabela, ~0 linhas)
  `i_agenda_tipos` integer, `descricao` character varying(64), `area` integer
- **`public.SGD_modulos`** (tabela, ~408 linhas)
  `i_sistemas` integer, `i_modulos` integer, `nome` character varying(60), `i_sistemas_compilacao` integer, `i_modulos_solucoes` integer, `visualiza_rank_melhorias` integer
- **`public.SGD_resales`** (tabela, ~121 linhas)
  `I_controle` integer, `Name` character varying, `SmallName` character varying, `tipo` character varying
- **`public.SGD_schedule`** (tabela, ~906 mil linhas)
  `dDate` character varying, `i_user` integer, `i_type` integer, `i_absent_reasons` integer, `minutes` bigint
- **`public.SGD_sistemas`** (tabela, ~0 linhas)
  `i_sistemas` integer, `nome` character varying(60), `ativo` integer, `apelido` character varying(60), `interno` integer
- **`public.SGD_ss`** (tabela, ~485.3 mil linhas)
  `i_ss` integer, `DateEntry` character varying, `i_classification` integer, `i_system` integer, `i_module` integer, `i_topc` integer, `i_satisfaction` integer, `i_dissatisfied_reason` integer, `i_userreasales` integer, `i_resales` integer, `i_situacao` integer
- **`public.SGD_ss_conclusion`** (tabela, ~96.4 mil linhas)
  `i_ssc` numeric(10,0), `dateconclusion` character varying, `description` text
- **`public.SGD_ss_dissatisfiedReason`** (tabela, ~0 linhas)
  `i_dissatisfiedReason` integer, `description` character varying
- **`public.SGD_ss_satisfactionDescription`** (tabela, ~0 linhas)
  `i_satisfaction` integer, `description` character varying
- **`public.SGD_ss_situation`** (tabela, ~0 linhas)
  `i_situation` integer, `description` character varying, `pending` character varying
- **`public.SGD_ss_tramites`** (tabela, ~3.7 mi linhas)
  `i_ss` integer, `i_ss_tramites` integer, `DateEntry` character varying, `situation` integer, `i_user` integer, `typeforwarding` integer, `dateanalysisforwarding` character varying, `i_userforwarding` integer, `exists_requestsql` integer
- **`public.SGD_ssc`** (tabela, ~20.1 mi linhas)
  `i_ssc` integer, `DateEntry` character varying, `classification` integer, `i_system` integer, `i_module` integer, `i_topic` integer, `i_subtopic` integer, `system` character varying, `module` character varying, `topic` character varying, `subtopic` character varying, `i_revendas` integer, `i_user` integer, `i_client` integer, `i_means_of_access` integer
- **`public.SGD_sscClassification`** (tabela, ~0 linhas)
  `i_sss_classificacoes` integer, `descricao` character varying(60), `ordem` integer
- **`public.SGD_ssc_BK`** (tabela, ~4.5 mi linhas)
  `i_ssc` integer, `DateEntry` character varying, `classification` integer, `i_system` integer, `i_module` integer, `i_topic` integer, `system` character varying, `module` character varying, `topic` character varying, `i_revendas` integer, `i_user` integer, `i_client` integer
- **`public.SGD_ssc_situation`** (tabela, ~4.8 mi linhas)
  `i_ssc` integer, `i_situation` integer
- **`public.SGD_topicosSuporte`** (tabela, ~1.7 mil linhas)
  `i_topicos_suportes` integer, `i_sistemas` integer, `i_modulos` integer, `topico` character varying(200), `tags` character varying(1000), `i_sss_classificacoes` integer
- **`public.SGD_usersResales`** (tabela, ~12.3 mil linhas)
  `i_user` integer, `name` character varying, `DateRegister` character varying, `i_userResales` integer, `Situation` character varying
- **`public.SGD_usersUAN`** (tabela, ~2 mil linhas)
  `i_user` integer, `name` character varying, `user` character varying, `email` character varying, `DateRegister` character varying, `manager` character varying, `i_alocacao` integer, `alocation` character varying, `situation` character varying
- **`public._piracyClient`** (tabela, ~244.2 mil linhas)
  `I_clientes` numeric, `NameClient` character varying, `I_representantes` numeric, `I_revenda` numeric, `ResaleSmallName` character varying, `DateRegister` character varying(10), `Referencial` character varying, `Cep` character varying, `City` character varying, `InitialsState` character varying, `State` character varying, `numberOfUsers` numeric, `Situation` character varying
- **`public._piracyLiberacoes`** (tabela, ~608.2 mil linhas)
  `i_hist_liberacoes` integer, `origem` smallint, `sequ_liberacao` integer, `i_produtos` integer, `i_clientes` integer, `i_representantes` integer, `i_unnegocio` integer, `versao_liberada` character varying, `nec` integer, `inf_banco` character varying, `tipo_usuario` smallint, `usuario_interno` character varying, `usuario_web` character varying, `ip_usuario` character varying, `processo_gerador` smallint, `i_grupos_situacoes` integer, `i_vendedor_gerente` integer, `i_bancos` integer, `dt_base` character varying, `dt_geracao` character varying, `vencto_mais_antigo_em_aberto` character varying, `tam_db` integer, `tam_log` integer
- **`public._piracyProdutos`** (tabela, ~60 linhas)
  `i_produtos` numeric, `descricao` character varying, `i_pacotes` numeric, `i_segmentos` numeric
- **`public._piracyultimoBackup`** (tabela, ~2.2 mi linhas)
  `i_clientes` numeric, `ultimo_backup` character varying, `i_produtos` numeric, `tam_db` numeric, `tam_log` numeric, `i_hist_liberacoes` numeric
- **`public.clientUsuariosHist`** (tabela, ~76.7 mi linhas)
  `firstdaymonth` character varying(10), `lastdaymonth` character varying(10), `i_client` numeric, `i_contrat` numeric, `dateregister` character varying(10), `totusers` numeric
- **`public.client_dw_historic`** (tabela, ~38.8 mi linhas)
  `daymonth` character varying(10), `dw` numeric, `i_client` numeric, `i_contrat` numeric, `dateregister` character varying(10)
- **`public.dCalendar`** (tabela, ~1.1 mil linhas)
  `Date` date, `Day` integer, `DayName` character varying, `Month` integer, `MonthName` character varying, `DayOfWeek` integer, `DayOfYear` integer, `Holiday` character varying, `Ten` integer, `TenName` character(2), `DayUsefulOfMonth` integer, `DayUsefulOfYear` integer, `Year` integer
- **`public.dTime`** (tabela, ~48 linhas)
  `dTime` text
- **`public.geolocalizacaoip`** (tabela, ~690.4 mil linhas)
  `ip` character varying, `country` character varying, `region` character varying, `region_name` character varying, `city` character varying, `isp` character varying
- **`public.sgd_ss_client`** (tabela, ~1.2 mi linhas)
  `i_ss` integer, `cliente` text
- **`public.sgd_ssc_disregard_dissatisfaction`** (tabela, ~631 linhas)
  `i_response` integer, `i_ssc_ss_chat` character varying, `type` character varying, `justif` character varying, `date_incl` timestamp without time zone, `email` character varying

## Schema `ss`

- **`ss.calendar`** (tabela, ~1.5 mil linhas)
  `date` date, `day` integer, `day_name` character varying, `month` integer, `month_name` character varying, `day_of_week` integer, `day_of_year` integer, `holiday` character varying, `ten` integer, `ten_name` character(2), `day_useful_month` integer, `day_useful_year` integer, `year` integer
- **`ss.ss`** (tabela, ~499.3 mil linhas)
  `i_ss` integer, `date_entry` character varying, `i_classification` integer, `i_system` integer, `i_module` integer, `i_topc` integer, `i_subtopic` integer, `i_satisfaction` integer, `i_dissatisfied_reason` integer, `i_userreasales` integer, `i_resales` integer, `i_situacao` integer, `last_update` character varying
- **`ss.ss_category`** (tabela, ~0 linhas)
  `i_ss_category` integer, `category_name` character varying, `description` character varying
- **`ss.ss_classification`** (tabela, ~9 linhas)
  `i_ss_classification` integer, `description` character varying
- **`ss.ss_conclusion_text`** (tabela, ~78.8 mil linhas)
  `i_ssc` numeric(10,0), `dateconclusion` character varying, `description` text
- **`ss.ss_disregard_dissatisfaction`** (tabela, ~64 linhas)
  `i_response` integer, `i_ss` character varying, `justif` character varying, `date_incl` timestamp without time zone, `email` character varying
- **`ss.ss_dissatisfied_reason`** (tabela, ~0 linhas)
  `i_reason` integer, `description` character varying
- **`ss.ss_module`** (tabela, ~410 linhas)
  `i_system` integer, `i_modules` integer, `description` character varying, `i_system_compilation` integer, `i_modules_solution` integer, `view_ranking_improvement` integer
- **`ss.ss_pendency`** (tabela, ~2.6 mi linhas)
  `i_ss` integer, `ddate` character varying, `ddatetime` character varying, `i_user` integer, `i_ss_tramites` integer, `i_ss_situation` integer, `description_situation` character varying, `pending` character varying(50)
- **`ss.ss_satisfaction_description`** (tabela, ~0 linhas)
  `i_satisfaction` integer, `description` character varying
- **`ss.ss_situation`** (tabela, ~38 linhas)
  `i_situation` integer, `description` character varying, `pending` character varying
- **`ss.ss_sub_topic`** (tabela, ~3.8 mil linhas)
  `i_origens` integer, `description` character varying, `i_topic_suport` integer
- **`ss.ss_system`** (tabela, ~50 linhas)
  `i_system` integer, `description` character varying, `active` integer, `nickname` character varying
- **`ss.ss_topic`** (tabela, ~1.7 mil linhas)
  `i_topic` integer, `i_system` integer, `i_module` integer, `description` character varying, `tags` character varying, `i_ss_classification` integer
- **`ss.ss_tramites`** (tabela, ~3.8 mi linhas)
  `i_ss` integer, `i_ss_tram` integer, `date_tram` character varying, `situation` integer, `i_user` integer, `typeforwarding` integer, `dateanalysisforwarding` character varying, `i_userforwarding` integer, `exists_requestsql` integer, `i_category` integer, `sla_interacao` character varying, `sla_n3` character varying, `sla_tme` character varying
- **`ss.ss_tramites_time`** (tabela, ~4.3 mi linhas)
  `i_ss` integer, `i_ss_tram` integer, `time` integer
- **`ss.ultimo_backup_bkn`** (tabela, ~7.7 mi linhas)
  `i_client` numeric, `backup` character varying, `days` numeric, `data_record` timestamp without time zone
