CREATE TABLE pokemon (
    pokemon_id character varying(36) NOT NULL,
    name character varying(255) not null,
    poke_json jsonb not null default '{}'::jsonb
);
