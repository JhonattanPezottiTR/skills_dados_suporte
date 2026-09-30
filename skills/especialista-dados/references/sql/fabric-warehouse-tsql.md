# T-SQL no Fabric Warehouse e SQL analytics endpoint
> Última atualização: 2026-09-29 · Fonte: microsoft/skills-for-fabric v0.3.18 + Microsoft Learn · Links: https://learn.microsoft.com/en-us/fabric/data-warehouse/tsql-surface-area · https://learn.microsoft.com/en-us/fabric/data-warehouse/data-types · https://learn.microsoft.com/en-us/fabric/data-warehouse/table-constraints · https://learn.microsoft.com/en-us/fabric/data-warehouse/identity · https://learn.microsoft.com/en-us/fabric/data-warehouse/temp-tables · https://learn.microsoft.com/en-us/sql/t-sql/statements/copy-into-transact-sql?view=fabric · https://learn.microsoft.com/en-us/fabric/data-warehouse/time-travel · https://learn.microsoft.com/en-us/fabric/data-warehouse/statistics · https://learn.microsoft.com/en-us/fabric/data-warehouse/data-clustering · https://learn.microsoft.com/en-us/fabric/data-warehouse/query-insights · https://github.com/microsoft/skills-for-fabric/tree/main/skills/sqldw-cli

> Para SQL database no Fabric (OLTP) as regras são outras — ver skill `sqldb-cli` e "Limitations in SQL database". Este documento cobre **Warehouse** e **SQL analytics endpoint** (Lakehouse / Mirrored DB).

---

## 1. Warehouse vs SQL analytics endpoint

| Capacidade | Warehouse | SQL analytics endpoint (Lakehouse / Mirrored) |
|---|---|---|
| SELECT, views, inline TVFs, funções, procedures, schemas, permissões | Sim | Sim |
| CREATE/ALTER/DROP TABLE, INSERT/UPDATE/DELETE/MERGE, TRUNCATE | Sim | **Não** (dados são read-only; tabelas vêm das Delta do Lakehouse) |
| COPY INTO / ingestão | Sim | Não |
| OPENROWSET | Sim | Somente leitura |
| `sp_rename` | Sim | Não |
| `queryinsights.*` | Sim | Sim |
| `sys.sp_get_table_health_metrics` | Não aplicável | Sim (requer `VIEW DEFINITION`) |
| Time travel | Sim (retenção configurável) | Só com "New metadata sync (preview)"; limitado pelo vacuum retention |
| Data clustering (`CLUSTER BY`) | Sim (preview) | — |

- Ambos usam o mesmo engine SQL distribuído. Dados em Delta/Parquet no OneLake.
- Conexão TDS: `<unique-id>.datawarehouse.fabric.microsoft.com:1433`, token audience `https://database.windows.net` (SQL auth não suportada).
- Isolamento: **somente snapshot**; `SET TRANSACTION ISOLATION LEVEL` não suportado. Conflitos de escrita concorrente são detectados em **nível de tabela** (erros 24556/24706 — serializar e fazer retry com backoff).

---

## 2. Superfície T-SQL suportada (destaques)

- Tabelas, views, stored procedures, funções, permissões e security roles.
- **IDENTITY** suportado (apenas `BIGINT`, ver seção 5).
- CTEs standard, sequential e nested (nested = preview). **CTEs recursivas não suportadas.**
- `TRUNCATE TABLE` (Warehouse).
- `sp_rename` para renomear colunas/tabelas (Warehouse).
- Subconjunto de query/join hints.
- Session-scoped `#temp` tables (Warehouse).
- `MERGE` — **GA**.
- `SELECT`-first e `FROM`-first; `GROUP BY ALL` e `ORDER BY ALL`; `QUALIFY`.
- Funções analíticas: `APPROX_MEDIAN`, `APPROX_QUANTILE`, `MEDIAN`, `QUANTILE`.
- AI functions (preview) — mas tipo **vector não é suportado**.
- `ALTER TABLE` (somente):
  - `ADD` colunas **nullable** de tipos suportados; `DROP COLUMN`.
  - `ADD`/`DROP` `PRIMARY KEY`, `UNIQUE`, `FOREIGN KEY` **somente com `NOT ENFORCED`**.
  - `ALTER TABLE` em distributed temp tables.
  - `ALTER TABLE ... ALTER COLUMN` — **preview**.
  - ALTER TABLE suportado pode rodar dentro de transação explícita.
  - Há limitações ao adicionar constraints/colunas quando se usa Git integration.

### Não suportado (Learn: "não tente usar; mesmo que pareça funcionar pode causar problemas")
- `BULK LOAD` (`bcp` é preview)
- `CREATE USER` (usar workspace roles / item permissions)
- `FOR JSON` só como último operador (não em subqueries)
- Estatísticas multi-coluna criadas manualmente
- Materialized views (obs.: a página "What is Fabric Data Warehouse" menciona materialized views; a página de surface area e a skill `sqldw-cli` as listam como **não suportadas** — trate como não suportado)
- `PREDICT`
- Queries que misturam tabelas de sistema e de usuário
- Queries recursivas
- Nomes de schema/tabela com `/` ou `\`
- `SELECT ... FOR XML`
- `SET ROWCOUNT`
- `SET TRANSACTION ISOLATION LEVEL`
- `sp_showspaceused`
- Synonyms
- Triggers
- Tipo vector e funções de busca vetorial

### Complementos da skill `sqldw-cli` (não recomendar)
| Não suportado | Alternativa |
|---|---|
| Índices nonclustered | V-Order, pruning, pushdown |
| Materialized views | Views comuns |
| Index hints | Simplificar a query |
| `ALTER TABLE SET DATA_CLUSTERING_KEY` | CTAS com `CLUSTER BY` + `sp_rename` |
| `RENAME OBJECT` | `sp_rename` |
| Triggers | Pipelines ou lógica de aplicação |
| MARS | — (não suportado) |
| `DEFAULT` em CREATE TABLE | Não há default constraints |
| `WITH (DISTRIBUTION = ...)` em tabela de usuário | Distribuição automática |

---

## 3. Tipos de dados

### Suportados para tabelas (persistidos)
| Categoria | Tipos |
|---|---|
| Numéricos exatos | `bit`, `smallint`, `int`, `bigint`, `decimal`/`numeric` |
| Numéricos aproximados | `float`, `real` |
| Data e hora | `date`, `time`*, `datetime2`* |
| Strings fixas | `char` |
| Strings variáveis | `varchar` (`varchar(max)` limitado a **16 MB**) |
| Binário | `varbinary` (`varbinary(max)` limitado a 16 MB), `uniqueidentifier`** |

\* `datetime2` e `time`: no máximo **6 dígitos** de fração de segundo — escreva sempre `DATETIME2(6)` (a skill trata `DATETIME2` sem precisão como erro).
\** `uniqueidentifier` é armazenado como binário no Delta: legível no Warehouse, mas **não** no SQL analytics endpoint (aparece como binário); joins Warehouse x endpoint por `uniqueidentifier` não funcionam como esperado.

### Não suportados e alternativas
| Não suportado | Alternativa |
|---|---|
| `money`, `smallmoney` | `decimal` (não guarda a unidade monetária) |
| `datetime`, `smalldatetime` | `datetime2` |
| `datetimeoffset` | `datetime2` (pode usar `datetimeoffset` em CAST com `AT TIME ZONE`) |
| `nchar`, `nvarchar` | `char`, `varchar` (collation UTF-8; pode ocupar mais que UTF-16) |
| `text`, `ntext` | `varchar` |
| `image` | `varbinary` |
| `tinyint` | `smallint` |
| `geography`, `geometry` | par (lat, long), `varbinary` com WKB ou `varchar` com WKT |
| `json` | `varchar` |
| `xml`, CLR UDT | Sem equivalente |
| `vector` | Sem equivalente (considere AI functions) |

Tipos não suportados **podem** ser usados em variáveis, parâmetros, saída de funções/procs e uso em memória — só não em tabelas/views persistidas.

### Mapeamento Delta -> SQL no SQL analytics endpoint
| Delta | SQL |
|---|---|
| `LONG`, `BIGINT` | `bigint` |
| `BOOLEAN`, `BOOL` | `bit` |
| `INT`, `INTEGER` | `int` |
| `TINYINT`, `BYTE`, `SMALLINT`, `SHORT` | `smallint` |
| `DOUBLE` | `float` |
| `FLOAT`, `REAL` | `real` |
| `DATE` | `date` |
| `TIMESTAMP` | `datetime2` |
| `CHAR(n)` | `varchar(n)` collation `Latin1_General_100_BIN2_UTF8` |
| `VARCHAR(n)` com n < 2000 | `varchar(4*n)` collation `Latin1_General_100_BIN2_UTF8` |
| `STRING`, `VARCHAR(n)` com n >= 2000 | `varchar(8000)` (Lakehouse) / `varchar(max)` (mirrored) |
| `BINARY` | `varbinary(n)` |
| `DECIMAL`, `DEC`, `NUMERIC` | `decimal(p,s)` |

Tipos Delta fora da tabela **não aparecem** como colunas no endpoint. Atenção: a collation `..._BIN2_UTF8` é **binária** (case-sensitive) em comparações de string no endpoint.

---

## 4. Constraints (PK, UNIQUE, FK)

- Não podem ser criadas inline no `CREATE TABLE`; use `ALTER TABLE`.
- `PRIMARY KEY` e `UNIQUE`: somente `NONCLUSTERED` + `NOT ENFORCED`. `FOREIGN KEY`: somente `NOT ENFORCED`.
- Não são validadas: a unicidade/integridade é responsabilidade do ETL. Servem como metadados (ex.: para o otimizador e ferramentas).
- Sem default constraints.

```sql
CREATE TABLE dbo.DimCustomer (CustomerKey INT NOT NULL, CustomerName VARCHAR(100) NULL);
ALTER TABLE dbo.DimCustomer
  ADD CONSTRAINT PK_DimCustomer PRIMARY KEY NONCLUSTERED (CustomerKey) NOT ENFORCED;

CREATE TABLE dbo.FactSales (CustomerKey INT NOT NULL, Amount DECIMAL(19,4) NULL);
ALTER TABLE dbo.FactSales
  ADD CONSTRAINT FK_FactSales_DimCustomer FOREIGN KEY (CustomerKey)
  REFERENCES dbo.DimCustomer (CustomerKey) NOT ENFORCED;

ALTER TABLE dbo.DimCustomer
  ADD CONSTRAINT UK_DimCustomer_Name UNIQUE NONCLUSTERED (CustomerName) NOT ENFORCED;
```

---

## 5. IDENTITY

- Somente `BIGINT IDENTITY`; **sem seed/increment** customizados. Valores positivos, únicos enquanto a tabela existir (se `IDENTITY_INSERT` não for usado), **não sequenciais**, com gaps possíveis (alocação distribuída).
- Não é possível adicionar IDENTITY a tabela existente via `ALTER TABLE` — use CTAS ou `SELECT ... INTO` (que herdam a propriedade, com limitações).
- `sys.identity_columns`: `seed_value`/`increment_value` retornam NULL; `last_value` vira `-1` após o primeiro identity insert.
- `DBCC CHECKIDENT` só com `RESEED` (sem valor customizado; sem `NORESEED`).
- IDENTITY não pode ser coluna de `CLUSTER BY`.

```sql
CREATE TABLE dbo.Employees (
    EmployeeID BIGINT IDENTITY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50)
);
INSERT INTO dbo.Employees (FirstName, LastName) VALUES ('Ensi', 'Vasala');

-- Membro "Unknown" (-1) em dimensão
SET IDENTITY_INSERT dbo.Employees ON;
INSERT INTO dbo.Employees (EmployeeID, FirstName, LastName) VALUES (-1, 'Unknown', 'Unknown');
SET IDENTITY_INSERT dbo.Employees OFF;
DBCC CHECKIDENT('dbo.Employees', RESEED);

-- COPY INTO com valores explícitos
COPY INTO dbo.Employees (EmployeeID 1, FirstName 2, LastName 3)
FROM 'https://myaccount.blob.core.windows.net/myblobcontainer/folder1/'
WITH (FILE_TYPE = 'CSV', IDENTITY_INSERT = 'ON');
```
Com `IDENTITY_INSERT ON`: lista de colunas obrigatória e só uma tabela por sessão.

---

## 6. Temp tables

- Session-scoped `#temp` (Warehouse); invisíveis a outras sessões; dropadas no fim da sessão. **`##global` não suportado.**
- Dois tipos:
  - Não distribuída (MDF-backed, padrão): `CREATE TABLE #t (...)` — não aceita `ALTER TABLE`.
  - **Distribuída (Parquet-backed, recomendada)**: `WITH (DISTRIBUTION = ROUND_ROBIN)` — alinhada a tabelas normais (armazenamento ilimitado, tipos e operações T-SQL). A skill orienta usar ROUND_ROBIN quando precisar de `INSERT INTO ... SELECT`.
- Time travel (`FOR TIMESTAMP AS OF`) não afeta temp tables.

```sql
CREATE TABLE #stg_vendas (
    VendaID BIGINT,
    DataVenda DATE,
    Valor DECIMAL(19,4)
) WITH (DISTRIBUTION = ROUND_ROBIN);

INSERT INTO #stg_vendas SELECT VendaID, DataVenda, Valor FROM dbo.FactSales WHERE DataVenda >= '2026-01-01';
```

---

## 7. Ingestão: COPY INTO, OPENROWSET, CTAS

### COPY INTO (forma recomendada, maior throughput)
- Formatos no Fabric: **CSV, JSONL, PARQUET**. Fontes: ADLS Gen2, Azure Blob Storage, **OneLake**.
- Roda no contexto de segurança SQL do usuário; `CREDENTIAL = (IDENTITY = 'Workspace Identity')` só autoriza o acesso à fonte.
- Credenciais: storage público -> Entra ID, SAS ou Storage Account Key; storage com firewall -> Entra ID ou Workspace Identity; OneLake -> Entra ID ou Workspace Identity (SAS/chave/connection string **não**). Contas privadas (public network access desabilitado) **não suportadas**, mesmo com private links.
- Opções principais: `FILE_TYPE`, `CREDENTIAL`, `ERRORFILE` (CSV/JSONL; cria `_rejectedrows`), `ERRORFILE_CREDENTIAL` (só SAS), `MAXERRORS` (CSV/JSONL; **não** com PARQUET), `FIRSTROW` (CSV), `FIELDTERMINATOR`, `ROWTERMINATOR`, `FIELDQUOTE`, `ENCODING`, `COMPRESSION`, `PARSER_VERSION` (`'2.0'` padrão; CSV comprimido/UTF-16 cai para 1.0; terminadores multicaractere exigem `'1.0'`), `MATCH_COLUMN_COUNT` (`OFF` padrão), `IDENTITY_INSERT`.
- Padrões: `MAXERRORS = 0`, `FIELDQUOTE = '"'`, `FIELDTERMINATOR = ','`, `ROWTERMINATOR = '\n'` (tratado como `\r\n`), `FIRSTROW = 1`, `ENCODING = 'UTF8'`, `FILE_TYPE = 'CSV'`.
- Wildcards permitidos (recursivos); arquivos iniciados por `_` ou `.` são ignorados. Evite wildcards que expandem para muitos arquivos.
- Limites: Parquet — coluna `varchar(max)`/`varbinary(max)` até 16 MB, linha até 1 GB; CSV/JSONL — coluna até 1 MB, linha até 16 MB. Precisão maior que a coluna destino é **truncada** (não arredondada).
- OneLake como fonte: caminho com **IDs** (`https://onelake.dfs.fabric.microsoft.com/<workspaceId>/<lakehouseId>/Files/...`), Warehouse não pode ser fonte; com Entra ID do usuário -> Contributor nos dois workspaces; com Workspace Identity -> identity com Contributor no workspace fonte, usuário com Viewer no destino + `INSERT` na tabela.
- Permissões data plane (usuário só com Read): `GRANT ADMINISTER DATABASE BULK OPERATIONS` + `GRANT INSERT`.
- Sensitivity labels restritivos no destino podem fazer o COPY falhar. Não altere os arquivos durante a carga. Data scanned aparece como 0 no Query Insights para COPY INTO.

```sql
-- Parquet público
COPY INTO dbo.TaxiTrips
FROM 'https://azureopendatastorage.blob.core.windows.net/nyctlc/yellow'
WITH (FILE_TYPE = 'PARQUET');

-- CSV com SAS, arquivo de rejeitados
COPY INTO dbo.test_1
FROM 'https://myaccount.blob.core.windows.net/myblobcontainer/folder1/'
WITH (
    FILE_TYPE = 'CSV',
    CREDENTIAL = (IDENTITY = 'Shared Access Signature', SECRET = '<Your_SAS_Token>'),
    FIELDQUOTE = '"',
    FIELDTERMINATOR = ';',
    ROWTERMINATOR = '0X0A',
    ENCODING = 'UTF8',
    MAXERRORS = 10,
    ERRORFILE = '/errorsfolder'
);

-- OneLake (Files de um Lakehouse), pulando cabeçalho
COPY INTO dbo.t1
FROM 'https://onelake.dfs.fabric.microsoft.com/<workspaceId>/<lakehouseId>/Files/*.csv'
WITH (FILE_TYPE = 'CSV', FIRSTROW = 2);

-- Workspace Identity (storage com firewall / OneLake)
COPY INTO dbo.SalesOrders
FROM 'https://<account>.dfs.core.windows.net/<container>/sales/*.parquet'
WITH (FILE_TYPE = 'PARQUET', CREDENTIAL = (IDENTITY = 'Workspace Identity'));

-- JSONL com mapeamento de campos
COPY INTO dbo.Countries (
  CountryID '$.CountryKey', CountryName '$.CountryName', RegionID '$.RegionKey', Population '$.Population'
)
FROM 'https://myaccount.blob.core.windows.net/myblobcontainer/folder1/countries.jsonl'
WITH (FILE_TYPE = 'JSONL');

SELECT COUNT_BIG(*) FROM dbo.TaxiTrips;  -- verificação
```
`BULK INSERT` também é suportado (reuso de código SQL Server), mas `COPY INTO` é o recomendado para código novo.

### OPENROWSET(BULK) — explorar arquivos antes de ingerir
- Lê Parquet, CSV e JSONL de Blob, ADLS ou OneLake (**OneLake = preview**). Formato inferido pela extensão (`.parquet`, `.csv`, `.jsonl`/`.ldjson`/`.ndjson`); caso contrário `FORMAT = '...'`.
```sql
SELECT TOP 10 *
FROM OPENROWSET(BULK 'https://onelake.dfs.fabric.microsoft.com/<workspaceId>/<lakehouseId>/Files/latest/<file>.jsonl') AS data;

SELECT *
FROM OPENROWSET(BULK 'https://<account>.blob.core.windows.net/public/<sub>/<file>.csv',
                FORMAT = 'CSV', HEADER_ROW = TRUE, ROWTERMINATOR = '\n', FIELDTERMINATOR = ',') AS data;

-- Descobrir schema
EXEC sp_describe_first_result_set
N'SELECT TOP 0 * FROM OPENROWSET(BULK ''https://<account>.blob.core.windows.net/public/<sub>/<file>.parquet'') AS data';

-- Schema explícito com WITH
SELECT TOP 10 *
FROM OPENROWSET(BULK 'https://<account>.blob.core.windows.net/public/<sub>/<file>.csv') AS data
WITH (updated date, id int, confirmed int, country_region varchar(8000)) AS data;
```

### CTAS, SELECT INTO, CLONE, sp_rename
```sql
-- CTAS com CAST explícito (controla tipos de saída)
CREATE TABLE dbo.FactSales_New
AS
SELECT CAST(OrderID AS INT) AS OrderID,
       CAST(Amount AS DECIMAL(19,4)) AS Amount,
       CAST(OrderDate AS DATE) AS OrderDate
FROM dbo.FactSales_Staging;

-- Troca atômica em vez de UPDATE massivo / mudança de tipo
EXEC sp_rename 'dbo.FactSales', 'FactSales_Old';
EXEC sp_rename 'dbo.FactSales_New', 'FactSales';

-- Zero-copy clone
CREATE TABLE [dbo].[FactSales_Clone] AS CLONE OF [dbo].[FactSales];

-- CTAS com variáveis: usar SQL dinâmico
EXEC sp_executesql N'CREATE TABLE dbo.X AS SELECT ...';
```
Boas práticas (skill `sqldw-cli`): CTAS > CREATE + INSERT; `INSERT ... SELECT` > inserts linha a linha (geram Parquet minúsculo); TRUNCATE > DELETE sem filtro; DELETE + INSERT > MERGE com escritores concorrentes; `DROP TABLE IF EXISTS` + recriar **perde o histórico de time travel**; transações curtas; `SET NOCOUNT ON;`.

---

## 8. Cross-database queries

- Three-part naming (`database.schema.table`) entre Warehouses, SQL analytics endpoints e mirrored DBs **do mesmo workspace**.
- A query aparece no Query Insights do item em cujo contexto foi executada.
```sql
SELECT c.RecordTypeID, a.AffiliationName
FROM ContosoLakehouse.dbo.ContosoSalesTable AS c
INNER JOIN My_lakehouse.dbo.Affiliation AS a
    ON a.AffiliationId = c.RecordTypeID;

-- Carga do endpoint do Lakehouse para o Warehouse
INSERT INTO ContosoWarehouse.dbo.Affiliation
SELECT * FROM My_Lakehouse.dbo.Affiliation;
```

---

## 9. Time travel

- `OPTION (FOR TIMESTAMP AS OF 'YYYY-MM-DDTHH:MM:SS[.fff]')` no nível de statement; afeta todas as tabelas do SELECT. Resultado read-only (sem INSERT/UPDATE/DELETE).
- **UTC** apenas; no máximo **3 dígitos** de fração (senão Msg 22440). Use `CONVERT` com style 126.
- Retenção do Warehouse: padrão **30 dias**, configurável de **1 a 120 dias**. SQL endpoint: limitado pelo vacuum retention da tabela e só com "New metadata sync (preview)".
- Retorna o **schema mais recente**; colunas criadas depois do timestamp falham. Drop + recreate apaga o histórico.
- Só em queries que começam com `SELECT`; uma vez por statement; valor determinístico; não pode estar na definição de view (mas pode consultar a view com o hint); pode ser usado dentro de stored procedure. Não suportado no Power BI Desktop DirectQuery nem em "Explore this data".
- Permissão: Admin/Member/Contributor/Viewer; RLS/CLS/DDM continuam aplicados.
```sql
SELECT CustomerKey, CustomerName
FROM dbo.DimCustomer
OPTION (FOR TIMESTAMP AS OF '2026-09-01T00:00:00.000');
```
Alternativa em nível de tabela: `CREATE TABLE ... AS CLONE OF ...` (clone table).

---

## 10. Estatísticas

- Automáticas no momento da query (histograma `_WA_Sys_*`, average column length `ACE-AverageColumnLength_*` para varchar > 100, cardinalidade `ACE-Cardinality`), de forma síncrona (podem somar tempo à primeira execução). Refresh incremental e **proactive statistics refresh** (ligado por padrão, configurável via `ALTER DATABASE`).
- Manuais: **somente single-column** (multi-coluna não suportado).
```sql
CREATE STATISTICS DimCustomer_CustomerKey_FullScan ON dbo.DimCustomer (CustomerKey) WITH FULLSCAN;
UPDATE STATISTICS dbo.DimCustomer (DimCustomer_CustomerKey_FullScan) WITH FULLSCAN;
DBCC SHOW_STATISTICS ("dbo.DimCustomer", "DimCustomer_CustomerKey_FullScan") WITH HISTOGRAM;
DROP STATISTICS dbo.DimCustomer.DimCustomer_CustomerKey_FullScan;

-- Inventário de estatísticas automáticas
SELECT object_name(s.object_id) AS [object_name], c.name AS column_name, s.name AS stats_name,
       STATS_DATE(s.object_id, s.stats_id) AS stats_update_date, s.auto_created, s.user_created
FROM sys.stats AS s
JOIN sys.objects AS o ON o.object_id = s.object_id
LEFT JOIN sys.stats_columns AS sc ON s.object_id = sc.object_id AND s.stats_id = sc.stats_id
LEFT JOIN sys.columns AS c ON sc.object_id = c.object_id AND c.column_id = sc.column_id
WHERE o.type = 'U' AND s.auto_created = 1 AND o.name = '<YOUR_TABLE_NAME>';
```
Crie manualmente em colunas muito usadas em GROUP BY, ORDER BY, filtros e JOINs; atualize após mudanças grandes de volume/distribuição.

---

## 11. Data clustering (preview, Warehouse)

- Definido **na criação** da tabela com `WITH (CLUSTER BY (...))` — 1 a **4 colunas**; não dá para converter tabela existente nem mudar as colunas depois (use CTAS). `SELECT INTO` com clustering não suportado. Ordem das colunas não importa.
- Tipos suportados: `bigint`, `int`, `smallint`, `decimal`, `numeric`, `float`, `real`, `date`, `datetime2`, `time`, `char`, `varchar`. Não: `bit`, `varchar(max)`, `varbinary(max)`, `varbinary`, `uniqueidentifier`, IDENTITY. Strings: só os 32 primeiros caracteres entram nas estatísticas; `decimal` com precisão > 18 não tem pushdown.
- Beneficia predicados `WHERE` (range, alta cardinalidade) em tabelas grandes; **joins de igualdade não se beneficiam**. DMLs de pelo menos ~1 milhão de linhas para melhor efeito; ingestão fica mais cara em CU.
```sql
CREATE TABLE dbo.Sales (
    SaleID INT, CustomerID INT, SaleDate DATE, Amount DECIMAL(10,2)
) WITH (CLUSTER BY (CustomerID, SaleDate));

CREATE TABLE dbo.Sales_CTAS WITH (CLUSTER BY (SaleDate)) AS SELECT * FROM dbo.Sales;

SELECT t.name AS table_name, c.name AS column_name, ic.data_clustering_ordinal
FROM sys.tables t
JOIN sys.columns c ON t.object_id = c.object_id
JOIN sys.index_columns ic ON c.object_id = ic.object_id AND c.column_id = ic.column_id
WHERE ic.data_clustering_ordinal > 0
ORDER BY t.name, ic.data_clustering_ordinal;
```

---

## 12. Monitoramento: Query Insights (`queryinsights.*`)

- Disponível em Warehouse e SQL analytics endpoint; sempre ativo; **30 dias** de histórico; até **15 min** de atraso; só queries de usuário (não de sistema); texto completo visível para Admin/Member/Contributor (a skill exige Contributor+). Warehouse com menos de ~2 min ainda não tem o schema.
- Queries com mesmo "shape" (predicados parametrizados) são agregadas por `query_hash`.

| View | Conteúdo |
|---|---|
| `queryinsights.exec_requests_history` | Cada request concluído (`distributed_statement_id`, `login_name`, `command`, `start_time`, `end_time`, `status`, `error_code`, `total_elapsed_time_ms`, `allocated_cpu_time_ms`, `data_scanned_remote_storage_mb`/`_memory_mb`/`_disk_mb`, `result_cache_hit`, `label`, `program_name`, `sql_pool_name`, `statement_type`, `query_hash`) |
| `queryinsights.exec_sessions_history` | Sessões concluídas |
| `queryinsights.long_running_queries` | Por tempo de execução (`median_total_elapsed_time_ms`, `last_run_total_elapsed_time_ms`, `number_of_runs`, `last_run_command`) |
| `queryinsights.frequently_run_queries` | Mais executadas (`number_of_runs`, `number_of_successful_runs`, `avg_total_elapsed_time_ms`) |
| `queryinsights.sql_pool_insights` | Alocação de recursos, mudanças de configuração e pressão dos SQL pools (`is_pool_under_pressure`, `max_resource_percentage`, `current_workspace_capacity`) |
| `queryinsights.external_api_call_stats` | Diagnóstico por função para queries que chamam APIs externas via AI functions |

```sql
-- Minhas queries dos últimos 30 minutos
SELECT distributed_statement_id, status, total_elapsed_time_ms, command
FROM queryinsights.exec_requests_history
WHERE start_time >= DATEADD(MINUTE, -30, GETUTCDATE()) AND login_name = USER_NAME();

-- Top CPU
SELECT TOP 100 distributed_statement_id, query_hash, allocated_cpu_time_ms, label, command
FROM queryinsights.exec_requests_history
ORDER BY allocated_cpu_time_ms DESC;

-- Scan remoto vs cache
SELECT TOP 50 distributed_statement_id, query_hash, data_scanned_remote_storage_mb,
       data_scanned_memory_mb, data_scanned_disk_mb, label, command
FROM queryinsights.exec_requests_history
ORDER BY data_scanned_remote_storage_mb DESC;

-- Falhas por código nas últimas 24 h
SELECT TOP 20 status, error_code, COUNT(*) AS requests, COUNT(DISTINCT login_name) AS users
FROM queryinsights.exec_requests_history
WHERE status IN ('Failed','Canceled') AND start_time >= DATEADD(HOUR, -24, GETUTCDATE())
GROUP BY status, error_code
ORDER BY requests DESC
OPTION (LABEL = 'MONITOR_FAILURES');

-- Efeito de clustering numa execução específica
SELECT allocated_cpu_time_ms, data_scanned_disk_mb, data_scanned_memory_mb, data_scanned_remote_storage_mb
FROM queryinsights.exec_requests_history
WHERE distributed_statement_id = '<Query_Statement_ID>';
```
- Lakehouse (SQL endpoint): `EXEC sys.sp_get_table_health_metrics @table_name = 'dbo.FactSales';` (anomalias: small files, deleted rows, invalid stats, sem checkpoint — manutenção via Spark/OPTIMIZE, fora do SQL).
- Interpretação (skill `sqldw-cli`): scan remoto alto -> layout (clustering/OPTIMIZE); CPU alta -> simplificar joins/colunas; elapsed alto com CPU baixa -> pressão do pool (checar `sql_pool_insights`); comparar cold vs warm cache antes de concluir que a query é lenta. Result set caching está desabilitado por known issue — trate `result_cache_hit` como histórico.

---

## 13. Checklist de performance

1. Tipos enxutos: `varchar(n)` dimensionado (evite `varchar(max)`), `DATETIME2(6)`, `DECIMAL` com precisão adequada (<= 18 favorece pushdown).
2. Cargas em lote (COPY INTO / CTAS / `INSERT ... SELECT`); nunca `INSERT ... VALUES` em loop.
3. Clustering nas colunas de filtro `WHERE` recorrentes de tabelas grandes (CTAS + `sp_rename`).
4. Estatísticas single-column em colunas de filtro/join após cargas grandes.
5. Evitar UPDATE/DELETE concorrentes na mesma tabela; serializar ou usar DELETE + INSERT.
6. `TOP`/`WHERE` sempre; `COUNT(*)` antes de varrer; rotular com `OPTION (LABEL = '...')` para rastrear no Query Insights.
7. Lakehouse: manter tabelas Delta saudáveis (OPTIMIZE/V-Order no Spark) — o endpoint é read-only.
8. Via MCP da skill: um batch por chamada, sem `GO`, limite de 10.000 linhas / 300 s / 20 req/min.
