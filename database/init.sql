CREATE TABLE pokemon (
    pokemon_id integer NOT NULL,
    name character varying(255) not null,
    poke_json jsonb not null default '{}'::jsonb
);
