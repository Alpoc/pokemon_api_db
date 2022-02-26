CREATE TABLE pokemon (
    pokemon_id character varying(36) NOT NULL,
    poke_json jsonb not null default '{}'::jsonb
);
