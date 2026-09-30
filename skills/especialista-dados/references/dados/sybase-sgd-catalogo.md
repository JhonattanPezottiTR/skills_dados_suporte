# Catálogo de objetos Sybase liberados (SGD · SGSAI · CTS)

> Última atualização: 2026-09-30 · Fonte: Maestro v1.9.9 (`analytics-bi-dominio-orquestrador`) — `shared/sybase_objetos.py` + varredura de `modules/**`
> **Gerado automaticamente** por `scripts/mapear_maestro.py` — não editar à mão (regras e contexto de negócio ficam em `dados-sgd-regras-e-joins.md`).

**372 objetos liberados** ao login de BI. Engine SAP SQL Anywhere 17 (família Sybase). Todo SQL novo deve usar **somente** estes objetos (views `vw_*` e funções), nunca tabela física — regra do Maestro (reg. 0207/0209): objeto fora da lista quebra o build.

Nomes em três partes (`sgd.bethadba.vw_x`) indicam o banco; o mesmo nome de view pode existir em bancos diferentes com conteúdo diferente (ex.: `vw_modulos` em `sgd` e `cts`).

## Banco `sgd` (314 objetos)

### Agenda

| Objeto | Usado por (jobs/módulos) |
|---|---|
| `bethadba.vw_agenda` | import-cts/import-agendas (lib _import_dominio), produtividade-pendencia-realtime |
| `bethadba.vw_agenda_motivos_ausencias` | import-cts/import-agendas (lib _import_dominio), import-sgd-diario/meiodia/observacoes/consultas (lib _import_sgd), produtividade-pendencia-realtime |
| `bethadba.vw_agenda_tipos` | import-cts/import-agendas (lib _import_dominio), import-sgd-diario/meiodia/observacoes/consultas (lib _import_sgd), produtividade-pendencia-realtime |
| `bethadba.vw_feriados` | import-cts/import-agendas (lib _import_dominio) |

### CTS / TRIA

| Objeto | Usado por (jobs/módulos) |
|---|---|
| `bethadba.vw_cts_contagem_acessos` | import-cts/import-agendas (lib _import_dominio) |
| `bethadba.vw_cts_modulos_solucoes` | import-cts/import-agendas (lib _import_dominio) |
| `bethadba.vw_cts_palavras_chaves_hist` | import-cts/import-agendas (lib _import_dominio) |
| `bethadba.vw_cts_perfil_cliente` | import-cts/import-agendas (lib _import_dominio) |
| `bethadba.vw_cts_perfil_cliente_solucoes` | import-cts/import-agendas (lib _import_dominio) |
| `bethadba.vw_cts_pesquisa_conteudos` | import-cts/import-agendas (lib _import_dominio) |
| `bethadba.vw_cts_pesquisa_satisfacoes` | import-cts/import-agendas (lib _import_dominio) |
| `bethadba.vw_cts_solucoes` | import-cts/import-agendas (lib _import_dominio) |
| `bethadba.vw_cts_solucoes_excluidas` | import-cts/import-agendas (lib _import_dominio) |
| `bethadba.vw_cts_solucoes_historico_responsaveis` | import-cts/import-agendas (lib _import_dominio) |

### Clientes, contratos e produtos

| Objeto | Usado por (jobs/módulos) |
|---|---|
| `bethadba.vw_adendos` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_ceprodutos` | import-sgd-diario/meiodia/observacoes/consultas (lib _import_sgd) |
| `bethadba.vw_cmcontratos` | import-cts/import-agendas (lib _import_dominio), import-sgd-diario/meiodia/observacoes/consultas (lib _import_sgd) |
| `bethadba.vw_cmcontratos_hist_usuarios` | import-sgd-diario/meiodia/observacoes/consultas (lib _import_sgd) |
| `bethadba.vw_cmcontratos_hist_valores` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_cmversoes` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_contratos` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_gecidades` | import-cts/import-agendas (lib _import_dominio), import-sgd-diario/meiodia/observacoes/consultas (lib _import_sgd) |
| `bethadba.vw_geclientes` | import-cts/import-agendas (lib _import_dominio), import-sgd-diario/meiodia/observacoes/consultas (lib _import_sgd), produtividade-pendencia-realtime |
| `bethadba.vw_geclientes_contatos_adicionais` | import-sgd-diario/meiodia/observacoes/consultas (lib _import_sgd) |
| `bethadba.vw_geclientes_contratacoes_onbalance` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_geclientes_eventuais` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_geclientes_observacoes` | import-cts/import-agendas (lib _import_dominio), import-sgd-diario/meiodia/observacoes/consultas (lib _import_sgd), import-sgd-observacoes |
| `bethadba.vw_geestados` | import-cts/import-agendas (lib _import_dominio), import-sgd-diario/meiodia/observacoes/consultas (lib _import_sgd) |
| `bethadba.vw_gefontes` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_gemunicipios` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_geregiaocli` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_gerepresentantes` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_gerepresentantes_estados` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_gerepresentantes_regioes` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_gerestricoes_representantes` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_gesegmentos` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_revendas` | import-cts/import-agendas (lib _import_dominio), import-sgd-diario/meiodia/observacoes/consultas (lib _import_sgd), produtividade-pendencia-realtime |
| `bethadba.vw_revendas_fusos` | — (liberado, sem uso no Maestro) |

### Conversões

| Objeto | Usado por (jobs/módulos) |
|---|---|
| `bethadba.vw_conversao_prioridade_interna_historicos` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_conversao_prospescts_desconsiderados` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_conversao_situacoes` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_conversao_tramites` | import-sgd-diario/meiodia/observacoes/consultas (lib _import_sgd) |
| `bethadba.vw_conversoes` | import-sgd-diario/meiodia/observacoes/consultas (lib _import_sgd) |

### Funções / procedures

| Objeto | Usado por (jobs/módulos) |
|---|---|
| `bethadba.amostragem_ssc_ia_ssi30167` | — (liberado, sem uso no Maestro) |
| `bethadba.cancelamentosdominioweb` | — (liberado, sem uso no Maestro) |
| `bethadba.f_get_gestor_suporte` | import-cts/import-agendas (lib _import_dominio), produtividade-pendencia-realtime |
| `bethadba.f_get_tempo_entre_situacoes_sscs` | — (liberado, sem uso no Maestro) |
| `bethadba.f_get_tempo_pendente_ssc` | produtividade-pendencia-realtime |
| `bethadba.fg_remove_acentuacao` | — (liberado, sem uso no Maestro) |
| `bethadba.minutosuteis` | import-sgd-diario/meiodia/observacoes/consultas (lib _import_sgd), produtividade-pendencia-realtime |
| `bethadba.p_dias_uteis_do_periodo` | — (liberado, sem uso no Maestro) |
| `bethadba.p_ebs_dados_suporte_por_dia` | — (liberado, sem uso no Maestro) |
| `bethadba.p_listagem_clientesativos_usuariosativos_email` | — (liberado, sem uso no Maestro) |
| `bethadba.p_listagem_ssc_mesmoclientesistemamodulo` | — (liberado, sem uso no Maestro) |
| `bethadba.prel_demanda_suporte_cliente` | — (liberado, sem uso no Maestro) |
| `bethadba.prel_demanda_usuarios_normalizados` | — (liberado, sem uso no Maestro) |
| `bethadba.rel_lista_ocorrencias` | — (liberado, sem uso no Maestro) |
| `bethadba.rel_planilhas_clientes_ativos_unidade` | — (liberado, sem uso no Maestro) |
| `bethadba.rel_planilhas_dados_folha` | — (liberado, sem uso no Maestro) |
| `bethadba.rel_planilhas_listagem_pendencias_sss` | — (liberado, sem uso no Maestro) |
| `bethadba.rel_planilhas_listagem_sscs` | — (liberado, sem uso no Maestro) |
| `bethadba.rel_planilhas_ssc_detalhada` | — (liberado, sem uso no Maestro) |
| `bethadba.rel_planilhas_sscs_concluidas_por_solucoes` | — (liberado, sem uso no Maestro) |
| `bethadba.rel_planilhas_tempo_resposta_atendimentos_sss` | — (liberado, sem uso no Maestro) |
| `bethadba.rel_planilhas_tempos_atendimentos_sscs` | — (liberado, sem uso no Maestro) |
| `bethadba.rel_planilhas_vida_util_sss` | — (liberado, sem uso no Maestro) |
| `bethadba.relatorioprodutividadesuporteinterno` | — (liberado, sem uso no Maestro) |
| `bethadba.relatorioresumochamadospendentes` | — (liberado, sem uso no Maestro) |
| `bethadba.relatoriosaldopendenciaspordia` | — (liberado, sem uso no Maestro) |
| `bethadba.relatoriosaldopendenciasspordia` | — (liberado, sem uso no Maestro) |
| `bethadba.relatoriosscpordia` | — (liberado, sem uso no Maestro) |
| `bethadba.relatoriotemporespostaanalitico` | import-sgd-diario/meiodia/observacoes/consultas (lib _import_sgd) |
| `bethadba.removerhtml` | import-cts/import-agendas (lib _import_dominio), import-sgd-diario/meiodia/observacoes/consultas (lib _import_sgd) |
| `bethadba.removerhtmleacentuacao` | import-sgd-diario/meiodia/observacoes/consultas (lib _import_sgd) |

### IA / Open Arena

| Objeto | Usado por (jobs/módulos) |
|---|---|
| `bethadba.vw_completion_ai_ssc_chat` | import-sgd-diario/meiodia/observacoes/consultas (lib _import_sgd) |
| `bethadba.vw_completion_ia_ssc_chat` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_confg_fluxo_acao_open_arena_interacao` | import-sgd-diario/meiodia/observacoes/consultas (lib _import_sgd) |
| `bethadba.vw_configuracao_fluxo_acao_open_arena` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_ia_ssc_chat` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_prompt_ia` | — (liberado, sem uso no Maestro) |

### Implantação e treinamentos

| Objeto | Usado por (jobs/módulos) |
|---|---|
| `bethadba.vw_externo` | import-sgd-diario/meiodia/observacoes/consultas (lib _import_sgd) |
| `bethadba.vw_externo_atendimento_implantacoes_reduzir` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_externo_cancelados` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_externo_categoria` | import-sgd-diario/meiodia/observacoes/consultas (lib _import_sgd) |
| `bethadba.vw_externo_checklist` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_externo_checklist_itens` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_externo_faturamento` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_externo_forma_treinamento` | import-sgd-diario/meiodia/observacoes/consultas (lib _import_sgd) |
| `bethadba.vw_externo_historico` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_externo_local_treinamento` | import-sgd-diario/meiodia/observacoes/consultas (lib _import_sgd) |
| `bethadba.vw_externo_programacao` | import-sgd-diario/meiodia/observacoes/consultas (lib _import_sgd) |
| `bethadba.vw_externo_programacao_categoria_treinamento` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_externo_programacao_cronograma` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_externo_programacao_cronograma_anotacao` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_externo_situacoes` | import-sgd-diario/meiodia/observacoes/consultas (lib _import_sgd) |
| `bethadba.vw_externo_treinamento` | import-sgd-diario/meiodia/observacoes/consultas (lib _import_sgd) |
| `bethadba.vw_externo_treinamento_conteudo` | import-sgd-diario/meiodia/observacoes/consultas (lib _import_sgd) |
| `bethadba.vw_externo_treinamento_motivo` | import-sgd-diario/meiodia/observacoes/consultas (lib _import_sgd) |
| `bethadba.vw_externo_treinamento_porte` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_externo_treinamento_programa` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_externo_treinamento_programacao` | import-sgd-diario/meiodia/observacoes/consultas (lib _import_sgd) |
| `bethadba.vw_externo_treinamento_programacao_tempo` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_externo_treinamento_programacao_usuario` | import-sgd-diario/meiodia/observacoes/consultas (lib _import_sgd) |
| `bethadba.vw_externo_treinamento_situacao` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_externos_historicos_dados` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_externos_questionarios` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_externos_questionarios_relatorios` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_externos_questionarios_respostas` | — (liberado, sem uso no Maestro) |

### Liberações

| Objeto | Usado por (jobs/módulos) |
|---|---|
| `bethadba.vw_liberacao_chat` | import-webchat-plug |
| `bethadba.vw_liliberacoes` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_liliberacoes_bancos` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_liliberacoes_cortesias` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_liliberacoes_hist` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_liliberacoes_hist_tecnico` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_liliberacoes_hist_tecnico_acessos_modulos_negados` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_liliberacoes_hist_tecnico_acessos_negados` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_liliberacoes_hist_tecnico_contabil` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_liliberacoes_hist_tecnico_esocial` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_liliberacoes_hist_tecnico_importacao_concorrentes` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_liliberacoes_hist_tecnico_modulos` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_liliberacoes_parametros` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_liliberacoes_sync` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_lisituacoes` | — (liberado, sem uso no Maestro) |

### Ocorrências

| Objeto | Usado por (jobs/módulos) |
|---|---|
| `bethadba.view_sla_ocorrencia` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_ocorrencia` | import-sgd-diario/meiodia/observacoes/consultas (lib _import_sgd) |
| `bethadba.vw_ocorrencia_anotacao` | import-sgd-diario/meiodia/observacoes/consultas (lib _import_sgd) |
| `bethadba.vw_ocorrencia_area` | import-sgd-diario/meiodia/observacoes/consultas (lib _import_sgd) |
| `bethadba.vw_ocorrencia_categoria` | import-sgd-diario/meiodia/observacoes/consultas (lib _import_sgd) |
| `bethadba.vw_ocorrencia_prioridade` | import-sgd-diario/meiodia/observacoes/consultas (lib _import_sgd) |
| `bethadba.vw_ocorrencia_sane` | import-sgd-diario/meiodia/observacoes/consultas (lib _import_sgd) |
| `bethadba.vw_ocorrencia_setor` | import-sgd-diario/meiodia/observacoes/consultas (lib _import_sgd) |
| `bethadba.vw_ocorrencia_situacao` | import-sgd-diario/meiodia/observacoes/consultas (lib _import_sgd) |
| `bethadba.vw_ocorrencia_situacao_de_para` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_ocorrencia_ss` | import-sgd-diario/meiodia/observacoes/consultas (lib _import_sgd) |
| `bethadba.vw_ocorrencia_ssc` | import-sgd-diario/meiodia/observacoes/consultas (lib _import_sgd) |
| `bethadba.vw_ocorrencia_tramite` | import-sgd-diario/meiodia/observacoes/consultas (lib _import_sgd) |
| `bethadba.vw_subtipos_ocorrencias` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_tipos_ocorrencias` | — (liberado, sem uso no Maestro) |

### Outros

| Objeto | Usado por (jobs/módulos) |
|---|---|
| `bethadba.view_planilha_detalhamento_tempo_interno_ssc` | — (liberado, sem uso no Maestro) |
| `bethadba.view_tramites_aguardando_resposta_interna` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_anexos` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_dado_relatorio_sose` | import-sgd-diario/meiodia/observacoes/consultas (lib _import_sgd) |
| `bethadba.vw_dado_relatorio_sose_tramites` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_dado_relatorio_treinamento_sose` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_dispositivos` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_dispositivos_so_estacao` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_keywords` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_navegadores` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_pa_metas` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_palavra_chaves_pesquisa` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_preferencias_pesquisas` | import-cts/import-agendas (lib _import_dominio) |
| `bethadba.vw_ranking_melhorias_votacoes` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_segmentos_roles` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_so_estacao` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_so_estacao_navegadores` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_so_servidor` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_soses_assinaturas` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_soses_situacoes` | import-sgd-diario/meiodia/observacoes/consultas (lib _import_sgd) |
| `bethadba.vw_swift_situacao_migracao_onvio` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_swift_situacao_migracao_onvio_historico` | — (liberado, sem uso no Maestro) |

### Perfis e SLA

| Objeto | Usado por (jobs/módulos) |
|---|---|
| `bethadba.vw_perfil_sla` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_perfil_sla_historico` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_perfil_sla_ss` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_perfis_atendimentos` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_perfis_atendimentos_classificacoes` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_perfis_atendimentos_modulos` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_perfis_atendimentos_sistemas` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_perfis_atendimentos_topicos` | — (liberado, sem uso no Maestro) |

### Pesquisa NPS

| Objeto | Usado por (jobs/módulos) |
|---|---|
| `bethadba.vw_pesquisa_nps` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_pesquisa_nps_area` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_pesquisa_nps_classificacao` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_pesquisa_nps_classificacao_pendencia` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_pesquisa_nps_coluna_importar` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_pesquisa_nps_historico` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_pesquisa_nps_motivo` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_pesquisa_nps_pesquisa` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_pesquisa_nps_tipo` | — (liberado, sem uso no Maestro) |

### Pós-venda

| Objeto | Usado por (jobs/módulos) |
|---|---|
| `bethadba.vw_pos_venda` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_pos_venda_analise` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_pos_venda_atendimento` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_pos_venda_atividade_situacao` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_pos_venda_atividades` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_pos_venda_cargo` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_pos_venda_categorias` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_pos_venda_checklist` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_pos_venda_checklist_itens` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_pos_venda_diagnostico` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_pos_venda_historico` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_pos_venda_programacao` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_pos_venda_requisicao` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_pos_venda_situacoes` | — (liberado, sem uso no Maestro) |

### SA / NE

| Objeto | Usado por (jobs/módulos) |
|---|---|
| `bethadba.vw_feedback_sa` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_forum_sa` | import-sgd-diario/meiodia/observacoes/consultas (lib _import_sgd) |
| `bethadba.vw_forum_sa_classificacoes` | import-sgd-diario/meiodia/observacoes/consultas (lib _import_sgd) |
| `bethadba.vw_forum_sa_situacoes` | import-sgd-diario/meiodia/observacoes/consultas (lib _import_sgd) |
| `bethadba.vw_psai_situacoes` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_sane_interna` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_sane_interna_situacao` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_sane_interna_situacao_grupo` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_sane_ssc_demanda` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_sane_ssc_demanda_log` | — (liberado, sem uso no Maestro) |

### SR

| Objeto | Usado por (jobs/módulos) |
|---|---|
| `bethadba.vw_sr` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_sr_situacoes` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_sr_tipos` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_sr_tramites` | — (liberado, sem uso no Maestro) |

### SS (N2)

| Objeto | Usado por (jobs/módulos) |
|---|---|
| `bethadba.vw_ss` | import-sgd-diario/meiodia/observacoes/consultas (lib _import_sgd), produtividade-pendencia-realtime |
| `bethadba.vw_ss_anotacoes` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_ss_categorias` | import-sgd-diario/meiodia/observacoes/consultas (lib _import_sgd) |
| `bethadba.vw_ss_motivos_insatisfacao` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_ss_prioridade_interna_historicos` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_ss_situacoes` | import-sgd-diario/meiodia/observacoes/consultas (lib _import_sgd), produtividade-pendencia-realtime |
| `bethadba.vw_ss_situacoes_permissoes_realizar` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_ss_situacoes_restricoes_realizar` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_ss_tramites` | import-sgd-diario/meiodia/observacoes/consultas (lib _import_sgd), produtividade-pendencia-realtime |
| `bethadba.vw_ss_usuarios_seguir` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_ss_usuarios_seguir_historico` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_sss_classificacao_modulos` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_sss_classificacoes` | import-cts/import-agendas (lib _import_dominio), import-sgd-diario/meiodia/observacoes/consultas (lib _import_sgd), produtividade-pendencia-realtime |
| `bethadba.vw_sss_classificacoes_alocacoes` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_sss_classificacoes_roles` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_sss_publicacao` | — (liberado, sem uso no Maestro) |

### SSC (solicitações N1)

| Objeto | Usado por (jobs/módulos) |
|---|---|
| `bethadba.vw_ssc` | import-cts/import-agendas (lib _import_dominio), import-sgd-diario/meiodia/observacoes/consultas (lib _import_sgd), produtividade-pendencia-realtime |
| `bethadba.vw_ssc_anotacoes` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_ssc_avaliacao_tria` | import-cts/import-agendas (lib _import_dominio) |
| `bethadba.vw_ssc_categorias` | import-sgd-diario/meiodia/observacoes/consultas (lib _import_sgd) |
| `bethadba.vw_ssc_conversoes` | import-sgd-diario/meiodia/observacoes/consultas (lib _import_sgd) |
| `bethadba.vw_ssc_cookies_backup_nuvem` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_ssc_dados_faturamentos` | import-sgd-diario/meiodia/observacoes/consultas (lib _import_sgd) |
| `bethadba.vw_ssc_destaque_atencao` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_ssc_download_backup_historico` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_ssc_historico_alteracao_usuario` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_ssc_motivos_insatisfacao` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_ssc_origens` | import-cts/import-agendas (lib _import_dominio), import-sgd-diario/meiodia/observacoes/consultas (lib _import_sgd), produtividade-pendencia-realtime |
| `bethadba.vw_ssc_pesquisa_nps` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_ssc_pesquisa_resposta_utiliza_solucao` | import-sgd-diario/meiodia/observacoes/consultas (lib _import_sgd) |
| `bethadba.vw_ssc_pre_cadastro` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_ssc_pre_cadastro_anexos` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_ssc_pre_cadastro_tramites` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_ssc_pre_chat` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_ssc_prioridades_historicos` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_ssc_responsaveis` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_ssc_responsaveis_revendas` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_ssc_sincronizacao_fila` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_ssc_situacoes` | import-cts/import-agendas (lib _import_dominio), import-sgd-diario/meiodia/observacoes/consultas (lib _import_sgd), produtividade-pendencia-realtime |
| `bethadba.vw_ssc_situacoes_permissoes_realizar` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_ssc_solicitacoes_agendamentos` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_ssc_solicitacoes_arquivos_onbalance` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_ssc_solicitacoes_backup` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_ssc_sqs_dead_letter` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_ssc_sr` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_ssc_ss` | import-sgd-diario/meiodia/observacoes/consultas (lib _import_sgd) |
| `bethadba.vw_ssc_ssql` | import-sgd-diario/meiodia/observacoes/consultas (lib _import_sgd) |
| `bethadba.vw_ssc_status_conclusao_solucao` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_ssc_temp` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_ssc_tipos_servicos_soses` | import-sgd-diario/meiodia/observacoes/consultas (lib _import_sgd) |
| `bethadba.vw_ssc_tramite_anexo_sa_ne` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_ssc_tramite_anexo_ssc` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_ssc_tramite_responsavel` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_ssc_tramites` | import-sgd-diario/meiodia/observacoes/consultas (lib _import_sgd), produtividade-pendencia-realtime |
| `bethadba.vw_ssc_tramites_respostas` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_ssc_usuarios_seguir` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_ssc_usuarios_seguir_historicos` | — (liberado, sem uso no Maestro) |

### SSQL

| Objeto | Usado por (jobs/módulos) |
|---|---|
| `bethadba.vw_ssql` | import-sgd-diario/meiodia/observacoes/consultas (lib _import_sgd) |
| `bethadba.vw_ssql_prioridade_interna_historicos` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_ssql_situacoes` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_ssql_tramites` | import-sgd-diario/meiodia/observacoes/consultas (lib _import_sgd) |

### Sistemas, módulos, tópicos e classificações

| Objeto | Usado por (jobs/módulos) |
|---|---|
| `bethadba.vw_meios_acesso` | import-sgd-diario/meiodia/observacoes/consultas (lib _import_sgd), produtividade-pendencia-realtime |
| `bethadba.vw_meios_retorno` | produtividade-pendencia-realtime |
| `bethadba.vw_modulos` | import-cts/import-agendas (lib _import_dominio), import-sgd-diario/meiodia/observacoes/consultas (lib _import_sgd), produtividade-pendencia-realtime |
| `bethadba.vw_sistemas` | import-cts/import-agendas (lib _import_dominio), import-sgd-diario/meiodia/observacoes/consultas (lib _import_sgd), produtividade-pendencia-realtime |
| `bethadba.vw_sistemas_dispositivos` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_sistemas_produtos` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_sistemas_roles` | import-cts/import-agendas (lib _import_dominio) |
| `bethadba.vw_sistemas_so_estacao` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_submodulos` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_topicos_suportes` | import-cts/import-agendas (lib _import_dominio), import-sgd-diario/meiodia/observacoes/consultas (lib _import_sgd), produtividade-pendencia-realtime |
| `bethadba.vw_versoes` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_versoes_situacoes` | — (liberado, sem uso no Maestro) |

### Solicitações de agendamento

| Objeto | Usado por (jobs/módulos) |
|---|---|
| `bethadba.vw_solicitacoes_agendamentos` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_solicitacoes_agendamentos_programacoes` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_solicitacoes_agendamentos_programacoes_treinamentos` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_solicitacoes_agendamentos_situacoes` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_solicitacoes_agendamentos_situacoes_permitidas` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_solicitacoes_agendamentos_tramites` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_solicitacoes_agendamentos_treinamentos` | — (liberado, sem uso no Maestro) |

### Tarefas

| Objeto | Usado por (jobs/módulos) |
|---|---|
| `bethadba.vw_tarefas` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_tarefas_anotacoes_tipos` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_tarefas_categorias` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_tarefas_convidados` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_tarefas_convidados_situacoes` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_tarefas_historicos` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_tarefas_quadrantes` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_tarefas_situacoes` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_tarefas_situacoes_tramites` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_tarefas_usuarios_emails` | — (liberado, sem uso no Maestro) |

### Usuários, alocação e cargos

| Objeto | Usado por (jobs/módulos) |
|---|---|
| `bethadba.vw_alocacao` | genesys-sla, import-sgd-diario/meiodia/observacoes/consultas (lib _import_sgd), produtividade-pendencia-realtime |
| `bethadba.vw_cargos` | import-sgd-diario/meiodia/observacoes/consultas (lib _import_sgd) |
| `bethadba.vw_normalizacao_usuarios` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_setores` | import-cts/import-agendas (lib _import_dominio) |
| `bethadba.vw_usuarios` | import-cts/import-agendas (lib _import_dominio) |
| `bethadba.vw_usuarios_acessos` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_usuarios_acessos_backup_2` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_usuarios_alocacao_historico` | genesys-sla, import-sgd-diario/meiodia/observacoes/consultas (lib _import_sgd), produtividade-pendencia-realtime |
| `bethadba.vw_usuarios_auditoria` | genesys-import, import-cts/import-agendas (lib _import_dominio), import-sgd-diario/meiodia/observacoes/consultas (lib _import_sgd) |
| `bethadba.vw_usuarios_cargo_historico` | import-sgd-diario/meiodia/observacoes/consultas (lib _import_sgd) |
| `bethadba.vw_usuarios_dados` | genesys-import, import-cts/import-agendas (lib _import_dominio), import-sgd-diario/meiodia/observacoes/consultas (lib _import_sgd), produtividade-pendencia-realtime |
| `bethadba.vw_usuarios_departamentos_onvio` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_usuarios_gestor_historico` | import-sgd-diario/meiodia/observacoes/consultas (lib _import_sgd), produtividade-pendencia-realtime |
| `bethadba.vw_usuarios_horario_trabalho_historico` | import-sgd-diario/meiodia/observacoes/consultas (lib _import_sgd) |
| `bethadba.vw_usuarios_informacoes_adicionais` | import-sgd-diario/meiodia/observacoes/consultas (lib _import_sgd) |
| `bethadba.vw_usuarios_permissoes` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_usuarios_revendas` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_usuarios_roles` | import-cts/import-agendas (lib _import_dominio) |
| `power_bi.vw_usuarios` | genesys-import, genesys-sla, import-cts/import-agendas (lib _import_dominio), import-sgd-diario/meiodia/observacoes/consultas (lib _import_sgd), produtividade-pendencia-realtime |

## Banco `sgsai` (27 objetos)

### Funções / procedures

| Objeto | Usado por (jobs/módulos) |
|---|---|
| `bethadba.removerhtml` | import-cts/import-agendas (lib _import_dominio), import-sgd-diario/meiodia/observacoes/consultas (lib _import_sgd) |

### SA / NE

| Objeto | Usado por (jobs/módulos) |
|---|---|
| `bethadba.vw_feedback_sa` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_forum_sa` | import-sgd-diario/meiodia/observacoes/consultas (lib _import_sgd) |
| `bethadba.vw_forum_sa_classificacoes` | import-sgd-diario/meiodia/observacoes/consultas (lib _import_sgd) |
| `bethadba.vw_forum_sa_motivos_reprovacao` | import-sgd-diario/meiodia/observacoes/consultas (lib _import_sgd) |
| `bethadba.vw_forum_sa_prioridades` | import-sgd-diario/meiodia/observacoes/consultas (lib _import_sgd) |
| `bethadba.vw_forum_sa_sai` | import-sgd-diario/meiodia/observacoes/consultas (lib _import_sgd) |
| `bethadba.vw_forum_sa_situacoes` | import-sgd-diario/meiodia/observacoes/consultas (lib _import_sgd) |
| `bethadba.vw_forum_sa_situacoes_tramites` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_forum_sa_topicos` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_psai` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_psai_situacoes` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_psai_tramites` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_sai` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_sai_classif_seq` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_sai_linhas` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_sai_linhas_situacoes` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_sai_previsao` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_sai_prioridades` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_sai_situacoes` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_sai_tramites` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_sai_versoes` | — (liberado, sem uso no Maestro) |

### Sistemas, módulos, tópicos e classificações

| Objeto | Usado por (jobs/módulos) |
|---|---|
| `bethadba.vw_modulos` | import-cts/import-agendas (lib _import_dominio), import-sgd-diario/meiodia/observacoes/consultas (lib _import_sgd), produtividade-pendencia-realtime |
| `bethadba.vw_sistemas` | import-cts/import-agendas (lib _import_dominio), import-sgd-diario/meiodia/observacoes/consultas (lib _import_sgd), produtividade-pendencia-realtime |
| `bethadba.vw_versoes` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_versoes_situacoes` | — (liberado, sem uso no Maestro) |
| `bethadba.vw_versoes_tramites` | — (liberado, sem uso no Maestro) |

## Banco `cts` (31 objetos)

### CTS / TRIA

| Objeto | Usado por (jobs/módulos) |
|---|---|
| `bethadba.vw_cts_chat_interacoes` | import-cts/import-agendas (lib _import_dominio) |
| `bethadba.vw_cts_contagem_acessos` | import-cts/import-agendas (lib _import_dominio) |
| `bethadba.vw_cts_gpt_sugestao` | import-cts/import-agendas (lib _import_dominio) |
| `bethadba.vw_cts_modulos_solucoes` | import-cts/import-agendas (lib _import_dominio) |
| `bethadba.vw_cts_palavras_chaves_hist` | import-cts/import-agendas (lib _import_dominio) |
| `bethadba.vw_cts_perfil_cliente` | import-cts/import-agendas (lib _import_dominio) |
| `bethadba.vw_cts_perfil_cliente_solucoes` | import-cts/import-agendas (lib _import_dominio) |
| `bethadba.vw_cts_pesquisa_conteudos` | import-cts/import-agendas (lib _import_dominio) |
| `bethadba.vw_cts_pesquisa_satisfacoes` | import-cts/import-agendas (lib _import_dominio) |
| `bethadba.vw_cts_solucoes` | import-cts/import-agendas (lib _import_dominio) |
| `bethadba.vw_cts_solucoes_excluidas` | import-cts/import-agendas (lib _import_dominio) |
| `bethadba.vw_cts_solucoes_futuras` | import-cts/import-agendas (lib _import_dominio) |
| `bethadba.vw_cts_solucoes_historico` | import-cts/import-agendas (lib _import_dominio) |
| `bethadba.vw_cts_solucoes_historico_responsaveis` | import-cts/import-agendas (lib _import_dominio) |
| `bethadba.vw_cts_solucoes_intencoes` | import-cts/import-agendas (lib _import_dominio) |
| `bethadba.vw_cts_solucoes_revisao_motivos` | import-cts/import-agendas (lib _import_dominio) |
| `bethadba.vw_cts_solucoes_revisoes` | import-cts/import-agendas (lib _import_dominio) |
| `bethadba.vw_cts_solucoes_solr` | import-cts/import-agendas (lib _import_dominio) |
| `bethadba.vw_cts_usuarios_preferencias` | import-cts/import-agendas (lib _import_dominio) |
| `bethadba.vw_cts_usuarios_solucoes_favoritas` | import-cts/import-agendas (lib _import_dominio) |
| `bethadba.vw_suportes_tria` | import-cts/import-agendas (lib _import_dominio) |
| `bethadba.vw_topicos_telefonia` | import-cts/import-agendas (lib _import_dominio) |

### Clientes, contratos e produtos

| Objeto | Usado por (jobs/módulos) |
|---|---|
| `bethadba.vw_central_telefonia` | import-cts/import-agendas (lib _import_dominio) |

### SS (N2)

| Objeto | Usado por (jobs/módulos) |
|---|---|
| `bethadba.vw_sss_classificacoes` | import-cts/import-agendas (lib _import_dominio), import-sgd-diario/meiodia/observacoes/consultas (lib _import_sgd), produtividade-pendencia-realtime |

### SSC (solicitações N1)

| Objeto | Usado por (jobs/módulos) |
|---|---|
| `bethadba.vw_ssc_origens` | import-cts/import-agendas (lib _import_dominio), import-sgd-diario/meiodia/observacoes/consultas (lib _import_sgd), produtividade-pendencia-realtime |

### Sistemas, módulos, tópicos e classificações

| Objeto | Usado por (jobs/módulos) |
|---|---|
| `bethadba.vw_modulos` | import-cts/import-agendas (lib _import_dominio), import-sgd-diario/meiodia/observacoes/consultas (lib _import_sgd), produtividade-pendencia-realtime |
| `bethadba.vw_sistemas` | import-cts/import-agendas (lib _import_dominio), import-sgd-diario/meiodia/observacoes/consultas (lib _import_sgd), produtividade-pendencia-realtime |
| `bethadba.vw_sistemas_roles` | import-cts/import-agendas (lib _import_dominio) |
| `bethadba.vw_topicos_suportes` | import-cts/import-agendas (lib _import_dominio), import-sgd-diario/meiodia/observacoes/consultas (lib _import_sgd), produtividade-pendencia-realtime |

### Usuários, alocação e cargos

| Objeto | Usado por (jobs/módulos) |
|---|---|
| `bethadba.vw_usuarios` | import-cts/import-agendas (lib _import_dominio) |
| `bethadba.vw_usuarios_roles` | import-cts/import-agendas (lib _import_dominio) |

## Referências fora da allowlist (comentários, legado ou tabelas físicas)

Aparecem no código mas não estão em `sybase_objetos.py`. Não usar em SQL novo.

- `bethadba.agenda` — import-cts/import-agendas (lib _import_dominio)
- `bethadba.cts_chat_interacoes` — import-cts/import-agendas (lib _import_dominio)
- `bethadba.externo_` — import-sgd-diario/meiodia/observacoes/consultas (lib _import_sgd)
- `bethadba.geclientes` — import-cts/import-agendas (lib _import_dominio)
- `bethadba.usuarios_roles` — import-cts/import-agendas (lib _import_dominio)
- `bethadba.vw_` — import-cts/import-agendas (lib _import_dominio)
- `bethadba.vw_chat_open_arena_interacao` — import-sgd-diario/meiodia/observacoes/consultas (lib _import_sgd)
- `bethadba.vw_cts_` — import-cts/import-agendas (lib _import_dominio)
- `dba.revendas` — import-cts/import-agendas (lib _import_dominio)
