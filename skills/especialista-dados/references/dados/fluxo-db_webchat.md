# Fluxo `DB_WEBCHAT`

> Última atualização: 2026-09-30 · Fonte: `DB_WEBCHAT.json` (Dataflow Power BI, modificado em 2026-09-23, cultura en-US) · **Gerado automaticamente** por `scripts/mapear_fluxos.py`.

| Entidade | Carrega | Origem | Base | Tabelas de origem | Colunas | Último refresh (UTC) |
|---|---|---|---|---|---|---|
| `webchat_first_answer` | sim | Postgres | DB_WEBCHAT | `public.protocols`, `public.protocols_sequence_message` | 8 | 2026-09-29T08:33:04 |
| `webchat_historic` | sim | Postgres | DB_WEBCHAT | `public.protocols`, `public.protocols_history`, `public.protocols_ia` | 17 | 2026-09-29T08:38:05 |
| `webchat_historic_status` | sim | Postgres | DB_WEBCHAT | `public.users`, `public.users_historicstatus` | 7 | 2026-09-29T08:39:06 |
| `webchat_protocols` | sim | Postgres | DB_WEBCHAT | `public.disregard_dissatisfaction`, `public.protocols`, `public.protocols_history`, `public.protocols_ia`, `public.sgd_alocation_historic`, `public.users` | 31 | 2026-09-29T08:41:36 |
| `webchat_protocols_ia` | sim | Postgres | DB_WEBCHAT | `public.protocols_ia` | 8 | 2026-09-29T08:42:07 |
| `webchat_queues` | sim | Postgres | DB_WEBCHAT | `public.protocols`, `public.tenant_id` | 5 | 2026-09-29T08:42:37 |
| `webchat_users` | sim | Postgres | DB_WEBCHAT | `public.users` | 10 | 2026-09-29T08:43:08 |
| `sgd_clients_control_chat` | sim | Postgres | DB_WEBCHAT | `public.sgd_cli_liberados_chat` | 6 | 2026-09-29T08:43:39 |
| `webchat_historic_messages` | sim | Postgres | DB_WEBCHAT | `public.protocols`, `public.protocols_sequence_message` | 8 | 2026-09-29T09:02:40 |
| `webchat_historic_total` | sim | Postgres | DB_WEBCHAT | `public.protocols`, `public.protocols_sequence_message` | 8 | 2026-09-29T09:16:41 |
| `webchat_tenent` | sim | Postgres | DB_WEBCHAT | `public.tenant_id` | 3 | 2026-09-29T09:17:11 |
| `webchat_motivo_insatisf` | sim | Json.Document, Table.FromRows | — | — | 2 | 2026-09-29T09:17:42 |
| `webchat_protocols_faturamento` | sim | Postgres | DB_WEBCHAT | `public.protocols_all` | 4 | 2026-09-29T09:18:12 |
| `webchat_protocols_faturamento_detalhes` | sim | Postgres | DB_WEBCHAT | `public.vw_protocolos_all` | 20 | 2026-09-29T09:19:43 |

## `webchat_first_answer`

- **Origem:** Postgres · base `DB_WEBCHAT`
- `public.protocols` ← plug-queue-realtime
- `public.protocols_sequence_message` ← não mapeado no Maestro
- **Colunas entregues:** `createdatdate` (int64), `hora_resposta` (string), `protocol_number` (string), `agent` (int64), `primeira_resposta` (double), `initialqueue` (string), `queue_id` (string), `link` (string)

SQL nativo:

```sql
WITH Filtered AS (
    SELECT 
        protocol_number,
        _date,
        integrated_id,
        type,
        LEAD(_date) OVER (PARTITION BY protocol_number ORDER BY _date) AS next_date,
        LEAD(type) OVER (PARTITION BY protocol_number ORDER BY _date) AS next_type,
        LEAD(integrated_id) OVER (PARTITION BY protocol_number ORDER BY _date) AS next_integrated_id,
        details
    FROM 
        public.protocols_sequence_message
    WHERE 
        integrated_id != 0 AND (type = 'transfer-automatic' OR type = 'text' OR type ='transfer' or type = 'note' )
),
Differences AS (
    SELECT 
        protocol_number,
        _date,
        integrated_id,
        type,
        next_date,
        next_type,
        next_integrated_id,
        EXTRACT(EPOCH FROM (next_date::timestamptz - _date::timestamptz)) AS diff_seconds
    FROM 
        Filtered
    WHERE 
       (
           (type = 'transfer-automatic' AND (next_type = 'text'  or next_type = 'transfer') ) 
            OR
                (type = 'transfer' AND (next_type = 'text'))
            OR
                (type = 'note' AND (next_type = 'text') and details like 'Protocolo assumido%' )
                        )
        
)

SELECT distinct p.createdatdate::date,
        diff._date as hora_resposta,
        diff.protocol_number, 
        diff.next_integrated_id as agent,
        diff.diff_seconds as primeira_resposta,
        CASE 
            WHEN initialqueue = '' THEN 'Transferência telefonia'
            WHEN initialqueue = 'Escrita Fiscal - Simples Nacional  (SUDESTE)' THEN 'Escrita Fiscal - Simples Nacional (SUDESTE)'
            WHEN initialqueue = 'Simples Nacional - Sudeste' THEN 'Escrita Fiscal - Simples Nacional (SUDESTE)'
            WHEN initialqueue = 'Simples Nacional - Sul' THEN 'Escrita Fiscal - Simples Nacional (SUL)'
            ELSE initialqueue
        END AS initialqueue,
        (CASE   
            WHEN initialqueue = '' THEN 'Transferência telefonia'  
            WHEN initialqueue = 'Escrita Fiscal - Simples Nacional  (SUDESTE)' THEN 'Escrita Fiscal - Simples Nacional (SUDESTE)'  
            WHEN initialqueue = 'Simples Nacional - Sudeste' THEN 'Escrita Fiscal - Simples Nacional (SUDESTE)'  
            WHEN initialqueue = 'Simples Nacional - Sul' THEN 'Escrita Fiscal - Simples Nacional (SUL)'  
            ELSE initialqueue  
        END || ' - ' || tenant_id) AS queue_id,
        CONCAT('https://tr.plugsocial.com.br/#/app/chatbox/view/', p._id) AS link
        FROM Differences as diff inner join public.protocols as p on p.protocol_number = diff.protocol_number 
        where p.id_client not IN (40579,96797)
        order by 1,3,2
```

## `webchat_historic`

- **Origem:** Postgres · base `DB_WEBCHAT`
- `public.protocols` ← plug-queue-realtime
- `public.protocols_history` ← não mapeado no Maestro
- `public.protocols_ia` ← insights-realtime/insights-resumos (lib _insights)
- **Colunas entregues:** `_id` (string), `protocol_number` (string), `date_start` (date), `date_start_int` (int64), `hour_start` (time), `date_end` (date), `date_end_int` (int64), `hour_end` (time), `startinterval` (string), `seconds` (int64), `actor` (string), `i_userchat` (string), `queuegroup` (string), `transfer` (string), `queue_id` (string), `area_group` (string), `motivo_encerramento_ia` (string)

SQL nativo:

```sql
SELECT 
        h._id, 
        h.protocol_number, 
        h.startdate::date as date_start, 
        h.startdate::date as date_start_int,
        h.startdate::timetz as hour_start,
        h.stopdate::date as date_end, 
        h.stopdate::date as date_end_int, 
        h.stopdate::timetz as hour_end,
        h.startinterval, 
        h.seconds,         
        --TO_CHAR(seconds / 3600, 'FM00') || ':' || TO_CHAR((seconds % 3600) / 60, 'FM00') || ':' || TO_CHAR(seconds % 60, 'FM00') AS tempo,
        h.actor, 
        coalesce(h.i_userchat,'') as i_userchat, 
        CASE 
            WHEN h.queuegroup = '' THEN 'Transferência telefonia'
            WHEN h.queuegroup = 'Escrita Fiscal - Simples Nacional  (SUDESTE)' THEN 'Escrita Fiscal - Simples Nacional (SUDESTE)'
            WHEN h.queuegroup = 'Simples Nacional - Sudeste' THEN 'Escrita Fiscal - Simples Nacional (SUDESTE)'
            WHEN h.queuegroup = 'Simples Nacional - Sul' THEN 'Escrita Fiscal - Simples Nacional (SUL)'
            ELSE h.queuegroup
        END AS queuegroup,        
        h.transfer,
        (CASE   
        WHEN p.initialqueue = '' THEN 'Transferência telefonia'  
        WHEN p.initialqueue = 'Escrita Fiscal - Simples Nacional  (SUDESTE)' THEN 'Escrita Fiscal - Simples Nacional (SUDESTE)'  
        WHEN p.initialqueue = 'Simples Nacional - Sudeste' THEN 'Escrita Fiscal - Simples Nacional (SUDESTE)'  
        WHEN p.initialqueue = 'Simples Nacional - Sul' THEN 'Escrita Fiscal - Simples Nacional (SUL)'  
        ELSE p.initialqueue  
    END || ' - ' || tenant_id) AS queue_id,
    CASE
        WHEN tenant_id = '633cd75c16179f6a15cdace8'
            THEN (
                CASE
                    WHEN queuegroup LIKE 'Folha%'        THEN 'FOLHA'
                    WHEN queuegroup LIKE 'Contabilidade%'
                      OR queuegroup LIKE 'Escrita%'
                      OR queuegroup LIKE 'Fiscont%'
                      OR queuegroup LIKE 'Fiscal%'
                      OR queuegroup LIKE 'Reforma%'       THEN 'FISCONT'
                    ELSE 'AT'
                END
            )
        ELSE 'Revendas'
    END AS area_group,
    coalesce(ia.motivo_encerramento,'Não Identificado') as motivo_encerramento_ia
    FROM public.protocols_history as h inner join public.protocols as p 
                                                ON h.protocol_number = p.protocol_number  
                                                AND p.id_client not IN (40579,96797)
                                                AND p.protocol_number NOT IN ('20269241970611121538')
                                        left join public.protocols_ia as ia
                                                ON ia.protocolo_number = h.protocol_number
                                               --and p.tenant_id = '633cd75c16179f6a15cdace8'
    order by h.protocol_number, h.startdate asc
```

## `webchat_historic_status`

- **Origem:** Postgres · base `DB_WEBCHAT`
- `public.users` ← não mapeado no Maestro
- `public.users_historicstatus` ← não mapeado no Maestro
- **Colunas entregues:** `i_userchat` (string), `date` (int64), `start_status` (time), `end_status_time` (time), `seconds` (double), `status` (string), `dtime` (string)

SQL nativo:

```sql
WITH status_changes AS (
    SELECT
        st.i_userchat,
        st.historicstart,
        LEAD(st.historicstart, 1, st.historicstart) OVER (PARTITION BY st.i_userchat, DATE(st.historicstart) ORDER BY st.historicstart) AS end_status,
        st.status
    FROM public.users_historicstatus AS st inner join public.users as u on u.i_userchat = st.i_userchat AND u.tenant_id IN (
            '633cd75c16179f6a15cdace8',
            '67be22e302af10c13a9ee1e7',
            '68713eb6f56a72d281bee56d',
            '6924449e1321ea1e706ef1af',
            '6862a94d548a9612e239796d',
            '69a5f0d3506fb60b57017cce',
            '685949db370b587a0d2d3d4a',
            '68f8ed4c73a48fe9152e9b1a',
            '6979ee9130ac632769785c22',
            '6979eedc652a8864c0af7ebb',
            '6942a6b3530cb42cd2b70222'
       )
)
SELECT
    i_userchat,
    historicstart::date AS date,
    historicstart::time AS start_status,
    end_status::time AS end_status_time,
    EXTRACT(EPOCH FROM (end_status::time - historicstart::time)) AS seconds,
    status,
    CASE 
        WHEN EXTRACT(MINUTE FROM historicstart::time) < 30 THEN TO_CHAR(DATE_TRUNC('hour', historicstart::time), 'HH24:MI')
        ELSE TO_CHAR(DATE_TRUNC('hour', historicstart::time) + INTERVAL '30 minutes', 'HH24:MI')
    END AS dTime
FROM status_changes
ORDER BY date, i_userchat, start_status
```

## `webchat_protocols`

- **Origem:** Postgres · base `DB_WEBCHAT`
- `public.disregard_dissatisfaction` ← import-sgd-diario (recarga TOTAL)
- `public.protocols` ← plug-queue-realtime
- `public.protocols_history` ← não mapeado no Maestro
- `public.protocols_ia` ← insights-realtime/insights-resumos (lib _insights)
- `public.sgd_alocation_historic` ← import-sgd-diario/meiodia/observacoes/consultas (lib _import_sgd)
- `public.users` ← não mapeado no Maestro
- 🔒 **Credencial/infra embutida no SQL** (connection string de `dblink`) — mascarada aqui como `***`. Não copie esse padrão: use foreign server/user mapping ou uma view.
- **Colunas entregues:** `_id` (string), `protocol_number` (string), `i_userchat` (string), `initialqueue` (string), `created_date` (int64), `created_time` (time), `interval` (string), `rating` (string), `ratingdesc` (string), `id_motv_insatisf` (int64), `conclusion_motive` (string), `duration` (int64), `closed_date` (int64), `closed_time` (time), `id_client` (int64), `clinamecontact` (string), `cliuseronvio` (string), `link` (string), `i_meansofacess` (int64), `last_queue` (string), `disregarddissatisfaction` (int64), `i_ssc` (int64), `sgd_i_user` (string), `tenant_id` (string), `sgd_i_alocation` (int64), `queue_id` (string), `grupo_atendimento` (string), `area_group` (string), `attendancedate` (dateTime), `motivo_encerramento_ia` (string), `different_queue` (string)

SQL nativo:

```sql
SELECT 
    p._id,
    p.protocol_number,
    p.i_userchat,      
    CASE 
        WHEN p.initialqueue = '' THEN 'Transferência telefonia'
        WHEN p.initialqueue = 'Escrita Fiscal - Simples Nacional  (SUDESTE)' THEN 'Escrita Fiscal - Simples Nacional (SUDESTE)'
        WHEN p.initialqueue = 'Simples Nacional - Sudeste' THEN 'Escrita Fiscal - Simples Nacional (SUDESTE)'
        WHEN p.initialqueue = 'Simples Nacional - Sul' THEN 'Escrita Fiscal - Simples Nacional (SUL)'
        ELSE p.initialqueue
    END AS initialqueue,
    p.createdatdate::date as created_date,
    p.createdatdate::time as created_time,
    p."interval",
    CASE 
        WHEN p.rating = '0' THEN 'Insatisfeito'
        WHEN p.rating = '1' THEN 'Satisfeito'
        ELSE 'Não Opinou'
    END AS rating,
    p.ratingdesc, 
    p.id_motv_insatisf,
    coalesce(p.closure_motive,'')as conclusion_motive,
    p.duration, 
    p.closedate::date as closed_date,
    p.closedate::time as closed_time,
    p.id_client,    
    coalesce(p.cli_name_contact,'') as cliNameContact,
    coalesce(p.cli_user_onvio,'') as cliUserOnvio,
   CONCAT('https://tr.plugsocial.com.br/#/app/chatbox/view/', p._id) AS link,
    10 AS i_meansOfAcess,
    h.queuegroup AS last_queue,    
    CASE WHEN d.i_response IS NOT NULL THEN 1 ELSE 0 END AS disregardDissatisfaction,
    p.i_ssc,
    g.i_user_sgd as sgd_i_user, 
    p.tenant_id,
    coalesce(aloc.i_alocation,999) as sgd_i_alocation,
    (CASE   
        WHEN p.initialqueue = '' THEN 'Transferência telefonia'  
        WHEN p.initialqueue = 'Escrita Fiscal - Simples Nacional  (SUDESTE)' THEN 'Escrita Fiscal - Simples Nacional (SUDESTE)'  
        WHEN p.initialqueue = 'Simples Nacional - Sudeste' THEN 'Escrita Fiscal - Simples Nacional (SUDESTE)'  
        WHEN p.initialqueue = 'Simples Nacional - Sul' THEN 'Escrita Fiscal - Simples Nacional (SUL)'  
        ELSE p.initialqueue  
    END || ' - ' || p.tenant_id) AS queue_id,
    coalesce(p.grupo_atend,'Sem Grupo') AS grupo_atendimento,
    CASE
        WHEN p.tenant_id = '633cd75c16179f6a15cdace8'
            THEN (
                CASE
                    WHEN queuegroup LIKE 'Folha%'        THEN 'FOLHA'
                    WHEN queuegroup LIKE 'Contabilidade%'
                      OR queuegroup LIKE 'Escrita%'
                      OR queuegroup LIKE 'Fiscont%'
                      OR queuegroup LIKE 'Fiscal%'
                      OR queuegroup LIKE 'Reforma%'       THEN 'FISCONT'
                    ELSE 'AT'
                END
            )
        ELSE 'Revendas'
    END AS area_group,
    p.attendancedate,
    coalesce(ia.motivo_encerramento,'Não Identificado') as motivo_encerramento_ia
FROM 
    public.protocols p
                LEFT JOIN 
                    (
                        SELECT 
                            _id,
                            queuegroup,
                            ROW_NUMBER() OVER (PARTITION BY _id ORDER BY startdate DESC) AS row_num
                        FROM 
                            public.protocols_history
                    ) h ON p._id = h._id AND h.row_num = 1
                LEFT JOIN public.disregard_dissatisfaction AS d ON p.protocol_number =d.i_ssc_ss_chat AND d."type" = 'CHAT'    
                
                INNER JOIN 
                        public.users AS g ON g.i_userchat =  p.i_userchat
                    -- =========================================================================================
                    -- AJUSTE PRINCIPAL AQUI: Trocamos o JOIN direto por um JOIN em uma subquery que busca o maior i_usuarios
                    -- =========================================================================================
                    
                    LEFT JOIN (
                        SELECT 
                            date,
                            i_user, 
                            i_alocation
                        FROM dblink(
                            'host=*** dbname=DB_SGD user=*** password=***',
                            'SELECT date, i_user, i_alocation FROM public.sgd_alocation_historic'
                        ) AS t(
                            date DATE,
                            i_user INT, 
                            i_alocation INT
                        )
                    ) AS aloc ON g.i_user_sgd::int = aloc.i_user
                             AND p.createdatdate::date = aloc.date
                    
                    left join public.protocols_ia as ia
                                                ON ia.protocolo_number = p.protocol_number        
                   WHERE p.id_client not IN (40579,96797)
                    --where g.i_usuarios = 1272708
                    --where coalesce(aloc.i_alocation,0) = 0 and "historic_callsAgents"."dateTime_start"::date <= '2025-09-15'::date
                    ORDER BY  p.createdatdate::date asc, p.protocol_number
```

## `webchat_protocols_ia`

- **Origem:** Postgres · base `DB_WEBCHAT`
- `public.protocols_ia` ← insights-realtime/insights-resumos (lib _insights)
- **Colunas entregues:** `protocolo_number` (string), `resumo` (string), `problema_1` (string), `problema_2` (string), `frustracoes` (string), `dificuldades` (string), `analise_especifica_original` (string), `analise_especifica` (string)

SQL nativo:

```sql
SELECT  
        protocolo_number, 
        resumo, 
        problema_1, 
        problema_2, 
        frustacoes as frustracoes  , 
        dificuldades, 
                analise_especifica as analise_especifica_original,
        CASE
           WHEN analise_especifica LIKE '%tributaria%' THEN 'reforma_tributaria'
           WHEN analise_especifica LIKE '%erro_8%' THEN 'erro_8'
           ELSE ''
       END AS analise_especifica
    FROM public.protocols_ia
```

## `webchat_queues`

- **Origem:** Postgres · base `DB_WEBCHAT`
- `public.protocols` ← plug-queue-realtime
- `public.tenant_id` ← não mapeado no Maestro
- **Colunas entregues:** `name_queue` (string), `type_resale` (string), `resale` (string), `tenant_id` (string), `queue_id` (string)

SQL nativo:

```sql
SELECT DISTINCT  
    CASE   
        WHEN initialqueue = '' THEN 'Transferência telefonia'  
        WHEN initialqueue = 'Escrita Fiscal - Simples Nacional  (SUDESTE)' THEN 'Escrita Fiscal - Simples Nacional (SUDESTE)'  
        WHEN initialqueue = 'Simples Nacional - Sudeste' THEN 'Escrita Fiscal - Simples Nacional (SUDESTE)'  
        WHEN initialqueue = 'Simples Nacional - Sul' THEN 'Escrita Fiscal - Simples Nacional (SUL)'  
        ELSE initialqueue  
    END AS name_queue,
      
    /*CASE   
        WHEN upper(initialqueue) LIKE '%SUDESTE%' THEN 'SUDESTE'  
        WHEN upper(initialqueue) LIKE '%SUL%' THEN 'SUL'  
        WHEN upper(initialqueue) LIKE '%TEKPLAN%' THEN 'Tekplan'  
        WHEN upper(initialqueue) LIKE '%TOOL BUSINESS%' THEN 'TOOL BUSINESS'  
        WHEN upper(initialqueue) = '' THEN 'TELEFONIA'  
        WHEN tenant_id = '633cd75c16179f6a15cdace8' THEN 'GERAL'  
        ELSE tenant_desc  
    END AS resale,*/
      
    CASE   
        WHEN upper(initialqueue) LIKE '%TEKPLAN%' THEN 'Revendas'  
        WHEN upper(initialqueue) LIKE '%TOOL BUSINESS%' THEN 'Revendas'  
        WHEN tenant_id = '633cd75c16179f6a15cdace8' THEN 'Filiais'  
        ELSE 'Revendas'  
    END AS type_resale,
      
    CASE   
        WHEN upper(initialqueue) LIKE '%TEKPLAN%' THEN 'Tekplan'  
        WHEN upper(initialqueue) LIKE '%TOOL BUSINESS%' THEN 'TOOL BUSINESS'  
        WHEN tenant_id = '633cd75c16179f6a15cdace8' THEN (CASE   
                                                            WHEN upper(initialqueue) LIKE '%SUDESTE%' THEN 'SUDESTE'  
                                                            WHEN upper(initialqueue) LIKE '%SUL%' THEN 'SUL' 
                                                            ELSE 'GERAL' END)
        ELSE tenant_desc  
    END AS resale,
      
    CASE   
        WHEN upper(initialqueue) LIKE '%TEKPLAN%' THEN '6862a94d548a9612e239796d'  
        WHEN upper(initialqueue) LIKE '%TOOL BUSINESS%' THEN '67be22e302af10c13a9ee1e7'  
        ELSE tenant_id  
    END AS tenant_id,
      
    (CASE   
        WHEN initialqueue = '' THEN 'Transferência telefonia'  
        WHEN initialqueue = 'Escrita Fiscal - Simples Nacional  (SUDESTE)' THEN 'Escrita Fiscal - Simples Nacional (SUDESTE)'  
        WHEN initialqueue = 'Simples Nacional - Sudeste' THEN 'Escrita Fiscal - Simples Nacional (SUDESTE)'  
        WHEN initialqueue = 'Simples Nacional - Sul' THEN 'Escrita Fiscal - Simples Nacional (SUL)'  
        ELSE initialqueue  
    END || ' - ' || tenant_id) AS queue_id
  
FROM   
    (SELECT DISTINCT p.initialqueue, t.tenant_desc, p.tenant_id   
     FROM public.protocols AS p   
     INNER JOIN public.tenant_id AS t ON p.tenant_id = t.tenant_id  
     WHERE p.i_userchat <> '0') AS unique_initialqueues
```

## `webchat_users`

- **Origem:** Postgres · base `DB_WEBCHAT`
- `public.users` ← não mapeado no Maestro
- **Colunas entregues:** `i_userchat` (string), `email` (string), `username` (string), `name` (string), `status` (string), `role` (string), `createddate` (dateTime), `updatedate` (dateTime), `i_user_sgd` (int64), `tenant_id` (string)

SQL nativo:

```sql
WITH RankedUsers AS (
    SELECT 
        i_userchat,
        email,
        username,
        name,
        status,
        role,
        createddate,
        updatedate,
        replace(i_user_sgd, '\t', '') as i_user_sgd,
        tenant_id,
        ROW_NUMBER() OVER (PARTITION BY i_userchat ORDER BY createddate DESC) AS rn
    FROM 
        public.users
    WHERE 
        i_userchat <> '6792760db822492aae7de8ad' 
        AND i_user_sgd <> '0'
        AND email LIKE '%@%'
        -- AND tenant_id = '633cd75c16179f6a15cdace8'
        --AND i_user_sgd = '1061984'
)
SELECT 
    i_userchat,
    lower(email) as email,
    username,
    name,
    status,
    role,
    createddate,
    updatedate,
    i_user_sgd,
    tenant_id
FROM 
    RankedUsers
WHERE 
    rn = 1
```

## `sgd_clients_control_chat`

- **Origem:** Postgres · base `DB_WEBCHAT`
- `public.sgd_cli_liberados_chat` ← não mapeado no Maestro
- **Colunas entregues:** `i_cliente` (int64), `liberado_chat_gpt` (int64), `liberado_tria_plug` (int64), `liberado_chat_humano` (int64), `data_hora` (dateTime), `date_int` (int64)

SQL nativo:

```sql
SELECT i_cliente,
        liberado_chat_gpt, 
        liberado_tria_plug, 
        liberado_chat_humano, 
        data_hora
FROM public.sgd_cli_liberados_chat
```

## `webchat_historic_messages`

- **Origem:** Postgres · base `DB_WEBCHAT`
- `public.protocols` ← plug-queue-realtime
- `public.protocols_sequence_message` ← não mapeado no Maestro
- **Colunas entregues:** `protocol_number` (string), `_date` (int64), `integrated_id` (int64), `seconds` (int64), `actor` (string), `initialqueue` (string), `queue_id` (string), `grupo_atendimento` (string)

SQL nativo:

```sql
WITH filtered_data AS (
    SELECT
        a.protocol_number,
        a._date,
        a.integrated_id,
        a.seconds,
        a.type,
        a.details,
        a.actor,
        LEAD(a.actor, 1) OVER (PARTITION BY a.protocol_number ORDER BY a._date) AS next_actor,
        LEAD(a.type, 1) OVER (PARTITION BY a.protocol_number ORDER BY a._date) AS next_type,
        CASE 
            WHEN b.initialqueue = '' THEN 'Transferência telefonia'
            WHEN b.initialqueue = 'Escrita Fiscal - Simples Nacional  (SUDESTE)' THEN 'Escrita Fiscal - Simples Nacional (SUDESTE)'
            WHEN b.initialqueue = 'Simples Nacional - Sudeste' THEN 'Escrita Fiscal - Simples Nacional (SUDESTE)'
            WHEN b.initialqueue = 'Simples Nacional - Sul' THEN 'Escrita Fiscal - Simples Nacional (SUL)'
            ELSE b.initialqueue
        END AS initialqueue,
        (CASE   
            WHEN initialqueue = '' THEN 'Transferência telefonia'  
            WHEN initialqueue = 'Escrita Fiscal - Simples Nacional  (SUDESTE)' THEN 'Escrita Fiscal - Simples Nacional (SUDESTE)'  
            WHEN initialqueue = 'Simples Nacional - Sudeste' THEN 'Escrita Fiscal - Simples Nacional (SUDESTE)'  
            WHEN initialqueue = 'Simples Nacional - Sul' THEN 'Escrita Fiscal - Simples Nacional (SUL)'  
            ELSE initialqueue  
        END || ' - ' || tenant_id) AS queue_id,
        b.grupo_atend as grupo_atendimento
    FROM
        public.protocols_sequence_message as a
    INNER JOIN public.protocols as b
        ON b.protocol_number = a.protocol_number
        --AND b.tenant_id = '633cd75c16179f6a15cdace8'
        AND b.i_userchat <> '0'
),
sequence_check AS (
    SELECT
        *,
        CASE 
            WHEN actor = 'bot' AND type = 'custom' AND next_actor = 'contact' AND next_type = 'text' THEN 1
            ELSE 0
        END AS sequence_flag
    FROM filtered_data
),
marked_rows AS (
    SELECT
        *,
        SUM(sequence_flag) OVER (PARTITION BY protocol_number ORDER BY _date ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS cum_sequence_flag,
        MIN(CASE WHEN type = 'rating' THEN _date END) OVER (PARTITION BY protocol_number) AS min_rating_date
    FROM sequence_check
),
filtered_marked_rows AS (
    SELECT
        *,
        ROW_NUMBER() OVER (PARTITION BY protocol_number ORDER BY _date) AS rn
    FROM marked_rows
    WHERE
        cum_sequence_flag > 0
        AND (_date < min_rating_date OR min_rating_date IS NULL)
)
SELECT
    protocol_number,
    _date,
    integrated_id,
    seconds,
    (CASE
        WHEN type = 'note' AND details LIKE '%colocado em ocioso%' THEN 'contact'
        WHEN type = 'note' AND details LIKE '%removido de ocioso%' THEN 'ocioso'
        WHEN type = 'text' AND
             LAG(details) OVER (PARTITION BY protocol_number ORDER BY _date) LIKE '%colocado em ocioso%' AND
             integrated_id IS NOT NULL THEN 'ocioso'
        WHEN type = 'note' AND
             LAG(details) OVER (PARTITION BY protocol_number ORDER BY _date) LIKE '%colocado em ocioso%' AND
             LAG(_date) OVER (PARTITION BY protocol_number ORDER BY _date) <> _date AND
             integrated_id IS NOT NULL THEN 'ocioso'
        ELSE actor
    END) AS actor,
    initialqueue,
    queue_id,
    grupo_atendimento
    
FROM
    filtered_marked_rows
WHERE
    rn > 2  -- Exclude the first two rows of each protocol after all filters
    --AND protocol_number = '20252127310077651454'
ORDER BY
    protocol_number,
    _date
```

## `webchat_historic_total`

- **Origem:** Postgres · base `DB_WEBCHAT`
- `public.protocols` ← plug-queue-realtime
- `public.protocols_sequence_message` ← não mapeado no Maestro
- **Colunas entregues:** `protocol_number` (string), `integrated_id` (int64), `actor` (string), `total_seconds` (int64), `initialqueue` (string), `createdatdate` (int64), `queue_id` (string), `grupo_atendimento` (string)

SQL nativo:

```sql
WITH filtered_data AS (
    SELECT
        a.protocol_number,
        a._date,
        a.integrated_id,
        a.seconds,
        a.type,
        a.details,
        a.actor,
        LEAD(a.actor, 1) OVER (PARTITION BY a.protocol_number ORDER BY a._date) AS next_actor,
        LEAD(a.type, 1) OVER (PARTITION BY a.protocol_number ORDER BY a._date) AS next_type,
        CASE 
            WHEN b.initialqueue = '' THEN 'Transferência telefonia'
            WHEN b.initialqueue = 'Escrita Fiscal - Simples Nacional  (SUDESTE)' THEN 'Escrita Fiscal - Simples Nacional (SUDESTE)'
            WHEN b.initialqueue = 'Simples Nacional - Sudeste' THEN 'Escrita Fiscal - Simples Nacional (SUDESTE)'
            WHEN b.initialqueue = 'Simples Nacional - Sul' THEN 'Escrita Fiscal - Simples Nacional (SUL)'
            ELSE b.initialqueue
        END AS initialqueue,
        b.createdatdate,
        (CASE   
            WHEN b.initialqueue = '' THEN 'Transferência telefonia'  
            WHEN b.initialqueue = 'Escrita Fiscal - Simples Nacional  (SUDESTE)' THEN 'Escrita Fiscal - Simples Nacional (SUDESTE)'  
            WHEN b.initialqueue = 'Simples Nacional - Sudeste' THEN 'Escrita Fiscal - Simples Nacional (SUDESTE)'  
            WHEN b.initialqueue = 'Simples Nacional - Sul' THEN 'Escrita Fiscal - Simples Nacional (SUL)'  
            ELSE b.initialqueue  
        END || ' - ' || b.tenant_id) AS queue_id,
        b.grupo_atend as grupo_atendimento
    FROM
        public.protocols_sequence_message as a
    INNER JOIN public.protocols as b
        ON b.protocol_number = a.protocol_number
        --AND b.tenant_id = '633cd75c16179f6a15cdace8'
        AND b.i_userchat <> '0'
        --AND a._date::date >='2026-03-01'
    --AND b.protocol_number =  '20240002136455308450'
),
sequence_check AS (
    SELECT
        *,
        CASE 
            WHEN actor = 'bot' AND type = 'custom' AND next_actor = 'contact' AND next_type = 'text' THEN 1
            ELSE 0
        END AS sequence_flag
    FROM filtered_data
),
marked_rows AS (
    SELECT
        *,
        SUM(sequence_flag) OVER (PARTITION BY protocol_number ORDER BY _date ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS cum_sequence_flag,
        MIN(CASE WHEN type = 'rating' THEN _date END) OVER (PARTITION BY protocol_number) AS min_rating_date
    FROM sequence_check
),
filtered_marked_rows AS (
    SELECT
        *,
        ROW_NUMBER() OVER (PARTITION BY protocol_number ORDER BY _date) AS rn
    FROM marked_rows
    WHERE
        cum_sequence_flag > 0
        AND (_date < min_rating_date OR min_rating_date IS NULL)
),
actor_adjustment AS (
    SELECT
        protocol_number,
        seconds,
        integrated_id,
        (CASE
            WHEN type = 'note' AND details LIKE '%colocado em ocioso%' THEN 'contact'
            WHEN type = 'note' AND details LIKE '%removido de ocioso%' THEN 'ocioso'
            WHEN type ='transfer-state-automatic' AND details LIKE '%para Ocioso%' THEN 'contact'
            WHEN type = 'transfer-state-automatic' AND details LIKE '%de Ocioso%' THEN 'ocioso'
            WHEN type = 'text' AND
                 LAG(details) OVER (PARTITION BY protocol_number ORDER BY _date) LIKE '%colocado em ocioso%' AND
                 integrated_id IS NOT NULL THEN 'contact'
            WHEN type = 'note' AND
                 LAG(details) OVER (PARTITION BY protocol_number ORDER BY _date) LIKE '%colocado em ocioso%' AND
                 LAG(_date) OVER (PARTITION BY protocol_number ORDER BY _date) <> _date AND
                 integrated_id IS NOT NULL THEN 'contact'
            ELSE actor
        END) AS actor,
        initialqueue,
        createdatdate,
        queue_id,
        grupo_atendimento,
        rn
        
    FROM
        filtered_marked_rows
    WHERE
        rn > 2
)
SELECT
    protocol_number,
    /*(case when actor = 'contact' or actor = 'ocioso' then 0 else integrated_id end) as  integrated_id,
    (case when integrated_id <> 0 and actor <> 'ocioso' then 'suporte' else actor end ) as actor,*/
    (case     when actor = 'contact' and  integrated_id <> 0 then integrated_id
            when actor = 'contact' or actor = 'ocioso' then 0 else integrated_id end) as  integrated_id,
    (case when integrated_id = 0 and actor = 'suporte' then 'ocioso'
          when integrated_id <> 0 and actor <> 'ocioso' then 'suporte' else actor end ) as actor ,
    SUM(seconds) AS total_seconds,
    initialqueue,
    createdatdate,    
    queue_id,
    grupo_atendimento
FROM
    actor_adjustment  
    where actor <>''
    --actor_adjustment  where actor ='ocioso'
    
GROUP BY
    protocol_number,
    /*(case when actor = 'contact' or actor = 'ocioso' then 0 else integrated_id end),
    (case when integrated_id <> 0 and actor <> 'ocioso' then 'suporte' else actor end ),*/
    (case when actor = 'contact' and  integrated_id <> 0 then integrated_id
          when actor = 'contact' or actor = 'ocioso' then 0 else integrated_id end),
    (case when integrated_id = 0 and actor = 'suporte' then 'ocioso'
          when integrated_id <> 0 and actor <> 'ocioso' then 'suporte' else actor end ),
    initialqueue,
    createdatdate,    
    queue_id,
    grupo_atendimento
ORDER BY
    protocol_number
```

## `webchat_tenent`

- **Origem:** Postgres · base `DB_WEBCHAT`
- `public.tenant_id` ← não mapeado no Maestro
- **Colunas entregues:** `tenant_id` (string), `tenant_desc` (string), `type_resales` (string)

SQL nativo:

```sql
SELECT 
            tenant_id, 
            tenant_desc, 
            (case 
                when tenant_id = '633cd75c16179f6a15cdace8' THEN 'Filiais' --Suporte
                when tenant_id = '6a60bd21f29f6d8e02bf06a1' THEN 'Filiais' --Líderes
                else 'Revendas' -- Revendas 
              END ) as type_resales
    FROM public.tenant_id where token_tenant is not null
```

## `webchat_motivo_insatisf`

- **Origem:** Json.Document, Table.FromRows
- **Colunas entregues:** `cod_motiv_insatisf` (int64), `motivo_insatisfação` (string)

## `webchat_protocols_faturamento`

- **Origem:** Postgres · base `DB_WEBCHAT`
- `public.protocols_all` ← não mapeado no Maestro
- **Colunas entregues:** `total protocol` (int64), `origem` (string), `createdatdate_int` (int64), `tenant_id` (string)

SQL nativo:

```sql
SELECT   
    COUNT(DISTINCT protocol_number) as "total protocol",   
    origem,   
    createdatdate::date ,
   tenant_id 
FROM public.protocols_all  
WHERE createdatdate::date >= '2026-01-01' 
GROUP BY   
    origem, 
    createdatdate::date  , tenant_id
ORDER BY createdatdate::date
```

## `webchat_protocols_faturamento_detalhes`

- **Origem:** Postgres · base `DB_WEBCHAT`
- `public.vw_protocolos_all` ← não mapeado no Maestro
- **Colunas entregues:** `_id` (string), `protocol_number` (string), `i_userchat` (string), `origem` (string), `origem_dados` (string), `createdatdate_int` (int64), `closedate_int` (int64), `id_client` (int64), `tenant_id` (string), `rating` (string), `rating_desc` (string), `id_motv_insatisf` (string), `i_ssc` (int64), `interval` (string), `tag` (string), `modulo` (string), `i_system_sgd` (int64), `i_module_sgd` (int64), `sistema_sgd` (string), `modulo_sgd` (string)

SQL nativo:

```sql
SELECT * FROM public.vw_protocolos_all where id_client not IN (40579,96797)
```
