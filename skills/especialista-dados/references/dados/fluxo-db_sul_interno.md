# Fluxo `DB_SUL_INTERNO`

> Última atualização: 2026-09-30 · Fonte: `DB_SUL_INTERNO.json` (Dataflow Power BI, modificado em 2025-10-21, cultura en-US) · **Gerado automaticamente** por `scripts/mapear_fluxos.py`.

| Entidade | Carrega | Origem | Base | Tabelas de origem | Colunas | Último refresh (UTC) |
|---|---|---|---|---|---|---|
| `dados_teams_sul` | sim | Postgres | DB_SGD | `suporte.dados_teams_sul` | 17 | 2026-09-29T15:32:33 |

## `dados_teams_sul`

- **Origem:** Postgres · base `DB_SGD`
- `suporte.dados_teams_sul` ← excel.main_teams_sul (UPSERT (ON CONFLICT DO UPDATE))
- **Colunas entregues:** `auxiliar` (string), `data` (int64), `time` (time), `equipe_teams` (string), `canal_teams` (string), `email_ajuda` (string), `email_lider` (string), `email_lider_respondeu` (string), `assunto` (string), `descricao` (string), `link_conversa` (string), `quem_pediu_ajuda` (string), `quem_respondeu` (string), `adaptacao_apoio` (string), `email_lider_adapt` (string), `tempo_reacao` (string), `tempo_reacao_novo` (string)

SQL nativo:

```sql
SELECT auxiliar, 
           data::date,
           data::time,
           equipe_teams, 
           canal_teams, 
           email_ajuda, 
           email_lider, 
           email_lider_respondeu, 
           assunto, descricao, 
           link_conversa, 
           quem_pediu_ajuda, 
           quem_respondeu, 
           adaptacao_apoio, 
           email_lider_adapt, 
           tempo_reacao,
           tempo_reacao_novo
    FROM suporte.dados_teams_sul
```
