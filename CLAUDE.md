# Projeto: Skill "especialista-dados" (SQL · Power BI · Microsoft Fabric · Dados do time)

Este repositório mantém a skill `skills/especialista-dados/`, publicada numa chain do **Open Arena** via um servidor **MCP** (`scripts/mcp_server.py`, registrado em `.mcp.json`) que o Open Arena lê direto deste repositório no GitHub — o servidor da chain sincroniza com `git pull` periódico. Aqui no Claude Code, você é ao mesmo tempo o especialista **e** o mantenedor da skill.

**Publicar = dar `git push` na branch principal.** Não existe build nem upload manual de pasta: depois de qualquer alteração, o próximo passo é sempre avisar o usuário para commitar e enviar (`git push`) — **eu (Claude Code) nunca commito nem faço push sozinho**, só deixo os arquivos prontos.

## Ao abrir a sessão
Se houver hooks `SessionStart` configurados em `.claude/settings.json` (ainda não trazidos para este repositório), siga o mesmo padrão do projeto irmão: avisar o usuário no início da primeira resposta e executar o protocolo correspondente automaticamente, mostrando o resumo do que mudou ao final.

## Fontes monitoradas
*(a preencher conforme este domínio for mapeado — ver seção "Roadmap")*
- **Bancos** (só estrutura): credenciais e conexões ficam fora deste repositório, nunca em texto plano aqui.
- Snapshots para detectar mudanças (se adotados): pasta fora do Git, no padrão `.dados-sync/*.json`.

## Regras de manutenção (obrigatórias)
1. **Versionamento por calendário, padrão Maestro** ([docs/VERSIONAMENTO.md](docs/VERSIONAMENTO.md), a criar se ainda não existir):
   - `MAJOR.MINOR.PATCH` = (ano − 2025).(mês).(N-ésima alteração publicada no mês);
   - toda alteração publicada ganha uma entrada no `CHANGELOG.md` (`## [X.Y.Z] — AAAA-MM-DD`), começando pela linha `**Resumo:**` em linguagem simples;
   - atualize também o frontmatter e a tabela "Histórico de versões" do `SKILL.md`.
2. Cada arquivo em `references/` começa com `> Última atualização: AAAA-MM-DD · Fonte: ...`.
3. Regras ensinadas pelo usuário seguem `references/regras/formato.md` (IDs REG/COR/NOM/FON/SQL/DAX, nunca reutilizados). Se a regra estiver ambígua, pergunte antes de gravar.
4. Só registre fatos verificados. Nunca de memória.
5. Conteúdo da skill em pt-BR; código, APIs e termos técnicos em inglês.
6. Depois de qualquer alteração publicada, avise o usuário para **commitar e dar `git push`** na branch principal — o servidor da chain no Open Arena sincroniza via `git pull` periódico e o MCP (`scripts/mcp_server.py`) serve o conteúdo atualizado automaticamente, sem build nem upload manual.
7. Arquivos temporários enviados pelo usuário (JSON solto na raiz etc.) devem ser incorporados e depois **excluídos**, se ele pedir.

## Fontes externas: somente consulta
- Tudo fora deste repositório é **somente leitura**: outros repositórios em `C:\GitHub\TR`, bancos de dados, workspaces do Power BI.
- Nunca edite, mova ou grave nada nessas fontes. O conhecimento extraído delas é gravado **só aqui**, em `skills/especialista-dados/references/`.

## Segurança (inviolável)
- **Nunca** leia, exiba, copie nem grave credenciais (`.env`, senhas, connection strings, tokens). Qualquer script que precise de credenciais deve carregá-las só em memória.
- **Bancos:** sessão sempre **READ ONLY**, e só consultas de catálogo. Nenhum SELECT em dados de negócio sem pedido explícito do usuário.
- **Skill publicada:** nunca inclui host, porta, usuário, senha, URL de blob ou connection string. SQL com credencial embutida é mascarado como `***`. Antes de publicar (dar push), faça uma varredura manual direto contra `skills/especialista-dados/`. O próprio `scripts/mcp_server.py` também aplica essa máscara em tempo de leitura, como camada extra — mas isso não substitui a varredura antes do push.
- O `.mcp.json`/`scripts/mcp_server.py` só expõe arquivos dentro de `skills/especialista-dados/` (SKILL.md, `references/*.md` não excluídos, `assets/tema-oficial-powerbi.json`) — nunca `.env`, banco, nem qualquer caminho fora dessa árvore.
- Nenhum texto bruto de bases internas é citado em arquivo da skill — sempre fato reescrito e generalizado, nunca cópia literal de conversa ou log. Qualquer padrão de credencial é mascarado como `***` **antes** de a IA sequer exibir um resumo ao usuário.

## Estrutura
- `skills/especialista-dados/SKILL.md` — arquivo principal (persona, regras de ouro, tema rápido, fluxo de decisão, índice).
- `skills/especialista-dados/references/{fabric,sql,powerbi,regras,dados,negocio,visual}/*.md` — conhecimento.
- `skills/especialista-dados/assets/tema-oficial-powerbi.json` — tema oficial Padrão TR Clario.
- `scripts/mcp_server.py` — servidor MCP que publica a skill para o Open Arena (transporte stdio, só resources, sem tools).
- `config/fora-do-open-arena.txt` — lista de exclusão: arquivos de `references/` que não são expostos pelo MCP.
- `.mcp.json` — manifest do servidor MCP (`scripts/mcp_server.py`), lido pelo Open Arena direto do GitHub.

## Roadmap
- **Fase 1** (feita): skill trazida do projeto irmão (`analytics_bi_dominio-skills-bi_suporte_dados`) e renomeada para `especialista-dados`, com servidor MCP funcional publicando via `.mcp.json`.
- **Fase 2** (atual): adaptar o conteúdo de `references/` para o escopo próprio deste domínio (dados/suporte) — remapear fontes, scripts de sincronização e comandos (`/sincronizar-dados`, `/nova-regra` etc.) equivalentes aos do projeto irmão, se aplicável.
- **Fase 3** (futura): MCP com tools de consulta direta aos bancos (somente leitura) para responder com dados reais — diferente do MCP de publicação atual, que só expõe os arquivos da skill como resources.
