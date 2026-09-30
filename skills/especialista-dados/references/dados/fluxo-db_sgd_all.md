# Fluxo `DB_SGD_ALL`

> Última atualização: 2026-09-30 · Fonte: `DB_SGD_ALL.json` (Dataflow Power BI, modificado em 2026-09-09, cultura en-US) · **Gerado automaticamente** por `scripts/mapear_fluxos.py`.

| Entidade | Carrega | Origem | Base | Tabelas de origem | Colunas | Último refresh (UTC) |
|---|---|---|---|---|---|---|
| `calendar` | sim | Postgres | DB_SGD | `public.calendar` | 22 | 2026-09-29T08:30:37 |
| `sgd_alocation_reg` | sim | Postgres | DB_SGD | `forecast.de_para_alocacao`, `public.sgd_alocation_reg` | 5 | 2026-09-29T08:31:08 |
| `sgd_alocation_historic` | sim | Postgres | DB_SGD | `public.sgd_alocation_historic` | 4 | 2026-09-29T08:31:38 |
| `sgd_bkn_last_backup` | sim | Postgres | DB_SGD_N2 | `ss.ultimo_backup_bkn` | 4 | 2026-09-29T08:32:39 |
| `sgd_cargos` | sim | Postgres | DB_SGD | `public.sgd_cargos` | 3 | 2026-09-29T08:33:09 |
| `sgd_client` | sim | Postgres | DB_SGD | `public.protocols`, `public.sgd_client`, `public.sgd_client_observ`, `public.sgd_users` | 21 | 2026-09-29T08:33:40 |
| `sgd_client_user` | sim | Postgres | DB_SGD | `public.sgd_user_client` | 14 | 2026-09-29T08:34:10 |
| `sgd_client_phone` | sim | Postgres | DB_SGD | `public.sgd_client_contact` | 4 | 2026-09-29T08:34:41 |
| `sgd_client_product` | sim | Postgres | DB_SGD | `public.sgd_product_client` | 8 | 2026-09-29T08:35:12 |
| `sgd_config_pref_pesquisas` | sim | Postgres | DB_SGD | `public.sgd_alocation_historic`, `public.sgd_preferencia_pesquisa` | 8 | 2026-09-29T08:35:42 |
| `sgd_product` | sim | Postgres | DB_SGD | `public.sgd_product` | 2 | 2026-09-29T08:36:13 |
| `sgd_resales` | sim | Postgres | DB_SGD | `public.sgd_resale` | 6 | 2026-09-29T08:36:44 |
| `sgd_ss` | sim | Postgres | DB_SGD_N2 | `ss.date_entry`, `ss.html`, `ss.i_classification`, `ss.i_dissatisfied_reason`, `ss.i_module`, `ss.i_resales`, `ss.i_satisfaction`, `ss.i_situacao`, `ss.i_ss`, `ss.i_subtopic`, `ss.i_system`, `ss.i_topc`, `ss.i_userreasales`, `ss.last_update`, `ss.ss`, `ss.ss_classification`, `ss.ss_disregard_dissatisfaction`, `ss.ss_module`, `ss.ss_sub_topic`, `ss.ss_system`, `ss.ss_topic`, `ss.ss_tramites`, `ss.ss_tramites_time` | 21 | 2026-09-29T08:37:14 |
| `sgd_ss_category` | sim | Postgres | DB_SGD_N2 | `ss.ss_category` | 3 | 2026-09-29T08:37:45 |
| `sgd_ss_classification` | sim | Postgres | DB_SGD_N2 | `ss.ss_classification` | 2 | 2026-09-29T08:38:16 |
| `sgd_ss_tramite` | sim | Postgres | DB_SGD_N2 | `ss.ss_tramites`, `ss.ss_tramites_time` | 20 | 2026-09-29T08:40:17 |
| `sgd_ss_dissatisfied_conclusion_text` | sim | Postgres | DB_SGD_N2 | `ss.ss_conclusion_text` | 3 | 2026-09-29T08:40:47 |
| `sgd_ss_dissatisfied_reason` | sim | Postgres | DB_SGD_N2 | `ss.ss_dissatisfied_reason` | 2 | 2026-09-29T08:41:18 |
| `sgd_ss_dissatisfied_description` | sim | Postgres | DB_SGD_N2 | `ss.ss_satisfaction_description` | 2 | 2026-09-29T08:41:49 |
| `sgd_ss_forwarding` | sim | Postgres | DB_SGD_N2 | `ss.i_classification`, `ss.i_resales`, `ss.i_ss`, `ss.ss`, `ss.ss_situation`, `ss.ss_tramites` | 9 | 2026-09-29T08:42:49 |
| `sgd_ss_pendency` | sim | Postgres | DB_SGD_N2 | `ss.i_classification`, `ss.i_ss`, `ss.ss`, `ss.ss_pendency` | 8 | 2026-09-29T08:43:20 |
| `sgd_ss_pendency_time` | sim | Postgres | DB_SGD_N2 | `ss.ss_situation`, `ss.ss_tramites`, `ss.ss_tramites_time` | 5 | 2026-09-29T08:44:21 |
| `sgd_ss_situation` | sim | Postgres | DB_SGD_N2 | `ss.ss_situation` | 3 | 2026-09-29T08:44:51 |
| `sgd_ssc` | sim | Postgres | DB_SGD | `public.sgd_alocation_historic`, `public.sgd_client`, `public.sgd_ssc`, `public.sgd_ssc_disregard_dissatisfaction`, `public.sgd_ssc_tramites` | 45 | 2026-09-29T08:56:52 |
| `sgd_ssc_answer_time` | sim | Postgres | DB_SGD | `public.sgd_ssc`, `public.sgd_ssc_answer_time` | 18 | 2026-09-29T09:02:23 |
| `sgd_ssc_classification` | sim | Postgres | DB_SGD | `public.sgd_ssc_classification` | 2 | 2026-09-29T09:02:54 |
| `sgd_ssc_disregard_dissatisfaction` | sim | Postgres | DB_SGD | `public.sgd_ssc_disregard_dissatisfaction` | 6 | 2026-09-29T09:03:25 |
| `sgd_ssc_dissatisfaction_historic` | sim | Postgres | DB_SGD | `public.sgd_ssc_dissatisfaction_historic` | 4 | 2026-09-29T09:03:56 |
| `sgd_ssc_internal_time` | sim | Postgres | DB_SGD | `public.sgd_ssc`, `public.sgd_ssc_internal_time` | 15 | 2026-09-29T09:04:56 |
| `sgd_ssc_means_access` | sim | Json.Document, Table.FromRows | — | — | 2 | 2026-09-29T09:05:27 |
| `sgd_ssc_pendency` | sim | Postgres | DB_SGD | `public.sgd_pendency` | 24 | 2026-09-29T09:07:27 |
| `sgd_ssc_pesquisa_resposta_utiliza_solucao` | sim | Postgres | DB_SGD | `public.sgd_ssc_utiliza_solucao` | 8 | 2026-09-29T09:08:58 |
| `sgd_ssc_reason_dissatisfaction` | sim | Postgres | DB_SGD | `public.sgd_ssc_reason_dissatisfaction` | 2 | 2026-09-29T09:09:29 |
| `sgd_ssc_sa` | sim | Postgres | DB_SGD | `public.sgd_ssc_sa` | 3 | 2026-09-29T09:10:00 |
| `sgd_ssc_situation` | sim | Postgres | DB_SGD | `public.sgd_ssc_situation` | 2 | 2026-09-29T09:10:31 |
| `sgd_ssc_soses` | sim | Postgres | DB_SGD | `public.sgd_soses` | 13 | 2026-09-29T09:11:01 |
| `sgd_ssc_text_conclusion` | sim | Postgres | DB_SGD | `public.sgd_ssc_text_conclusion` | 4 | 2026-09-29T09:11:32 |
| `sgd_ssc_tramites` | sim | Postgres | DB_SGD | `public.sgd_ssc_tramites` | 10 | 2026-09-29T09:21:03 |
| `sgd_ssc_vs_genesys` | sim | Postgres | DB_SGD | `public.sgd_genesys` | 4 | 2026-09-29T09:21:34 |
| `sgd_schedule_absences_reason` | sim | Postgres | DB_SGD | `public.sgd_schedule_absences_reason` | 4 | 2026-09-29T09:22:05 |
| `sgd_schedule_absences_type` | sim | Postgres | DB_SGD | `public.sgd_schedule_absences_type` | 3 | 2026-09-29T09:22:36 |
| `sgd_schedule` | sim | Postgres | DB_SGD | `public.sgd_alocation_historic`, `public.sgd_schedule` | 11 | 2026-09-29T09:24:06 |
| `sgd_schedule_past_future` | sim | Postgres | DB_SGD | `public.sgd_schedule_past_future` | 9 | 2026-09-29T09:24:37 |
| `sgd_schedule_three_days` | sim | Postgres | DB_SGD | `public.sgd_alocation_historic`, `public.sgd_schedule_three_days` | 11 | 2026-09-29T09:26:07 |
| `sgd_users` | sim | Postgres | DB_SGD | `public.sgd_users` | 10 | 2026-09-29T09:26:38 |
| `sgd_users_horario_historic` | sim | Postgres | DB_SGD | `public.sgd_horario_historic` | 8 | 2026-09-29T09:27:09 |
| `sgd_user_manager_historic` | sim | Postgres | DB_SGD | `public.sgd_alocation_historic`, `public.sgd_user_manager_historic` | 11 | 2026-09-29T09:29:09 |
| `sgd_user_position_historic` | sim | Postgres | DB_SGD | `public.sgd_user_cargo_historico` | 4 | 2026-09-29T09:29:40 |
| `sgd_sa_module` | sim | Postgres | DB_SGD | `public.sgd_sa_module` | 3 | 2026-09-29T09:30:11 |
| `sgd_sa_system` | sim | Postgres | DB_SGD | `public.sgd_sa_system` | 2 | 2026-09-29T09:30:41 |
| `sgd_sa` | sim | Postgres | DB_SGD | `public.sgd_sa` | 13 | 2026-09-29T09:31:12 |
| `sgd_sa_description` | sim | Postgres | DB_SGD | `public.sgd_sa` | 3 | 2026-09-29T09:31:43 |
| `sgd_sa_classification` | sim | Postgres | DB_SGD | `public.sgd_sa_classification` | 2 | 2026-09-29T09:32:14 |
| `sgd_sa_disapproval_reason` | sim | Postgres | DB_SGD | `public.sgd_sa_disapproval_reason` | 2 | 2026-09-29T09:32:44 |
| `sgd_sa_priority` | sim | Postgres | DB_SGD | `public.sgd_sa_priority` | 4 | 2026-09-29T09:33:15 |
| `sgd_sa_situations` | sim | Postgres | DB_SGD | `public.sgd_sa_situations` | 2 | 2026-09-29T09:33:46 |
| `sgd_sai_vs_sane` | sim | Postgres | DB_SGD | `public.sgd_sai_sane` | 2 | 2026-09-29T09:34:16 |
| `forecast_ajuste_demanda` | sim | Postgres | DB_SGD | `forecast.ajuste_demanda`, `public.calendar` | 4 | 2026-09-29T09:34:47 |
| `forecast_avg_produtividade` | sim | Postgres | DB_SGD | `forecast.produtividade_media`, `public.calendar` | 4 | 2026-09-29T09:35:17 |
| `forecast_client_user_history` | sim | Postgres | DB_SGD | `forecast.client_user_history` | 6 | 2026-09-29T09:45:48 |
| `forecast_coefficient` | sim | Postgres | DB_SGD | `forecast.coefficient` | 12 | 2026-09-29T09:46:20 |
| `forecast_demanda_projetada` | sim | Postgres | DB_SGD | `forecast.demanda_projetada` | 6 | 2026-09-29T09:46:50 |
| `forecast_de_para_alocacao_area` | sim | Postgres | DB_SGD | `forecast.de_para_alocacao` | 3 | 2026-09-29T09:47:21 |
| `forecast_de_para_calendar` | sim | Postgres | DB_SGD | `forecast.de_para_calendar` | 2 | 2026-09-29T09:47:52 |
| `forecast_FTE_aprovado` | sim | Postgres | DB_SGD | `forecast.fte_aprovado`, `public.calendar` | 4 | 2026-09-29T09:48:22 |
| `forecast_proj_ausencias` | sim | Postgres | DB_SGD | `forecast.ausencias_projetado`, `public.calendar` | 5 | 2026-09-29T09:49:23 |
| `forecast_proj_tme` | sim | Postgres | DB_SGD | `forecast.tme_projetado` | 6 | 2026-09-29T09:49:54 |
| `forecast_projetado` | sim | Postgres | DB_SGD | `forecast.projetado` | 10 | 2026-09-29T09:50:24 |
| `forecast_users_proj` | sim | Postgres | DB_SGD | `forecast.users` | 3 | 2026-09-29T09:50:55 |
| `sgd_ssc_ss` | sim | Postgres | DB_SGD | `public.sgd_ssc_ss` | 2 | 2026-09-29T09:51:25 |
| `sgd_chain_ia_interacao` | sim | Postgres | DB_SGD | `public.chain_ia_interacao` | 10 | 2026-09-29T09:51:56 |

## `calendar`

- **Origem:** Postgres · base `DB_SGD`
- `public.calendar` ← mantida manualmente por fora do Maestro (orq:modules/import_agendas/skills.md:55)
- **Colunas entregues:** `date` (date), `date_int` (int64), `day` (int64), `day_name` (string), `month` (int64), `month_name` (string), `day_of_week` (int64), `day_of_year` (int64), `holiday` (string), `ten` (int64), `ten_name` (string), `day_useful_month` (int64), `day_useful_year` (int64), `fone_folha_seq_deman` (int64), `fone_fiscont_seq_deman` (int64), `fone_at_seq_deman` (int64), `chat_folha_seq_deman` (int64), `chat_fiscont_seq_deman` (int64), `chat_at_seq_deman` (int64), `year` (int64), `NomeMes` (string), `NomeMesAbreviado` (string)

## `sgd_alocation_reg`

- **Origem:** Postgres · base `DB_SGD`
- `forecast.de_para_alocacao` ← import-sgd-diario, import-sgd-meiodia (recarga TOTAL)
- `public.sgd_alocation_reg` ← import-sgd-diario (recarga TOTAL)
- **Colunas entregues:** `i_alocation` (int64), `description` (string), `abbreviation` (string), `area` (string), `meio_acesso_alocacao` (string)

SQL nativo:

```sql
SELECT     al.i_alocation, 
        al.description, 
        al.abbreviation,
        (case when a.area = '0' then 'DEMAIS ÁREAS' else upper(a.area) end) as area,
        (case when a.meio_acesso_alocacao = '0' then 'SEM MEIO DE ACESSO' else upper(a.meio_acesso_alocacao) end) as meio_acesso_alocacao
    FROM public.sgd_alocation_reg as al left join forecast.de_para_alocacao as a
                                            on a.i_alocation = al.i_alocation        
                                            
UNION
select 999,'.Sem Alocação','Sem Alocação','SEM ÁREA', 'SEM MEIO DE ACESSO' from generate_series(1,1)
order by 1
```

## `sgd_alocation_historic`

- **Origem:** Postgres · base `DB_SGD`
- `public.sgd_alocation_historic` ← import-sgd-diario (substitui janela de 60 dia(s))
- **Colunas entregues:** `date` (int64), `i_user` (int64), `i_alocation` (int64), `from_of` (int64)

SQL nativo:

```sql
SELECT date, i_user, i_alocation, from_of
    FROM public.sgd_alocation_historic
    
    WHERE date::date >= '2024-01-01' 
    order by 1 asc;
```

## `sgd_bkn_last_backup`

- **Origem:** Postgres · base `DB_SGD_N2`
- `ss.ultimo_backup_bkn` ← não mapeado no Maestro
- **Colunas entregues:** `i_client` (double), `last_backup` (string), `days` (double), `data_record` (int64)

SQL nativo:

```sql
SELECT 
i_client, 
backup, 
days, 
data_record::date
FROM ss.ultimo_backup_bkn
```

## `sgd_cargos`

- **Origem:** Postgres · base `DB_SGD`
- `public.sgd_cargos` ← import-sgd-diario (recarga TOTAL)
- **Colunas entregues:** `i_cargo` (int64), `descricao` (string), `ativo` (int64)

SQL nativo:

```sql
SELECT * FROM public.sgd_cargos
```

## `sgd_client`

- **Origem:** Postgres · base `DB_SGD`
- **Usa outras consultas do fluxo:** `sgd_users`
- `public.protocols` ← plug-queue-realtime
- `public.sgd_client` ← import-sgd-diario (recarga TOTAL)
- `public.sgd_client_observ` ← import-sgd-observacoes (recarga TOTAL)
- `public.sgd_users` ← import-sgd-diario (recarga TOTAL)
- 🔒 **Credencial/infra embutida no SQL** (connection string de `dblink`) — mascarada aqui como `***`. Não copie esse padrão: use foreign server/user mapping ou uma view.
- **Colunas entregues:** `i_client` (int64), `name_client` (string), `date_register` (date), `referential` (string), `cep` (string), `city` (string), `initial_state` (string), `desc_state` (string), `phone` (string), `i_resale` (int64), `name_resale` (string), `type_resale` (string), `situation` (int64), `date_inactivation` (date), `date_signature` (date), `observation` (string), `exist_web_chat` (int64), `i_cms_responsible` (int64), `cms_responsible` (string), `i_cms_manager` (int64), `cms_manager` (string)

SQL nativo:

```sql
SELECT 
        sgd_client.i_client, 
        name_client, 
        date_register, 
        referential, 
        cep, 
        city, 
        initial_state, 
        desc_state, 
        phone, 
        sgd_client.i_resale, 
        name_resale, 
        sgd_client.type_resale, 
        situation, 
        (case when situation = 0 then '' else sgd_client.date_inactivation end ) as date_inactivation,
        date_signature,
        coalesce(obs.observation,'') as observation,        
        (case when webchat_protocols.id_client > 0 then 1 else 0 end) as exist_web_chat,
         sgd_client.i_cms_responsible,
         coalesce(user_respo."name",'') as cms_responsible,
         sgd_client.i_cms_manager,
         coalesce(user_manag."name",'') as cms_manager
    FROM public.sgd_client left join public.sgd_client_observ obs
                              on obs.i_client = sgd_client.i_client
                           LEFT JOIN dblink('dbname=DB_WEBCHAT host=*** user=*** password=***', 
                                    'SELECT distinct id_client FROM public.protocols')
                                    AS webchat_protocols(id_client bigint)
                                    ON sgd_client.i_client = webchat_protocols.id_client
                            left join public.sgd_users as user_respo
                                            on user_respo.i_user = sgd_client.i_cms_responsible
                            left join public.sgd_users as user_manag
                                            on user_manag.i_user = sgd_client.i_cms_manager
                                            
                                            
    where date_register <> ''
```

## `sgd_client_user`

- **Origem:** Postgres · base `DB_SGD`
- `public.sgd_user_client` ← import-sgd-diario (recarga TOTAL)
- **Colunas entregues:** `i_client` (int64), `i_user` (int64), `name_user` (string), `email_user` (string), `date_entry` (date), `situation` (string), `cpf` (string), `date_nasc` (date), `escolaridade` (string), `curso` (string), `forma_trabalho` (string), `total_dias_trabalho` (int64), `YearsOld` (double), `YearsRegistered` (double)

## `sgd_client_phone`

- **Origem:** Postgres · base `DB_SGD`
- `public.sgd_client_contact` ← import-sgd-diario (recarga TOTAL)
- **Colunas entregues:** `i_contact` (int64), `i_client` (int64), `phone_number` (string), `name` (string)

## `sgd_client_product`

- **Origem:** Postgres · base `DB_SGD`
- `public.sgd_product_client` ← import-sgd-diario (recarga TOTAL)
- **Colunas entregues:** `i_contract` (double), `i_product` (double), `date_register` (date), `i_client` (double), `date_ass_cont` (date), `date_ini_serv` (date), `date_fim_serv` (date), `situacao` (string)

SQL nativo:

```sql
SELECT 
            i_contract, 
            i_product, 
            date_register, 
            i_client, 
            date_ass_cont, 
            date_ini_serv, 
            date_fim_serv, 
            (CASE WHEN situ_contract = 1 THEN 'Inativo' else 'Ativo' end ) as situacao
    
FROM public.sgd_product_client
```

## `sgd_config_pref_pesquisas`

- **Origem:** Postgres · base `DB_SGD`
- **Usa outras consultas do fluxo:** `sgd_alocation_historic`
- `public.sgd_alocation_historic` ← import-sgd-diario (substitui janela de 60 dia(s))
- `public.sgd_preferencia_pesquisa` ← import-cts (INSERT sem limpeza (ACUMULA))
- **Colunas entregues:** `data_consulta` (date), `i_usuario` (double), `sistema_config` (string), `modulo_config` (string), `situacao_config` (string), `classificacao_config` (string), `Configuração Completa` (string), `i_alocation` (int64)

SQL nativo:

```sql
SELECT 
        data_consulta, 
        i_usuario, 
        sistema_config, 
        modulo_config, 
        situacao_config, 
        classificacao_config,
        CASE
            WHEN 
                sistema_config <> '' AND
                modulo_config <> '' AND
                situacao_config <> '' AND
                classificacao_config <> ''
                THEN 'Sim'
                ELSE 'Não'
            END AS "Configuração Completa",
         coalesce(h.i_alocation,999) as i_alocation
    FROM public.sgd_preferencia_pesquisa left join public.sgd_alocation_historic h
                                                on h.i_user = i_usuario
                                               and h.date = data_consulta 
                                                
    where sistema_config <> '';
```

## `sgd_product`

- **Origem:** Postgres · base `DB_SGD`
- `public.sgd_product` ← import-sgd-diario (recarga TOTAL)
- **Colunas entregues:** `i_product` (double), `description` (string)

SQL nativo:

```sql
SELECT 
i_product, 
description
FROM public.sgd_product;
```

## `sgd_resales`

- **Origem:** Postgres · base `DB_SGD`
- `public.sgd_resale` ← import-sgd-diario (recarga TOTAL)
- **Colunas entregues:** `i_resale` (int64), `name_resale` (string), `active` (int64), `type_resale` (string), `regiao_atend` (string), `agrupado` (string)

SQL nativo:

```sql
SELECT i_resale, apelido as name_resale, active,
    (case when i_resale IN (3,4,13,14,18,40,74,83,102,137,144,155,156,160,163) then 'Filiais' else 'Revendas' end ) as type_resale,
    (case when i_resale IN (40,102,155,160,163) then 'Campinas' 
           when i_resale IN (1,3,4,13,18,74,83,137,144,156) then 'Sul'
          when i_resale IN (1,148) then 'Interno(UPG-USI)' 
          else 'Demais' end ) as regiao_atend,
( CASE 
    WHEN i_resale IN (57) then '2B'
    WHEN i_resale IN (76) then 'Alpha'
    WHEN i_resale IN (17) then 'Atlas'
    WHEN i_resale IN (41) then 'Campos'
    WHEN i_resale IN (166,85,10) then 'Designer + R&S'
    WHEN i_resale IN (31,67) then 'Gtek SM + XAP'
    WHEN i_resale IN (109) then 'Harv'
    WHEN i_resale IN (5,81) then 'Implantta - AL + SE + PE'
    WHEN i_resale IN (25,54,77,103) then 'J.DREL - MT + AM + ES'
    WHEN i_resale IN (22) then 'Modulo'
    WHEN i_resale IN (18) then 'Moretto'
    WHEN i_resale IN (32) then 'Novo Oeste'
    WHEN i_resale IN (69,152) then 'PC + PC Minas'
    WHEN i_resale IN (7,37,131,140) then 'Soft News - GO + CE + DF'
    WHEN i_resale IN (161,27) then 'Teknordeste PB + RN'
    WHEN i_resale IN (64) then 'Teknorte'
    WHEN i_resale IN (134,36) then 'Tekplan RS + PA'
    WHEN i_resale IN (84,16) then 'Teksul + Sibrum'
    WHEN i_resale IN (51) then 'Tekvale'
    WHEN i_resale IN (63,75) then 'Tool - POO + BHZ'
    WHEN i_resale IN (4) then 'UNCWB'
    WHEN i_resale IN (13) then 'UNPOA'
    WHEN i_resale IN (74) then 'UNRIO'
    WHEN i_resale IN (40) then 'UNSAO - Capital'
    WHEN i_resale IN (160) then 'UNSAO - Interior'
    WHEN i_resale IN (3) then 'UNSC'
    WHEN i_resale IN (1,148) then 'Interno(UPG-USI)'
    
    ELSE '' END ) as agrupado
    FROM public.sgd_resale;
```

## `sgd_ss`

- **Origem:** Postgres · base `DB_SGD_N2`
- `ss.date_entry` ← não mapeado no Maestro
- `ss.html` ← não mapeado no Maestro
- `ss.i_classification` ← não mapeado no Maestro
- `ss.i_dissatisfied_reason` ← não mapeado no Maestro
- `ss.i_module` ← não mapeado no Maestro
- `ss.i_resales` ← não mapeado no Maestro
- `ss.i_satisfaction` ← não mapeado no Maestro
- `ss.i_situacao` ← não mapeado no Maestro
- `ss.i_ss` ← não mapeado no Maestro
- `ss.i_subtopic` ← não mapeado no Maestro
- `ss.i_system` ← não mapeado no Maestro
- `ss.i_topc` ← não mapeado no Maestro
- `ss.i_userreasales` ← não mapeado no Maestro
- `ss.last_update` ← não mapeado no Maestro
- `ss.ss` ← import-sgd-diario (substitui janela de SS_DIAS dia(s) (default 31))
- `ss.ss_classification` ← import-sgd-diario (recarga TOTAL)
- `ss.ss_disregard_dissatisfaction` ← import-sgd-diario (recarga TOTAL)
- `ss.ss_module` ← import-sgd-diario (recarga TOTAL)
- `ss.ss_sub_topic` ← import-sgd-diario (recarga TOTAL)
- `ss.ss_system` ← import-sgd-diario (recarga TOTAL)
- `ss.ss_topic` ← import-sgd-diario (recarga TOTAL)
- `ss.ss_tramites` ← import-sgd-diario (substitui janela de 5 dia(s))
- `ss.ss_tramites_time` ← import-sgd-diario (recarga TOTAL)
- **Colunas entregues:** `i_ss` (int64), `date_entry_int` (int64), `date_entry` (date), `_interval` (string), `time_entry` (time), `classification` (string), `system` (string), `module` (string), `subtopic` (string), `topic` (string), `i_satisfaction` (int64), `i_dissatisfied_reason` (int64), `i_userreasales` (int64), `i_resales` (int64), `i_situacao` (int64), `last_date_update_int` (int64), `last_date_update` (date), `_time_without_analysis` (int64), `i_user_last_responsible` (int64), `last_time_update` (time), `disregarddissatisfaction` (int64)

SQL nativo:

```sql
SELECT 
            ss.i_ss, 
            ss.date_entry::date as date_entry, 
            ss.date_entry::time as time_entry,
            to_char(date_trunc('hour', ss.date_entry::time ) + 
            CASE 
                WHEN EXTRACT(MINUTE FROM ss.date_entry::time ) < 30 THEN interval '0 minutes'
                ELSE interval '30 minutes'
            END, 'HH24:MI') as _interval,
            coalesce(ss_classification.description,'') as classification, 
            coalesce(ss_system.description,'') as system,
            coalesce(ss_module.description,'') as module,
            coalesce(ss_topic.description,'') as topic,
            coalesce(ss_sub_topic.description,'') as subTopic,
            ss.i_satisfaction, 
            ss.i_dissatisfied_reason, 
            ss.i_userreasales, 
            ss.i_resales, 
            ss.i_situacao, 
            ss.last_update::date as last_date_update,
            ss.last_update::timetz as last_time_update,
            --CONCAT('https://sgd.dominiosistemas.com.br/sgsa/faces/ss.html?ss=', ss.i_ss, '&visualizarSSOutrasUnidades=true') as link_ss
            CASE WHEN d.i_response IS NOT NULL THEN 1 ELSE 0 END AS disregardDissatisfaction,
            coalesce(tram."time",0) as _time_without_analysis,
            coalesce( (select tram_use.i_user 
                        FROM ss.ss_tramites as tram_use 
                       WHERE tram_use.i_ss = ss.i_ss
                         and tram_use.situation = 3
                         order by tram_use.i_ss_tram desc 
                         limit 1)
                        ,0) as i_user_last_responsible
            
    FROM ss.ss inner join ss.ss_classification
                       on ss_classification.i_ss_classification = ss.i_classification
               inner join ss.ss_system 
                       on ss_system.i_system = ss.i_system
               inner join ss.ss_module
                       on ss_module.i_system = ss.i_system
                      and ss_module.i_modules = ss.i_module
                left join ss.ss_topic
                          on ss_topic.i_system = ss.i_system
                      and ss_topic.i_module = ss.i_module
                      and ss_topic.i_topic = ss.i_topc
                left join ss.ss_sub_topic
                       on ss_sub_topic.i_topic_suport = ss.i_topc
                      and ss_sub_topic.i_origens = ss.i_subtopic
                left join ss.ss_disregard_dissatisfaction as d
                       on d.i_ss::int = ss.i_ss
                left join  ss.ss_tramites_time as tram 
                               on tram.i_ss = ss.i_ss
                              and tram.i_ss_tram = 0

order by ss.date_entry asc
```

## `sgd_ss_category`

- **Origem:** Postgres · base `DB_SGD_N2`
- `ss.ss_category` ← import-sgd-diario (recarga TOTAL)
- **Colunas entregues:** `i_ss_category` (int64), `category_name` (string), `description` (string)

SQL nativo:

```sql
SELECT 
    i_ss_category, 
    category_name, 
    description
FROM ss.ss_category
```

## `sgd_ss_classification`

- **Origem:** Postgres · base `DB_SGD_N2`
- `ss.ss_classification` ← import-sgd-diario (recarga TOTAL)
- **Colunas entregues:** `i_ss_classification` (int64), `description` (string)

SQL nativo:

```sql
SELECT 
        i_ss_classification, 
        description
FROM ss.ss_classification
```

## `sgd_ss_tramite`

- **Origem:** Postgres · base `DB_SGD_N2`
- `ss.ss_tramites` ← import-sgd-diario (substitui janela de 5 dia(s))
- `ss.ss_tramites_time` ← import-sgd-diario (recarga TOTAL)
- **Colunas entregues:** `i_ss` (int64), `i_ss_tram` (int64), `date_tram` (date), `_interval` (string), `date_tram_int` (int64), `hour_tram` (time), `situation` (int64), `i_user` (int64), `typeforwarding` (int64), `dateanalysisforwarding` (string), `i_userforwarding` (int64), `_timetram` (int64), `i_category` (int64), `seq_interacao` (int64), `sla_interacao` (string), `sla_interacao_minutos` (int64), `sla_n3` (string), `sla_tme` (string), `exists_requestsql` (string), `is_first_tram_user` (string)

SQL nativo:

```sql
select 
        ss_tramites.i_ss, 
        ss_tramites.i_ss_tram, 
        date_tram,
        to_char(date_trunc('hour', date_tram::time ) + 
            CASE 
                WHEN EXTRACT(MINUTE FROM date_tram::time ) < 30 THEN interval '0 minutes'
                ELSE interval '30 minutes'
            END, 'HH24:MI') as _interval,
        situation, 
        i_user, 
        typeforwarding, 
        dateanalysisforwarding, 
        i_userforwarding, 
        (case when exists_requestsql = 1 then 'Sim' else 'Não' END) as exists_requestsql,
        (case when 
        (
            (select f.i_ss_tram from  ss.ss_tramites as f where ss.ss_tramites.i_ss = f.i_ss 
                                                                 and ss.ss_tramites.i_user = f.i_user
                                                                and ss.ss_tramites.situation = f.situation
                                                                order by f.i_ss_tram asc limit 1 ) = ss.ss_tramites.i_ss_tram )
        then 'Sim' else 'Não' end) as is_first_tram_user,
        coalesce(tram."time",0) as _timeTram,
        coalesce(i_category,0) as i_category,
        CASE 
                WHEN ss_tramites.sla_interacao IS NOT NULL AND ss_tramites.sla_interacao <> '' 
                THEN COUNT(*) FILTER (WHERE ss_tramites.sla_interacao IS NOT NULL AND ss_tramites.sla_interacao <> '') 
                     OVER (PARTITION BY ss_tramites.i_ss ORDER BY ss_tramites.date_tram ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW)
                ELSE NULL 
            END AS seq_interacao,
        coalesce(ss_tramites.sla_interacao,''),
        CASE 
            WHEN ss_tramites.sla_interacao IS NOT NULL AND ss_tramites.sla_interacao <> '' THEN
                EXTRACT(EPOCH FROM ss_tramites.sla_interacao::INTERVAL)::INTEGER/60
            ELSE NULL 
            END AS sla_interacao_minutos,
        coalesce(ss_tramites.sla_n3,''), 
        coalesce(ss_tramites.sla_tme,'')

    
    from ss.ss_tramites left join  ss.ss_tramites_time as tram 
                               on tram.i_ss = ss_tramites.i_ss
                              and tram.i_ss_tram = ss_tramites.i_ss_tram
    
    order by i_ss, i_ss_tram
```

## `sgd_ss_dissatisfied_conclusion_text`

- **Origem:** Postgres · base `DB_SGD_N2`
- `ss.ss_conclusion_text` ← import-sgd-diario (substitui janela de 5 dia(s))
- **Colunas entregues:** `i_ssc` (double), `dateconclusion` (int64), `description` (string)

SQL nativo:

```sql
SELECT 
    i_ssc, 
    dateconclusion::date, 
    description
FROM ss.ss_conclusion_text
```

## `sgd_ss_dissatisfied_reason`

- **Origem:** Postgres · base `DB_SGD_N2`
- `ss.ss_dissatisfied_reason` ← não mapeado no Maestro
- **Colunas entregues:** `i_reason` (int64), `description` (string)

SQL nativo:

```sql
SELECT 
i_reason, 
description

FROM ss.ss_dissatisfied_reason
```

## `sgd_ss_dissatisfied_description`

- **Origem:** Postgres · base `DB_SGD_N2`
- `ss.ss_satisfaction_description` ← não mapeado no Maestro
- **Colunas entregues:** `i_satisfaction` (int64), `description` (string)

SQL nativo:

```sql
SELECT 
    i_satisfaction, 
    description
FROM ss.ss_satisfaction_description
```

## `sgd_ss_forwarding`

- **Origem:** Postgres · base `DB_SGD_N2`
- `ss.i_classification` ← não mapeado no Maestro
- `ss.i_resales` ← não mapeado no Maestro
- `ss.i_ss` ← não mapeado no Maestro
- `ss.ss` ← import-sgd-diario (substitui janela de SS_DIAS dia(s) (default 31))
- `ss.ss_situation` ← import-sgd-diario (recarga TOTAL)
- `ss.ss_tramites` ← import-sgd-diario (substitui janela de 5 dia(s))
- **Colunas entregues:** `i_ss` (int64), `i_classificacao` (int64), `data_encaminhamento` (int64), `i_user_responsavel_encaminhamento` (int64), `i_ss_tramites` (int64), `situacao` (string), `pendencia` (string), `i_resale` (int64), `existe_texto_requestsql` (string)

SQL nativo:

```sql
SELECT  ss.i_ss as i_ss
        ,ss.i_classification as i_classificacao
       ,min(tram.date_tram) as data_encaminhamento       
       ,tram.i_user as i_user_responsavel_encaminhamento
       ,tram.i_ss_tram as i_ss_tramites
       ,ss_situation.description as situacao
       ,ss_situation.pending as pendencia
       ,ss.i_resales as i_resale
       ,coalesce((SELECT 'Sim' 
                    FROM ss.ss_tramites AS ss_tram 
                    WHERE ss_tram .i_ss = ss.i_ss  
                    AND ss_tram .exists_requestsql=1
                        limit 1),'Não') AS existe_texto_requestsql
       
                    
  FROM ss.ss as ss join ss.ss_tramites as tram
                   on ss.i_ss = tram.i_ss
                  --and "SGD_ss_tramites"."situation" in(6)
                 --and "SGD_ss".i_ss = 841542
                  and tram.i_ss_tram = (select tr.i_ss_tram from ss.ss_tramites as tr
                                                                   where tr.i_ss = tram.i_ss
                                                                 --and tr.situation = "SGD_ss_tramites".situation
                                                                    and tr.situation IN(8,23,27,31)
                                                               order by tr.i_ss_tram asc limit 1)

                                            
                                             
                                  join ss.ss_situation as ss_situation
                                              on tram.situation = ss_situation.i_situation
                                                                            


group by ss.i_ss
      ,ss.i_classification
      ,tram.date_tram
      ,tram.i_user
      ,tram.i_ss_tram
      ,ss_situation.description
      ,ss_situation.pending    
      ,ss.i_resales
      
UNION

 SELECT  ss.i_ss as i_ss
        ,ss.i_classification as i_classificacao
       ,min(tram.date_tram) as data_encaminhamento       
       ,tram.i_user as i_user_responsavel_encaminhamento
       ,tram.i_ss_tram as i_ss_tramites
       ,ss_situation.description as situacao
       ,ss_situation.pending as pendencia
       ,ss.i_resales as i_resale
       ,coalesce((SELECT 'Sim' 
                    FROM ss.ss_tramites AS ss_tram 
                    WHERE ss_tram .i_ss = ss.i_ss  
                    AND ss_tram .exists_requestsql=1
                        limit 1),'Não') AS existe_texto_requestsql
       
                    
  FROM ss.ss as ss join ss.ss_tramites as tram
                   on ss.i_ss = tram.i_ss
                  --and "SGD_ss_tramites"."situation" in(6)
                 --and "SGD_ss".i_ss = 841542
                  and tram.i_ss_tram = (select tr.i_ss_tram from ss.ss_tramites as tr
                                                                   where tr.i_ss = tram.i_ss
                                                                 --and tr.situation = "SGD_ss_tramites".situation
                                                                    and tr.situation IN(6)
                                                               order by tr.i_ss_tram asc limit 1)

                                            
                                             
                                  join ss.ss_situation as ss_situation
                                              on tram.situation = ss_situation.i_situation
                                                                            


group by ss.i_ss
      ,ss.i_classification
      ,tram.date_tram
      ,tram.i_user
      ,tram.i_ss_tram
      ,ss_situation.description
      ,ss_situation.pending    
      ,ss.i_resales
```

## `sgd_ss_pendency`

- **Origem:** Postgres · base `DB_SGD_N2`
- `ss.i_classification` ← não mapeado no Maestro
- `ss.i_ss` ← não mapeado no Maestro
- `ss.ss` ← import-sgd-diario (substitui janela de SS_DIAS dia(s) (default 31))
- `ss.ss_pendency` ← import-sgd-diario (INSERT sem limpeza (ACUMULA))
- **Colunas entregues:** `i_ss` (int64), `ddate` (int64), `ddatetime` (time), `i_user` (int64), `i_ss_tramites` (int64), `i_ss_situation` (int64), `pending` (string), `i_classification` (int64)

SQL nativo:

```sql
SELECT p.i_ss, 
       p.ddate,
       p.ddatetime, 
       p.i_user, 
       p.i_ss_tramites, 
       p.i_ss_situation, 
       p.pending,
       ss.i_classification
      
     FROM ss.ss_pendency as p left join ss.ss as ss 
                              on ss.i_ss = p.i_ss
     where p.ddate >='2023-01-01'
     order by 2 asc;
```

## `sgd_ss_pendency_time`

- **Origem:** Postgres · base `DB_SGD_N2`
- `ss.ss_situation` ← import-sgd-diario (recarga TOTAL)
- `ss.ss_tramites` ← import-sgd-diario (substitui janela de 5 dia(s))
- `ss.ss_tramites_time` ← import-sgd-diario (recarga TOTAL)
- **Colunas entregues:** `i_ss` (int64), `sequential_iteraction` (int64), `total_time` (double), `date_iteraction` (dateTime), `iteracao_open` (int64)

SQL nativo:

```sql
WITH base_data AS (
    SELECT 
        a.i_ss,
        a.i_ss_tram, 
        a."time",
        t.situation,
        t.date_tram,
        COALESCE(s.pending, 'N/A') AS pending
    FROM 
        ss.ss_tramites_time AS a
    LEFT JOIN 
        ss.ss_tramites AS t ON t.i_ss = a.i_ss AND t.i_ss_tram = a.i_ss_tram
    LEFT JOIN 
        ss.ss_situation AS s ON s.i_situation = t.situation
),
interaction_groups AS (
    SELECT 
        i_ss,
        i_ss_tram,
        "time",
        situation,
        date_tram,
        pending,
        CASE 
            WHEN i_ss_tram = 0 THEN 1
            WHEN pending = 'N2' THEN 0
            ELSE 1
        END AS group_reset,
        SUM(CASE 
                WHEN i_ss_tram = 0 THEN 1 
                WHEN pending = 'N2' THEN 0 
                ELSE 1 
            END) OVER (PARTITION BY i_ss ORDER BY i_ss_tram ROWS UNBOUNDED PRECEDING) AS interaction_group
    FROM 
        base_data
),
adjusted_groups AS (
    SELECT 
        i_ss,
        i_ss_tram,
        "time",
        situation,
        pending,
        date_tram,
        CASE 
            WHEN i_ss_tram = 0 THEN interaction_group - 1
            ELSE interaction_group
        END AS adjusted_group,
        LAST_VALUE(date_tram) OVER (PARTITION BY i_ss, CASE WHEN i_ss_tram = 0 THEN interaction_group - 1 ELSE interaction_group END ORDER BY i_ss_tram ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) AS last_date_tram
    FROM 
        interaction_groups
),
summed_groups AS (
    SELECT 
        i_ss,
        adjusted_group,
        SUM("time") AS total_time,
        MAX(last_date_tram) AS last_date_tram
    FROM 
        adjusted_groups
    WHERE 
        pending = 'N2' OR i_ss_tram = 0
    GROUP BY 
        i_ss, adjusted_group
),
final_groups AS (
    SELECT 
        i_ss,
        CASE 
            WHEN row_number() OVER (PARTITION BY i_ss ORDER BY adjusted_group) <= 2 THEN 1
            ELSE adjusted_group
        END AS consolidated_group,
        total_time,
        last_date_tram
    FROM 
        summed_groups
),
consolidated_final_groups AS (
    SELECT 
        i_ss,
        consolidated_group,
        SUM(total_time) AS total_time,
        MAX(last_date_tram) AS last_date_tram,
        ROW_NUMBER() OVER (PARTITION BY i_ss ORDER BY consolidated_group) AS new_interaction_group
    FROM 
        final_groups
    GROUP BY 
        i_ss, consolidated_group
),
last_n2 AS (
    SELECT 
        i_ss,
        MAX(i_ss_tram) AS last_n2_tram
    FROM 
        base_data
    WHERE 
        pending = 'N2'
    GROUP BY 
        i_ss
),
last_tram AS (
    SELECT 
        i_ss,
        MAX(i_ss_tram) AS last_tram
    FROM 
        base_data
    GROUP BY 
        i_ss
)
SELECT 
    cfg.i_ss,
    cfg.new_interaction_group AS interaction_group,
    cfg.total_time,
    cfg.last_date_tram,
    CASE 
        WHEN cfg.new_interaction_group = MAX(cfg.new_interaction_group) OVER (PARTITION BY cfg.i_ss) 
             AND lt.last_tram = ln.last_n2_tram THEN 1
        ELSE 0
    END AS last_pending_is_n2
FROM 
    consolidated_final_groups cfg
LEFT JOIN 
    last_n2 ln ON cfg.i_ss = ln.i_ss
LEFT JOIN 
    last_tram lt ON cfg.i_ss = lt.i_ss
--WHERE 
--    cfg.i_ss IN (887700,909506)
ORDER BY 
    cfg.i_ss, cfg.new_interaction_group;
```

## `sgd_ss_situation`

- **Origem:** Postgres · base `DB_SGD_N2`
- `ss.ss_situation` ← import-sgd-diario (recarga TOTAL)
- **Colunas entregues:** `i_situation` (int64), `description` (string), `pending` (string)

SQL nativo:

```sql
SELECT 
    i_situation,
    description, 
    pending
FROM ss.ss_situation
```

## `sgd_ssc`

- **Origem:** Postgres · base `DB_SGD`
- **Usa outras consultas do fluxo:** `sgd_alocation_historic`, `sgd_client`, `sgd_ssc_disregard_dissatisfaction`, `sgd_ssc_tramites`
- `public.sgd_alocation_historic` ← import-sgd-diario (substitui janela de 60 dia(s))
- `public.sgd_client` ← import-sgd-diario (recarga TOTAL)
- `public.sgd_ssc` ← import-sgd-diario (substitui janela de 5 dia(s))
- `public.sgd_ssc_disregard_dissatisfaction` ← import-sgd-diario (recarga TOTAL)
- `public.sgd_ssc_tramites` ← import-sgd-diario (substitui janela de 3 dia(s))
- **Colunas entregues:** `code_ssc` (int64), `i_ssc` (int64), `date_entry` (date), `date_time` (dateTime), `i_classification` (int64), `system` (string), `module` (string), `topic` (string), `subtopic` (string), `i_means_of_access` (int64), `lista_ss` (string), `i_clientes` (int64), `i_user` (int64), `total_procedures_waiting_answer` (int64), `total_procedures` (int64), `time_before_first_analysis` (int64), `time_total` (int64), `time_medium` (int64), `dateconclusion` (date), `time_ss` (int64), `time_ssql` (int64), `bond_sa_ne` (int64), `disapproval` (date), `time_bond_sa_ne` (int64), `time_phone` (int64), `time_final_support` (int64), `time_final_client` (int64), `time_last_procedure_without_analysis` (int64), `number_procedure_conclusion` (int64), `satisfaction_ssc` (string), `i_ssc_satisfaction_reason` (int64), `i_user_resales` (int64), `number_procedure_attachement` (int64), `bond_attachment_sa_ne` (int64), `time_scd` (int64), `priority` (int64), `no_acess_system` (int64), `dtime` (string), `ia_register` (double), `disregarddissatisfaction` (int64), `aux_i_means_of_access` (int64), `i_alocation` (int64), `first_user` (int64), `i_resales` (int64), `link_url` (string)

SQL nativo:

```sql
SELECT DISTINCT
    r.*,
    CASE WHEN d.i_response IS NOT NULL THEN 1 ELSE 0 END AS disregardDissatisfaction,
    COALESCE(st.i_ssc_situation, r.i_means_of_access) AS aux_i_Means_of_Access,
    COALESCE(h.i_alocation, 999) AS i_alocation,
    COALESCE(tram.i_user, 0) AS first_user,
    cli.i_resale AS i_resales
FROM public.sgd_ssc AS r
    INNER JOIN public.sgd_client AS cli ON cli.i_client = r.i_clientes
    AND r.date_entry::date >= '2024-01-01'::date
    LEFT JOIN public.sgd_ssc_disregard_dissatisfaction AS d 
        ON r.i_ssc = d.i_ssc_ss_chat::INT AND d.type = 'SSC'
    LEFT JOIN public.sgd_ssc_tramites AS st 
        ON st.i_ssc = r.i_ssc AND st.i_ssc_situation = 1
    LEFT JOIN public.sgd_alocation_historic AS h 
        ON h.i_user = r.i_user AND h.date::date = r.date_entry::date
    LEFT JOIN LATERAL (
        SELECT i_user
        FROM public.sgd_ssc_tramites
        WHERE i_ssc = r.i_ssc
          AND i_ssc_situation  IN (2, 3, 5,14,38)
          AND i_user != 1078032
        ORDER BY i_ssc_tramites
        LIMIT 1
    ) AS tram ON true
```

## `sgd_ssc_answer_time`

- **Origem:** Postgres · base `DB_SGD`
- **Usa outras consultas do fluxo:** `sgd_ssc`
- `public.sgd_ssc` ← import-sgd-diario (substitui janela de 5 dia(s))
- `public.sgd_ssc_answer_time` ← import-sgd-diario (INSERT sem limpeza (ACUMULA))
- **Colunas entregues:** `i_ssc` (int64), `i_user` (int64), `datewithoutanalysis` (int64), `datewaitinganswer` (int64), `timesupport` (int64), `timess` (int64), `timessql` (int64), `timeconversao` (int64), `timesr` (int64), `timewithoutanalysis` (int64), `firstprocedure` (string), `i_client` (int64), `i_means_of_access` (int64), `i_classification` (int64), `system` (string), `module` (string), `topic` (string), `subtopic` (string)

SQL nativo:

```sql
SELECT 
a.i_ssc, 
a.i_user, 
a.datewithoutanalysis,
a.datewaitinganswer, 
a.timesupport, 
a.timess, 
a.timessql, 
a.timeconversao, 
a.timesr, 
a.timewithoutanalysis, 
a.firstprocedure, 
a.i_client,
sgd_ssc.i_means_of_access,
sgd_ssc.i_classification,
sgd_ssc."system",
sgd_ssc.module,
sgd_ssc.topic,
sgd_ssc.subtopic
FROM public.sgd_ssc_answer_time as a left join public.sgd_ssc 
                                                on sgd_ssc.i_ssc = a.i_ssc
                                            and sgd_ssc.date_entry::date >= '2024-01-01'::date
```

## `sgd_ssc_classification`

- **Origem:** Postgres · base `DB_SGD`
- `public.sgd_ssc_classification` ← import-sgd-diario (recarga TOTAL)
- **Colunas entregues:** `i_classification` (int64), `desription` (string)

## `sgd_ssc_disregard_dissatisfaction`

- **Origem:** Postgres · base `DB_SGD`
- `public.sgd_ssc_disregard_dissatisfaction` ← import-sgd-diario (recarga TOTAL)
- **Colunas entregues:** `i_response` (int64), `i_ssc_ss_chat` (int64), `justif` (string), `date` (date), `time` (time), `email` (string)

SQL nativo:

```sql
SELECT i_response, 
            i_ssc_ss_chat, 
            justif, 
            date_incl as date, 
            date_incl as time, 
            email
    FROM public.sgd_ssc_disregard_dissatisfaction

where type = 'SSC'
```

## `sgd_ssc_dissatisfaction_historic`

- **Origem:** Postgres · base `DB_SGD`
- `public.sgd_ssc_dissatisfaction_historic` ← import-sgd-diario (substitui janela de 30 dia(s))
- **Colunas entregues:** `i_ssc` (int64), `text_dissatisfaction` (string), `allow_contact` (string), `conclusion_date` (date)

## `sgd_ssc_internal_time`

- **Origem:** Postgres · base `DB_SGD`
- **Usa outras consultas do fluxo:** `sgd_ssc`
- `public.sgd_ssc` ← import-sgd-diario (substitui janela de 5 dia(s))
- `public.sgd_ssc_internal_time` ← import-sgd-diario (substitui janela de 5 dia(s))
- **Colunas entregues:** `i_ssc` (int64), `i_ssc_tramites` (int64), `datewaitinganswer` (date), `dateanswered` (date), `category` (string), `i_userrequest` (int64), `i_userresponsible` (int64), `timeanswer` (int64), `i_means_of_access` (int64), `i_classification` (int64), `system` (string), `module` (string), `topic` (string), `subtopic` (string), `i_clientes` (int64)

SQL nativo:

```sql
SELECT 
a.i_ssc, 
a.i_ssc_tramites, 
a.datewaitinganswer, 
a.dateanswered, 
a.category, 
a.i_userrequest, 
a.i_userresponsible, 
a.timeanswer,
sgd_ssc.i_means_of_access,
sgd_ssc.i_classification,
sgd_ssc."system",
sgd_ssc.module,
sgd_ssc.topic,
sgd_ssc.subtopic,
sgd_ssc.i_clientes
FROM public.sgd_ssc_internal_time as a left join public.sgd_ssc 
                                                on sgd_ssc.i_ssc = a.i_ssc
```

## `sgd_ssc_means_access`

- **Origem:** Json.Document, Table.FromRows
- **Colunas entregues:** `i_means_access` (int64), `descricao` (string)

## `sgd_ssc_pendency`

- **Origem:** Postgres · base `DB_SGD`
- `public.sgd_pendency` ← import-sgd-diario (INSERT sem limpeza (ACUMULA)); import-sgd-diario (UPDATE no lugar)
- **Colunas entregues:** `i_ssc` (int64), `date` (date), `i_user` (int64), `i_ssc_tramites` (int64), `i_ssc_situation` (int64), `i_ss` (int64), `i_ssql` (int64), `i_sr` (int64), `i_conversoes` (int64), `n1_pendency` (int64), `n2_pendency` (int64), `sector_pendency` (int64), `i_clientes` (int64), `i_meios_acesso` (int64), `i_meios_retorno` (int64), `i_sss_classificacoes` (int64), `system` (string), `module` (string), `topic` (string), `entry` (string), `pendency_days` (int64), `useful_pendency_days_n1` (int64), `useful_pendency_days_n2` (int64), `subtopic` (string)

## `sgd_ssc_pesquisa_resposta_utiliza_solucao`

- **Origem:** Postgres · base `DB_SGD`
- `public.sgd_ssc_utiliza_solucao` ← import-sgd-diario (substitui janela de 5 dia(s))
- **Colunas entregues:** `seq` (int64), `i_ssc` (int64), `i_user` (int64), `opcao_utilizada` (string), `origem_resposta` (string), `destino` (string), `alterou_texto` (string), `data_int` (int64)

SQL nativo:

```sql
SELECT 
        seq,
        i_ssc, 
        i_user, 
        (case when opcao_utilizada = 1 then 'Pesquisar Resposta' 
                when opcao_utilizada = 2 then 'Utilizar Solução' 
              
           when opcao_utilizada = 3 then 'Utilizar Solução - SSC gravada' 
               else '-' END) as opcao_utilizada, 
        (case when origem_resposta = 1 then 'SSC' 
               when origem_resposta = 2 then 'Solução' 
               else '-' END) as origem_resposta, 
              
        (case when destino = 1 then 'Gerado no Cadastro'
               when destino = 2 then 'Gerado na Visualização da SSC'
              else '-' END) as destino, 
              
        (case when alterou_texto = 1 then 'Sim'
              when alterou_texto = 0 then 'Não'
              else '-' END ) as alterou_texto ,
        data_hora::timestamp as data_
    FROM public.sgd_ssc_utiliza_solucao order by data_hora desc;
```

## `sgd_ssc_reason_dissatisfaction`

- **Origem:** Postgres · base `DB_SGD`
- `public.sgd_ssc_reason_dissatisfaction` ← não mapeado no Maestro
- **Colunas entregues:** `i_ssc_satisfaction_reason` (int64), `description` (string)

## `sgd_ssc_sa`

- **Origem:** Postgres · base `DB_SGD`
- `public.sgd_ssc_sa` ← import-sgd-diario (recarga TOTAL)
- **Colunas entregues:** `i_ssc` (int64), `i_resale` (int64), `i_sa_ne` (int64)

## `sgd_ssc_situation`

- **Origem:** Postgres · base `DB_SGD`
- `public.sgd_ssc_situation` ← import-sgd-diario (recarga TOTAL)
- **Colunas entregues:** `i_ssc_situation` (int64), `description` (string)

## `sgd_ssc_soses`

- **Origem:** Postgres · base `DB_SGD`
- `public.sgd_soses` ← import-sgd-diario (recarga TOTAL)
- **Colunas entregues:** `i_ssc` (int64), `tipo_servico` (string), `duracao` (int64), `valor_total` (double), `parcelas` (int64), `vencimento` (date), `autorizacao` (date), `exclusao` (date), `entregue` (int64), `prazo_anterior` (int64), `situacao` (string), `data_emissao` (date), `link_url` (string)

## `sgd_ssc_text_conclusion`

- **Origem:** Postgres · base `DB_SGD`
- `public.sgd_ssc_text_conclusion` ← import-sgd-diario (substitui janela de 5 dia(s))
- **Colunas entregues:** `i_ssc` (double), `date` (date), `conclusion_date` (dateTime), `description` (string)

## `sgd_ssc_tramites`

- **Origem:** Postgres · base `DB_SGD`
- `public.sgd_ssc_tramites` ← import-sgd-diario (substitui janela de 3 dia(s))
- **Colunas entregues:** `i_ssc` (int64), `i_ssc_tramites` (int64), `entry` (date), `entry_date_time` (dateTime), `i_ssc_situation` (int64), `i_user` (int64), `tipo_resposta` (string), `i_visualizado` (string), `data_visualizacao` (string), `existe_texto_web` (string)

## `sgd_ssc_vs_genesys`

- **Origem:** Postgres · base `DB_SGD`
- `public.sgd_genesys` ← import-sgd-diario (substitui janela de 5 dia(s))
- **Colunas entregues:** `i_ssc` (int64), `cadastro_ia` (int64), `tags` (string), `conversation_id` (string)

SQL nativo:

```sql
SELECT 
        i_ssc, 
        cadastro_ia, 
        tags, 
        conversation_id
    FROM public.sgd_genesys
```

## `sgd_schedule_absences_reason`

- **Origem:** Postgres · base `DB_SGD`
- `public.sgd_schedule_absences_reason` ← import-sgd-diario (recarga TOTAL)
- **Colunas entregues:** `i_absences_reason` (int64), `description` (string), `active` (string), `i_schedule_type` (int64)

## `sgd_schedule_absences_type`

- **Origem:** Postgres · base `DB_SGD`
- `public.sgd_schedule_absences_type` ← import-sgd-diario (recarga TOTAL)
- **Colunas entregues:** `i_schedule_type` (int64), `description` (string), `area` (int64)

## `sgd_schedule`

- **Origem:** Postgres · base `DB_SGD`
- **Usa outras consultas do fluxo:** `sgd_alocation_historic`
- `public.sgd_alocation_historic` ← import-sgd-diario (substitui janela de 60 dia(s))
- `public.sgd_schedule` ← import-agendas (substitui janela de 60 dia(s))
- **Colunas entregues:** `date` (int64), `i_user` (int64), `i_type` (int64), `responsible` (string), `i_absences_reason` (int64), `minutes` (int64), `minutes_old` (int64), `data_hora_ini` (string), `data_hora_fim` (string), `description` (string), `i_alocation` (int64)

SQL nativo:

```sql
SELECT s.date, 
        s.i_user, 
        s.i_type, 
        s.responsible, 
        s.i_absences_reason, 
        LEAST(480,  
        (CASE    
            -- Se algum dos campos for NULL ou vazio, retorna NULL    
            WHEN s.data_hora_ini IS NULL     
                 OR s.data_hora_fim IS NULL     
                 OR s.data_hora_ini::text = ''     
                 OR s.data_hora_fim::text = '' THEN    
                480
                
            -- Se o período não cruza o horário de almoço    
            WHEN s.data_hora_fim::time < '12:00:00'::time     
                 OR s.data_hora_ini::time >= '13:30:00'::time THEN    
                EXTRACT(EPOCH FROM (s.data_hora_fim::time - s.data_hora_ini::time)) / 60
                
            -- Se cruza completamente o horário de almoço (início antes das 12h e fim depois das 13:30)    
            WHEN s.data_hora_ini::time < '12:00:00'::time     
                 AND s.data_hora_fim::time > '13:30:00'::time THEN    
                EXTRACT(EPOCH FROM (s.data_hora_fim::time - s.data_hora_ini::time)) / 60 - 90
                
            -- Se início é antes das 12h e fim é entre 12h e 13:30    
            WHEN s.data_hora_ini::time < '12:00:00'::time     
                 AND s.data_hora_fim::time >= '12:00:00'::time     
                 AND s.data_hora_fim::time <= '13:30:00'::time THEN    
                EXTRACT(EPOCH FROM ('12:00:00'::time - data_hora_ini::time)) / 60
                
            -- Se início é entre 12h e 13:30 e fim é depois das 13:30    
            WHEN s.data_hora_ini::time >= '12:00:00'::time     
                 AND s.data_hora_ini::time < '13:30:00'::time     
                 AND s.data_hora_fim::time >= '13:30:00'::time THEN    
                EXTRACT(EPOCH FROM (s.data_hora_fim::time - '13:30:00'::time)) / 60
                
            -- Se início e fim estão dentro do horário de almoço    
            WHEN s.data_hora_ini::time >= '12:00:00'::time     
                 AND s.data_hora_fim::time <= '13:30:00'::time THEN    
                0
                
            ELSE     
                EXTRACT(EPOCH FROM (s.data_hora_fim::time - s.data_hora_ini::time)) / 60    
        END)  
    )::int AS minutes,
        s.minutes as minutes_old,
        s.data_hora_ini,   
        s.data_hora_fim, 
        s.description,
        coalesce(h.i_alocation,999) as i_alocation
    
    
    FROM public.sgd_schedule as s LEFT JOIN public.sgd_alocation_historic as h 
                                         on h.i_user = s.i_user 
                                        AND s.date::date = h.date::date order by s.date::date desc
```

## `sgd_schedule_past_future`

- **Origem:** Postgres · base `DB_SGD`
- `public.sgd_schedule_past_future` ← import-agendas (substitui janela de 60 dia(s)); import-agendas (substitui janela de 90 dia(s))
- **Colunas entregues:** `date` (int64), `i_user` (int64), `i_type` (int64), `responsible` (string), `i_absences_reason` (int64), `minutes` (int64), `description` (string), `data_hora_ini` (string), `data_hora_fim` (string)

SQL nativo:

```sql
SELECT date, i_user, i_type, responsible, i_absences_reason, minutes, description, data_hora_ini, data_hora_fim
    FROM public.sgd_schedule_past_future;

SELECT  s.date, 
        s.i_user, 
        s.i_type, 
        s.responsible, 
        s.i_absences_reason, 
        LEAST(480,  
        (CASE    
            -- Se algum dos campos for NULL ou vazio, retorna NULL    
            WHEN s.data_hora_ini IS NULL     
                 OR s.data_hora_fim IS NULL     
                 OR s.data_hora_ini::text = ''     
                 OR s.data_hora_fim::text = '' THEN    
                480
                
            -- Se o período não cruza o horário de almoço    
            WHEN s.data_hora_fim::time < '12:00:00'::time     
                 OR s.data_hora_ini::time >= '13:30:00'::time THEN    
                EXTRACT(EPOCH FROM (s.data_hora_fim::time - s.data_hora_ini::time)) / 60
                
            -- Se cruza completamente o horário de almoço (início antes das 12h e fim depois das 13:30)    
            WHEN s.data_hora_ini::time < '12:00:00'::time     
                 AND s.data_hora_fim::time > '13:30:00'::time THEN    
                EXTRACT(EPOCH FROM (s.data_hora_fim::time - s.data_hora_ini::time)) / 60 - 90
                
            -- Se início é antes das 12h e fim é entre 12h e 13:30    
            WHEN s.data_hora_ini::time < '12:00:00'::time     
                 AND s.data_hora_fim::time >= '12:00:00'::time     
                 AND s.data_hora_fim::time <= '13:30:00'::time THEN    
                EXTRACT(EPOCH FROM ('12:00:00'::time - data_hora_ini::time)) / 60
                
            -- Se início é entre 12h e 13:30 e fim é depois das 13:30    
            WHEN s.data_hora_ini::time >= '12:00:00'::time     
                 AND s.data_hora_ini::time < '13:30:00'::time     
                 AND s.data_hora_fim::time >= '13:30:00'::time THEN    
                EXTRACT(EPOCH FROM (s.data_hora_fim::time - '13:30:00'::time)) / 60
                
            -- Se início e fim estão dentro do horário de almoço    
            WHEN s.data_hora_ini::time >= '12:00:00'::time     
                 AND s.data_hora_fim::time <= '13:30:00'::time THEN    
                0
                
            ELSE     
                EXTRACT(EPOCH FROM (s.data_hora_fim::time - s.data_hora_ini::time)) / 60    
        END)  
    )::int AS minutes,
        s.minutes as minutes_old,
        s.data_hora_ini,   
        s.data_hora_fim, 
        s.description
    
    
    FROM public.sgd_schedule_past_future as s  order by 1
```

## `sgd_schedule_three_days`

- **Origem:** Postgres · base `DB_SGD`
- **Usa outras consultas do fluxo:** `sgd_alocation_historic`
- `public.sgd_alocation_historic` ← import-sgd-diario (substitui janela de 60 dia(s))
- `public.sgd_schedule_three_days` ← import-agendas (janela dos ultimos dias uteis)
- **Colunas entregues:** `date` (int64), `i_user` (int64), `i_type` (int64), `responsible` (string), `i_absences_reason` (int64), `minutes` (int64), `minutes_old` (int64), `data_hora_ini` (string), `data_hora_fim` (string), `description` (string), `i_alocation` (int64)

SQL nativo:

```sql
SELECT s.date, 
        s.i_user, 
        s.i_type, 
        s.responsible, 
        s.i_absences_reason, 
        LEAST(480,  
        (CASE    
            -- Se algum dos campos for NULL ou vazio, retorna NULL    
            WHEN s.data_hora_ini IS NULL     
                 OR s.data_hora_fim IS NULL     
                 OR s.data_hora_ini::text = ''     
                 OR s.data_hora_fim::text = '' THEN    
                480
                
            -- Se o período não cruza o horário de almoço    
            WHEN s.data_hora_fim::time < '12:00:00'::time     
                 OR s.data_hora_ini::time >= '13:30:00'::time THEN    
                EXTRACT(EPOCH FROM (s.data_hora_fim::time - s.data_hora_ini::time)) / 60
                
            -- Se cruza completamente o horário de almoço (início antes das 12h e fim depois das 13:30)    
            WHEN s.data_hora_ini::time < '12:00:00'::time     
                 AND s.data_hora_fim::time > '13:30:00'::time THEN    
                EXTRACT(EPOCH FROM (s.data_hora_fim::time - s.data_hora_ini::time)) / 60 - 90
                
            -- Se início é antes das 12h e fim é entre 12h e 13:30    
            WHEN s.data_hora_ini::time < '12:00:00'::time     
                 AND s.data_hora_fim::time >= '12:00:00'::time     
                 AND s.data_hora_fim::time <= '13:30:00'::time THEN    
                EXTRACT(EPOCH FROM ('12:00:00'::time - data_hora_ini::time)) / 60
                
            -- Se início é entre 12h e 13:30 e fim é depois das 13:30    
            WHEN s.data_hora_ini::time >= '12:00:00'::time     
                 AND s.data_hora_ini::time < '13:30:00'::time     
                 AND s.data_hora_fim::time >= '13:30:00'::time THEN    
                EXTRACT(EPOCH FROM (s.data_hora_fim::time - '13:30:00'::time)) / 60
                
            -- Se início e fim estão dentro do horário de almoço    
            WHEN s.data_hora_ini::time >= '12:00:00'::time     
                 AND s.data_hora_fim::time <= '13:30:00'::time THEN    
                0
                
            ELSE     
                EXTRACT(EPOCH FROM (s.data_hora_fim::time - s.data_hora_ini::time)) / 60    
        END)  
    )::int AS minutes,
        s.minutes as minutes_old,
        s.data_hora_ini,   
        s.data_hora_fim, 
        s.description,
        coalesce(h.i_alocation,999) as i_alocation
    
    
    FROM public.sgd_schedule_three_days as s LEFT JOIN public.sgd_alocation_historic as h 
                                         on h.i_user = s.i_user 
                                        AND s.date::date = h.date::date order by s.date::date desc
```

## `sgd_users`

- **Origem:** Postgres · base `DB_SGD`
- `public.sgd_users` ← import-sgd-diario (recarga TOTAL)
- **Colunas entregues:** `i_user` (int64), `user` (string), `email` (string), `admission` (date), `date_inactivation` (date), `dismission` (string), `name` (string), `resale` (string), `i_resale` (int64), `type_resale` (string)

SQL nativo:

```sql
SELECT 
        i_user, 
        "user", 
        email, 
        admission, 
        left(date_inactivation,10) as date_inactivation,
        dismission, 
        name, 
        resale, 
        i_resale,
        (case 
            WHEN i_user IN (1405244,1444989) then 'BOT-IA'
            ELSE type_resale END ) as type_resale
    FROM public.sgd_users;
```

## `sgd_users_horario_historic`

- **Origem:** Postgres · base `DB_SGD`
- `public.sgd_horario_historic` ← import-sgd-diario (substitui janela de 15 dia(s))
- **Colunas entregues:** `date` (int64), `i_user` (int64), `i_responsavel_lancto` (int64), `horario_inicio_matutino` (string), `horario_fim_matutino` (string), `horario_inicio_vespertino` (string), `horario_fim_vespertino` (string), `vigencia` (string)

SQL nativo:

```sql
SELECT date, 
     i_user, 
     i_responsavel_lancto, 
     horario_inicio_matutino, 
     horario_fim_matutino, 
     horario_inicio_vespertino, 
     horario_fim_vespertino, vigencia
    FROM public.sgd_horario_historic
```

## `sgd_user_manager_historic`

- **Origem:** Postgres · base `DB_SGD`
- **Usa outras consultas do fluxo:** `sgd_alocation_historic`
- `public.sgd_alocation_historic` ← import-sgd-diario (substitui janela de 60 dia(s))
- `public.sgd_user_manager_historic` ← import-sgd-diario (substitui janela de 365 dia(s))
- **Colunas entregues:** `date` (int64), `i_historic` (int64), `i_user` (int64), `from_of` (int64), `i_superv` (int64), `superv` (string), `manager` (string), `responsible_alter` (string), `date_alter` (int64), `unity` (string), `i_alocation` (int64)

SQL nativo:

```sql
SELECT 
    h.date, 
    h.i_historic, 
    h.i_user, 
    h.from_of, 
    h.i_superv, 
    (case  h.superv
        WHEN 'Thiago Candelaria Birck (SP)' then 'Thiago Candelaria Birck'
        WHEN 'Eloiza Kulckamp Alberton (Suporte SC)' THEN 'Eloiza Kulckamp Alberton'
        --WHEN 'Adas Pavei Fontana (Sup SC)' THEN 'Everton Batisti'
        WHEN 'Everton Carlos Batisti (Int)' THEN 'Everton Batisti'
        WHEN 'Marina Ferrari ' THEN 'Marina Ferrari'  
        WHEN 'Camila Becker Meller (CT)' THEN 'Camila Becker Meller'
        ELSE  h.superv END) as superv,
        
    (case h.manager
        WHEN 'Thiago Candelaria Birck (SP)' then 'Thiago Candelaria Birck'
        WHEN 'Eloiza Kulckamp Alberton (Suporte SC)' THEN 'Eloiza Kulckamp Alberton'
        WHEN 'Adas Pavei Fontana (Sup SC)' THEN 'Everton Batisti'
        WHEN 'Everton Carlos Batisti (Int)' THEN 'Everton Batisti'
        WHEN 'Marina Ferrari ' THEN 'Marina Ferrari'
        WHEN 'Camila Becker Meller (CT)' THEN 'Camila Becker Meller'
        WHEN '' THEN (case  h.superv
                    WHEN 'Thiago Candelaria Birck (SP)' then 'Thiago Candelaria Birck'
                    WHEN 'Eloiza Kulckamp Alberton (Suporte SC)' THEN 'Eloiza Kulckamp Alberton'
                    WHEN 'Adas Pavei Fontana (Sup SC)' THEN 'Everton Batisti'
                    WHEN 'Everton Carlos Batisti (Int)' THEN 'Everton Batisti'
                    WHEN 'Marina Ferrari ' THEN 'Marina Ferrari'    
                    WHEN 'Camila Becker Meller (CT)' THEN 'Camila Becker Meller'
                    ELSE  h.superv END)
        ELSE h.manager END) as manager,
    h.responsible_alter, 
    h.date_alter,
    (case h.manager
        WHEN 'Thiago Candelaria Birck' then 'CAMPINAS'
        WHEN 'Thiago Candelaria Birck (SP)' then 'CAMPINAS'
        WHEN 'Marina Ferrari' then 'CAMPINAS'
        WHEN 'Marina Ferrari ' then 'CAMPINAS'
        WHEN 'Eloiza Kulckamp Alberton (Suporte SC)' THEN 'SUL'
        WHEN 'Eloiza Kulckamp Alberton' THEN 'SUL'
        WHEN 'Adas Pavei Fontana (Sup SC)' THEN 'CONV-EXP-IMP'
        WHEN 'Everton Carlos Batisti (Upg)' THEN 'REVENDAS'
        WHEN 'Everton Carlos Batisti (Int)' THEN 'CONV-EXP-IMP'
        WHEN 'Everton Carlos Batisti' THEN 'REVENDAS'
        WHEN 'Camila Becker Meller (CT)' THEN 'BOT-IA'
        WHEN '' THEN (case h.superv
                        WHEN 'Thiago Candelaria Birck' then 'CAMPINAS'
                        WHEN 'Thiago Candelaria Birck (SP)' then 'CAMPINAS'
                        WHEN 'Marina Ferrari' then 'CAMPINAS'
                        WHEN 'Marina Ferrari ' then 'CAMPINAS'
                        WHEN 'Eloiza Kulckamp Alberton (Suporte SC)' THEN 'SUL'
                        WHEN 'Eloiza Kulckamp Alberton' THEN 'SUL'
                        WHEN 'Adas Pavei Fontana (Sup SC)' THEN 'CONV-EXP-IMP'
                        WHEN 'Everton Carlos Batisti (Upg)' THEN 'REVENDAS'
                        WHEN 'Everton Carlos Batisti (Int)' THEN 'CONV-EXP-IMP'
                        WHEN 'Everton Carlos Batisti' THEN 'REVENDAS'
                        WHEN 'Camila Becker Meller (CT)' THEN 'BOT-IA'
                        ELSE 'REVENDAS' END)
        ELSE 'REVENDAS' END) as unity,
    coalesce(sgd_alocation_historic.i_alocation,999) as i_alocation
FROM public.sgd_user_manager_historic as h 


LEFT JOIN public.sgd_alocation_historic 
    ON sgd_alocation_historic.i_user = h.i_user
    AND sgd_alocation_historic.date = h.date


UNION ALL

SELECT 
    (current_date::date - 1)::text as date,  -- Data sempre current_date - 1
    h.i_historic, 
    h.i_user, 
    h.from_of, 
    h.i_superv, 
    (case  h.superv
        WHEN 'Thiago Candelaria Birck (SP)' then 'Thiago Candelaria Birck'
        WHEN 'Eloiza Kulckamp Alberton (Suporte SC)' THEN 'Eloiza Kulckamp Alberton'
       -- WHEN 'Adas Pavei Fontana (Sup SC)' THEN 'Everton Batisti'
        WHEN 'Everton Carlos Batisti (Int)' THEN 'Everton Batisti'
        WHEN 'Marina Ferrari ' THEN 'Marina Ferrari'
        WHEN 'Camila Becker Meller (CT)' THEN 'Camila Becker Meller'
        ELSE  h.superv END) as superv,
    (case h.manager
        WHEN 'Thiago Candelaria Birck (SP)' then 'Thiago Candelaria Birck'
        WHEN 'Eloiza Kulckamp Alberton (Suporte SC)' THEN 'Eloiza Kulckamp Alberton'
        WHEN 'Adas Pavei Fontana (Sup SC)' THEN 'Everton Batisti'
        WHEN 'Everton Carlos Batisti (Int)' THEN 'Everton Batisti'
        WHEN 'Marina Ferrari ' THEN 'Marina Ferrari'
        WHEN 'Camila Becker Meller (CT)' THEN 'Camila Becker Meller'
        WHEN '' THEN (case  h.superv
                    WHEN 'Thiago Candelaria Birck (SP)' then 'Thiago Candelaria Birck'
                    WHEN 'Eloiza Kulckamp Alberton (Suporte SC)' THEN 'Eloiza Kulckamp Alberton'
                    WHEN 'Adas Pavei Fontana (Sup SC)' THEN 'Everton Batisti'
                    WHEN 'Everton Carlos Batisti (Int)' THEN 'Everton Batisti'
                    WHEN 'Marina Ferrari ' THEN 'Marina Ferrari'
                    WHEN 'Camila Becker Meller (CT)' THEN 'Camila Becker Meller'
                    ELSE  h.superv END)
        ELSE h.manager END) as manager,
    h.responsible_alter, 
    h.date_alter,
    (case h.manager
        WHEN 'Thiago Candelaria Birck' then 'CAMPINAS'
        WHEN 'Thiago Candelaria Birck (SP)' then 'CAMPINAS'
        WHEN 'Marina Ferrari' then 'CAMPINAS'
        WHEN 'Marina Ferrari ' then 'CAMPINAS'
        WHEN 'Eloiza Kulckamp Alberton (Suporte SC)' THEN 'SUL'
        WHEN 'Eloiza Kulckamp Alberton' THEN 'SUL'
        WHEN 'Adas Pavei Fontana (Sup SC)' THEN 'CONV-EXP-IMP'
        WHEN 'Everton Carlos Batisti (Upg)' THEN 'REVENDAS'
        WHEN 'Everton Carlos Batisti (Int)' THEN 'CONV-EXP-IMP'
        WHEN 'Everton Carlos Batisti' THEN 'REVENDAS'
        WHEN 'Camila Becker Meller (CT)' THEN 'BOT-IA'
        WHEN '' THEN (case h.superv
                        WHEN 'Thiago Candelaria Birck' then 'CAMPINAS'
                        WHEN 'Thiago Candelaria Birck (SP)' then 'CAMPINAS'
                        WHEN 'Marina Ferrari' then 'CAMPINAS'
                        WHEN 'Marina Ferrari ' then 'CAMPINAS'
                        WHEN 'Eloiza Kulckamp Alberton (Suporte SC)' THEN 'SUL'
                        WHEN 'Eloiza Kulckamp Alberton' THEN 'SUL'
                        WHEN 'Adas Pavei Fontana (Sup SC)' THEN 'CONV-EXP-IMP'
                        WHEN 'Everton Carlos Batisti (Upg)' THEN 'REVENDAS'
                        WHEN 'Everton Carlos Batisti (Int)' THEN 'CONV-EXP-IMP'
                        WHEN 'Everton Carlos Batisti' THEN 'REVENDAS'
                        WHEN 'Camila Becker Meller (CT)' THEN 'BOT-IA'
                        ELSE 'REVENDAS' END)
        ELSE 'REVENDAS' END) as unity,
    coalesce(sgd_alocation_historic.i_alocation,999) as i_alocation
FROM public.sgd_user_manager_historic as h 
LEFT JOIN public.sgd_alocation_historic 
    ON sgd_alocation_historic.i_user = h.i_user
    AND sgd_alocation_historic.date = h.date
WHERE h.date::date != current_date - 1
AND h.date = (
    SELECT MAX(h2.date) 
    FROM public.sgd_user_manager_historic h2 
    WHERE h2.i_user = h.i_user 
    AND h2.date::date != current_date - 1
)
AND NOT EXISTS (
    SELECT 1 
    FROM public.sgd_user_manager_historic h3 
    WHERE h3.i_user = h.i_user 
    AND h3.date::date = current_date - 1
)
ORDER BY 1 desc
```

## `sgd_user_position_historic`

- **Origem:** Postgres · base `DB_SGD`
- `public.sgd_user_cargo_historico` ← import-sgd-diario (recarga TOTAL)
- **Colunas entregues:** `data_dia` (int64), `i_usuario` (int64), `i_cargo_historico` (int64), `a_partir_de` (date)

SQL nativo:

```sql
SELECT data_dia, 
      i_usuario,
      i_cargo_historico, 
      a_partir_de
    FROM public.sgd_user_cargo_historico;
```

## `sgd_sa_module`

- **Origem:** Postgres · base `DB_SGD`
- `public.sgd_sa_module` ← import-sgd-diario (recarga TOTAL)
- **Colunas entregues:** `i_system` (int64), `i_module` (int64), `description` (string)

## `sgd_sa_system`

- **Origem:** Postgres · base `DB_SGD`
- `public.sgd_sa_system` ← import-sgd-diario (recarga TOTAL)
- **Colunas entregues:** `i_system` (int64), `description` (string)

## `sgd_sa`

- **Origem:** Postgres · base `DB_SGD`
- `public.sgd_sa` ← import-sgd-diario (substitui janela de 1 dia(s))
- **Colunas entregues:** `i_sa` (int64), `date_entry` (date), `subject` (string), `i_sa_classification` (int64), `i_status` (int64), `i_resales` (int64), `i_system` (int64), `i_module` (int64), `type_sa` (int64), `type_sa_ne` (string), `client` (string), `i_user` (int64), `i_sa_disapproval_reason` (int64)

SQL nativo:

```sql
SELECT 
    s.i_sa, 
    s.date_entry, 
    s.subject, 
    s.i_sa_classification, 
    s.i_status, 
    s.i_resales, 
    s.i_system,
    s.i_module, 
    s.type_sa,
    ( case 
         when reason = 0 then 'NE'
         when reason = 1 then 'SA'
         when reason = 2 then 'SAL'
         when reason = 3 then 'SAIL'
      else 'NAO_CADASTRADO' end) as type_sa_ne,
    s.client, 
    s.i_user, 
    s.i_sa_disapproval_reason
FROM public.sgd_sa AS s;
```

## `sgd_sa_description`

- **Origem:** Postgres · base `DB_SGD`
- **Usa outras consultas do fluxo:** `sgd_sa`
- `public.sgd_sa` ← import-sgd-diario (substitui janela de 1 dia(s))
- **Colunas entregues:** `i_sa` (int64), `description` (string), `justification` (string)

SQL nativo:

```sql
SELECT
      s.i_sa,
      s.description, 
      s.justification
   FROM public.sgd_sa as s
```

## `sgd_sa_classification`

- **Origem:** Postgres · base `DB_SGD`
- `public.sgd_sa_classification` ← import-sgd-diario (recarga TOTAL)
- **Colunas entregues:** `i_sa_classification` (int64), `description` (string)

## `sgd_sa_disapproval_reason`

- **Origem:** Postgres · base `DB_SGD`
- `public.sgd_sa_disapproval_reason` ← import-sgd-diario (recarga TOTAL)
- **Colunas entregues:** `i_sa_disapproval_reason` (int64), `description` (string)

## `sgd_sa_priority`

- **Origem:** Postgres · base `DB_SGD`
- `public.sgd_sa_priority` ← import-sgd-diario (INSERT sem limpeza (ACUMULA))
- **Colunas entregues:** `i_sa` (int64), `entry` (string), `i_user` (int64), `description` (string)

## `sgd_sa_situations`

- **Origem:** Postgres · base `DB_SGD`
- `public.sgd_sa_situations` ← import-sgd-diario (recarga TOTAL)
- **Colunas entregues:** `i_sa_situation` (int64), `description` (string)

## `sgd_sai_vs_sane`

- **Origem:** Postgres · base `DB_SGD`
- `public.sgd_sai_sane` ← import-sgd-diario (recarga TOTAL)
- **Colunas entregues:** `i_sai` (int64), `i_sa_ne` (int64)

SQL nativo:

```sql
SELECT i_sai, i_sa_ne
    FROM public.sgd_sai_sane;
```

## `forecast_ajuste_demanda`

- **Origem:** Postgres · base `DB_SGD`
- **Usa outras consultas do fluxo:** `calendar`
- `forecast.ajuste_demanda` ← import-sgd-diario, import-sgd-meiodia (recarga TOTAL)
- `public.calendar` ← mantida manualmente por fora do Maestro (orq:modules/import_agendas/skills.md:55)
- **Colunas entregues:** `date` (int64), `area` (string), `vlr_ajuste` (double), `gerente` (string)

SQL nativo:

```sql
select c.date, 
  a.area,
  a.vlr_ajuste,
  a.gerente
       
from forecast.ajuste_demanda as a,
        public.calendar as c
     
where to_DATE(cast(c.date as TEXT),'yyyy-mm-dd') between to_DATE(a.ini,'yyyy-mm-dd') and to_DATE(a.fim,'yyyy-mm-dd')

group by c.date, a.area ,a.vlr_ajuste,a.gerente
  
  
  order by 4,1
```

## `forecast_avg_produtividade`

- **Origem:** Postgres · base `DB_SGD`
- **Usa outras consultas do fluxo:** `calendar`
- `forecast.produtividade_media` ← import-sgd-diario, import-sgd-meiodia (recarga TOTAL)
- `public.calendar` ← mantida manualmente por fora do Maestro (orq:modules/import_agendas/skills.md:55)
- **Colunas entregues:** `date` (int64), `area` (string), `medprodut` (int64), `gerente` (string)

SQL nativo:

```sql
select c.date, 
      a.area,
      a.medprodut,
        a.gerente
       
from forecast.produtividade_media as a,
        public.calendar as c
     
where to_DATE(cast(c.date as TEXT),'yyyy-mm') between to_DATE(a.ini,'yyyy-mm') and to_DATE(a.fim,'yyyy-mm')
  
  
  order by 4,1
```

## `forecast_client_user_history`

- **Origem:** Postgres · base `DB_SGD`
- `forecast.client_user_history` ← import-sgd-diario (INSERT sem limpeza (ACUMULA))
- **Colunas entregues:** `date` (int64), `i_client` (double), `i_contrat` (double), `dateregister` (date), `totusers` (double), `i_product` (double)

SQL nativo:

```sql
SELECT 
firstdaymonth, 
i_client, 
i_contrat, 
dateregister, 
( case totusers 
         WHEN 0 then 1 
     else totusers END ) as totusers, 
i_product
    
FROM forecast.client_user_history order by  firstdaymonth asc
```

## `forecast_coefficient`

- **Origem:** Postgres · base `DB_SGD`
- `forecast.coefficient` ← congelada (decisão: "As 3 tabelas congelam como estão", orq:modules/_import_sgd/catalog.py:210-214) — não é escrita por nenhum job ativo
- **Colunas entregues:** `date` (string), `calls_folha` (string), `calls_fiscont` (string), `calls_funcional` (string), `coeff_geral` (string), `perc_folha` (string), `coeff_folha` (string), `perc_fiscont` (string), `coeff_fiscont` (string), `calls_at` (string), `coeff_at` (string), `unity` (string)

## `forecast_demanda_projetada`

- **Origem:** Postgres · base `DB_SGD`
- `forecast.demanda_projetada` ← import-sgd-diario (recarga TOTAL)
- **Colunas entregues:** `_data` (double), `regional` (string), `area` (string), `demanda_fone` (double), `demanda_web` (double), `demanda_chat` (double)

SQL nativo:

```sql
SELECT 
        _data, 
        regional, 
        area, 
        demanda_fone, 
        demanda_web, 
        demanda_chat
    FROM forecast.demanda_projetada 
    
    order by _data asc
```

## `forecast_de_para_alocacao_area`

- **Origem:** Postgres · base `DB_SGD`
- `forecast.de_para_alocacao` ← import-sgd-diario, import-sgd-meiodia (recarga TOTAL)
- **Colunas entregues:** `i_alocation` (int64), `alocation` (string), `area` (string)

SQL nativo:

```sql
SELECT i_alocation, 
       alocation, 
       (CASE when area = '0' then 'NÃO RELACIONADO' 
        else area end) as area
    FROM forecast.de_para_alocacao;
```

## `forecast_de_para_calendar`

- **Origem:** Postgres · base `DB_SGD`
- `forecast.de_para_calendar` ← import-sgd-diario, import-sgd-meiodia (recarga TOTAL)
- **Colunas entregues:** `date_projet` (string), `date_origem` (string)

## `forecast_FTE_aprovado`

- **Origem:** Postgres · base `DB_SGD`
- **Usa outras consultas do fluxo:** `calendar`
- `forecast.fte_aprovado` ← import-sgd-diario, import-sgd-meiodia (recarga TOTAL)
- `public.calendar` ← mantida manualmente por fora do Maestro (orq:modules/import_agendas/skills.md:55)
- **Colunas entregues:** `date` (int64), `area` (string), `fte_apovado` (int64), `gerente` (string)

SQL nativo:

```sql
select c.date, 
       a.area,
       a.aprovado as fte_apovado,
         a.gerente
       
from forecast.fte_aprovado as a inner join public.calendar as c
                                                      on to_DATE(cast(c.date as TEXT),'yyyy-mm') between to_DATE(a.ini,'yyyy-mm') and to_DATE(a.fim,'yyyy-mm')
                                        
  
  
  
  order by 4,1
```

## `forecast_proj_ausencias`

- **Origem:** Postgres · base `DB_SGD`
- **Usa outras consultas do fluxo:** `calendar`
- `forecast.ausencias_projetado` ← import-sgd-diario, import-sgd-meiodia (recarga TOTAL)
- `public.calendar` ← mantida manualmente por fora do Maestro (orq:modules/import_agendas/skills.md:55)
- **Colunas entregues:** `date_int` (int64), `area` (string), `total` (double), `tipo` (string), `reg` (string)

SQL nativo:

```sql
select c.date, 
       a.area,
       a.total,
       a.tipo,
       a.reg
       
from forecast.ausencias_projetado as a,
     public.calendar as c
where to_DATE(left(cast(c.date as TEXT),7),'yyyy-mm') between to_DATE(a.ini,'yyyy-mm') and to_DATE(a.fim,'yyyy-mm')
  and length(a.ini) <= 7 
  
union all

select c.date, 
       a.area,
       a.total,
       a.tipo,
       a.reg
       
from forecast.ausencias_projetado as a,
     public.calendar as c
     
where to_DATE(cast(c.date as TEXT),'yyyy-mm-dd') between to_DATE(a.ini,'yyyy-mm-dd') and to_DATE(a.fim,'yyyy-mm-dd')
  and length(a.ini) > 7 
  
  order by 5,1
```

## `forecast_proj_tme`

- **Origem:** Postgres · base `DB_SGD`
- `forecast.tme_projetado` ← import-sgd-diario, import-sgd-meiodia (recarga TOTAL)
- **Colunas entregues:** `year` (int64), `ini` (double), `fim` (double), `seg` (int64), `setor` (string), `canal` (string)

SQL nativo:

```sql
SELECT year, ini, fim, seg,setor,canal
    FROM forecast.tme_projetado
```

## `forecast_projetado`

- **Origem:** Postgres · base `DB_SGD`
- `forecast.projetado` ← congelada (decisão: "As 3 tabelas congelam como estão", orq:modules/_import_sgd/catalog.py:210-214) — não é escrita por nenhum job ativo
- **Colunas entregues:** `date_projet` (string), `date_origem` (string), `unity` (string), `coeff_folha` (string), `coeff_fiscont` (string), `coeff_at` (string), `tot_users` (int64), `proj_folha` (int64), `proj_fiscont` (int64), `proj_at` (int64)

## `forecast_users_proj`

- **Origem:** Postgres · base `DB_SGD`
- `forecast.users` ← import-sgd-diario, import-sgd-meiodia (recarga TOTAL)
- **Colunas entregues:** `date_month` (string), `tot_sc` (int64), `tot_sp` (int64)

## `sgd_ssc_ss`

- **Origem:** Postgres · base `DB_SGD`
- `public.sgd_ssc_ss` ← não mapeado no Maestro
- **Colunas entregues:** `ssc` (int64), `ss` (int64)

## `sgd_chain_ia_interacao`

- **Origem:** Postgres · base `DB_SGD`
- `public.chain_ia_interacao` ← import-sgd-diario (substitui janela de 1 dia(s))
- **Colunas entregues:** `id` (int64), `login_usuario` (string), `nome_usuario` (string), `i_usuarios_gestor` (int64), `i_revendas` (int64), `i_chain_ai_chat` (int64), `prompt_usuario` (string), `resposta_copiada` (string), `data_interacao` (date), `horario_interacao` (time)
