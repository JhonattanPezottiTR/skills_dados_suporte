# Fluxo `DB_OCORRENCIAS`

> Última atualização: 2026-09-30 · Fonte: `DB_OCORRENCIAS.json` (Dataflow Power BI, modificado em 2026-09-09, cultura en-US) · **Gerado automaticamente** por `scripts/mapear_fluxos.py`.

| Entidade | Carrega | Origem | Base | Tabelas de origem | Colunas | Último refresh (UTC) |
|---|---|---|---|---|---|---|
| `sgd_ocorrencia` | sim | Postgres | DB_SGD | `public.sgd_ocorrencia` | 21 | 2026-09-29T09:02:33 |
| `sgd_ocorrencia_area` | sim | Postgres | DB_SGD | `public.sgd_ocorrencia_area` | 3 | 2026-09-29T09:03:03 |
| `sgd_ocorrencia_categoria` | sim | Postgres | DB_SGD | `public.sgd_ocorrencia_categoria` | 4 | 2026-09-29T09:03:34 |
| `sgd_ocorrencia_setor` | sim | Postgres | DB_SGD | `public.sgd_ocorrencia_setor` | 2 | 2026-09-29T09:04:04 |
| `sgd_ocorrencia_situacao` | sim | Postgres | DB_SGD | `public.sgd_ocorrencia_situacao` | 2 | 2026-09-29T09:04:35 |
| `sgd_ocorrencia_sane` | sim | Postgres | DB_SGD | `public.sgd_ocorrencia_sane` | 2 | 2026-09-29T09:05:05 |
| `sgd_ocorrencia_ss` | sim | Postgres | DB_SGD | `public.sgd_ocorrencia_ss` | 2 | 2026-09-29T09:05:36 |
| `sgd_ocorrencia_ssc` | sim | Postgres | DB_SGD | `public.sgd_ocorrencia_ssc` | 2 | 2026-09-29T09:06:06 |
| `sgd_ocorrencia_tramite` | sim | Postgres | DB_SGD | `public.sgd_ocorrencia_tramite` | 5 | 2026-09-29T09:06:37 |
| `sgd_ocorrencia_prioridade` | sim | Postgres | DB_SGD | `public.sgd_ocorrencia_prioridade` | 3 | 2026-09-29T09:07:07 |

## `sgd_ocorrencia`

- **Origem:** Postgres · base `DB_SGD`
- `public.sgd_ocorrencia` ← import-sgd-diario (UPDATE no lugar); import-sgd-diario (substitui por situação (não por data))
- **Colunas entregues:** `i_ocorrencia` (int64), `date_entry` (int64), `date_time` (time), `i_area_origem` (int64), `i_area_destino` (int64), `i_responsavel` (int64), `i_usuario` (int64), `i_clientes` (int64), `i_revendas` (int64), `i_situacao` (int64), `i_categoria` (int64), `i_setor_origem` (int64), `i_setor_destino` (int64), `i_ocorrencia_pai` (string), `ultimo_tramite` (dateTime), `tipo` (int64), `entrada_email` (string), `resposta_email` (string), `tme_minutos` (int64), `tma_total_minutos` (int64), `tma_sub_minutos` (int64)

SQL nativo:

```sql
SELECT 
i_ocorrencia, 
date_entry, 
date_time, 
i_area_origem, 
i_area_destino, 
i_responsavel, 
i_usuario, 
i_clientes, 
i_revendas, 
i_situacao, 
i_categoria, 
i_setor_origem, 
i_setor_destino, 
i_ocorrencia_pai, 
ultimo_tramite, 
tipo, 
entrada_email, 
resposta_email, 
tme_minutos, 
tma_total_minutos,
tma_sub_minutos
FROM public.sgd_ocorrencia;
```

## `sgd_ocorrencia_area`

- **Origem:** Postgres · base `DB_SGD`
- `public.sgd_ocorrencia_area` ← import-sgd-diario (recarga TOTAL)
- **Colunas entregues:** `i_area` (int64), `description` (string), `i_setor` (int64)

## `sgd_ocorrencia_categoria`

- **Origem:** Postgres · base `DB_SGD`
- `public.sgd_ocorrencia_categoria` ← import-sgd-diario (recarga TOTAL)
- **Colunas entregues:** `i_categoria` (int64), `description` (string), `i_area` (int64), `i_setor` (int64)

SQL nativo:

```sql
SELECT 
i_categoria, 
description, 
i_area, 
i_setor
FROM public.sgd_ocorrencia_categoria;
```

## `sgd_ocorrencia_setor`

- **Origem:** Postgres · base `DB_SGD`
- `public.sgd_ocorrencia_setor` ← import-sgd-diario (recarga TOTAL)
- **Colunas entregues:** `i_setor` (int64), `description` (string)

SQL nativo:

```sql
SELECT 
i_setor, 
description
FROM public.sgd_ocorrencia_setor;
```

## `sgd_ocorrencia_situacao`

- **Origem:** Postgres · base `DB_SGD`
- `public.sgd_ocorrencia_situacao` ← import-sgd-diario (recarga TOTAL)
- **Colunas entregues:** `i_situacao` (int64), `description` (string)

SQL nativo:

```sql
SELECT 
i_situacao, 
description
FROM public.sgd_ocorrencia_situacao;
```

## `sgd_ocorrencia_sane`

- **Origem:** Postgres · base `DB_SGD`
- `public.sgd_ocorrencia_sane` ← import-sgd-diario (recarga TOTAL)
- **Colunas entregues:** `i_ocorrencia` (int64), `i_sane` (int64)

SQL nativo:

```sql
SELECT 
i_ocorrencia, 
i_sane
FROM public.sgd_ocorrencia_sane;
```

## `sgd_ocorrencia_ss`

- **Origem:** Postgres · base `DB_SGD`
- `public.sgd_ocorrencia_ss` ← import-sgd-diario (recarga TOTAL)
- **Colunas entregues:** `i_ocorrencia` (int64), `i_ss` (int64)

SQL nativo:

```sql
SELECT 
i_ocorrencia, 
i_ss
FROM public.sgd_ocorrencia_ss;
```

## `sgd_ocorrencia_ssc`

- **Origem:** Postgres · base `DB_SGD`
- `public.sgd_ocorrencia_ssc` ← import-sgd-diario (recarga TOTAL)
- **Colunas entregues:** `i_ocorrencia` (int64), `i_ssc` (int64)

SQL nativo:

```sql
SELECT 
i_ocorrencia, 
i_ssc
FROM public.sgd_ocorrencia_ssc;
```

## `sgd_ocorrencia_tramite`

- **Origem:** Postgres · base `DB_SGD`
- `public.sgd_ocorrencia_tramite` ← import-sgd-diario (substitui janela de 1 dia(s))
- **Colunas entregues:** `i_tram` (int64), `date_tram` (string), `i_user` (int64), `i_ocorrencia` (int64), `i_situacao` (int64)

## `sgd_ocorrencia_prioridade`

- **Origem:** Postgres · base `DB_SGD`
- `public.sgd_ocorrencia_prioridade` ← import-sgd-diario (recarga TOTAL)
- **Colunas entregues:** `id_ocorrencia` (int64), `id_prioridade` (int64), `descricao` (string)
