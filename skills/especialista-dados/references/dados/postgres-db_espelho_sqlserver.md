# Postgres · DB_ESPELHO_SQLSERVER — estrutura

> Última atualização: 2026-09-29 · Fonte: catálogo `pg_catalog` lido por `scripts/catalogo_postgres.py` (sessão READ ONLY, sem leitura de dados) · **Gerado automaticamente** — não editar à mão.
> Linhas = estimativa do planner (`reltuples`), não contagem exata. Quem carrega cada tabela: `dados-postgres-destinos.md` / `dados-fluxos-maestro.md`.

| Schema | Tabelas | Views |
|---|---|---|
| `public` | 1 | 0 |

## Schema `public`

- **`public.interacoes_bi`** (tabela, ~53.8 mil linhas)
  `unidade` text, `grupo` text, `canal` text, `origem` text, `data_evento` timestamp without time zone, `tecnico` text, `lider` text, `mensagem` text, `id_lider_reacao` text, `data_hora_reacao` timestamp without time zone, `links` text, `tempo_reacao` text
