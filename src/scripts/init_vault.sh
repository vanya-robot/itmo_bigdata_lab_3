#!/bin/sh

# Инициализируем Vault
vault secrets enable -path=secret kv-v2

# Записываем секреты
vault kv put secret/postgres \
  user="penguin_user" \
  password="123321" \
  db="penguin_db" \
  port="5432"