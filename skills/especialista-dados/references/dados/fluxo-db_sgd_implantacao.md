# Fluxo `DB_SGD_IMPLANTACAO`

> Última atualização: 2026-09-30 · Fonte: `DB_SGD_IMPLANTACAO.json` (Dataflow Power BI, modificado em 2024-10-17, cultura en-US) · **Gerado automaticamente** por `scripts/mapear_fluxos.py`.

| Entidade | Carrega | Origem | Base | Tabelas de origem | Colunas | Último refresh (UTC) |
|---|---|---|---|---|---|---|
| `sgd_externo_categoria` | sim | Postgres | DB_SGD | `externo.categoria` | 2 | 2026-09-29T09:02:33 |
| `sgd_externo_forma_treinamento` | sim | Postgres | DB_SGD | `externo.forma_treinamento` | 2 | 2026-09-29T09:03:03 |
| `sgd_externo_implantacoes` | sim | Postgres | DB_SGD | `externo.implantacao` | 19 | 2026-09-29T09:03:33 |
| `sgd_externo_local_treinamento` | sim | Postgres | DB_SGD | `externo.local_treinamento` | 2 | 2026-09-29T09:04:04 |
| `sgd_externo_motivo_treinamento` | sim | Postgres | DB_SGD | `externo.motivo_treinamento` | 3 | 2026-09-29T09:04:35 |
| `sgd_externo_programacao` | sim | Postgres | DB_SGD | `externo.programacao` | 12 | 2026-09-29T09:05:05 |
| `sgd_externo_situacao` | sim | Postgres | DB_SGD | `externo.situacoes` | 3 | 2026-09-29T09:05:36 |
| `sgd_externo_treinamentos` | sim | Postgres | DB_SGD | `externo.treinamento`, `public.sgd_sa_module`, `public.sgd_sa_system` | 9 | 2026-09-29T09:06:06 |
| `sgd_externo_treinamento_conteudo` | sim | Postgres | DB_SGD | `externo.treinamento_conteudo` | 8 | 2026-09-29T09:06:36 |
| `sgd_externo_treinamento_programacao` | sim | Postgres | DB_SGD | `externo.treinamento_programacao` | 10 | 2026-09-29T09:08:37 |
| `sgd_externo_treinamento_programacao_usuarios` | sim | Postgres | DB_SGD | `externo.treinamento_programacao_usuario` | 6 | 2026-09-29T09:09:08 |

## `sgd_externo_categoria`

- **Origem:** Postgres · base `DB_SGD`
- `externo.categoria` ← import-sgd-diario (recarga TOTAL)
- **Colunas entregues:** `id_categoria` (int64), `desc_categoria` (string)

SQL nativo:

```sql
Select * from externo.categoria
```

## `sgd_externo_forma_treinamento`

- **Origem:** Postgres · base `DB_SGD`
- `externo.forma_treinamento` ← import-sgd-diario (recarga TOTAL)
- **Colunas entregues:** `id_forma_treinamento` (int64), `desc_forma_treinamento` (string)

SQL nativo:

```sql
SELECT 
    id_forma_treinamento, 
    desc_forma_treinamento
FROM externo.forma_treinamento
```

## `sgd_externo_implantacoes`

- **Origem:** Postgres · base `DB_SGD`
- `externo.implantacao` ← import-sgd-diario (substitui janela de 10 dia(s))
- **Colunas entregues:** `id_externos` (int64), `entrada` (date), `atualizacao` (date), `id_clientes` (int64), `i_usuarios` (int64), `i_responsaveis` (int64), `i_situacoes` (int64), `i_contratos` (int64), `tempo_treinamento` (int64), `tempo_treinamento_realizadas` (int64), `prazo_limite_iniciar` (date), `prazo_limite_concluir` (date), `quantidade_dias_produto` (int64), `numero_usuarios` (int64), `i_produtos` (int64), `prazo_limte_concluir_antiga` (date), `tempo_original` (int64), `id_forma_treinamento` (int64), `prazo_limite_concluir_passagem_bastao` (date)

SQL nativo:

```sql
SELECT 
        imp.id_externos, 
        imp.entrada::date, 
        imp.atualizacao::date, 
        imp.id_clientes, 
        imp.i_usuarios, 
        imp.i_responsaveis, 
        imp.i_situacoes, 
        imp.i_contratos, 
        imp.tempo_treinamento, 
        imp.tempo_treinamento_realizadas, 
        imp.prazo_limite_iniciar, 
        imp.prazo_limite_concluir, 
        imp.quantidade_dias_produto, 
        imp.numero_usuarios, 
        imp.i_produtos, 
        imp.prazo_limte_concluir_antiga, 
        imp.tempo_original, 
        imp.id_forma_treinamento,  
        imp.prazo_limite_concluir_passagem_bastao
        
    FROM externo.implantacao as imp
```

## `sgd_externo_local_treinamento`

- **Origem:** Postgres · base `DB_SGD`
- `externo.local_treinamento` ← import-sgd-diario (recarga TOTAL)
- **Colunas entregues:** `id_local` (int64), `desc_local` (string)

SQL nativo:

```sql
SELECT 
    id_local, 
    desc_local
FROM externo.local_treinamento
```

## `sgd_externo_motivo_treinamento`

- **Origem:** Postgres · base `DB_SGD`
- `externo.motivo_treinamento` ← import-sgd-diario (recarga TOTAL)
- **Colunas entregues:** `id_motivo` (int64), `id_situacao` (int64), `desc_motivo` (string)

SQL nativo:

```sql
SELECT 
    id_motivo, 
    id_situacao, 
    desc_motivo

FROM externo.motivo_treinamento
```

## `sgd_externo_programacao`

- **Origem:** Postgres · base `DB_SGD`
- `externo.programacao` ← import-sgd-diario (substitui janela de 5 dia(s))
- **Colunas entregues:** `id_programacoes` (int64), `id_externos` (int64), `descricao` (string), `dt_inicio` (date), `duracao` (int64), `id_usuarios_resp` (int64), `id_situacoes` (int64), `tempo_treinamento` (int64), `instrucoes` (string), `id_local_treinamento` (int64), `id_categorias` (int64), `id_usuarios_cadastro` (int64)

SQL nativo:

```sql
SELECT 
    id_programacoes, 
    id_externos, 
    descricao, 
    dt_inicio::date, 
    duracao, 
    id_usuarios_resp, 
    id_situacoes, 
    tempo_treinamento, 
    instrucoes, 
    id_local_treinamento, 
    id_categorias, 
    id_usuarios_cadastro
FROM externo.programacao
```

## `sgd_externo_situacao`

- **Origem:** Postgres · base `DB_SGD`
- `externo.situacoes` ← import-sgd-diario (recarga TOTAL)
- **Colunas entregues:** `id_situacao` (int64), `desc_situacao` (string), `id_situacao_grupo` (int64)

SQL nativo:

```sql
SELECT 
    id_situacao, 
    desc_situacao, 
    id_situacao_grupo
FROM externo.situacoes
```

## `sgd_externo_treinamentos`

- **Origem:** Postgres · base `DB_SGD`
- `externo.treinamento` ← import-sgd-diario (recarga TOTAL)
- `public.sgd_sa_module` ← import-sgd-diario (recarga TOTAL)
- `public.sgd_sa_system` ← import-sgd-diario (recarga TOTAL)
- **Colunas entregues:** `id_treinamento` (int64), `sigla` (string), `id_tipo` (int64), `desc_treinamento` (string), `id_situacao` (int64), `id_sistemas` (int64), `id_modulos` (int64), `sistema` (string), `modulo` (string)

SQL nativo:

```sql
SELECT id_treinamento, sigla, id_tipo, desc_treinamento, id_situacao, id_sistemas, id_modulos,
        
            s.description as sistema,
            m.description as modulo
            
            
    FROM externo.treinamento inner JOIN PUBLIC.sgd_sa_system s on s.i_system = id_sistemas
                             inner JOIN public.sgd_sa_module m on m.i_system = id_sistemas and m.i_module = id_modulos    
                                ORDER BY ID_SISTEMAS,ID_MODULOS
```

## `sgd_externo_treinamento_conteudo`

- **Origem:** Postgres · base `DB_SGD`
- `externo.treinamento_conteudo` ← import-sgd-diario (recarga TOTAL)
- **Colunas entregues:** `id_conteudo` (int64), `id_treinamento` (int64), `ordem` (int64), `descricao` (string), `detalhamento` (string), `tempo` (int64), `id_situacao` (int64), `concluido` (int64)

SQL nativo:

```sql
SELECT 
id_conteudo, 
id_treinamento, 
ordem,
descricao, 
detalhamento, 
tempo, 
id_situacao, 
concluido
    FROM externo.treinamento_conteudo
```

## `sgd_externo_treinamento_programacao`

- **Origem:** Postgres · base `DB_SGD`
- `externo.treinamento_programacao` ← import-sgd-diario (substitui janela de 5 dia(s))
- **Colunas entregues:** `id_treinamento_programacao` (int64), `id_externo` (int64), `id_programacoes` (int64), `id_treinamento` (int64), `id_conteudo` (int64), `id_situacao` (int64), `concluido` (int64), `prazo` (date), `i_produtos` (int64), `entrada` (date)

SQL nativo:

```sql
SELECT 
id_treinamento_programacao, 
id_externo, 
id_programacoes, 
id_treinamento, 
id_conteudo, 
id_situacao, 
concluido, 
prazo, 
i_produtos, 
entrada
    FROM externo.treinamento_programacao
```

## `sgd_externo_treinamento_programacao_usuarios`

- **Origem:** Postgres · base `DB_SGD`
- `externo.treinamento_programacao_usuario` ← import-sgd-diario (recarga TOTAL)
- **Colunas entregues:** `id_programacao_usuarios` (int64), `id_programacoes` (int64), `id_treinamento` (int64), `i_usuarios` (int64), `i_programacao_categoria` (int64), `i_categorias` (int64)

SQL nativo:

```sql
SELECT 
id_programacao_usuarios,
id_programacoes, 
id_treinamento, 
i_usuarios, 
i_programacao_categoria, 
i_categorias
    FROM externo.treinamento_programacao_usuario
```
