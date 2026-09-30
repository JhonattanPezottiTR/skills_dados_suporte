# Fluxo `TB_SYBASE_SGD_AGENDA`

> Última atualização: 2026-09-30 · Fonte: `TB_SYBASE_SGD_AGENDA.json` (Dataflow Power BI, modificado em 2026-09-09, cultura pt-BR) · **Gerado automaticamente** por `scripts/mapear_fluxos.py`.

| Entidade | Carrega | Origem | Base | Tabelas de origem | Colunas | Último refresh (UTC) |
|---|---|---|---|---|---|---|
| `Agenda` | sim | Sybase (SGD direto) | sgd | `bethadba.f_get_gestor_suporte`, `bethadba.vw_agenda`, `bethadba.vw_agenda_motivos_ausencias`, `bethadba.vw_agenda_tipos`, `bethadba.vw_alocacao`, `bethadba.vw_setores`, `bethadba.vw_usuarios_alocacao_historico`, `bethadba.vw_usuarios_dados`, `power_bi.vw_usuarios` | 26 | 2026-09-29T20:05:32 |

## `Agenda`

- **Origem:** Sybase (SGD direto) · base `sgd`
- **Objetos Sybase:** `bethadba.f_get_gestor_suporte`, `bethadba.vw_agenda`, `bethadba.vw_agenda_motivos_ausencias`, `bethadba.vw_agenda_tipos`, `bethadba.vw_alocacao`, `bethadba.vw_setores`, `bethadba.vw_usuarios_alocacao_historico`, `bethadba.vw_usuarios_dados`, `power_bi.vw_usuarios`
- **Colunas entregues:** `inicio` (string), `fim` (string), `'Last Update: ' || dateformat(now(),'dd/mm/yyyy HH:MM:SS')` (string), `data_inicio` (dateTime), `data_fim` (dateTime), `nome_do_tecnico` (string), `email` (string), `responsavel_lancto` (string), `Lancto_Diferente` (int64), `data_registro` (string), `i_tipos` (int64), `ausencia_tipo` (string), `ausencia_motivo` (string), `descricao` (string), `descricao_agenda` (string), `Gerente` (string), `coordenador` (string), `alocaco_anterior` (int64), `alocaco_tecnico` (string), `setor` (string), `unidade` (string), `h.NomeMes` (string), `DataInicio` (date), `h.dia` (int64), `h.mes` (int64), `h.ano` (int64)

SQL nativo:

```sql
SELECT inicio = left(cast(dateadd(ss,1,dateadd(mm,-2,ymd(year(today()),month(today()),1))) as char ),10),
         fim = cast(dateadd(ss,-1,dateadd(mm,6,ymd(year(today()),month(today()),1))) as char ),
         'Last Update: '||dateformat(now(),'dd/mm/yyyy HH:MM:SS'), 
         data_inicio = cast(agenda.data_inicio as CHAR),
         data_fim = cast(agenda.data_fim as CHAR), 
         nome_do_tecnico = usuarios.nome,
         email = lower(usuarios.email),
         responsavel_lancto = coalesce((select x.nome from power_bi.vw_usuarios as x where x.i_usuarios=agenda.i_usuarios),''),
        Lancto_Diferente = ( case
                                WHEN nome_do_tecnico <> responsavel_lancto then 1
                                else 0 end ),

         data_registro = cast(entrada as char),
         agenda.i_tipos,
         ausencia_tipo = agenda_tipos.descricao,
         ausencia_motivo = agenda_motivos_ausencias.descricao,
         descricao = dateformat(agenda.data_inicio,'HH:MM')||' as '|| dateformat(agenda.data_fim,'HH:MM')||' - '||  nome_do_tecnico,
         descricao_agenda = agenda.descricao,
         Gerente = (select coordenador.nome
                         from power_bi.vw_usuarios as coordenador
                        where coordenador.i_usuarios = bethadba.f_get_gestor_suporte(bethadba.f_get_gestor_suporte(usuarios.i_usuarios))),
         coordenador = (select coordenador.nome
                         from power_bi.vw_usuarios as coordenador
                        where coordenador.i_usuarios = bethadba.f_get_gestor_suporte(usuarios.i_usuarios)),
        alocaco_anterior = (SELECT TOP 1 uah2.i_alocacao_nova
                                FROM bethadba.vw_usuarios_alocacao_historico AS uah2 
                                INNER JOIN bethadba.vw_usuarios_alocacao_historico AS uah ON uah2.i_usuarios = uah.i_usuarios
                                WHERE uah2.i_usuarios = usuarios.i_usuarios
                                    AND uah2.i_historico < usuarios_alocacao_historico.i_historico
                                    AND uah2.i_historico = uah.i_historico
                                ORDER BY uah.i_historico DESC  )  ,           
         alocaco_tecnico = alocacao.descricao,

         CASE 
                WHEN alocacao.i_alocacao IN (2, 3, 4, 11, 29, 30) THEN 'Técnica'
                WHEN alocacao.i_alocacao IN (36) THEN 'Suporte Interno Técnico - Performance'
                WHEN alocacao.i_alocacao IN (10, 8) THEN 'Apoio'
                WHEN alocacao.i_alocacao IN (13,60) THEN 'M.Aprendiz/Estagiário'
                WHEN alocacao.i_alocacao IN (25, 26, 37, 38, 39) THEN 'Folha'
                WHEN alocacao.i_alocacao IN (27, 28) THEN 'Fical/Contábil'
                WHEN alocacao.i_alocacao IN (31) THEN 'AT - Imp/Exp/Imp'
                WHEN alocacao.i_alocacao IN (32) THEN 'Treinamento'
                WHEN alocacao.i_alocacao IN (34) THEN 'Em formação - Monitorado'
                WHEN alocacao.i_alocacao IN (40, 41, 42) THEN 'Secundários'
                WHEN alocacao.i_alocacao IN (43, 44) THEN 'Suporte DW'
                WHEN alocacao.i_alocacao IN (52, 53, 54, 55) THEN 'Folha/Contábil'
                WHEN alocacao.i_alocacao IN (48, 68, 69, 70) THEN 'Chat'
                WHEN alocacao.i_alocacao IN (71) THEN 'Folha/AT Fone'
                WHEN alocacao.i_alocacao IN (72) THEN 'Contábil/AT Fone'
                WHEN alocacao.i_alocacao IN (73) THEN 'Folha/Contábil/AT Fone'
                WHEN alocacao.i_alocacao IN (74) THEN 'Folha/AT Web'
                WHEN alocacao.i_alocacao IN (75) THEN 'Contábil/AT Web'
                WHEN alocacao.i_alocacao IN (76) THEN 'Folha/Contábil/AT Web'
                ELSE 'Outros'
        END AS setor,
        CASE 
            WHEN usuarios.i_revendas IN (102, 144) THEN 'Regional Campinas'
            WHEN usuarios.i_revendas IN (83, 82, 137) THEN 'Regional Sul'
            WHEN usuarios.i_revendas IN (155) THEN 'AT Campinas'
            WHEN usuarios.i_revendas IN (156) THEN 'AT Criciuma'
            WHEN usuarios.i_revendas IN (163) THEN 'AT SP'
            WHEN usuarios.i_revendas IN (1) THEN 'CTD'
            ELSE 'Outras'
        END AS unidade                                                                      
        
    FROM bethadba.vw_agenda AS agenda 
                         inner join bethadba.vw_agenda_tipos AS agenda_tipos
                                 on agenda_tipos.i_agenda_tipos = agenda.i_tipos             
                         left outer join bethadba.vw_agenda_motivos_ausencias AS agenda_motivos_ausencias
                                 on agenda_motivos_ausencias.i_agenda_motivos_ausencias = agenda.i_motivos_ausencias
                         inner join power_bi.vw_usuarios as usuarios
                                 on usuarios.i_usuarios = agenda.i_responsaveis
                and usuarios.i_revendas in(83,102,137,144,155,156,163)/*SP,BA,SUL,Secundarios, POA, curitiba*/
                         inner join bethadba.vw_usuarios_alocacao_historico AS usuarios_alocacao_historico
                                 on usuarios_alocacao_historico.i_usuarios = usuarios.i_usuarios
                                and usuarios_alocacao_historico.i_historico = (select max(uah.i_historico)
                                                                      from bethadba.vw_usuarios_alocacao_historico as uah
                                                                     where uah.i_usuarios = usuarios_alocacao_historico.i_usuarios
                                                                       and convert(date,uah.apartir_de ) <= convert(date,today()))                                                         
                         inner join bethadba.vw_alocacao AS alocacao
                                 on alocacao.i_alocacao = if usuarios_alocacao_historico.i_alocacao_nova = 33 
                                                             then alocaco_anterior 
                                                             else usuarios_alocacao_historico.i_alocacao_nova end if  
                                 
   WHERE ( convert(date,agenda.data_inicio) between convert(date,inicio) and convert(date,fim) 
      or convert(date,agenda.data_inicio) <= convert(date,inicio) and convert(date,data_fim) >= convert(date,fim))
     and usuarios.ativo = 1 /*Apenas usuários ativos*/
     and Gerente IN ('Eloiza Kulckamp Alberton (Suporte SC)',
                     'Everton Carlos Batisti (Int)',
                     'Everton Carlos Batisti (Rev)',
             'Thiago Candelaria Birck (SP)', 'Marina Ferrari ', 'Marina Ferrari')  

UNION

SELECT inicio = left(cast(dateadd(ss,1,dateadd(mm,-2,ymd(year(today()),month(today()),1))) as char ),10),
         fim = cast(dateadd(ss,-1,dateadd(mm,6,ymd(year(today()),month(today()),1))) as char ),
         'Last Update: '||dateformat(now(),'dd/mm/yyyy HH:MM:SS'), 
         data_inicio = cast(agenda.data_inicio as CHAR),
         data_fim = cast(agenda.data_fim as CHAR), 
         nome_do_tecnico = usuarios.nome,
         email = lower(usuarios.email),
         responsavel_lancto = coalesce((select x.nome from power_bi.vw_usuarios as x where x.i_usuarios=agenda.i_usuarios),''),
        Lancto_Diferente = ( case
                                WHEN nome_do_tecnico <> responsavel_lancto then 1
                                else 0 end ),

         data_registro = cast(entrada as char),
         agenda.i_tipos,
         ausencia_tipo = agenda_tipos.descricao,
         ausencia_motivo = agenda_motivos_ausencias.descricao,
         descricao = dateformat(agenda.data_inicio,'HH:MM')||' as '|| dateformat(agenda.data_fim,'HH:MM')||' - '||  nome_do_tecnico,
         descricao_agenda = agenda.descricao,
         Gerente = 'Camila Meller',
         coordenador = 'Camila Meller',
        alocaco_anterior = (SELECT TOP 1 uah2.i_alocacao_nova
                                FROM bethadba.vw_usuarios_alocacao_historico AS uah2 
                                INNER JOIN bethadba.vw_usuarios_alocacao_historico AS uah ON uah2.i_usuarios = uah.i_usuarios
                                WHERE uah2.i_usuarios = usuarios.i_usuarios
                                    AND uah2.i_historico < usuarios_alocacao_historico.i_historico
                                    AND uah2.i_historico = uah.i_historico
                                ORDER BY uah.i_historico DESC  )  ,           
         alocaco_tecnico = alocacao.descricao,
        'CTD' AS setor,
        'CTD' AS unidade                                                                      
        
    FROM bethadba.vw_agenda AS agenda 
                         inner join bethadba.vw_agenda_tipos AS agenda_tipos
                                 on agenda_tipos.i_agenda_tipos = agenda.i_tipos             
                         left outer join bethadba.vw_agenda_motivos_ausencias AS agenda_motivos_ausencias
                                 on agenda_motivos_ausencias.i_agenda_motivos_ausencias = agenda.i_motivos_ausencias
                         inner join power_bi.vw_usuarios as usuarios
                                 on usuarios.i_usuarios = agenda.i_responsaveis
                and usuarios.i_revendas in(1)/*SP,BA,SUL,Secundarios, POA, curitiba*/                        
                                 
                         inner join bethadba.vw_usuarios_alocacao_historico AS usuarios_alocacao_historico
                                 on usuarios_alocacao_historico.i_usuarios = usuarios.i_usuarios
                                and usuarios_alocacao_historico.i_historico = (select max(uah.i_historico)
                                                                      from bethadba.vw_usuarios_alocacao_historico as uah
                                                                     where uah.i_usuarios = usuarios_alocacao_historico.i_usuarios
                                                                       and convert(date,uah.apartir_de ) <= convert(date,today()))                                                         
                         inner join bethadba.vw_alocacao AS alocacao
                                 on alocacao.i_alocacao = if usuarios_alocacao_historico.i_alocacao_nova = 33 
                                                             then alocaco_anterior 
                                                             else usuarios_alocacao_historico.i_alocacao_nova end if ,
                                                             
      bethadba.vw_usuarios_dados AS dados, 
      bethadba.vw_setores AS setor
                                  
   WHERE dados.i_departamento = setor.i_setores
      and setor.nome = 'Centro de Treinamento'
      and dados.i_usuarios = usuarios.i_usuarios
      and ( convert(date,agenda.data_inicio) between convert(date,inicio) and convert(date,fim) 
      or convert(date,agenda.data_inicio) <= convert(date,inicio) and convert(date,data_fim) >= convert(date,fim))
     and usuarios.ativo = 1 
              
   order by 3 desc, 5
```
