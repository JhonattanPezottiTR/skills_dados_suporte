# Fluxo `DB_LOGMEIN`

> Última atualização: 2026-09-30 · Fonte: `DB_LOGMEIN.json` (Dataflow Power BI, modificado em 2026-02-11, cultura en-US) · **Gerado automaticamente** por `scripts/mapear_fluxos.py`.

| Entidade | Carrega | Origem | Base | Tabelas de origem | Colunas | Último refresh (UTC) |
|---|---|---|---|---|---|---|
| `logmein_sessoes` | sim | Postgres | DB_SGD | `public.sgd_alocation_historic`, `public.sgd_users` | 24 | 2026-09-29T08:34:02 |

## `logmein_sessoes`

- **Origem:** Postgres · base `DB_SGD`
- `public.sgd_alocation_historic` ← import-sgd-diario (substitui janela de 60 dia(s))
- `public.sgd_users` ← import-sgd-diario (recarga TOTAL)
- **Colunas entregues:** `data` (int64), `hora` (time), `session_id` (string), `session_type` (string), `status` (string), `client` (string), `tracking_id` (string), `incident_tools_used` (string), `resolved_unresolved` (string), `calling_card` (string), `connecting_time_seg` (int64), `waiting_time_seg` (int64), `total_time_seg` (int64), `active_time_seg` (int64), `work_time_seg` (int64), `hold_time_seg` (int64), `time_in_transfer_seg` (int64), `rebooting_time_seg` (int64), `reconnecting_time_seg` (int64), `email` (string), `i_alocation` (int64), `i_user` (int64), `supervisor` (string), `gerente` (string)

SQL nativo:

```sql
WITH alocation_data AS (  
    SELECT   
        lower(u.email) as email,  
        h.date::date as date,  
        h.i_alocation, 
        h.i_user,
        ROW_NUMBER() OVER (  
            PARTITION BY lower(u.email), h.date::date   
            ORDER BY h.date DESC, h.i_alocation DESC  
        ) as rn ,
        hist.superv, 
        hist.manager
    FROM public.sgd_alocation_historic h  
    INNER JOIN public.sgd_users u ON h.i_user = u.i_user AND u.i_resale <> 1 and u.type_resale = 'Filiais'
    inner join sgd_user_manager_historic as hist ON hist.i_user = h.i_user and hist.date::date = h.date::date
        
)  


SELECT   
    start_time::date as data,
        start_time::time as hora,
        technician_id, 
        session_id, 
        session_type, 
        status, 
        name as Client, 
        tracking_id, 
        incident_tools_used,
        resolved_unresolved, 
        calling_card,  
        (CASE   
            WHEN connecting_time IS NULL OR connecting_time = '' THEN 0  
            ELSE EXTRACT(EPOCH FROM connecting_time::interval)  
        END)::int AS connecting_time_seg, 
        (CASE   
            WHEN waiting_time IS NULL OR waiting_time = '' THEN 0  
            ELSE EXTRACT(EPOCH FROM waiting_time::interval)  
        END)::int AS waiting_time_seg,
        (CASE   
            WHEN total_time IS NULL OR total_time = '' THEN 0  
            ELSE EXTRACT(EPOCH FROM total_time::interval)  
        END)::int AS total_time_seg,
        (CASE   
            WHEN active_time IS NULL OR active_time = '' THEN 0  
            ELSE EXTRACT(EPOCH FROM active_time::interval)  
        END)::int AS active_time_seg,
        (CASE   
            WHEN work_time IS NULL OR work_time = '' THEN 0  
            ELSE EXTRACT(EPOCH FROM work_time::interval)  
        END)::int AS work_time_seg,
        (CASE   
            WHEN hold_time IS NULL OR hold_time = '' THEN 0  
            ELSE EXTRACT(EPOCH FROM hold_time::interval)  
        END)::int AS hold_time_seg,
        (CASE   
            WHEN time_in_transfer IS NULL OR time_in_transfer = '' THEN 0  
            ELSE EXTRACT(EPOCH FROM time_in_transfer::interval)  
        END)::int AS time_in_transfer_seg,
        (CASE   
            WHEN rebooting_time IS NULL OR rebooting_time = '' THEN 0  
            ELSE EXTRACT(EPOCH FROM rebooting_time::interval)  
        END)::int AS rebooting_time_seg,
        (CASE   
            WHEN reconnecting_time IS NULL OR reconnecting_time = '' THEN 0  
            ELSE EXTRACT(EPOCH FROM reconnecting_time::interval)  
        END)::int AS reconnecting_time_seg,
        platform, 
        lower(acessos.email) as email,  
    coalesce(ad.i_alocation,999) as i_alocation ,
    coalesce(ad.i_user,999) as i_user,
    ad.superv as supervisor, 
    (case when ad.manager like 'Marina%' then 'Marina Ferrari'
          when ad.manager like 'Eloiza%' then 'Eloiza Kulckamp Alberton'
          when ad.manager like 'Thiago%' then 'Thiago Candelaria Birck'
          when ad.manager like 'Everton%' then 'Everton Batisti'
         else ad.manager 
    END )as gerente
FROM logmein.acessos   
inner JOIN alocation_data ad   
    ON lower(acessos.email) = ad.email   
    AND acessos.start_time::date = ad.date  
    AND ad.rn = 1  
    AND coalesce(ad.i_user,999) <> 999 AND coalesce(ad.manager,'')<>''
    AND coalesce(lower(ad.manager),'') ~* '^(marina|eloiza|thiago|everton)'
ORDER BY session_id ASC
```
