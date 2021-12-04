query_pibpercapita = '''
  SELECT pop.*, dsc.nome_municipio, pib.pib, pib.pib/pop.populacao as pibpercapita FROM `basedosdados.br_ibge_populacao.municipio` pop
  LEFT JOIN `basedosdados.br_ibge_pib.municipio` pib on pop.id_municipio = pib.id_municipio and pib.ano = pop.ano
  LEFT JOIN (
   select distinct (sc.id_municipio), sc.nome_municipio from `basedosdados.br_geobr_mapas.setor_censitario_2010` sc
   ) as dsc on dsc.id_municipio = pop.id_municipio
  '''

query_consumo_energia = '''
   SELECT ano, sigla_uf, sum(consumo) as consumo_anual_uf 
   FROM `basedosdados.br_mme_consumo_energia_eletrica.uf` 
   WHERE tipo_consumo='Total'
   GROUP BY ano, sigla_uf
   '''

