create table tipos (
    id integer primary key autoincrement,
    nome text,
    clima text,
    local text
);

create table flores (
    id integer primary key autoincrement,
    nome_p text,
    nome_c text,
    valor float,
    quantidade integer,
    caracteristica text,
    tipo_id integer,
    foreign key(tipo_id) references tipos(id)
);

