# Fluxo `DB_GENESYS`

> Última atualização: 2026-09-30 · Fonte: `DB_GENESYS.json` (Dataflow Power BI, modificado em 2026-09-28, cultura en-US) · **Gerado automaticamente** por `scripts/mapear_fluxos.py`.

| Entidade | Carrega | Origem | Base | Tabelas de origem | Colunas | Último refresh (UTC) |
|---|---|---|---|---|---|---|
| `genesys_agentAvailable` | sim | Postgres | DB_GENESYS | `public.agentavailable`, `public.sgd_alocations` | 19 | 2026-09-29T08:13:34 |
| `genesys_areaSkillQueue` | sim | Postgres | DB_GENESYS | `public.queue`, `public.skills` | 6 | 2026-09-29T08:14:05 |
| `genesys_callsAgentsHalfHour` | sim | Postgres | DB_GENESYS | `public.calls_agents_halfhour`, `public.sgd_alocations` | 49 | 2026-09-29T08:19:05 |
| `genesys_historicAgentStatus` | sim | Postgres | DB_GENESYS | `public.historicagentstatus`, `public.sgd_alocations` | 13 | 2026-09-29T08:23:36 |
| `genesys_historicCallsAbandoned` | sim | Postgres | DB_GENESYS | `public.historic_callsabandoned`, `public.queue`, `public.skills`, `temp.sgd_clientcontact` | 14 | 2026-09-29T08:25:07 |
| `genesys_historicCallsAgents` | sim | Postgres | DB_GENESYS | `public.callswithclient`, `public.historic_calls_ia_new`, `public.historic_callsagents`, `public.queue`, `public.sgd_alocations`, `public.skills` | 61 | 2026-09-29T08:54:08 |
| `genesys_historicCalls_ia` | sim | Postgres | DB_GENESYS | `public.historic_calls_ia`, `public.historic_calls_ia_new` | 9 | 2026-09-29T08:55:09 |
| `genesys_historicCallsTransfer` | sim | Postgres | DB_GENESYS | `public.historic_callstranfers`, `public.users_genesys` | 13 | 2026-09-29T08:55:40 |
| `genesys_presenceDefinitions` | sim | Postgres | DB_GENESYS | `public.presencedefinitions` | 4 | 2026-09-29T08:56:10 |
| `genesys_qualificationsSkills` | sim | Postgres | DB_GENESYS | `public.historic_qualifications`, `public.queue`, `public.skills` | 48 | 2026-09-29T08:57:11 |
| `genesys_queue` | sim | Postgres | DB_GENESYS | `public.queue` | 5 | 2026-09-29T08:57:41 |
| `genesys_queuePerformance_HalfHour` | sim | Postgres | DB_GENESYS | `public.queue_performance` | 38 | 2026-09-29T08:58:12 |
| `genesys_skill` | sim | Postgres | DB_GENESYS | `public.skills` | 4 | 2026-09-29T08:58:42 |
| `dTime` | sim | Json.Document, Table.FromRows | — | — | 1 | 2026-09-29T08:59:13 |
| `genesys_users` | sim | Postgres | DB_GENESYS | `public.users_genesys` | 10 | 2026-09-29T08:59:43 |
| `genesys_survey` | sim | Postgres | DB_GENESYS | `public.historic_callsagents`, `public.survey`, `public.survey_question`, `public.survey_question_option` | 7 | 2026-09-29T09:00:44 |

## `genesys_agentAvailable`

- **Origem:** Postgres · base `DB_GENESYS`
- `public.agentavailable` ← genesys-import
- `public.sgd_alocations` ← import-sgd-diario (recarga TOTAL)
- **Colunas entregues:** `user_id` (string), `ddate` (int64), `dtime` (string), `interacting` (double), `available` (double), `busy` (double), `on_queue` (double), `idle` (double), `offline` (double), `away` (double), `break` (double), `meal` (double), `meeting` (double), `training` (double), `not_responding` (double), `sgd_i_user` (int64), `sgd_i_alocation` (int64), `dDateTime` (dateTime), `conectado` (int64)

SQL nativo:

```sql
SELECT  a.* ,
        coalesce(g.i_user,0) as sgd_i_user, 
        coalesce(g.i_alocation,999) as sgd_i_alocation
    
    FROM public."agentAvailable" as a
        LEFT JOIN  public.sgd_alocations AS g ON g.id_user_genesys = a.user_id
                            and g.ddate = a.ddate


ORDER BY  a.ddate
```

## `genesys_areaSkillQueue`

- **Origem:** Postgres · base `DB_GENESYS`
- `public.queue` ← genesys-import
- `public.skills` ← genesys-import
- **Colunas entregues:** `id_skill` (string), `id_queue` (string), `name_skill` (string), `name_queue` (string), `area` (string), `regional` (string)

SQL nativo:

```sql
SELECT s.id_skill, q.id_queue,substring(s.name_skill,13) as name_skill,
substring(q.name_queue,13) as name_queue, s.area, s.regional
    FROM public.SKILLS as s full outer join public.queue as q 
    on substring(s.name_skill,1,24) = substring(q.name_queue,1,24)
```

## `genesys_callsAgentsHalfHour`

- **Origem:** Postgres · base `DB_GENESYS`
- `public.calls_agents_halfhour` ← genesys-import
- `public.sgd_alocations` ← import-sgd-diario (recarga TOTAL)
- **Colunas entregues:** `date_interval` (int64), `id_user` (string), `time_interval` (string), `_nAnswered` (double), `_tAnswered` (double), `_tAnsweredMax` (double), `_tAnsweredMin` (double), `_nHandle` (double), `_tHandle` (double), `_tHandleMax` (double), `_tHandleMin` (double), `_nTalkComplete` (double), `_tTalkComplete` (double), `_tTalkCompleteMax` (double), `_tTalkCompleteMin` (double), `_tHeldComplete` (double), `_nAcw` (double), `_tAcw` (double), `_tAcwMax` (double), `_tAcwMin` (double), `_nDialing` (double), `_tDialing` (double), `_tDialingMax` (double), `_tDialingMin` (double), `_nContacting` (double), `_tContacting` (double), `_tContactingMax` (double), `_tContactingMin` (double), `_nTransferred` (double), `_nOutbound` (double), `_nNotResponding` (double), `_tNotResponding` (double), `_tNotRespondingMax` (double), `_tNotRespondingMin` (double), `_nAlert` (double), `_tAlert` (double), `_tAlertMax` (double), `_tAlertMin` (double), `_nMonitoring` (double), `_tMonitoring` (double), `_tMonitoringMax` (double), `_tMonitoringMin` (double), `_nBlindTransferred` (double), `_nConsultTransferred` (double), `direction` (string), `_queue` (string), `sgd_i_user` (int64), `sgd_i_alocation` (int64), `dDateTime` (dateTime)

SQL nativo:

```sql
SELECT 
      
    c.*, 
    coalesce(g.i_user,0) as sgd_i_user, 
    coalesce(g.i_alocation,999) as sgd_i_alocation
    
FROM 
    public."calls_agents_halfHour" AS c 
LEFT JOIN 
    public.sgd_alocations AS g ON g.id_user_genesys = c.id_user
                              and g.ddate = c.date_interval


ORDER BY date_interval::date ASC
```

## `genesys_historicAgentStatus`

- **Origem:** Postgres · base `DB_GENESYS`
- `public.historicagentstatus` ← genesys-import
- `public.sgd_alocations` ← import-sgd-diario (recarga TOTAL)
- **Colunas entregues:** `dDateStart` (int64), `dTime` (string), `id_user` (string), `id_presenceDef` (string), `nameSystemPresence` (string), `nameSecondPresence` (string), `dTimeStart` (time), `dTimeEnd` (time), `duration` (int64), `namesecondpresence_pt` (string), `sgd_i_user` (int64), `sgd_i_alocation` (int64), `dDateTime` (dateTime)

SQL nativo:

```sql
SELECT ag.*,
         
        (CASE "nameSecondPresence"
        WHEN 'Available' THEN 'Disponível'
        WHEN 'Busy' THEN 'Ocupado'
        WHEN 'Chat' THEN 'Bate Papo'
        WHEN 'Projects' THEN 'Projeto'
        WHEN 'Admin' THEN 'Apoio'
        WHEN 'Call Back / Follow Up' THEN 'Chamada Externa'
        WHEN 'Coaching' THEN 'Coaching'
        WHEN 'Email' THEN 'Email'
        WHEN 'System Issues' THEN 'Testes / Análises'
        WHEN 'WhatsApp' THEN 'WhatsApp'
        WHEN 'MyAcct' THEN 'MyAcct'
        WHEN 'Remote Access' THEN 'Remote Access'
        WHEN 'Away' THEN 'Ausente'
        WHEN 'Break' THEN 'Intervalo'
        WHEN 'Meal' THEN 'Refeição'
        WHEN 'Meeting' THEN 'Reunião'
        WHEN 'Training' THEN 'Treinamento'
        WHEN 'On Queue' THEN 'Atendendo'
        WHEN 'Offline' THEN 'Desconectado'
        WHEN 'Idle' THEN 'Ocioso'
        ELSE "nameSecondPresence"
        END) AS nameSecondPresence_pt,
        coalesce(g.i_user,0) as sgd_i_user, 
        coalesce(g.i_alocation,999) as sgd_i_alocation
        
      
  FROM public."HistoricAgentStatus" as ag
                                    LEFT JOIN 
                                                public.sgd_alocations AS g ON g.id_user_genesys = ag.id_user
                                              and g.ddate::date = ag."dDateStart"::date
ORDER BY  ag."dDateStart"::date
```

## `genesys_historicCallsAbandoned`

- **Origem:** Postgres · base `DB_GENESYS`
- `public.historic_callsabandoned` ← genesys-import
- `public.queue` ← genesys-import
- `public.skills` ← genesys-import
- `temp.sgd_clientcontact` ← não mapeado no Maestro
- **Colunas entregues:** `conversation_id` (string), `dateTime_start` (dateTime), `dateTime_end` (dateTime), `dtime_start` (string), `dtime_end` (string), `queue_id` (string), `_ani` (string), `metric_tAbandon` (double), `aband_txt` (string), `name_skill` (string), `i_client` (double), `linkcall` (string), `_mos` (double), `dDate` (int64)

SQL nativo:

```sql
SELECT 
    c.conversation_id, 
    c."dateTime_start", 
    c."dateTime_end", 
    c.dtime_start, 
    c.dtime_end, 
    c.queue_id, 
    c._ani, 
    c."metric_tAbandon",
    CASE 
        WHEN c."metric_tAbandon" <= 8000 THEN 'Immediate' /*Immediate*/
        WHEN c."metric_tAbandon" <= 30000 THEN '30 Sec' /*30seg*/
        WHEN c."metric_tAbandon" <= 60000 THEN '60 Sec' /*60seg*/ 
        WHEN c."metric_tAbandon" <= 120000 THEN '2 Min' /*120seg*/
        WHEN c."metric_tAbandon" <= 180000 THEN '3 Min' /*180seg*/
        WHEN c."metric_tAbandon" <= 300000 THEN '5 Min' /*300seg*/
        WHEN c."metric_tAbandon" <= 600000 THEN '10 Min' /*600seg*/
        WHEN c."metric_tAbandon" <= 1200000 THEN '20 Min' /*1200seg*/
        ELSE '> 20 Min' /* > 1200seg*/
    END AS aband_txt,
    CASE 
        WHEN substring((SELECT name_skill FROM public.skills WHERE id_skill = 
            (CASE
                WHEN (SELECT RIGHT(name_skill,6) FROM public.skills WHERE id_skill = c.skill_id_2) IN ('CAMP_S','CRIC_S') THEN skill_id_2     
                ELSE skill_id_1
            END)),14) IS NULL THEN substring((SELECT name_queue FROM public.queue WHERE id_queue = queue_id),14)
        ELSE substring((SELECT name_skill FROM public.skills WHERE id_skill =
            (CASE
                WHEN (SELECT RIGHT(name_skill,6) FROM public.skills WHERE id_skill = c.skill_id_2) IN ('CAMP_S','CRIC_S') THEN skill_id_2
                ELSE skill_id_1
            END)),14)
    END AS name_skill ,
    (select cli.i_clientes from temp."SGD_ClientContact" cli where RIGHT(cli.numero_telefone,8) = RIGHT(c._ani,8) limit 1) as i_client
, ('https://apps.mypurecloud.com/directory/#/engage/admin/interactions/'||c.conversation_id) as linkCall,
coalesce(_mos,0) as _mos

FROM 
    public."historic_callsAbandoned" AS c
```

## `genesys_historicCallsAgents`

- **Origem:** Postgres · base `DB_GENESYS`
- `public.callswithclient` ← genesys-import
- `public.historic_calls_ia_new` ← insights-realtime/insights-resumos (lib _insights)
- `public.historic_callsagents` ← genesys-import; produtividade-pendencia-realtime
- `public.queue` ← genesys-import
- `public.sgd_alocations` ← import-sgd-diario (recarga TOTAL)
- `public.skills` ← genesys-import
- **Colunas entregues:** `conversation_id` (string), `user_id` (string), `metric_tAcd` (double), `metric_tAcw` (double), `metric_tTalkComplete` (double), `metric_tIvr` (double), `metric_tHeldComplete` (double), `metric_tAlert` (double), `metric_tAbandon` (double), `metric_nTransferred` (double), `metric_tTalk` (double), `metric_tHeld` (double), `metric_nOutboundAttempted` (double), `metric_tContacting` (double), `metric_tDialing` (double), `metric_tHandle` (double), `metric_nBlindTransferred` (double), `metric_nConsult` (double), `metric_nConsultTransferred` (double), `metric_oMediaCount` (double), `metric_oExternalMediaCount` (double), `metric_tVoicemail` (double), `metric_tMonitoring` (double), `metric_tFlowOut` (double), `metric_nOffered` (double), `metric_tAnswered` (double), `dDateTime` (dateTime), `dDate` (int64), `dtime_start` (string), `dtime_end` (string), `queue_id` (string), `skill_id_1` (string), `skill_id_2` (string), `bullseye` (double), `direction` (string), `purpose` (string), `disconnecttype_out` (string), `disconnecttype` (string), `wrapupcode` (string), `_ani` (string), `_dnis` (string), `metric_nNotResponding` (double), `metric_tNotResponding` (double), `sla` (int64), `sla_txt` (string), `tma_txt` (string), `name_queue` (string), `name_skill` (string), `skill_filter` (string), `area` (string), `removed_skill` (string), `sgd_iclient` (int64), `sgd_i_user` (int64), `sgd_i_alocation` (int64), `_mos` (double), `survey_id` (string), `mencao_pesquisa` (int64), `sgd_namecontact` (string), `TimeStartInteraction` (time), `_aniDDD` (string), `LinkCall` (string)

SQL nativo:

```sql
SELECT "historic_callsAgents".conversation_id as conversation_id, user_id, "metric_tAcd", "metric_tAcw", "metric_tTalkComplete", "metric_tIvr", "metric_tHeldComplete", "metric_tAlert", "metric_tAbandon", "metric_nTransferred", "metric_tTalk", "metric_tHeld", "metric_nOutboundAttempted", "metric_tContacting", "metric_tDialing", "metric_tHandle", "metric_nBlindTransferred", "metric_nConsult", "metric_nConsultTransferred", "metric_oMediaCount", "metric_oExternalMediaCount", "metric_tVoicemail", "metric_tMonitoring", "metric_tFlowOut", "metric_nOffered", "metric_tAnswered", "dateTime_start", "dateTime_end", dtime_start, dtime_end, queue_id, skill_id_1, skill_id_2, bullseye, direction, purpose, disconnecttype, disconnecttype_out, wrapupcode, _ani, _dnis,"metric_nNotResponding","metric_tNotResponding",
(case 
when "metric_tAnswered" <= 8000 then 8 /*8seg*/
when "metric_tAnswered" <= 30000 then 30 /*30seg*/
when "metric_tAnswered" <= 60000 then 60 /*60seg*/
when "metric_tAnswered" <= 90000 then 90 /*90seg*/
when "metric_tAnswered" <= 120000 then 120 /*120seg*/
when "metric_tAnswered" <= 180000 then 180 /*180seg*/
when "metric_tAnswered" <= 300000 then 300 /*300seg*/
when "metric_tAnswered" <= 600000 then 600 /*600seg*/
when "metric_tAnswered" <= 1200000 then 1200 /*1200seg*/
when "metric_tAnswered" >  1200000 then 9999 /* > 1200seg*/
else 0 end) as sla,

(case 
when "metric_tAnswered" <= 8000 then 'Immediate' /*Immediate*/
when "metric_tAnswered" <= 30000 then '30 Sec' /*30seg*/
when "metric_tAnswered" <= 60000 then '60 Sec' /*60seg*/
when "metric_tAnswered" <= 90000 then '90 Sec' /*90seg*/
when "metric_tAnswered" <= 120000 then '2 Min' /*120seg*/
when "metric_tAnswered" <= 180000 then '3 Min' /*180seg*/
when "metric_tAnswered" <= 300000 then '5 Min' /*300seg*/
when "metric_tAnswered" <= 600000 then '10 Min' /*600seg*/
when "metric_tAnswered" <= 1200000 then '20 Min' /*1200seg*/
when "metric_tAnswered" >  1200000 then '> 20 Min' /* > 1200seg*/
else '' end) as sla_txt,

(case 
when "metric_tTalk" <= 8000 then 'Immediate' /*Immediate*/
when "metric_tTalk" <= 30000 then '30 Sec' /*30seg*/
when "metric_tTalk" <= 60000 then '60 Sec' /*60seg*/
when "metric_tTalk" <= 90000 then '90 Sec' /*90seg*/
when "metric_tTalk" <= 120000 then '2 Min' /*120seg*/
when "metric_tTalk" <= 180000 then '3 Min' /*180seg*/
when "metric_tTalk" <= 300000 then '5 Min' /*300seg*/
when "metric_tTalk" <= 600000 then '10 Min' /*600seg*/
when "metric_tTalk" <= 1200000 then '20 Min' /*1200seg*/
when "metric_tTalk" >  1200000 then '> 20 Min' /* > 1200seg*/
else '' end) as tma_txt,

substring((select name_queue from public.queue where id_queue = queue_id),14) AS name_queue,

(case 
when substring((select name_skill from public.skills where id_skill = 
 (
case
when (select RIGHT(name_skill,6) from public.skills where id_skill = skill_id_2) IN ('CAMP_S','CRIC_S','_SUL_S') THEN skill_id_2
when bullseye > 1 then  removed_skill     
else skill_id_1
 end)),14) isnull then substring((select name_queue from public.queue where id_queue = queue_id),14)
 
 else 
substring((select name_skill from public.skills where id_skill =
 (
case
when (select RIGHT(name_skill,6) from public.skills where id_skill = skill_id_2) IN ('CAMP_S','CRIC_S','_SUL_S') THEN skill_id_2
when bullseye > 1 then  removed_skill
else skill_id_1
 end)),14) end ) as name_skill,


(case 
when (select right(name_skill,6) from public.skills where id_skill =
 (
case
when (select RIGHT(name_skill,6) from public.skills where id_skill = skill_id_2) IN ('CAMP_S','CRIC_S','_SUL_S') THEN skill_id_2
else skill_id_1
 end)) in ('CAMP_S') then 'Campinas'

when (select RIGHT(name_skill,6) from public.skills where id_skill =
 (
case
when (select right(name_skill,6) from public.skills where id_skill = skill_id_2) IN ('CAMP_S','CRIC_S','_SUL_S') THEN skill_id_2
else skill_id_1
 end)) in ('CRIC_S','_SUL_S') then 'Regional Sul'

when (select name_skill from public.skills where id_skill = skill_id_1) like '%31%' then 'AT'
when (select name_skill from public.skills where id_skill = skill_id_1) like '%32%' then 'AT'
when (select name_skill from public.skills where id_skill = skill_id_1) like '%41%' then 'AT'
when (select name_skill from public.skills where id_skill = skill_id_1) like '%42%' then 'AT'
when (select name_skill from public.skills where id_skill = skill_id_1) like '%43%' then 'AT'
when (select name_skill from public.skills where id_skill = skill_id_1) like '%51%' then 'AT'
when (select name_skill from public.skills where id_skill = skill_id_1) like '%52%' then 'AT'
when (select name_skill from public.skills where id_skill = skill_id_1) like '%61%' then 'AT'
when (select name_skill from public.skills where id_skill = skill_id_1) like '%62%' then 'AT'
when (select name_skill from public.skills where id_skill = skill_id_1) like '%Conversao%' then 'AT' 
when (select name_skill from public.skills where id_skill = skill_id_1) like '%Performance%' then 'AT'
when (select name_skill from public.skills where id_skill = skill_id_1) like '%_DS_%' then 'TR BANK'  

 
else 'Queue' end) as Skill_Filter, q.area,
substring((select name_skill from public.skills where id_skill = removed_skill),14) as removed_Skill,
coalesce((select c.i_client from public."callsWithClient" as c where c.conversation_id = "historic_callsAgents".conversation_id limit 1),0) as sgd_iClient, 
coalesce((select c.name_contact from public."callsWithClient" as c where c.conversation_id = "historic_callsAgents".conversation_id limit 1),'') as sgd_nameContact,
coalesce(g.i_user,0) as sgd_i_user, 
coalesce(g.i_alocation,999) as sgd_i_alocation,
coalesce(_mos,0) as _mos,
coalesce ("historic_callsAgents".survey_id,'') as survey_id,
cast( (CASE 
            WHEN length(ia_new.mencao_pesquisa) > 1 THEN '0'
            ELSE coalesce(ia_new.mencao_pesquisa, '0') 
        END) as int) AS mencao_pesquisa



FROM public."historic_callsAgents" inner join public.queue as q on q.id_queue = queue_id /*and direction = 'inbound'*/
                                    LEFT JOIN 
                                                public.sgd_alocations AS g ON g.id_user_genesys = "historic_callsAgents".user_id
                                              and g.ddate::date = "historic_callsAgents"."dateTime_start"::date
                                    left JOIN
                                                public.historic_calls_ia_new as ia_new
                                                ON ia_new.conversation_id = "historic_callsAgents".conversation_id
                                                and ia_new.session_id = "historic_callsAgents".session_id

--where "historic_callsAgents"."dateTime_start"::date >= '2026-05-25'
ORDER BY  "historic_callsAgents"."dateTime_start"::date asc, "historic_callsAgents".conversation_id
```

## `genesys_historicCalls_ia`

- **Origem:** Postgres · base `DB_GENESYS`
- `public.historic_calls_ia` ← não mapeado no Maestro
- `public.historic_calls_ia_new` ← insights-realtime/insights-resumos (lib _insights)
- **Colunas entregues:** `conversation_id` (string), `resumo` (string), `problema_1` (string), `problema_2` (string), `frustracoes` (string), `dificuldades` (string), `analise_especifica_original` (string), `analise_especifica` (string), `analise_saudacao` (string)

SQL nativo:

```sql
WITH base AS (
    SELECT 
        conversation_id, 
        resumo, 
        problema_1,
        problema_2, 
        frustacoes AS frustracoes, 
        dificuldades, 
        COALESCE(analise_especifica, '') AS analise_especifica_original,
        CASE
            WHEN analise_especifica ILIKE '%tributaria%' THEN 'reforma_tributaria'
            WHEN analise_especifica ILIKE '%erro_8%' THEN 'erro_8'
            ELSE ''
        END AS analise_especifica,
        CASE 
            WHEN analise_saudacao = 'Não' THEN 'Não'
            WHEN analise_saudacao = 'Sim' THEN 'Sim'
            ELSE 'Não Identificado'
        END AS analise_saudacao,
        2 AS prioridade
    FROM public.historic_calls_ia

    UNION ALL

    SELECT 
        conversation_id, 
        resumo_breve AS resumo, 
        problema_principal AS problema_1,
        problemas_secundarios AS problema_2, 
        frustracao_cliente AS frustracoes, 
        dificuldades_atendimento AS dificuldades, 
        COALESCE(classificacao_especifica, '') AS analise_especifica_original,
        CASE
            WHEN classificacao_especifica ILIKE '%tributaria%' THEN 'reforma_tributaria'
            WHEN classificacao_especifica ILIKE '%erro_8%' THEN 'erro_8'
            ELSE ''
        END AS analise_especifica,
        CASE 
            WHEN saudacao_agent = 'Não' THEN 'Não'
            WHEN saudacao_agent = 'Sim' THEN 'Sim'
            ELSE 'Não Identificado'
        END AS analise_saudacao,
        1 AS prioridade
    FROM public.historic_calls_ia_new
),

deduplicado AS (
    SELECT *,
           ROW_NUMBER() OVER (
               PARTITION BY conversation_id
               ORDER BY prioridade
           ) AS rn
    FROM base
)

SELECT 
    conversation_id,
    resumo,
    problema_1,
    problema_2,
    frustracoes,
    dificuldades,
    analise_especifica_original,
    analise_especifica,
    analise_saudacao
FROM deduplicado
WHERE rn = 1
```

## `genesys_historicCallsTransfer`

- **Origem:** Postgres · base `DB_GENESYS`
- `public.historic_callstranfers` ← genesys-import
- `public.users_genesys` ← genesys-import
- **Colunas entregues:** `conversation_id` (string), `link` (string), `queue_name` (string), `dateTime_start` (int64), `start` (time), `end` (time), `_user` (string), `disconnect` (string), `gerente` (string), `supervisor` (string), `status` (string), `mesma_fila` (int64), `fora_dominio` (int64)

SQL nativo:

```sql
WITH cte AS (
    SELECT 
        conversation_id, 
        queue_name, 
        "dateTime_start", 
        "dateTime_end", 
        _user,
        disconnect,
        LEAD(queue_name) OVER (Partition BY conversation_id order by "dateTime_start") AS next_queue_name,
        LEAD(_user) OVER (ORDER BY conversation_id, "dateTime_start") AS next_user
        
    FROM public."historic_callsTranfers"
    order by 1,3
)
SELECT
    conversation_id,
    'https://apps.mypurecloud.com/directory/#/engage/admin/interactions/'||conversation_id||'/timeline' as link,
    queue_name,
    "dateTime_start",
    "dateTime_end",
    _user,
    cte.disconnect,
    coalesce(u.gerente,'Flow') as gerente,
    coalesce(u.supervisor,'Flow') as supervisor,
    coalesce(u.status,'Flow') as status,
    CASE WHEN _user <> 'Flow' and next_user = 'Flow'  AND next_queue_name = queue_name and cte.disconnect = 'transfer'THEN 1 ELSE 0 END AS mesma_fila,
    CASE when next_queue_name isnull then 0
         when next_queue_name ='erro' then 0
         when left(next_queue_name,20) <>'LATAM_Brazil_Dominio'  then 1
         ELSE 0 END AS fora_dominio
FROM cte left join public."users_Genesys" as u on u.name = _user
--where conversation_id = '0ce38bf6-5445-4e65-89bf-e93e13ca99d0'
order by 1,4
```

## `genesys_presenceDefinitions`

- **Origem:** Postgres · base `DB_GENESYS`
- `public.presencedefinitions` ← genesys-import
- **Colunas entregues:** `id_SystemPresence` (string), `nameSystemPresence` (string), `nameSecondPresence` (string), `primaryStatus` (boolean)

SQL nativo:

```sql
Select * from public."presenceDefinitions"
```

## `genesys_qualificationsSkills`

- **Origem:** Postgres · base `DB_GENESYS`
- `public.historic_qualifications` ← genesys-import; genesys-sla
- `public.queue` ← genesys-import
- `public.skills` ← genesys-import
- **Colunas entregues:** `skill_id_1` (string), `skill_id_2` (string), `date_interval` (int64), `time_interval` (string), `metric_nOffered` (double), `metric_nAnswered` (double), `metric_tAnswered` (double), `metric_tAnsweredMax` (double), `metric_tAnsweredMin` (double), `metric_nAbandon` (double), `metric_tAbandon` (double), `metric_tAbandonMax` (double), `metric_tAbandonMin` (double), `metric_tFlowOut` (double), `metric_oServiceLevel` (double), `metric_oServiceTarget` (double), `metric_nHandle` (double), `metric_tHandle` (double), `metric_tHandleMax` (double), `metric_tHandleMin` (double), `metric_nTalkComplete` (double), `metric_tTalkComplete` (double), `metric_tTalkCompleteMax` (double), `metric_tTalkCompleteMin` (double), `metric_tHeldComplete` (double), `metric_nAcw` (double), `metric_tAcw` (double), `metric_tAcwMax` (double), `metric_tAcwMin` (double), `metric_nTransferred` (double), `metric_nOverSla` (double), `metric_tShortAbandon` (double), `metric_nWait` (double), `metric_tWait` (double), `metric_tWaitMax` (double), `metric_tWaitMin` (double), `metric_nOutboundAttempted` (double), `metric_tVoicemail` (double), `metric_tAbandon60` (double), `metric_tAbandon120` (double), `metric_tAbandon180` (double), `metric_tAbandon300` (double), `metric_tAbandon600` (double), `metric_tAbandonMore600` (double), `namequeue` (string), `nameskill` (string), `dDateTime` (dateTime), `Area` (string)

SQL nativo:

```sql
SELECT skill_id_1, skill_id_2, date_interval, time_interval,"metric_nOffered", "metric_nAnswered", "metric_tAnswered", "metric_tAnsweredMax", "metric_tAnsweredMin", "metric_nAbandon", "metric_tAbandon", "metric_tAbandonMax", "metric_tAbandonMin", "metric_tFlowOut", "metric_oServiceLevel", "metric_oServiceTarget", "metric_nHandle", "metric_tHandle", "metric_tHandleMax", "metric_tHandleMin", "metric_nTalkComplete", "metric_tTalkComplete", "metric_tTalkCompleteMax", "metric_tTalkCompleteMin", "metric_tHeldComplete", "metric_nAcw", "metric_tAcw", "metric_tAcwMax", "metric_tAcwMin", "metric_nTransferred", "metric_nOverSla", "metric_tShortAbandon", "metric_nWait", "metric_tWait", "metric_tWaitMax", "metric_tWaitMin", "metric_nOutboundAttempted", "metric_tVoicemail","metric_tAbandon60", "metric_tAbandon120", "metric_tAbandon180", "metric_tAbandon300", "metric_tAbandon600", "metric_tAbandonMore600",
substring((select name_queue from public.queue where id_queue = skill_id_1),14) as nameQueue,
substring((
         case 
              when skill_id_2 in ('e86472be-1a9e-4e33-a433-e3be222fd09a','ccc418b3-bd1e-4a4c-851e-d98b3a2758d2','dff724ce-b2c1-4695-b933-d3698d724dae')
                         then 'Latam_Brazil_Dominio_CAMP_S'

              when (select name_skill from public.skills where id_skill = skill_id_2) isnull 
                            then (select name_queue from public.queue where id_queue = skill_id_1)

              else (select name_skill from public.skills where id_skill = skill_id_2) end),14) as nameSkill

FROM public.historic_qualifications
```

## `genesys_queue`

- **Origem:** Postgres · base `DB_GENESYS`
- `public.queue` ← genesys-import
- **Colunas entregues:** `id_queue` (string), `name_queue` (string), `area` (string), `description` (string), `region` (string)

SQL nativo:

```sql
Select id_queue, substring(name_queue,14) as name_queue,area,description, region from public."queue"
```

## `genesys_queuePerformance_HalfHour`

- **Origem:** Postgres · base `DB_GENESYS`
- `public.queue_performance` ← genesys-import
- **Colunas entregues:** `date_interval` (int64), `id_queue` (string), `time_interval` (string), `_nOffered` (double), `_tAnswered` (double), `_tAbandon` (double), `_nOutbound` (double), `_tFlowOut` (double), `_nConnected` (double), `_oServiceLevel` (double), `_tWait` (double), `_tWaitMax` (double), `_tWaitMin` (double), `_tHandle` (double), `_tHandleMin` (double), `_tHandleMax` (double), `_tTalkComplete` (double), `_tTalkCompleteMax` (double), `_tTalkCompleteMin` (double), `_tHeldComplete` (double), `_tAcw` (double), `_tAcd` (double), `_tAcMax` (double), `_tAcdMin` (double), `_tDialing` (double), `_tContacting` (double), `_nTransferred` (double), `_nBlindTransferred` (double), `_nConsult` (double), `_nConsultTransferred` (double), `_oExternalMediaCount` (double), `_oMediaCount` (double), `_nOverSla` (double), `_tShortAbandon` (double), `_nOutboundAttempted` (double), `_tVoicemail` (double), `_nError` (double), `dDateTime` (dateTime)

SQL nativo:

```sql
Select * from public."queue_Performance"
```

## `genesys_skill`

- **Origem:** Postgres · base `DB_GENESYS`
- `public.skills` ← genesys-import
- **Colunas entregues:** `id_skill` (string), `name_skill` (string), `area` (string), `regional` (string)

SQL nativo:

```sql
Select id_skill, substring(name_skill,14)as name_skill,area, regional from public."skills"
```

## `dTime`

- **Origem:** Json.Document, Table.FromRows
- **Colunas entregues:** `dTime` (string)

## `genesys_users`

- **Origem:** Postgres · base `DB_GENESYS`
- `public.users_genesys` ← genesys-import
- **Colunas entregues:** `id_user` (string), `email` (string), `name` (string), `status` (string), `supervisor` (string), `department` (string), `gerente` (string), `role_genesys` (string), `lider` (string), `lider_area` (string)

SQL nativo:

```sql
SELECT  id_user, lower(email) as email,name, status, supervisor, 
department, gerente, role_genesys, 
(case 
    when lider is true then 'Sim'
else 'Não' end ) as lider,
coalesce(lider_area,'') as lider_area
    FROM public."users_Genesys" order by name asc
```

## `genesys_survey`

- **Origem:** Postgres · base `DB_GENESYS`
- `public.historic_callsagents` ← genesys-import; produtividade-pendencia-realtime
- `public.survey` ← genesys-import; produtividade-pendencia-realtime
- `public.survey_question` ← não mapeado no Maestro
- `public.survey_question_option` ← não mapeado no Maestro
- **Colunas entregues:** `conversation_id` (string), `user_id` (string), `survey_id` (string), `total_agents` (int64), `Problema Resolvido` (string), `Satisfação Atendente` (string), `Detalhe Votação` (string)

SQL nativo:

```sql
SELECT 
    ca.conversation_id,
    ca.user_id,
    survey_numbered.survey_id,
    (SELECT distinct count(t.user_id) 
     FROM public."historic_callsAgents" as t 
     WHERE t.conversation_id = ca.conversation_id)::int AS total_agents,

    coalesce(MAX(CASE WHEN question_order = 1 THEN coalesce(resposta,'') END),'') AS "Problema Resolvido",
    coalesce(MAX(CASE WHEN question_order = 2 THEN coalesce(resposta,'') END),'') AS "Satisfação Atendente",
    COALESCE(MAX(CASE WHEN 
                     question_order = 3 THEN NULLIF(TRIM(replace(resposta, '[null]', '')), '')
                     END), '') AS "Detalhe Votação"

FROM (
    SELECT
        s.survey_id,
        s.user_id,
        q.question_order,
        CASE 
            -- Pergunta 3: Se não achar na tabela de opções, aceita o que estiver escrito na survey
            WHEN q.question_order = 3 THEN COALESCE(NULLIF(op.answer, ''), s.answer_id)
            -- Demais perguntas: Só traz se achar o texto correspondente, senão vazio
            ELSE COALESCE(op.answer, '')
        END AS resposta
    FROM public.survey AS s
    LEFT JOIN public.survey_question AS q
        ON q.question_id = s.question_id
    LEFT JOIN public.survey_question_option AS op
        -- ALTERADO: Filtrando apenas pelo ID da resposta (UUID), 
        -- removendo a trava do question_id que costuma causar incompatibilidade
        ON op.answer_id = s.answer_id
) AS survey_numbered

LEFT JOIN public."historic_callsAgents" AS ca
    ON ca.survey_id = survey_numbered.survey_id

GROUP BY
    ca.conversation_id,
    ca.user_id,
    survey_numbered.survey_id;
```
