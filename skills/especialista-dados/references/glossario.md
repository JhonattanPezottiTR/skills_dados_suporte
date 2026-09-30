# Glossário

> Última atualização: 2026-09-29 · Fonte: Microsoft Learn + termos do time

| Termo | Significado |
|---|---|
| **OneLake** | Data lake único do Fabric (um por tenant); armazena tabelas em Delta Parquet. |
| **Workspace** | Contêiner de itens do Fabric (lakehouses, warehouses, modelos, relatórios), associado a uma capacidade. |
| **Capacidade (F SKU)** | Recurso computacional pago do Fabric (F2…F2048), medido em CU (Capacity Units). |
| **Lakehouse** | Item que combina arquivos e tabelas Delta; acessado por Spark e por um SQL analytics endpoint. |
| **SQL analytics endpoint** | Endpoint T-SQL **somente leitura** criado automaticamente sobre as tabelas Delta do Lakehouse. |
| **Warehouse** | Data warehouse do Fabric com T-SQL completo de leitura/escrita (DML/DDL), sobre Delta no OneLake. |
| **SQL database (Fabric)** | Banco OLTP (engine do Azure SQL) dentro do Fabric, com espelhamento automático para o OneLake. |
| **Dataflow Gen2** | Ferramenta de ETL low-code baseada em Power Query (M), com destinos como Lakehouse/Warehouse. |
| **Pipeline (Data Factory)** | Orquestração de atividades (Copy, Notebook, Dataflow, Stored Procedure...). |
| **Notebook** | Código Spark (PySpark/Scala/SQL/R) executado no Fabric. |
| **Medallion** | Arquitetura em camadas Bronze (bruto), Silver (limpo/conformado), Gold (modelado para consumo). |
| **Semantic model** | Antigo "dataset": modelo tabular (tabelas, relacionamentos, medidas DAX) consumido por relatórios. |
| **Direct Lake** | Storage mode que lê Delta do OneLake direto na memória do VertiPaq, sem import nem DirectQuery. |
| **Import / DirectQuery** | Modos clássicos: cópia comprimida em memória / consulta à fonte em tempo real. |
| **VertiPaq** | Engine colunar em memória do Analysis Services/Power BI. |
| **DAX** | Data Analysis Expressions — linguagem de medidas e queries do modelo tabular. |
| **M / Power Query** | Linguagem de transformação usada em Dataflows e no Power BI Desktop. |
| **TMDL** | Tabular Model Definition Language — formato texto do semantic model (usado em PBIP/Git). |
| **PBIP / PBIR** | Power BI Project (pasta com modelo + relatório em texto) / formato de relatório em JSON por visual. |
| **RLS / OLS** | Row-Level Security / Object-Level Security. |
| **SGD** | Sistema de gestão do suporte (Sybase SQL Anywhere): SSC, SS, agenda, usuários, clientes. |
| **SSC** | Solicitação de suporte do cliente — atendimento N1. |
| **SS** | Solicitação de serviço — nível N2 (réplica em DB_SGD_N2, schema `ss`). ⚠️ **Divergência de nome** (P-11, `negocio-perguntas-em-aberto.md`): o sql-base chama SS de "Solicitação de Suporte", não "Solicitação de serviço". Confirmar com o time antes de usar em texto publicado. |
| **N1 / N2** | Níveis de atendimento; pendência N1/N2 definida pelos flags `situacao_pendente_nivel_um/dois`. **Em revisão:** há duas regras de N1 em produção (batch × tempo real), ver `dados-sgd-regras-e-joins.md` §Pendência e P-01. |
| **SA / NE / SAL / SAIL** | **Confirmado pelo usuário** (REG-001, resolve P-11): SA = Solicitação de Alteração · NE = Notificação de Erro · SAL = Solicitação de Alteração Legal · SAIL = Solicitação de Implementação Legal. ⚠️ Os **códigos numéricos** ainda divergem entre fontes (`reason` no Dataflow: 0=NE/1=SA/2=SAL/3=SAIL; sql-base `motivo`: 1=SAM/2=SAL/3=SAIL) — isso não foi resolvido, só o nome de cada sigla. |
| **TFM** | Tempo de Fila Médio (chat/Plug) — definição do módulo `plug_queue_realtime`. |
| **TEM** | Tempo de Espera Médio (chat/Plug) — definição do módulo `plug_queue_realtime`. ⚠️ Cuidado: "TME" aparece em outros relatórios do time com um significado diferente (métrica candidata `MC-###` em `powerbi-metricas-candidatas.md`) — confirme qual sigla e qual fonte antes de comparar números. |
| **CTS / TRIA** | Central de soluções e assistente de IA (banco Sybase `cts`, réplica DB_CTS). |
| **Maestro** | Orquestrador do time (`analytics-bi-dominio-orquestrador`): agenda e executa os jobs de ETL e tempo real. |
| **Allowlist Sybase** | Lista de views/funções liberadas ao login de BI (`shared/sybase_objetos.py`); só elas podem ser usadas. |
| **Push dataset** | Dataset do Power BI alimentado por API (linhas enviadas pelos jobs de tempo real); tabela `RealTimeData`. |
| **Dataflow (Power BI)** | Fluxo Power Query no serviço Power BI que prepara entidades reutilizáveis pelos relatórios. |
| **Skill (IA)** | Arquivo de instruções (SKILL.md) que ensina uma IA a executar uma tarefa. |
| **MCP** | Model Context Protocol — servidor que dá à IA acesso a dados/ações (executa), enquanto a skill ensina. |
