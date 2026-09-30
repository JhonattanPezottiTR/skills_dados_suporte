# Modelagem de modelos semânticos Power BI
> Última atualização: 2026-09-29 · Fonte: microsoft/skills-for-fabric v0.3.18 + Microsoft Learn · Links: https://github.com/microsoft/skills-for-fabric/tree/main/skills/semantic-model-authoring · https://learn.microsoft.com/en-us/power-bi/guidance/star-schema · https://learn.microsoft.com/en-us/fabric/fundamentals/direct-lake-overview · https://learn.microsoft.com/en-us/fabric/fundamentals/direct-lake-how-it-works

Este guia junta o que a skill upstream **`semantic-model-authoring`** recomenda (arquivos `SKILL.md`, `references/modeling-guidelines.md`, `naming-conventions.md`, `direct-lake-guidelines.md`, `tmdl-guidelines.md`, `pbip.md`, `field-parameters.md`, `metadata-discovery.md`, `semantic-model-rest-api.md`, `semantic-model-ai-readiness.md`) com a documentação oficial do Microsoft Learn.

Legenda de origem usada no texto:
- **[upstream]**: regra lida na skill `semantic-model-authoring` v0.3.18.
- **[Learn]**: Microsoft Learn.
- **[prática]**: prática consolidada de mercado, sem atribuição ao upstream.

> Nota sobre o upstream: na v0.3.18 **não existe** uma skill `semantic-model-consumption` (retorna 404). Quem responde perguntas de negócio via DAX é a skill **`fabriciq`**, e o DAX de consulta está coberto em `powerbi-dax-padroes.md`.

---

## 1. Star schema (esquema estrela)

### 1.1 Conceito [Learn]
- **Dimensões** descrevem entidades de negócio (produto, cliente, local, data). Servem para **filtrar e agrupar**.
- **Fatos** guardam eventos/observações (vendas, saldos, metas). Servem para **sumarizar**.
- O tipo da tabela é definido pelo **relacionamento**: o lado "um" é dimensão e o lado "muitos" é fato. Não existe propriedade de tabela para isso.
- A **dimensionalidade** do fato vem das colunas de chave. A **granularidade** vem dos valores dessas chaves (ex.: data sempre no dia 1 = grão mensal).
- Não misture tipos numa mesma tabela e carregue os fatos sempre num grão consistente.

### 1.2 Regras do upstream [upstream]
- Star schema é o padrão: fatos + dimensões desnormalizadas, **chaves de coluna única** e relacionamentos **1:N**. Snowflake só quando o requisito não pode ser atendido de outra forma.
- **Consistência antes de perfeição:** num modelo existente, siga as convenções que já estão lá.
- **Medidas explícitas** sempre. Oculte a coluna base agregada e sugira ativar `discourageImplicitMeasures`.
- **Modelo enxuto:** remova tabelas/colunas que não servem para análise. Os maiores consumidores de memória são GUIDs, IDs de transação, chaves compostas e DateTime não dividido. Na dúvida sobre uma coluna, pergunte ao usuário.
- Toda tabela precisa de pelo menos um relacionamento, exceto tabelas utilitárias. Evite tabelas órfãs.
- Evite relacionamento dimensão→dimensão e mais de ~30 colunas visíveis por tabela (sinal de problema de desnormalização).

### 1.3 Padrões dimensionais [Learn]
| Conceito | O que é | Como tratar no Power BI |
|---|---|---|
| Surrogate key | Chave artificial única na dimensão | Se a dimensão não tem coluna única, crie índice no Power Query (ou, melhor, no DW). O upstream pede **não** criar surrogate keys em fatos. |
| Snowflake | Dimensão normalizada em várias tabelas (Produto → Subcategoria → Categoria) | Em geral, desnormalize numa tabela só. Assim você pode criar hierarquia entre níveis (não é possível criar hierarquia entre tabelas). |
| SCD Tipo 1 | Sobrescreve com o valor mais recente | Refresh não incremental já resulta em Tipo 1. |
| SCD Tipo 2 | Versiona membros (StartDate/EndDate/IsCurrent + surrogate key) | Deve vir pronto do DW (Power Query não consegue gerar). Exponha uma coluna para o membro e outra para a versão, ex.: `David Campbell (06/27/2019-Current)`. |
| Role-playing | Mesma dimensão filtrando o fato de formas diferentes (data do pedido, envio, entrega) | Opção A: vários relacionamentos, um ativo e os demais inativos + `USERELATIONSHIP`. Opção B: uma tabela por papel (`Ship Date`, `Delivery Date`) com colunas autoexplicativas (`Ship Year`). |
| Junk dimension | Consolida várias dimensões pequenas (status, flags) | Produto cartesiano + surrogate key. |
| Degenerate dimension | Atributo do fato usado para filtrar (nº do pedido) | Pode ficar no fato. |
| Factless fact / bridge | Só chaves, sem medidas | Padrão recomendado para relacionamento muitos-para-muitos entre dimensões. |

---

## 2. Relacionamentos

### 2.1 Regras [upstream]
- Crie os relacionamentos **antes** das medidas.
- Direção de filtro padrão: **única** (`OneDirection`). Bidirecional só quando for indispensável.
- Prefira chaves **inteiras** (`Int64`), com o **mesmo tipo de dado** dos dois lados.
- **Oculte as chaves estrangeiras** no lado "muitos".
- **Não use chaves compostas** (não são suportadas). Se precisar, concatene a chave na origem.
- Muitos-para-muitos só se for exigido. A soma de relacionamentos bidirecionais + M:N deve ficar **abaixo de 30%** do total.
- Não mantenha relacionamento **inativo** que nenhuma medida ativa com `USERELATIONSHIP`.
- **Não use `USERELATIONSHIP` em tabelas com RLS.**
- Vários fatos ligados à mesma dimensão por chaves diferentes exigem **dimensão conformada**.
- Não defina `isKey = true` nas chaves primárias das dimensões.

### 2.2 Cardinalidade e direção [Learn + prática]
| Cardinalidade | Quando usar | Observação |
|---|---|---|
| 1:N (muitos-para-um) | Padrão dimensão → fato | Lado "um" deve ter valores únicos. Em Direct Lake a consulta **falha** se houver duplicata no lado "um" [Learn]. |
| 1:1 | Raro; em geral indica que as tabelas deviam ser uma só | Avalie mesclar. |
| M:N | Fatos em grãos diferentes (ex.: metas por mês × vendas por dia) ou bridge | Preferir tabela ponte (factless fact) entre dimensões [Learn]. |

### 2.3 Em TMDL [upstream]
- `fromColumn` = lado **muitos** (fato). `toColumn` = lado **um** (dimensão).
- Role-playing: `isActive: false` e ative no DAX com `USERELATIONSHIP()`.

```tmdl
relationship 'Sales_Order Date_Date'
	fromColumn: Sales.'Order Date Key'
	toColumn: Date.'Date Key'

relationship 'Sales_Ship Date_Date'
	isActive: false
	fromColumn: Sales.'Ship Date Key'
	toColumn: Date.'Date Key'
```

Medida que ativa o relacionamento inativo:

```dax
Sales by Ship Date =
CALCULATE (
    [Total Sales],
    USERELATIONSHIP ( 'Sales'[Ship Date Key], 'Date'[Date Key] )
)
```

---

## 3. Tabela de datas (calendário)

### 3.1 Regras [upstream]
- É obrigatória para time intelligence (LY, YTD etc.).
- **Prefira a tabela de datas da origem**, carregada via M. Crie em DAX só se a origem não tiver, e **nunca** crie uma se a origem já tem.
- Na criação de um modelo novo, o upstream pede uma dimensão de data separada **em Power Query/M, não em tabela calculada DAX**, salvo pedido explícito.
- Intervalo **contínuo, sem lacunas**. `dataCategory: Time`.
- Colunas mínimas: Year, Quarter, Month, Day, Week (opcional: Day of Week, Month Name).
- `Month Name` ordenado por número do mês (`sortByColumn`).
- **Desative auto date/time**: ele cria tabelas ocultas `LocalDateTable_*` que incham a memória.
- Divida DateTime em Date + Time para reduzir cardinalidade.

### 3.2 Objetos de calendário em TMDL [upstream]
Opcional. Fica dentro da tabela de datas, depois das hierarquias. Cada `calendarColumnGroup = <granularidade>` define um `primaryColumn` (coluna de ordenação/numérica) e `associatedColumn` opcionais (texto de exibição). Granularidades suportadas: `year`, `quarter`, `month`, `week`, `date`, `monthOfYear`, `dayOfWeek`.

### 3.3 Exemplo de calendário DAX (só quando a origem não tem) [prática]
```dax
Date =
VAR _Inicio = DATE ( YEAR ( MIN ( 'Sales'[Order Date] ) ), 1, 1 )
VAR _Fim    = DATE ( YEAR ( MAX ( 'Sales'[Order Date] ) ), 12, 31 )
RETURN
    ADDCOLUMNS (
        CALENDAR ( _Inicio, _Fim ),
        "Year", YEAR ( [Date] ),
        "Quarter", "T" & QUARTER ( [Date] ),
        "Month Number", MONTH ( [Date] ),
        "Month Name", FORMAT ( [Date], "MMMM" ),
        "Year Month", FORMAT ( [Date], "YYYY-MM" ),
        "Week", WEEKNUM ( [Date], 2 ),
        "Day of Week", WEEKDAY ( [Date], 2 )
    )
```
Depois: marcar como tabela de datas, `Month Name` → sort by `Month Number`, `SummarizeBy = None` em Year/Month Number.

---

## 4. Modos de armazenamento

### 4.1 Escolha padrão [upstream]
| Origem | Modo |
|---|---|
| OneLake (Lakehouse/Warehouse Fabric) | **Direct Lake** |
| Qualquer outra | **Import** (padrão) |
| DirectQuery | **Só se o usuário pedir explicitamente** |

### 4.2 Comparação [Learn]
| Capacidade | Direct Lake on OneLake | Direct Lake on SQL | Import | DirectQuery |
|---|---|---|---|---|
| Licença | Só capacidade Fabric (F SKU) | Só capacidade Fabric | Qualquer | Qualquer |
| Origem | 1 ou mais itens Fabric com Delta (inclui shortcuts) | 1 item Fabric com SQL analytics endpoint | Qualquer conector | Conector com DQ |
| Views SQL | Não | Sim, mas cai em DirectQuery | Sim | Sim |
| Composite | Sim (com Import; DQ via XMLA) | Não no mesmo modelo | Sim | Sim |
| Tabelas calculadas | Sim (preview) | Não (exceto calculation groups, what-if e field parameters) | Sim | Não (viram Import) |
| Colunas calculadas | Sim, só User Context (preview) | Não | Sim | Sim |
| Partições no modelo | Não (particione a Delta) | Não | Sim | Não |
| Fallback para DirectQuery | **Não existe** | Sim, controlado por `DirectLakeBehavior` | — | — |
| RLS do SQL endpoint | Não aplicada (usa acesso aos arquivos OneLake) | Força fallback | Duplicar no modelo | Sim |
| RLS/OLS do modelo | Sim (recomendado fixed identity) | Sim (recomendado fixed identity) | Sim | Sim |

- Direct Lake e Import são processados pelo **VertiPaq**. DirectQuery federa a consulta à origem e costuma ser mais lento [Learn].
- O refresh de Direct Lake é **framing**: copia só metadados (segundos), apontando para a versão mais recente das Delta tables. As colunas são carregadas sob demanda (**transcoding**) e podem ser removidas da memória (eviction) [Learn].
- A configuração **"Keep your Direct Lake data up to date"** (ativada por padrão) faz framing automático quando as Delta mudam. Desative se precisar esperar o ETL terminar antes de expor dados [Learn].
- **Direct Lake on OneLake é a opção recomendada para modelos novos** [Learn].

### 4.3 Fallback (só Direct Lake on SQL) [Learn]
A consulta continua em Direct Lake somente se: não há RLS/OLS/DDM SQL no endpoint, nenhuma tabela é view SQL não materializada, nenhuma tabela excede os guardrails do SKU (arquivos Parquet, row groups, linhas) e o modelo foi refreshed (framed) após criar/alterar as Delta. **Uma única tabela acima do guardrail impede Direct Lake no modelo inteiro.**

| `DirectLakeBehavior` | Comportamento | Uso |
|---|---|---|
| `Automatic` (padrão) | Cai silenciosamente em DirectQuery | Produção |
| `DirectLakeOnly` | Falha com erro | Desenvolvimento, para achar causas |
| `DirectQueryOnly` | Sempre DirectQuery | Medir desempenho de fallback |

Diagnóstico:
```dax
EVALUATE TABLETRAITS ()
-- coluna [DirectLakeFallbackInfo]: "None" = tabela em Direct Lake
```
Correções: refresh para tabelas não framed; materializar views; mover RLS/OLS para o modelo; `OPTIMIZE`/`VACUUM` quando exceder guardrails; ou subir SKU.

Guardrails por SKU (trecho) [Learn]: F2–F32 = 1.000 arquivos Parquet / 1.000 row groups / 300 milhões de linhas por tabela. F64 = 5.000 / 5.000 / 1.500 milhões. F512+ = 10.000 / 10.000 / 12.000–24.000 milhões. Em Direct Lake on OneLake, estourar guardrail faz o **refresh falhar**. Em Direct Lake on SQL, cai em DirectQuery.

Outras limitações relevantes [Learn]: sem tipos complexos, binary ou GUID; strings até 32.764 caracteres; sem NaN; modelo na **mesma região** do item de origem; sem gateway (só cloud connections); sem My Workspace; ferramentas XMLA precisam de `compatibilityLevel` ≥ 1604; tabelas criadas via XMLA ficam não processadas até um refresh.

### 4.4 Construção Direct Lake [upstream]
1. Criar a **named expression compartilhada** com `AzureStorage.DataLake` (não use `Sql.Database` salvo pedido explícito). Nome sugerido: `DirectLake - [Model Name]`.
2. Inspecionar o schema das tabelas no OneLake.
3. Declarar tabelas e colunas com `sourceColumn` e tipos iguais aos da origem. Partição `EntityPartitionSource`, `mode: directLake`, **sem M/Power Query**.
4. Deploy em workspace de desenvolvimento e refresh para validar os mapeamentos.
5. Não inclua colunas `binary`.

```tmdl
expression DL_Sales_Named_Expression =
		let
		    Source = AzureStorage.DataLake("https://onelake.dfs.fabric.microsoft.com/<WORKSPACE_ID>/<LAKEHOUSE_ID>", [HierarchicalNavigation=true])
		in
		    Source

table Product

	column 'Product Key'
		dataType: int64
		formatString: 0
		summarizeBy: none
		sourceColumn: product_key

	column Category
		dataType: string
		summarizeBy: none
		sourceColumn: category

	partition Product = entity
		mode: directLake
		source
			entityName: Product
			schemaName: dbo
			expressionSource: DL_Sales_Named_Expression
```

### 4.5 Composite models [Learn]
- **Composite** = modelo com tabelas em modos diferentes (Import + DirectQuery + Dual, ou Direct Lake on OneLake + Import).
- Direct Lake on SQL não mistura com DQ/Dual no mesmo modelo, mas é possível criar um composite **sobre** o modelo Direct Lake no Desktop.
- Import pode ter **agregações definidas pelo usuário** sobre fatos DirectQuery. O upstream (padrão MDL004) sugere tabelas de agregação Import sobre fatos DQ para desempenho.

---

## 5. Import: partições, colunas e tipos [upstream]

- **Ordem de construção por tabela:** partição (query de origem) → colunas → relacionamentos → medidas.
- Import/DirectQuery: use **parâmetros M** (`Server`, `Database`) em named expressions com `IsParameterQuery=true`. Não converta modelos existentes para parâmetros sem pedido.
- Tipos de partição: **M** (Import/DQ), **Entity** (Direct Lake, sem M), **Calculated** (Import via DAX).
- Toda coluna de dados precisa de `sourceColumn` e `dataType` (tabelas calculadas podem inferir).

| Tipo (`dataType`, case-sensitive) | Uso |
|---|---|
| `Int64` | Chaves e IDs |
| `Decimal` | Moeda e valores precisos (até 4 casas) |
| `String` | Texto |
| `DateTime` | Datas e timestamps |
| `Boolean` | Verdadeiro/falso |

- **Nunca use `Double`**: gera erro de arredondamento e é mais lento.
- Oculte colunas técnicas, IDs, FKs e colunas agregadas por medidas.
- `SummarizeBy = None` em números que não somam (IDs, telefone, CEP, ano, número do mês).
- `isAvailableInMdx = false` em colunas ocultas que não são usadas em sort-by, hierarquias ou variações.
- `dataCategory` em colunas geográficas e de latitude/longitude.
- Flags: "Yes"/"No" (string) ou `Boolean`.
- Chaves de texto de alta cardinalidade: substitua por surrogate inteira na origem.
- Referencie colunas sempre qualificadas: `'Table Name'[Column Name]`.

```tmdl
expression Server = "sql-prod.database.windows.net" meta [IsParameterQuery=true, Type="Text", IsParameterQueryRequired=true]
expression Database = "SalesDW" meta [IsParameterQuery=true, Type="Text", IsParameterQueryRequired=true]

table Sales

	/// Total da venda em moeda local, sem impostos.
	measure 'Total Sales' = SUM ( Sales[Sales Amount] )
		formatString: $#,##0.00
		displayFolder: Measures\Value

	column 'Sales Amount'
		dataType: decimal
		isHidden
		sourceColumn: SalesAmount

	partition Sales = m
		mode: import
		source =
				let
				    Source = Sql.Database(#"Server", #"Database"),
				    #"Navigated to Sales" = Source{[Schema="dbo",Item="FactSales"]}[Data]
				in
				    #"Navigated to Sales"
```

### Colunas calculadas vs. lógica na origem [upstream]
- Use com moderação (calculadas por linha no refresh). Prefira medidas ou empurre a lógica para a origem.
- Revise modelos com **mais de 5** colunas calculadas e mova lógica com `RELATED()` para a origem.
- Não use para agregação simples, filtro ou valores que dependem do contexto de filtro.

---

## 6. TMDL e estrutura PBIP

### 6.1 Estrutura de pastas PBIP [upstream]
```text
<Name>.pbip                          -> atalho que abre o relatório
<Name>.SemanticModel/
    definition.pbism                 -> obrigatório; usar exatamente como modelo (version 4.2, qnaEnabled true)
    definition/
        database.tmdl                -> compatibility level; começa com "database <nome/GUID>"
        model.tmdl                   -> propriedades do modelo + "ref table/role/perspective/cultureInfo"
        relationships.tmdl
        functions.tmdl               -> DAX UDFs
        expressions.tmdl             -> named expressions/parâmetros [prática: local usual]
        tables/<Tabela>.tmdl         -> um arquivo por tabela
        roles/<Role>.tmdl
        cultures/<locale>.tmdl
        perspectives/<Nome>.tmdl
<Name>.Report/
    definition.pbir                  -> datasetReference byPath ou byConnection
    definition/                      -> relatório em PBIR
```
- `definition.pbir` com **byPath** (modelo local): `{"path": "../Sales.SemanticModel"}`. Somente caminho relativo, com barras `/`.
- **byConnection** (modelo no workspace): `connectionString` `semanticmodelid=<id>`. Nesse caso o Desktop não abre o modelo para edição.
- Exportar para PBIP gera só os TMDL. É preciso **montar** o `definition.pbism`, a pasta `.Report` com `definition.pbir` (byPath para `../<Name>.SemanticModel`) e o `<Name>.pbip`.

### 6.2 Regras de sintaxe TMDL [upstream]
- Indentação consistente, **tabs** preferidos (PowerShell: `` `t ``).
- Declaração: `table Customer`, `measure 'Total Sales' = ...`.
- Aspas simples se o nome tiver espaço ou `.`, `=`, `:`, `'`.
- Descrição com `///` acima do objeto (não use a propriedade `description`).
- Comentários `//` **não** são permitidos no nível TMDL, só dentro de M/DAX.
- **Omita `lineageTag`** em objetos novos (o engine gera).
- DAX multilinha entre três crases (```` ``` ````).
- Medidas antes das colunas. **Toda medida visível com `formatString`.**
- Nunca escreva anotações `PBI_*` (ex.: `PBI_FormatHint`); anotações customizadas são permitidas.
- Modelos Import precisam de `defaultPowerBIDataSourceVersion: powerBI_V3`.
- Scripts TMDL (`TMDLScripts/`): o único comando suportado é `createOrReplace`.
- Passos M: nome `#"..."` iniciando com verbo no passado, até 50 caracteres. Comentário acima do passo, até 225 caracteres.

### 6.3 Prioridade de ferramentas [upstream]
1. **Tier 1 – `powerbi-modeling-mcp`** (Desktop, workspace Fabric ou pasta PBIP). Com MCP conectado, **ler `*.tmdl` é anti-pattern** (arquivo em disco fica defasado), salvo pedido explícito.
2. **Tier 2 – editar TMDL direto** (sem MCP). Para Fabric: `getDefinition` → editar → `updateDefinition`.
3. **Fallback** (só Desktop, sem PBIP e sem MCP): parar e pedir para instalar o MCP ou salvar como PBIP.
- Não misture tiers. Deploy, Manage in Fabric e Connection Binding têm prioridade própria.
- Prefira **TMDL a TMSL**. Não escreva à mão `model.tmdl`, `database.tmdl`, `relationships.tmdl` ou `tables/*.tmdl` quando o MCP estiver registrado.

---

## 7. Field parameters

### 7.1 Estrutura (tabela calculada) [upstream]
Tupla `("Rótulo", NAMEOF('Tabela'[Campo]), Ordem)` com três colunas:

| Coluna | Origem | Configuração |
|---|---|---|
| Label (visível) | `[Value1]` | sort by Order, group by Fields; é a coluna que o slicer usa |
| Fields (oculta) | `[Value2]` | sort by Order; **`extendedProperty ParameterMetadata` com `"kind": 2`** |
| Order (oculta) | `[Value3]` | int64, `summarizeBy: sum`, format `0` |

- Ordem **começando em 0, sem lacunas**, seguindo a ordem dos campos.
- `NAMEOF` tanto para colunas quanto para medidas.
- Escape duplicando: `"` em rótulos, `'` em nomes de tabela, `]` em referências.
- Sem `kind: 2`, o Desktop **não** reconhece como field parameter.

```dax
Metric Selector = {
    ( "Vendas",  NAMEOF ( 'Sales'[Total Sales] ),  0 ),
    ( "Margem",  NAMEOF ( 'Sales'[Gross Margin] ), 1 ),
    ( "Pedidos", NAMEOF ( 'Sales'[# Orders] ),     2 )
}
```

### 7.2 Fluxos [upstream] (novidade 0.3.17)
- **Criar:** verificar se já existe (`kind: 2`) para não duplicar → `table_operations` `CreateFieldParameter` (MCP) ou TMDL à mão.
- **Editar:** não existe `UpdateFieldParameter`. Reescreva a **lista completa** da partição (`partition_operations` Update). Campo omitido é removido. Recalcule as ordens.
- **Renomear/excluir:** `table_operations` Rename/Delete ou `column_operations` no rótulo. Renomear muda o alvo de binding, então os slicers do relatório precisam ser reapontados.
- Não substitua silenciosamente por uma tabela com `SWITCH` quando pediram field parameter.
- Slicer e visual ficam do lado do relatório (ver `powerbi-relatorios.md`).

---

## 8. Calculation groups

### Regras [upstream]
- Use para variações de time intelligence (YTD, LY etc.) e evite a explosão de medidas.
- Pelo menos um item por grupo, com nomes claros: `Current`, `YTD`, `PY`, `PY YTD`. Nunca deixe grupo vazio.
- Dispensável quando poucas variações simples resolvem.
- TMDL: `calculationGroup` sem nome, com `calculationItem Nome = DAX`. A tabela precisa de uma coluna (geralmente com o nome da tabela) e de uma partição `= calculationGroup`.
- Para sobrescrever o formato use **`formatStringDefinition`**, não `formatString`.
- Para IA: liste os itens na descrição da coluna do grupo.

```tmdl
table 'Time Calculation'

	calculationGroup

		calculationItem Current = SELECTEDMEASURE ()

		calculationItem YTD = CALCULATE ( SELECTEDMEASURE (), DATESYTD ( 'Date'[Date] ) )

		calculationItem PY = CALCULATE ( SELECTEDMEASURE (), SAMEPERIODLASTYEAR ( 'Date'[Date] ) )

		calculationItem 'YoY %' =
				```
				VAR _Atual = SELECTEDMEASURE ()
				VAR _PY = CALCULATE ( SELECTEDMEASURE (), SAMEPERIODLASTYEAR ( 'Date'[Date] ) )
				RETURN DIVIDE ( _Atual - _PY, _PY )
				```
			formatStringDefinition = "0.0%"

	column 'Time Calculation'
		dataType: string
		sourceColumn: Name

	partition 'Time Calculation' = calculationGroup
```
(`SELECTEDMEASURE` e os itens acima são padrão DAX [prática]; a estrutura TMDL segue o upstream.)

Observação de desempenho [upstream, guia de performance]: calculation groups afetam todas as medidas que interceptam e podem **quebrar a fusão** de scans no Storage Engine quando os itens aplicam filtros próprios.

---

## 9. Segurança: RLS e OLS

### Regras [upstream]
- Expressões de filtro **simples**. Lógica complexa vai para o warehouse.
- Relacionamentos de direção única nas tabelas de segurança. Teste os filtros.
- Evite funções de string (`RIGHT`, `LEFT`, `UPPER`, `LOWER`, `FIND`) em RLS.
- Não use `USERELATIONSHIP` em tabelas com RLS.
- TMDL: um arquivo por role em `roles/`, `role <Nome>` com `modelPermission` (`read` ou `readRefresh`), no máximo um `tablePermission <Tabela> = <filtro DAX>` por tabela e referência em `model.tmdl`. Nunca adicione a anotação `PBI_Id`.
- **Proibido (Deny):** gerenciar **membros** das roles RLS/OLS. Recuse e direcione ao portal do Power BI (membros são atribuídos no serviço via Entra ID). Não use `INFO.ROLEMEMBERSHIPS()`.

```tmdl
role 'Regional Manager'
	modelPermission: read

	tablePermission Region = 'Region'[Manager Email] = USERPRINCIPALNAME ()
```

### RLS/OLS em Direct Lake [Learn]
- RLS do modelo é suportada, mas é **fortemente recomendado** usar conexão cloud com **fixed identity**.
- RLS/OLS/DDM definidos no SQL endpoint forçam fallback (Direct Lake on SQL) ou **não são aplicados** (Direct Lake on OneLake). Para garantir a segurança, defina-a no modelo.
- `executeQueries` aceita `impersonatedUserName` para testar RLS [upstream, REST].

---

## 10. Nomenclatura [upstream]

- Nomes legíveis com espaços. Nada de CamelCase, snake_case ou CAIXA ALTA.
- Termos de negócio, sem prefixos `Fact`, `Dim`, `DIM_`, `FACT_`, `STG_`.
- Fatos no **plural** (Sales, Orders). Dimensões no **singular** (Product, Customer, Date).
- Coluna descritiva principal com o nome da tabela ("Product", não "Product Name"). **Exceção:** em modelos usados por Copilot/data agents, qualifique (`Product Name`, `Customer Name`).
- Medidas: `Total Sales`, `# Customers` (contagens com `#`).
- Variações no padrão **[Base] [Período] ([Unidade])**: `Total Sales (ly)`, `Total Sales (ytd)`, `Gross Margin (%)`. Use uma convenção de período de forma consistente.
- Só siglas conhecidas (YTD, MTD, QTD), sempre explicadas na descrição.
- Sem emojis, tabs, quebras de linha ou espaços no início/fim.
- Display folders: fatos com `Measures\Value`, `Measures\Quantity`, `Measures\Counts`, `Facts`, `Keys`; dimensões com `Attributes` e `Keys`.
- Medidas distribuídas nas tabelas relevantes, **não** numa tabela "Measures" dedicada.
- Toda tabela, coluna e medida visível com **descrição** em termos de negócio (propósito e grão da tabela). Descrição que só repete o nome é ruim.

| Ruim | Melhor |
|---|---|
| `OrderStatus` | Order Status |
| `TOTAL_COST` | Total Cost |
| `FACT_Orders` | Orders |
| `Del. Mrgn %` | Delivery Margin (%) |
| `SM pct 1YP` | Standard Margin (ly) (%) |

Formatos (`formatString`) de referência [upstream]: moeda `$#,##0.00` · percentual `0.00%` · inteiro `#,##0` · decimal `#,##0.00` · milhares `#,##0,K` · milhões `#,##0,,M`. (Para padrão BR, ajuste o símbolo de moeda conforme `regras-formato.md` do time.)

---

## 11. Hierarquias, perspectivas e traduções [upstream]
- Hierarquias para caminhos comuns (Year > Quarter > Month > Day). Níveis na mesma tabela, do mais grosso ao mais fino. Nada de hierarquia de nível único nem entre tabelas.
- Perspectivas: `perspective <Nome>` + `perspectiveTable` (`includeAll` ou colunas/medidas específicas). Remova perspectivas vazias.
- Traduções: um arquivo por locale em `cultures/` (`cultureInfo pt-BR`), `caption:` e `description:`.

---

## 12. Performance do modelo [upstream + Learn]
- Star schema, não snowflake. Chaves `Int64`.
- Reduza **cardinalidade**: divida DateTime, arredonde/bin decimais contínuos, separe endereços completos (padrão MDL003).
- Evite `Double`, auto date/time, bidirecional/M:N desnecessários e colunas sem uso.
- Despivote dados com um mês por coluna.
- DirectQuery: cuidado com time intelligence; em Premium/Fabric, considere tabelas de agregação.
- **Integridade referencial:** chaves órfãs no fato violam RI. Detecte com `DISCOVER_STORAGE_TABLES` onde `RIVIOLATION_COUNT > 0` e crie uma linha "Unknown" na dimensão (MDL007).
- Direct Lake: V-Order (`spark.sql.parquet.vorder.default=true` + `OPTIMIZE`, ou perfil `readHeavyForPBI`) e **1–16 milhões de linhas por row group** (DL001/DL002). Para Direct Lake, trace via endpoint XMLA do Fabric, não pelo proxy local do Desktop.
- Manutenção: remova colunas/medidas ocultas sem referência, relacionamentos inativos sem uso, fontes não usadas e perspectivas vazias.

---

## 13. Fluxos do upstream `semantic-model-authoring`

### 13.1 Regras transversais
- Header de telemetria em **toda** chamada a `api.fabric.microsoft.com` (inclusive polls de LRO e retries): `x-ms-fabric-skill: semantic-model-authoring`.
- IDs nunca são adivinhados: liste workspaces/itens e filtre com JMESPath.
- Entenda o schema de origem antes. Se faltar informação da origem, **pare e pergunte**, nunca invente.

### 13.2 Workflows
| # | Workflow | Pontos-chave |
|---|---|---|
| 1 | Criar modelo | Requisitos → modo (Direct Lake/Import) → star schema + data → carregar guidelines → construir (compat level **≥ 1702**, uma passada só) → deploy único → validar |
| 2 | Descobrir metadados | MCP List/Get (exige Write). Com só Build: `INFO.VIEW.*` via `dax_query_operations` (carregar `metadata-discovery.md` antes). Sem MCP: `getDefinition` |
| 3 | Modificar | Conectar e descobrir (inclui modo) → planejar e checar conflitos de nome → partições → colunas → relacionamentos → medidas → salvar e validar |
| 4 | Field parameters | Ver seção 7 |
| 5 | Otimizar DAX | Cliente com trace (MCP). Ver `powerbi-dax-padroes.md` |
| 6 | Best practices | Inventário → avaliar (star, nomes, cardinalidade/direção, `formatString`, tipos, FKs ocultas, colunas calculadas × medidas, limites Direct Lake) → achados **critical / recommended / optional** → aguardar aprovação → aplicar |
| 7 | AI readiness (Copilot/Data Agents) | Ver seção 14 |
| 8 | Exportar PBIP | Ver seção 6.1 |
| 9 | Deploy | Arquivos em disco → REST (`createItemWithDefinition` / `updateDefinition`), mesmo com MCP ativo. Só em sessão MCP → MCP Deploy. **Não idempotente**: retry cria duplicata ("multiple datasets named…"). Apague duplicatas e faça deploy uma vez |
| 10 | Refresh | Só em modelo "vivo". Desktop: MCP. Fabric: MCP ou Enhanced Refresh API. Erro de credencial: **pare** e mande o usuário ao portal |
| 11 | Manage in Fabric | `az rest`. Data sources/parâmetros/permissões via Power BI REST. Connection binding via Fabric **Bind Semantic Model Connection** (substitui `BindToGateway`), **uma requisição por data source**; tipos gateway, cloud, VNet, automatic, none |

### 13.3 Endpoints [upstream]
Fabric Items API (`--resource https://api.fabric.microsoft.com`, base `https://api.fabric.microsoft.com/v1`):
| Método | Caminho | Uso |
|---|---|---|
| GET | `/workspaces/{wsId}` | Confirmar `capacityId` antes de criar |
| POST | `/workspaces/{wsId}/semanticModels` | Criar com definição TMDL completa (LRO) |
| POST | `/workspaces/{wsId}/semanticModels/{id}/getDefinition?format=TMDL` | Baixar a definição (é POST) |
| POST | `/workspaces/{wsId}/semanticModels/{id}/updateDefinition` | Substituir a definição inteira (LRO) |

Power BI Datasets API (`--resource https://analysis.windows.net/powerbi/api`, base `https://api.powerbi.com/v1.0/myorg`, `…` = `/groups/{wsId}/datasets/{id}`):
`POST …/refreshes` · `GET …/refreshes?$top=5` · `DELETE …/refreshes/{refreshId}` (só `ViaEnhancedApi`) · `GET/PATCH …/refreshSchedule` · `GET …/datasources` · `GET …/parameters` · `POST …/Default.UpdateParameters` (depois refresh) · `GET/POST/PUT …/users` · `POST …/executeQueries`.

Regras:
- Sempre passe `--resource`. Audiência errada retorna 401.
- Payload: `{"definition": {"format": "TMDL", "parts": [{"path", "payload" (base64), "payloadType": "InlineBase64"}]}}`.
- Partes obrigatórias: `definition.pbism`, `definition/database.tmdl`, `definition/model.tmdl` e ≥ 1 `definition/tables/*.tmdl`.
- **`updateDefinition` exige todas as partes**; omitir uma parte a apaga. Nunca envie `.platform` em updates.
- 202 → poll do `Operation-Id` até Succeeded e depois `/result`.
- `executeQueries`: 1 query por requisição; limite de 100k linhas, 1M valores ou 15 MB; 120 req/min por usuário; exige Build.

### 13.4 Checklist de validação [upstream]
1. Estrutura PBIP íntegra (se veio de PBIP).
2. Toda mudança revisada contra as guidelines de modelagem e Direct Lake.
3. (Modelo vivo) Testar cada medida nova: `EVALUATE { [Measure Name] }`; conferir `EVALUATE INFO.MEASURES()` → coluna `ErrorMessage`.
4. (Modelo vivo) Refresh das tabelas novas. Falha costuma indicar `sourceColumn` errado, M inválido ou entidade Direct Lake errada.

### 13.5 Troubleshooting [upstream]
| Sintoma | Ação |
|---|---|
| 403 / identity None | Precisa de Contributor+. Pare, sem retry |
| 401 | Corrija `--resource` uma vez. Persistiu = permissão |
| 202 sem resultado | Poll do LRO |
| Partes sumiram após update | Envie todas as partes |
| Erros DAX | Nomes são case-sensitive; objetos devem existir |
| Falha no deploy | Permissões, compatibility level, referências de expressão Direct Lake |

---

## 14. Preparação para IA (Copilot / Data Agents) [upstream]
Checklist sequencial (falha numa etapa anterior invalida as seguintes):
1. **Contexto de negócio**: conversar com o usuário, olhar relatórios existentes, achar métricas disputadas (margem, orçamento, forecast) e vocabulário.
2. **Arquitetura**: star schema, tipos corretos, medidas explícitas para toda métrica-chave, hierarquias, `SummarizeBy = None` em IDs/anos/CEP, coluna de rótulo padrão, remover sobras.
3. **Nomes** legíveis no idioma do usuário + sinônimos.
4. **Descrições**: o Copilot lê só os **primeiros 200 caracteres**. Coloque uso, desambiguação, grão e unidade primeiro.
5. **AI Instructions** (até 10.000 caracteres), **AI Data Schema** e **Verified Answers**: o agente só **sugere**. O usuário configura em "Prep data for AI".
- Classifique cada achado como **Agent-editable** (TOM via MCP/TMDL) ou **User configuration – Prep data for AI**.
- Confirme que Copilot e Q&A estão habilitados (em PBIP, `qnaEnabled: true` no `definition.pbism`).

---

## 15. Descoberta de metadados via DAX (`INFO.VIEW.*`) [upstream]
```dax
-- 1) Estimar escopo
EVALUATE
ROW (
    "Tables",        COUNTROWS ( INFO.VIEW.TABLES () ),
    "Columns",       COUNTROWS ( INFO.VIEW.COLUMNS () ),
    "Measures",      COUNTROWS ( INFO.VIEW.MEASURES () ),
    "Relationships", COUNTROWS ( INFO.VIEW.RELATIONSHIPS () )
)

-- 2) Filtrar e projetar só o necessário (ORDER BY usa o alias novo)
EVALUATE
SELECTCOLUMNS (
    FILTER ( INFO.VIEW.MEASURES (), [Table] = "Sales" ),
    "Measure", [Name],
    "Expr", [Expression]
)
ORDER BY [Measure]

-- 3) Schema de uma função sem dados
EVALUATE TOPN ( 0, INFO.VIEW.COLUMNS () )
```
- Muitas funções `INFO.*` exigem permissão elevada. Nesse caso, volte para `INFO.VIEW.*`.
- Dependências: `INFO.DEPENDENCIES` (nomes de colunas variam por versão, então rode uma sonda sem filtro antes).
- Os nomes das colunas de retorno (`[Table]`, `[Name]`, `[Expression]`) podem variar. Confirme com a sonda `TOPN(0, ...)`.

---

## 16. Handoffs entre skills upstream
- Publicação de projeto PBIP e visuais → **`powerbi-report-cli`**.
- Perguntas de negócio em linguagem natural → **`fabriciq`** (endpoint `https://fabriciq.svc.cloud.microsoft/v1/mcp/fabriciq` desde 0.3.17; a ferramenta `ResolveFabricItem` substituiu `ResolveReportIdFromUrl`).
- `semantic-model-consumption`, `powerbi-consumption-cli` e `powerbi-authoring-cli` **não existem** na v0.3.18 (404). `powerbi-authoring` é o nome do **bundle/plugin**, não de uma skill.
