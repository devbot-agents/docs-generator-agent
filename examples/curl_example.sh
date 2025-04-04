#!/bin/bash
# Exemplo de como chamar o endpoint do agente usando curl

curl -X POST \
  http://localhost:8000/api/v1/execute \
  -H "Content-Type: application/json" \
  -d '{"type": "exemplo_type", "properties": {"name": {"type": "exemplo_type"}, "description": {"type": "exemplo_type"}, "input_schema": {"type": "exemplo_type"}, "output_schema": {"type": "exemplo_type"}, "endpoint_url": {"type": "exemplo_type"}}}'
