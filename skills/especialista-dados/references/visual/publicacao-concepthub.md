# Concept Hub / publicação de app — fora do escopo desta skill

> Última atualização: 2026-09-30 · Fonte: skill `alia-trpublish` (pipeline de publicação TR)

Existe, no ecossistema Alia/AI Champions, uma skill (`alia-trpublish`) que conduz o ciclo completo para publicar
um **aplicativo web (MFE)** no **Concept Hub** da Thomson Reuters: branch → commit assinado → PR → checks →
merge → deploy, usando `gh` (GitHub CLI). É um pipeline real de código-para-produção de um portal/app.

**Isso não tem relação com os entregáveis desta skill** (PBIP, Excel, relatório HTML) e **não é executado por
ela**:
- o `especialista-dados` nunca comita, cria branch nem faz push em nenhum repositório — nem neste, nem em outro;
- "publicar um BI" aqui significa o usuário abrir o PBIP no Power BI Desktop e publicar manualmente no workspace
  **Dominio FLOWS** (fluxo de `/criar-bi`), ou abrir/enviar o Excel/HTML gerado — não um deploy de aplicação.

Se o usuário pedir, de fato, para publicar um aplicativo web/MFE na TR (fora do escopo de BI), isso é trabalho
para a skill `alia-trpublish` (fora deste repositório) e para quem administra o Concept Hub — não invente esse
procedimento aqui, e não execute `gh`/`git push` para esse fim.

## Relacionadas
- `visual-identidade-tr.md` / `visual-blocos-aihub.md` — a parte de identidade visual e componentes, que **é**
  usada por esta skill (RG-13/RG-14).
- `CLAUDE.md` (regra permanente do usuário) — este repositório nunca faz commit/branch/push.
