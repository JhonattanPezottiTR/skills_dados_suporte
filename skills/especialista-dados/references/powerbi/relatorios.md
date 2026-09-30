# Relatórios Power BI (PBIR/PBIP, design e temas)
> Última atualização: 2026-09-29 · Fonte: microsoft/skills-for-fabric v0.3.18 + Microsoft Learn · Links: https://github.com/microsoft/skills-for-fabric/tree/main/skills/powerbi-report-cli · https://raw.githubusercontent.com/microsoft/skills-for-fabric/main/CHANGELOG.md · https://learn.microsoft.com/en-us/power-bi/developer/agentic/power-bi-report-authoring-skill-overview · https://learn.microsoft.com/en-us/power-bi/create-reports/desktop-report-themes

Origem das regras:
- **[upstream]**: skill `powerbi-report-cli` v0.3.18 (`SKILL.md`, `references/planning.md`, `design.md`, `authoring*.md`, `management*.md`, `references/authoring/*.md`, `references/design/*.md`).
- **[Learn]**: Microsoft Learn.
- **[prática]**: prática geral, sem atribuição ao upstream.

> **Tema do time:** o tema oficial obrigatório está em `powerbi-tema-cores.md` / `tema-oficial-powerbi.json` (regra COR-001). O JSON de tema da seção 8 é só para explicar a estrutura. Não o use no lugar do oficial.

---

## 1. Histórico recente (CHANGELOG)
- **0.3.17 (2026-09-17):** nasce **`powerbi-report-cli`**, "one Power BI report skill covering the whole report item". Ela substitui e **renomeia** `powerbi-report-authoring`, `powerbi-report-design`, `powerbi-report-management` e `powerbi-report-planning`, que foram removidas. O bundle `powerbi-authoring` passa a entregar só essa skill, e os prompts antigos continuam funcionando. Quem fixava os nomes antigos deve migrar.
- **0.3.18 (2026-09-24):** novos guias de **drillthrough no mesmo relatório, bookmarks, buttons/actions, custom visuals, field parameters, KPI, model binding e preview** (Desktop ou serviço). Planning/design/authoring/validação/screenshot review/publicação foram reforçados. O roteamento de preview ficou mais seguro, os checks de model binding rodam **antes de publicar**, e o trabalho normal no Desktop passa por `powerbi-report-author preview`. Há orientação de reload "model-aware" (processar o modelo, verificar DAX e revisar a renderização).
- **0.3.16:** sem mudanças específicas de Power BI.
- Obs.: a página do Microsoft Learn (atualizada em 2026-09-17) ainda descreve as skills separadas (Report Authoring, Design, Planner, Management) e está em **preview**. O conteúdo equivale aos modos da nova skill.

---

## 2. O que a `powerbi-report-cli` cobre [upstream]
Ela funciona como **dispatcher de modos**. Escolha o modo e leia **o arquivo de referência inteiro** antes de agir. Anuncie cada troca de modo e trate um modo por vez.

| Modo | Escopo | Saída | Nunca faz |
|---|---|---|---|
| **Planning** | Requisitos, inspeção do modelo, escopo, plano de páginas, aprovação | `_brief/report-spec.md` e **para** (aprovação é fronteira de turno) | Construir/publicar antes da aprovação |
| **Design** | Tom, assinatura, arquétipo, gráficos, layout, cor, tipografia, acessibilidade, branding | Bloco `Design Brief:` com `design_identity` e `layout_contract` por página | Editar PBIR ou chamar o Fabric |
| **Authoring** | Ler/editar PBIR/PBIP local, validar por lote, preview, screenshots | Arquivos PBIR editados + revisão renderizada | Publicar |
| **Management** | Upload, download, publish, list, get, update, delete, rebind, LRO, verificação | Item de relatório no Fabric | Escrever conteúdo PBIR |

Regras de fronteira:
- Classifique pelo intuito. Reestilizar relatório local = authoring. Edição pontual pula o planning.
- Relatório novo segue **planning → design → authoring → management**.
- Use o modo mais estreito que resolva. Use a metadata/validação da CLI `powerbi-report-author`, **nunca** adivinhe schemas, roles ou enums.
- Mudanças ficam locais, salvo pedido de publicação.
- Header de telemetria em toda chamada a `api.fabric.microsoft.com`: `x-ms-fabric-skill: powerbi-report-cli`.
- IDs de workspace/item: liste e filtre com JMESPath (só em fluxos de management; em preview, **pergunte** os IDs que faltarem).

Divisão de camadas [Learn]: modelo (tabelas, medidas, DAX) → Power BI Authoring/Modeling MCP ou `semantic-model-authoring`. Consultas e insights → Fabric IQ MCP (`fabriciq`). Camada de relatório (PBIR) → esta skill. Verificação no Desktop → Power BI Desktop CLI (Desktop Bridge).

Considerações [Learn]: funciona **só com PBIP**; faça commit de uma baseline antes de deixar o agente editar; **o PBIR é a fonte da verdade** (salve o Desktop antes, senão mudanças não salvas são ignoradas); evite Q&A, Bing maps e filled maps (serão descontinuados).

---

## 3. Fluxo recomendado

### 3.1 Planning [upstream]
Define → Inspect → Spec → Approve → Build → Validate → Publish.
- Perguntas **uma por vez** (`ask_user`), em 3–5 rodadas no máximo. Não repita o que já foi respondido.
- **Rodada 0:** modo de entrada: **Local Model** (arquivos), **Live Connected Model** (resolver workspace/modelo) ou **No Model** (redirecionar para `semantic-model-authoring`). Registrar dependências (Desktop, PBIP/PBIR/TMDL, MCP, Node.js). Dependência ausente = fase bloqueada/manual, sem parar o planejamento.
- **Rodada 1:** público e objetivo (tom, critérios de sucesso).
- **Rodada 2:** inventário do modelo (fatos, dimensões, medidas, lacunas, riscos) antes de fechar escopo.
- **Rodada 3:** plano de páginas com 2–3 formatos baseados nos **5 arquétipos** (um recomendado), com páginas, visuais, campos e camada de interação (slicers, drillthrough, **um** modelo de navegação, buttons/bookmarks).
- **Rodada 4:** 2–3 opções de identidade visual + destino (local, publicar, novo, update).
- Defaults automáticos: contraste WCAG AA, alt text em todo gráfico, **Azure Map** no lugar de mapas descontinuados, tabelas mais embaixo, interações previsíveis.
- Um `_brief/report-spec.md` **travado** e aprovado antes de qualquer build. Em modelo live, a seção *Semantic model binding* guarda nomes/IDs e a connection string.

### 3.2 Design [upstream]
0. **Dados primeiro**: catalogar tabelas/medidas/hierarquias e amostrar dados.
1. **Identidade**: um *tone* + uma *signature* (um recurso visual recorrente). O tom declarado precisa mudar paleta, tipo e bordas.
2. **Arquétipo por página**:
   | Arquétipo | Pergunta | Variantes de layout |
   |---|---|---|
   | Executive Summary | "Estamos no rumo?" | Hero-Right / KPI-Strip / Headline-Hero |
   | Operational Monitor | "Algo quebrou?" | 4-Up Status / Wallboard / Incident-First |
   | Analytical Canvas (padrão na dúvida) | "Por que X aconteceu?" | Filter-Rail / Inline-Slicers / Small-Multiples-Grid |
   | Narrative Story | Argumento conduzido | 7/5 Split / Single-Column-Scroll / Annotated-Hero |
   | Comparative Benchmark | "Em relação a quê?" | Side-by-Side / Stacked-Pairs / Slope-Graph-First |
3. **Escolha de gráfico** pela hierarquia de codificação: posição → comprimento → ângulo → área → matiz.
4. **Configuração** (cookbook) e **layout** (grid de 8 px).
5. **Tema**: adaptar a partir do base, preservando salvaguardas por tipo; manter o tema existente salvo pedido.
6. **Contrato** (YAML `Design Brief:`): `generated_by: powerbi-report-cli`, `contract_version`, modo greenfield/brownfield, `design_identity`, `navigation_model`; por página: nome em forma de insight, papel (landing/detail/drillthrough/tooltip), arquétipo, variante; `layout_contract` (canvas FHD 1920×1080, margem 32, gutter 24, snap 8, grid 12×12, placements e `space_audit`).
7. Revisão com checklists (design-brief, pre-flight) antes do handoff.

### 3.3 Authoring [upstream]
1. Confirmar a CLI: Node.js ≥ 20; `npm install -g @microsoft/powerbi-report-authoring-cli@latest`; `powerbi-report-author --version`.
2. Aprender o modelo (MCP, skill de modelo ou TMDL).
3. Definir o contexto de preview (host e argumentos).
4. Rotear pelo tópico (ver §4).
5. Consultar metadata da CLI (`catalog list`, `catalog describe <type>`, `formatting describe-object`, `formatting list-objects <type>`, `formatting search <type> <regex>`).
6. Ler os anti-patterns (`authoring-part-04.md`).
7. `powerbi-report-author validate <pasta .Report>` **após cada lote lógico**.
8. Verificar renderização: carregar o PBIR mais recente, capturar **toda página afetada** e revisar (`screenshot-review.md`).
9. Reportar problemas maiores/menores.

**Completion gate:** "Schema success alone is never task completion." Validar → carregar no host → screenshot de cada página afetada (`--all-pages` para mudança global, ex.: tema) → revisar → corrigir e repetir. Se não der para carregar/capturar, reporte como **bloqueado**, não como concluído.

Scaffold: `powerbi-report-author scaffold <out> --name <Report> [--model-path ../Sales.SemanticModel] [--page-name] [--force] [--offline]`. Sem `--model-path`, o binding fica como placeholder e precisa ser reapontado. `--offline` usa schemas fixados na CLI.

### 3.4 Preview [upstream]
| Host | Uso | Requisitos |
|---|---|---|
| `--host desktop` | Power BI Desktop local | O `.pbip` dono do relatório. Nunca `--pid` |
| `--host service` | PBIR local renderizado contra modelo publicado | `--group <workspace-guid>` e `--dataset <model-guid>` em **todo** comando. Pergunte se faltar, nunca deduza |

- Primeiro comando de open/reload: `powerbi-report-author preview "<pasta>" --host <desktop|service> --status`.
- `hasUnsavedChanges: true` = **parada obrigatória**. `HOST_UNAVAILABLE` permite open, não reload.
- `--reload` só se o usuário disser "reload/refresh". `--reload-with-model` só para mudanças de TMDL.
- **Nunca** combine `--reload` com `--screenshot` (timeout de 30 s): são chamadas separadas.
- Screenshot: PNG para uma página, diretório para `--all-pages`, `--scale 1-3` (padrão 2). Caminho absoluto, fora do projeto PBIP, com pasta aprovada pelo usuário e apagada no fim.
- Retry **uma vez** só se o resultado trouxer um objeto `correction` legível por máquina. Sem isso, encerre sem mais chamadas.
- Serviço: depois da revisão aprovada, abrir preview visível e deixar aberto.
- Preview **não publica**.

### 3.5 Management / publicação [upstream]
- **Nenhuma escrita remota sem permissão explícita** ("publish", "upload", "push", "deploy"). Aprovação de edição, validação ou preview não conta. **Sobrescrever exige confirmação separada.**
- Transporte **só** via CLI (≥ 0.3.0-beta.0): `pack` (`--raw` para corpo de request; `--mode create --display-name ...`) e `unpack` (`--input`, `--force` só em pasta descartável; só PBIR). jq/base64 manual não é suportado.
- Preflight antes do pack: existe `definition/report.json`; `validate` sem erros. `.Report` legado gera payload parcial, e `updateDefinition` apagaria as partes omitidas.
- Publicar `.pbip` local:
  1. Detectar fonte local (`.pbip`, `.Report` + `.SemanticModel`, `byPath`).
  2. Confirmar **um** workspace para modelo e relatório.
  3. Perguntar: publicar o modelo local (handoff para `semantic-model-authoring`) ou usar um existente.
  4. Resolver `semanticModelId` (listar modelos por nome).
  5. **Verificar bindings**: baixar o TMDL do modelo e comparar com os campos do relatório (o deploy pode renomear).
  6. **Rebind** `definition.pbir`: `byPath` → `byConnection` `semanticmodelid=<id>` (o Fabric rejeita `byPath`) **antes** do pack.
  7. Nome padrão = nome do `.pbip`; se existir, perguntar se sobrescreve, renomeia ou cancela.
  8. `pack --raw` → `az rest --resource "https://api.fabric.microsoft.com"` → `POST /v1/workspaces/$WS_ID/reports` (criar) ou `POST /v1/workspaces/$WS_ID/reports/$REPORT_ID/updateDefinition` (sobrescrever) → capturar `x-ms-operation-id` e fazer poll do LRO.
  9. Limpar temporários e entregar a URL (a renderização não é verificável programaticamente).
- **Nunca** refaça um POST de criação após `202` (gera duplicata).

---

## 4. Tópicos de authoring [upstream]

### 4.1 Formato PBIR
```text
<Report>.pbip
<Report>.Report/
  .platform
  definition.pbir                      (version "4.0"; datasetReference)
  definition/
    version.json                       ("2.0.0", manter $schema)
    report.json                        (tema, resourcePackages, publicCustomVisuals)
    bookmarks/bookmarks.json + <id>.bookmark.json
    pages/
      pages.json                       (pageOrder, activePageName)
      <pageId>/page.json
      <pageId>/visuals/<visualId>/visual.json
  CustomVisuals/
  StaticResources/ (SharedResources/BaseThemes, RegisteredResources)
<Report>.SemanticModel/                (fora do escopo desta skill)
```
- Não altere `$schema` existentes. Para arquivo novo, copie de um do mesmo tipo no mesmo relatório. Nunca faça bump de versão por conta própria (`UnrecognizedSchemaVersion` indica família errada).
- Página nova entra em `pageOrder`, senão fica invisível. Não commite `localSettings.json`.
- Nomes: visual = 20 hex minúsculos (único na página); página = 20 hex (moderno) ou `ReportSection` + 24 hex; filtro = `Filter` + 24 hex (único no relatório). Em Node: `crypto.randomBytes(10|12).toString('hex')`.
- Página nova (exemplo do upstream): `displayOption: "FitToPage"`, 1280×720. O design mode recomenda **FHD 1920×1080** para relatórios novos. Siga o `layout_contract`.
- Visual: `position` (x, y, z, height, width, tabOrder), `visual.visualType` e `visual.query.queryState` com projeções por role (`field`, `queryRef` `Entity.Property`, `nativeQueryRef`). Projeções **dentro de `queryState`**. `z` em passos de 1000 e `tabOrder` acompanhando.
- Edição de JSON: faça parse → modifique → serialize (Node). Evite `ConvertTo-Json` do PowerShell (reordena e trunca profundidade; se usar, `-Depth 20`) e regex.

### 4.2 Model binding (`definition.pbir`)
| Cenário | Forma |
|---|---|
| Modelo no disco ao lado | `byPath` → `"path": "../<Projeto>.SemanticModel"` (relativo, só essa chave) |
| PBIP local ligado a modelo remoto em host local | `byConnection` completo: `Data Source=powerbi://api.powerbi.com/v1.0/myorg/<Workspace>;Initial Catalog=<Modelo>;Integrated Security=ClaimsToken;semanticModelId=<GUID>` |
| Publicação via REST | `byConnection` mínimo: `semanticmodelid=<id>` (não abre em host local) |

Erros comuns: propriedade extra em `byConnection` (deixe só `connectionString`); falta `semanticModelId`; *serverName assertion* (falta Data Source/Initial Catalog).

### 4.3 Drillthrough (mesmo relatório)
- `page.json` da página destino: filtro em `filterConfig.filters` (`Filter<24hex>`, `Column`, `type: "Categorical"`, `"howCreated": "Drillthrough"`) + `pageBinding` (`name: "Pod"`, `type: "Drillthrough"` ou `"Tooltip"`, `parameters` com `boundFilter` e `fieldExpr` iguais ao filtro).
- Fluxo: campo projetado no visual de origem → página destino com filtro → parâmetro → visuais + **botão Voltar obrigatório** → menu de contexto ou botão de drillthrough → validar/recarregar → testar filtro e Voltar.
- Botão de drillthrough só ativa quando o **ponto de dados selecionado** carrega o campo. Seleção em slicer não basta.

### 4.4 Interações entre visuais
`visualInteractions` em `page.json` (`source`, `target`, `type`: `NoFilter`, `DataFilter`, `HighlightFilter`). Sem entrada, vale o cross-filter padrão.

### 4.5 Bookmarks
- Um `definition/bookmarks/<name>.bookmark.json` por bookmark, com nome de arquivo = `name`, registrado em `bookmarks.json` (direto ou em grupo). Referências sempre por **IDs PBIR crus**, nunca por display names.
- Opções invertidas: Data = `suppressData: false`; Display = `suppressDisplay: false`; Current page = `suppressActiveSection: false`; Selected visuals = `applyOnlyToTargetVisuals: true`.
- Show/hide e troca de gráfico: `suppressData: true` (não reseta slicers) e guarde o estado **dos dois lados** do toggle (`singleVisual.display.mode: "hidden"`).
- Filtros em `byExpr` (não `byName`).
- Botão: `visualContainerObjects.visualLink` com `show: true`, `type: 'Bookmark'`, `bookmark: '<name>'`.
- Não adivinhe o encoding de `bookmarkNavigator`; prefira `actionButton`.
- Mantenha 5–8 bookmarks (anti-patterns de design).

### 4.6 Buttons
- Sem data roles; ação via `visualLink` (tipos de ação: consulte `formatting search actionButton "action|link|type"`).
- Largura por `text measure` (`recommendedButtonWidthPx`); altura `clamp(fontPt×4, 40, 56)`; ≥ 8 px entre botões; margem de 16–32 px do canvas.
- Contrato de renderização: container `background.show=false`, `border.show=false`, `tileShape='rectangleRounded'`, `icon.placement` left/right.
- `pageNavigator` e `bookmarkNavigator` são alternativas automáticas.

### 4.7 Custom visuals
| Tipo | Registro em `report.json` | `visualType` |
|---|---|---|
| AppSource | `publicCustomVisuals` (GUIDs) | `<GUID>` |
| Organizacional | `resourcePackages` tipo `OrganizationalStoreCustomVisual`, item `resources/<GUID>_OrgStore.pbiviz.json`, `path: ""` | `<GUID>_OrgStore` |
| Privado `.pbiviz` | Descompactar em `CustomVisuals/<GUID>/` **e** `resourcePackages` tipo `CustomVisual` | `<GUID>` |
- **Nunca adivinhe GUID** (pegue do `package.json` do `.pbiviz` ou de um `report.json` salvo pelo Desktop). `PBIR_VISUAL_TYPE_UNKNOWN` é só warning, mas na prática significa que o visual não renderiza.
- Visuais freemium: categoria de baixa cardinalidade (~30), sem legenda, uma medida.

### 4.8 Field parameters (lado do relatório)
- A tabela do parâmetro é do **modelo** (`semantic-model-authoring`). Aqui só se lê o TMDL para reconhecer (`ParameterMetadata` `kind: 2`).
- Slicer: `visualType: slicer`, `data.mode: "Basic"`, coluna **visível** em `Values`, sem `drillFilterOtherVisuals`.
- Visual alvo: projeta os campos subjacentes na ordem do `NAMEOF` + array `fieldParameters` (`parameterExpr`, `index`, `length`).
- A página deve ter **as duas metades** (slicer + visual).

### 4.9 KPI
- Roles: `Indicator` (obrigatório, **medida**), `TrendLine` (data/datetime/numérico crescente), `Goal` (até 2 medidas). Schema 2.10.0 para visuais novos.
- Renderiza em branco quando: Indicator é coluna crua (`PBIR_ROLE_KIND_MISMATCH`), Indicator é BLANK no último ponto (use `LASTNONBLANK`/`COALESCE`), TrendLine é texto, ou Goal está em grão diferente.

### 4.10 Outros pitfalls de PBIR
- Filtros: dentro de `Where` use `"Source"` com o alias do `From` (não `"Entity"`). Sempre inclua `nativeQueryRef`. Literais: `true/false` sem aspas, números com sufixo `D`/`L`.
- Descontinuados: `multiRowCard` → `cardVisual` (role `"Data"`); `map`/`filledMap` → `azureMap`. `tableEx` com tudo em Values não mostra linhas → `pivotTable`.
- Vários KPIs relacionados: um `cardVisual` multi-valor em vez de vários cartões.
- Tabelas/matrizes: `columnAdjustment: growToFit` e `autoSizeColumnWidth: true`.
- `dataPoint.defaultColor` em gráfico multi-série colapsa tudo numa cor. `ThemeDataColor` com seletor de metadata pode virar branco/preto (use hex `Literal`).
- Mantenha um **mapa medida→cor**: `dataColors` atribui por índice, e a mesma medida pode mudar de cor entre visuais.
- Page `background` aceita só `color`, `image` e `transparency`. Divisórias finas: `shape` retângulo (textbox tem ~24 px mínimo). `paragraphs` de textbox é array JSON.

---

## 5. Validações (resumo)
| Momento | Validação |
|---|---|
| Cada lote de edição | `powerbi-report-author validate <.Report>` |
| Após validate | Preview (status → reload), screenshot de cada página afetada, revisão |
| Bookmarks | Códigos `PBIR_BOOKMARK_*` (arquivo × nome, índice, refs de página/visual, alvo de ação) + teste A→B→A no Desktop |
| Custom visuals | Renderização real no Desktop (org visuals carregam devagar: esperar 15–20 s e recarregar) |
| Field parameter | `validate` passa com referência errada; confirme sempre pelo screenshot |
| Antes de publicar | Model binding verificado (diff TMDL × campos), rebind para `byConnection`, preflight do pack |
| Depois de publicar | Listar relatórios no workspace; entregar URL ao usuário |

---

## 6. Boas práticas de design de relatório

### 6.1 Layout [upstream design/layout.md]
- Item mais importante no **canto superior esquerdo**. Leitura em **F** (analítico/operacional) ou **Z** (executivo/narrativo).
- **Grid de 8 px**: posições e tamanhos múltiplos de 8. Espaçamentos: 16 (dentro do grupo), 24 (entre grupos/margens), 32 (seções). Use um valor intragrupo e um intergrupo, nunca três numa linha.
- **7 ± 2 grupos visuais por página.** Canvas padrão FHD 1920×1080 (margem 32, gutter 24, 12 colunas de ~132,7 px). Faixa de título de ~72 px.
- Splits comuns (FHD): 12 (~1856), 8+4, 6+6 (~916), 7+5, 4+4+4 (~603), 3+3+3+3 (~446).
- Slicers: 1–3 inline à direita da linha de título (~230×64 px no FHD, 16–24 px entre eles); 4+ num **filter rail** vertical (~310 px), justificado se os slicers ocuparem ≥ 50% da altura. Slicers fora do canto superior esquerdo.
- Sem sobreposição (z-order não conserta layout). Nada fora do canvas. `tabOrder` = ordem de leitura.
- Espaço vazio ≤ 15% (analítico/operacional/comparativo) ou ≤ 20% (executivo/narrativo). Cartão de valor único nunca é o "herói": precisa de delta, sparkline, limite ou anotação.
- Títulos de gráfico como **insight** ("Vendas caíram 8% no T4"), não como tipo do gráfico.

### 6.2 Anti-patterns de design [upstream design/anti-patterns.md]
- **Ruído visual:** nada de 3D, sombras ou fundos saturados; canvas branco/quase branco.
- **Codificação enganosa:** barras começam no zero; sem eixo Y duplo; pizza no máximo com 5 fatias (senão, barra horizontal ordenada); small multiples com eixos iguais; gauge → cartão + sparkline ou bullet; radar → barras agrupadas.
- **Sobrecarga:** 3–4 cartões KPI; 5–7 grupos por página (não 12+); 2–3 slicers; slicer de data no grão do dado (ano em dropdown para páginas executivas); matrizes grandes fora de páginas executivas; navegação em relatórios multipágina.
- **Cor:** rampa sequencial para dados ordenados; vermelho/verde acompanhado de ícone ou texto; nunca inverter "verde = bom"; no máximo 7–8 matizes categóricas; vermelho/âmbar só para exceções.
- **Interatividade:** insight principal visível no carregamento; estado dos filtros visível; botão Voltar em drillthrough; sem carrossel automático.
- **Arquétipo:** operacional com timestamp de atualização; analítico com drillthrough e export; comparativo com slicers sincronizados; modelos grandes com pré-filtro padrão.
- Rótulos legíveis ("Total de Vendas", não "Sum of sales_amt").

### 6.3 Acessibilidade [upstream design/accessibility.md]
- Cor nunca é o único canal (WCAG 1.4.1).
- Contraste: texto **4,5:1**; texto grande (≥ 18 pt ou ≥ 14 pt negrito) e elementos não textuais (barras, linhas, ícones) **3:1**; AAA 7:1.
- **Alt text** focado no insight, com números reais (cartão < 150 caracteres, visual complexo < 300). Pode ser dinâmico via DAX (ver `powerbi-dax-padroes.md` §10).
- Navegação por teclado (Tab/Enter/Esc); ordem de foco lógica pelo Selection pane; alvos ≥ 24×24 px; legível com zoom de 200%; testar com Windows High Contrast; "Show as table" como fallback.
- Paletas seguras para daltonismo: Okabe-Ito, viridis, cividis. Simule com Coblis/Viz Palette/Chrome DevTools.
- Checklist pré-publicação: só teclado, leitor de tela (NVDA/Narrator), zoom 200%, alto contraste, simulação de daltonismo, medição de contraste, tab order, alt text, tamanho de alvo, Show as table.

---

## 7. Tema do relatório: como é registrado no PBIR [upstream authoring/theming.md]
- Arquivo em `StaticResources/RegisteredResources/<Nome>-<guid8a12hex>.json` (o GUID no nome serve de cache-busting, porque o Desktop faz cache pelo nome do arquivo).
- `report.json`: `themeCollection.customTheme` (`name`, `reportVersionAtImport`, `type: "RegisteredResources"`) + entrada em `resourcePackages` do tipo `RegisteredResources` com item `type: CustomTheme`.
- `customTheme.name`, `items[].name` e `items[].path` **idênticos e com `.json`**. `path` é só o nome do arquivo (prefixo de pasta faz o Desktop ignorar o tema). `"SharedResources"` como tipo falha em silêncio.
- A cada edição do tema: gere novo GUID, mantenha o nome base, renomeie o arquivo, atualize as 3 referências e recarregue. Depois, preview com `--all-pages`.
- Mudar o tema **não** altera cores hex `Literal` fixadas nos visuais: faça uma varredura em `definition/`.
- `$schema`: reutilize o dos base themes, se houver; senão, o `reportThemeSchema-<x.y>.json` mais recente de `microsoft/powerbi-desktop-samples`.

---

## 8. Estrutura JSON do tema [Learn + upstream]

Como funciona [Learn]: todo relatório tem um **base theme** (gerenciado pela Microsoft). O **custom theme** fica por cima e sobrescreve cores/estilos. Formatação feita direto no visual prevalece até **Reset to default**. Aplicar ou importar tema remove customizações de tema anteriores. Use sempre **cores do tema** nos visuais: elas acompanham trocas de tema. Em formatação condicional por *Field value*, uma medida pode retornar o nome `good`, `bad` ou `neutral`. Cores de séries são atribuídas **pela ordem** em que aparecem no visual (a mesma região pode ter cores diferentes em visuais diferentes).

| Chave | O que controla | Default (base) |
|---|---|---|
| `name` | Nome do tema (no PBIR, igual ao nome do arquivo com `.json`) | — |
| `dataColors` | Paleta categórica por índice. Substitui a do base inteira (base tem 41 cores); o Power BI deriva tons quando acaba | — |
| `good` / `neutral` / `bad` | Sentimento (waterfall, KPI) | `#1AAB40` / `#D9B300` / `#D64554` |
| `maximum` / `center` / `minimum` / `null` | Sementes do gradiente de formatação condicional | `#118DFF` / `#D9B300` / `#DEEFFF` / `#FF7F48` |
| `foreground` (≈ `firstLevelElements`) | Rótulos, textboxes, data labels de cartão | — |
| `foregroundNeutralSecondary` (≈ `secondLevelElements`) | Legenda, eixos, cabeçalho de tabela | — |
| `backgroundLight` (≈ `thirdLevelElements`) | Gridlines, fundo de cabeçalho de slicer | — |
| `foregroundNeutralTertiary` (≈ `fourthLevelElements`) | Legenda esmaecida, rótulo de categoria do cartão | — |
| `background` | Tooltips, botões, dropdown de slicer | — |
| `backgroundNeutral` (≈ `secondaryBackground`) | Faixas, botão desabilitado | — |
| `tableAccent` | Contorno de grade de tabela/matriz | — |
| `textClasses` | `label` (Segoe UI 10), `title` (DIN 12), `callout` (DIN 45), `header` (Segoe UI Semibold 12) + derivadas (`largeTitle`, `semiboldLabel`, `largeLabel`, `smallLabel`, `boldLabel`, `lightLabel`, `largeLightLabel`, `smallLightLabel`). Propriedades: `fontFace`, `fontSize` (pt), `color`, `bold` | — |
| `visualStyles` | tipo de visual → preset → objeto → array de propriedades; `"*"` curinga em cada nível | — |
| `icons` | Ícones customizados | — |

Resolução de `visualStyles` (o primeiro que casar vence): custom tipo+preset → custom tipo+`*` → custom `*`+preset → custom `*`+`*` → base tipo+`*` → base `*`+`*` → default do sistema.

Tema escuro: troque **todas** as cores estruturais juntas e defina explicitamente `outspacePane` e `filterCard` em `visualStyles["*"]["*"]` (o painel de filtros não herda). Objetos multi-instância usam `$id` (ex.: `filterCard` `"Applied"`/`"Available"`). Cor: na dúvida, use a forma `{ "solid": { "color": "#hex" } }`.

### 8.1 Exemplo mínimo (do Microsoft Learn)
```json
{
    "name": "Valentine's Day",
    "dataColors": ["#990011", "#cc1144", "#ee7799", "#eebbcc", "#cc4477", "#cc5555", "#882222", "#A30E33"],
    "background": "#FFFFFF",
    "foreground": "#ee7799",
    "tableAccent": "#990011"
}
```

### 8.2 Exemplo estrutural mais completo (ilustrativo; cores genéricas, **não** é o tema do time)
```json
{
  "name": "Exemplo-1a2b3c4d.json",
  "dataColors": ["#1F4E79", "#2E86C1", "#7FB3D5", "#F39C12", "#7A7A7A"],
  "good": "#1AAB40",
  "neutral": "#D9B300",
  "bad": "#D64554",
  "maximum": "#118DFF",
  "center": "#D9B300",
  "minimum": "#DEEFFF",
  "foreground": "#252423",
  "background": "#FFFFFF",
  "tableAccent": "#1F4E79",
  "textClasses": {
    "label":   { "fontFace": "Segoe UI", "fontSize": 10, "color": "#252423" },
    "title":   { "fontFace": "Segoe UI Semibold", "fontSize": 12, "color": "#252423" },
    "callout": { "fontFace": "Segoe UI", "fontSize": 28, "color": "#252423" },
    "header":  { "fontFace": "Segoe UI Semibold", "fontSize": 12, "color": "#252423" }
  },
  "visualStyles": {
    "*": {
      "*": {
        "background": [{ "show": true, "color": { "solid": { "color": "#FFFFFF" } } }],
        "border": [{ "show": true, "radius": 4 }]
      }
    },
    "barChart": { "*": { "border": [{ "radius": 8 }] } }
  }
}
```
No PBIR, `name` inclui `.json` e deve bater com o nome do arquivo registrado [upstream]. No Desktop (Import theme), o `name` é só o rótulo do tema [Learn].

Para o time, use **sempre** `tema-oficial-powerbi.json` (ver `powerbi-tema-cores.md`).
