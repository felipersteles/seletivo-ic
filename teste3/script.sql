
/* 	
	Utilizando banco de dados Postgresql
	Criando tabelas com as caracteristias apresentadas no
 */
CREATE TABLE IF NOT EXISTS demonstracoes_contabeis(
	trimestre DATE,
	reg_ans NUMERIC,
	conta NUMERIC,
	description TEXT,
	saldo_ini numeric,
	saldo_fim numeric
);

CREATE TABLE IF NOT EXISTS operadoras_ativas(
id serial primary key,
	reg_ans int,
	cnpj bigint, 
	razao_social text,
	nome_fantasia varchar(99)
);

/*
	Importando dados presentes
	nos arqquivos csv, antes de realizar este procediment
	é necessario inserir o arquivo na maquina em que hospeda
	o banco de dados.
*/
COPY demonstracoes_contabeis TO '/var/lib/postgresql/table1.csv' csv header;
COPY operadoras_ativas TO '/var/lib/postgresql/table2021.csv' csv header;
COPY operadoras_ativas TO '/var/lib/postgresql/table2022.csv' csv header;

/*  
    Após ter a tabela com dados 
	Basta aplicar as condições a query
 */
select * from operadoras_ativas oa, demonstracoes_contabeis dc 
where oa.reg_ans = dc.reg_ans and trimestre = '2022-10-01' and dc.description like 'EVENTOS INDENIZÁVEIS LÍQUIDOS / SINISTROS RETIDOS' order by (dc.saldo_fim - dc.saldo_ini) desc 

select * from operadoras_ativas oa, demonstracoes_contabeis dc 
where oa.reg_ans = dc.reg_ans and date_part('year', trimestre) = 2022  and dc.description like 'EVENTOS INDENIZÁVEIS LÍQUIDOS / SINISTROS RETIDOS' order by (dc.saldo_fim - dc.saldo_ini) desc 
