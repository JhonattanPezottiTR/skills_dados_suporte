# Fluxo `DB_SGD_IA`

> Última atualização: 2026-09-30 · Fonte: `DB_SGD_IA.json` (Dataflow Power BI, modificado em 2026-06-03, cultura en-US) · **Gerado automaticamente** por `scripts/mapear_fluxos.py`.

| Entidade | Carrega | Origem | Base | Tabelas de origem | Colunas | Último refresh (UTC) |
|---|---|---|---|---|---|---|
| `sgd_ssc_ia_chat` | sim | Postgres | DB_SGD | `public.sgd_ssc_ia_chat` | 7 | 2026-09-29T09:05:02 |
| `sgd_utilizou_reescrever_IA` | sim | Postgres | DB_SGD | `public.sgd_alocation_historic`, `public.sgd_ssc_reescrever_ia` | 8 | 2026-09-29T09:05:33 |
| `sgd_chain_ia_interacao` | sim | Postgres | DB_SGD | `public.chain_ia_interacao` | 10 | 2026-09-29T09:06:03 |

## `sgd_ssc_ia_chat`

- **Origem:** Postgres · base `DB_SGD`
- `public.sgd_ssc_ia_chat` ← import-sgd-diario (substitui janela de 5 dia(s))
- **Colunas entregues:** `i_ssc` (int64), `satisfeito` (string), `motivo_satisfacao` (string), `exemplo` (string), `motivo_acesso` (string), `poderia_nao_usar` (string), `teve_acesso` (string)

SQL nativo:

```sql
SELECT 
    ssc.i_ssc,
    -- Dados do prompt 1
    CASE 
    -- Respostas indeterminadas
    WHEN LOWER(satisfeito) LIKE 'desconhecido%' OR
         LOWER(satisfeito) LIKE 'incerto%' OR
         LOWER(satisfeito) LIKE 'indeterminado%' OR
         LOWER(satisfeito) = 'n/a' OR
         LOWER(satisfeito) LIKE 'não avaliado%' OR
         LOWER(satisfeito) LIKE 'não é possível%' OR
         LOWER(satisfeito) LIKE 'não pode%' OR
         LOWER(satisfeito) LIKE 'não especificado%' OR
         LOWER(satisfeito) LIKE 'não identificado%' OR
         LOWER(satisfeito) LIKE 'sem dados%' OR
         LOWER(satisfeito) LIKE 'sem informação%'
    THEN 'Indeterminado'
    -- Respostas positivas
    WHEN LOWER(satisfeito) LIKE 'sim%' OR LOWER(satisfeito) = 'yes' 
    THEN 'Sim'
    -- Respostas negativas
    WHEN LOWER(satisfeito) LIKE 'não%' OR 
         LOWER(satisfeito) LIKE 'nao%' OR 
         LOWER(satisfeito) LIKE 'nâo%'
    THEN 'Não'
    -- Outros casos
    ELSE 'Indeterminado'
    END AS satisfeito,

    -- Motivo de satisfação - Versão mais objetiva
    CASE 
        -- Cliente satisfeito
        WHEN LOWER(satisfeito) LIKE 'sim%' OR LOWER(satisfeito) = 'yes'
        THEN 'Satisfeito'

        -- Não identificado
        WHEN satisfeito is null
        THEN 'Não identificado'
        
        -- Atendente não soluciona
        WHEN LOWER(motivo) LIKE '%atendente não soluciona%' OR 
             LOWER(motivo) LIKE '%atendente não solucionou%' OR
             LOWER(motivo) LIKE '%atendente: não soluciona%' OR
             LOWER(motivo) LIKE '%ausência de interação%' OR
             LOWER(motivo) LIKE '%não solucion%'
        THEN  'Atendente não soluciona'
            
        
        -- Vários motivos
        WHEN LOWER(motivo) LIKE '%vários%' OR 
             LOWER(motivo) LIKE '%varios%'
        THEN 'Múltiplas insatisfações'

        -- Necessidade de melhorias
        WHEN LOWER(motivo) LIKE '%necessidade de melhorias%' OR 
             LOWER(motivo) LIKE '%sam%'
        THEN 'SAM / Melhorias'
        
        -- Demora na resposta
        WHEN LOWER(motivo) LIKE '%demora na resposta%' 
        THEN 'Demora na resposta'
        
        -- Bugs/erros
        WHEN LOWER(motivo) LIKE '%bugs%' OR 
             LOWER(motivo) LIKE '%erros do sistema%' OR
             LOWER(motivo) LIKE '%ne - bugs%' OR
             LOWER(motivo) LIKE '%ne – bugs%'
        THEN 'Bugs/Erros/NE'
            
            
        
        
        -- Problemas recorrentes
        WHEN LOWER(motivo) LIKE '%problemas recorrentes%' 
        THEN 'Problemas sem solução definitiva'
        
        
                
        -- Indeterminado
        WHEN LOWER(motivo) LIKE '%indeterminado%' OR
             LOWER(motivo) LIKE '%não avaliado%' OR
             LOWER(motivo) LIKE '%não é possível determinar%' OR
             LOWER(motivo) LIKE '%não especificado%' OR
             LOWER(motivo) LIKE '%não identificado%' OR
             LOWER(motivo) LIKE '%não pode ser determinado%' OR
             LOWER(motivo) LIKE '%sem informação suficiente%' OR
             LOWER(motivo) LIKE '%não há evidências suficientes%' OR
             LOWER(motivo) = 'n/a' OR
             LOWER(motivo) = 'não aplicável'
        THEN 'Motivo não especificado'
        
        -- Outros casos
        ELSE 'Outro motivo'
END AS motivo_satisfacao,
    --motivo as motivo_original,
    
    COALESCE(prompt1.exemplo, 'Sem informação suficiente') AS exemplo,
    
    -- Dados do prompt 3
    --COALESCE(prompt3.acesso_remoto, 'Sem informação suficiente') AS acesso_remoto,

    CASE
        WHEN LOWER(prompt3.acesso_remoto) LIKE 'não%' OR
             LOWER(prompt3.acesso_remoto) LIKE 'nao%' OR
             LOWER(prompt3.acesso_remoto) = 'não'  
        THEN 'Não'
        ELSE COALESCE(prompt3.acesso_remoto, 'Não')
    END AS acesso_remoto,
    
    CASE
        WHEN LOWER(prompt3.motivo_acesso) LIKE 'não%' OR
             LOWER(prompt3.motivo_acesso) LIKE 'nao%' OR
             LOWER(prompt3.motivo_acesso) = 'não'  
        THEN 'Não houve acesso remoto'
        ELSE COALESCE(prompt3.motivo_acesso, 'Sem informação suficiente')
    END AS motivo_acesso,
    
    CASE
        WHEN prompt3.acesso_remoto = 'Não' THEN 'Não houve acesso remoto'
        ELSE COALESCE(prompt3.poderia_nao_usar, 'Sem informação suficiente')
    END AS poderia_nao_usar
FROM 
    (SELECT DISTINCT i_ssc FROM public.sgd_ssc_ia_chat) ssc
LEFT JOIN LATERAL (
    SELECT 
        SUBSTRING(completion FROM 'Satisfeito: (.*?) Motivo:') AS satisfeito,
        COALESCE(
        SUBSTRING(completion FROM 'Motivo: (.*?) Exemplo:'),
        SUBSTRING(completion FROM 'Motivo: (.*?) Exemplos:'),
        SUBSTRING(completion FROM 'Motivo: (.*?)$')
    ) AS motivo,
    COALESCE(
        SUBSTRING(completion FROM 'Exemplo: (.*?)$'),
        SUBSTRING(completion FROM 'Exemplos: (.*?)$')
    ) AS exemplo
    FROM 
        public.sgd_ssc_ia_chat
    WHERE 
        i_ssc = ssc.i_ssc 
        AND id_prompt = 1
    LIMIT 1
) prompt1 ON true
LEFT JOIN LATERAL (
    SELECT 
        
        replace(cast(TRIM(SPLIT_PART(completion, ';', 1)) as text), '*', '') AS acesso_remoto,
        replace(cast(TRIM(SPLIT_PART(completion, ';', 2)) as text), '*', '') AS motivo_acesso,
        TRIM(SPLIT_PART(completion, ';', 3)) AS poderia_nao_usar
    FROM 
        public.sgd_ssc_ia_chat
    WHERE 
        i_ssc = ssc.i_ssc 
        AND id_prompt = 3
    LIMIT 1
) prompt3 ON true
ORDER BY 
    ssc.i_ssc ASC
```

## `sgd_utilizou_reescrever_IA`

- **Origem:** Postgres · base `DB_SGD`
- `public.sgd_alocation_historic` ← import-sgd-diario (substitui janela de 60 dia(s))
- `public.sgd_ssc_reescrever_ia` ← import-sgd-diario (substitui janela de 5 dia(s))
- **Colunas entregues:** `seq` (int64), `data_entrada` (int64), `utilizou_resposta` (string), `alterou_resposta` (string), `i_usuario` (int64), `prompt_usuario` (string), `retorno_ia` (string), `i_alocation` (int64)

SQL nativo:

```sql
SELECT ia.seq,
     ia.data_entrada::date,
     case 
         when ia.utilizou_resposta = 1 then 'Sim'
        else 'Não'
        END as utilizou_resposta,
     case 
         when ia.alterou_resposta = 1 then 'Sim'
        else 'Não'
        END as alterou_resposta,
     ia.i_usuario,
     ia.prompt_usuario,
     ia.retorno_ia,
     coalesce(h.i_alocation,999) as i_alocation
    FROM public.sgd_ssc_reescrever_ia as ia inner join public.sgd_alocation_historic as h
                                                ON h.date::date = ia.data_entrada::date
                                                and h.i_user = ia.i_usuario
    
    order by 1
```

## `sgd_chain_ia_interacao`

- **Origem:** Postgres · base `DB_SGD`
- `public.chain_ia_interacao` ← import-sgd-diario (substitui janela de 1 dia(s))
- **Colunas entregues:** `id` (int64), `login_usuario` (string), `nome_usuario` (string), `i_usuarios_gestor` (int64), `i_revendas` (int64), `i_chain_ai_chat` (int64), `prompt_usuario` (string), `resposta_copiada` (string), `data_interacao` (date), `horario_interacao` (time)
