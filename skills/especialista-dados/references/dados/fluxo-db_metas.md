# Fluxo `DB_METAS`

> Última atualização: 2026-09-30 · Fonte: `DB_METAS.json` (Dataflow Power BI, modificado em 2026-01-05, cultura en-US) · **Gerado automaticamente** por `scripts/mapear_fluxos.py`.

| Entidade | Carrega | Origem | Base | Tabelas de origem | Colunas | Último refresh (UTC) |
|---|---|---|---|---|---|---|
| `goals` | sim | Postgres | DB_SGD | `public.calendar`, `public.goals` | 7 | 2026-09-29T15:37:33 |

## `goals`

- **Origem:** Postgres · base `DB_SGD`
- `public.calendar` ← mantida manualmente por fora do Maestro (orq:modules/import_agendas/skills.md:55)
- `public.goals` ← import-sgd-diario, import-sgd-meiodia (INSERT sem limpeza (ACUMULA)); import-sgd-diario, import-sgd-meiodia (recarga TOTAL)
- **Colunas entregues:** `date` (int64), `email` (string), `descmeta` (string), `valormeta` (double), `meta_at` (double), `meta_folha` (double), `meta_fiscont` (double)

SQL nativo:

```sql
select cal.date::date, 
       replace(goal.email,' ','') as email,
       goal.descmeta,
       goal.valormeta,
       goal.meta_at,
       goal.meta_folha,
       goal.meta_fiscont
from public.goals as goal
join public.calendar as cal
  on to_DATE(left(cast(cal.date as TEXT), 7), 'yyyy-mm') between to_DATE(goal.compini, 'yyyy-mm') and to_DATE(goal.compfim, 'yyyy-mm')
 where length(goal.compini) <= 7

union all

select cal.date::date, 
       goal.email,
       goal.descmeta,
       goal.valormeta,
       goal.meta_at,
       goal.meta_folha,
       goal.meta_fiscont
from public.goals as goal
join public.calendar as cal
  on to_DATE(cast(cal.date as TEXT), 'yyyy-mm-dd') between to_DATE(goal.compini, 'yyyy-mm-dd') and to_DATE(goal.compfim, 'yyyy-mm-dd')
 where length(goal.compini) > 7
```
