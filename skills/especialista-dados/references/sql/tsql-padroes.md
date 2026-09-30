# Padrões e boas práticas de T-SQL

> Última atualização: 2026-09-29 · Fonte: boas práticas SQL Server/Azure SQL/Fabric (Microsoft Learn) · Para limitações específicas do Fabric, ver `sql-fabric-warehouse-tsql.md`

## 1. Estilo
```sql
-- Palavras-chave em MAIÚSCULAS, um campo por linha, schema sempre qualificado
SELECT
    c.cliente_id,
    c.nome_cliente,
    SUM(v.valor_liquido) AS valor_liquido_total
FROM dbo.fato_vendas AS v
INNER JOIN dbo.dim_cliente AS c
    ON c.cliente_sk = v.cliente_sk
WHERE v.data_venda >= '2026-01-01'
  AND v.data_venda <  '2027-01-01'      -- intervalo semiaberto: sargável e sem problema de hora
GROUP BY
    c.cliente_id,
    c.nome_cliente;
```
- Evite `SELECT *` (quebra com mudança de schema, lê colunas desnecessárias — crítico em armazenamento colunar).
- Use aliases curtos e significativos; sempre prefixe colunas com o alias em joins.
- Termine instruções com `;`.

## 2. Sargabilidade (filtros que usam índice/eliminação de segmentos)
| Evite | Prefira |
|---|---|
| `WHERE YEAR(data) = 2026` | `WHERE data >= '2026-01-01' AND data < '2027-01-01'` |
| `WHERE CONVERT(VARCHAR, id) = '10'` | `WHERE id = 10` (tipos compatíveis) |
| `WHERE nome LIKE '%abc'` | `LIKE 'abc%'` quando possível |
| `WHERE ISNULL(col, 0) = 0` | `WHERE (col = 0 OR col IS NULL)` |

## 3. CTEs e legibilidade
```sql
WITH vendas_mes AS (
    SELECT
        DATEFROMPARTS(YEAR(v.data_venda), MONTH(v.data_venda), 1) AS mes,
        SUM(v.valor_liquido) AS valor
    FROM dbo.fato_vendas AS v
    GROUP BY DATEFROMPARTS(YEAR(v.data_venda), MONTH(v.data_venda), 1)
)
SELECT
    mes,
    valor,
    LAG(valor) OVER (ORDER BY mes) AS valor_mes_anterior,
    valor - LAG(valor) OVER (ORDER BY mes) AS variacao
FROM vendas_mes;
```

## 4. Window functions (padrões úteis)
```sql
-- Último registro por chave (deduplicação)
WITH ranked AS (
    SELECT *,
           ROW_NUMBER() OVER (PARTITION BY cliente_id ORDER BY data_atualizacao DESC) AS rn
    FROM stg.cliente
)
SELECT <colunas> FROM ranked WHERE rn = 1;

-- Acumulado e participação
SELECT
    mes,
    valor,
    SUM(valor) OVER (ORDER BY mes ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS acumulado,
    valor * 1.0 / SUM(valor) OVER () AS participacao
FROM vendas_mes;
```
- Sempre declare o frame (`ROWS BETWEEN ...`) em acumulados: o default com `ORDER BY` é `RANGE`, mais lento e com comportamento diferente em empates.

## 5. Joins e cardinalidade
- Confirme a granularidade de cada tabela antes do join; joins que multiplicam linhas são a principal causa de totais errados.
- Valide com: `SELECT chave, COUNT(*) FROM dim GROUP BY chave HAVING COUNT(*) > 1;` (chave de dimensão deve ser única).
- `LEFT JOIN` + filtro na tabela da direita no `WHERE` vira `INNER JOIN` — coloque o filtro no `ON`.
- Prefira `EXISTS` / `NOT EXISTS` a `IN` / `NOT IN` com subquery (`NOT IN` com NULL retorna vazio).

## 6. NULLs
- `NULL = NULL` é desconhecido; use `IS NULL`, `IS DISTINCT FROM` (quando suportado) ou `COALESCE`.
- Agregações ignoram NULL (`AVG` pode enganar); `COUNT(*)` vs `COUNT(col)` diferem.

## 7. Tipos e precisão
- Valores monetários: `DECIMAL(p,s)` — nunca `FLOAT`.
- Datas: `DATE` quando não houver hora; `DATETIME2(n)` quando houver.
- Strings: `VARCHAR(n)` com tamanho adequado (evite `MAX` sem necessidade).

## 8. Carga incremental e idempotência
- Use chave natural + data de atualização (watermark) para cargas incrementais.
- Scripts de carga devem ser re-executáveis (delete+insert por período ou upsert por chave).
- Sempre registre auditoria: data de carga, origem, linhas afetadas.

## 9. Validação (checklist)
1. Contagem de linhas origem × destino.
2. Soma de métricas-chave origem × destino.
3. Unicidade de chaves de dimensão.
4. Órfãos: fatos sem dimensão correspondente (`LEFT JOIN ... WHERE dim.sk IS NULL`).
5. Intervalo de datas esperado (`MIN`/`MAX`).

## 10. Anti-patterns
- Cursores/loops para lógica de conjunto.
- Funções escalares em colunas de filtro/join.
- `DISTINCT` para "consertar" duplicidade de join (esconde o problema).
- `ORDER BY` em views/subqueries sem `TOP`.
- `NOLOCK` como padrão (lê dados sujos; no Fabric Warehouse não se aplica — isolamento é snapshot).
