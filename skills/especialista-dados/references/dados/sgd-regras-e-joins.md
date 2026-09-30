# SGD — entidades, joins, códigos e regras de negócio

> Última atualização: 2026-09-29 (lista de filiais corrigida) · Visão de negócio completa, com citações: `negocio-indice.md` · Fonte: código do Maestro (`modules/_import_sgd`, `modules/_import_dominio`, `modules/produtividade_pendencia_realtime`, `modules/genesys_sla`) e dos projetos legados `import-sgd-geral`, `import-sgd-pendencias`, `productivity-pendency-realtime`, `cts-import`, `etl-tb-*`; `sql-base/agente` · **Arquivo curado** (editado à mão)
> ⚠️ **Status dos códigos: Em revisão.** Os valores foram **extraídos do código** e ainda não foram validados pelo time. Quando usar um deles, diga isso e peça confirmação. Os validados viram regras `REG-###` em `regras-negocio.md`.

## 1. Arquitetura dos dados do SGD

```
Sybase SQL Anywhere 17 (SGD)                Postgres (réplicas BI)                 Power BI
┌──────────────────────────┐   Maestro      ┌───────────────────────────┐  Dataflows  ┌──────────────┐
│ sgd   · bethadba.vw_*    │ ─ import-sgd ─▶│ DB_SGD (public/externo/    │ ──────────▶ │ Relatórios   │
│ sgsai · bethadba.vw_*    │   (D-1, deltas)│   forecast), DB_SGD_N2 (ss)│             │ (Import)     │
│ cts   · bethadba.vw_*    │ ─ import-cts ─▶│ DB_CTS                     │             │              │
│ power_bi.vw_usuarios     │                │ DB_GENESYS, DB_WEBCHAT     │             │              │
└──────────────────────────┘                │ DB_REPORTS_ANALITICOS (tb_*)│            │              │
        │  leitura direta (tempo real)       └───────────────────────────┘             │              │
        ├── Dataflow TB_SYBASE_SGD_AGENDA ───────────────────────────────────────────▶ │              │
        └── jobs realtime do Maestro (produtividade-pendencia, genesys-sla) ─ push ──▶ │ Push datasets│
                                                                                        └──────────────┘
```

- **Tempo real no SGD** só existe em duas situações:
  - leitura direta no Sybase: o Dataflow `TB_SYBASE_SGD_AGENDA` (agenda) e os jobs realtime do Maestro;
  - push datasets do workspace "Dashboard - Real Time".
- Todo o resto é **réplica no Postgres**, carregada pelo Maestro com agenda definida (ver `dados-fluxos-maestro.md`). A maior parte roda de madrugada, é D-1 e substitui uma janela de N dias (ver `dados-postgres-destinos.md`).
- **Padrão atual:** SQL no Sybase usa só `bethadba.vw_*` / `power_bi.vw_usuarios` (views liberadas). Projetos legados ainda leem tabelas físicas (`bethadba.ssc`, `bethadba.usuarios`, `dba.revendas`). O de-para tabela → view está em `import-sgd-geral/sgd_import/tools/aplica_depara_views.py`. Em SQL novo, use sempre a view.
- **Três bancos Sybase:** `sgd` (principal), `sgsai` (SA/NE) e `cts` (CTS/TRIA). O mesmo nome de view pode existir em mais de um banco com conteúdo diferente (ex.: `vw_modulos`).

## 2. Entidades principais

| Sigla | O que é | View Sybase | Réplica Postgres |
|---|---|---|---|
| **SSC** | Solicitação de suporte do cliente (atendimento N1) | `vw_ssc`, `vw_ssc_tramites`, `vw_ssc_situacoes` | DB_SGD `public.sgd_ssc`, `sgd_ssc_tramites`, `sgd_ssc_situation` |
| **SS** | Solicitação de serviço (N2) | `vw_ss`, `vw_ss_tramites`, `vw_ss_situacoes`, `vw_ss_categorias` | DB_SGD_N2 `ss.ss`, `ss.ss_tramites`, `ss.ss_situation`, `ss.ss_category` |
| **SSQL / Conversão / SR** | Demandas vinculadas à SSC (tempo de terceiros) | `vw_ssql*`, `vw_conversoes`, `vw_conversao_tramites`, `vw_sr*` | usadas nos tempos de `sgd_ssc` |
| **SA / NE** | Sugestão de alteração / necessidade (fórum) | sgsai `vw_forum_sa*`, `vw_sai*` | `public.sgd_sa`, `sgd_ssc_sa`, `sgd_sai_sane` |
| **Cliente** | Cliente, cidade, contrato, produto | `vw_geclientes`, `vw_gecidades`, `vw_geestados`, `vw_cmcontratos`, `vw_ceprodutos` | `public.sgd_client`, `sgd_product_client`, `sgd_product` |
| **Revenda / Unidade** | Filial ou revenda que atende | `vw_revendas` (`i_controle`) | `public.sgd_resale` |
| **Usuário** | Colaborador ou usuário do SGD | `power_bi.vw_usuarios`, `vw_usuarios_dados`, `vw_usuarios_auditoria` | `public.sgd_users` |
| **Alocação / Gestor / Cargo** | Histórico de equipe, gestor, cargo, horário | `vw_alocacao`, `vw_usuarios_alocacao_historico`, `vw_usuarios_gestor_historico`, `vw_usuarios_cargo_historico`, `vw_usuarios_horario_trabalho_historico` | `sgd_alocation_reg`, `sgd_alocation_historic`, `sgd_user_manager_historic`, `sgd_user_cargo_historico`, `sgd_horario_historic` |
| **Agenda** | Ausências, treinamentos, compromissos | `vw_agenda`, `vw_agenda_tipos`, `vw_agenda_motivos_ausencias`, `vw_feriados` | `sgd_schedule*`; **tempo real:** Dataflow `TB_SYBASE_SGD_AGENDA` |
| **Ocorrência** | Ocorrências internas (áreas, setores) | `vw_ocorrencia*` | `public.sgd_ocorrencia*`, DB_REPORTS_ANALITICOS `tb_ocorrencias_analitica` |
| **Implantação** | Implantação e treinamentos | `vw_externo*` | `externo.*` |
| **CTS / TRIA** | Base de soluções, pesquisas, chat IA | cts `vw_cts_*` | DB_CTS `public."CTS_*"`, `cts_*`, `tria.*` |

**Tabelas analíticas consolidadas** (DB_REPORTS_ANALITICOS, reconstruídas por jobs `historic-tb-*`):
- `tb_colaboradores`: quem estava ativo em cada dia, com cargo, alocação e supervisor. Chave `(data, id_usuario_sgd)`, também ligada por e-mail ao Genesys e ao WebChat.
- `tb_ocorrencias_analitica`
- `tb_demanda_lideres`

## 3. Joins e chaves

```sql
-- SSC → sistema / módulo / tópico / subtópico (chaves compostas)
FROM bethadba.vw_ssc ssc
JOIN bethadba.vw_sistemas s        ON s.i_sistemas = ssc.i_modulos_sistema
JOIN bethadba.vw_modulos m         ON m.i_sistemas = ssc.i_modulos_sistema AND m.i_modulos = ssc.i_modulos
JOIN bethadba.vw_topicos_suportes t ON t.i_sistemas = ssc.i_modulos_sistema AND t.i_modulos = ssc.i_modulos
                                   AND t.i_topicos_suportes = ssc.i_topicos_suportes
LEFT JOIN bethadba.vw_ssc_origens o ON o.i_topicos_suportes = ssc.i_topicos_suportes AND o.i_origens = ssc.i_origens  -- subtópico
```

| De | Para | Chave |
|---|---|---|
| SSC | trâmites | `vw_ssc_tramites.i_ssc = vw_ssc.i_ssc`; último = `MAX(i_ssc_tramites)`; ordem = `entrada`, `i_ssc_tramites` |
| SSC | situação / classificação | `i_ssc_situacoes`, `i_sss_classificacoes` |
| SSC | meio de acesso / retorno | `i_meios_acesso`, `i_meios_retorno` |
| SSC | SS / SSQL / conversão | `ssc.i_ss` ou `vw_ssc_ss(i_ssc, i_ss)`; `vw_ssc_ssql`; `vw_ssc_conversoes` |
| SSC | SA/NE | `ssc.i_forum_sa = forum_sa.i_controle` (banco sgsai) |
| SSC | revenda / cliente / responsável | `vw_revendas.i_controle = ssc.i_revendas`; `i_clientes`; `power_bi.vw_usuarios.i_usuarios = ssc.i_responsaveis` |
| SS | situação | `vw_ss_situacoes.i_ss_situacoes = vw_ss.situacao` (sistema em `ss.i_sistemas`) |
| Cliente | revenda | `geclientes.i_representantes = revendas.i_representantes` (com `ativa = 1`) |
| Cliente | cidade → estado | `gecidades.i_cidades` → `geestados.i_estados` |
| Contrato | histórico de usuários | `cmcontratos.i_contratos = cmcontratos_hist_usuarios.i_contratos` |
| Usuário | alocação vigente | `vw_alocacao.i_alocacao = uah.i_alocacao_nova`, com o histórico mais recente em que `apartir_de <= data` |
| Usuário | coordenador / gerente | `bethadba.f_get_gestor_suporte(i_usuarios)` dá o coordenador; aplicar duas vezes dá o gerente |
| Agenda | tipo / motivo | `agenda.i_tipos = agenda_tipos.i_agenda_tipos`; `agenda.i_motivos_ausencias = agenda_motivos_ausencias.i_agenda_motivos_ausencias` |
| Ocorrência | trâmites / pai | `ocorrencia.id = ocorrencia_tramite.i_ocorrencia`; `i_ocorrencia_pai = id` |
| SOSE | faturamento | `vw_ssc_dados_faturamentos.i_ssc = ssc.i_ssc` |

**Funções do Sybase** (liberadas):
- `bethadba.minutosuteis(1, ini, fim)`: minutos úteis entre duas datas.
- `f_get_gestor_suporte(i_usuarios)`: gestor do usuário.
- `f_get_tempo_pendente_ssc`
- `removerhtml`, `removerhtmleacentuacao`
- `relatoriotemporespostaanalitico(...)`: tempos de resposta da SSC.
- `sa_rowgenerator` (função de sistema): gera uma linha por dia.

No Postgres, os dias úteis vêm de `public.calendar`.

## 4. Códigos de negócio (Em revisão — extraídos do código)

### Situações de SSC (`i_ssc_situacoes`)
| Uso | Códigos |
|---|---|
| Sem análise (entrada no setor) | 1 |
| Em análise | 2, 14 |
| Aguardando resposta / negociação | 3, 19 |
| Aguardando resposta interna | 6 |
| Respondido interna | 7 |
| Pendente Domínio | 9 |
| Reprovação SA | 11 |
| Troca de responsável | 18 |
| Vínculo SA/NE | 9, 11, 12, 15, 16, 37 |
| Concluída / prescrita | 5, 10, 13, 17, 19, 37, 38, 43 |

### Pendência
- **Pendente:** `situacao_pendente_nivel_um = 1 OR situacao_pendente_nivel_dois = 1`.
- **N1 (regra batch, `sgd_pendency`/histórico):** nível um ≠ 0 e nível dois ≠ 1. **N2:** nível dois ≠ 0. **Setor:** `i_ssc_situacoes = 1`.
- **N1 (regra tempo real, SGSC):** `(situacao_pendente_geral = 1 OU responsavel_um = 0 OU responsavel_dois = 0) E situacao_pendente_nivel_um = 1`; N2 é independente do N1.
- ⚠️ **Duas regras de N1 em produção** (P-01, `negocio-perguntas-em-aberto.md`): o painel tempo real usa a regra SGSC, o histórico/`sgd_pendency` usa a regra batch. Os números **não batem** entre si até o time decidir se a regra do SGSC também deve valer para o histórico.
- **Corte do dia:** 18:00:59. Fim de semana excluído (`day_of_week NOT IN (1,7)`).

### Situações de SS (N2) por área
⚠️ **Três mapas divergentes** (P-06, `negocio-perguntas-em-aberto.md`): `ss_n2.py` (cadastro `pending`), `ss_n2.py` (`ss_pendency`) e `produtividade_pendencia_realtime/sql/queries.sql` não usam exatamente as mesmas listas. A tabela abaixo é o mapa do **realtime**; as diferenças conhecidas são: 25 é TI no realtime e N2 nos outros dois; 16/17 são COORD no realtime e N2 no batch; 26/27 são "DV INT" só no `ss_pendency`; 3,5,13,14,20,21 são N1 só no `ss_pendency`. Não use nenhum dos três como oficial sem citar qual foi usado.

| Área | Códigos (mapa realtime) |
|---|---|
| DV | 8, 11, 12 (DV INT = 26, 27) |
| GP | 6, 10, 29 |
| TI | 23, 24 |
| PAR | 31, 32 |
| N1 | 3, 5, 13, 14, 20, 21 |
| COORD (só no realtime) | 16, 17 |
| N2 | demais |
| Concluída | 5, 13, 14, 20, 21, 22 |

### Satisfação (`satisfacao`)
- **Valores:** 1–2 = Satisfeito · 3–4 = Insatisfeito · 0 = Não opinou.
- **Texto de conclusão:** só é considerado para satisfeitos. Textos 'OK' e 'OBRIGADO' e textos com `x00` são ignorados.

### Classificações (`i_sss_classificacoes`)
| Código | Classificação |
|---|---|
| 1 | Técnica |
| 4 | Conversão |
| 9 | Secundários |
| 10 | Funcional |
| 11 | Relatório |
| 12 | Domínio Web |
| 13 | Performance |
| 17, 18 | TR Digital Banking |
| 19 | ATEND-EXTERNO |

### Meios de acesso (`i_meios_acesso`)
| Código | Meio |
|---|---|
| 1 | Web |
| 2 | Telefone |
| 3 | Fax |
| 4 | e-Mail |
| 5 | SOSE |
| 6 | Chat |
| 9 | Ligações |
| 10 | Chat-Plug |

### Alocação → área (`i_alocacao`, conforme o Dataflow de agenda)
| Código | Área |
|---|---|
| 2, 3, 4, 11, 29, 30 | Técnica |
| 36 | Suporte Interno Técnico - Performance |
| 8, 10 | Apoio |
| 13, 60 | M.Aprendiz/Estagiário |
| 25, 26, 37, 38, 39 | Folha |
| 33 | Ausente (usa a alocação anterior, agenda) |
| 999 | Sem alocação |
| demais | ver o SQL completo em `dados-fluxo-tb_sybase_sgd_agenda.md` |

⚠️ **Mapa divergente na produtividade** (P-08, `negocio-perguntas-em-aberto.md`): o CASE de `produtividade_pendencia_realtime`/legado usa outra classificação para os mesmos códigos — ex.: 11 = "Coordenação" (agenda diz "Técnica"), 31 = "Técnica" (agenda diz "AT - Imp/Exp/Imp"), 33 = "Ausente" mesmo nome mas origem diferente. Cite qual mapa foi usado ao responder.

### Universo de regionais carregadas, exclusões e produtos
- **Revendas carregadas pelo ETL** (listas `REG_*` do `import-sgd`): 3, 4, 13, 14, 18, 40, 74, 83, 102, 137, 144, 155, 156, 160, 163, 165, mais a lista de revendas `REVENDAS_COM18`. ⚠️ Correção de 2026-09-29: essa lista define **quais revendas são importadas** e **não é a lista oficial de filiais**. Cada fonte tem a sua lista de filiais e o de-para revenda → regional diverge entre elas (a 144 aparece como Sul e como Campinas; a revenda 1 aparece como UPG, Sul ou CTD). Detalhes e citações em `negocio-conceitos.md` e `negocio-perguntas-em-aberto.md`. Tipos de revenda: Filiais / Revendas / UPG.
- **Exclusões fixas:**
  - revenda 112 (Televendas);
  - clientes 59827, 40580, 40581, 40579, 59879;
  - usuários 1280525, 1174250, 1220608.
- **Usuário interno:** `i_clientes IS NULL AND terceiro = 0 AND ativo = 1`. Para saber se estava ativo numa data, use o último registro de `vw_usuarios_auditoria`.
- **Produtos:**
  - principais (forecast): 101, 102, 103, 104, 170, 211, 212, 213;
  - para data de cadastro e assinatura: 101–104, 110, 170, 174, 190;
  - `vlr_contrato > 0`.
- **Ocorrências:**
  - `id = 4120` é excluída;
  - as situações 4, 5, 9 e 11 ficam fora do TMA.

### Janelas de carga
- ETL D-1 com deltas de 3, 5, 10, 15, 30, 60, 365 e 490 dias, conforme a tabela (ver `dados-postgres-destinos.md`).
- Datas de corte fixas no código: SOSE a partir de 2022-01-01, cargos a partir de 2024-01-01, prioridade de ocorrência a partir de 2026-05-01, horários a partir de 2026-08-01.

## 5. Como responder "qual tabela usar"
1. **Relatório novo, com dados até ontem.** Use a entidade do Dataflow (índice em `dados-fluxos-powerbi.md`). Se não houver entidade, use a tabela Postgres de destino (`dados-postgres-<base>.md`).
2. **Precisa do estado de agora no SGD** (agenda do dia, pendência atual). Use o Dataflow Sybase (agenda) ou o push dataset do Maestro (pendência e produtividade). SELECT novo no Sybase só com as views de `dados-sybase-colunas.md`.
3. **Indicador de colaborador por dia.** Parta de `DB_REPORTS_ANALITICOS.public.tb_colaboradores`, que já resolve ativo, cargo, alocação e gestor.
4. Sempre cite a origem (view Sybase → tabela Postgres → entidade do fluxo) e o job que atualiza. Assim quem usa sabe o quão atual o dado é.

## 6. Outras fontes de conhecimento
- `C:\GitHub\TR\sql-base\agente\` — dicionário de negócios, templates de queries e catálogos de produtos, revendas e treinamentos (foco em implantação, contratos e pós-venda).
- `analytics_bi_dominio-app-busca-tabelas` — explorador do catálogo Sybase e Postgres.
