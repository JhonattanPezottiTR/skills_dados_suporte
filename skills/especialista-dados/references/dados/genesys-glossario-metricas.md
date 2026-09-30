# Glossário DB_GENESYS × documentação oficial Genesys Cloud

> Última atualização: 2026-09-30 · Fonte: documentação oficial Genesys Cloud (`developer.genesys.cloud/api/rest/v2/analytics/metrics.html`, `help.genesys.cloud/articles/metric-definitions/`) cruzada com as colunas reais de `dados-fluxo-db_genesys.md` e `dados-postgres-db_genesys.md` · **Arquivo curado** · Status: **parcialmente confirmado** — ver coluna Confirmação.

## Como usar este arquivo
- Toda coluna `metric_*`/`_n*`/`_t*`/`_o*` do DB_GENESYS é uma métrica da **Genesys Cloud Analytics API** (endpoints `conversations/aggregates/query` e `conversations/details/query`, ver `dados-fluxos-maestro.md`), não um cálculo próprio do time — **nunca redefina o significado sem citar a doc oficial**.
- Antes de responder algo sobre DB_GENESYS, consulte a tabela §2 pelo nome da coluna. Se a linha estiver marcada **Em revisão**, avise o usuário que a definição não foi confirmada na documentação oficial (só inferida pelo nome/convenção).
- Prefixo `_` (ex.: `_tAnswered` em `genesys_callsAgentsHalfHour`) e prefixo `metric_` (ex.: `metric_tAnswered` em `genesys_historicCallsAgents`) são o **mesmo catálogo de métricas** — só mudam de nome entre entidades porque vêm de endpoints diferentes (aggregates vs. details) do mesmo Dataflow.

## 1. Convenção de prefixos (confirmado)
| Prefixo | Categoria | Estrutura no agregado |
|---|---|---|
| `n*` | Contador (counter) | só `count` |
| `t*` | Timer | `count`, `min`, `max`, `sum` (todos em **milissegundos**) — nas tabelas do time isso já vem achatado em colunas `*`, `*Max`, `*Min` |
| `o*` | Observação | a maioria é contador simples; **exceções:** `oServiceLevel` (`target`, `ratio`, `numerator`, `denominator`) e `oServiceTarget` (só `target`) |

## 2. Métricas e campos — nome real → definição oficial

| Coluna real (fluxo/Postgres) | Métrica/campo Genesys | Definição | Confirmação |
|---|---|---|---|
| `metric_nOffered` / `_nOffered` | `nOffered` | Contador de interações oferecidas à fila/agente. | Confirmado (developer.genesys.cloud/metrics) |
| `metric_tAcd` / `_tAcd` | `tAcd` | Tempo em fila esperando até ser atendida, abandonada ou sair da fila (flow out). | Confirmado |
| `metric_tAlert` / `_nAlert`/`_tAlert` | `tAlert` | Tempo em que o agente está sendo alertado (telefone chamando) sobre a interação, antes de atender. | Confirmado |
| `metric_tTalk` / `_tTalkComplete` | `tTalk` / `tTalkComplete` | Tempo conectado falando com o cliente. `tTalkComplete` é a versão "uma linha por conversa completa" (equivalente a `tTalk` agregado). | Confirmado |
| `metric_tHeld` / `_tHeldComplete` | `tHeld` / `tHeldComplete` | Tempo em espera (hold). `tHeld` conta por segmento de hold dentro da conversa; `tHeldComplete` soma uma vez por conversa inteira. | Confirmado |
| `metric_tAcw` / `_tAcw` / `_nAcw` | `tAcw` | Tempo em after-call work (finalização/anotação pós-atendimento). | Confirmado |
| `metric_tIvr` | `tIvr` | Tempo que a interação passou sendo processada pela URA (IVR), antes de chegar à fila/agente. | Confirmado |
| `metric_tHandle` / `_tHandle` | `tHandle` | Métrica composta: fala + hold + ACW (e, em outbound, + discagem/contato). Timestamp registrado no fim do ACW. | Confirmado |
| `metric_oServiceLevel` / `_oServiceLevel` | `oServiceLevel` | Nível de serviço da fila: `target` (meta, ex.: 80% em 20s), `ratio` (percentual realizado), `numerador`/`denominador` (interações dentro da meta / total). Nas colunas do time normalmente já vem como o `ratio` (percentual). | Confirmado (estrutura); **conferir com o time** se a coluna achatada é ratio ou numerador — não confirmado qual campo específico o ETL grava |
| `metric_oServiceTarget` | `oServiceTarget` | Só a meta (target) de SLA configurada na fila (ex.: 80). | Confirmado |
| `metric_tAnswered` / `_tAnswered` | `tAnswered` | Tempo entre a interação chegar na fila/ser oferecida e ser atendida por um agente (tempo de espera até atender) — usada no time como base do SLA de voz (ver `sla_txt` no SQL de `genesys_historicCallsAgents`). | **Em revisão** — página oficial não confirmada por fetch estático nesta rodada; definição acima é a mais consistente com o uso no SQL do time (faixas de SLA) e com fontes secundárias, mas não foi lida diretamente na doc developer.genesys.cloud |
| `metric_tAbandon` / `_tAbandon` | `tAbandon` | Tempo que a interação esperou antes do cliente desistir (abandonar) a chamada. | **Em revisão** |
| `metric_tWait` / `_tWait` | `tWait` | Tempo de espera (uso genérico; distinto de `tAcd` em alguns relatórios da Genesys — checar se aqui é sinônimo de `tAcd` ou de espera pós-fila). | **Em revisão** |
| `metric_tContacting` / `_tContacting` | `tContacting` | Tempo entre o disparo do outbound e o contato ser estabelecido (discagem em campanhas). | **Em revisão** |
| `metric_tDialing` / `_tDialing` | `tDialing` | Tempo de discagem (outbound), antes do `tContacting`. | **Em revisão** |
| `metric_tMonitoring` / `_tMonitoring` | `tMonitoring` | Tempo que um supervisor passou monitorando a interação. | **Em revisão** |
| `metric_tVoicemail` | `tVoicemail` | Tempo/registro de correio de voz deixado pelo cliente. | **Em revisão** |
| `metric_tFlowOut` / `_tFlowOut` | `tFlowOut` | Tempo até a interação saltar (flow out) da fila/fluxo sem ser atendida nem abandonada explicitamente (ex.: desconectada pelo IVR). | **Em revisão** |
| `metric_tShortAbandon` / `_tShortAbandon` | `tShortAbandon` | Abandono "curto": cliente desiste em poucos segundos (o `aband_txt` do SQL usa faixa `<= 8000ms` como "Immediate", possivelmente o corte de short abandon). | **Em revisão** |
| `metric_nConnected` / `_nConnected` | `nConnected` | Contador de interações efetivamente conectadas a um agente. | **Em revisão** |
| `metric_nOverSla` / `_nOverSla` | `nOverSla` | Contador de interações que ficaram fora da meta de SLA (excedeu o `oServiceTarget`). | **Em revisão** |
| `metric_nTransferred` / `_nTransferred` | `nTransferred` | Contador de interações transferidas. | **Em revisão** |
| `metric_nBlindTransferred` / `_nBlindTransferred` | `nBlindTransferred` | Contador de transferências "às cegas" (sem consulta prévia). | **Em revisão** |
| `metric_nConsultTransferred` / `_nConsultTransferred` | `nConsultTransferred` | Contador de transferências feitas após consulta (o agente falou com o destino antes de transferir). | **Em revisão** |
| `metric_nConsult` / `_nConsult` | `nConsult` | Contador de consultas (conferência antes de transferir) iniciadas. | **Em revisão** |
| `metric_nOutboundAttempted` / `_nOutboundAttempted`/`_nOutbound` | `nOutboundAttempted` | Contador de tentativas de contato outbound (discagem em campanha). | **Em revisão** |
| `metric_oMediaCount` / `_oMediaCount` | `oMediaCount` | Contador de interações por tipo de mídia. **Nota:** `perguntas-em-aberto.md` Q-14 já registra que esta coluna grava sempre 0 no time (bug/TODO reg. 0221) — não usar para métrica publicada sem confirmar. | **Em revisão** (e com bug conhecido, Q-14) |
| `metric_oExternalMediaCount` / `_oExternalMediaCount` | `oExternalMediaCount` | Mesma observação de `oMediaCount`, para mídia externa. Também sempre 0 (Q-14). | **Em revisão** (e com bug conhecido, Q-14) |
| `metric_nNotResponding` / `_nNotResponding` | `nNotResponding` | Contador de vezes que o agente não respondeu ao alerta (interação perdida pelo agente). | **Em revisão** |
| `metric_tNotResponding` / `_tNotResponding` | `tNotResponding` | Tempo em que a interação ficou tocando sem resposta do agente antes de ser redirecionada. | **Em revisão** |
| `mediaType` | `mediaType` | Tipo de mídia da interação (voice, chat, email...). Não aparece como coluna própria nas entidades lidas (o Dataflow já filtra/assume voz na maioria); confirmar se existe em alguma entidade não mapeada aqui. | **Em revisão** |
| `direction` | `direction` | Direção da interação: inbound/outbound. | Confirmado (nome autoexplicativo, uso direto no SQL: `and direction = 'inbound'`) |
| `purpose` | `purpose` | Papel/propósito do participante na interação (ex.: agent, customer, ivr, acd). | **Em revisão** |
| `disconnecttype` / `disconnecttype_out` | `disconnectType` | Como a interação foi desconectada (client, agent, transfer, system...). | **Em revisão** |
| `wrapupcode` | `wrapUpCode` | Código de finalização (motivo) escolhido pelo agente ao fim da chamada — de-para em `routing/wrapupcodes` (`genesys_import`, ver `dados-fluxos-maestro.md`). | Confirmado (origem do endpoint) |
| `_ani` / `_dnis` | `ani` / `dnis` | `ani` = número de origem (quem chamou); `dnis` = número discado (destino). Convenção padrão de telefonia, usada como está na Genesys. | Confirmado (convenção de telefonia padrão) |
| `bullseye` | `bullseye` | Anel (ring) do algoritmo de roteamento Bullseye no momento da interação — quanto maior, mais a busca por agente já expandiu além da skill/fila original (ver uso em `skill_id_2`/`removed_skill` no SQL de `genesys_historicCallsAgents`). | Confirmado (comportamento consistente com o SQL do time) |
| `skill_id_1` / `skill_id_2` / `removed_skill` | — | IDs de skill roteados/removidos durante o Bullseye; não são métricas Genesys, são atributos da conversa. | Confirmado (estrutural, não precisa de doc externa) |

## 3. Como usar num BI de Genesys

| Indicador de negócio | Métrica Genesys | Observação |
|---|---|---|
| **SLA de voz** | `oServiceLevel` (ratio/target) — mas o time hoje calcula via faixas de `metric_tAnswered` (`sla`/`sla_txt` no SQL de `genesys_historicCallsAgents`) | ⚠️ **Divergência a validar:** `negocio/conceitos.md` (linhas ~411-413) descreve SLA por faixas de `tAnswered`/`tTalk`, não pelo `oServiceLevel` nativo da Genesys. Perguntar ao time: o SLA publicado deve usar o `oServiceLevel` oficial (ratio vs. meta) ou continuar com o corte manual em `tAnswered`? Registrado como novo item a levar ao time (ver `perguntas-em-aberto.md`). |
| **TMA / AHT (tempo médio de atendimento)** | `tHandle` | Já é a métrica composta oficial (fala + hold + ACW); não recalcular somando `tTalk`+`tHeld`+`tAcw` manualmente quando `tHandle` já existir na fonte. |
| **TME (tempo médio de espera/fila)** | `tAcd` (tempo em fila) — distinto do `TME`/`TFM` do chat/Plug, que é outra métrica (`glossario.md`) | Não confundir: TME "de voz" (Genesys, `tAcd`) ≠ TME do Plug/chat (`tempo de espera médio`, tabela `plug_queue_realtime`). |
| **Abandono** | `tAbandon` (tempo até abandonar) / `nOffered` − `nConnected` (contagem) | Definição de `tAbandon` ainda **Em revisão** — usar com essa ressalva. |
| **Transferências** | `nTransferred` = `nBlindTransferred` + `nConsultTransferred` (esperado, não confirmado na doc) | Verificar essa soma contra os dados antes de publicar um número fechado. |

## 4. Limitações desta rodada
- As páginas `developer.genesys.cloud/api/rest/v2/analytics/metrics.html` e `conversation_detail_model.html` são SPAs renderizadas em JavaScript — não foi possível ler o corpo completo via fetch estático nesta sessão. As definições **Confirmado** vieram de buscas (WebSearch) com trechos citáveis da documentação oficial; as **Em revisão** são inferidas pelo nome/convenção e pelo uso no SQL do time, não por leitura direta da página oficial.
- Próxima tentativa recomendada para fechar as pendências: o Swagger/OpenAPI público da Analytics API (texto puro, ex.: `api.mypurecloud.com/api/v2/docs/...` ou o spec no GitHub `purecloudlabs/platform-client-sdk-common`), que não é JS-rendered.
