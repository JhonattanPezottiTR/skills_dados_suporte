# Postgres · DB_CTS — estrutura

> Última atualização: 2026-09-29 · Fonte: catálogo `pg_catalog` lido por `scripts/catalogo_postgres.py` (sessão READ ONLY, sem leitura de dados) · **Gerado automaticamente** — não editar à mão.
> Linhas = estimativa do planner (`reltuples`), não contagem exata. Quem carrega cada tabela: `dados-postgres-destinos.md` / `dados-fluxos-maestro.md`.

| Schema | Tabelas | Views |
|---|---|---|
| `public` | 34 | 2 |
| `temp_import` | 10 | 0 |
| `tria` | 5 | 0 |

## Schema `public`

- **`public.CTS_Access_Count`** (tabela, ~107.8 mi linhas)
  `I_contagem_acessos` bigint, `I_solucoes` integer, `I_usuarios` integer, `DateEntry` date, `MeansOfAccess` integer
- **`public.CTS_HistoryOfResponsible`** (tabela, ~275.3 mil linhas · PK (I_historicos))
  `I_historicos` integer, `I_solucoes` integer, `I_responsaveis` integer, `DateEntry` timestamp with time zone, `DateExpiration` timestamp with time zone
- **`public.CTS_HistoryOfResponsibleFinally`** (tabela, ~114 mil linhas)
  `I_historicos` integer, `I_solucoes` integer, `I_responsaveis` integer, `DateEntry` timestamp with time zone, `DateExpiration` timestamp with time zone, `Action` text
- **`public.CTS_ModulosSolucoes`** (tabela, ~0 linhas)
  `id_module_solution` bigint, `name_module` character varying(50)
- **`public.CTS_Responsible`** (tabela, ~61 linhas)
  `I_usuarios` integer, `Name` character varying, `Situation` character varying(9), `email` character varying(4000)
- **`public.CTS_SatisfactionSearch`** (tabela, ~505.4 mil linhas)
  `I_satisfaction_search` integer, `I_solucoes` integer, `I_usuarios` integer, `Useful` character varying, `Detail` character varying(4000), `DateEntry` date, `I_historicos` integer, `I_responsaveis` integer
- **`public.CTS_Schedule`** (tabela, ~62.7 mil linhas)
  `dDate` timestamp with time zone, `dDateTime` timestamp with time zone, `i_user` integer, `i_type` integer, `i_absent_reasons` integer, `minutes` bigint
- **`public.CTS_SearchContent`** (tabela, ~40.7 mi linhas · PK (id_search))
  `id_search` bigint, `id_userResales` bigint, `content_search` character varying(4096), `dDataSearch` date, `dTimeSearch` time without time zone, `i_modulo_sol` integer, `ids_telas_contabil` integer, `id_origem_pesquisa` integer
- **`public.CTS_Solutions`** (tabela, ~13.2 mil linhas · PK (I_solucoes))
  `I_solucoes` integer, `DateEntry` timestamp with time zone, `DateExpiration` timestamp with time zone, `Description` character varying, `System` character varying, `Module` character varying, `Topic` character varying, `SubTopic` character varying, `Classification` character varying, `linkSGD` character varying, `linkExternal` character varying, `type` character varying, `texto_solucao` character varying
- **`public.CTS_Solutions_Video_URL`** (tabela, ~16.7 mil linhas)
  `i_solucoes` numeric, `url_video` text, `date_alter` date, `i_responsavel` numeric
- **`public.CTS_Solutions_Video_URL_TESTE`** (tabela, ~5.5 mil linhas)
  `i_solucoes` numeric, `url_video` text, `date_alter` date, `i_responsavel` numeric
- **`public.CTS_Solutions_Video_URL_Teste2`** (tabela, ~9.6 mil linhas)
  `i_solucoes` numeric, `url_video` text, `date_alter` date, `i_responsavel` numeric
- **`public.CTS_Users`** (tabela, ~1.4 mi linhas)
  `I_usuarios` integer, `Name` character varying, `I_Clientes` integer
- **`public.SGD_Client`** (tabela, ~251.4 mil linhas)
  `I_clientes` integer, `NameClient` character varying, `I_representantes` integer, `I_revenda` integer, `ResaleSmallName` character varying, `DateRegister` date, `Referential` character varying, `Cep` character varying, `City` character varying, `InitialsState` character varying, `State` character varying
- **`public.SGD_UserSituation`** (tabela, ~6.7 mil linhas)
  `i_usuarios` integer, `Situation` character varying(9)
- **`public.User_SGD_CTS`** (tabela, ~0 linhas)
  `id_user` integer, `name_user` character varying, `user_sgd_cts` character varying
- **`public.cts_access_count`** (tabela, ~156.7 mi linhas)
  `i_access_count` bigint, `i_solution` integer, `i_user` integer, `date_entry` date, `means_of_access` integer
- **`public.cts_dados_digital`** (tabela, ~994 linhas)
  `data_dia` character varying(10), `youtube` numeric(10,2), `instagram` numeric(10,2)
- **`public.cts_gpt_saudacao`** (tabela, ~55 mil linhas)
  `data_consulta` character varying(10), `config_inicio` integer, `config_fim` integer, `i_usuario` numeric, `tipo` integer
- **`public.cts_solucoes`** (tabela, ~13.2 mil linhas · PK (i_solucao))
  `i_solucao` integer, `entrada` timestamp with time zone, `expiracao` timestamp with time zone, `descricao` character varying, `sistema` character varying, `modulo` character varying, `topico` character varying, `subtopico` character varying, `classificacao` character varying, `link_sgd` character varying, `link_externo` character varying, `_type` character varying, `texto_solucao` character varying
- **`public.cts_solucoes_futuras`** (tabela, ~0 linhas)
  `i_solucao` integer, `valido_de` character varying, `pergunta` character varying, `resposta` character varying, `tags` character varying, `url_video` character varying, `solucoes_relacionadas` character varying
- **`public.cts_solucoes_historico`** (tabela, ~68.3 mil linhas)
  `id_seq` integer, `i_solucoes` integer, `sistema` character varying, `modulo` character varying, `topico` character varying, `i_usuarios` integer, `i_motivos` integer, `alterado_video` integer, `tempo` integer, `comentario` character varying, `entrada` character varying
- **`public.cts_solucoes_revisoes`** (tabela, ~25.8 mil linhas)
  `i_solucao` integer, `versao` integer, `entrada` character varying(10), `i_usuarios` integer
- **`public.cts_solucoes_revisoes_motivos`** (tabela, ~8 linhas)
  `i_motivos` integer, `descricao` character varying
- **`public.cts_solucoes_usuarios`** (tabela, ~61 linhas)
  `i_user` integer, `nome` character varying, `situacao` character varying(9), `email` character varying(4000)
- **`public.dCalendar`** (tabela, ~1.5 mil linhas)
  `Date` date, `Day` integer, `DayName` character varying, `Month` integer, `MonthName` character varying, `DayOfWeek` integer, `DayOfYear` integer, `Holiday` character varying, `Ten` integer, `TenName` character(2), `DayUsefulOfMonth` integer, `DayUsefulOfYear` integer, `Year` integer
- **`public.dCalendar_new`** (tabela, ~1.1 mil linhas)
  `Date` date, `Day` integer, `DayName` character varying, `Month` integer, `MonthName` character varying, `DayOfWeek` integer, `DayOfYear` integer, `Holiday` character varying, `Ten` integer, `TenName` character(2), `DayUsefulOfMonth` integer, `DayUsefulOfYear` integer, `Year` integer
- **`public.sgd_absences_type`** (tabela, ~0 linhas · PK (i_agenda_tipos))
  `i_agenda_tipos` integer, `descricao` character varying(64), `area` integer
- **`public.sgd_absencesreason`** (tabela, ~0 linhas)
  `i_agenda_motivos_ausencias` integer, `descricao` character varying(60), `ativo` boolean, `i_agenda_tipos` integer
- **`public.sgd_avaliacao_tria`** (tabela, ~10.5 mil linhas)
  `id` integer, `i_ssc` integer, `assunto` character varying, `descricao` character varying, `i_usuarios` integer, `sistema` character varying, `pergunta` character varying, `resposta` character varying, `resposta_ssc` character varying, `links` character varying, `utilizou` character varying, `motivo_nao` character varying, `entrada` character varying
- **`public.sgd_classification`** (tabela, ~0 linhas)
  `i_sss_classificacoes` integer, `descricao` character varying, `i_sss_classificacoes_ref` integer, `ordem` integer
- **`public.sgd_request`** (tabela, ~23.5 mi linhas)
  `code_ssc` integer, `i_ssc` integer, `date_entry` date, `dtime_entry` time without time zone, `classification` integer, `i_means_of_access` integer, `i_clientes` integer, `i_revendas` integer, `i_user_resales` integer, `dateconclusion` date, `i_user` integer, `no_access_system` integer, `i_sistema` integer, `i_modulo` integer, `i_topicos` integer
- **`public.sgd_schedule`** (tabela, ~36 linhas)
  `ddate` timestamp without time zone, `ddatetime` timestamp(6) without time zone, `i_user` integer, `i_type` integer, `i_absent_reasons` integer, `minutes` bigint
- **`public.sgd_usersclient`** (tabela, ~204 mil linhas)
  `i_user_resales` integer, `name` character varying(80), `email` character varying(256), `dateentry` timestamp(0) without time zone, `i_clientes` integer, `situation` character varying(7)
- **`public.vw_rel_acessos_ssc_usuarios`** (view, — linhas)
  `nome_unidade` character varying, `i_cliente` integer, `i_usuario` integer, `dt_entrada` date, `qtd_sscs` integer, `qtd_acessos` integer
- **`public.vw_rel_cts_gpt_saudacao`** (view, — linhas)
  `data_consulta` character varying(10), `i_usuario` numeric, `Inicio Saudação Configurado` text, `Fim Saudação Configurado` text, `Tipo Configuração` text, `i_alocation` integer

## Schema `temp_import`

- **`temp_import.CTS_Access_Count`** (tabela, ~397.5 mil linhas)
  `I_contagem_acessos` bigint, `I_solucoes` integer, `I_usuarios` integer, `DateEntry` date, `MeansOfAccess` integer
- **`temp_import.CTS_HistoryOfResponsible`** (tabela, ~1.6 mil linhas)
  `I_historicos` integer, `I_solucoes` integer, `I_responsaveis` integer, `DateEntry` timestamp with time zone, `DateExpiration` timestamp with time zone
- **`temp_import.CTS_Responsible`** (tabela, ~41 linhas)
  `I_usuarios` integer, `Name` character varying, `Situation` character varying(9), `email` character varying(4000)
- **`temp_import.CTS_SatisfactionSearch`** (tabela, ~63 linhas)
  `I_satisfaction_search` integer, `I_solucoes` integer, `I_usuarios` integer, `Useful` character varying, `Detail` character varying(4000), `DateEntry` date
- **`temp_import.CTS_Schedule`** (tabela, ~8.4 mil linhas)
  `dDate` timestamp with time zone, `dDateTime` timestamp with time zone, `i_user` integer, `i_type` integer, `i_absent_reasons` integer, `minutes` bigint
- **`temp_import.CTS_Solutions`** (tabela, ~9.1 mil linhas · PK (I_solucoes))
  `I_solucoes` integer, `DateEntry` timestamp with time zone, `DateExpiration` timestamp with time zone, `Description` character varying, `System` character varying, `Module` character varying, `Topic` character varying, `Classification` character varying, `linkSGD` character varying, `linkExternal` character varying
- **`temp_import.CTS_Solutions_VideoURL`** (tabela, ~8 mil linhas)
  `i_solucoes` numeric, `url_video` text
- **`temp_import.CTS_Users`** (tabela, ~911.5 mil linhas)
  `I_usuarios` integer, `Name` character varying, `I_Clientes` integer
- **`temp_import.SGD_Client`** (tabela, ~91.7 mil linhas)
  `I_clientes` integer, `NameClient` character varying, `I_representantes` integer, `I_revenda` integer, `ResaleSmallName` character varying, `DateRegister` date, `Referential` character varying, `Cep` character varying, `City` character varying, `InitialsState` character varying, `State` character varying
- **`temp_import.SGD_UserSituation`** (tabela, ~6.7 mil linhas)
  `i_usuarios` integer, `Situation` character varying(9)

## Schema `tria`

- **`tria.authentication`** (tabela, ~4 linhas · PK (id))
  `id` integer, `name` character varying(100), `user` character varying(100), `password` character varying(100), `access` character varying(50)
- **`tria.chat_interacoes`** (tabela, ~478.2 mil linhas)
  `i_chat_interacoes` integer, `i_user` integer, `DateEntry` timestamp with time zone, `contexto` character varying, `prompt` character varying, `completion` character varying, `likedislike` integer, `comentario` character varying, `curadoria_sit` character varying, `curadoria_mot` character varying, `curadoria_user` integer
- **`tria.chat_interacoes_bkp`** (tabela, ~578 linhas)
  `i_chat_interacoes` integer, `i_user` integer, `DateEntry` timestamp with time zone, `contexto` character varying, `prompt` character varying, `completion` character varying
- **`tria.chat_interacoes_teste`** (tabela, ~24 linhas)
  `i_chat_interacoes` integer, `i_user` integer, `DateEntry` timestamp with time zone, `contexto` character varying, `prompt` character varying, `completion` character varying, `likedislike` integer, `comentario` character varying
- **`tria.chat_sit_motv`** (tabela, ~11 linhas · PK (id_sit_motv))
  `id_sit_motv` integer, `desc` character varying, `type` character varying, `atv` boolean
