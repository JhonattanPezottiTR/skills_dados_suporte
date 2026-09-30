# Catálogo de skills upstream (microsoft/skills-for-fabric)
> Última atualização: 2026-09-29 · Fonte: microsoft/skills-for-fabric v0.3.18 + Microsoft Learn · Links: https://github.com/microsoft/skills-for-fabric/tree/main/skills · https://raw.githubusercontent.com/microsoft/skills-for-fabric/main/CHANGELOG.md · https://learn.microsoft.com/en-us/fabric/fundamentals/skills-for-fabric-discover

---

## 0. Notas de versão relevantes

- **0.3.18 (2026-09-24)**: `powerbi-report-cli` ganhou drillthrough, bookmarks, buttons, custom visuals, field parameters, KPIs, model binding e preview (`powerbi-report-author preview`); nova skill `project-osmos`; `synapse-migration` passa a migrar dedicated SQL pools para Lakehouse (schema/código) ou Warehouse.
- **0.3.17**: quatro skills de report Power BI fundidas em `powerbi-report-cli`; endpoint/header do FabricIQ MCP mudaram; `ResolveReportIdFromUrl` -> `ResolveFabricItem`; field parameters em `semantic-model-authoring`.
- **0.3.16**: `apm.yml` por skill (instalação individual via APM).
- **0.3.15**: `sqldw-cli` ganhou workflow read-only de Capacity Metrics; nova `onelake-catalog-govern-cli`.
- **0.3.12**: `sqldw-*` e `eventschemaset-*` unificadas; bundles reduzidos a `fabric-skills` e `powerbi-authoring`; **`check-updates` removida (BREAKING)**.
- **0.3.11**: skills de Git integration e deployment pipelines; convenção `{item}-cli` com modos internos.
- **0.3.10**: SQL DW passa a usar a ferramenta MCP `fabric-sqlendpoint-execute_query` em vez de `sqlcmd`.

**Nomes solicitados que NÃO existem mais (404)**: `sqldw-authoring-cli`, `sqldw-consumption-cli`, `sqldw-operations-cli`, `sqldw-monitoring-cli` (hoje modos de `sqldw-cli`); `dataflows-authoring-cli`, `dataflows-consumption-cli` (hoje modos de `dataflows-cli`); `check-updates` (removida na 0.3.12). Obs.: a página Learn "Discover" ainda cita `sqldw-authoring-cli` e `eventhouse-consumption-cli` como exemplos — está desatualizada.

---

## 1. Tabela de todas as skills (pasta `skills/`, 25 pastas)

| Skill | Área | Resumo (1 linha) |
|---|---|---|
| `activator-cli` | Real-Time Intelligence | Cria/inspeciona alertas Activator (Reflex): regras, fontes, condições, ações Teams/e-mail; decodifica ReflexEntities. Modos `authoring`/`consumption`. |
| `azmon-mirroredcatalogs-operations-cli` | RTI / Observabilidade | Traz telemetria Azure Monitor/App Insights/Log Analytics ao Fabric como external delta tables no Eventhouse e correlaciona com dados de negócio. |
| `databricks-migration` | Migração | Converte notebooks/jobs Databricks (dbutils->notebookutils, DBFS->OneLake, Unity Catalog->schema-enabled Lakehouse, Jobs/DLT->SJD/Pipelines, Photon->Native Execution Engine). |
| `dataflows-cli` | Data Factory | Dataflow Gen2: criação, M, conexões, output destinations, get/updateDefinition, executeQuery, refresh; upgrade Gen1->Gen2.1. Modos `authoring`/`consumption`/`upgrade`. |
| `deployment-pipelines-authoring-cli` | ALM / CI-CD | Promoção dev/test/prod via deployment pipelines: stages, assign workspace, deploy seletivo, polling, roles. |
| `e2e-fabric-cost-estimation` | Planejamento | Estima custo de capacity antes de migração (Spark, SQL, Power BI, RTI); recomenda SKU; compara Reserved/PAYG/Autoscale. |
| `e2e-medallion-architecture` | Engenharia de dados | Planeja e constrói Bronze/Silver/Gold ponta a ponta (Lakehouse, notebooks/MLVs, pipeline, Direct Lake). |
| `eventhouse-cli` | RTI | Eventhouse/KQL DB: tabelas, funções, policies, materialized views, ingestão, KQL read-only. Modos `authoring`/`consumption`. |
| `eventschemaset-cli` | RTI | Event Schema Sets (registro de tipos de evento/schemas de payload). Modos `authoring`/`consumption`. |
| `eventstream-cli` | RTI | Eventstream: sources, operators, destinations, routing, retention, throughput, connection strings. Modos `authoring`/`consumption`. |
| `fabriciq-ontology-cli` | Fabric IQ | Ontology items: entity/relationship types, data bindings, grafo, lineage, grounding. Modos `authoring`/`consumption`. |
| `fabriciq` | Power BI / Q&A | Perguntas de negócio em linguagem natural sobre reports/semantic models existentes via FabricIQ MCP (gera DAX sozinho). |
| `git-integration-operations-cli` | ALM | Conecta workspace a Azure DevOps/GitHub; commit/update, status, conflitos, disconnect, automação SPN. |
| `hdinsight-migration` | Migração | HDInsight Spark/Hive -> Fabric (SparkSession, WASB/ABFS->OneLake shortcuts, Hive DDL->Delta, Oozie->pipelines). |
| `onelake-catalog-govern-cli` | Governança | Auditoria e remediação da saúde/proteção/confiança do catálogo OneLake (domínios, labels, tags, capacity). |
| `pipeline-migration` | Migração | Pipelines Synapse Data Factory -> Fabric Data Factory (linked services->connections, global params->Variable Libraries). |
| `powerbi-report-cli` | Power BI | Ciclo de vida de reports: requisitos, design de páginas, edição PBIR/PBIP, validação, screenshots, publish, rebind. Modos `planning`/`design`/`authoring`/`management`. |
| `project-osmos` | Engenharia de dados | Orquestra tarefas longas do Project Osmos (status, mensagens, cancel, delete) a partir de agentes locais. |
| `search-consumption-cli` | Descoberta | Catalog Search API para localizar itens em todos os workspaces e obter workspace/item IDs (não suporta Dataflow Gen1/Gen2). |
| `semantic-model-authoring` | Power BI | Semantic models: tabelas, colunas, medidas, relacionamentos, field parameters, DAX, storage modes (Import/DirectQuery/Direct Lake), refresh, deploy. |
| `spark-cli` | Engenharia de dados | Notebooks, Livy, runs, diagnóstico de falhas/OOM, ciclo de vida de Materialized Lake Views. Modos `authoring`/`consumption`/`operations`/`mlv`. |
| `sqldb-cli` | Banco de dados | SQL database do Fabric (OLTP): T-SQL via sqlcmd, vector, temporal, dacpac, Query Store. Modos `authoring`/`consumption`/`operations`. |
| `sqldw-cli` | Data Warehouse | Warehouse, SQL analytics endpoint e Mirrored DB: DDL/DML, COPY INTO, T-SQL read-only, Query Insights, correlação Capacity Metrics. Modos `authoring`/`consumption`/`operations`. |
| `synapse-migration` | Migração | Azure Synapse -> Fabric: Dedicated SQL Pool -> Lakehouse ou Warehouse, Spark, Lake Database, Linked Services. |
| `variable-library-cli` | ALM / Config | Variable Library: definições, `libraryVariables`, `valueSets`, consumidores (pipelines, notebooks, Dataflow Gen2, Copy Jobs, shortcuts...), value set ativo por stage. |

Convenções comuns: header `x-ms-fabric-skill: <skill>` em toda chamada `api.fabric.microsoft.com` (incl. polls/retries); IDs sempre por list + filtro JMESPath; SKILL.md é dispatcher — ler `references/<mode>.md` inteiro, uma vez; executar de verdade e reportar resultados reais; referências compartilhadas `common/COMMON-CLI.md` e `common/COMMON-CORE.md`.

---

## 2. `sqldw-cli` (substitui sqldw-authoring/consumption/operations/monitoring-cli)

**Propósito**: T-SQL contra Warehouse, Lakehouse SQL analytics endpoint ou Mirrored Database — DDL/DML, COPY INTO, consultas read-only, diagnósticos Query Insights, correlação de picos de CU (Capacity Metrics) com atividade SQL.

**Gatilhos**: "query warehouse", "create warehouse table", "failed or canceled query", "CU spike", "Capacity Metrics app", "custom SQL pool", "Lakehouse table health".

**Desambiguação**: SQL de migração Synapse/Dedicated Pool -> `synapse-migration`; notebook/PySpark -> `spark-cli`; SQL database OLTP -> `sqldb-cli`.

### Modos
| Modo | Escopo | Referência |
|---|---|---|
| `authoring` | DDL, DML, ingestão, transações, procedures, schema evolution, time travel (COPY INTO, OPENROWSET, INSERT/UPDATE/DELETE, MERGE, CTAS, sp_rename) | `references/authoring.md` |
| `consumption` | Leituras: SELECT, contagens, agregações, discovery, export CSV (read-only) | `references/consumption.md` |
| `operations` | Performance, falhas, capacity, SQL pools, saúde (`queryinsights.*`, `sys.sp_get_table_health_metrics`) (read-only) | `references/operations.md` + folhas em `references/operations/` |

Folhas de operations: `scenarios.md`, `query-reference.md`, `failure-analysis.md`, `pool-pressure.md`, `resource-consumers.md`, `lakehouse-health.md`, `capacity-metrics-correlation.md`.

**Regra de fronteira**: classificar por **intenção**. SELECT de descoberta para planejar um CREATE = authoring; SELECT que responde ao usuário = consumption; `queryinsights.*`/`sp_get_table_health_metrics` = operations; SELECT lento em tabela de usuário **não** é operations.

### Superfície de execução
```text
fabric-sqlendpoint-execute_query(workspaceId, itemId, query)
```
- Preferir sempre o MCP (sobrepõe a orientação SQL/TDS do COMMON-CLI). `sqlcmd` só no "Legacy CLI Fallback". `az rest` continua para discovery de control plane.
- `itemId` é **GUID**: Warehouse/Mirrored DB = item id; **Lakehouse = `properties.sqlEndpointProperties.id`** (não o id do Lakehouse).
- **Um batch por chamada**: sem `GO`, sem `:setvar`, `:r`, `-i`. Só o **último result set** retorna; um erro falha o batch inteiro.
- Retorno CSV (RFC 4180). Colunas binárias com sufixo `[base64]`.
- Limites observados (não contratuais): **10.000 linhas** (exatamente 10.000 = truncado), **300 s** timeout, **20 req/min** por identidade (HTTP 429).
- MCP global: `https://api.fabric.microsoft.com/v1/mcp/dataPlane/sqlEndpoint`; por item: `.../v1/mcp/dataPlane/workspaces/{workspaceId}/items/{itemId}/sqlEndpoint`.

### Descoberta de IDs
```bash
WS_ID=$(az rest --method get --resource "https://api.fabric.microsoft.com" \
  --url "https://api.fabric.microsoft.com/v1/workspaces" \
  --query "value[?displayName=='MyWorkspace'].id" --output tsv)

az rest --method get --resource "https://api.fabric.microsoft.com" \
  --url "https://api.fabric.microsoft.com/v1/workspaces/$WS_ID/warehouses" \
  --query "value[?displayName=='MyWarehouse'].id" --output tsv

# Lakehouse: usar o id do SQL endpoint
az rest --method get --resource "https://api.fabric.microsoft.com" \
  --url "https://api.fabric.microsoft.com/v1/workspaces/$WS_ID/lakehouses" \
  --query "value[?displayName=='MyLakehouse'].properties.sqlEndpointProperties.id" --output tsv
```

### Consumption — sequência de discovery
```sql
SELECT schema_name FROM INFORMATION_SCHEMA.SCHEMATA ORDER BY schema_name;

SELECT table_schema, table_name, table_type FROM INFORMATION_SCHEMA.TABLES
ORDER BY table_schema, table_name;

SELECT column_name, data_type, character_maximum_length, is_nullable
FROM INFORMATION_SCHEMA.COLUMNS
WHERE table_schema='dbo' AND table_name='FactSales' ORDER BY ordinal_position;

SELECT TOP 5 * FROM dbo.FactSales;

SELECT s.name AS [schema], t.name AS [table], SUM(p.rows) AS row_count
FROM sys.tables t
JOIN sys.schemas s ON t.schema_id=s.schema_id
JOIN sys.partitions p ON t.object_id=p.object_id AND p.index_id IN (0,1)
GROUP BY s.name, t.name ORDER BY row_count DESC;

SELECT name, type_desc FROM sys.objects
WHERE type IN ('V','FN','IF','P','TF') ORDER BY type_desc, name;
```
Fluxo: discover -> sample -> formulate -> execute -> iterate -> present. Boas práticas: `TOP`/`WHERE` sempre; `COUNT(*)` antes de varrer tabela grande; `TOP` + `ORDER BY` para determinismo; `SET NOCOUNT ON;` em multi-statement; `OPTION (LABEL = 'AGENTCLI_...')`; combinar leituras com JOIN/UNION ALL por causa do rate limit. Cross-database = three-part naming, **mesmo workspace**.

### Authoring — regras de DDL (erro duro se violadas)
- Sem `DEFAULT` em CREATE TABLE; PK **não** inline — adicionar depois com ALTER TABLE.
- PK/UNIQUE/FK = `NONCLUSTERED ... NOT ENFORCED`; colunas da PK `NOT NULL`.
- Sempre `DATETIME2(6)` (nunca `DATETIME2` puro).
- Tipos não suportados: `NCHAR`, `NVARCHAR`, `TEXT`, `IMAGE`, `MONEY`, `SMALLMONEY`, `DATETIME` -> use `VARCHAR`, `DECIMAL`, `DATETIME2(6)`.
- Sem `WITH (DISTRIBUTION ...)` em tabelas de usuário (distribuição automática).
- ALTER TABLE: add/drop colunas nullable e add/drop constraints NOT ENFORCED = GA; `ALTER COLUMN` = preview. `MERGE` = GA.
- Tabelas só são graváveis em **Warehouse**; SQL endpoint/Mirrored DB: só views/funções/procs/schemas; OPENROWSET só leitura.

```sql
CREATE TABLE dbo.Orders (
    OrderID INT NOT NULL,
    CustomerName VARCHAR(100) NULL,
    Amount DECIMAL(19,4) NULL,
    CreatedAt DATETIME2(6) NULL
);
ALTER TABLE dbo.Orders ADD CONSTRAINT PK_Orders PRIMARY KEY NONCLUSTERED (OrderID) NOT ENFORCED;

CREATE TABLE [dbo].[clone] AS CLONE OF [dbo].[source];

-- Variáveis em CTAS: usar SQL dinâmico
EXEC sp_executesql N'CREATE TABLE ...';

-- Readback obrigatório
SELECT table_schema, table_name FROM INFORMATION_SCHEMA.TABLES WHERE table_name = 'FactSales';
SELECT COUNT(*) AS row_count FROM dbo.FactSales;
```
**Workflow**: resolver GUIDs (`az rest --resource https://api.fabric.microsoft.com`) -> discovery de schema -> amostra `TOP 5` -> escolher padrão -> executar -> verificar. Checar `capacityId` do workspace antes de criar warehouse.

**Preferir**: CTAS a CREATE + INSERT; INSERT…SELECT a inserts linha a linha; COPY INTO para arquivos externos (maior throughput); DELETE + INSERT a MERGE quando houver escritores concorrentes; TRUNCATE a DELETE sem filtro; CTAS + `sp_rename` a UPDATEs grandes ou troca de tipo em produção; `CAST()` explícito em CTAS.
**Evitar**: `SELECT *` sem limite; `INSERT ... VALUES` em escala (gera Parquet minúsculo); `DROP TABLE IF EXISTS` + recriar (perde histórico de time travel); UPDATE/DELETE concorrentes na mesma tabela (conflito detectado em nível de tabela); MARS.

| Sintoma | Correção |
|---|---|
| Erro 24556/24706 (snapshot conflict) | Serializar escritas e retry com backoff |
| COPY INTO erro de auth | Storage Blob Data Reader no ADLS ou SAS em `CREDENTIAL` |
| COPY INTO de OneLake falha | Provisionar workspace identity; checar firewall |
| HTTP 429 | Esperar 60 s e consolidar chamadas |
| `sp_rename` falha | Só funciona em Warehouse, não em SQL endpoint |
| DB project deploy recria tabela | Aplicar ALTER TABLE manualmente |
| `queryinsights` inexistente | Warehouse com < 2 min; aguardar ~2 min |
| 403 | Precisa Viewer+ no workspace/item |
| Resultado vazio | Possível RLS; checar `USER_NAME()` |

### Operations — Query Insights e diagnósticos
- `queryinsights.*` existe em Warehouse e SQL endpoint, **sempre ligado** (não há setting de "enable"); leitura requer **Contributor+**; retenção **30 dias**; latência de até **15 min**.
- Somente SELECT; única exceção: `EXEC sys.sp_get_table_health_metrics` (apenas Lakehouse SQL endpoint, requer `VIEW DEFINITION`). Nunca `ALTER`/`CREATE`/`DROP`/SET de configuração (inclusive `ALTER DATABASE ... SET RESULT_SET_CACHING ON`).
- Citar a fonte de cada número: `2,140 ms (queryinsights.long_running_queries)`, `268 files (sys.sp_get_table_health_metrics)`; zero linhas é achado válido. Formato de resposta: **Diagnosis / Evidence / Ruled out / Recommendations / Follow-ups**.
- Labels de monitoramento `OPTION (LABEL = 'AGENTCLI_MONITOR_...')` e excluir as próprias queries: `label NOT LIKE 'AGENTCLI_MONITOR_%'`, `command NOT LIKE '%queryinsights%'`.

```sql
SELECT TOP 5 last_run_command, last_run_total_elapsed_time_ms, median_total_elapsed_time_ms, number_of_runs
FROM queryinsights.long_running_queries
ORDER BY last_run_total_elapsed_time_ms DESC;

-- Top consumidores (última hora)
SELECT TOP 5 command, total_elapsed_time_ms, allocated_cpu_time_ms,
       data_scanned_remote_storage_mb, data_scanned_memory_mb, data_scanned_disk_mb
FROM queryinsights.exec_requests_history
WHERE start_time > DATEADD(HOUR, -1, GETUTCDATE())
ORDER BY allocated_cpu_time_ms DESC;

-- Falhas/cancelamentos (janela UTC semiaberta)
DECLARE @window_end datetime2 = GETUTCDATE();
DECLARE @window_start datetime2 = DATEADD(HOUR, -24, @window_end);
SELECT
  SUM(IIF(status='Failed',1,0))   AS failed_cnt,
  SUM(IIF(status='Canceled',1,0)) AS canceled_cnt,
  COUNT(DISTINCT ISNULL(login_name,'Unknown User')) AS users_hit,
  MIN(start_time) AS first_seen, MAX(start_time) AS last_seen
FROM queryinsights.exec_requests_history
WHERE status IN ('Failed','Canceled')
  AND start_time >= @window_start AND start_time < @window_end;

-- Saúde de tabela Lakehouse (somente SQL endpoint)
EXEC sys.sp_get_table_health_metrics @table_name = 'dbo.FactSales';
```
- Mensagens de erro: resolver em `sys.messages` (`language_id = 1033`), nunca inventar texto. Categorias: conflito de transação 24556/24706; integridade 2601/2627/547; tipo/forma 511/611/8152/2628/8115/8134; authoring/schema 102/156/207/208/2812; acesso 229/916/18456.
- `sp_get_table_health_metrics` retorna só a anomalia de maior severidade (`PotentialAnomalyDescription`): 0 nenhuma, 1 estatísticas de arquivo inválidas, 2 muitas linhas deletadas, 3 muitos arquivos pequenos, 4 sem checkpoint recente. Manutenção (OPTIMIZE/checkpoint) é fora do SQL (Spark/pipelines). Falha da proc = "Not evaluated", nunca "healthy".
- **Pool pressure** (`queryinsights.sql_pool_insights`: `timestamp`, `sql_pool_name`, `is_pool_under_pressure`, `max_resource_percentage`, `current_workspace_capacity`): construir intervalos com `LEAD([timestamp], 1, @window_end) OVER (PARTITION BY sql_pool_name ORDER BY [timestamp])` e **filtrar pressure=1 depois do LEAD** (senão perde o evento que fecha o intervalo). Correlacionar requests por tempo **e** `sql_pool_name`.
- Interpretação: scan remoto alto -> layout de dados (OPTIMIZE/clustering); CPU alta vs elapsed -> CPU-bound; elapsed alto com CPU baixa -> espera/pressão. Result set caching está **desabilitado por known issue** (campos de cache só históricos); `result_cache_hit`: 1 = entrada criada, 2 = hit, 0 = nem criado nem usado.
- Limiares de referência: remoto > 1.000 MB, CPU > 5.000.000 ms, elapsed > 300.000 ms; regressão > 20% vs baseline de 7 dias.
- Clustering: só predicados `WHERE` beneficiam (não `JOIN ON` de igualdade); cardinalidade média-alta; máx. 4 colunas; aplicar com CTAS `WITH (CLUSTER BY (...))` + `sp_rename`; verificar `sys.index_columns.data_clustering_ordinal > 0`.
- **Capacity Metrics**: via skill `fabriciq`/FabricIQ MCP (`DiscoverArtifacts` "Fabric Capacity Metrics" -> `GetReportMetadata` -> `GetSemanticModelSchema` -> DAX). Nunca juntar Operation Id do Capacity Metrics com `distributed_statement_id`; CU-segundos e CPU-ms não são intercambiáveis; resultado é "best-effort". Custom SQL pools: preview, escopo de workspace, Workspace Admin, máx. 8 pools; skill só recomenda.

**Não recomendar no Fabric DW**: índices nonclustered (usar V-Order/pruning), materialized views (usar views), index hints, estatísticas multi-coluna, `ALTER TABLE SET DATA_CLUSTERING_KEY` (usar CTAS com CLUSTER BY), `RENAME OBJECT` (usar `sp_rename`), mudança de isolamento (só snapshot), `CREATE USER` (usar workspace roles), triggers, CTEs recursivas.

---

## 3. `sqldb-cli`

**Propósito**: SQL database do Fabric (engine OLTP SQL Server): T-SQL via sqlcmd, temporal, vector similarity, inspeção de schema, dacpac, Query Store, blocking, planos regredidos. Warehouse/SQL endpoint/Mirrored -> `sqldw-cli`.

| Modo | Escopo | Gatilhos | Ref |
|---|---|---|---|
| `authoring` | DDL/DML, constraints, índices, colunas vector, procs, dacpac, MERGE; cria DB só se pedido | "create sqldb table", "dacpac deploy", "create a sql database in fabric" | `references/authoring.md` |
| `consumption` | Read-only via sqlcmd: SELECT, catálogo, vector, temporal | "sqldb sys.tables", "vector similarity sqldb" | `references/consumption.md` |
| `operations` | Query Store, blocking, regressed plans, wait stats | "sqldb query store", "sqldb slow query" | `references/operations.md` |

**Endpoints/comandos**:
- Terminal write: T-SQL executado via `sqlcmd -Q` ou `-i`; novo DB = `POST /v1/workspaces/{ws}/sqlDatabases` + poll do LRO.
- sqlcmd (versão Go, não ODBC): sempre `-d <DatabaseName>` (FQDN sozinho não basta) e `-G` ou `--authentication-method` (SQL auth não funciona). FQDN via REST (`properties.serverFqdn`, `databaseName`).
- Operations pode criar `CREATE EVENT SESSION ... ON DATABASE` com target `ring_buffer` para blocking intermitente — **deve ser dropada depois**.

**Escolha de endpoint**: OLTP para dados vivos, vector, procs, temporal, políticas de segurança; SQL analytics endpoint para cross-database (three-part), agregações pesadas e BI (read-only, máx. 1000 tabelas).

**Armadilhas**: cross-database falha no endpoint OLTP; o analytics endpoint **não espelha** RLS/DDM/OLS, colunas vector/json/computed, views/procs/funções; LOBs > 1 MB truncados; 7º dígito de `datetime2(7)` cortado. Não suportado: MARS, `CREATE LOGIN`, SQL auth, `EXECUTE AS`; full-text só preview. Porta 1433 (redirect pode exigir 11000–11999). Lag de replicação: `sys.dm_change_feed_log_scan_sessions`; tabelas faltando: `sys.dm_change_feed_errors`. CSV: `-W -s"," -w 4000` + `SET NOCOUNT ON;`. JSON: `FOR JSON PATH` / `OPENJSON`.

---

## 4. `dataflows-cli` (substitui dataflows-authoring/consumption-cli)

**Propósito**: Dataflow Gen2 — criação, M, conexões, output destinations, getDefinition/updateDefinition, executeQuery, histórico de refresh, upgrade Gen1->Gen2 via `saveAsNativeArtifact`. Pipeline JSON -> `pipeline-migration`; Spark -> `spark-cli`; T-SQL -> `sqldw-cli`.

| Modo | Escopo | Ref |
|---|---|---|
| `authoring` | Criar/alterar, conexões, credenciais, preview de M antes de salvar, destinations | `references/authoring.md` |
| `consumption` | Read-only: definição, parâmetros, histórico de refresh, queries salvas/ad-hoc, parsing Arrow | `references/consumption.md` |
| `upgrade` | Gen1 -> Gen2.1 via save-as + rebind; avaliação de prontidão/risco | `references/upgrade.md` |

**Endpoints-chave**:
- Criar: `POST /v1/workspaces/{ws}/dataflows` body `{"displayName":"<displayName>"}` (201 síncrono) ou `/items`.
- Salvar: `POST .../dataflows/{df}/updateDefinition?updateMetadata=true` com `{"definition":{"parts":[{path,payload,payloadType}...]}}` (200/201 ou 202 com `Location` — sempre seguir `Location`).
- `getDefinition` é **POST** (GET = 405).
- Preview: `executeQuery` com `{"QueryName":"<shared member>"}` (formato `{"queries":[…]}` sempre falha com "Invalid query name"); `customMashupDocument` = string M UTF-8 (não base64), documento completo `section Section1; ...`. Resposta = stream **Arrow IPC**; `{"Error":"..."}` embutido = falha mesmo com HTTP 200. Não confundir com `EvaluateQuery`.
- Refresh: `POST .../jobs/instances?jobType=Refresh` body `{"executionData":{"executeOption":"ApplyChangesIfNeeded"}}` (obrigatório no 1º refresh após mudar definição).

**Partes da definição** (todas base64, `payloadType: "InlineBase64"`): `mashup.pq` (documento M), `queryMetadata.json` (`formatVersion: "202502"`, `name` = displayName, `queriesMetadata`, `connections[]`), `.platform` (`metadata.type = "Dataflow"`, `config.version "2.0"`, `logicalId` GUID). `updateDefinition` **substitui tudo** — menos de 3 partes descarta queries silenciosamente; não enviar `"format": "json"` (400 InvalidDefinitionFormat).

**Conexões**: reutilizar (`GET /v1/connections`); consultar `GET /v1/connections/supportedConnectionTypes` antes de `POST /v1/connections`; ClusterId via `https://api.powerbi.com/v2.0/myorg/me/gatewayClusterDatasources` (audience `https://analysis.windows.net/powerbi/api` sem barra). Em `queryMetadata.json` o `connectionId` é composto stringificado `{"ClusterId":"…","DatasourceId":"…"}`. Preferir `WorkspaceIdentity`/`ServicePrincipal` para refresh desassistido; nunca segredo em texto — só campos `*Reference`.

**Output destinations**: anotação `[DataDestinations = {[...]}]` na query fonte; query oculta `_DataDestination` com `loadEnabled: false` e `isHidden: true`; `IsNewTarget = true`; todas as colunas tipadas (sem `Any`).

| Destino | Kind | Função |
|---|---|---|
| Lakehouse Table | `Lakehouse` | `Lakehouse.Contents(...)` |
| Lakehouse Files | `Lakehouse` | `Lakehouse.Contents(...)` + `TypeSettings = [Kind = "File"]` |
| Warehouse | `Warehouse` | `Fabric.Warehouse(...)` |
| ADX | `AzureDataExplorer` | `AzureDataExplorer.Contents(...)` (path exato, com barra final) |
| Azure SQL | `Sql` | `Sql.Database(...)` |

```m
// trecho do exemplo (CSV via Web)
Source = Csv.Document(Web.Contents(url), [Delimiter=",", Encoding=65001, QuoteStyle=QuoteStyle.Csv]),
Promoted = Table.PromoteHeaders(Source, [PromoteAllScalars=true])
// Fast copy: [StagingDefinition = [Kind = "FastCopy"]] antes de "section"
```

**Status de refresh**: poll só em `NotStarted`/`InProgress`; `Completed` = sucesso (LRO usa `Succeeded`); `Deduped` = outro refresh rodando (não é sucesso); `Failed`/`Cancelled`/`isRetriable: false` = parar e reportar erro bruto.

**Armadilhas**: previews retornam o dataset inteiro (usar `Table.FirstN` e remover antes de salvar); `connections[]` do create só fica visível ao `executeQuery` após um `updateDefinition`; verificar binding via `getDefinition` (não `GET /items/{id}/connections`); `EntityUserFailure` costuma ser conexão faltando; PowerShell: gravar UTF-8 sem BOM (`[IO.File]::WriteAllText`) e `--body "@file"`. Upgrade: save-as só Gen1 -> Gen2.1; se origem for Gen2/desconhecida, **parar** (não há endpoint público).

---

## 5. `e2e-medallion-architecture`

**Propósito**: planejar e construir plataformas Bronze/Silver/Gold: ingestão, camadas PySpark/Delta, orquestração por pipeline, tuning Spark por camada, MLV vs notebooks, handoff Direct Lake. Perguntas sobre report existente -> `fabriciq`.

| Camada | Papel | Otimização | Particionamento | Schema |
|---|---|---|---|---|
| Bronze | Aterrissagem bruta, auditoria, reprocessamento | Escrita, append-only; V-Order off, autoCompact on | Data de ingestão | Schema-on-read |
| Silver | Deduplicado, validado, conformado | Balanceado; V-Order on, AQE, ZORDER em colunas filtradas | Data de negócio | Enforced; `mergeSchema` |
| Gold | Métricas pré-agregadas para BI/SQL | Leitura; V-Order, Optimize Write 1g, ZORDER | Mês/ano | Estrito |

```python
# Gold: antes de qualquer escrita
spark.conf.set("spark.sql.parquet.vorder.default", "true")
spark.conf.set("spark.databricks.delta.optimizeWrite.enabled", "true")
spark.conf.set("spark.databricks.delta.optimizeWrite.binSize", "1g")

# Bronze
.withColumn("source_file", input_file_name())
df.write.mode("append").partitionBy("ingestion_date").format("delta").saveAsTable("bronze.events_raw")
```

**Arquitetura**: Opção A (preferida) — um workspace `{project}-{env}`, um Lakehouse **schema-enabled** `{project}_lakehouse` com schemas `bronze`/`silver`/`gold`; MLVs disponíveis (Spark SQL MLV suporta refresh incremental; PySpark MLV só full). Opção B (legado) — workspaces `{project}-bronze-{env}` etc.; requer `spark.sql.fabric.catalog.enable-schemaless-lakehouses=true` num Environment ou nomes de 4 partes; sem MLV.

**Comandos-chave**:
```bash
az rest --method post --resource "https://api.fabric.microsoft.com" \
  --url "https://api.fabric.microsoft.com/v1/workspaces" --body @/tmp/body.json --query "id" --output tsv
# body workspace: {"displayName": "sales-analytics-dev"}
# lakehouse: POST /v1/workspaces/$workspace_id/items  {"displayName": "sales_bronze", "type": "Lakehouse"}
```
- DDL via REST: só Livy — `POST /livyApi/versions/2023-12-01/sessions` e `.../statements`.
- Notebook: `updateDefinition` com `.ipynb` em base64; cada code cell com `"outputs": []` e `"execution_count": null` (senão "Job instance failed without detail error"); binding em `metadata.dependencies.lakehouse` (`default_lakehouse`, `default_lakehouse_name`, `default_lakehouse_workspace_id`).
- Executar: `POST .../jobs/instances?jobType=RunNotebook` com `executionData.configuration.defaultLakehouse` (`id` e `name`); Bronze -> Silver -> Gold, poll até `Completed`.
- Schedule de MLV: `POST /workspaces/{workspaceId}/lakehouses/{lakehouseId}/jobs/refreshMaterializedLakeViews/schedules` (nunca inventar `/mlvRefreshSchedules`).
- Handoff Power BI: `GET /v1/workspaces/{id}/lakehouses/{goldId}` -> `properties.sqlEndpointProperties.connectionString` (aguardar `provisioningStatus = Success`) -> validar `INFORMATION_SCHEMA.TABLES` -> `POST /items` `type: "SemanticModel"` + TMDL (Direct Lake; nomes idênticos às tabelas Delta) -> `type: "Report"` PBIR via `definition.pbir` -> validar com DAX (`semantic-model-authoring`).

**Boas práticas**: incremental por watermark; um notebook por camada; OPTIMIZE/ZORDER em Silver/Gold; Variable Libraries para config; shortcuts para compartilhar Gold; completar o fluxo inteiro. **Evitar**: todas as camadas num lakehouse sem schema; pular Silver; hardcode de IDs; `SELECT *` em Bronze; VACUUM sem checar dependências; encadear shortcuts entre camadas; ler HTTP direto no Spark (`https://` não é suportado — estagiar em `Files/`).
**Inconsistências no upstream**: exemplo 1 pede workspaces separados mas cria um só; Bronze particiona por `ingestion_date` sem criá-la; usa `/Files/...` vs `Files/...`.

---

## 6. `spark-cli` (breve)

- **Propósito**: células de notebook (`%%configure`, `%%sql`, PySpark, notebookutils), runs, sessões Livy, triagem de falhas/OOM, ciclo de vida de **Materialized Lake Views** (`CREATE MATERIALIZED LAKE VIEW` e cláusula `CONSTRAINT` são exclusivos do Fabric). KQL MVs -> `eventhouse-cli`; T-SQL read-only -> `sqldw-cli`.
- **Modos**: `authoring` (células, runs, definições MLV), `consumption` (PySpark ad-hoc em Livy, read-only), `operations` (falhas/throttling/OOM, read-only), `mlv` (agendar, refresh, monitorar, cancelar MLVs). `%%sql` em notebook continua sendo authoring.
- **Endpoints**: `POST .../notebooks/{id}/updateDefinition`; novo notebook `POST /v1/workspaces/{ws}/items`; run via Jobs API; refresh MLV `POST /v1/workspaces/{ws}/lakehouses/{lakehouse}/jobs/refreshMaterializedLakeViews/instances`.
- **Armadilhas**: mostrar código não salva nem executa; pedidos vagos ("set up my data") exigem pergunta de esclarecimento.

---

## 7. `onelake-catalog-govern-cli`

**Propósito**: governar saúde, proteção e confiança do catálogo OneLake via Fabric Admin, Core e Power BI REST APIs; auditorias tenant-wide ou por owner e correções guardadas (domínios, atribuição de workspace, capacity, labels, tags, descrições, refresh, identidade de item). Descoberta de itens -> `search-consumption-cli`.

| Tier | Audit (read-only) | Remediate (write) |
|---|---|---|
| Fabric tenant admin (`/v1/admin/*`) | `admin-audit` | `admin-remediate` |
| Data owner / admin operacional (Core + Power BI APIs) | `dataowner-audit` | `dataowner-remediate` |

- Tier depende da **superfície de API**, não do cargo: `/v1/admin/*` exige Fabric administrator (Fabric admin, Power Platform admin ou M365 global admin); admins de domínio/capacity/workspace não servem.
- **Gap conhecido**: admins de domínio/workspace não-tenant não têm API para ver postura de governança do seu escopo — declarar isso logo de início.
- Sempre auditar antes de remediar; nunca usar 401/403 como motivo para contornar RBAC; informar escopo, exclusões, completude da paginação e frescor dos dados; 202 assíncrono não é conclusão.

| Operação irreversível | Gate |
|---|---|
| `DELETE /v1/admin/domains/{id}` | Checar subdomínios (`parentDomainId`) e workspaces; API não bloqueia cascata |
| Deletar tag | Reportar quantos itens a usam |
| Bulk-assign workspaces a domínio | Checar `domainId` atual (sobrescrita silenciosa); dry-run |
| Bulk sensitivity label | Dry-run antes/depois + confirmação; SPN/MI não podem |
| Assign workspace a capacity | Workspace Admin + capacity Contributor/Admin; poll do 202 |

Sem API de escrita para endorsement, DLP e deleção admin de itens -> gerar lista de escalonamento (`no-write-api-escalation.md`).

---

## 8. `git-integration-operations-cli`

**Propósito** (experimental): conectar workspace a Azure DevOps/GitHub, commit, update from Git, status, conflitos, disconnect, automação SPN. Promoção entre stages -> `deployment-pipelines-authoring-cli`.

**Ferramentas**: primária `fab api` (após `fab auth login`); fallback `az rest --resource "https://api.fabric.microsoft.com"`. Body do `fab api` só via `-i` (pipe gera o enganoso `commitToGitRequest is required`). Saída `{"status_code", "text"}`; `--show_headers` para `x-ms-operation-id`.

| Operação | Endpoint (sob `/v1/workspaces/{id}/`) |
|---|---|
| Connect | `POST git/connect` |
| Initialize | `POST git/initializeConnection` |
| Commit | `POST git/commitToGit` |
| Update | `POST git/updateFromGit` |
| Status | `GET git/status` |
| Disconnect | `POST git/disconnect` |
| Credenciais | `PATCH git/myGitCredentials` |
| Criar conexão | `POST /v1/connections` |
| Workspace relations (preview) | `POST/GET git/workspaceRelations` |
| Poll LRO | `GET operations/{id}` |

```json
// connect
{ "gitProviderDetails": { "gitProviderType": "AzureDevOps", "organizationName": "<org>", "projectName": "<proj>",
  "repositoryName": "<repo>", "branchName": "main", "directoryName": "/workspace-a" },
  "myGitCredentials": { "source": "ConfiguredConnection", "connectionId": "<guid>" } }
// initializeConnection
{"initializationStrategy":"PreferWorkspace"}   // ou PreferRemote
// commitToGit
{ "mode": "All", "workspaceHead": "<current>", "comment": "<msg>" }
// updateFromGit
{ "workspaceHead": "<h>", "remoteCommitHash": "<r>",
  "conflictResolution": { "conflictResolutionType": "Workspace", "conflictResolutionPolicy": "PreferRemote" },
  "options": { "allowOverrideItems": true } }
```
**Pré-requisitos**: capacity atribuída; Connect/disconnect = Admin; commit/update = Contributor com escrita em todos os itens; um Git op por workspace por vez; GitHub sync **desligado por padrão** no tenant; GitHub sempre exige PAT (fine-grained Contents Read/Write ou classic `repo`); SPN/desassistido exige `ConfiguredConnection`.
**LRO**: `commitToGit`, `updateFromGit` e até `git/status` podem retornar 202 -> poll `operations/{id}` e reler status. Sincronizado só quando `workspaceHead == remoteCommitHash` **e** `changes` vazio.
**Armadilhas**: API **não cria** `directoryName` inexistente (`404 GitProviderResourceNotFound`) — pré-criar `README.md` via API do provedor; conflito sem política = `400 MissingWorkspaceConflictResolution`; `400 WorkspaceHeadMismatch` = reler status; diffs fantasmas (CRLF/LF, newline final) — fixar com `.editorconfig`/`.gitattributes`; nunca humanos e automação escrevendo no mesmo branch.

---

## 9. `deployment-pipelines-authoring-cli`

**Propósito**: ALM dev/test/prod — criar stages, atribuir workspaces, deploy seletivo forward/backward, polling, role assignments. Git sync -> `git-integration-operations-cli`.

**Conceitos**: 2–10 stages (`order` a partir de 0), 1 workspace por stage e vice-versa; backward deploy só para stage vazio; pairing (autobinding) automático, visível via `sourceItemId`/`targetItemId`; **deployment/parameter rules só no portal** (sem REST); tipos não suportados são pulados silenciosamente; não há API de compare.

| Operação | Endpoint (base `https://api.fabric.microsoft.com/v1`) |
|---|---|
| Listar/criar | `GET`/`POST /deploymentPipelines` |
| Stages | `GET .../{id}/stages[/{stageId}]`, `PATCH .../stages/{stageId}` |
| Itens do stage | `GET .../stages/{stageId}/items` |
| Assign/unassign | `POST .../stages/{stageId}/assignWorkspace` / `unassignWorkspace` |
| Deploy (LRO) | `POST .../{id}/deploy` |
| Operações | `GET .../{id}/operations`, `GET .../operations/{operationId}` |
| Roles | `GET/POST/DELETE .../{id}/roleAssignments` |

```json
// deploy
{ "sourceStageId": "<s>", "targetStageId": "<t>",
  "items": [ { "sourceItemId": "<id>", "itemType": "SemanticModel" } ],
  "note": "release X",
  "options": { "allowCrossRegionDeployment": false },
  "createdWorkspaceDetails": { "name": "<ws>", "capacityId": "<cap>" } }
```
**Escopos**: leitura `Pipeline.Read.All`; CRUD `Pipeline.ReadWrite.All`; assign + `Workspace.ReadWrite.All`; deploy exige `Pipeline.Deploy` (senão 403).
**Deploy só do que mudou**: listar itens dos dois stages, parear por `targetItemId`, excluir filhos `SQLEndpoint`, `getDefinition` dos dois lados e comparar com `references/scripts/diff_item_definitions.py source.json target.json` (exit 0 idêntico / 1 alterado; normaliza IDs rebindados). Warehouse não tem definition API — comparar por presença. Deploy seletivo **não propaga deleções**.
**Armadilhas**: uma operação por pipeline (`WorkspaceMigrationOperationInProgress`); workspace recém-atribuído leva 60–120 s (`Alm_InvalidRequest_WorkloadUnavailable`); operation id vem no header `x-ms-operation-id` (usar `curl -i`/Python, `az rest` expõe mal headers); deploy copia **definições, não dados**; máx. 300 itens por deploy; nomes de pipeline únicos no tenant; `note` é write-only; unassign apaga histórico e rules do stage.

---

## 10. Skills solicitadas não encontradas

| Nome solicitado | Situação |
|---|---|
| `sqldw-authoring-cli`, `sqldw-consumption-cli`, `sqldw-operations-cli`, `sqldw-monitoring-cli` | 404 — unificadas em `sqldw-cli` (modos) na 0.3.12 |
| `dataflows-authoring-cli`, `dataflows-consumption-cli` | Não existem — modos de `dataflows-cli` |
| `check-updates` | 404 — removida na 0.3.12 (BREAKING) |
