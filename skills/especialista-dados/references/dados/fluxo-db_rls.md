# Fluxo `DB_RLS`

> Última atualização: 2026-09-30 · Fonte: `DB_RLS.json` (Dataflow Power BI, modificado em 2025-12-23, cultura en-US) · **Gerado automaticamente** por `scripts/mapear_fluxos.py`.

| Entidade | Carrega | Origem | Base | Tabelas de origem | Colunas | Último refresh (UTC) |
|---|---|---|---|---|---|---|
| `rls_user` | sim | Postgres | DB_SGD | `public.sgd_resale`, `public.sgd_users` | 7 | 2026-09-29T07:02:34 |
| `rls_resale_old` | não (auxiliar) | Json.Document, Table.FromRows | — | — | 0 | — |
| `rls_username_old` | não (auxiliar) | Json.Document, Table.FromRows | — | — | 0 | — |
| `rls_username` | sim | Excel.Workbook, Web.Contents | — | — | 11 | 2026-09-29T07:03:05 |
| `rls_resale` | sim | Excel.Workbook, Web.Contents | — | — | 3 | 2026-09-29T07:03:36 |
| `rls_resale_tenant_id` | sim | Excel.Workbook, Web.Contents | — | — | 2 | 2026-09-29T07:04:06 |

## `rls_user`

- **Origem:** Postgres · base `DB_SGD`
- `public.sgd_resale` ← import-sgd-diario (recarga TOTAL)
- `public.sgd_users` ← import-sgd-diario (recarga TOTAL)
- **Colunas entregues:** `i_user` (int64), `user` (string), `email` (string), `servidor_email` (string), `name` (string), `resale` (string), `i_resale` (int64)

SQL nativo:

```sql
SELECT 
        i_user, 
        "user", 
        email,
        email as servidor_email,
        name, 
        resale,
        coalesce(r.i_resale,0) as i_resale
    FROM public.sgd_users left join public.sgd_resale as r on r.i_resale = sgd_users.i_resale
    where dismission = '0'
    and "user" <> ''
```

## `rls_resale_old`

- **Origem:** Json.Document, Table.FromRows

## `rls_username_old`

- **Origem:** Json.Document, Table.FromRows

## `rls_username`

- **Origem:** Excel.Workbook, Web.Contents
- **Colunas entregues:** `email` (string), `email_rls` (string), `rel_satisfacao` (string), `rel_produtividade` (string), `rel_demanda` (string), `rel_pendencia` (string), `rel_tempo_interno` (string), `rel_ausencias` (string), `rel_utiliza_solucao` (string), `rel_chat_plug` (string), `reescrever_ia` (string)

## `rls_resale`

- **Origem:** Excel.Workbook, Web.Contents
- **Colunas entregues:** `email` (string), `i_resales` (string), `tennant_id_chat` (string)

## `rls_resale_tenant_id`

- **Origem:** Excel.Workbook, Web.Contents
- **Colunas entregues:** `i_resales` (int64), `tennant_id_chat` (string)
