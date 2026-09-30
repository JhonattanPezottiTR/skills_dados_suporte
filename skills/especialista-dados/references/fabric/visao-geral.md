# Visão geral: Microsoft Fabric e Skills for Fabric
> Última atualização: 2026-09-29 · Fonte: microsoft/skills-for-fabric v0.3.18 + Microsoft Learn · Links: https://github.com/microsoft/skills-for-fabric · https://learn.microsoft.com/en-us/fabric/fundamentals/skills-for-fabric-overview · https://learn.microsoft.com/en-us/fabric/fundamentals/skills-for-fabric-discover · https://github.com/microsoft/skills-for-fabric/blob/main/mcp-setup/README.md · https://learn.microsoft.com/en-us/fabric/data-warehouse/data-warehousing

---

## 1. O que é o Microsoft Fabric (resumo operacional)

Hierarquia (conforme `common/COMMON-CORE.md` do repositório):

| Nível | Descrição |
|---|---|
| **Tenant** | Uma instância do Fabric por organização, ligada a um único tenant Entra ID. |
| **Capacity** | Pool de computação F-SKU ou P-SKU. **Todo workspace precisa estar atribuído a uma capacity** (sem ela, várias APIs falham, ex.: `WorkspaceHasNoCapacityAssigned` na Git integration). |
| **Workspace** | Contêiner de itens; fronteira de colaboração e segurança. "My workspace" é pessoal, não tem workspace identity e não pode ser compartilhado. |
| **Item** | Artefato dentro do workspace, identificado por GUID (`itemId`). |
| **OneLake** | Data lake único do tenant. Todo item armazena dados como arquivos Delta/Parquet. |

### Itens de dados principais

| Item | O que é | Escrita via T-SQL? |
|---|---|---|
| **Lakehouse** | Armazenamento Delta (pastas `Files/` e `Tables/`), desenvolvido principalmente com Spark. Ao criar, provisiona automaticamente um **SQL analytics endpoint**; a resposta REST traz `sqlEndpointProperties`, `oneLakeFilesPath`, `oneLakeTablesPath`. | Não (endpoint é read-only para dados) |
| **SQL analytics endpoint** | Visão "SQL" do Lakehouse (também provisionado para Warehouse, SQL database e mirrored items). Permite consultar tabelas Delta, criar views, inline TVFs, procedures e gerenciar permissões, **mas não manipular dados**. | Não (somente views/funções/procs/schemas/permissões) |
| **Warehouse** | Data warehouse relacional "lake warehouse", desenvolvido em T-SQL, com transações ACID multi-tabela, DDL e DML completos. Dados em Delta no OneLake. Ideal para star/snowflake schemas, data marts curados. | Sim |
| **Mirrored Database** | Réplica espelhada de fonte externa; consultável via SQL analytics endpoint. | Não |
| **SQL database (Fabric)** | Banco OLTP com engine SQL Server (tabelas, índices, constraints, vector, temporal, Query Store). TDS porta 1433. Também gera um SQL analytics endpoint (read-only, espelha no máx. 1000 tabelas). | Sim (OLTP) |
| **Eventhouse / KQL Database** | Real-Time Intelligence; KQL para séries temporais e tempo real. URIs de cluster/ingestão por item (`https://trd-<hash>.z<n>.kusto.fabric.microsoft.com`). | KQL management commands |
| **Eventstream** | Topologia de streaming (sources, operators, destinations). | — |
| **Dataflow Gen2** | Power Query M no Fabric; definição com partes `mashup.pq`, `queryMetadata.json`, `.platform`; output destinations (Lakehouse, Warehouse, ADX, Azure SQL). | — |
| **Data Pipeline** | Orquestração (Copy, Notebook, etc.); `jobType=Pipeline`. | — |
| **Notebook / Spark Job Definition / Environment** | Engenharia de dados com Spark/PySpark; `jobType=RunNotebook`. | — |
| **Semantic model** | Modelo Power BI (Import, DirectQuery, Direct Lake); definição TMDL via `updateDefinition`. | — |
| **Report** | Relatório Power BI (formato PBIR), referencia o modelo via `definition.pbir`. | — |

**Direct Lake**: modo de armazenamento de semantic models que lê as tabelas Delta do OneLake diretamente. No padrão medallion das skills, o semantic model é criado em Direct Lake sobre a camada Gold, e **nomes de tabelas/colunas devem bater exatamente com as tabelas Delta**.

### Warehouse vs Lakehouse (Microsoft Learn)
- Escolha **Warehouse** quando precisar de solução enterprise, "no knobs", dados estruturados/semiestruturados, DDL/DML T-SQL completos.
- Escolha **Lakehouse** para grande repositório de dados não estruturados de fontes heterogêneas, com Spark como ferramenta principal; o SQL analytics endpoint cobre relatórios T-SQL.
- Ambos usam **o mesmo engine SQL** para todas as consultas T-SQL. Cross-database queries (three-part naming) funcionam **dentro do mesmo workspace**.

### URLs de ambiente (nuvem pública)

| Serviço | URL |
|---|---|
| Fabric REST | `https://api.fabric.microsoft.com/v1/` |
| OneLake DFS | `https://onelake.dfs.fabric.microsoft.com` (regional: `<region>-onelake...`) |
| OneLake Blob | `https://onelake.blob.fabric.microsoft.com` |
| OneLake API | `https://api.onelake.fabric.microsoft.com` |
| Warehouse / SQL endpoint (TDS) | `<unique-id>.datawarehouse.fabric.microsoft.com:1433` |
| SQL Database (TDS) | `<unique-id>.database.windows.net:1433` (COMMON-CORE). Obs.: a referência `sqldb-cli/consumption.md` cita o padrão `<endpoint>.database.fabric.microsoft.com` — descubra o FQDN via REST (`properties.serverFqdn`), nunca hardcode. |
| XMLA | `powerbi://api.powerbi.com/v1.0/myorg/<workspace>` |
| Power BI REST | `https://api.powerbi.com/v1.0/myorg/` |
| Entra token | `https://login.microsoftonline.com/<tenantId>/oauth2/v2.0/token` |

---

## 2. O que são as Skills for Fabric

- Instruções reutilizáveis (arquivos `SKILL.md`, open source, licença MIT) que ensinam ferramentas de IA (GitHub Copilot CLI, VS Code, Claude Code, Cursor, Windsurf, Codex/Jules/OpenCode) a trabalhar com workloads do Fabric: quais REST APIs chamar, sintaxe de query (T-SQL, KQL, PySpark, M, DAX), autenticação e boas práticas.
- Cada `SKILL.md` define: gatilhos/intenções, APIs/comandos/sintaxe, setup de autenticação/ambiente, boas práticas.
- **Skills são conhecimento estático; não executam código.** A ferramenta de IA decide as ações.
- Fluxo: intenção do usuário -> ferramenta de IA casa o prompt com a skill -> skill fornece endpoints/sintaxe/auth -> ferramenta chama APIs do Fabric -> recurso criado/alterado.
- Observação do Learn: as skills produzem definições de itens e código de movimentação de dados, **mas não renderizam relatórios Power BI finalizados** (para visualização: dashboard Python local, PDF, ou relatório manual sobre o semantic model gerado). A partir da 0.3.17/0.3.18 existe `powerbi-report-cli` para edição PBIR/PBIP.
- Versão atual: **0.3.18 (2026-09-24)**.

### Convenções comuns a todas as skills (v0.3.18)
- Nomenclatura `{item}-cli` com **modos internos** (ex.: `sqldw-cli` com `authoring` / `consumption` / `operations`). Desde a 0.3.11/0.3.12 as antigas skills separadas (`sqldw-authoring-cli`, `sqldw-consumption-cli`, `eventschemaset-*` etc.) foram **unificadas**. `check-updates` foi **removida na 0.3.12 (BREAKING)**.
- O `SKILL.md` é um **dispatcher de modos, sem procedimentos**: escolha um modo e leia `references/<mode>.md` inteiro antes de executar.
- **Header de telemetria obrigatório** em toda chamada a `api.fabric.microsoft.com` (inclusive polls de LRO e retries): `x-ms-fabric-skill: <nome-da-skill>`. Com `az rest`: `--headers "x-ms-fabric-skill=sqldw-cli"`.
- **Nunca adivinhar GUIDs**: listar workspaces/itens e filtrar por `displayName` com JMESPath.
- "Terminal write": mostrar SQL/código no chat não persiste nada; é preciso executar e ler de volta (readback).

### Skills vs MCP (Microsoft Learn)

| Aspecto | Skills | MCP servers |
|---|---|---|
| **Propósito** | Fornecem conhecimento e padrões | Fornecem acesso a dados ao vivo |
| **Conteúdo** | Documentação Markdown | Servidores executáveis |
| **Runtime** | Carregadas no contexto da IA | Rodam como processos separados |
| **Exemplo** | "Como consultar um warehouse" | "Execute esta query SQL" |

Resumo: *skills ensinam o que fazer; MCP servers fazem*. Funcionam melhor juntos.

---

## 3. Bundles (plugins)

| Bundle | Conteúdo |
|---|---|
| `fabric-skills` | Bundle completo do Fabric: authoring, consumption, operations, migration, arquitetura end-to-end (SQL DW, Spark/Lakehouse, semantic models, Eventhouse/KQL, Eventstreams, Dataflows Gen2, catalog search, migração, medallion). |
| `powerbi-authoring` | Semantic models, reports e fluxos PBIP do Power BI (planejamento, design e gestão de relatórios). Plugin stdio separado. |

- Os bundles antigos por persona (`fabric-authoring`, `fabric-consumption`, `fabric-operations`) foram **aposentados**; os ids ainda funcionam como aliases deprecados de `fabric-skills`.

### Instalação
```bash
# GitHub Copilot CLI
/plugin marketplace add microsoft/skills-for-fabric
/plugin install fabric-skills@fabric-collection
/plugin install powerbi-authoring@fabric-collection
/plugin update fabric-skills@fabric-collection
copilot plugin update --all

# Claude Code
claude plugin marketplace add microsoft/skills-for-fabric
claude plugin install fabric-skills@fabric-collection
claude plugin update fabric-skills@fabric-collection
claude mcp list        # ou /mcp dentro do Claude

# Skill individual via APM (Agent Package Manager) - desde 0.3.16
apm install microsoft/skills-for-fabric --skill sqldw-cli --target <tool>
```
- APM: flags `--skill` (repetível), `--target/-t` (copilot, claude, cursor, codex...), `--global/-g`, `--only apm|mcp`, `--update`, `--dry-run`, `--verbose`. Skills vão para `.agents/skills/<name>/`; material compartilhado em `apm_modules/`. Instale o repositório e restrinja com `--skill` (instalar o caminho da skill direto quebra links de referência). Todos os MCP servers do Fabric são registrados independentemente da skill escolhida (use `--only apm` para pular).
- Auto-update no Copilot CLI: `"autoUpdate": true` na entrada `fabric-collection` em `extraKnownMarketplaces` de `~/.copilot/settings.json` (source `{ "source": "github", "repo": "microsoft/skills-for-fabric" }`); só vale em settings pessoais.
- Outras ferramentas: ao clonar o repo, são auto-detectados `CLAUDE.md`, `.cursorrules`, `.windsurfrules`, `AGENTS.md`, `GEMINI.md`.
- Listar skills instaladas: `/env` (Copilot CLI / Claude Code); detalhes: `/skills info <skill-name>`.

---

## 4. Agentes (agent specializations, experimentais)

Pasta `agents/` do repositório (5 arquivos):

| Agente | Arquivo |
|---|---|
| `FabricAdmin` | `agents/FabricAdmin.agent.md` (administração) |
| `FabricAppDev` | `agents/FabricAppDev.agent.md` (desenvolvimento de apps) |
| `FabricDataEngineer` | `agents/FabricDataEngineer.agent.md` (engenharia de dados) |
| `FabricIQ` | `agents/FabricIQ.agent.md` |
| `FabricMigrationEngineer` | `agents/FabricMigrationEngineer.agent.md` (migração) |

Uso no Copilot CLI:
```text
Using FabricAdmin, document my Workspace FabricCLIDemo
@FabricDataEngineer help me design a medallion architecture for my lakehouse
```
`/agent` lista agentes instalados. Agentes podem referenciar skills não instaladas (ficam inertes até instalar).

---

## 5. MCP servers (mcp-setup/README.md)

| Nome | Endpoint | Headers extras |
|---|---|---|
| **FabricIQ** | `https://fabriciq.svc.cloud.microsoft/v1/mcp/fabriciq` | `X-VARIANTS: Fabric.Routing.FabricIQ.V1` |
| **powerbi-modeling-mcp** | `https://api.fabric.microsoft.com/v1/mcp/powerbi/authoring` | — |
| **fabric-sqlendpoint** | `https://api.fabric.microsoft.com/v1/mcp/dataPlane/sqlEndpoint` | — |

- SQL endpoint MCP com escopo de item: `https://api.fabric.microsoft.com/v1/mcp/dataPlane/workspaces/{workspaceId}/items/{itemId}/sqlEndpoint`.
- Ferramenta SQL: `fabric-sqlendpoint-execute_query(workspaceId, itemId, query)` (nome pode vir prefixado, ex.: `sqlendpoint-global-execute_query`). Desde 0.3.10 as skills SQL DW usam essa ferramenta em vez de `sqlcmd`.
- Ferramentas FabricIQ (skill `fabriciq`): `DiscoverArtifacts`, `ResolveFabricItem` (substituiu `ResolveReportIdFromUrl` na 0.3.17), `GetReportMetadata`, `GetSemanticModelSchema`, `ValueSearch`, `ExecuteQuery`.
- Endpoint e header de roteamento do FabricIQ mudaram na **0.3.17**.
- **Autenticação**: os três usam bearer token de um `az login` existente, recurso `https://api.fabric.microsoft.com` (um login cobre todos). FabricIQ também aceita token com audience Power BI (`https://analysis.windows.net/powerbi/api`).
- **Claude Code**: via plugin, que fornece `headersHelper` nativo com Azure CLI. Se uma entrada local obsoleta de FabricIQ sobrescrever o plugin: `claude mcp remove --scope local FabricIQ` (com aprovação do usuário).
- **Codex** (>= 0.153.4, `~/.codex/config.toml`): tabela `[mcp_servers.<name>]` com `url`, `http_headers` (só FabricIQ) e `http_headers_helper` chamando `az account get-access-token --resource https://api.fabric.microsoft.com` com saída `{Authorization: "Bearer <token>"}`.
- **VS Code** (`.vscode/mcp.json`): sem header helper; token colado manualmente:
```json
{
  "servers": {
    "FabricIQ": {
      "type": "http",
      "url": "https://fabriciq.svc.cloud.microsoft/v1/mcp/fabriciq",
      "headers": {
        "X-VARIANTS": "Fabric.Routing.FabricIQ.V1",
        "Authorization": "Bearer ${input:fabric-token}"
      }
    }
  },
  "inputs": [
    { "id": "fabric-token", "type": "promptString", "description": "Fabric access token", "password": true }
  ]
}
```
```bash
az account get-access-token --resource https://api.fabric.microsoft.com --query accessToken --output tsv
```
- Nunca colar token em `headers` nem comitar; nunca rodar o comando que gera credencial no chat.
- O alvo `claude` dos scripts legados `register-fabric-mcp` significa Claude Desktop, não Claude Code.

---

## 6. Autenticação típica

Toda chamada REST exige bearer token OAuth 2.0 do Entra ID (API keys, SAS e SQL auth **não** são suportados nas APIs). **Audience errada é a causa mais comum de `401`.**

| Alvo | Scope (MSAL) | Resource (`az`) |
|---|---|---|
| Fabric REST API | `https://api.fabric.microsoft.com/.default` | `https://api.fabric.microsoft.com` |
| Power BI REST (legado) / XMLA | `https://analysis.windows.net/powerbi/api/.default` | `https://analysis.windows.net/powerbi/api` (sem barra final; com barra dá AADSTS500011) |
| OneLake (DFS/Blob) | `https://storage.azure.com/.default` | `https://storage.azure.com` |
| Warehouse / SQL endpoint / SQL database (TDS) | `https://database.windows.net/.default` | `https://database.windows.net` |
| KQL / Kusto | `https://kusto.kusto.windows.net/.default` (ou URI do cluster) | idem |
| Azure Resource Manager | `https://management.azure.com/.default` | — |

Gotchas:
- OneLake rejeita qualquer scope que não seja `storage.azure.com` (ex.: `https://datalake.azure.net/` falha). Token Fabric no OneLake = 401.
- SQL com MSAL v1.0 exige barra dupla: `https://database.windows.net//.default` (o `az` já trata isso).
- Tokens duram ~60-90 min; confira `expiresOn`. Debug: decodificar o JWT e checar `aud`, `exp`, `oid`, `tid`.
- Client credentials (SPN) exige admin consent + tenant setting "Service principals can use Fabric APIs".

```bash
az login
az login --allow-no-subscriptions --tenant <tenantId>
az login --use-device-code --tenant <tenantId>
az login --service-principal --username <appId> --password <clientSecret> --tenant <tenantId>
az login --identity                       # managed identity
az account show --query tenantId --output tsv
az account get-access-token --resource https://api.fabric.microsoft.com --query accessToken --output tsv
```

---

## 7. CLIs usadas

| CLI | Uso nas skills |
|---|---|
| **`az`** (>= 2.55) | `az login`, `az account get-access-token`, `az rest` para o control plane do Fabric. **Sempre passar `--resource`** (senão: "Can't derive appropriate Azure AD resource"). |
| **`fab`** (Fabric CLI) | Ferramenta primária na `git-integration-operations-cli`: `fab auth login` (interativo; SPN `-u <client-id> -p <secret> --tenant <id>`; MI `--identity`), `fab api <endpoint>` (define base URL e audience automaticamente). Body só via `-i` (arquivo ou JSON inline), nunca stdin. |
| **`sqlcmd`** (versão Go) | Fallback legado para SQL DW; principal na `sqldb-cli`. `-G` reutiliza o `az login`. Instalação: `winget install sqlcmd` / `brew install sqlcmd`. |
| `curl`, `jq`, `bash` | OneLake DFS, headers de LRO (`Location`, `x-ms-operation-id`). |
| `copilot`, `claude`, `apm` | Instalação/atualização de plugins e skills. |

### Padrões de `az rest`
```bash
az rest --method get \
  --resource "https://api.fabric.microsoft.com" \
  --url "https://api.fabric.microsoft.com/v1/workspaces" \
  --headers "x-ms-fabric-skill=$SKILL_NAME" \
  --query "value[?displayName=='$WS_NAME'] | [0].id" --output tsv
```
- Filtre por `displayName`, não `name`. Aspas simples em JMESPath: escapar com backtick (`` `Alice's Workspace` ``).
- Catalog search: `POST /v1/catalog/search` com `{"search": ..., "filter": "Type eq 'Lakehouse'", "pageSize": 30}` (itens novos podem levar até 24 h para aparecer).
- `getDefinition` é **POST** (use `--body '{}'` para evitar 411); `updateDefinition` para conteúdo; PATCH para metadados.
- Jobs: `jobType=RunNotebook` (não `DefaultJob`, que falha silenciosamente), `Pipeline`, `Refresh`. Schedules: `/jobs/{jobType}/schedules` (`endDateTime` obrigatório).
- Paginação: repetir enquanto `continuationToken`/`continuationUri` não for nulo (token opaco, não modificar).
- LRO: `202 Accepted` com `Location`, `x-ms-operation-id`, `Retry-After`; poll `GET /v1/operations/<id>` até `Succeeded`/`Failed`; depois `/result`. Re-adquirir token dentro do loop.
- 429: respeitar `Retry-After`. Admin APIs: 200 req/hora por principal por tenant. Warehouse TDS: ~128 conexões concorrentes.
- PowerShell/Windows: passar corpos JSON como arquivo (`--body @file.json`); corpos inline multilinha chegam vazios.

### sqlcmd
```bash
sqlcmd -S <server>.datawarehouse.fabric.microsoft.com -d "<DatabaseName>" -G -Q "SELECT @@VERSION"
sqlcmd -S <server>.datawarehouse.fabric.microsoft.com -d "<DatabaseName>" -G -i ./my_query.sql
sqlcmd ... -G -Q "SELECT ..." -s "," -W -h -1 > output.csv
```
Connection string via REST: Warehouse `properties.connectionString`; Lakehouse `properties.sqlEndpointProperties.connectionString` (aguardar `provisioningStatus = Success`); SQL database `properties.serverFqdn` + `databaseName`.

### OneLake via curl
Header obrigatório `x-ms-version: 2021-06-08`, token audience `storage.azure.com`. Listar: `?resource=filesystem&recursive=false`; upload em 3 passos: `PUT ?resource=file` -> `PATCH ?action=append&position=0` -> `PATCH ?action=flush&position=$FILE_SIZE`.
