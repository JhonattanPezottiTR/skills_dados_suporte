# Blocos visuais aihub — o que escrever, degradar ou evitar

> Última atualização: 2026-09-30 · Fonte: skill `alia-trtools` (catálogo de 68 blocos visuais do portal AI Champions, "aihub")

Catálogo de referência para quando o pedido for um **Excel** ou um **relatório/dashboard/apresentação em HTML**
(fora do Power BI — para PBIP, ver `powerbi-criacao-pbip.md`/RG-12). Não é o catálogo completo de 68 blocos (não
copiado aqui); é a orientação de **tier** — o que dá para montar direto, o que degrada e o que evitar
reimplementar — pensada para este time.

## Tiers

| Tier | O que fazer |
|---|---|
| ✅ Reproduzível | Monte o bloco direto (tabela, card, KPI, indicador, grade, lista, timeline simples, badge, callout) usando a identidade de `visual-identidade-tr.md`. |
| ⚠️ Parcial | Dá para montar uma versão boa, mas **diga ao usuário o que ficou de fora** (ex.: timeline sem todas as variantes, infográfico sem todos os layouts). |
| ⛔ Não reimplementar | Blocos grandes e interativos de verdade (tabela com ordenação/filtro/export, pivot dinâmico, dashboard com drag-and-drop, apresentação com export PPTX). Ver substitutos abaixo. |

### Os casos ⛔ mais comuns neste time e o substituto

| Pedido | Não reimplemente | Use no lugar |
|---|---|---|
| Tabela com ordenar/filtrar/exportar | Motor de tabela completo | Excel de verdade (é a ferramenta certa para isso) ou tabela estática + aviso de que ordenação/filtro exigem abrir no Excel |
| Cruzamento dinâmico (pivot) | Pivot interativo em HTML | Tabela dinâmica do Excel, ou pré-computar o cruzamento e renderizar como tabela estática |
| Apresentação com export PPTX | Motor de slides | Os padrões de capa/slide de `visual-identidade-tr.md` (modo canvas), entregues como HTML/imagem — sem exportar PPTX |
| Dashboard com posicionamento livre (drag & resize) | Canvas de dashboard | Grade estática de blocos ✅ (KPI + gráfico + tabela) |
| Gráfico com 15+ tipos, eixos duplos, sankey | Motor de gráfico genérico | Escolher o tipo certo pelo formato do dado (ver "Cores em gráfico" abaixo) e usar uma lib de gráfico real (ex. Chart.js/Recharts) só estilizada com a paleta TR |

## Cores em gráfico (aplicação da paleta de `visual-identidade-tr.md`)

- **Categorias distintas** (séries que não têm ordem/hierarquia entre si) → percorrer, nesta ordem: azul-céu →
  verde-água → dourado → âmbar → lima. Escolhidas para se distinguirem entre si e do laranja da marca.
- **Ranquear volume da mesma grandeza** (ex.: top 10 revendas por SSC) → rampa do laranja, do mais escuro
  (`#D64000`) ao mais claro. Cor categórica aqui sugeriria diferença de tipo que não existe.
- **Realizado × projeção** → verde-sucesso `#2D7A3F` no medido, laranja no projetado (o laranja sinaliza "ainda
  não aconteceu").

## Regra de fidelidade (não negociável — irmã da RG-01 desta skill)

**Todo valor que o leitor vai entender como vindo dos dados tem que vir dos dados.** Não existe categoria
liberada para "ilustrar". Se falta o dado:
- omita o campo ou a seção inteira — um relatório com uma seção a menos é honesto;
- **nunca** preencha pessoa, cargo, área, meta ou comentário qualitativo com algo plausível — isso é pior que
  deixar vazio, porque tem a mesma aparência de um relatório correto.

**Exceção única:** quando o pedido é explicitamente por um **modelo/template para preencher depois**, use
placeholder óbvio (`999,99`, "Categoria A", "Mês 1") — óbvio de propósito, para ninguém confundir com dado real.

Esta regra está registrada como **RG-14** no `SKILL.md`.

## Erros comuns

| Erro | Consequência |
|---|---|
| Reimplementar tabela/dashboard/pivot do zero | Sai bonito e sem ordenação, filtro ou export — parece pronto e não é |
| Inventar pessoa, cargo ou meta que não veio nos dados | Mentira com aparência de relatório |
| Escolher o gráfico pela aparência, não pelo formato do dado | Pizza com 12 fatias, linha para categoria |
| Cor categórica para ranquear volume | Sugere diferença de natureza; usar a rampa do laranja |

## Relacionadas
- `visual-identidade-tr.md` — paleta, tipografia, os dois modos (RG-13).
- RG-01 (`SKILL.md`) — nunca inventar nome de tabela/coluna; RG-14 estende o mesmo princípio a dado de conteúdo.
- RG-15 (`SKILL.md`) — nenhum dado de conexão no artefato entregue.
