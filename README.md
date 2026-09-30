# analytics_bi_dominio-skills-dados_suporte

Skill **`especialista-dados`**: um agente especialista em **SQL, Power BI e Microsoft Fabric** que também conhece os **dados do time**:
- tabelas do SGD no Sybase;
- réplicas no Postgres carregadas pelo Maestro;
- Dataflows do Power BI;
- relatórios existentes.

A skill é publicada numa chain do **Open Arena** e mantida aqui com o Claude Code. O conteúdo desta skill foi trazido do projeto irmão `analytics_bi_dominio-skills-bi_suporte_dados` e renomeado para `especialista-dados` — este repositório é o dono da própria cópia a partir de agora, que evolui de forma independente.

## Como a skill chega no Open Arena
A chain aponta direto para este repositório no GitHub via um servidor **MCP**
(`scripts/mcp_server.py`, manifest em `.mcp.json`) e o servidor da chain sincroniza com `git pull`
periódico — **publicar é dar `git push` na branch principal**, sem build nem upload manual de pasta.

O MCP expõe como *resources* (sem transformação, lidos direto do disco a cada chamada):
- `SKILL.md`, o arquivo principal;
- todo `skills/especialista-dados/references/**/*.md`, exceto o que estiver em
  `config/fora-do-open-arena.txt`;
- `skills/especialista-dados/assets/tema-oficial-powerbi.json`.

## Conhecimento

| Domínio | Arquivos (em `skills/especialista-dados/references/`) | Fonte |
|---|---|---|
| Microsoft Fabric | `fabric/*` | microsoft/skills-for-fabric + Microsoft Learn |
| SQL e Power BI (padrões) | `sql/*`, `powerbi/dax-padroes.md`, `modelagem.md`, `relatorios.md` | Microsoft Learn + skills oficiais |
| Tema oficial | `powerbi/tema-cores.md`, `assets/tema-oficial-powerbi.json` | Padrão TR Clario (time) |
| Regras do time | `regras/*` | time de BI |
| Dados do time | `dados/*` | Maestro, SGD/Sybase, Postgres, Dataflows |
| Relatórios | `powerbi/catalogo-relatorios.md`, `powerbi/tipos-de-bi.md` | PBIP + inventário do serviço Power BI |

> Este conteúdo foi importado do projeto irmão. Os processos automáticos de sincronização (hooks, scripts de mapeamento, comandos `/sincronizar-dados`, `/nova-regra` etc.) ainda não foram trazidos para este repositório — ver "Roadmap" no [CLAUDE.md](CLAUDE.md).

## Segurança
- Nenhuma credencial (host, porta, usuário, senha, connection string) entra na skill.
- Bancos são acessados (quando aplicável) em modo somente leitura, apenas pelo catálogo.
- Veja a seção "Segurança" do [CLAUDE.md](CLAUDE.md) para as regras completas.

## Histórico de versões
Versionamento por calendário, mesmo padrão do Maestro ([docs/VERSIONAMENTO.md](docs/VERSIONAMENTO.md), a criar). O histórico fica em `CHANGELOG.md` (a criar).
