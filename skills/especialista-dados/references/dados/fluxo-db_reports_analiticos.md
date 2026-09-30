# Fluxo `DB_REPORTS_ANALITICOS`

> Última atualização: 2026-09-30 · Fonte: `DB_REPORTS_ANALITICOS.json` (Dataflow Power BI, modificado em 2026-08-28, cultura pt-BR) · **Gerado automaticamente** por `scripts/mapear_fluxos.py`.

| Entidade | Carrega | Origem | Base | Tabelas de origem | Colunas | Último refresh (UTC) |
|---|---|---|---|---|---|---|
| `tb_colaboradores` | sim | Postgres | DB_REPORTS_ANALITICOS | `public.tb_colaboradores` | 34 | 2026-09-29T09:35:02 |
| `tb_meta_capacidade_atendimento` | sim | Postgres | DB_REPORTS_ANALITICOS | `public.tb_meta_capacidade_atendimento` | 7 | 2026-09-29T09:35:32 |
| `tb_ocorrencias_analitica` | sim | Postgres | DB_REPORTS_ANALITICOS | `public.tb_ocorrencias_analitica` | 69 | 2026-09-29T09:36:03 |
| `tb_interacoes_lideres_plug_analitico` | sim | Postgres | DB_REPORTS_ANALITICOS | `public.tb_interacoes_lideres_plug_analitico` | 27 | 2026-09-29T09:36:34 |

## `tb_colaboradores`

- **Origem:** Postgres · base `DB_REPORTS_ANALITICOS`
- `public.tb_colaboradores` ← historic-tb-colaboradores
- **Colunas entregues:** `data` (date), `id_usuario_sgd` (int64), `ususrio_sgd` (string), `email` (string), `data_admissao` (date), `tempo_casa_dias` (int64), `tempo_casa_meses` (double), `tempo_casa_anos` (double), `data_inativacao` (date), `demissao` (int64), `nome` (string), `resale` (string), `id_resale` (int64), `tipo_resale` (string), `id_usuario_genesys` (string), `status_genesys` (string), `jabber_id` (string), `i_alocation` (int64), `desde` (date), `descricao` (string), `abreviacao` (string), `id_cargo` (int64), `descricao_cargo` (string), `descricao_resale` (string), `id_supervisor` (int64), `supervisor` (string), `gerente` (string), `id_chat` (string), `atibuicao_chat` (string), `tenant_id` (string), `horario_inicio_matutino` (string), `horario_fim_matutino` (string), `horario_inicio_vespertino` (string), `horario_fim_vespertino` (string)

## `tb_meta_capacidade_atendimento`

- **Origem:** Postgres · base `DB_REPORTS_ANALITICOS`
- `public.tb_meta_capacidade_atendimento` ← não mapeado no Maestro
- **Colunas entregues:** `id_meta_atendimento` (int64), `acesso` (string), `setor` (string), `cargo` (string), `tempo_casa_min_meses` (int64), `tempo_casa_max_meses` (int64), `meta_maxima_atendimento` (int64)

## `tb_ocorrencias_analitica`

- **Origem:** Postgres · base `DB_REPORTS_ANALITICOS`
- `public.tb_ocorrencias_analitica` ← historic-tb-ocorrencias-analitica
- **Colunas entregues:** `i_tram` (int64), `date_tram` (string), `ordem_tramite` (int64), `tempo_tramite_seg` (int64), `i_user` (int64), `i_ocorrencia` (int64), `i_ssc` (int64), `i_sane` (int64), `i_ss` (int64), `id_situacao_tramite` (int64), `descricao_situacao_tramite` (string), `votacao` (string), `motivo` (string), `tempo` (int64), `date_entry` (string), `data_hora_abertura_ocorrencia` (dateTime), `i_area_origem` (int64), `i_area_destino` (int64), `i_responsavel` (int64), `i_usuario` (int64), `i_clientes` (int64), `nome_cliente` (string), `cidade` (string), `estado` (string), `i_revendas` (int64), `i_situacao` (int64), `i_categoria` (int64), `i_setor_origem` (int64), `i_setor_destino` (int64), `i_ocorrencia_pai` (string), `ultimo_tramite` (dateTime), `tipo` (int64), `descricao_area_origem` (string), `descricao_area_destino` (string), `descricao_setor_origem` (string), `descricao_setor_destino` (string), `descricao_categoria` (string), `id_prioridade` (int64), `nome_prioridade` (string), `data` (date), `id_usuario_sgd` (int64), `usuario_sgd` (string), `email` (string), `data_admissao` (date), `tempo_casa_dias` (int64), `tempo_casa_meses` (double), `tempo_casa_anos` (double), `data_inativacao` (date), `demissao` (int64), `nome` (string), `resale` (string), `id_resale` (int64), `tipo_resale` (string), `id_usuario_genesys` (string), `status_genesys` (string), `jabber_id` (string), `id_alocacao` (int64), `desde` (date), `descricao` (string), `abreviacao` (string), `id_cargo` (int64), `descricao_cargo` (string), `descricao_resale` (string), `id_supervisor` (int64), `supervisor` (string), `gerente` (string), `id_chat` (string), `atribuicao_chat` (string), `tenant_id` (string)

## `tb_interacoes_lideres_plug_analitico`

- **Origem:** Postgres · base `DB_REPORTS_ANALITICOS`
- `public.tb_interacoes_lideres_plug_analitico` ← historic-tb-interacoes-lideres-plug
- **Colunas entregues:** `_id` (string), `protocol_number` (string), `i_userchat` (string), `origem` (string), `createddate` (string), `closedate` (string), `id_client` (int64), `tenant_id` (string), `rating` (string), `rating_desc` (string), `id_motiv_insatisf` (string), `issc` (int64), `interval` (string), `tag` (string), `modulo` (string), `grupo_atend` (string), `i_system` (int64), `i_modulo` (int64), `tenant_desc` (string), `descricao_modulo` (string), `lider` (string), `coordenador_lider` (string), `gerente_lider` (string), `tecnico` (string), `coordenador_tecnico` (string), `gerente_tecnico` (string), `descricao_sistema` (string)
