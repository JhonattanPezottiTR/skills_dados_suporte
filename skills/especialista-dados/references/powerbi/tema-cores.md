# Tema oficial e padrão de cores do Power BI — "Padrão TR Clario"

> Última atualização: 2026-09-29 · Fonte: arquivo oficial `Padrão TR_Clario.json` fornecido pelo time de BI (2026-09-29) · Arquivo do tema: `tema-oficial-powerbi.json`

Este é o **único** tema visual aceito nos relatórios do time (RG-03). O JSON completo está em `tema-oficial-powerbi.json` e deve ser importado sem alterações.

## Como aplicar
- **Power BI Desktop:** *Exibição → Temas → Procurar temas* → selecionar `tema-oficial-powerbi.json`.
- **PBIP/PBIR:** o tema personalizado fica em `StaticResources/RegisteredResources/<nome>.json` e é referenciado em `report.json` (`themeCollection.customTheme`).
- Ao sugerir cores, cite o **papel + hex + ID da regra** (ex.: "Destaque `#D64000` — COR-002").
- Prefira que o visual **herde do tema**. Só fixe uma cor manualmente quando a regra exigir (ex.: formatação condicional).

## Paleta de séries (`dataColors`) — ordem oficial

| Ordem | Hex | Descrição | Uso recomendado |
|---|---|---|---|
| 1 | `#D64000` | Laranja TR (cor principal) | Série principal, destaque, valor atual |
| 2 | `#123015` | Verde escuro | Segunda série, comparativo, meta |
| 3 | `#7A7A7A` | Cinza médio | Séries de apoio, período anterior |
| 4 | `#9F9F9F` | Cinza claro-médio | Séries de apoio |
| 5 | `#E5E5E5` | Cinza muito claro | Fundo de barras, "restante" em rosca/gauge, grades |
| 6 | `#E9B045` | Amarelo ouro | Categoria adicional, alerta leve |
| 7 | `#D4792A` | Laranja ocre | Categoria adicional (variação do principal) |
| 8 | `#4DB299` | Verde água | Categoria adicional |

## Cores semânticas (KPI / status)

| Papel no tema | Hex | Descrição |
|---|---|---|
| `good` | `#123015` | Verde escuro — resultado bom / atingido |
| `neutral` | `#8FCB64` | Verde claro — resultado neutro / dentro da tolerância |
| `bad` | `#DC0A0A` | Vermelho — resultado ruim / não atingido |

## Gradiente divergente (formatação condicional por escala)

| Ponto | Hex | Descrição |
|---|---|---|
| `minimum` | `#DC0A0A` | Vermelho |
| `center` | `#A00000` | Vermelho escuro |
| `maximum` | `#6E3AB7` | Roxo |

## Texto e neutros

| Papel | Hex | Uso |
|---|---|---|
| `foreground` | `#404040` | Texto principal (títulos, rótulos, cabeçalhos) |
| `foregroundNeutralSecondary` | `#666555` | Texto secundário |
| `foregroundNeutralTertiary` | `#AFAFAF` | Texto terciário, legendas discretas, desabilitado |
| `backgroundLight` | `#666666` | Fundo claro de elementos (definido no tema) |
| `backgroundNeutral` | `#D0D0D0` | Fundo neutro, divisórias |

## Tipografia (`textClasses`) — fonte **Clario**

| Classe | Fonte | Cor | Tamanho | Onde aparece |
|---|---|---|---|---|
| `title` | Clario | `#404040` | 10 | Títulos de visuais |
| `header` | Clario | `#404040` | 10 | Cabeçalhos (tabelas, matrizes, segmentações) |
| `label` | Clario | `#404040` | 10 | Rótulos de dados, eixos, legendas |
| `callout` | Clario | `#404040` | 30 | Valor principal de cartões/KPIs |

## Estilos globais (`visualStyles`)
- **Tooltip:** título e valores em branco `#FFFFFF`.
- **Painel de filtros:** cartão *Applied* com fundo branco `#FFFFFF`, sem transparência, texto tamanho 8; cartão *Available* texto 8; painel com título 10 e cabeçalho 8.
- **Página:** fundo com transparência 100% (a página não tem cor de fundo própria; o fundo vem da tela ou de imagem/wallpaper).

---

## Regras de cor (COR)

### COR-001 · Usar somente o tema oficial Padrão TR Clario
- **Status:** Ativa · **Criada em:** 2026-09-29 · **Atualizada em:** 2026-09-29
- **Origem:** arquivo `Padrão TR_Clario.json` enviado pelo time
- **Escopo:** todos os relatórios Power BI
- **Regra:** todo relatório usa `tema-oficial-powerbi.json` como tema; nenhuma cor fora das tabelas deste documento.
- **Como aplicar:** ao sugerir qualquer cor, usar só os hex listados aqui. Se o usuário pedir uma cor fora da paleta, avisar que ela não é oficial e oferecer a mais próxima.
- **Exemplo válido:** "Barra do ano atual em `#D64000`, ano anterior em `#7A7A7A`."
- **Exemplo inválido:** "Use azul `#118DFF` nas barras." (cor padrão do Power BI, não é oficial)

### COR-002 · Ordem das séries segue `dataColors`
- **Status:** Ativa · **Criada em:** 2026-09-29 · **Atualizada em:** 2026-09-29
- **Origem:** `dataColors` do tema oficial
- **Regra:** séries recebem as cores na ordem oficial: 1ª `#D64000`, 2ª `#123015`, 3ª `#7A7A7A`, 4ª `#9F9F9F`, 5ª `#E5E5E5`, 6ª `#E9B045`, 7ª `#D4792A`, 8ª `#4DB299`.
- **Como aplicar:** deixar o visual herdar do tema. Na comparação atual × anterior, o atual fica com o laranja `#D64000` e o anterior/referência com um cinza.

### COR-003 · Status de KPI usa as cores semânticas
- **Status:** Ativa · **Criada em:** 2026-09-29 · **Atualizada em:** 2026-09-29
- **Origem:** `good`/`neutral`/`bad` do tema oficial
- **Regra:** indicadores de desempenho (ícones, cores de fundo/fonte condicionais, visual KPI) usam bom `#123015`, neutro `#8FCB64`, ruim `#DC0A0A`.
- **Exemplo válido (DAX para formatação condicional por campo):**
  ```dax
  Cor Status Meta =
  VAR _ating = DIVIDE ( [Realizado], [Meta] )
  RETURN
      SWITCH (
          TRUE (),
          ISBLANK ( _ating ), BLANK (),
          _ating >= 1,    "#123015",   -- good (COR-003)
          _ating >= 0.9,  "#8FCB64",   -- neutral (COR-003) — limiar 90% é exemplo, confirmar regra de negócio
          "#DC0A0A"                    -- bad (COR-003)
      )
  ```
- **Exemplo inválido:** usar verde `#00FF00` ou vermelho `#FF0000` puros.

### COR-004 · Gradiente de escala usa minimum/center/maximum do tema
- **Status:** Ativa · **Criada em:** 2026-09-29 · **Atualizada em:** 2026-09-29
- **Origem:** `minimum`/`center`/`maximum` do tema oficial
- **Regra:** formatação condicional por escala de cores (heatmap em matriz, mapa coroplético) usa mín `#DC0A0A`, centro `#A00000`, máx `#6E3AB7`, salvo regra específica do relatório.

### COR-005 · Tipografia Clario, cor #404040
- **Status:** Ativa · **Criada em:** 2026-09-29 · **Atualizada em:** 2026-09-29
- **Origem:** `textClasses` e `foreground` do tema oficial
- **Regra:** a fonte é **Clario** em todos os textos, cor `#404040`. Títulos, cabeçalhos e rótulos no tamanho 10; valor de cartão/KPI (callout) no tamanho 30. Texto secundário `#666555`, terciário `#AFAFAF`.
- **Como aplicar:** não trocar fonte nem tamanho visual a visual. Se a Clario não estiver instalada na máquina, avisar que o Power BI vai usar a fonte substituta na renderização.

### COR-006 · Fundo de página transparente e padrões globais
- **Status:** Ativa · **Criada em:** 2026-09-29 · **Atualizada em:** 2026-09-29
- **Origem:** `visualStyles` do tema oficial
- **Regra:** o fundo da página fica 100% transparente, o texto do tooltip fica branco e os cartões de filtro seguem o tema (Applied com fundo branco, texto 8). Não sobrescrever esses valores nos visuais.

---

## Pontos a confirmar com o time
1. `neutral` é o verde claro `#8FCB64`, e não um amarelo/cinza. Confirmar se "neutro" significa "próximo da meta".
2. No gradiente, o `center` `#A00000` é um vermelho escuro entre o vermelho e o roxo. Confirmar se essa escala divergente é intencional ou se deve ser usada só em casos específicos.
3. `good` `#123015` é a mesma cor da 2ª série. Em visuais com série + status, conferir se não gera ambiguidade.
