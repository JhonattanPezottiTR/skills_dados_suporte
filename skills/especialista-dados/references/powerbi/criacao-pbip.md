# Criação de BI como projeto PBIP completo (TMDL + PBIR + tema TR Clario)
> Última atualização: 2026-09-29 · Fonte: regra do usuário (2026-09-29: "todo BI pedido é entregue como PBIP completo gerado localmente"); PBIP reais do time salvos pelo Power BI Desktop 2.157 (26.08); schemas públicos `developer.microsoft.com/json-schemas/fabric/...` (report 3.3.0, page 2.0.0, visualContainer 2.6.0, pagesMetadata 1.1.0, definitionProperties 2.0.0, semanticModel definitionProperties 1.0.0, platformProperties 2.0.0, pbipProperties 1.0.0); Microsoft Learn (PBIP, TMDL, PBIR, conector Dataflows); `scripts/gerar_pbip.py` · Links: https://learn.microsoft.com/en-us/power-bi/developer/projects/projects-overview · https://learn.microsoft.com/en-us/analysis-services/tmdl/tmdl-overview · https://learn.microsoft.com/en-us/power-bi/developer/projects/projects-report · https://learn.microsoft.com/en-us/power-query/connectors/dataflows · https://github.com/microsoft/json-schemas/tree/main/fabric/item/report

**Regra do usuário:** quando pedirem para **criar um BI**, a entrega é o **projeto PBIP completo**:
- modelo TMDL: tabelas, **relacionamentos**, medidas DAX e tabela de datas;
- relatório PBIR: páginas e visuais;
- tema oficial TR Clario aplicado (COR-001).

O usuário abre o projeto no Power BI Desktop, atualiza com o login dele e **publica manualmente** no workspace **Dominio FLOWS**. A IA não publica nada, e as fontes são somente leitura.

### Padrão obrigatório de todo BI (regra do usuário, 2026-09-29)
| # | Exigência | Como cumprir |
|---|---|---|
| 1 | Fontes = **tabelas dos Dataflows do Dominio FLOWS** | Entidades de `dados-fluxos-powerbi.md` e colunas/tipos de `dados-fluxo-<df>.md`. Os ids dos dataflows estão em `powerbi-servico-powerbi.md`. Nunca invente coluna. |
| 2 | **JSON de cores e padrões** | Registrar `tema-oficial-powerbi.json` sem alterações. Seguir COR-001..006. Nenhuma cor fora da paleta. |
| 3 | **Boas práticas Microsoft** + regras do time | Avaliar `powerbi-modelagem.md`, `powerbi-dax-padroes.md`, `powerbi-relatorios.md` e `fabric-catalogo-skills-upstream.md` (semantic-model-authoring, powerbi-report-cli), mais `regras-negocio.md` e `negocio-*`. |
| 4 | **Relacionamento de tabelas** | Star schema: fato → dimensões e `dCalendario`, 1:N, direção única, chaves com o mesmo tipo, colunas técnicas ocultas. |
| 5 | **Boa apresentação de dados** | Visual certo para cada pergunta; 3–4 KPIs no topo; filtros agrupados; títulos com o insight; 5–7 grupos por página; texto alternativo; formato BR. |
| 6 | **Medidas comentadas** | Toda medida tem `///` descrição (o que calcula e qual regra usa) **e** comentário `//` no topo do DAX. Passos não triviais levam `//` explicativo. Métrica não validada leva `[Em revisão]`. |
| 7 | **Calendário oficial `DB_SGD_ALL.calendar`** | Todo BI com vínculo de data usa a entidade `calendar` do Dataflow `DB_SGD_ALL` como `dCalendario`, marcada como tabela de datas. A entidade traz `date` → Data, `holiday` → Feriado, `day_useful_month`/`day_useful_year` → Dia útil do mês/ano e `ten_name` → Decêndio; somam-se as colunas PT-BR de ano, mês, trimestre e semana. **Toda** data de fato se relaciona com `dCalendario[Data]`, e filtros e eixos de tempo usam colunas do `dCalendario`. Calendário só em M é exceção. |
| 8 | **Visuais criados, usuário só publica** | Entregar modelo + páginas + visuais prontos. O usuário só abre, faz login no Dataflow, atualiza e publica. |

Exemplo de medida comentada (TMDL):
```
	/// Taxa de insatisfação: SSCs avaliadas como insatisfeitas ÷ SSCs avaliadas. Regra: satisfação 3–4 = insatisfeito (Em revisão).
	measure '% Insatisfação' = ```
			// Taxa de insatisfação: insatisfeitas ÷ avaliadas (quem não opinou fica fora do denominador).
			VAR _Avaliadas = CALCULATE ( [Qtd SSC], fSSC[Satisfação] IN { 1, 2, 3, 4 } )
			VAR _Insatisfeitas = CALCULATE ( [Qtd SSC], fSSC[Satisfação] IN { 3, 4 } )  // 3–4 = insatisfeito
			RETURN
			    DIVIDE ( _Insatisfeitas, _Avaliadas )
			```
		formatString: 0.0%;-0.0%;0.0%
		displayFolder: Satisfação
```

---

## 1. Como a IA usa este arquivo

| Ambiente | Como entregar |
|---|---|
| **Claude Code (repositório)** | Monta a especificação JSON (§3) → `python scripts/gerar_pbip.py <spec> --validar` → gera em `saidas/bi/<nome>/`. Procedimento completo: `/criar-bi` |
| **Open Arena (sem script)** | Escreve **todos os arquivos** da §2 à mão, um bloco de código por arquivo, com o caminho completo no título. Segue os modelos das §4–§6 **literalmente** (nomes de chave, `$schema`, indentação com TAB no TMDL). No fim, faz a checagem da §8 e entrega o checklist da §9 |

Antes de montar, sempre:
1. Escolha a entidade do Dataflow: `dados-fluxos-powerbi.md` → `dados-fluxo-<df>.md` (colunas e **tipos reais**).
2. Confira o conceito de negócio: `negocio-indice.md`.
3. Informe a linhagem (RG-11).
4. Nunca invente coluna (RG-01).
5. Medidas seguem `powerbi-dax-padroes.md`. Métrica com regra não validada vai marcada **[Em revisão]** na descrição e é avisada ao usuário.
6. Layout segue `powerbi-relatorios.md` §6. Cores seguem `powerbi-tema-cores.md`.

---

## 2. Anatomia do projeto gerado

```text
<nome>/
  <nome>.pbip                                  atalho que o Desktop abre (aponta para o .Report)
  .gitignore                                   **/.pbi/localSettings.json, **/.pbi/cache.abf
  LEIA-ME.md                                   resumo + checklist (só no gerador)
  <nome>.SemanticModel/
    .platform                                  type SemanticModel, logicalId (GUID)
    definition.pbism                           version 4.2 (formato TMDL)
    definition/
      database.tmdl                            compatibilityLevel
      model.tmdl                               cultura pt-BR, opções, ref table
      expressions.tmdl                         parâmetros WorkspaceId / DataflowId_<DF> + navegação do dataflow
      relationships.tmdl
      tables/<Tabela>.tmdl                     1 arquivo por tabela (fatos, dCalendario, _Medidas)
  <nome>.Report/
    .platform                                  type Report
    definition.pbir                            byPath → ../<nome>.SemanticModel
    definition/
      version.json                             "2.0.0"
      report.json                              themeCollection + resourcePackages
      pages/pages.json                         pageOrder + activePageName
      pages/<pageId>/page.json                 1280×720, FitToPage
      pages/<pageId>/visuals/<visualId>/visual.json
    StaticResources/
      RegisteredResources/PadraoTRClario-<12hex>.json      = tema-oficial-powerbi.json SEM alterações
      SharedResources/BaseThemes/CY24SU06.json             base theme da Microsoft (cópia da instalação do Desktop)
```

- **IDs:** página e visual usam **20 caracteres hex minúsculos**, únicos. O visual é único na página e o nome da pasta é igual ao `name`. `logicalId` e nome de relacionamento usam GUID. O gerador usa IDs determinísticos (hash do nome), então regerar mantém os mesmos IDs.
- **Codificação:** UTF-8 sem BOM, com CRLF, como grava o Desktop. O Desktop também lê LF.
- Página nova só aparece se estiver em `pageOrder`.
- Sem `lineageTag`: o Desktop gera ao salvar.
- Sem `diagramLayout.json` e sem `cultures/`: o Desktop também cria esses dois.

---

## 3. Especificação do gerador (JSON)

O exemplo completo está em `config/exemplos-bi/exemplo-metas.json`. Chaves que começam com `_` são comentários.

| Chave | Obrigatória | Conteúdo |
|---|---|---|
| `nome` | sim | Pasta e arquivos (`[A-Za-z0-9 _.-]`, recomendado kebab-case) |
| `titulo`, `descricao` | não | Título do LEIA-ME; documentação |
| `workspace_id` | não | Padrão: `config/powerbi.json` (Dominio FLOWS) |
| `dataflows.<DF>.id` | não | objectId do dataflow. Sem ele, o gerador procura **pelo nome** em `.dados-sync/powerbi-servico.json` (gravado pelo inventário com login). Se não achar, dá erro com instrução |
| `tabelas[]` | sim | `nome`, `descricao`, `dataflow`, `entidade`, `colunas[]`, `colunas_derivadas[]` |
| `tabelas[].colunas[]` | não (padrão: todas) | `origem` (atributo do model.json), `nome` (PT-BR), `tipo`, `oculta`, `formato`, `resumir`, `chave`, `pasta`, `ordenar_por`, `descricao` |
| `tabelas[].colunas_derivadas[]` | não | `nome`, `origem`, `conversao` = `numero_para_data` \| `texto_para_data` (+`formato_texto`) \| `data_de_datahora` \| `m` (+`m`: corpo de `each`), `tipo` |
| `calendario` | não (padrão: `DB_SGD_ALL.calendar`) | `nome` (`dCalendario`), `inicio` (AAAA-MM-DD), `anos_futuros`, `fonte` (`dataflow` = padrão oficial; `m` = gerado em Power Query, só como exceção). `false` desliga |
| `relacionamentos[]` | não | `de` = `Fato[Chave]` (lado muitos), `para` = `Dim[Chave]` (lado um), `ativo` (true), `direcao` (`unica`\|`ambas`) |
| `tabela_medidas` | não | Padrão `_Medidas` |
| `medidas[]` | não | `nome`, `expressao` (DAX; `\n` para multilinha), `formato`, `pasta`, `descricao`, `status` (`Em revisão`) |
| `paginas[]` | sim | `nome`, `titulo`, `subtitulo`, `visuais[]` |
| `paginas[].visuais[]` | — | `tipo`, `titulo`, `campos`, `grade` ou `posicao`, `ordenar`, `modo` (slicer), `rotulos_de_dados`, `cores`, `cor_condicional`, `texto_alternativo`, `texto` (textbox) |

Tipos aceitos (`tipo`): `string`/texto, `int64`/inteiro, `decimal`/moeda, `double`, `date`/data, `dateTime`, `time`/hora, `boolean`.

Formatos nomeados (`formato`):

| Nome | formatString |
|---|---|
| `inteiro` | `#,0` |
| `decimal` | `#,0.00` |
| `decimal1` | `#,0.0` |
| `percentual` | `0.0%` |
| `percentual2` | `0.00%` |
| `moeda` | `\R$\ #,0.00` |
| `milhares` | `#,0, \m\i\l` |
| `data` | `dd/mm/yyyy` |

Também aceita qualquer formatString literal.

Campos em visuais e relacionamentos:
- coluna: `Tabela[Coluna]` ou `'Tabela com espaço'[Coluna]`;
- medida: `[Medida]`;
- com rótulo: `{"campo": "...", "rotulo": "..."}`.

Papéis (`campos`) por tipo de visual (apelidos pt-BR → `visualType`):

| Apelido → visualType | Papéis (spec → PBIR) | Regras |
|---|---|---|
| `cartao` → `card` | `valores`→`Values` | 1 **medida**. Título do container ligado e rótulo de categoria desligado |
| `cartao_novo` → `cardVisual` | `valores`→`Data` | medidas |
| `kpi` → `kpi` | `indicador`→`Indicator`, `tendencia`→`TrendLine`, `meta`→`Goal` | Indicator/Goal são medidas; TrendLine é coluna de data |
| `barra` → `clusteredBarChart` · `coluna` → `clusteredColumnChart` · `linha` → `lineChart` | `categoria`→`Category`, `valores`→`Y`, `legenda`→`Series`, `dicas`→`Tooltips` | Category/Series são colunas; Y/Tooltips são medidas. Linha ordena a categoria em ordem crescente por padrão |
| `pizza` → `pieChart` · `rosca` → `donutChart` | `categoria`→`Category`, `valores`→`Y` | no máximo 5 fatias (anti-pattern) |
| `tabela` → `tableEx` | `valores`→`Values` | colunas e medidas |
| `segmentacao` → `slicer` | `valores`→`Values` | 1 coluna. `modo`: `entre` (padrão para data/número), `suspenso` (padrão para texto), `lista`. O título vira o cabeçalho |
| `texto` → `textbox` | — | `texto`, `subtitulo`, `tamanho` |

**Grade (1280×720):**
- margem 24, gutter 16;
- **12 colunas** de 88 px: `x = 24 + (col−1)·104` e `largura = larg·88 + (larg−1)·16`;
- **10 linhas** de 48 px a partir de y = 72: `y = 72 + (lin−1)·64` e `altura = alt·48 + (alt−1)·16`;
- faixa de título em y 16–64 (textbox automático com `titulo`/`subtitulo` da página);
- tudo é múltiplo de 8;
- sem `grade`, o visual vai para a primeira célula livre (padrões: cartão/slicer 3×2, gráficos 6×4, pizza 4×4, tabela 12×4);
- sobreposição ou estouro de limite é erro;
- `z` e `tabOrder` seguem a ordem de leitura, em passos de 1000.

**Validações do gerador:**
- JSON válido;
- nomes únicos (sem diferenciar maiúsculas);
- dataflow, entidade e colunas existentes no `model.json`;
- tipos válidos;
- DAX: toda `Tabela[Coluna]` e `[Medida]` existe e os parênteses estão balanceados;
- papéis de medida × coluna, obrigatórios e máximos por visual;
- relacionamento: colunas existentes, tipos iguais, um ativo por par e FK oculta automaticamente;
- `ordenar_por` existe;
- grade dentro dos limites e sem sobreposição;
- cores só da paleta (COR-001/003);
- todo JSON gerado é reaberto;
- `pageOrder` bate com as páginas.

Com erro, **nada é gravado** e todos os erros são listados em pt-BR.

---

## 4. Modelo semântico (TMDL) — sintaxe usada

Regras de sintaxe:
- Indentação com **TAB**. Propriedades ficam um nível abaixo do objeto.
- Expressão multilinha:
  - em `measure`, o corpo fica 1 nível abaixo das propriedades (3 TABs), entre três crases;
  - em `partition … source =`, o corpo fica 2 níveis abaixo de `source` (4 TABs);
  - em `expression` raiz, o corpo tem 2 TABs.
- Nome com espaço, acento ou símbolo vai entre aspas simples: `'Nº de analistas'`. Aspa simples interna é dobrada.
- Descrição com `///` na linha acima do objeto. Não existe comentário `//` fora de M/DAX.
- `formatString` nunca começa com `"`. Use `\R$\ #,0.00`, não `"R$" #,0.00`.
- Booleanos são flag sozinha: `isHidden`, `isKey`, `discourageImplicitMeasures`.

### 4.1 `definition.pbism`, `.platform`, `database.tmdl`, `model.tmdl`
```json
{ "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/semanticModel/definitionProperties/1.0.0/schema.json",
  "version": "4.2", "settings": { "qnaEnabled": true } }
```
```json
{ "$schema": "https://developer.microsoft.com/json-schemas/fabric/gitIntegration/platformProperties/2.0.0/schema.json",
  "metadata": { "type": "SemanticModel", "displayName": "metas-teste" },
  "config": { "version": "2.0", "logicalId": "<GUID novo>" } }
```
```tmdl
database
	compatibilityLevel: 1606
```
```tmdl
model Model
	culture: pt-BR
	defaultPowerBIDataSourceVersion: powerBI_V3
	discourageImplicitMeasures
	sourceQueryCulture: pt-BR
	dataAccessOptions
		legacyRedirects
		returnErrorValuesAsNull

annotation __PBI_TimeIntelligenceEnabled = 0

ref table Metas
ref table dCalendario
ref table _Medidas
```
- `compatibilityLevel: 1606` é o nível gravado pelo Desktop do time.
- `__PBI_TimeIntelligenceEnabled = 0` desliga o auto date/time, que criaria `LocalDateTable_*`. É a forma como o Desktop grava essa opção, a única anotação `PBI` usada.
- `discourageImplicitMeasures` obriga medidas explícitas (RG-05).

### 4.2 Conector de Dataflow (`expressions.tmdl`)
```tmdl
/// ID do workspace Dominio FLOWS (config/powerbi.json). Não é segredo.
expression WorkspaceId = "0db4c1a0-c589-45bb-a610-fe2dd81279d1" meta [IsParameterQuery=true, Type="Text", IsParameterQueryRequired=true]

/// ID (objectId) do dataflow DB_METAS no workspace Dominio FLOWS.
expression DataflowId_DB_METAS = "85a9bf63-6a68-4ade-a063-dcf4709bdf63" meta [IsParameterQuery=true, Type="Text", IsParameterQueryRequired=true]

/// Navegação até o dataflow DB_METAS (não carregada; as tabelas partem daqui).
expression 'Dataflow DB_METAS' =
		let
		    Fonte = PowerPlatform.Dataflows(null),
		    Workspaces = Fonte{[Id = "Workspaces"]}[Data],
		    Workspace = Workspaces{[workspaceId = WorkspaceId]}[Data],
		    Dataflow = Workspace{[dataflowId = DataflowId_DB_METAS]}[Data]
		in
		    Dataflow
```
- A navegação `Workspaces → workspaceId → dataflowId → {[entity="<entidade>", version=""]}` é a que o Desktop gera. É o mesmo padrão dos PBIX do time (`catalogo-pbix.md`).
- `PowerPlatform.Dataflows(null)` **não leva credencial no arquivo**. No 1º refresh, o Desktop pede login (Conta organizacional). No serviço, a credencial é OAuth2 do dataset.
- Ler o dataflow exige permissão de leitura no workspace. Para Dataflow Gen2, exige Contributor ou maior [Learn].
- Onde achar os IDs: `WorkspaceId` em `config/powerbi.json`; `objectId` do dataflow em `dados-servico-powerbi.md` / `.dados-sync/powerbi-servico.json`, ou na URL do dataflow no serviço (`.../dataflows/<id>`).
- Os IDs de DB_METAS acima são reais (inventário de 2026-09-29).
- **Sem o id (Open Arena):** use o placeholder `"<ID_DO_DATAFLOW>"` e avise o usuário para preencher em *Transformar dados → Gerenciar parâmetros*. Como alternativa manual, dá para navegar pelo nome com `Workspace{[dataflowName = "DB_METAS"]}[Data]`. Esse caminho não foi testado no Desktop do time, então prefira o id.

### 4.3 Tabela fato (colunas tipadas + partição M)
```tmdl
/// Fato de metas: 1 linha por dia × e-mail × descrição da meta ...
table Metas

	/// E-mail do analista (sem espaços). Chave do analista.
	column 'E-mail'
		dataType: string
		summarizeBy: none
		sourceColumn: E-mail

	column 'Valor da meta'
		dataType: decimal
		isHidden
		formatString: #,0.00
		summarizeBy: sum
		sourceColumn: Valor da meta

	column Data
		dataType: dateTime
		isHidden
		formatString: Short Date
		summarizeBy: none
		sourceColumn: Data

		annotation UnderlyingDateTimeDataType = Date

	partition Metas = m
		mode: import
		source =
				let
				    Fonte = #"Dataflow DB_METAS",
				    Entidade = Fonte{[entity = "goals", version = ""]}[Data],
				    #"Colunas selecionadas" = Table.SelectColumns(Entidade, {"email", "valormeta", "date"}),
				    #"Tipos definidos" = Table.TransformColumnTypes(#"Colunas selecionadas", {{"email", type text}, {"valormeta", Currency.Type}, {"date", Int64.Type}}),
				    #"Coluna Data adicionada" = Table.AddColumn(#"Tipos definidos", "Data", each let v = Record.Field(_, "date") in if v = null then null else if v >= 19000101 then #date(Number.IntegerDivide(v, 10000), Number.Mod(Number.IntegerDivide(v, 100), 100), Number.Mod(v, 100)) else Date.From(v), type date),
				    #"Colunas renomeadas" = Table.RenameColumns(#"Coluna Data adicionada", {{"email", "E-mail"}, {"valormeta", "Valor da meta"}}),
				    #"Colunas finais" = Table.SelectColumns(#"Colunas renomeadas", {"E-mail", "Valor da meta", "Data"})
				in
				    #"Colunas finais"
```
Mapeamento de tipos (dataType do `model.json` → TMDL / M):

| Dataflow | TMDL `dataType` | Tipo M | Observação |
|---|---|---|---|
| `string` | `string` | `type text` | `summarizeBy: none` |
| `int64` | `int64` | `Int64.Type` | ID/código/ano/mês → `summarizeBy: none`, formato `0` |
| `double` | **`decimal`** | `Currency.Type` | Valores e metas em decimal fixo (4 casas). `double` só se a precisão exigir (modelagem §5) |
| `date` | `dateTime` + `annotation UnderlyingDateTimeDataType = Date` | `type date` | formato `Short Date` |
| `dateTime` | `dateTime` | `type datetime` | Para relacionar com o calendário, derive uma coluna só de data |
| `time` | `dateTime` + `UnderlyingDateTimeDataType = Time` | `type time` | formato `Long Time` |
| `boolean` | `boolean` | `type logical` | |

- `sourceColumn` = nome final da coluna **depois** do M. O gerador renomeia no M, e o TMDL usa o nome PT-BR.
- Toda coluna do TMDL precisa sair do M com o mesmo nome e tipo (`Table.SelectColumns` final).
- **Data que chega como número** (caso real: `DB_METAS.goals[date]` é `int64`):
  - o fluxo faz `date → Int64.Type`, o que gera o **serial de data** (dias desde 30/12/1899, ex.: 46000 ≈ 2025-12);
  - `Date.From(v)` converte de volta;
  - o M acima trata também `AAAAMMDD` (≥ 19000101);
  - sem essa conversão, o relacionamento com `dCalendario[Data]` é impossível (int64 × dateTime).
  O gerador faz isso com `colunas_derivadas` + `conversao: numero_para_data`.

### 4.4 Tabela de datas `dCalendario` — **fonte oficial: `DB_SGD_ALL.calendar`**
**Regra do usuário (2026-09-29):** tudo que tiver vínculo de data usa o calendário do Dataflow `DB_SGD_ALL`, entidade `calendar` (Postgres `DB_SGD.public.calendar`), para relacionamentos e filtros. A partição do `dCalendario` começa assim; as colunas PT-BR de ano, mês, trimestre e semana vêm depois, iguais ao modelo abaixo:
```m
let
    DataInicial = #date(2023, 1, 1),
    DataFinal = Date.EndOfYear(Date.AddYears(Date.From(DateTime.LocalNow()), 1)),
    // Calendário oficial do time: DB_SGD_ALL.calendar (feriados e dias úteis).
    Fonte = #"Dataflow DB_SGD_ALL",
    Entidade = Fonte{[entity = "calendar", version = ""]}[Data],
    Selecionadas = Table.SelectColumns(Entidade, {"date", "holiday", "day_useful_month", "day_useful_year", "ten_name"}),
    Tipos = Table.TransformColumnTypes(Selecionadas, {{"date", type date}, {"holiday", type text}, {"day_useful_month", Int64.Type}, {"day_useful_year", Int64.Type}, {"ten_name", type text}}),
    Renomeadas = Table.RenameColumns(Tipos, {{"date", "Data"}, {"holiday", "Feriado"}, {"day_useful_month", "Dia útil do mês"}, {"day_useful_year", "Dia útil do ano"}, {"ten_name", "Decêndio"}}),
    Periodo = Table.SelectRows(Renomeadas, each [Data] <> null and [Data] >= DataInicial and [Data] <= DataFinal),
    Tabela = Table.Distinct(Periodo, {"Data"}),
    // ... colunas Ano, Trimestre, Mês, Mês/Ano, AnoMês, Dia da semana, Semana do ano, Fim de semana (como abaixo)
```
- Isso exige o parâmetro `DataflowId_DB_SGD_ALL` e a expressão `'Dataflow DB_SGD_ALL'` no `expressions.tmdl`. O gerador inclui os dois sozinho.
- ⚠️ Para marcar como tabela de datas, o intervalo precisa ser **contínuo**: uma linha por dia, sem buracos. Se o Desktop recusar a marcação, a `public.calendar` tem dias faltando no período; avise o usuário.
- O modelo abaixo, com o calendário gerado só em M, é a **alternativa** (`"calendario": {"fonte": "m"}`), para quando o `DB_SGD_ALL` não puder ser usado.

```tmdl
/// Tabela de datas (calendário) gerada em Power Query. Marcada como tabela de datas.
table dCalendario
	dataCategory: Time

	column Data
		dataType: dateTime
		isKey
		formatString: Short Date
		summarizeBy: none
		sourceColumn: Data

		annotation UnderlyingDateTimeDataType = Date

	column 'Mês/Ano'
		dataType: string
		summarizeBy: none
		sourceColumn: Mês/Ano
		sortByColumn: AnoMês

	hierarchy 'Calendário'

		level Ano
			column: Ano

		level Mês
			column: Mês
```
- `dataCategory: Time` na tabela + `isKey` na coluna `Data` = **"Marcar como tabela de datas"**. É a única coluna com `isKey`.
- Colunas geradas:

| Coluna | Tipo | Exemplo / observação |
|---|---|---|
| `Data` | data | |
| `Ano` | int64 | |
| `Nº do trimestre` | int64 | oculta |
| `Trimestre` | texto | "T1" |
| `Ano/Trimestre` | texto | "2026 T1" |
| `Nº do mês` | int64 | |
| `Mês` | texto | "Janeiro" |
| `Mês abreviado` | texto | "Jan" |
| `AnoMês` | int64 | 202601, oculta |
| `Mês/Ano` | texto | "Jan/2026" |
| `Início do mês` | data | |
| `Dia` | int64 | |
| `Nº do dia da semana` | int64 | 1 = segunda, oculta |
| `Dia da semana` | texto | |
| `Semana do ano` | int64 | |
| `Fim de semana` | texto | Sim/Não |

- Ordenação:
  - `Mês` e `Mês abreviado` → `Nº do mês`;
  - `Mês/Ano` → `AnoMês`;
  - `Trimestre` → `Nº do trimestre`;
  - `Dia da semana` → `Nº do dia da semana`.
- Hierarquia `Calendário`: Ano > Trimestre > Mês > Data.
- Partição M (contínua, sem lacunas, cultura pt-BR). Trecho:
```powerquery
let
    DataInicial = #date(2023, 1, 1),
    DataFinal = Date.EndOfYear(Date.AddYears(Date.From(DateTime.LocalNow()), 1)),
    Datas = List.Dates(DataInicial, Duration.Days(DataFinal - DataInicial) + 1, #duration(1, 0, 0, 0)),
    Tabela = Table.FromList(Datas, Splitter.SplitByNothing(), type table [Data = date]),
    Maiuscula = (t as text) as text => Text.Upper(Text.Start(t, 1)) & Text.Middle(t, 1),
    Ano = Table.AddColumn(Tabela, "Ano", each Date.Year([Data]), Int64.Type),
    NumMes = Table.AddColumn(Ano, "Nº do mês", each Date.Month([Data]), Int64.Type),
    Mes = Table.AddColumn(NumMes, "Mês", each Maiuscula(Date.MonthName([Data], "pt-BR")), type text),
    AnoMes = Table.AddColumn(Mes, "AnoMês", each [Ano] * 100 + [#"Nº do mês"], Int64.Type),
    MesAno = Table.AddColumn(AnoMes, "Mês/Ano", each Text.Start([#"Mês"], 3) & "/" & Text.From([Ano]), type text)
in
    MesAno
```
Calendário em M é o recomendado pelo upstream para modelo novo. Em DAX (`CALENDAR`), só se o usuário pedir.

### 4.5 Relacionamentos
```tmdl
relationship 13f3960b-6808-5c31-8687-d3fad738357a
	fromColumn: Metas.Data
	toColumn: dCalendario.Data
```
- `fromColumn` é o lado **muitos** (fato) e `toColumn` o lado **um** (dimensão).
- Padrão: 1:N, direção única, ativo.
- Opcionais: `isActive: false` (role-playing + `USERELATIONSHIP`) e `crossFilteringBehavior: bothDirections` (evitar).
- Os tipos precisam ser iguais nos dois lados.
- A FK do fato fica oculta (`isHidden`). Os slicers usam a coluna da dimensão.

### 4.6 Tabela de medidas `_Medidas`
```tmdl
/// Tabela só de medidas (a coluna é técnica e fica oculta).
table _Medidas

	/// [Em revisão] Soma das metas: 1 valor por analista × meta × mês (MAX) ...
	measure 'Meta total' = ```
			VAR _MetaPorAnalistaMes =
			    SUMMARIZE ( Metas, Metas[E-mail], Metas[Descrição da meta], dCalendario[AnoMês] )
			RETURN
			    SUMX ( _MetaPorAnalistaMes, CALCULATE ( MAX ( Metas[Valor da meta] ) ) )
			```
		formatString: #,0.00
		displayFolder: Metas

	/// Quantidade de analistas (e-mails distintos) com meta no contexto de filtro.
	measure 'Nº de analistas' = DISTINCTCOUNT ( Metas[E-mail] )
		formatString: #,0
		displayFolder: Metas

	column 'Coluna oculta'
		dataType: string
		isHidden
		summarizeBy: none
		sourceColumn: Coluna oculta

	partition _Medidas = m
		mode: import
		source =
				let
				    Fonte = #table(type table [#"Coluna oculta" = text], {})
				in
				    Fonte
```
- Convenção do time: todas as medidas ficam em `_Medidas` (pedido do usuário). Isso difere do upstream, que distribui as medidas nas tabelas.
- Com a única coluna oculta, o Desktop mostra `_Medidas` como tabela de medidas.
- `formatString` segue o padrão invariável. A cultura pt-BR do modelo exibe `1.234,56`.
- Toda medida visível leva `formatString`, `displayFolder` e descrição `///`, que começa com `[Em revisão]` quando a regra não foi validada.
- **Grão de `DB_METAS.goals`:** o Dataflow expande a competência pelo calendário e repete `valormeta` em cada dia. `SUM(Metas[Valor da meta])` **multiplica** a meta. Use o padrão acima (1 valor por analista × meta × mês).

---

## 5. Relatório (PBIR) — arquivos fixos

```json
// <nome>.pbip
{ "$schema": "https://developer.microsoft.com/json-schemas/fabric/pbip/pbipProperties/1.0.0/schema.json",
  "version": "1.0", "artifacts": [ { "report": { "path": "metas-teste.Report" } } ],
  "settings": { "enableAutoRecovery": true } }

// <nome>.Report/definition.pbir  (modelo local; para publicar pelo Desktop não precisa mudar)
{ "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definitionProperties/2.0.0/schema.json",
  "version": "4.0", "datasetReference": { "byPath": { "path": "../metas-teste.SemanticModel" } } }

// <nome>.Report/definition/version.json
{ "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/versionMetadata/1.0.0/schema.json",
  "version": "2.0.0" }

// <nome>.Report/definition/pages/pages.json
{ "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/pagesMetadata/1.1.0/schema.json",
  "pageOrder": [ "1e422d629b61efa3165a" ], "activePageName": "1e422d629b61efa3165a" }

// <nome>.Report/definition/pages/<id>/page.json
{ "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/page/2.0.0/schema.json",
  "name": "1e422d629b61efa3165a", "displayName": "Metas", "displayOption": "FitToPage",
  "height": 720, "width": 1280 }
```
(Os comentários `//` acima são só para leitura. JSON real não tem comentários.)

**Tema (`report.json`):**
- O arquivo `StaticResources/RegisteredResources/PadraoTRClario-<12hex>.json` é cópia **byte a byte** de `tema-oficial-powerbi.json`.
- `customTheme.name`, `items[].name` e `items[].path` são **idênticos** ao nome do arquivo, com `.json` e **sem pasta**.
- O item tem tipo `CustomTheme`.
- Troque o sufixo hex quando o tema mudar (cache do Desktop).
```json
{
  "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/report/3.3.0/schema.json",
  "themeCollection": {
    "baseTheme":   { "name": "CY24SU06", "reportVersionAtImport": { "visual": "1.8.91", "report": "2.0.91", "page": "1.3.91" }, "type": "SharedResources" },
    "customTheme": { "name": "PadraoTRClario-134e89f351a6.json", "reportVersionAtImport": { "visual": "1.8.91", "report": "2.0.91", "page": "1.3.91" }, "type": "RegisteredResources" }
  },
  "objects": { "section": [ { "properties": { "verticalAlignment": { "expr": { "Literal": { "Value": "'Top'" } } } } } ] },
  "resourcePackages": [
    { "name": "RegisteredResources", "type": "RegisteredResources",
      "items": [ { "name": "PadraoTRClario-134e89f351a6.json", "path": "PadraoTRClario-134e89f351a6.json", "type": "CustomTheme" } ] },
    { "name": "SharedResources", "type": "SharedResources",
      "items": [ { "name": "CY24SU06", "path": "BaseThemes/CY24SU06.json", "type": "BaseTheme" } ] }
  ],
  "settings": { "useStylableVisualContainerHeader": true, "exportDataMode": "AllowSummarized",
    "defaultDrillFilterOtherVisuals": true, "allowChangeFilterTypes": true,
    "useEnhancedTooltips": true, "useDefaultAggregateDisplayName": true }
}
```
**Base theme:**
- `CY24SU06` é o base theme da Microsoft. O gerador copia o arquivo da instalação do Desktop (`...\bin\WebView2Resources\minerva\sharedresources\BaseThemes\`).
- **Open Arena (sem esse arquivo):** omita `baseTheme` e o pacote `SharedResources`. O schema permite `themeCollection` só com `customTheme`, e o Desktop aplica o base padrão.

---

## 6. Visuais (`visual.json`)

Estrutura comum (schema visualContainer 2.6.0):
```json
{
  "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.6.0/schema.json",
  "name": "<20 hex>",
  "position": { "x": 24, "y": 200, "width": 712, "height": 496, "z": 5000, "tabOrder": 5000 },
  "visual": {
    "visualType": "lineChart",
    "query": {
      "queryState": {
        "Category": { "projections": [ {
          "field": { "Column": { "Expression": { "SourceRef": { "Entity": "dCalendario" } }, "Property": "Mês/Ano" } },
          "queryRef": "dCalendario.Mês/Ano", "nativeQueryRef": "Mês/Ano", "active": true } ] },
        "Y": { "projections": [ {
          "field": { "Measure": { "Expression": { "SourceRef": { "Entity": "_Medidas" } }, "Property": "Meta total" } },
          "queryRef": "_Medidas.Meta total", "nativeQueryRef": "Meta total" } ] }
      },
      "sortDefinition": { "sort": [ { "field": { "Column": { "Expression": { "SourceRef": { "Entity": "dCalendario" } }, "Property": "Mês/Ano" } }, "direction": "Ascending" } ] }
    },
    "objects": { "labels": [ { "properties": { "show": { "expr": { "Literal": { "Value": "false" } } } } } ] },
    "visualContainerObjects": {
      "title":   [ { "properties": { "show": { "expr": { "Literal": { "Value": "true" } } }, "text": { "expr": { "Literal": { "Value": "'Meta total por mês'" } } } } } ],
      "general": [ { "properties": { "altText": { "expr": { "Literal": { "Value": "'Linha com a meta total por mês.'" } } } } } ]
    },
    "drillFilterOtherVisuals": true
  }
}
```
- **Projeção:**
  - `field` usa `Column` ou `Measure` com `SourceRef.Entity` = nome da tabela;
  - `queryRef` = `Tabela.Campo`, único no visual;
  - `nativeQueryRef` = rótulo;
  - `displayName` opcional, renomeia no visual.
- **Literais:**
  - texto entre aspas simples (`"'Top'"`), com a aspa interna dobrada;
  - booleano `"true"`/`"false"`;
  - número com sufixo `D` (`"8D"`) ou `L`.
- **Cartão** (`card`): `"Values"` com 1 medida, mais `"objects": { "categoryLabels": [ { "properties": { "show": {false} } } ] }` quando o título do container está ligado.
- **Barras/colunas** (`clusteredBarChart`/`clusteredColumnChart`): `Category` + `Y`. Maior para menor: `sortDefinition` com a **medida** e `"direction": "Descending"`. Rótulos: `objects.labels.show = true`.
- **Slicer:**
  - `Values` com 1 coluna;
  - `"objects": { "data": [ { "properties": { "mode": { "expr": { "Literal": { "Value": "'Between'" } } } } } ] }`;
  - modos: `'Between'` (intervalo de datas), `'Dropdown'`, `'Basic'`;
  - o texto do cabeçalho vem do `displayName` da projeção (ex.: "Período").
- **Tabela** (`tableEx`): `Values` com colunas e medidas. Com tudo em Values e nenhuma coluna de agrupamento, as linhas não aparecem; nesse caso use `pivotTable`.
- **Pizza/rosca**: `Category` + `Y`.
- **KPI**: `Indicator` (medida), `TrendLine` (coluna de data), `Goal` (medida). Ver `powerbi-relatorios.md` §4.9.
- **Textbox** (título da página): `paragraphs` é **JSON puro** (sem `expr`):
```json
"visual": { "visualType": "textbox", "objects": { "general": [ { "properties": { "paragraphs": [
  { "textRuns": [ { "value": "Metas por analista", "textStyle": { "fontFamily": "Clario", "fontWeight": "bold", "fontSize": "16pt", "color": "#404040" } } ] },
  { "textRuns": [ { "value": "Fonte: Dataflow DB_METAS (goals)", "textStyle": { "fontFamily": "Clario", "fontSize": "10pt", "color": "#666555" } } ] }
] } } ] }, "drillFilterOtherVisuals": true }
```
- **Cor** (só quando necessário e só da paleta). Por série/medida:
  `"dataPoint": [ { "properties": { "fill": { "solid": { "color": { "expr": { "Literal": { "Value": "'#D64000'" } } } } } }, "selector": { "metadata": "_Medidas.Meta total" } } ]`
  Formatação condicional por medida que devolve hex da paleta (COR-003):
  `"dataPoint": [ { "properties": { "fill": { "solid": { "color": { "expr": { "Measure": { "Expression": { "SourceRef": { "Entity": "_Medidas" } }, "Property": "Cor status" } } } } } }, "selector": { "data": [ { "dataViewWildcard": { "matchingOption": 1 } } ] } } ]`
  Sem cor fixa, o visual herda do tema (COR-002), que é o preferido.

---

## 7. Convenções do time

| Tema | Convenção |
|---|---|
| Nomes | PT-BR legíveis, com espaços e acentos (`Descrição da meta`, `Nº de analistas`). Tabela de datas `dCalendario`, medidas em `_Medidas`. Fatos no plural (`Metas`) |
| Pastas de medidas | `displayFolder` por assunto (`Metas`, `Atendimento\Volume`...) |
| Formatos | Inteiro `#,0`, decimal `#,0.00`, % `0.0%`, moeda `\R$\ #,0.00`, data `Short Date` ou `dd/mm/yyyy`. Com a cultura pt-BR, sai `1.234,56` e `29/09/2026` |
| Tipos | Chaves `int64`, valores/metas `decimal`, datas `dateTime` (data pura com `UnderlyingDateTimeDataType = Date`). Nunca `double` sem motivo |
| Colunas | FK oculta, numéricas somáveis ocultas (expostas por medida), `summarizeBy: none` em IDs/ano/mês |
| Modelo | Import, estrela, 1:N direção única, auto date/time desligado, `discourageImplicitMeasures` |
| Relatório | Página 1280×720 FitToPage, grade de 8 px (§3), título da página em textbox, de 3 a 4 cartões, de 1 a 3 slicers à direita no topo, títulos em forma de insight, alt text em todo gráfico, tema TR Clario sem cores fixas |

---

## 8. Checagem antes de entregar (sobretudo quando escrito à mão)

1. Todo JSON é válido (sem comentários, sem vírgula sobrando) e tem o `$schema` exato das §5–§6.
2. Os IDs de página/visual têm 20 hex, a pasta tem o mesmo nome que `name` e toda página está em `pageOrder`.
3. Toda projeção aponta para uma tabela/coluna/medida que existe no TMDL, com a mesma grafia, incluindo acentos e maiúsculas.
4. Toda coluna do TMDL sai do M com o mesmo nome (`sourceColumn`) e o mesmo tipo.
5. Os relacionamentos ligam colunas de tipos iguais. Fato → dimensão.
6. `dCalendario` tem `dataCategory: Time` e `Data` com `isKey`. O `sortByColumn` aponta para uma coluna existente.
7. TMDL: TAB na indentação, nomes com espaço entre aspas simples, `formatString` em toda medida, sem `lineageTag` inventado.
8. O tema foi copiado sem alterações. Os três nomes em `report.json` são iguais ao nome do arquivo.
9. Nenhum segredo: só IDs de workspace/dataflow, sem host, usuário, senha ou connection string.

## 9. Checklist para o usuário (entregar sempre)

1. Abrir `<nome>.pbip` no Power BI Desktop.
2. No 1º **Atualizar**, em credenciais de *Dataflows*, escolher **Conta organizacional** e entrar com a conta dele.
3. Clicar em **Atualizar** e aguardar todas as tabelas.
4. Conferir:
   - a exibição de modelo (relacionamentos e tabela de datas marcada);
   - os valores contra um relatório conhecido;
   - o tema em Exibição → Temas.
5. Salvar (Ctrl+S). O Desktop completa `lineageTag` e outros metadados, então é normal ver arquivos alterados.
6. **Publicar** → workspace **Dominio FLOWS**. No serviço, configurar a credencial OAuth2 do dataset e a atualização agendada, depois do refresh do dataflow de origem.

---

## 10. Limitações e riscos conhecidos

- **A IA não abre o Power BI Desktop.** A estrutura foi conferida contra PBIP reais salvos pelo Desktop do time e os JSON do exemplo `metas-teste` passam nos schemas públicos da Microsoft. Mesmo assim, a renderização, o parse do TMDL e o refresh só se confirmam quando o usuário abre o projeto.
- **Visuais com maior risco:** `cardVisual` (novo cartão), `kpi`, formatação condicional por medida (`cor_condicional`) e cores por série (`dataPoint`). Os nomes das propriedades de formatação não são validados pelo schema (objetos livres). Prefira herdar do tema.
- **Fora do gerador** (fazer no Desktop ou à mão, com mais risco):
  - visuais custom/AppSource (GUID não pode ser adivinhado);
  - bookmarks;
  - drillthrough;
  - botões e navegação;
  - field parameters;
  - RLS;
  - calculation groups;
  - Direct Lake;
  - fontes que não sejam Dataflow (SQL/Postgres direto etc.).
  Ver `powerbi-relatorios.md` §4.3–§4.8.
- **Uma fonte só:** Dataflows do Dominio FLOWS via `PowerPlatform.Dataflows`. O tipo das colunas vem do `model.json`. Se o dataflow mudar, rode `/sincronizar-dados` e gere de novo.
- **DataflowId:** vem de `.dados-sync/powerbi-servico.json` (inventário com login). Dataflow recriado muda de id: sincronize de novo.
- **Premissas de negócio:** medidas marcadas **[Em revisão]** dependem de validação do time (ex.: grão de `DB_METAS.goals`, a meta mensal repetida por dia).
- **Base theme:** se o Desktop não estiver instalado no caminho padrão, o relatório sai só com o custom theme (aviso do gerador).
- **Regerar sobrescreve** a pasta do projeto (`--forcar`) e perde as alterações feitas no Desktop. Regere antes de editar no Desktop, ou mude o nome.
