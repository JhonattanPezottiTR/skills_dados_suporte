# Identidade visual TR (brand kit 2026) — para Excel e relatório visual fora do Power BI

> Última atualização: 2026-09-30 · Fonte: skill `alia-trdesign` (brand kit TR 2026, extraído do portal AI Champions em produção)

No Power BI, a identidade oficial já é aplicada via `tema-oficial-powerbi.json` (RG-03, `powerbi-tema-cores.md`)
e **usa a mesma paleta** deste arquivo — nada muda ali. Este arquivo entra em cena quando o entregável **não é**
um PBIP: um Excel, uma página/relatório HTML, um slide ou uma apresentação "como se fosse publicada" na TR
(RG-13).

Os assets binários (fonte Clario, ícones, logos, foto de capa, espirais) são licenciados pela TR para uso
**interno** — confirmado pelo usuário (colaborador TR) que este uso está autorizado — e foram copiados para
`skills/especialista-dados/assets/identidade-tr/`:

| Caminho | Conteúdo |
|---|---|
| `assets/identidade-tr/tokens.css` | CSS com todas as variáveis de cor/tipografia (as mesmas tabelas abaixo, em `--tr-*`) |
| `assets/identidade-tr/fonts/clario/*.woff2` | As 14 variações da fonte Clario (pesos/itálicos) |
| `assets/identidade-tr/icons/tr-icons.json` | Bundle completo dos ícones do brand kit (847), indexado por nome |
| `assets/identidade-tr/icons/tr-icons-index.txt` | Índice de nomes de ícone (Font Awesome 6, kebab-case) — consultar antes de escolher um ícone |
| `assets/identidade-tr/icons/tr-sample/*.svg` | 17 ícones de amostra, prontos para uso direto |
| `assets/identidade-tr/icons/tr-spirals/waypt_1..16.svg` | As 16 espirais oficiais (grafismo de marca) |
| `assets/identidade-tr/logos/*` | Logo TR (preto/branco) e logo do hub |
| `assets/identidade-tr/photos/header.jpg` | Foto de capa oficial (golden hour) |

Ao gerar um HTML/Excel para o time, usar os arquivos acima diretamente (copiar para o projeto/artefato final)
em vez de recriar cor/ícone à mão. **Não incluídos aqui** (não vieram na skill de origem, só o essencial):
scripts de instalação automática (`install-assets.ps1`/`.sh`) e o `self-check.html`/`tailwind.config` de
referência visual — se precisar deles, peça para o usuário disponibilizar o pacote `alia-trdesign` completo.

## Paleta — o que cada cor faz

| Papel | Hex |
|---|---|
| Acento, ação, régua (laranja TR) | `#D64000` |
| Hover do laranja | `#B53600` |
| Título, superfície escura editorial (Racing Green) | `#123015` |
| Superfície escura de app | `#1A1F36` |
| Fundo de página | `#FAF7F2` |
| Fundo alternado de seção | `#F5F0E8` |
| Corpo de texto | `#212223` |
| Texto secundário | `#595959` |
| Borda de card | `#E8E4DE` |

**Os três verdes** — não trocar um pelo outro:

| Hex | Papel |
|---|---|
| `#123015` | Racing Green — título e fundo de painel escuro |
| `#0F7B45` | Acento interativo — chip ativo, foco de busca, badge "pronto" |
| `#2D7A3F` | Estado — série "realizado" em gráfico, marco concluído |

Sobre fundo escuro, o laranja `#D64000` fica abafado — usar `#FF6A2C` (número/ênfase) em vez disso.

Estas cores **são as mesmas** de `powerbi-tema-cores.md` (COR-001/002/003) — confirmado, sem divergência.

## Tipografia

Fonte da marca: **Clario**. Escala (do maior para o menor):

```
Display   Clario peso 200, 88px   — capa
H1        Clario peso 200, 72px
H2        Clario peso 300, 48px
H3        Clario peso 500, 22px
H4        CAPS 14px bold, tracking 0.12em
Lead      Clario peso 300, 19px, máx. 720px de largura
```

⚠️ Em Clario, **Air é peso 100 e Thin é peso 200** — invertido em relação à convenção usual. Trocar os dois
deixa os títulos mais pesados do que deveriam.

Se Clario não estiver disponível no ambiente de destino (ex. Excel), usar a fonte padrão da ferramenta e manter
as demais regras (cor, hierarquia, régua) — não é motivo para abandonar a identidade inteira.

## Dois modos — não misturar na mesma peça

- **Modo página/view** — portal, landing, listagem, relatório longo: seções alternando fundo `#FAF7F2`/`#F5F0E8`,
  tudo com canto reto, hairline de 1px, sombra só no hover.
- **Modo canvas** — capa, slide, divisor de seção, encerramento: fundo de cor secundária, topbar laranja de 8px
  no topo, título grande em Racing Green, régua laranja retangular.

Para um relatório Excel/HTML de time (o caso comum aqui), o modo **página/view** é o padrão. Use modo canvas só
para capa/slide de apresentação.

## O que faz a peça parecer oficial (checklist rápido)

- [ ] Título em Racing Green `#123015` — nunca navy, nunca preto.
- [ ] Laranja `#D64000` só como acento (régua, destaque, CTA) — nunca fundo de área grande.
- [ ] Régua/linha de destaque **retangular**, nunca arredondada.
- [ ] Sem `border-radius`/canto arredondado em elemento de página (card, tabela, filtro) — só é aceitável em
      superfície de app interativo (8–12px).
- [ ] Só um destaque em itálico/ênfase por seção.
- [ ] Cor de gráfico segue `blocos-aihub.md` (categórica sky→teal→gold→amber→lime; rampa laranja para ranking).

## Erros comuns

| Erro | Por que importa |
|---|---|
| Título em navy ou preto | Brand kit 2026 usa Racing Green `#123015` |
| Fundo laranja em área grande | Laranja é acento, não fundo |
| Régua ou card arredondado numa página | Página é reta; raio só em app interativo |
| Trocar os três verdes entre si | Cada um tem um papel (título / acento / estado) |
| Inventar ícone ou cor fora da paleta/índice acima | Os 847 ícones oficiais estão em `assets/identidade-tr/icons/tr-icons-index.txt` — consulte o índice antes de adivinhar um nome |

## Relacionadas
- `powerbi-tema-cores.md` / `tema-oficial-powerbi.json` (RG-03) — mesma paleta, aplicada ao Power BI.
- `visual-blocos-aihub.md` (RG-13/RG-14) — que bloco/visual usar para cada tipo de dado.
- `visual-publicacao-concepthub.md` — por que a publicação de verdade (deploy de app) não é feita por esta skill.
