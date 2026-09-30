# Base de conhecimento do negócio — índice

> Última atualização: 2026-09-29 · Fonte: arquivos desta pasta (`references/negocio/`), montados a partir do Maestro, dos projetos legados, do `sql-base\agente`, dos Dataflows e de `references/dados/*` · **Arquivo curado** · Status: **Em revisão** (extraído de comentários/código — validar com o time)

## O que tem em cada arquivo

| Arquivo | Conteúdo | Use para |
|---|---|---|
| `conceitos.md` | Dicionário de conceitos de negócio: organização (revenda, filial, UPG, Televendas, regional), cliente/contrato/produto, pessoas (usuário interno × cliente × terceiro, colaborador ativo, alocação/área, gestor, cargo, horário), atendimento (SSC, SS, SSQL, conversão, SR, SA/NE, SOSE, classificação, situação, trâmite, meio de acesso), pendência/tempo/SLA, agenda, ocorrência, implantação, forecast, metas, canais (Genesys, Plug, CTS/TRIA, IA, LogMeIn), satisfação por canal, RLS. Cada item traz citação literal `arquivo:linha`, códigos, view Sybase, tabela Postgres, entidade do Dataflow e ⚠️ divergências. | "O que significa X?", "quais códigos são Y?", "qual a regra de Z?" |
| `linhagem-por-conceito.md` | Caminho de cada assunto: **Sybase (views/colunas) → carga (job, rotina, agenda, função e o COMO: TRUNCATE+INSERT, DELETE janela, DELETE por id, ACUMULA, UPDATE, UPSERT, dblink) → Postgres (base.schema.tabela, grão) → Dataflow (entidade) → relatório**. Inclui as tabelas derivadas (`tb_colaboradores`, `tb_demanda_lideres`, `tb_ocorrencias_analitica`, `tb_interacoes_lideres_plug_analitico`, `sgd_pendency`, `ss_pendency`, `calendar`, `goals`, `forecast.*`) e o tempo real. | "De onde vem?", "como é inserido?", "quão atual é?", "por que o número mudou?" |
| `tabelas-postgres-negocio.md` | Fichas das tabelas Postgres mais usadas: significado, grão (1 linha = ?), colunas de negócio, quem grava/como/frequência, quem consome, armadilhas. | "Qual tabela uso?", "posso somar esta coluna?", "tem histórico?" |
| `perguntas-em-aberto.md` | Divergências entre projetos (P-xx), tabelas sem job conhecido (L-xx), bugs/qualidade (Q-xx), propostas de correção para outros arquivos da skill e alertas de segurança (S-xx). | Avisar o usuário quando uma regra está em disputa; levar perguntas ao time |

## Ordem de consulta recomendada

**1. "De onde vem este campo / esta métrica?"**
- `linhagem-por-conceito.md`: ache o assunto e veja o caminho completo.
- Depois `dados-fluxo-<dataflow>.md`, para o SQL exato da entidade.
- Por fim `dados-linhagem.md` e `postgres-destinos.md`, para a lista gerada completa de função → tabela.

**2. "Como é inserido / por que duplicou / por que sumiu?"**
- A coluna **Carga** em `linhagem-por-conceito.md` e a ficha em `tabelas-postgres-negocio.md`.
- Os itens Q-xx e L-xx em `perguntas-em-aberto.md` (duplicação em reexecução, janelas, datas fixas, tabelas órfãs).

**3. "Qual tabela/entidade usar para o BI X?"**
1. Entidade de Dataflow existente (`dados-fluxos-powerbi.md`).
2. Tabela Postgres (`tabelas-postgres-negocio.md` + `dados-postgres-<base>.md`).
3. Para indicador por colaborador/dia, prefira `DB_REPORTS_ANALITICOS.public.tb_colaboradores`, lembrando da duplicidade (Q-05).
4. Tempo real: push datasets / `TB_SYBASE_SGD_AGENDA`.

**4. "O que significa o código N / qual a regra?"**
- `conceitos.md`.
- Se o item tiver ⚠️ ou estiver em `perguntas-em-aberto.md`, **diga que está em revisão** e cite as versões concorrentes (RG-11).
- Regras validadas pelo time ficam em `regras-negocio.md` (REG-###) e **prevalecem** sobre esta pasta.

## Regras de uso pela skill
- Esta pasta é **curada e está em revisão**: nada aqui é regra oficial até virar `REG-###`.
- Sempre cite a fonte (arquivo:linha) quando usar uma regra daqui. Diga "(inferido)" quando o arquivo marcar assim.
- Em conflito entre esta pasta e os arquivos gerados de `references/dados/`, **os gerados valem para estrutura** (tabelas, colunas, jobs, agendas) e **esta pasta vale para significado**. Registre o conflito em `perguntas-em-aberto.md`.
- Nunca copie credenciais, hosts ou connection strings (RG-06). Os `fontes/dataflows/*.json` contêm dblink com senha (S-01).
- **Glossário de caminhos usado nas citações:**
  - `orq:` = `C:\GitHub\TR\analytics-bi-dominio-orquestrador\`
  - `sqlbase:` = `C:\GitHub\TR\sql-base\`
  - `legado:<projeto>` = `C:\GitHub\TR\<projeto>\`
  - `fluxo-X.md:N` = linha N de `dados-fluxo-X.md`

## Cobertura atual
- **Conceitos:** 40 fichas (~50 conceitos) em 10 seções (organização, cliente/produto, pessoas, atendimento, pendência/tempo/SLA, agenda/ocorrência/implantação, planejamento/metas, canais, satisfação, RLS).
- **Linhagens:** 19 assuntos, com mais de 60 tabelas Postgres rastreadas, incluindo 6 tabelas derivadas e 5 caminhos de tempo real.
- **Fichas de tabela:** cerca de 35 fichas, mais tabelas-resumo de DB_GENESYS e DB_WEBCHAT.
- **Pendências:** 16 perguntas de regra (P), 13 lacunas de carga (L), 14 itens de qualidade (Q), 5 propostas de correção e 4 alertas de segurança.

- `negocio-filiais-revendas.md` — **consultar primeiro** para qualquer pergunta sobre Filial × Revenda × região × grupo: como o fluxo `DB_SGD_ALL.sgd_resales` monta o retorno, as divergências entre fontes e a dimensão `dRevenda` para BI (adicionado em 2026-09-29). ⚠️ **Em revisão:** a lista oficial de Filiais e o de-para revenda → regional ainda não foram confirmados pelo time — ver P-02 e P-03 em `negocio-perguntas-em-aberto.md` antes de publicar um número fechado.
