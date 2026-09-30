# Padrões DAX (medidas, consultas e performance)
> Última atualização: 2026-09-29 · Fonte: microsoft/skills-for-fabric v0.3.18 + Microsoft Learn · Links: https://github.com/microsoft/skills-for-fabric/tree/main/skills/semantic-model-authoring/references · https://github.com/microsoft/skills-for-fabric/tree/main/skills/fabriciq · https://learn.microsoft.com/en-us/dax/best-practices/dax-variables · https://learn.microsoft.com/en-us/dax/best-practices/dax-avoid-avoid-filter-as-filter-argument · https://learn.microsoft.com/en-us/dax/

Origem das regras:
- **[upstream]**: `semantic-model-authoring/references/dax-guidelines.md`, `dax-perf-decision-guide.md`, `dax-perf-patterns.md`, `modeling-guidelines.md` e a skill `fabriciq` (regras de consulta DAX).
- **[Learn]**: DAX best practices do Microsoft Learn.
- **[prática]**: padrões DAX consolidados, sem atribuição ao upstream.

> A skill `semantic-model-consumption` **não existe** na v0.3.18 (404). As regras de consulta DAX (EVALUATE, SUMMARIZECOLUMNS, DEFINE MEASURE) vêm do `dax-guidelines.md` e da skill `fabriciq`, que é quem executa DAX para responder perguntas.

Convenção dos exemplos: tabelas `Sales` (fato), `Product`, `Customer`, `Date` (dimensões), medida base `[Total Sales]`.

---

## 1. Medida vs. coluna calculada

| | Medida | Coluna calculada |
|---|---|---|
| Quando é calculada | Na consulta, respeitando o contexto de filtro | No refresh, linha a linha (fica armazenada) |
| Custo | CPU na consulta | Memória + tempo de refresh |
| Usar para | Agregações, razões, KPIs, time intelligence | Atributo fixo por linha para filtrar/agrupar/ordenar, quando não dá para fazer na origem |
| Depende de filtros/slicers? | Sim | Não |

Regras [upstream]:
- Medidas **explícitas** para todo numérico agregável. Oculte a coluna base e dê à medida um nome diferente.
- `formatString` em **toda** medida visível, mais descrição e `displayFolder`.
- Não defina `dataType` em medidas. Evite expressões duplicadas e medidas que apenas referenciam outra medida.
- Colunas calculadas com moderação. Prefira empurrar a lógica para a origem (Power Query/SQL). Não use colunas calculadas para agregação ou para valores dependentes de filtro.
- Referências: coluna **sempre qualificada** `'Tabela'[Coluna]`; medida **sem** prefixo de tabela `[Medida]`.

```dax
-- Medidas base
Total Sales   = SUM ( Sales[Sales Amount] )
Total Cost    = SUM ( Sales[Total Cost] )
# Orders      = DISTINCTCOUNT ( Sales[Order Number] )
# Customers   = DISTINCTCOUNT ( Sales[Customer Key] )

-- Coluna calculada (só se não der para fazer na origem)
-- Em Product:
Price Band =
SWITCH (
    TRUE (),
    Product[List Price] < 100, "Low",
    Product[List Price] < 1000, "Medium",
    "High"
)
```

---

## 2. Contexto de filtro, contexto de linha e transição de contexto [prática]

- **Contexto de filtro**: filtros ativos (linhas/colunas do visual, slicers, filtros de página/relatório, RLS). Toda medida é avaliada nele.
- **Contexto de linha**: existe em colunas calculadas e dentro de iteradores (`SUMX`, `FILTER`, `ADDCOLUMNS`...). Ele **não filtra** nada sozinho.
- **Transição de contexto**: `CALCULATE` (e toda referência a medida, que tem um `CALCULATE` implícito) converte o contexto de linha atual em contexto de filtro equivalente.

```dax
-- Sem transição: soma a coluna inteira da tabela filtrada, em toda linha
Col Errada = SUM ( Sales[Sales Amount] )          -- como coluna calculada em Customer: total geral

-- Com transição: filtra Sales pelo cliente da linha atual
Customer Sales = CALCULATE ( SUM ( Sales[Sales Amount] ) )   -- coluna calculada em Customer
-- ou equivalente:
Customer Sales = [Total Sales]
```

Cuidado: transição dentro de iterador sobre tabela grande é cara (ver DAX008/DAX015 na seção 12).

---

## 3. CALCULATE e argumentos de filtro

### 3.1 Predicados de coluna, não FILTER na tabela inteira [Learn + upstream]
```dax
-- Evitar: FILTER itera a tabela Product inteira e substitui filtros
Red Sales =
CALCULATE ( [Total Sales], FILTER ( 'Product', 'Product'[Color] = "Red" ) )

-- Preferir: predicado booleano; KEEPFILTERS preserva filtros existentes em Color
Red Sales =
CALCULATE ( [Total Sales], KEEPFILTERS ( 'Product'[Color] = "Red" ) )
```

Predicados combinados com `&&` → separe em argumentos (DAX001) [upstream]:
```dax
-- Evitar
CALCULATE ( [Total Sales], Sales[Region] = "West" && Sales[Amount] > 1000 )
-- Preferir
CALCULATE ( [Total Sales], Sales[Region] = "West", Sales[Amount] > 1000 )
```

Restrições dos filtros booleanos em `CALCULATE`/`CALCULATETABLE` [Learn + upstream]:
- **Não** podem referenciar medida nem conter `CALCULATE` aninhado. Guarde o valor numa variável antes.
- **Não** podem referenciar colunas de duas tabelas diferentes.
- Não podem usar funções que varrem/retornam tabela. Com `IN`, o operando tabela deve ser uma **variável de tabela**.
- Nunca atribua um filtro booleano a uma `VAR`.

Quando `FILTER` é necessário (medida, comparação entre colunas, OR entre colunas) [Learn]:
```dax
Sales for Profitable Months =
CALCULATE (
    [Total Sales],
    FILTER ( VALUES ( 'Date'[Month] ), [Profit] > 0 )
)
```

Medida no limite → variável [upstream]:
```dax
Sales Above Median Price =
VAR _Median = [Median List Price]
RETURN
    CALCULATE ( [Total Sales], 'Product'[List Price] > _Median )
```

### 3.2 ALL, ALLEXCEPT, REMOVEFILTERS, KEEPFILTERS, ALLSELECTED [prática + upstream]
| Função | Efeito | Uso típico |
|---|---|---|
| `REMOVEFILTERS ( T / T[c] )` | Remove filtros (modificador de `CALCULATE`) | Denominador de % do total. **Prefira a `ALL` como modificador** [upstream], porque a intenção fica mais clara |
| `ALL ( T / T[c] )` | Remove filtros; também retorna tabela sem filtros | Como tabela: `COUNTROWS ( ALL ( Product ) )` |
| `ALLEXCEPT ( T, T[c1] )` | Remove todos os filtros de T exceto os das colunas listadas | Só quando a coluna preservada é filtrada diretamente; senão use `REMOVEFILTERS(T), VALUES(T[c])` (DAX012) [upstream] |
| `ALLSELECTED ( T[c] )` | Volta aos filtros "externos" do visual (slicers) | % do total visível |
| `KEEPFILTERS ( expr )` | Faz o filtro **interseccionar** o existente em vez de substituí-lo | Filtros fixos que devem respeitar slicers |

```dax
% of Total Sales =
VAR _Atual = [Total Sales]
VAR _Total = CALCULATE ( [Total Sales], REMOVEFILTERS ( 'Product' ) )
RETURN DIVIDE ( _Atual, _Total )

% of Visible Total =
DIVIDE ( [Total Sales], CALCULATE ( [Total Sales], ALLSELECTED ( 'Product'[Category] ) ) )

% of Category (dentro da categoria) =
VAR _Cat = CALCULATE ( [Total Sales], REMOVEFILTERS ( 'Product' ), VALUES ( 'Product'[Category] ) )
RETURN DIVIDE ( [Total Sales], _Cat )
```

---

## 4. Variáveis [Learn + upstream]

Benefícios [Learn]: **performance** (expressão avaliada uma vez), **legibilidade**, **depuração** e **menos complexidade** (substitui `EARLIER`/`EARLIEST`). As variáveis são avaliadas **fora** dos filtros que o `RETURN` aplica.

Regras [upstream]: nomes descritivos com prefixo `_` para evitar colisão; divida lógica complexa em passos `VAR`; evite `CALCULATE` profundamente aninhado.

```dax
-- Antes (Learn): mesma expressão avaliada duas vezes
Sales YoY Growth % =
DIVIDE (
    [Sales] - CALCULATE ( [Sales], PARALLELPERIOD ( 'Date'[Date], -12, MONTH ) ),
    CALCULATE ( [Sales], PARALLELPERIOD ( 'Date'[Date], -12, MONTH ) )
)

-- Depois: cerca de metade do tempo de consulta
Sales YoY Growth % =
VAR _SalesPriorYear =
    CALCULATE ( [Sales], PARALLELPERIOD ( 'Date'[Date], -12, MONTH ) )
RETURN
    DIVIDE ( [Sales] - _SalesPriorYear, _SalesPriorYear )

-- Depuração: retorne a variável temporariamente
RETURN
    -- DIVIDE ( [Sales] - _SalesPriorYear, _SalesPriorYear )
    _SalesPriorYear
```

Substituindo `EARLIER` [Learn]:
```dax
Subcategory Sales Rank =
VAR _CurrentSales = Subcategory[Subcategory Sales]
RETURN
    COUNTROWS ( FILTER ( Subcategory, _CurrentSales < Subcategory[Subcategory Sales] ) ) + 1
```

---

## 5. DIVIDE e tratamento de erros [upstream + Learn]
- Use `DIVIDE()` por padrão: retorna BLANK (ou o 3º argumento) na divisão por zero.
- **Dentro de iteradores**, `/` é aceitável (e mais rápido, porque fica nativo no Storage Engine) se o denominador nunca for zero ou se as linhas com zero forem filtradas antes (DAX018).
- Não escreva `1-(x/y)` ou `1+(x/y)`. Guarde o denominador numa variável e passe o numerador completo ao `DIVIDE`.
- `IFERROR` fora de iteradores (força callbacks). Prefira `DIVIDE`, lógica condicional ou `COALESCE`.
- `EVALUATEANDLOG` só para debug, nunca em produção.

```dax
-- Evitar
Margin % = 1 - ( [Total Cost] / [Total Sales] )

-- Preferir
Margin % =
VAR _Revenue = [Total Sales]
RETURN DIVIDE ( _Revenue - [Total Cost], _Revenue )
```

---

## 6. Time intelligence

Pré-requisitos: tabela de datas contínua, marcada como date table, relacionada ao fato (ver `powerbi-modelagem.md`). Regra [upstream/fabriciq]: sempre estabeleça **contexto de data válido** e evite `MAX('Calendar'[Date])` solto como âncora.

```dax
Sales YTD = TOTALYTD ( [Total Sales], 'Date'[Date] )
-- equivalente
Sales YTD = CALCULATE ( [Total Sales], DATESYTD ( 'Date'[Date] ) )

-- Ano fiscal terminando em 30/06
Sales FYTD = CALCULATE ( [Total Sales], DATESYTD ( 'Date'[Date], "06-30" ) )

Sales MTD = CALCULATE ( [Total Sales], DATESMTD ( 'Date'[Date] ) )
Sales QTD = CALCULATE ( [Total Sales], DATESQTD ( 'Date'[Date] ) )

Sales (ly) = CALCULATE ( [Total Sales], SAMEPERIODLASTYEAR ( 'Date'[Date] ) )
Sales (ly) = CALCULATE ( [Total Sales], DATEADD ( 'Date'[Date], -1, YEAR ) )   -- alternativa
Sales PM   = CALCULATE ( [Total Sales], DATEADD ( 'Date'[Date], -1, MONTH ) )

Sales YTD (ly) =
CALCULATE ( [Total Sales], DATESYTD ( SAMEPERIODLASTYEAR ( 'Date'[Date] ) ) )

Sales YoY % =
VAR _Atual = [Total Sales]
VAR _LY    = [Sales (ly)]
RETURN IF ( NOT ISBLANK ( _Atual ) && NOT ISBLANK ( _LY ), DIVIDE ( _Atual - _LY, _LY ) )

-- Média móvel 3 meses: offset de DATESINPERIOD = tamanho da janela [upstream]
Sales 3M Avg =
VAR _Janela = DATESINPERIOD ( 'Date'[Date], MAX ( 'Date'[Date] ), -3, MONTH )
RETURN DIVIDE ( CALCULATE ( [Total Sales], _Janela ), 3 )

-- Rolling 12 meses
Sales R12M =
CALCULATE ( [Total Sales], DATESINPERIOD ( 'Date'[Date], MAX ( 'Date'[Date] ), -12, MONTH ) )
```

Evitar datas futuras vazias na tabela de datas [prática]:
```dax
Sales YTD (até último dado) =
VAR _UltimaVenda = CALCULATE ( MAX ( Sales[Order Date] ), REMOVEFILTERS ( 'Date' ) )
RETURN
    IF ( MIN ( 'Date'[Date] ) <= _UltimaVenda, [Sales YTD] )
```

No visual KPI: se o Indicator fica BLANK no último ponto da tendência (data futura), use `LASTNONBLANK` dentro de `CALCULATE` ou `COALESCE([Metric], 0)`. Meta em grão mais grosso: `CALCULATE([Annual Target], ALL('Date'[Month]))` [upstream, powerbi-report-cli/kpi.md].

Performance [upstream]: YTD aplicado **em cada** medida irmã impede fusão. Aplique a janela uma vez (DAX019/DAX020):
```dax
-- Evitar: [Revenue YTD] - [Cost YTD], cada uma com DATESYTD
-- Preferir
Profit YTD = CALCULATE ( [Revenue] - [Cost], DATESYTD ( 'Date'[Date] ) )
```

Para muitas variações de tempo, use **calculation groups** (ver `powerbi-modelagem.md` §8). Em DirectQuery, cuidado com time intelligence [upstream].

---

## 7. Iteradores (SUMX, AVERAGEX, MAXX, RANKX...)

```dax
-- Receita linha a linha (sem coluna calculada)
Sales Amount (calc) = SUMX ( Sales, Sales[Quantity] * Sales[Unit Price] )

-- Média por cliente
Avg Sales per Customer = AVERAGEX ( VALUES ( Customer[Customer Key] ), [Total Sales] )

-- Ranking
Product Rank =
IF (
    HASONEVALUE ( 'Product'[Product] ),
    RANKX ( ALLSELECTED ( 'Product'[Product] ), [Total Sales], , DESC, DENSE )
)
```

Regras de performance [upstream]:
- **DAX008:** evite transição de contexto no iterador quando der: itere `'Sales'[Unit Price] * 'Sales'[Quantity]` em vez de chamar `[Sales Amount]`. Reduza a tabela iterada (`VALUES('Customer'[CustomerKey])` em vez de `'Customer'`).
- **DAX015:** itere no grão necessário: `SUMX(VALUES('Customer'[DiscountRate]), ...)` (~5 iterações) em vez de `SUMX('Customer', ...)` (100 mil transições), desde que o resultado seja igual.
- **DAX003:** medida que não varia por linha → variável fora do iterador.
  ```dax
  VAR _AvgPrice = [Average Price]
  RETURN SUMX ( Sales, Sales[Quantity] * _AvgPrice * 1.1 )
  ```
- **DAX006:** pré-calcule a entrada do iterador:
  ```dax
  -- Evitar
  SUMX ( VALUES ( 'Product'[Attribute] ), CALCULATE ( SUM ( Sales[Amount] ) ) )
  -- Preferir
  SUMX ( SUMMARIZECOLUMNS ( 'Product'[Attribute], "@Amount", SUM ( Sales[Amount] ) ), [@Amount] )
  ```
- **DAX007:** booleano sem `IF`: `INT([Sales Amount] > 10000000)`; contagem condicional com `CALCULATE(COUNTROWS(Sales), Sales[Amount] > 1000)` em vez de `SUMX(Sales, IF(...,1,0))`.
- `IF`/`DIVIDE`/`IFERROR` dentro de iterador geram **callbacks** (ver §12).

---

## 8. TREATAS, relacionamentos virtuais e USERELATIONSHIP

- Prefira `TREATAS` a `INTERSECT` para relacionamento virtual [upstream].
- Na skill `fabriciq`, filtros positivos `IN` de relatório/Verified Answer são traduzidos com `TREATAS`, e outras condições com `KEEPFILTERS(FILTER(ALL(...)))`, **cada filtro como argumento separado**. Nunca junte filtros de várias colunas num `FILTER` de tabela, porque isso distorce os totais [upstream].

```dax
-- Metas por Categoria/Mês sem relacionamento físico com Product
Target Amount =
CALCULATE (
    SUM ( Targets[Target] ),
    TREATAS ( VALUES ( 'Product'[Category] ), Targets[Category] ),
    TREATAS ( VALUES ( 'Date'[Year Month] ), Targets[Year Month] )
)

-- Filtro de lista fixa
Sales Red or Black =
CALCULATE ( [Total Sales], TREATAS ( { "Red", "Black" }, 'Product'[Color] ) )

-- Relacionamento inativo (role-playing)
Sales by Ship Date =
CALCULATE ( [Total Sales], USERELATIONSHIP ( Sales[Ship Date Key], 'Date'[Date Key] ) )

-- Trocar ponte bidirecional por filtro local (DAX016) [upstream]
Sales via Bridge =
CALCULATE (
    [Total Sales],
    CROSSFILTER ( CustomerBridge[CustomerKey], Customer[CustomerKey], NONE ),
    TREATAS ( VALUES ( CustomerBridge[CustomerKey] ), Customer[CustomerKey] )
)
```
Regra [upstream]: não use `USERELATIONSHIP` em tabelas com RLS. Chaves grandes em `IN`/`TREATAS` são um sinal de custo (DAX021).

---

## 9. SELECTEDVALUE, HASONEVALUE, ISINSCOPE e SWITCH [prática]

```dax
Selected Category = SELECTEDVALUE ( 'Product'[Category], "Várias categorias" )

-- Título dinâmico
Chart Title =
"Vendas – " & SELECTEDVALUE ( 'Date'[Year], "Todos os anos" )

-- Seletor de métrica via tabela desconectada (quando NÃO for field parameter)
Selected Metric =
SWITCH (
    SELECTEDVALUE ( 'Metric'[Metric] ),
    "Vendas", [Total Sales],
    "Margem", [Margin %],
    [Total Sales]
)

-- Comportamento diferente no subtotal da matriz
Sales (sem total de produto) =
IF ( ISINSCOPE ( 'Product'[Product] ), [Total Sales] )
```
Performance [upstream, DAX013]: medidas com `SWITCH`/`IF` entre medidas devem ler a coluna seletora **filtrada diretamente**, ter uma agregação simples por ramo e tipo numérico consistente. Mova medidas que não variam por linha para variáveis. Ramificação escolhida pelo Formula Engine quebra a fusão. Se o pedido for field parameter, **não** substitua por `SWITCH` silenciosamente.

---

## 10. Formatação

`formatString` de referência [upstream]:
| Tipo | Format string |
|---|---|
| Moeda | `$#,##0.00` (ajuste o símbolo, ex.: `"R$" #,##0.00`, conforme `regras-formato.md`) |
| Percentual | `0.00%` |
| Inteiro | `#,##0` |
| Decimal | `#,##0.00` |
| Milhares | `#,##0,K` |
| Milhões | `#,##0,,M` |
| Sem decimais | `0` |
| Uma casa | `#,##0.0` |

- Em calculation groups, use `formatStringDefinition` [upstream].
- Formato dinâmico por medida (dynamic format strings) é recurso do Power BI [prática]. Prefira isso a `FORMAT()` na medida, porque `FORMAT` devolve **texto** (quebra ordenação, eixos e agregação).
- No relatório, exiba taxas decimais como percentual (`0%`/`0.0%`) [upstream, design].

```dax
-- Evitar: retorna texto
Sales Text = FORMAT ( [Total Sales], "#,##0" )

-- Texto só quando o destino é texto (título, alt text dinâmico)
Alt Text Sales =
"Receita de " & FORMAT ( [Total Sales] / 1e6, "#,##0.0" ) & " mi, "
    & FORMAT ( [Sales YoY %], "+0.0%;-0.0%" ) & " vs ano anterior"
```
Alt text dinâmico: até 300 caracteres, com valor-chave, contexto e direção [upstream, accessibility.md].

---

## 11. Consultas DAX (EVALUATE, DEFINE, SUMMARIZECOLUMNS)

### 11.1 Regras de sintaxe [upstream: dax-guidelines + fabriciq]
- **Um `EVALUATE` por consulta** (fabriciq), com **`ORDER BY`** quando retornar várias linhas. Não use a função `ORDERBY` para ordenar a saída final.
- **Um único bloco `DEFINE`**, necessário quando há `VAR`, `MEASURE`, `COLUMN` ou `TABLE`. Uma definição por linha, sem vírgula/ponto e vírgula.
- `MEASURE` definida com **tabela hospedeira existente**: `MEASURE 'Sales'[X] = ...`. Ao usar, referencie só `[X]`.
- **`SUMMARIZECOLUMNS`**: ordem **group-by → filtros → medidas**. É o padrão para tabelas-resumo com medidas; deve ter medida; **sem filtros booleanos**; descarta linhas em que todas as medidas são BLANK.
- **`SUMMARIZE`**: só para combinações distintas de colunas, **nunca com medidas**. De variável de tabela: `SUMMARIZE(_Var, [Col])` (`_Var[Col]` é inválido).
- **`GROUPBY`**: primeiro argumento deve ser variável de tabela. `CURRENTGROUP()` só dentro dele.
- **`SELECTCOLUMNS`**: para manter duplicatas ou renomear. Passos seguintes (TOPN, ORDER BY) usam os **novos nomes**.
- `INTERSECT`/`UNION`/`EXCEPT`: mesmo número de colunas.
- Com `ROW`, aplique filtros externos via `CALCULATETABLE`.
- Rankings com `TOPN`, limitados a 50 por padrão (fabriciq).
- fabriciq: não suporta funções `INFO`, DMVs nem MDX. Medidas que existem só no relatório precisam ser **redefinidas inline** (referência por nome falha). Subtotais com várias dimensões: `ROLLUPADDISSUBTOTAL`.

### 11.2 Exemplos
```dax
-- Testar uma medida (checklist de validação do upstream)
EVALUATE { [Total Sales] }

-- Resumo por ano e categoria com medida definida na consulta
DEFINE
    MEASURE Sales[Margin % (q)] =
        VAR _Rev = [Total Sales]
        RETURN DIVIDE ( _Rev - [Total Cost], _Rev )
EVALUATE
SUMMARIZECOLUMNS (
    'Date'[Year],
    'Product'[Category],
    TREATAS ( { "Red", "Black" }, 'Product'[Color] ),     -- filtro (tabela, não booleano)
    "Total Sales", [Total Sales],
    "Margin %", [Margin % (q)]
)
ORDER BY 'Date'[Year], 'Product'[Category]

-- Filtro guardado em variável e passado ao SUMMARIZECOLUMNS
DEFINE
    VAR _Cores = TREATAS ( { "Red", "Black" }, 'Product'[Color] )
EVALUATE
VAR _T =
    SUMMARIZECOLUMNS ( 'Product'[Product], _Cores, "Sales", [Total Sales] )
RETURN
    SELECTCOLUMNS ( FILTER ( _T, [Sales] > 1000000 ), "Produto", 'Product'[Product], "Vendas", [Sales] )
ORDER BY [Produto]

-- Top 10 produtos
EVALUATE
TOPN (
    10,
    SUMMARIZECOLUMNS ( 'Product'[Product], "Sales", [Total Sales] ),
    [Sales], DESC
)
ORDER BY [Sales] DESC

-- Estatística mensal agregada por ano (GROUPBY + CURRENTGROUP)
DEFINE
    VAR _Mensal =
        SUMMARIZECOLUMNS ( 'Date'[Year], 'Date'[Month Number], "Qty", SUM ( Sales[Quantity] ) )
EVALUATE
GROUPBY (
    _Mensal,
    'Date'[Year],
    "Avg Qty", AVERAGEX ( CURRENTGROUP (), [Qty] ),
    "Min Qty", MINX ( CURRENTGROUP (), [Qty] ),
    "Max Qty", MAXX ( CURRENTGROUP (), [Qty] )
)
ORDER BY 'Date'[Year]

-- YTD + média móvel 14 dias numa linha, com contexto de data explícito
DEFINE
    VAR _UltimaData = CALCULATETABLE ( { MAX ( Sales[Order Date] ) }, REMOVEFILTERS () )
EVALUATE
CALCULATETABLE (
    ROW (
        "Sales YTD", TOTALYTD ( [Total Sales], 'Date'[Date] ),
        "Avg 14d", AVERAGEX ( DATESINPERIOD ( 'Date'[Date], MAX ( 'Date'[Date] ), -14, DAY ), [Total Sales] )
    ),
    TREATAS ( _UltimaData, 'Date'[Date] ),
    'Product'[Color] = "Red"
)

-- Filtros de relatório não-IN (padrão fabriciq): cada coluna em seu próprio argumento
EVALUATE
SUMMARIZECOLUMNS (
    'Customer'[Region],
    KEEPFILTERS ( FILTER ( ALL ( 'Date'[Year] ), 'Date'[Year] >= 2024 ) ),
    KEEPFILTERS ( FILTER ( ALL ( 'Product'[Category] ), 'Product'[Category] <> "Services" ) ),
    "Sales", [Total Sales]
)
ORDER BY [Sales] DESC
```

### 11.3 Onde rodar [upstream]
- MCP `dax_query_operations` (inclui usuários só com Build).
- REST `POST https://api.powerbi.com/v1.0/myorg/groups/{wsId}/datasets/{id}/executeQueries`: 1 query por requisição, até 100k linhas / 1M valores / 15 MB, 120 req/min, `impersonatedUserName` para testar RLS.
- fabriciq `ExecuteQuery`: 1–4 queries, 250 linhas por padrão (máx. 1.000).
- `INFO.VIEW.*` para metadados (ver `powerbi-modelagem.md` §15).

---

## 12. Performance: VertiPaq, Formula Engine e Storage Engine [upstream]

### 12.1 Motor
- **Formula Engine (FE)**: executa toda a lógica DAX, é **single-thread** e costuma ser o gargalo.
- **Storage Engine (SE / VertiPaq)**: multi-thread; só faz aritmética básica, GROUP BY, left outer join, SUM/COUNT/MIN/MAX/DISTINCTCOUNT.
- **Callback** (`CallbackDataID`/`EncodeCallback`): o SE não consegue avaliar a expressão e chama o FE linha a linha. O scan vira praticamente single-thread.
- Princípio: **empurre o máximo para o SE, minimize scans e elimine callbacks.**
- **Fusão**: vertical (agregações com o mesmo filtro) e horizontal (scans que só diferem no valor de filtro). Quebra com: SWITCH/IF entre medidas, filtros de tempo em tabela/intervalo, coluna de fatiamento fora do group-by, valor de filtro em variável, itens de calculation group com filtros.
- Um thread por **segmento**: poucos segmentos ou segmentos desbalanceados limitam o paralelismo.

### 12.2 Cardinalidade e modelo [upstream + prática]
- Tamanho e velocidade no VertiPaq dependem sobretudo da **cardinalidade** das colunas (valores distintos) [prática].
- Chaves `Int64`, DateTime dividido em Date + Time, decimais "binados", colunas de alta cardinalidade divididas (MDL003).
- Evite `Double`. Remova colunas sem uso (GUIDs, IDs de transação).
- Colunas pré-calculadas de período (`SalesLY`) e tabela de time intelligence em linhas (MDL005/MDL006) são mudanças de modelo que exigem aprovação.

### 12.3 Fluxo de otimização (níveis de esforço)
| Nível | O que muda | Autonomia |
|---|---|---|
| 1 – DAX (DAX001–021) | Só medidas/UDFs no `DEFINE` | Automático, mantendo `EVALUATE` e grão iguais; resultado deve ser **semanticamente equivalente** |
| 2 – Consulta (QRY001–004) | EVALUATE, grão, filtros | Recomendar e esperar aprovação |
| 3 – Modelo (MDL001–009) | Relacionamentos, colunas, agregações, tipos | Alta cautela, de preferência numa cópia do modelo |
| 4 – Direct Lake (DL001–002) | Layout OneLake, V-Order, row groups | Exige ETL/Spark |

Baseline: inlinar recursivamente as medidas (inclusive UDFs e calculation groups) no `DEFINE` → 1 aquecimento + ≥ 2 execuções medidas limpando o cache do SE → usar a mais rápida se a variação for < ~20%. Melhoria = (baseline − otimizado) / baseline. Ganho dentro do ruído não conta. Resultado diferente → reverter.

Leitura do trace: muitas queries curtas de SE com FE alto = **problema de DAX**. Poucas queries de SE, FE baixo, SE lento e paralelismo baixo = **problema de layout de dados** (DAX não resolve). Gaps > 100 ms entre eventos de SE merecem análise.

### 12.4 Tabela de sinais → padrões
| Sinal no trace | Tentar |
|---|---|
| Callbacks / IF-DIVIDE em iteradores | DAX002, 007, 008, 018 |
| FE alto / expressões repetidas | DAX003, 006, 015 |
| Linhas no SE ≫ linhas do resultado; FILTER(Tabela) como filtro | DAX001, 005, 009, 010 |
| Scans repetidos do mesmo fato (medidas irmãs/janelas) | DAX019, 020, 013 |
| Scans que só diferem no valor de filtro | DAX017 |
| Conjuntos grandes em IN/TREATAS | DAX021 |
| DCOUNT no xmSQL | DAX011, 014 |
| ALLEXCEPT / filtros duplicados | DAX012, 004 |
| Bidirecional / M:N | DAX016 (e MDL001) |
| `__ValueFilterDM` na query gerada | QRY002 |

Exemplos:
```dax
-- DAX002: SUMMARIZECOLUMNS em vez de ADDCOLUMNS(SUMMARIZE(...), medida)
SUMMARIZECOLUMNS ( Sales[ProductKey], "Total Profit", [Profit] )

-- DAX010: CALCULATETABLE em vez de FILTER na tabela
CALCULATETABLE ( Sales, Sales[Year] = 2023 )

-- DAX011: testar alternativa (manter só se equivalente e mais rápida)
SUMX ( DISTINCT ( Sales[CustomerKey] ), 1 )    -- vs DISTINCTCOUNT ( Sales[CustomerKey] )

-- QRY002: limiar dentro da medida em vez de filtro de valor no visual
Revenue > 1M =
VAR __Rev = [Total Revenue]
RETURN IF ( __Rev > 1000000, __Rev )

-- QRY004: não force zeros com "+ 0" (destrói a supressão de BLANK)
-- Se zeros forem realmente necessários:
Sales With Zero = SUM ( Sales[SalesAmount] ) + IF ( NOT ISEMPTY ( Sales ), 0 )
```

---

## 13. DAX User-Defined Functions (UDFs) [upstream]
Ficam em `definition/functions.tmdl`. Sintaxe `function Nome = (params) => corpo`; use três crases se for multilinha.
- Tipos: `AnyVal` (padrão), `Scalar`, `Table`, `AnyRef`, `MeasureRef`, `ColumnRef`, `TableRef`, `CalendarRef`.
- Subtipos escalares: `Int64`, `Decimal`, `Double`, `String`, `DateTime`, `Boolean`, `Numeric`, `Variant`.
- Modos: `Val` (padrão, avalia uma vez) e `Expr` (reavalia em contextos internos como CALCULATE/iteradores). Use `Expr` só quando necessário.
- Declare os tipos, mantenha uma função por propósito, use VARs e trate BLANK/tabela vazia.

```tmdl
function PriorYear =
		```
		( _expr : Scalar Expr, _dateCol : AnyRef ) =>
		CALCULATE ( _expr, SAMEPERIODLASTYEAR ( _dateCol ) )
		```
```
(Assinatura ilustrativa, baseada na descrição do upstream. Confirme a sintaxe exata no seu build antes de usar.)

---

## 14. Anti-patterns (resumo)
| Anti-pattern | Por quê | Correção |
|---|---|---|
| `FILTER(Tabela, cond)` em CALCULATE | Itera a tabela inteira e substitui filtros | Predicado de coluna + `KEEPFILTERS` |
| `cond1 && cond2` num único filtro | Menos eficiente | Argumentos separados |
| Mesma sub-expressão repetida | Avalia várias vezes | `VAR` |
| `/` sem proteção fora de iterador | Erro/infinito | `DIVIDE` |
| `IFERROR` em iterador | Callback | `DIVIDE`/`IF`/`COALESCE` |
| `1 - x/y` | Legibilidade/precisão | `DIVIDE(num - den, den)` |
| `ALL` para remover filtro | Intenção pouco clara | `REMOVEFILTERS` |
| `INTERSECT` para relacionamento virtual | Mais lento | `TREATAS` |
| `SUMMARIZE` com medidas | Resultados/perf ruins | `SUMMARIZECOLUMNS` |
| Coluna calculada para agregação | Memória e refresh | Medida |
| `FORMAT()` em medida numérica | Vira texto | `formatString` / dynamic format string |
| Medida sem `formatString` | Viola regra do upstream | Definir formato |
| `+ 0` para mostrar zeros | Explode o grão da consulta | Remover ou `IF(NOT ISEMPTY(T), 0)` |
| `MAX('Date'[Date])` como âncora solta | Pega datas futuras | Âncora na última data com fato |
| Medida que só referencia outra | Redundância | Remover |
| `EVALUATEANDLOG` em produção | Debug | Remover |
| `USERELATIONSHIP` com RLS | Proibido pelo upstream | Tabela por papel |
