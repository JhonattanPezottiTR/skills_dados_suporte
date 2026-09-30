# Tipos de BI do time: métricas, campos e fontes

> Última atualização: 2026-09-29 · Fonte: definição do time de BI (a preencher) + `powerbi-catalogo-relatorios.md` · **Arquivo curado** (editado à mão)

Cada tipo de BI tem aqui o objetivo, o público, as métricas com a regra de cálculo, os campos e a fonte oficial (entidade do fluxo, tabela Postgres ou push dataset). As regras de cálculo validadas viram `REG-###` em `regras-negocio.md`.

## Modelo de ficha

```markdown
### <Nome do BI>
- **Objetivo / público:** ...
- **Relatório(s):** <nome no catálogo> · **Workspace:** ...
- **Atualização:** tempo real (push / Sybase direto) | D-1 (Dataflow) | ...
- **Fonte oficial:** Dataflow `<FLUXO>.<entidade>` | `DB_x.schema.tabela` | push `<dataset>` (job `<job>`)
- **Métricas:**
  | Métrica | Definição de negócio | Cálculo (DAX/SQL) | Regra |
  |---|---|---|---|
- **Dimensões / filtros padrão:** ...
- **Tema:** Padrão TR Clario (COR-001)
```

## BIs já identificados nos arquivos (a completar pelo time)

| BI | Relatório | Atualização | Fonte | Status da ficha |
|---|---|---|---|---|
| Pendências SGD (N1/N2) | `_sgdPendency` | tempo real (push) | job `produtividade-pendencia-realtime` | ⏳ aguardando definição |
| Produtividade SGD + Genesys | `_genesysSGD_Productivity` | tempo real (push) | job `produtividade-pendencia-realtime` | ⏳ aguardando definição |
| SLA das filas de voz | `_genesysQueueSLA` | tempo real (push) | job `genesys-sla` | ⏳ aguardando definição |
| Filas Genesys (espera) | `_genesysQueue` | tempo real (push) | job `genesys-queue-realtime` | ⏳ aguardando definição |
| Acompanhamento tempo real Fone / NOT READY | `Acompanhamento Tempo Real Fone_v2.1` | tempo real (push) | job `genesys-sla` | ⏳ aguardando definição |
| Demanda projetada | `Real Time projetado` | Import (Excel SharePoint) | planilhas de plano 2026 | ⏳ aguardando definição |
| Agenda em tempo real | — | tempo real (Sybase direto) | Dataflow `TB_SYBASE_SGD_AGENDA.Agenda` | ⏳ aguardando definição |
