create database if not exists shopper;
use shopper;
create table if not exists orders (
    order_id bigint not null auto_increment primary key,
    created_at timestamp not null default now(),
    customer_id integer not null,
    total_amount decimal(15, 4) not null,
    dispatched_at timestamp
);
create table if not exists customers
(
    customer_id integer not null auto_increment primary key,
    first_name  varchar(255),
    last_name   varchar(255),
    email       varchar(255)
);
