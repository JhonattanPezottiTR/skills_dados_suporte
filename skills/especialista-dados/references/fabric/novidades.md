# Novidades do Fabric / Skills for Fabric

> Última atualização: 2026-09-29 · Fonte: https://github.com/microsoft/skills-for-fabric/blob/main/CHANGELOG.md · Base sincronizada: v0.3.18

Resumo das mudanças upstream relevantes para SQL, Power BI e Fabric. Entradas mais novas no topo.

## ⚠️ Nomes antigos que ainda aparecem no Microsoft Learn
A página "Discover" do Learn e alguns artigos ainda citam nomes antigos de skills. Use sempre os nomes atuais:

| Nome antigo (Learn / blogs) | Nome atual (v0.3.18) | Desde |
|---|---|---|
| `sqldw-authoring-cli`, `sqldw-consumption-cli`, `sqldw-operations-cli`, `sqldw-monitoring-cli` | `sqldw-cli` (modos authoring/consumption/operations) | 0.3.12 |
| `dataflows-authoring-cli`, `dataflows-consumption-cli` | `dataflows-cli` (modos authoring/consumption/upgrade) | não informado no CHANGELOG |
| `powerbi-report-planning/-design/-authoring/-management` | `powerbi-report-cli` | 0.3.17 |
| `semantic-model-consumption`, `powerbi-consumption-cli`, `powerbi-authoring-cli` | não existem mais; use `semantic-model-authoring` + `fabriciq` para consultas DAX | — |
| `check-updates` | removida (BREAKING) | 0.3.12 |

## v0.3.18 — 2026-09-24 (sincronizada em 2026-09-29)
- **Adicionado:** `powerbi-report-cli` passou a cobrir drillthrough, bookmarks, buttons, custom visuals, field parameters, KPIs, model binding e fluxos de preview. Nova skill `project-osmos` para trabalho longo de engenharia de dados Fabric/OneLake a partir de agentes locais.
- **Alterado:** `powerbi-report-cli` com orientação mais forte de planejamento, validação e publicação; trabalho no Desktop passa por `powerbi-report-author preview`. `synapse-migration` migra dedicated SQL pools para Lakehouse (schema e código) ou Warehouse (assessment, segurança e movimentação de dados opcional).
- **Corrigido:** âncoras de referência quebradas; a continuação do "planning contract" passou a ser obrigatória antes de gerar uma spec aprovada.

## v0.3.17 — 2026-09-17
- **Adicionado:** orientação de field parameters em `semantic-model-authoring`; `powerbi-report-cli` unificado (modos planning, design, authoring, management).
- **Alterado:** bundle `powerbi-authoring` passa a ter uma única skill de relatório. Endpoint MCP do FabricIQ mudou para `https://fabriciq.svc.cloud.microsoft/v1/mcp/fabriciq` (header `X-VARIANTS: Fabric.Routing.FabricIQ.V1`). `ResolveReportIdFromUrl` substituído por `ResolveFabricItem`.
- **Removido:** as quatro skills `powerbi-report-*` (planning/design/authoring/management) — renomeadas e fundidas em `powerbi-report-cli`.

## v0.3.16 — 2026-09-10
- **Adicionado:** `apm.yml` raiz e por skill → instalação individual com `apm install microsoft/skills-for-fabric --skill <nome>`.
- **Corrigido:** plugin `fabric-skills` reutiliza login do Azure CLI para MCP remoto no Claude Code.
