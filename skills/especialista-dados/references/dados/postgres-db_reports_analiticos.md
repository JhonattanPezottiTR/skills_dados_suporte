# Postgres · DB_REPORTS_ANALITICOS — estrutura

> Última atualização: 2026-09-29 · Fonte: catálogo `pg_catalog` lido por `scripts/catalogo_postgres.py` (sessão READ ONLY, sem leitura de dados) · **Gerado automaticamente** — não editar à mão.
> Linhas = estimativa do planner (`reltuples`), não contagem exata. Quem carrega cada tabela: `dados-postgres-destinos.md` / `dados-fluxos-maestro.md`.

| Schema | Tabelas | Views |
|---|---|---|
| `public` | 5 | 1 |
| `view` | 0 | 1 |

## Schema `public`

- **`public.tb_colaboradores`** (tabela, ~4.9 mi linhas)
  `data` date, `id_usuario_sgd` integer, `ususrio_sgd` character varying, `email` character varying, `data_admissao` date, `tempo_casa_dias` integer, `tempo_casa_meses` numeric, `tempo_casa_anos` numeric, `data_inativacao` date, `demissao` integer, `nome` character varying, `resale` character varying, `id_resale` integer, `tipo_resale` character varying, `id_usuario_genesys` text, `status_genesys` text, `jabber_id` text, `i_alocation` integer, `desde` date, `descricao` character varying(100), `abreviacao` character varying(50), `id_cargo` integer, `descricao_cargo` character varying(100), `descricao_resale` character varying(100), `id_supervisor` integer, `supervisor` character varying, `gerente` character varying, `id_chat` character varying(25), `atibuicao_chat` character varying, `tenant_id` character varying, `horario_inicio_matutino` character varying, `horario_fim_matutino` character varying, `horario_inicio_vespertino` character varying, `horario_fim_vespertino` character varying
- **`public.tb_interacoes_lideres_plug_analitico`** (tabela, ~429 mil linhas)
  `_id` character varying(25), `protocol_number` character varying(25), `i_userchat` character varying(25), `origem` character varying, `createddate` character varying(25), `closedate` character varying(25), `id_client` bigint, `tenant_id` character varying, `rating` character varying, `rating_desc` character varying, `id_motiv_insatisf` character varying, `issc` integer, `interval` character varying, `tag` character varying, `modulo` character varying, `grupo_atend` character varying, `i_system` integer, `i_modulo` integer, `tenant_desc` character varying, `descricao_modulo` text, `lider` character varying, `coordenador_lider` character varying, `gerente_lider` character varying, `tecnico` character varying, `coordenador_tecnico` character varying, `gerente_tecnico` character varying, `descricao_sistema` character varying
- **`public.tb_meta_capacidade_atendimento`** (tabela, ~120 linhas · PK (id_meta_atendimento))
  `id_meta_atendimento` integer, `acesso` character varying(60), `setor` character varying(30), `cargo` character varying(120), `tempo_casa_min_meses` integer, `tempo_casa_max_meses` integer, `meta_maxima_atendimento` integer
- **`public.tb_ocorrencias_analitica`** (tabela, ~228.9 mil linhas)
  `i_tram` integer, `date_tram` character varying(19), `ordem_tramite` bigint, `tempo_tramite_seg` bigint, `i_user` integer, `i_ocorrencia` integer, `i_ssc` integer, `i_sane` integer, `i_ss` integer, `id_situacao_tramite` integer, `descricao_situacao_tramite` character varying(60), `votacao` character varying(50), `motivo` text, `tempo` integer, `date_entry` character varying(10), `data_hora_abertura_ocorrencia` timestamp without time zone, `i_area_origem` integer, `i_area_destino` integer, `i_responsavel` integer, `i_usuario` integer, `i_clientes` integer, `nome_cliente` text, `cidade` text, `estado` text, `i_revendas` integer, `i_situacao` integer, `i_categoria` integer, `i_setor_origem` integer, `i_setor_destino` integer, `i_ocorrencia_pai` character varying, `ultimo_tramite` timestamp without time zone, `tipo` integer, `descricao_area_origem` character varying(60), `descricao_area_destino` character varying(60), `descricao_setor_origem` character varying(60), `descricao_setor_destino` character varying(60), `descricao_categoria` character varying(60), `id_prioridade` integer, `nome_prioridade` character varying(250), `data` date, `id_usuario_sgd` integer, `usuario_sgd` character varying, `email` character varying, `data_admissao` date, `tempo_casa_dias` integer, `tempo_casa_meses` numeric, `tempo_casa_anos` numeric, `data_inativacao` date, `demissao` integer, `nome` character varying, `resale` character varying, `id_resale` integer, `tipo_resale` character varying, `id_usuario_genesys` text, `status_genesys` text, `jabber_id` text, `id_alocacao` integer, `desde` date, `descricao` character varying(100), `abreviacao` character varying(50), `id_cargo` integer, `descricao_cargo` character varying(100), `descricao_resale` character varying(100), `id_supervisor` integer, `supervisor` character varying, `gerente` character varying, `id_chat` character varying(25), `atribuicao_chat` character varying, `tenant_id` character varying
- **`public.tb_satisfacao_subocorrencias`** (tabela, ~1.6 mil linhas)
  `subocorrencia` integer, `votacao` character varying(50), `motivo` text
- **`public.vw_colaboradores_resale`** (view, — linhas)
  `nome` character varying, `email` character varying, `area` text, `canal` text, `coordenador` character varying, `gerente` character varying

## Schema `view`

- **`view.vw_colaboradores`** (view, — linhas)
  `nome` text, `email` text, `supervisor` text, `departamento` text, `gerente` text, `role_genesys` text, `lider_area` text, `revenda` text, `meio_acesso` text, `horario_inicio_matutino` character varying, `horario_fim_matutino` character varying, `horario_inicio_vespertino` character varying, `horario_fim_vespertino` character varying
