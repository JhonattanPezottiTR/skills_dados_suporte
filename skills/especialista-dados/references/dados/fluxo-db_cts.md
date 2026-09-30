# Fluxo `DB_CTS`

> Última atualização: 2026-09-30 · Fonte: `DB_CTS.json` (Dataflow Power BI, modificado em 2026-06-04, cultura en-US) · **Gerado automaticamente** por `scripts/mapear_fluxos.py`.

| Entidade | Carrega | Origem | Base | Tabelas de origem | Colunas | Último refresh (UTC) |
|---|---|---|---|---|---|---|
| `cts_config_saudacao` | sim | Postgres | DB_CTS | `public.vw_rel_cts_gpt_saudacao` | 6 | 2026-09-29T09:02:33 |
| `cts_dados_digital` | sim | Postgres | DB_CTS | `public.cts_dados_digital` | 3 | 2026-09-29T09:03:04 |
| `cts_sol_access_count` | sim | Postgres | DB_CTS | `public.cts_access_count` | 5 | 2026-09-29T09:15:35 |
| `cts_sol_cadastro` | sim | Postgres | DB_CTS | `public.cts_solucoes` | 12 | 2026-09-29T09:16:06 |
| `cts_sol_historico` | sim | Postgres | DB_CTS | `public.cts_solucoes_historico` | 12 | 2026-09-29T09:16:36 |
| `cts_sol_pesquisas` | sim | Postgres | DB_CTS | `public.cts_searchcontent` | 8 | 2026-09-29T09:21:37 |
| `cts_sol_revisoes` | sim | Postgres | DB_CTS | `public.cts_solucoes_revisoes` | 4 | 2026-09-29T09:22:07 |
| `cts_sol_revisoes_motivos` | sim | Postgres | DB_CTS | `public.cts_solucoes_revisoes_motivos` | 2 | 2026-09-29T09:22:38 |
| `cts_usuarios` | sim | Postgres | DB_CTS | `public.cts_solucoes_usuarios` | 4 | 2026-09-29T09:23:08 |
| `tria_interactions` | sim | Postgres | DB_CTS | `tria.authentication`, `tria.chat_interacoes` | 12 | 2026-09-29T09:27:39 |
| `tria_situ_motv` | sim | Postgres | DB_CTS | `tria.chat_sit_motv` | 3 | 2026-09-29T09:28:10 |
| `tria_plug` | não (auxiliar) | Postgres | tria | `public.dashboard` | 0 | — |
| `Sample file` | não (auxiliar) | Folder.Files | — | — | 0 | — |
| `Parameter` | não (auxiliar) | derivada | — | — | 0 | — |
| `Transform Sample file` | não (auxiliar) | Csv.Document | — | — | 0 | — |
| `Transform file` | não (auxiliar) | Csv.Document | — | — | 0 | — |

## `cts_config_saudacao`

- **Origem:** Postgres · base `DB_CTS`
- `public.vw_rel_cts_gpt_saudacao` ← não mapeado no Maestro
- **Colunas entregues:** `data_consulta` (date), `i_usuario` (double), `Inicio Saudação Configurado` (string), `Fim Saudação Configurado` (string), `Tipo Configuração` (string), `i_alocation` (int64)

SQL nativo:

```sql
select * from public.vw_rel_cts_gpt_saudacao
```

## `cts_dados_digital`

- **Origem:** Postgres · base `DB_CTS`
- `public.cts_dados_digital` ← import-cts (recarga TOTAL)
- **Colunas entregues:** `data_int` (int64), `youtube` (double), `instagram` (double)

SQL nativo:

```sql
select 
*
from public.cts_dados_digital
```

## `cts_sol_access_count`

- **Origem:** Postgres · base `DB_CTS`
- `public.cts_access_count` ← import-cts (substitui janela de 10 dia(s))
- **Colunas entregues:** `i_access_count` (int64), `i_solution` (int64), `i_user` (int64), `date_entry_int` (int64), `means_of_access` (int64)

SQL nativo:

```sql
SELECT 
        i_access_count, 
        i_solution, 
        i_user, 
        date_entry, 
        means_of_access
    FROM public.cts_access_count
    WHERE date_entry >= '2023-01-01'
```

## `cts_sol_cadastro`

- **Origem:** Postgres · base `DB_CTS`
- `public.cts_solucoes` ← import-cts (substitui janela de 5 dia(s))
- **Colunas entregues:** `i_solucao` (int64), `entrada` (int64), `descricao` (string), `sistema` (string), `modulo` (string), `topico` (string), `subtopico` (string), `classificacao` (string), `link_sgd` (string), `link_externo` (string), `_type` (string), `expiration_date` (int64)

SQL nativo:

```sql
SELECT 
    i_solucao, 
    entrada,
    expiracao, 
    descricao, 
    sistema, 
    modulo, 
    topico, 
        subtopico,
    classificacao, 
    link_sgd, 
    link_externo, 
    _type
FROM public.cts_solucoes
```

## `cts_sol_historico`

- **Origem:** Postgres · base `DB_CTS`
- `public.cts_solucoes_historico` ← import-cts (substitui janela de 30 dia(s))
- **Colunas entregues:** `Date` (int64), `id_seq` (int64), `i_solucoes` (int64), `sistema` (string), `modulo` (string), `topico` (string), `i_usuarios` (int64), `i_motivos` (int64), `alterado_video` (int64), `tempo_min` (int64), `comentario` (string), `Time` (time)

SQL nativo:

```sql
SELECT 
        id_seq, 
        i_solucoes, 
        sistema, 
        modulo, 
        topico,
        i_usuarios, 
        i_motivos, 
        alterado_video, 
        tempo, 
        comentario, 
        entrada
    FROM public.cts_solucoes_historico
```

## `cts_sol_pesquisas`

- **Origem:** Postgres · base `DB_CTS`
- `public.cts_searchcontent` ← import-cts (INSERT sem limpeza (ACUMULA))
- **Colunas entregues:** `id_pesquisa` (int64), `id_user_rev` (int64), `conteudo_pesquisa` (string), `data_pesquisa` (int64), `hora_pesquisa` (time), `i_modulo_sol` (int64), `origem_pesquisa` (string), `id_origem_pesquisa` (int64)

SQL nativo:

```sql
SELECT 
id_search as id_pesquisa, 
"id_userResales" as id_user_rev, 
content_search as conteudo_pesquisa, 
"dDataSearch" as data_pesquisa, 
"dTimeSearch" as hora_pesquisa, 
i_modulo_sol as i_modulo_sol, 
(case when ids_telas_contabil = 0 then 'SiteCTS'
        else 'Contabil' end) as origem_pesquisa , 
id_origem_pesquisa
    FROM public."CTS_SearchContent"
    
    where "dDataSearch" >='2023-01-01'
order by "dDataSearch" desc
```

## `cts_sol_revisoes`

- **Origem:** Postgres · base `DB_CTS`
- `public.cts_solucoes_revisoes` ← import-cts (substitui janela de 30 dia(s))
- **Colunas entregues:** `i_solucao` (int64), `versao` (int64), `entrada` (int64), `i_usuarios` (int64)

SQL nativo:

```sql
SELECT 
        i_solucao, 
        versao, 
        entrada, 
        i_usuarios
FROM public.cts_solucoes_revisoes
```

## `cts_sol_revisoes_motivos`

- **Origem:** Postgres · base `DB_CTS`
- `public.cts_solucoes_revisoes_motivos` ← import-cts (recarga TOTAL)
- **Colunas entregues:** `i_motivos` (int64), `descricao` (string)

SQL nativo:

```sql
SELECT i_motivos, 
       descricao
FROM public.cts_solucoes_revisoes_motivos
```

## `cts_usuarios`

- **Origem:** Postgres · base `DB_CTS`
- `public.cts_solucoes_usuarios` ← import-cts (recarga TOTAL)
- **Colunas entregues:** `i_user` (int64), `nome` (string), `situacao` (string), `email` (string)

SQL nativo:

```sql
SELECT 
        i_user, 
        nome, 
        situacao, 
        email
    FROM public.cts_solucoes_usuarios
```

## `tria_interactions`

- **Origem:** Postgres · base `DB_CTS`
- `tria.authentication` ← não mapeado no Maestro
- `tria.chat_interacoes` ← import-cts (INSERT sem limpeza (ACUMULA))
- **Colunas entregues:** `i_chat_interacoes` (int64), `i_user` (int64), `DateEntry` (int64), `HourEntry` (time), `contexto` (string), `prompt` (string), `completion` (string), `satisfacao` (string), `comentario` (string), `curadoria_sit` (string), `curadoria_mot` (string), `curadoria_user` (string)

SQL nativo:

```sql
SELECT i_chat_interacoes, 
       i_user, 
      "DateEntry", 
       contexto,
       prompt, 
      completion,
      ( case when likedislike = -1 then 'Insatisfeito'
             when likedislike = 1 then 'Satisfeito'
             else 'Não Opinou' end ) as satisfacao,
      replace(comentario,'null','') as comentario,
      curadoria_sit, 
      curadoria_mot, 
      coalesce(au."name",'Curadoria não realizada') as curadoria_user
    FROM tria.chat_interacoes left join tria.authentication as au 
                                     on au.id = chat_interacoes.curadoria_user

    Where "DateEntry" >= '2025-01-01'
```

## `tria_situ_motv`

- **Origem:** Postgres · base `DB_CTS`
- `tria.chat_sit_motv` ← não mapeado no Maestro
- **Colunas entregues:** `id_sit_motv` (int64), `desc` (string), `type` (string)

SQL nativo:

```sql
SELECT 
id_sit_motv, 
"desc", 
type
    FROM tria.chat_sit_motv
```

## `tria_plug`

- **Origem:** Postgres · base `tria`
- `public.dashboard` ← não mapeado no Maestro

SQL nativo:

```sql
SELECT 
    id,
    data,
    assunto,
    pergunta, 
    resposta_id,
    util,
    motivo,
    avaliacao
    FROM public.dashboard 
    where data::date >= '2024-01-01'::date order by 1 asc;
```

## `Sample file`

- **Origem:** Folder.Files

## `Parameter`

- **Origem:** derivada
- **Usa outras consultas do fluxo:** `Sample file`

## `Transform Sample file`

- **Origem:** Csv.Document
- **Usa outras consultas do fluxo:** `Parameter`

## `Transform file`

- **Origem:** Csv.Document
- **Usa outras consultas do fluxo:** `Parameter`
