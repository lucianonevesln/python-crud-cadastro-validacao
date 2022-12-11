use projetos;

create table cadastros (

    id int not null auto_increment,
    nome varchar (80) not null,
    cpf varchar (11) not null,
    email varchar (100) not null,
    telefone varchar (11) not null,
    primary key (id)

);

select * from projetos.cadastros;