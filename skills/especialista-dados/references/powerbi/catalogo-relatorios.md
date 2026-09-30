# Catálogo de relatórios Power BI

> Última atualização: 2026-09-30 · Fonte: arquivos PBIP/PBIR lidos por `scripts/mapear_powerbi.py` (pastas em `fontes/powerbi/` e `config/fontes-powerbi.txt`)
> **Gerado automaticamente** — não editar à mão. Contexto de negócio de cada BI: `powerbi-tipos-de-bi.md`.

## Visão geral

| Relatório | Modo | Workspace | Dataset | Job do Maestro que alimenta | Páginas | Medidas do relatório |
|---|---|---|---|---|---|---|
| **_genesysQueue** | Live connection (dataset publicado) | Dashboard - Real Time | `_genesysQueue` | genesys-queue-realtime | 3 | 0 |
| **_genesysQueueSLA** | Live connection (dataset publicado) | Dashboard - Real Time | `_genesysQueueSLA` | genesys-sla | 12 | 8 |
| **_genesysSGD_Productivity** | Live connection (dataset publicado) | Dashboard - Real Time | `_genesysSGD_Productivity` | produtividade-pendencia-realtime | 5 | 5 |
| **_sgdPendency** | Live connection (dataset publicado) | Dashboard - Real Time | `_sgdPendency` | produtividade-pendencia-realtime | 8 | 6 |
| **Acompanhamento Tempo Real Fone_v2.1** | Live connection (dataset publicado) | Dashboard - Real Time | `_genesysNotReady` | genesys-sla | 3 | 42 |
| **Real Time projetado** | Modelo local (PBIP) | — | `Real Time projetado` | — | 3 | 0 |

Push datasets (live connection) têm uma única tabela `RealTimeData`, cujas colunas são definidas pelo job que envia as linhas. Mudar uma coluna exige alterar o job **e** o dataset.

## _genesysQueue

- **Modo:** Live connection (dataset publicado) · **Workspace:** Dashboard - Real Time · **Dataset:** `_genesysQueue`
- **Alimentado por:** genesys-queue-realtime
- **Tema:** `Custom6681574776390331.json` — ⚠️ difere do tema oficial (COR-001)
- **Cópias encontradas:** 1

### Páginas

| Página | Visuais | Campos usados |
|---|---|---|
| Tiago Antunes - SGD | tableEx×1 | `RealTimeData[nWait]`, `RealTimeData[nameSkill_SGD_1]`, `RealTimeData[tWaiting]` |
| Maior Espera | card×3 | `RealTimeData[tWaiting]` |
| Duplicata de Tiago Antunes - SGD | tableEx×1 | `RealTimeData[atendendo_a_fila]`, `RealTimeData[ativos_na_fila]`, `RealTimeData[fora_da_fila]`, `RealTimeData[membros_da_fila]`, `RealTimeData[nWait]`, `RealTimeData[nameSkill_SGD_1]`, `RealTimeData[nameSkill_SGD_2]`, `RealTimeData[tWaiting]` |

## _genesysQueueSLA

- **Modo:** Live connection (dataset publicado) · **Workspace:** Dashboard - Real Time · **Dataset:** `_genesysQueueSLA`
- **Alimentado por:** genesys-sla
- **Tema:** `Custom03565331006295214.json` — ⚠️ difere do tema oficial (COR-001)
- **Cópias encontradas:** 1

### Páginas

| Página | Visuais | Campos usados |
|---|---|---|
| SLA by Skill | tableEx×2 | `RealTimeData[AbandonedAfter_3min] (medida)`, `RealTimeData[AbandonedUntil_3min] (medida)`, `RealTimeData[SLA] (medida)`, `RealTimeData[metric_nAbandon]`, `RealTimeData[metric_nOffered]`, `RealTimeData[metric_oServiceLevel]`, `RealTimeData[time_interval]` |
| SLA  by Skill Total | tableEx×1 | `RealTimeData[SLA] (medida)`, `RealTimeData[metric_nAbandon]`, `RealTimeData[metric_nOffered]`, `RealTimeData[nameQueue]` |
| Filas Funcionais | card×2, tableEx×6 | `RealTimeData[%Abandonadas] (medida)`, `RealTimeData[HoraComoTexto] (medida)`, `RealTimeData[SLA] (medida)`, `RealTimeData[TME(HH:MM:SS)] (medida)`, `RealTimeData[hora_ultimoEnvio]`, `RealTimeData[metric_nOffered]`, `RealTimeData[nameQueue]` |
| Filas FOLHA - Mês | card×1, tableEx×4 | `RealTimeData[%Abandonadas] (medida)`, `RealTimeData[SLA] (medida)`, `RealTimeData[TME(HH:MM:SS)] (medida)`, `RealTimeData[date_interval]`, `RealTimeData[hora_ultimoEnvio]`, `RealTimeData[metric_nOffered]`, `RealTimeData[nameQueue]` |
| Filas FOLHA - GERAL | card×1, tableEx×2 | `RealTimeData[%Abandonadas] (medida)`, `RealTimeData[SLA] (medida)`, `RealTimeData[TME(HH:MM:SS)] (medida)`, `RealTimeData[date_interval]`, `RealTimeData[hora_ultimoEnvio]`, `RealTimeData[metric_nOffered]`, `RealTimeData[nameQueue]` |
| Filas FISCONT  - Mês | card×1, tableEx×4 | `RealTimeData[%Abandonadas] (medida)`, `RealTimeData[SLA] (medida)`, `RealTimeData[TME(HH:MM:SS)] (medida)`, `RealTimeData[date_interval]`, `RealTimeData[hora_ultimoEnvio]`, `RealTimeData[metric_nOffered]`, `RealTimeData[nameQueue]` |
| Filas FISCONT - GERAL | card×1, tableEx×2 | `RealTimeData[%Abandonadas] (medida)`, `RealTimeData[SLA] (medida)`, `RealTimeData[TME(HH:MM:SS)] (medida)`, `RealTimeData[date_interval]`, `RealTimeData[hora_ultimoEnvio]`, `RealTimeData[metric_nOffered]`, `RealTimeData[nameQueue]` |
| Filas AT - Mês | card×1, tableEx×4 | `RealTimeData[%Abandonadas] (medida)`, `RealTimeData[SLA] (medida)`, `RealTimeData[TME(HH:MM:SS)] (medida)`, `RealTimeData[date_interval]`, `RealTimeData[hora_ultimoEnvio]`, `RealTimeData[metric_nOffered]`, `RealTimeData[nameQueue]` |
| Filas AT - GERAL | card×1, tableEx×2 | `RealTimeData[%Abandonadas] (medida)`, `RealTimeData[SLA] (medida)`, `RealTimeData[TME(HH:MM:SS)] (medida)`, `RealTimeData[date_interval]`, `RealTimeData[hora_ultimoEnvio]`, `RealTimeData[metric_nOffered]`, `RealTimeData[nameQueue]` |
| Filas a cada 30min | card×1, tableEx×3 | `RealTimeData[%Abandonadas] (medida)`, `RealTimeData[SLA] (medida)`, `RealTimeData[TME(HH:MM:SS)] (medida)`, `RealTimeData[hora_ultimoEnvio]`, `RealTimeData[metric_nOffered]`, `RealTimeData[time_interval]` |
| Fila AT | card×1, tableEx×3 | `RealTimeData[%Abandonadas] (medida)`, `RealTimeData[SLA] (medida)`, `RealTimeData[TME(HH:MM:SS)] (medida)`, `RealTimeData[metric_nOffered]`, `RealTimeData[nameQueue]`, `RealTimeData[time_interval]` |
| Página 1 | — | — |

### Medidas definidas no relatório

**AbandonedAfter_3min** (tabela `RealTimeData` · formato `General Number`)

```dax
coalesce(sum(RealTimeData[metric_tAbandon300])+sum(RealTimeData[metric_tAbandon600])+sum(RealTimeData[metric_tAbandonMore600]),0)
```

**SLA** (tabela `RealTimeData` · formato `0.00\ %;-0.00\ %;0.00\ %`)

```dax
if ( (sum(RealTimeData[metric_nOffered]) - RealTimeData[AbandonedUntil_3min]) <=0,0,calculate(sum(RealTimeData[metric_oServiceLevel]) / (sum(RealTimeData[metric_nOffered]) - RealTimeData[AbandonedUntil_3min]) ))
```

**AbandonedUntil_3min** (tabela `RealTimeData` · formato `General Number`)

```dax
coalesce(sum(RealTimeData[metric_tAbandon60])+sum(RealTimeData[metric_tAbandon120])+sum(RealTimeData[metric_tAbandon180]),0)
```

**SLA_numero** (tabela `RealTimeData` · formato `0.000`)

```dax
if ( (sum(RealTimeData[metric_nOffered]) - RealTimeData[AbandonedUntil_3min]) <=0,0,calculate(sum(RealTimeData[metric_oServiceLevel]) / (sum(RealTimeData[metric_nOffered]) - RealTimeData[AbandonedUntil_3min]) ))
```

**tme_decimal** (tabela `RealTimeData` · formato `0.0000`)

```dax
if ( sum(RealTimeData[metric_nAnswered]) <=0,0,
CALCULATE((sum(RealTimeData[metric_tAnswered])/1000 / sum(RealTimeData[metric_nAnswered]))/3600) )
```

**TME(HH:MM:SS)** (tabela `RealTimeData` · formato `00\:00\:00`)

```dax
VAR vHorasDecimal = RealTimeData[tme_decimal]
VAR vHoras = INT(vHorasDecimal)
VAR vMinutosDecimal = 60 * (vHorasDecimal - vHoras)
VAR vMinutos = INT(vMinutosDecimal)
VAR vSegundos = INT( 60 * (vMinutosDecimal - vMinutos) )
VAR vHH = IF(LEN(vHoras) = 1, "0" & vHoras, vHoras)
VAR vMM = IF(LEN(vMinutos) = 1, "0" & vMinutos, vMinutos)
VAR vSS = IF(vSegundos > 0, IF(LEN(vSegundos) = 1, "0" & vSegundos, vSegundos), "00") 
RETURN
CONVERT(vHH&vMM&vSS, INTEGER)
```

**%Abandonadas** (tabela `RealTimeData` · formato `0.00\ %;-0.00\ %;0.00\ %`)

```dax
coalesce(CALCULATE(sum(RealTimeData[metric_nAbandon]) / sum(RealTimeData[metric_nOffered])),0)
```

**HoraComoTexto** (tabela `RealTimeData` · formato `Long Time`)

```dax
FORMAT(max(RealTimeData[hora_ultimoEnvio]), "HH:mm:ss")
```


## _genesysSGD_Productivity

- **Modo:** Live connection (dataset publicado) · **Workspace:** Dashboard - Real Time · **Dataset:** `_genesysSGD_Productivity`
- **Alimentado por:** produtividade-pendencia-realtime
- **Tema:** tema base do Power BI — ⚠️ sem tema oficial aplicado (COR-001)
- **Cópias encontradas:** 2

### Páginas

| Página | Visuais | Campos usados |
|---|---|---|
| Dash | tableEx×1 | `RealTimeData[alocacao]`, `RealTimeData[colaborador]`, `RealTimeData[coordenador]`, `RealTimeData[gerente]`, `RealTimeData[setor]`, `RealTimeData[total_ligacoes]`, `RealTimeData[total_novas]`, `RealTimeData[total_plug_protocol]`, `RealTimeData[total_semResposta]`, `RealTimeData[total_tramitadas]`, `RealTimeData[unidade]` |
| Dash 2 | tableEx×1 | `RealTimeData[atendidas - transferidas] (medida)`, `RealTimeData[colaborador]`, `RealTimeData[coordenador]`, `RealTimeData[novasWeb+Ligacoes] (medida)`, `RealTimeData[total_ligacoes]`, `RealTimeData[total_novas]`, `RealTimeData[total_novas_web]`, `RealTimeData[total_plug_protocol]`, `RealTimeData[total_semResposta]`, `RealTimeData[total_tramitadas]`, `RealTimeData[total_transferidas]` |
| Aquario | Aquarium1442671919391×3 | `RealTimeData[colaborador]`, `RealTimeData[total_ligacoes]`, `RealTimeData[total_novas]`, `RealTimeData[total_tramitadas]` |
| Página 1 | slicer×1, tableEx×1 | `RealTimeData[alocacao]`, `RealTimeData[colaborador]`, `RealTimeData[coordenador]`, `RealTimeData[gerente]`, `RealTimeData[total_ligacoes]`, `RealTimeData[total_novas]`, `RealTimeData[total_semResposta]`, `RealTimeData[total_tramitadas]` |
| Dash PLUG | tableEx×1 | `RealTimeData[alocacao]`, `RealTimeData[colaborador]`, `RealTimeData[coordenador]`, `RealTimeData[gerente]`, `RealTimeData[novasWeb+Ligacoes(atendidas-transferidas)+PLUG] (medida)`, `RealTimeData[setor]`, `RealTimeData[total_ligacoes]`, `RealTimeData[total_novas_web]`, `RealTimeData[total_plug_protocol]`, `RealTimeData[total_semResposta]`, `RealTimeData[unidade]` |

### Medidas definidas no relatório

**novasWeb+Ligacoes** (tabela `RealTimeData` · formato `0.00`)

```dax
calculate(sum(RealTimeData[total_novas_web])+sum(RealTimeData[total_ligacoes]))
```

**atendidas - transferidas** (tabela `RealTimeData` · formato `0.00`)

```dax
coalesce(calculate(sum(RealTimeData[total_ligacoes]) - sum(RealTimeData[total_transferidas])),0)
```

**novasWeb+Ligacoes(atendidas-transferidas)** (tabela `RealTimeData` · formato `General Number`)

```dax
coalesce(calculate(sum(RealTimeData[total_novas_web])+[atendidas - transferidas]),0)
```

**novasWeb+Ligacoes+Plug** (tabela `RealTimeData` · formato `General Number`)

```dax
calculate(sum(RealTimeData[total_novas_web])+sum(RealTimeData[total_ligacoes])+sum(RealTimeData[total_plug_protocol]))
```

**novasWeb+Ligacoes(atendidas-transferidas)+PLUG** (tabela `RealTimeData` · formato `General Number`)

```dax
coalesce(calculate(sum(RealTimeData[total_novas_web])+[atendidas - transferidas] + sum(RealTimeData[total_plug_protocol])),0)
```


## _sgdPendency

- **Modo:** Live connection (dataset publicado) · **Workspace:** Dashboard - Real Time · **Dataset:** `_sgdPendency`
- **Alimentado por:** produtividade-pendencia-realtime
- **Tema:** tema base do Power BI — ⚠️ sem tema oficial aplicado (COR-001)
- **Cópias encontradas:** 1

### Páginas

| Página | Visuais | Campos usados |
|---|---|---|
| Dashboard | slicer×1, tableEx×5 | `RealTimeData[Prioridade Calculada] (medida)`, `RealTimeData[Ultimo Sem Análise] (medida)`, `RealTimeData[assunto]`, `RealTimeData[classificacao]`, `RealTimeData[coordenador]`, `RealTimeData[entrada]`, `RealTimeData[i_ssc (Sem analise)] (medida)`, `RealTimeData[i_ssc]`, `RealTimeData[n1] (medida)`, `RealTimeData[n2] (medida)`, `RealTimeData[prioridade]`, `RealTimeData[situacao]`, `RealTimeData[tecnico]`, `RealTimeData[ulti_tramite]` |
| Página 1 | tableEx×1 | `RealTimeData[assunto]`, `RealTimeData[entrada]`, `RealTimeData[tecnico]` |
| Detail | image×1, slicer×4, tableEx×1 | `RealTimeData[assunto]`, `RealTimeData[classificacao]`, `RealTimeData[coordenador]`, `RealTimeData[meio_acesso]`, `RealTimeData[modulo]`, `RealTimeData[sistema]`, `RealTimeData[situacao]`, `RealTimeData[tecnico]`, `RealTimeData[topico]`, `RealTimeData[ulti_tramite]` |
| Página 2 | pivotTable×1 | `RealTimeData[classificacao]`, `RealTimeData[n1] (medida)`, `RealTimeData[tecnico]` |
| PendênciasAgenda | tableEx×1 | `RealTimeData[Prioridade Calculada] (medida)`, `RealTimeData[agenda]`, `RealTimeData[n1] (medida)`, `RealTimeData[n2] (medida)`, `RealTimeData[tecnico]` |
| PendenciaUnidade | pivotTable×1 | `RealTimeData[n1] (medida)`, `RealTimeData[tecnico]`, `RealTimeData[unidade]` |
| ECD | image×1, slicer×4, tableEx×1 | `RealTimeData[assunto]`, `RealTimeData[classificacao]`, `RealTimeData[coordenador]`, `RealTimeData[meio_acesso]`, `RealTimeData[modulo]`, `RealTimeData[situacao]`, `RealTimeData[tecnico]`, `RealTimeData[topico]`, `RealTimeData[ulti_tramite]` |
| Duplicata de Dashboard | slicer×1, tableEx×5 | `RealTimeData[Prioridade Calculada] (medida)`, `RealTimeData[Ultimo Sem Análise] (medida)`, `RealTimeData[assunto]`, `RealTimeData[classificacao]`, `RealTimeData[coordenador]`, `RealTimeData[entrada]`, `RealTimeData[i_ssc (Sem analise)] (medida)`, `RealTimeData[i_ssc]`, `RealTimeData[n1] (medida)`, `RealTimeData[n2] (medida)`, `RealTimeData[prioridade]`, `RealTimeData[tecnico]`, `RealTimeData[ulti_tramite]` |

### Medidas definidas no relatório

**Ultimo Sem Análise** (tabela `RealTimeData` · formato `Short Date`)

```dax
IF( CALCULATE(min(RealTimeData[ulti_tramite]),RealTimeData[situacao] = "Sem Análise") = BLANK(),"Não há Sem Análise",
 CALCULATE(min(RealTimeData[ulti_tramite])-0.125,RealTimeData[situacao] = "Sem Análise"))
```

**Prioridade Calculada** (tabela `RealTimeData`)

```dax
var data = max(RealTimeData[DataHora])
return CALCULATE(count(RealTimeData[i_ssc]),RealTimeData[DataHora] = data, RealTimeData[prioridade] = "Sim")
```

**n1** (tabela `RealTimeData`)

```dax
SUM(RealTimeData[n1_pendency])
```

**n2** (tabela `RealTimeData`)

```dax
SUM(RealTimeData[n2_pendency])
```

**i_ssc (Sem analise)** (tabela `RealTimeData`)

```dax
CALCULATE(DISTINCTCOUNT(RealTimeData[i_ssc]), RealTimeData[situacao]="Sem Análise")
```

**Cor Analistas** (tabela `RealTimeData`)

```dax
VAR Nome = MAX('RealTimeData'[tecnico])

RETURN
IF(
    Nome IN {
        "Ana Carolina Gonçalves Ming",
        "Anna Flavia Lisboa Albano",
        "Antonio Bozzani",
        "Caick Dias Silva",
        "Cibele de Miranda Correia",
        "Deborah Liath Pellicer",
        "Eder Lúcio Carvalho dos Santos",
        "Felipe Costa Martins",
        "Gabriel Clodoaldo Souza",
        "Gabriel de Souza Custodio Vicentini",
        "Gabriela Luiza dos Santos Ruas",
        "Gessiany Oliveira",
        "Gilmar da Costa Figueiredo",
        "Ieremis Gabriel Bonini da Silva",
        "Jaqueline Campos da Silva",
        "Joyce Cavalcante",
        "Júlia Piotto da Silva",
        "Kauã Barbetta",
        "Larissa Chariel Correa",
        "Leticia Guimarães do Nascimento Sousa",
        "Marcelo Henrique Crescencio",
        "Mayane Pinheiro",
        "Natália Groff",
        "Thais Assumpção Santos Souza da Silva",
        "Vitória Domingues Cardoso",
        "William Correa Bezerra",
        "Marcelo Lorent Simione",
        "Nicolly Salla",
        "Giovana Pereira",
        "Beatriz Lustosa",
        "Elpidio Soares Junior",
        "Deiziane Oliveira de Azevedo",
        "Paloma Pereira Sousa",
        "Danzel Souza Cruz",
        "Eduardo Gardinal",
        "Jefferson Fais",
        "Rosilene da Silva",
        "STHEFANI DUARTE WILLMAN RAMOS",
        "Raissa Vichineski de Oliveira Milani",
        "Thais Miranda",
        "Evelyn Ribeiro Viana",
        "Milena Hilara",
        "Urai Silva Marques de Souza",
        "Artur de Souza Silva",
        "Giani Afonso da Silva",
        "Evandro Neves dos Santos",
        "Felipe dos Santos Nieto",
        "Daniel Favero de Albuquerque",
        "Daline Meireles Muller",
        "Jasminy Oliveira"
    },
    "#00B050",
    "#FFFFFF"
)
```


## Acompanhamento Tempo Real Fone_v2.1

- **Modo:** Live connection (dataset publicado) · **Workspace:** Dashboard - Real Time · **Dataset:** `_genesysNotReady`
- **Alimentado por:** genesys-sla
- **Tema:** tema base do Power BI — ⚠️ sem tema oficial aplicado (COR-001)
- **Cópias encontradas:** 1

### Páginas

| Página | Visuais | Campos usados |
|---|---|---|
| NotReady | tableEx×3 | `RealTimeData[%notReady] (medida)`, `RealTimeData[coordenador]`, `RealTimeData[interval]`, `RealTimeData[name]` |
| Tempo Real Fone_Eloiza | card×1, image×1, pivotTable×1, slicer×2 | `RealTimeData[Ultima Atualização_Hora] (medida)`, `RealTimeData[alocation]`, `RealTimeData[coordenador]`, `RealTimeData[gerente]`, `RealTimeData[name]`, `RealTimeData[novo_indicador_tempo_falado] (medida)`, `RealTimeData[novo_tempo_ausente] (medida)`, `RealTimeData[novo_tempo_conectado] (medida)`, `RealTimeData[novo_tempo_disponivel] (medida)`, `RealTimeData[novo_tempo_forafila] (medida)`, `RealTimeData[novo_tempo_interacao] (medida)`, `RealTimeData[novo_tempo_meta] (medida)`, `RealTimeData[novo_tempo_nafila] (medida)`, `RealTimeData[novo_tempo_ocioso] (medida)`, `RealTimeData[novo_tempo_ocupado] (medida)`, `RealTimeData[novo_tempo_pausa] (medida)`, `RealTimeData[novo_tempo_refeicao] (medida)`, `RealTimeData[novo_tempo_reuniao] (medida)`, `RealTimeData[novo_tempo_treinamento] (medida)` |
| Duplicata de Tempo Real Fone_Eloiza | card×1, image×1, slicer×2, tableEx×1 | `RealTimeData[Ultima Atualização_Hora] (medida)`, `RealTimeData[alocation]`, `RealTimeData[coordenador]`, `RealTimeData[gerente]`, `RealTimeData[name]`, `RealTimeData[novo_indicador_tempo_falado] (medida)`, `RealTimeData[novo_tempo_ausente] (medida)`, `RealTimeData[novo_tempo_conectado] (medida)`, `RealTimeData[novo_tempo_disponivel] (medida)`, `RealTimeData[novo_tempo_forafila] (medida)`, `RealTimeData[novo_tempo_interacao] (medida)`, `RealTimeData[novo_tempo_meta] (medida)`, `RealTimeData[novo_tempo_nafila] (medida)`, `RealTimeData[novo_tempo_ocioso] (medida)`, `RealTimeData[novo_tempo_ocupado] (medida)`, `RealTimeData[novo_tempo_pausa] (medida)`, `RealTimeData[novo_tempo_refeicao] (medida)`, `RealTimeData[novo_tempo_reuniao] (medida)`, `RealTimeData[novo_tempo_treinamento] (medida)` |

### Medidas definidas no relatório

**DacTotal_decimal** (tabela `RealTimeData`)

```dax
COALESCE(CALCULATE(sum(RealTimeData[idle])+sum(RealTimeData[interacting]))/1000/3600,0)
```

**disponivel_decimal** (tabela `RealTimeData`)

```dax
COALESCE(CALCULATE(sum(RealTimeData[available]))/1000/3600,0)
```

**foraFila_decimal** (tabela `RealTimeData`)

```dax
COALESCE(CALCULATE(sum(RealTimeData[available])+sum(RealTimeData[busy])+sum(RealTimeData[away]) + 
sum (RealTimeData[break]) + sum(RealTimeData[meal]) + sum(RealTimeData[meeting] ))/1000/3600,0)
```

**naFila_decimal** (tabela `RealTimeData`)

```dax
COALESCE(CALCULATE(sum(RealTimeData[on_queue]))/1000/3600,0)
```

**naoRespondendo_decimal** (tabela `RealTimeData`)

```dax
COALESCE(CALCULATE(sum(RealTimeData[not_responding]))/1000/3600,0)
```

**ocioso_decimal** (tabela `RealTimeData`)

```dax
COALESCE(CALCULATE(sum(RealTimeData[idle]))/1000/3600,0)
```

**treinamento_decimal** (tabela `RealTimeData`)

```dax
COALESCE(CALCULATE(sum(RealTimeData[training]))/1000/3600,0)
```

**%notReady** (tabela `RealTimeData` · formato `0.00\ %;-0.00\ %;0.00\ %`)

```dax
VAR vConectado = [conectado_decimal]
VAR vNotReady = IF(vConectado > 0, 1 - (RealTimeData[DacTotal_decimal] / vConectado), 0)
RETURN
    IF(vNotReady < 0, 0, vNotReady)
```

**conectado_decimal** (tabela `RealTimeData`)

```dax
[foraFila_decimal]+[naFila_decimal]+[treinamento_decimal]
```

**Ultima Atualização_Hora** (tabela `RealTimeData`)

```dax
FORMAT(MAX(RealTimeData[ultimaAtualizacao]), "HH:mm:ss")
```

**Ultima Atualização_data_hora** (tabela `RealTimeData`)

```dax
FORMAT(MAX(RealTimeData[ultimaAtualizacao]), "dd/MM/yyyy hh:mm:ss")
```

**novo_decimal_interacao** (tabela `RealTimeData`)

```dax
VAR vUltimaDataHora =
    MAX(RealTimeData[ultimaAtualizacao])

RETURN
CALCULATE(
    SUM(RealTimeData[interacting]),
    RealTimeData[ultimaAtualizacao] = vUltimaDataHora
) / 1000/3600
```

**novo_decimal_disponivel** (tabela `RealTimeData`)

```dax
VAR vUltimaDataHora =
    MAX(RealTimeData[ultimaAtualizacao])

RETURN
CALCULATE(
    SUM(RealTimeData[available]),
    RealTimeData[ultimaAtualizacao] = vUltimaDataHora
) / 1000/3600
```

**novo_decimal_ocioso** (tabela `RealTimeData`)

```dax
VAR vUltimaDataHora =
    MAX(RealTimeData[ultimaAtualizacao])

RETURN
CALCULATE(
    SUM(RealTimeData[idle]),
    RealTimeData[ultimaAtualizacao] = vUltimaDataHora
) / 1000/3600
```

**novo_decimal_treinamento** (tabela `RealTimeData`)

```dax
VAR vUltimaDataHora =
    MAX(RealTimeData[ultimaAtualizacao])

RETURN
CALCULATE(
    SUM(RealTimeData[training]),
    RealTimeData[ultimaAtualizacao] = vUltimaDataHora
) / 1000/3600
```

**novo_decimal_naorespondendo** (tabela `RealTimeData`)

```dax
VAR vUltimaDataHora =
    MAX(RealTimeData[ultimaAtualizacao])

RETURN
CALCULATE(
    SUM(RealTimeData[not_responding]),
    RealTimeData[ultimaAtualizacao] = vUltimaDataHora
) / 1000/3600
```

**novo_decimal_nafila** (tabela `RealTimeData`)

```dax
VAR vUltimaDataHora =
    MAX(RealTimeData[ultimaAtualizacao])

RETURN
CALCULATE(
    SUM(RealTimeData[on_queue]),
    RealTimeData[ultimaAtualizacao] = vUltimaDataHora
) / 1000/3600
```

**novo_decimal_reuniao** (tabela `RealTimeData`)

```dax
VAR vUltimaDataHora =
    MAX(RealTimeData[ultimaAtualizacao])

RETURN
CALCULATE(
    SUM(RealTimeData[meeting]),
    RealTimeData[ultimaAtualizacao] = vUltimaDataHora
) / 1000/3600
```

**novo_decimal_refeicao** (tabela `RealTimeData`)

```dax
VAR vUltimaDataHora =
    MAX(RealTimeData[ultimaAtualizacao])

RETURN
CALCULATE(
    SUM(RealTimeData[meal]),
    RealTimeData[ultimaAtualizacao] = vUltimaDataHora
) / 1000/3600
```

**novo_decimal_ocupado** (tabela `RealTimeData`)

```dax
VAR vUltimaDataHora =
    MAX(RealTimeData[ultimaAtualizacao])

RETURN
CALCULATE(
    SUM(RealTimeData[busy]),
    RealTimeData[ultimaAtualizacao] = vUltimaDataHora
) / 1000/3600
```

**novo_decimal_pausa** (tabela `RealTimeData`)

```dax
VAR vUltimaDataHora =
    MAX(RealTimeData[ultimaAtualizacao])

RETURN
CALCULATE(
    SUM(RealTimeData[break]),
    RealTimeData[ultimaAtualizacao] = vUltimaDataHora
) / 1000/3600
```

**novo_decimal_ausente** (tabela `RealTimeData`)

```dax
VAR vUltimaDataHora =
    MAX(RealTimeData[ultimaAtualizacao])

RETURN
CALCULATE(
    SUM(RealTimeData[away]),
    RealTimeData[ultimaAtualizacao] = vUltimaDataHora
) / 1000/3600
```

**novo_decimal_offline** (tabela `RealTimeData`)

```dax
VAR vUltimaDataHora =
    MAX(RealTimeData[ultimaAtualizacao])

RETURN
CALCULATE(
    SUM(RealTimeData[offline]),
    RealTimeData[ultimaAtualizacao] = vUltimaDataHora
) / 1000/3600
```

**novo_decimal_forafila** (tabela `RealTimeData`)

```dax
-- [disponivel_decimal] 
+ [novo_decimal_ausente] 
+ [novo_decimal_refeicao] 
+ [novo_decimal_reuniao] 
+ [novo_decimal_ocupado]
```

**novo_decimal_conectado** (tabela `RealTimeData`)

```dax
[novo_decimal_forafila] 
+ [novo_decimal_treinamento] 
+ [novo_decimal_nafila]
```

**novo_tempo_ausente** (tabela `RealTimeData` · formato `00\:00\:00`)

```dax
VAR HorasDec = [novo_decimal_ausente]
                    VAR Horas = INT(HorasDec)
                    VAR MinutosDec = (HorasDec - Horas) * 60
                    VAR Minutos = INT(MinutosDec)
                    VAR Segundos = ROUND((MinutosDec - Minutos) * 60, 0)
                    RETURN
                    FORMAT(Horas,"00")
                    & ":"
                    & FORMAT(Minutos,"00")
                    & ":"
                    & FORMAT(Segundos,"00")
```

**novo_tempo_conectado** (tabela `RealTimeData` · formato `00\:00\:00`)

```dax
VAR HorasDec = [novo_decimal_conectado]
                    VAR Horas = INT(HorasDec)
                    VAR MinutosDec = (HorasDec - Horas) * 60
                    VAR Minutos = INT(MinutosDec)
                    VAR Segundos = ROUND((MinutosDec - Minutos) * 60, 0)
                    RETURN
                    FORMAT(Horas,"00")
                    & ":"
                    & FORMAT(Minutos,"00")
                    & ":"
                    & FORMAT(Segundos,"00")
```

**novo_tempo_forafila** (tabela `RealTimeData` · formato `00\:00\:00`)

```dax
VAR HorasDec = [novo_decimal_forafila]
                    VAR Horas = INT(HorasDec)
                    VAR MinutosDec = (HorasDec - Horas) * 60
                    VAR Minutos = INT(MinutosDec)
                    VAR Segundos = ROUND((MinutosDec - Minutos) * 60, 0)
                    RETURN
                    FORMAT(Horas,"00")
                    & ":"
                    & FORMAT(Minutos,"00")
                    & ":"
                    & FORMAT(Segundos,"00")
```

**novo_tempo_disponivel** (tabela `RealTimeData` · formato `00\:00\:00`)

```dax
VAR HorasDec = [novo_decimal_disponivel]
                    VAR Horas = INT(HorasDec)
                    VAR MinutosDec = (HorasDec - Horas) * 60
                    VAR Minutos = INT(MinutosDec)
                    VAR Segundos = ROUND((MinutosDec - Minutos) * 60, 0)
                    RETURN
                    FORMAT(Horas,"00")
                    & ":"
                    & FORMAT(Minutos,"00")
                    & ":"
                    & FORMAT(Segundos,"00")
```

**novo_tempo_interacao** (tabela `RealTimeData` · formato `00\:00\:00`)

```dax
VAR HorasDec = [novo_decimal_interacao]
                    VAR Horas = INT(HorasDec)
                    VAR MinutosDec = (HorasDec - Horas) * 60
                    VAR Minutos = INT(MinutosDec)
                    VAR Segundos = ROUND((MinutosDec - Minutos) * 60, 0)
                    RETURN
                    FORMAT(Horas,"00")
                    & ":"
                    & FORMAT(Minutos,"00")
                    & ":"
                    & FORMAT(Segundos,"00")
```

**novo_tempo_nafila** (tabela `RealTimeData` · formato `00\:00\:00`)

```dax
VAR HorasDec = [novo_decimal_nafila]
                    VAR Horas = INT(HorasDec)
                    VAR MinutosDec = (HorasDec - Horas) * 60
                    VAR Minutos = INT(MinutosDec)
                    VAR Segundos = ROUND((MinutosDec - Minutos) * 60, 0)
                    RETURN
                    FORMAT(Horas,"00")
                    & ":"
                    & FORMAT(Minutos,"00")
                    & ":"
                    & FORMAT(Segundos,"00")
```

**novo_tempo_naorespondendo** (tabela `RealTimeData` · formato `00\:00\:00`)

```dax
VAR HorasDec = [novo_decimal_naorespondendo]
                    VAR Horas = INT(HorasDec)
                    VAR MinutosDec = (HorasDec - Horas) * 60
                    VAR Minutos = INT(MinutosDec)
                    VAR Segundos = ROUND((MinutosDec - Minutos) * 60, 0)
                    RETURN
                    FORMAT(Horas,"00")
                    & ":"
                    & FORMAT(Minutos,"00")
                    & ":"
                    & FORMAT(Segundos,"00")
```

**novo_tempo_ocioso** (tabela `RealTimeData` · formato `00\:00\:00`)

```dax
VAR HorasDec = [novo_decimal_ocioso]
                    VAR Horas = INT(HorasDec)
                    VAR MinutosDec = (HorasDec - Horas) * 60
                    VAR Minutos = INT(MinutosDec)
                    VAR Segundos = ROUND((MinutosDec - Minutos) * 60, 0)
                    RETURN
                    FORMAT(Horas,"00")
                    & ":"
                    & FORMAT(Minutos,"00")
                    & ":"
                    & FORMAT(Segundos,"00")
```

**novo_tempo_ocupado** (tabela `RealTimeData` · formato `00\:00\:00`)

```dax
VAR HorasDec = [novo_decimal_ocupado]
                    VAR Horas = INT(HorasDec)
                    VAR MinutosDec = (HorasDec - Horas) * 60
                    VAR Minutos = INT(MinutosDec)
                    VAR Segundos = ROUND((MinutosDec - Minutos) * 60, 0)
                    RETURN
                    FORMAT(Horas,"00")
                    & ":"
                    & FORMAT(Minutos,"00")
                    & ":"
                    & FORMAT(Segundos,"00")
```

**novo_tempo_offline** (tabela `RealTimeData` · formato `00\:00\:00`)

```dax
VAR HorasDec = [novo_decimal_offline]
                    VAR Horas = INT(HorasDec)
                    VAR MinutosDec = (HorasDec - Horas) * 60
                    VAR Minutos = INT(MinutosDec)
                    VAR Segundos = ROUND((MinutosDec - Minutos) * 60, 0)
                    RETURN
                    FORMAT(Horas,"00")
                    & ":"
                    & FORMAT(Minutos,"00")
                    & ":"
                    & FORMAT(Segundos,"00")
```

**novo_tempo_pausa** (tabela `RealTimeData` · formato `00\:00\:00`)

```dax
VAR HorasDec = [novo_decimal_pausa]
                    VAR Horas = INT(HorasDec)
                    VAR MinutosDec = (HorasDec - Horas) * 60
                    VAR Minutos = INT(MinutosDec)
                    VAR Segundos = ROUND((MinutosDec - Minutos) * 60, 0)
                    RETURN
                    FORMAT(Horas,"00")
                    & ":"
                    & FORMAT(Minutos,"00")
                    & ":"
                    & FORMAT(Segundos,"00")
```

**novo_tempo_refeicao** (tabela `RealTimeData` · formato `00\:00\:00`)

```dax
VAR HorasDec = [novo_decimal_refeicao]
                    VAR Horas = INT(HorasDec)
                    VAR MinutosDec = (HorasDec - Horas) * 60
                    VAR Minutos = INT(MinutosDec)
                    VAR Segundos = ROUND((MinutosDec - Minutos) * 60, 0)
                    RETURN
                    FORMAT(Horas,"00")
                    & ":"
                    & FORMAT(Minutos,"00")
                    & ":"
                    & FORMAT(Segundos,"00")
```

**novo_tempo_reuniao** (tabela `RealTimeData` · formato `00\:00\:00`)

```dax
VAR HorasDec = [novo_decimal_reuniao]
                    VAR Horas = INT(HorasDec)
                    VAR MinutosDec = (HorasDec - Horas) * 60
                    VAR Minutos = INT(MinutosDec)
                    VAR Segundos = ROUND((MinutosDec - Minutos) * 60, 0)
                    RETURN
                    FORMAT(Horas,"00")
                    & ":"
                    & FORMAT(Minutos,"00")
                    & ":"
                    & FORMAT(Segundos,"00")
```

**novo_tempo_treinamento** (tabela `RealTimeData` · formato `00\:00\:00`)

```dax
VAR HorasDec = [novo_decimal_treinamento]
                    VAR Horas = INT(HorasDec)
                    VAR MinutosDec = (HorasDec - Horas) * 60
                    VAR Minutos = INT(MinutosDec)
                    VAR Segundos = ROUND((MinutosDec - Minutos) * 60, 0)
                    RETURN
                    FORMAT(Horas,"00")
                    & ":"
                    & FORMAT(Minutos,"00")
                    & ":"
                    & FORMAT(Segundos,"00")
```

**novo_indicador_tempo_falado** (tabela `RealTimeData`)

```dax
SWITCH(
    TRUE(),
    [novo_decimal_meta] <= 0.1667, "Ruim",
    [novo_decimal_meta] <= 1, "Alerta",
    "Bom"
)
```

**novo_decimal_meta** (tabela `RealTimeData`)

```dax
VAR meta = 6
VAR falado = [novo_decimal_interacao] 
VAR restante = meta - falado
RETURN
-- meta
restante

-- IF(restante > 0 , restante, 0)
```

**novo_tempo_meta** (tabela `RealTimeData` · formato `00\:00\:00`)

```dax
VAR vHorasDecimal = [novo_decimal_meta]
VAR vHoras = INT(vHorasDecimal)
VAR vMinutosDecimal = 60 * (vHorasDecimal - vHoras)
VAR vMinutos = INT(vMinutosDecimal)
VAR vSegundos = INT( 60 * (vMinutosDecimal - vMinutos) )
VAR vHH = IF(LEN(vHoras) = 1, "0" & vHoras, vHoras)
VAR vMM = IF(LEN(vMinutos) = 1, "0" & vMinutos, vMinutos)
VAR vSS = IF(vSegundos > 0, IF(LEN(vSegundos) = 1, "0" & vSegundos, vSegundos), "00") 
RETURN
CONVERT(vHH&vMM&vSS, INTEGER)
```


## Real Time projetado

- **Modo:** Modelo local (PBIP) · **Workspace:** — · **Dataset:** `Real Time projetado`
- **Alimentado por:** não identificado
- **Tema:** tema base do Power BI — ⚠️ sem tema oficial aplicado (COR-001)
- **Cópias encontradas:** 1

### Páginas

| Página | Visuais | Campos usados |
|---|---|---|
| 2026 | slicer×1, tableEx×6 | `Area[Area]`, `Data[Data]`, `Diário fone separa[Demanda proj]`, `Diário fone separa[Diário fone junto.TME hbd]`, `Diário fone separa[Regional]` |
| Chat | slicer×1, tableEx×6 | `Area[Area]`, `Data[Data]`, `Diário chat separa[Demanda humano]`, `Diário chat separa[Demanda proj]`, `Diário chat separa[Diário chat junto.TME]`, `Diário chat separa[Regional]` |
| Por meia hora | slicer×1, tableEx×3 | `Area[Area]`, `Data[Data]`, `Projetado por meia hora junto[Demanda Projetada Acumulada] (medida)`, `Projetado por meia hora junto[Meia hora normal]`, `Projetado por meia hora junto[Meia hora]`, `Projetado por meia hora junto[TME proj]` |

### Modelo semântico local (TMDL)

| Tabela | Fonte | Arquivos | Medidas |
|---|---|---|---|
| `Area` | Json.Document, Table.FromRows | — | — |
| `AT` | Excel.Workbook, Web.Contents | Teste demanda.xlsx | — |
| `Data` | Excel.Workbook, Web.Contents | Plano 2026 - Diretoria - replan 1.xlsx | — |
| `Diário chat junto` | Excel.Workbook, Web.Contents | Plano 2026 - Diretoria - replan 1.xlsx | — |
| `Diário chat separa (2)` | Excel.Workbook, Web.Contents | Plano 2026 - Diretoria - replan 1.xlsx | — |
| `Diário chat separa` | Excel.Workbook, Web.Contents | Plano 2026 - Diretoria - replan 1.xlsx | — |
| `Diário fone junto` | Excel.Workbook, Web.Contents | Plano 2026 - Diretoria - replan 1.xlsx | — |
| `Diário fone separa` | Excel.Workbook, Web.Contents | Plano 2026 - Diretoria - replan 1.xlsx | — |
| `FisCont` | Excel.Workbook, Web.Contents | Teste demanda.xlsx | — |
| `Folha` | Excel.Workbook, Web.Contents | Teste demanda.xlsx | — |
| `Projetado por meia hora junto` | Excel.Workbook, Web.Contents | Plano 2026 - Diretoria - replan 1.xlsx | Demanda Projetada Acumulada |
| `Tabela` | Json.Document, Table.FromRows | — | — |

**Demanda Projetada Acumulada** (`Projetado por meia hora junto`)

```dax
```
```

