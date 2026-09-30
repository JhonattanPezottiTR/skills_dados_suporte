# Postgres · DB_REPORTS_CONSOLIDADOS — estrutura

> Última atualização: 2026-09-29 · Fonte: catálogo `pg_catalog` lido por `scripts/catalogo_postgres.py` (sessão READ ONLY, sem leitura de dados) · **Gerado automaticamente** — não editar à mão.
> Linhas = estimativa do planner (`reltuples`), não contagem exata. Quem carrega cada tabela: `dados-postgres-destinos.md` / `dados-fluxos-maestro.md`.

| Schema | Tabelas | Views |
|---|---|---|
| `public` | 10 | 0 |

## Schema `public`

- **`public.backup_nuvem`** (tabela, ~53.4 mil linhas · PK (i_clientes))
  `i_clientes` integer, `ultimo_backup_completo` timestamp without time zone, `i_hist_tecnico` bigint, `entrada` timestamp without time zone, `i_situacoes` smallint, `i_produtos` smallint, `users_regular` integer
- **`public.chains_ia`** (tabela, ~432.1 mil linhas)
  `login_usuario` character varying, `nome_usuario` character varying, `i_usuarios` integer, `i_usuarios_gestor` integer, `i_revendas` integer, `chain_utilizada` character varying, `prompt_usuario` text, `resposta_copiada` smallint, `entrada` timestamp without time zone
- **`public.jornada_fte`** (tabela, ~847 linhas · PK (id))
  `id` integer, `data_resposta` timestamp(0) without time zone, `email` character varying(150), `acao` character varying(50), `nome_registro` character varying(255), `tipo_vaga` character varying(50), `colaborador_saida` character varying(255), `id_colaborador` character varying(20), `data_identificacao` date, `coord_origem` character varying(150), `id_pai` integer, `etapa` character varying(100), `jreq` character varying(20), `candidato_aprovado` character varying(255), `coord_destino` character varying(150), `observacoes` text, `data_etapa` date, `verificacao` character varying(10), `data_carga` timestamp(0) without time zone, `cargo` character varying(100), `area_saida` character varying(100), `area_entrada` character varying(100)
- **`public.jornada_fte_etapas`** (tabela, ~0 linhas · PK (id))
  `id` integer, `ordem` smallint, `etapa_tarefa` character varying(255), `sla_etapa` smallint, `sla_acumulado` smallint, `responsavel` character varying(100), `legenda_quando_usar` text
- **`public.pendencias_suporte`** (tabela, ~5.6 mil linhas · PK (id))
  `id` integer, `i_ssc` integer, `i_ss` integer, `i_sss_classificacoes` integer, `i_cliente` integer, `pendente_n1` character varying(3), `pendente_n2` character varying(3), `pendente_n3` character varying(3), `data_pendente_n1` timestamp without time zone, `data_pendente_n2` timestamp without time zone, `data_pendente_n3` timestamp without time zone, `data_tramite_ssc` timestamp without time zone, `data_tramite_ss` timestamp without time zone, `nome_sistema` character varying(255), `nome_modulo` character varying(255), `nome_topico` character varying(255), `i_revendas` integer, `data_atualizacao` timestamp without time zone, `data_insercao` timestamp without time zone
- **`public.produtividade_n1`** (tabela, ~1.9 mi linhas · PK (id))
  `id` integer, `tipo` character varying(10), `unidade` character varying(100), `sistema` character varying(100), `modulo` character varying(100), `classificacao` character varying(200), `topico` character varying(500), `numero_ss` integer, `numero_ssc` integer, `numero_tramite` integer, `situacao_tramite` character varying(100), `data_tramite` date, `responsavel_tr` integer, `data_importacao` timestamp without time zone
- **`public.produtividade_n2`** (tabela, ~390.8 mil linhas · PK (id))
  `id` integer, `tipo` character varying(10), `unidade` character varying(100), `sistema` character varying(100), `modulo` character varying(100), `classificacao` character varying(100), `topico` character varying(255), `numero_ss` integer, `numero_tramite` integer, `situacao_tramite` character varying(100), `data_tramite` date, `responsavel_tramite` character varying(100)
- **`public.sla_pendency_time_snapshot`** (tabela, ~388.7 mil linhas · PK (data_snapshot, i_ss, sequential_iteraction))
  `data_snapshot` date, `i_ss` integer, `sequential_iteraction` integer, `total_time` numeric, `date_iteraction` date, `iteracao_open` integer, `processado_em` timestamp without time zone, `i_user` integer
- **`public.tb_demanda_lideres`** (tabela, ~663 mil linhas)
  `data` date, `email` character varying(150), `nome` character varying(200), `data_admissao` date, `anos_empresa` numeric(10,2), `area` character varying(100), `abreviacao_area` character varying(50), `cargo` character varying(120), `coordenador` character varying(200), `gerente` character varying(200), `ligacoes` integer, `dias_trabalhados` numeric(10,4), `total_ssc` integer, `meta_maxima_atendimento` integer, `valormeta` numeric(10,2), `pedido_ajuda` integer, `total_lider` integer, `atendimento_chat` integer
- **`public.tempo_tramite_interno`** (tabela, ~99.3 mil linhas · PK (id))
  `id` integer, `numero_ss` character varying(50), `analista_aguardando_resposta_interna` character varying(100), `analista_respondido_resposta_interna` character varying(100), `sistema` character varying(100), `modulo` character varying(100), `categoria_tramite_aguardando_resposta_interna` character varying(150), `tempo_resposta_interna` integer, `data_tramite_aguardando_resposta_interna` timestamp without time zone, `data_tramite_respondido_interna` timestamp without time zone, `data_importacao` timestamp without time zone
