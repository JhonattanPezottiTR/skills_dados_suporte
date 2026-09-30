# Fluxo `DB_GENESYS_TRANSCRIPTIONS`

> Última atualização: 2026-09-30 · Fonte: `DB_GENESYS_TRANSCRIPTIONS.json` (Dataflow Power BI, modificado em 2025-05-05, cultura pt-BR) · **Gerado automaticamente** por `scripts/mapear_fluxos.py`.

| Entidade | Carrega | Origem | Base | Tabelas de origem | Colunas | Último refresh (UTC) |
|---|---|---|---|---|---|---|
| `genesys_calls_transcription` | sim | Postgres | DB_GENESYS | `public.historic_calls_transcript` | 2 | 2026-09-29T15:36:38 |

## `genesys_calls_transcription`

- **Origem:** Postgres · base `DB_GENESYS`
- `public.historic_calls_transcript` ← genesys-import; genesys-transcricao-realtime
- **Colunas entregues:** `conversation_id` (string), `transcript` (string)

SQL nativo:

```sql
SELECT 
conversation_id,
transcript
    
FROM public.historic_calls_transcript
```
