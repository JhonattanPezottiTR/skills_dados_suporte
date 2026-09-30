# Postgres · DB_WEBCHAT — estrutura

> Última atualização: 2026-09-29 · Fonte: catálogo `pg_catalog` lido por `scripts/catalogo_postgres.py` (sessão READ ONLY, sem leitura de dados) · **Gerado automaticamente** — não editar à mão.
> Linhas = estimativa do planner (`reltuples`), não contagem exata. Quem carrega cada tabela: `dados-postgres-destinos.md` / `dados-fluxos-maestro.md`.

| Schema | Tabelas | Views |
|---|---|---|
| `public` | 15 | 2 |
| `temp` | 6 | 0 |

## Schema `public`

- **`public.OLDprotocols_transcription`** (tabela, ~58.9 mil linhas)
  `_id` character varying(25), `protocol_number` character varying(25), `trasncription` character varying
- **`public.disregard_dissatisfaction`** (tabela, ~631 linhas)
  `i_response` integer, `i_ssc_ss_chat` character varying, `type` character varying, `justif` character varying, `date_incl` timestamp without time zone, `email` character varying
- **`public.protocols`** (tabela, ~2.6 mi linhas)
  `_id` character varying(25), `protocol_number` character varying(25), `i_userchat` character varying(25), `initialqueue` character varying, `createdatdate` character varying(25), `interval` character varying(5), `rating` character varying(15), `ratingdesc` character varying, `duration` integer, `closedate` character varying(25), `id_client` bigint, `closure_motive` character varying, `cli_name_contact` character varying, `cli_user_onvio` character varying, `i_ssc` integer, `tenant_id` character varying, `grupo_atend` character varying, `id_motv_insatisf` character varying, `attendancedate` timestamp without time zone
- **`public.protocols_all`** (tabela, ~2.2 mi linhas)
  `_id` character varying(25), `protocol_number` character varying(25), `i_userchat` character varying(25), `origem` character varying, `createdatdate` character varying(25), `closedate` character varying(25), `id_client` bigint, `tenant_id` character varying, `rating` character varying, `rating_desc` character varying, `id_motv_insatisf` character varying, `i_ssc` integer, `interval` character varying, `tag` character varying, `modulo` character varying, `grupo_atend` character varying, `i_system` integer, `i_module` integer
- **`public.protocols_history`** (tabela, ~5.8 mi linhas)
  `_id` character varying(25), `protocol_number` character varying(25), `startdate` character varying(25), `stopdate` character varying(25), `startinterval` character varying(5), `seconds` integer, `actor` character varying(15), `i_userchat` character varying(25), `queuegroup` character varying, `transfer` character varying(1)
- **`public.protocols_ia`** (tabela, ~1 mi linhas)
  `_id` text, `protocolo_number` text, `resumo` text, `problema_1` text, `problema_2` text, `frustacoes` text, `dificuldades` text, `analise_especifica` text, `motivo_encerramento` text
- **`public.protocols_sequence_message`** (tabela, ~111.8 mi linhas)
  `protocol_number` character varying(25), `_date` character varying(25), `integrated_id` integer, `seconds` integer, `actor` character varying(50), `type` character varying(50), `details` character varying
- **`public.protocols_teste`** (tabela, ~40 linhas)
  `_id` character varying(25), `protocol_number` character varying(25), `trasncription` character varying
- **`public.protocols_transcript`** (tabela, ~697.5 mil linhas)
  `_id` character varying(25), `protocol_number` character varying(25), `trasncription` character varying
- **`public.protocols_transcription`** (tabela, ~2.8 mi linhas · PK (_id))
  `_id` character varying(25), `protocol_number` character varying(25), `trasncription` text
- **`public.sgd_cli_liberados_chat`** (tabela, ~246.1 mil linhas)
  `i_cliente` integer, `liberado_chat_gpt` integer, `liberado_tria_plug` integer, `liberado_chat_humano` integer, `data_hora` character varying
- **`public.sgd_users`** (tabela, ~9.4 mil linhas)
  `i_user` integer, `user` character varying, `email` character varying, `admission` character varying, `date_inactivation` character varying, `dismission` character varying, `name` character varying, `resale` character varying, `i_resale` integer, `type_resale` character varying
- **`public.tenant_id`** (tabela, ~17 linhas)
  `tenant_id` character varying, `tenant_desc` character varying, `token_tenant` character varying
- **`public.users`** (tabela, ~1.1 mil linhas)
  `i_userchat` character varying(25), `email` character varying, `username` character varying, `name` character varying, `status` character varying, `role` character varying, `createddate` character varying(25), `updatedate` character varying(25), `i_user_sgd` character varying, `tenant_id` character varying
- **`public.users_historicstatus`** (tabela, ~786.9 mil linhas)
  `i_userchat` character varying(25), `historicstart` character varying(25), `status` character varying
- **`public.vw_analytics_relatorio_chat`** (view, — linhas) — Relatório de transcrições de chat; users_Genesys via dblink; tenant_id filtrado no app.
  `ID` character varying(25), `Protocolo` character varying(25), `Data/Hora` character varying(25), `Data` date, `Nome` text, `Coordenador` text, `Gerente` text, `ID Cliente SGD` bigint, `ID SSC SGD` integer, `Região` text, `Fila` character varying, `Grupo Atendimento` character varying, `Votação` text, `Descrição Votação` text, `Resumo` text, `Problemas` text, `Frustrações` text, `Dificuldades` text, `Análise Específica` text, `Motivo Encerramento` text, `Transcrição` text, `tenant_id` character varying
- **`public.vw_protocolos_all`** (view, — linhas)
  `_id` character varying(25), `protocol_number` character varying(25), `i_userchat` character varying(25), `origem` character varying, `origem_dados` character varying, `createdatdate` date, `closedate` date, `id_client` bigint, `tenant_id` character varying, `rating` text, `rating_desc` character varying, `id_motv_insatisf` character varying, `i_ssc` integer, `interval` character varying, `tag` character varying, `modulo` character varying, `i_system_sgd` integer, `i_module_sgd` integer, `sistema_sgd` text, `modulo_sgd` text

## Schema `temp`

- **`temp.plugRealTimeFila`** (tabela, ~0 linhas)
  `id_protocol` text, `queue` text, `regional` text, `tempo` integer, `tenant_id` text, `id_cliente` text, `hora_envio` text
- **`temp.plugRealTimeFilaMaxDia`** (tabela, ~95 linhas · PK (queue, regional))
  `queue` text, `regional` text, `maior_seg` integer, `dia` date, `hora_pico` text, `atualizado_em` timestamp with time zone
- **`temp.tem_protocols`** (tabela, ~16.8 mil linhas)
  `_id` character varying(25), `i_userchat` character varying(25), `_protocol_number` character varying(25), `initialqueue` character varying, `integrated_id_contact` integer, `integrated_id_attendant` integer, `start_at` character varying(25), `end_at` character varying(25), `_time` integer, `_record` timestamp without time zone
- **`temp.tfm_protocols`** (tabela, ~2.3 mil linhas)
  `_id` character varying(25), `i_userchat` character varying(25), `_protocol_number` character varying(25), `initialqueue` character varying, `integrated_id_contact` integer, `integrated_id_attendant` integer, `start_at` character varying(25), `end_at` character varying(25), `_time` integer, `_record` timestamp without time zone
- **`temp.tma_protocols`** (tabela, ~2.3 mil linhas)
  `_id` character varying(25), `i_userchat` character varying(25), `_protocol_number` character varying(25), `initialqueue` character varying, `integrated_id_contact` integer, `integrated_id_attendant` integer, `start_at` character varying(25), `end_at` character varying(25), `_time` integer, `_record` timestamp without time zone
- **`temp.tme_protocols`** (tabela, ~2.5 mil linhas)
  `_id` character varying(25), `i_userchat` character varying(25), `_protocol_number` character varying(25), `initialqueue` character varying, `integrated_id_contact` integer, `integrated_id_attendant` integer, `start_at` character varying(25), `end_at` character varying(25), `_time` integer, `_record` timestamp without time zone
