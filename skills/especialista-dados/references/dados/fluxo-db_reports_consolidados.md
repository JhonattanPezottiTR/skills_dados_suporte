# Fluxo `DB_REPORTS_CONSOLIDADOS`

> Última atualização: 2026-09-30 · Fonte: `DB_REPORTS_CONSOLIDADOS.json` (Dataflow Power BI, modificado em 2026-07-20, cultura pt-BR) · **Gerado automaticamente** por `scripts/mapear_fluxos.py`.

| Entidade | Carrega | Origem | Base | Tabelas de origem | Colunas | Último refresh (UTC) |
|---|---|---|---|---|---|---|
| `tb_demanda_lideres` | sim | Postgres | DB_REPORTS_CONSOLIDADOS | `public.tb_demanda_lideres` | 18 | 2026-09-29T09:33:32 |
| `jornada_fte` | sim | Postgres | DB_REPORTS_CONSOLIDADOS | `public.jornada_fte` | 22 | 2026-09-29T09:34:03 |
| `jornada_fte_etapas` | sim | Postgres | DB_REPORTS_CONSOLIDADOS | `public.jornada_fte_etapas` | 7 | 2026-09-29T09:34:34 |
| `pendencias_suporte` | sim | Postgres | DB_REPORTS_CONSOLIDADOS | `public.pendencias_suporte` | 19 | 2026-09-29T09:35:05 |
| `chains_ia_usuarios` | sim | Postgres | DB_REPORTS_CONSOLIDADOS | `public.chains_ia` | 9 | 2026-09-29T09:35:35 |
| `sla_pendency_time_snapshot` | sim | Postgres | DB_REPORTS_CONSOLIDADOS | `public.sla_pendency_time_snapshot` | 8 | 2026-09-29T09:36:06 |
| `produtividade_n2` | sim | Postgres | DB_REPORTS_CONSOLIDADOS | `public.produtividade_n2` | 12 | 2026-09-29T09:36:37 |
| `backup_nuvem` | sim | Postgres | DB_REPORTS_CONSOLIDADOS | `public.backup_nuvem` | 7 | 2026-09-29T09:37:07 |
| `tempo_tramite_interno` | sim | Postgres | DB_REPORTS_CONSOLIDADOS | `public.tempo_tramite_interno` | 11 | 2026-09-29T09:37:38 |
| `produtividade_n1` | sim | Postgres | DB_REPORTS_CONSOLIDADOS | `public.produtividade_n1` | 14 | 2026-09-29T09:38:09 |

## `tb_demanda_lideres`

- **Origem:** Postgres · base `DB_REPORTS_CONSOLIDADOS`
- `public.tb_demanda_lideres` ← historic-tb-interacoes-lideres-plug
- **Colunas entregues:** `data` (date), `email` (string), `nome` (string), `data_admissao` (date), `anos_empresa` (double), `area` (string), `abreviacao_area` (string), `cargo` (string), `coordenador` (string), `gerente` (string), `ligacoes` (int64), `dias_trabalhados` (double), `total_ssc` (int64), `meta_maxima_atendimento` (int64), `valormeta` (double), `pedido_ajuda` (int64), `total_lider` (int64), `atendimento_chat` (int64)

## `jornada_fte`

- **Origem:** Postgres · base `DB_REPORTS_CONSOLIDADOS`
- `public.jornada_fte` ← não mapeado no Maestro
- **Colunas entregues:** `id` (int64), `data_resposta` (dateTime), `email` (string), `acao` (string), `nome_registro` (string), `tipo_vaga` (string), `colaborador_saida` (string), `id_colaborador` (string), `data_identificacao` (date), `coord_origem` (string), `id_reg_atualizado` (int64), `etapa` (string), `jreq` (string), `candidato_aprovado` (string), `coord_destino` (string), `observacoes` (string), `data_etapa` (date), `verificacao` (string), `data_carga` (dateTime), `cargo` (string), `area_saida` (string), `area_entrada` (string)

## `jornada_fte_etapas`

- **Origem:** Postgres · base `DB_REPORTS_CONSOLIDADOS`
- `public.jornada_fte_etapas` ← não mapeado no Maestro
- **Colunas entregues:** `id` (int64), `ordem` (int64), `etapa_tarefa` (string), `sla_etapa` (int64), `sla_acumulado` (int64), `responsavel` (string), `legenda_quando_usar` (string)

## `pendencias_suporte`

- **Origem:** Postgres · base `DB_REPORTS_CONSOLIDADOS`
- `public.pendencias_suporte` ← não mapeado no Maestro
- **Colunas entregues:** `id` (int64), `i_ssc` (int64), `i_ss` (int64), `i_sss_classificacoes` (int64), `i_cliente` (int64), `pendente_n1` (string), `pendente_n2` (string), `pendente_n3` (string), `data_pendente_n1` (dateTime), `data_pendente_n2` (dateTime), `data_pendente_n3` (dateTime), `data_tramite_ssc` (dateTime), `data_tramite_ss` (dateTime), `nome_sistema` (string), `nome_modulo` (string), `nome_topico` (string), `i_revendas` (int64), `data_atualizacao` (dateTime), `data_insercao` (dateTime)

## `chains_ia_usuarios`

- **Origem:** Postgres · base `DB_REPORTS_CONSOLIDADOS`
- `public.chains_ia` ← não mapeado no Maestro
- **Colunas entregues:** `login_usuario` (string), `nome_usuario` (string), `i_usuarios` (int64), `i_usuarios_gestor` (int64), `i_revendas` (int64), `chain_utilizada` (string), `prompt_usuario` (string), `resposta_copiada` (int64), `entrada` (dateTime)

## `sla_pendency_time_snapshot`

- **Origem:** Postgres · base `DB_REPORTS_CONSOLIDADOS`
- `public.sla_pendency_time_snapshot` ← não mapeado no Maestro
- **Colunas entregues:** `data_snapshot` (date), `i_ss` (int64), `sequential_iteraction` (int64), `total_time` (double), `date_iteraction` (date), `iteracao_open` (int64), `processado_em` (dateTime), `i_user` (int64)

## `produtividade_n2`

- **Origem:** Postgres · base `DB_REPORTS_CONSOLIDADOS`
- `public.produtividade_n2` ← não mapeado no Maestro
- **Colunas entregues:** `id` (int64), `tipo` (string), `unidade` (string), `sistema` (string), `modulo` (string), `classificacao` (string), `topico` (string), `numero_ss` (int64), `numero_tramite` (int64), `situacao_tramite` (string), `data_tramite` (date), `responsavel_tramite` (string)

## `backup_nuvem`

- **Origem:** Postgres · base `DB_REPORTS_CONSOLIDADOS`
- `public.backup_nuvem` ← não mapeado no Maestro
- **Colunas entregues:** `i_clientes` (int64), `ultimo_backup_completo` (dateTime), `i_hist_tecnico` (int64), `entrada` (dateTime), `i_situacoes` (int64), `i_produtos` (int64), `users_regular` (int64)

## `tempo_tramite_interno`

- **Origem:** Postgres · base `DB_REPORTS_CONSOLIDADOS`
- `public.tempo_tramite_interno` ← não mapeado no Maestro
- **Colunas entregues:** `id` (int64), `numero_ss` (string), `analista_aguardando_resposta_interna` (string), `analista_respondido_resposta_interna` (string), `sistema` (string), `modulo` (string), `categoria_tramite_aguardando_resposta_interna` (string), `tempo_resposta_interna` (int64), `data_tramite_aguardando_resposta_interna` (dateTime), `data_tramite_respondido_interna` (dateTime), `data_importacao` (dateTime)

## `produtividade_n1`

- **Origem:** Postgres · base `DB_REPORTS_CONSOLIDADOS`
- `public.produtividade_n1` ← não mapeado no Maestro
- **Colunas entregues:** `id` (int64), `tipo` (string), `unidade` (string), `sistema` (string), `modulo` (string), `classificacao` (string), `topico` (string), `numero_ss` (int64), `numero_ssc` (int64), `numero_tramite` (int64), `situacao_tramite` (string), `data_tramite` (date), `responsavel_tr` (int64), `data_importacao` (dateTime)
