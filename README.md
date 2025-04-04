# Docs Generator Agent

O **Docs Generator Agent** é uma ferramenta automatizada destinada a simplificar o processo de criação de documentação para agentes. Utilizando schemas JSON de entrada e saída, este agente gera documentação completa, exemplos de uso e arquivos complementares necessários para entender e interagir com diversos agentes.

## Funcionalidades

- Geração de documentação em Markdown
- Criação de exemplos de uso baseados em schemas JSON de entrada e saída
- Geração de arquivos Swagger para documentação de API
- Produção de arquivos `agent_json` para fácil distribuição e consumo

## Requisitos

Para utilizar o **Docs Generator Agent**, é necessário ter um ambiente capaz de executar código JavaScript, como Node.js.

## Instalação

1. Clone o repositório do agente para sua máquina local:

```bash
git clone <url-do-repositorio-do-agent>
```

2. Entre no diretório do agente clonado e instale as dependências:

```bash
cd docs-generator-agent
npm install
```

## Uso

Para gerar a documentação e os arquivos complementares, siga os passos abaixo:

1. Prepare um arquivo JSON contendo os dados de entrada conforme especificado. Por exemplo, `input.json`:

```json
{
  "name": "Seu Agente",
  "description": "Descrição do seu agente.",
  "input_schema": "schema_de_entrada.json",
  "output_schema": "schema_de_saída.json",
  "endpoint_url": "https://endpoint.do.seu.agente"
}
```

2. Execute o comando abaixo, substituindo `<input.json>` pelo caminho do seu arquivo de entrada:

```bash
node run.js <input.json>
```

3. Os arquivos gerados serão salvos no diretório especificado, incluindo a documentação (`readme.md`), exemplos (`examples.json`), a documentação da API em Swagger (`swagger.json`) e o arquivo `agent_json` para distribuição.

## Exemplos de Entrada/Saída

### Entrada

```json
{
  "name": "Example Agent",
  "description": "This agent provides an example.",
  "input_schema": "{\"type\": \"object\", \"properties\": {\"example\": {\"type\": \"string\"}}}",
  "output_schema": "{\"type\": \"object\", \"properties\": {\"result\": {\"type\": \"string\"}}}",
  "endpoint_url": "https://example.agent.endpoint"
}
```

### Saída

A saída incluirá quatro strings representando os arquivos gerados:

- `readme`: A documentação em Markdown.
- `swagger`: A documentação Swagger da API.
- `examples`: Exemplos de uso baseados nos schemas de entrada e saída.
- `agent_json`: Um arquivo JSON contendo todas as informações necessárias para utilizar o agente.

## Endpoint

O **Docs Generator Agent** interage com um endpoint especificado no arquivo de entrada. Este endpoint deve ser capaz de processar os schemas de entrada e saída para gerar a documentação e os arquivos complementares.

---

Para mais informações, entre em contato ou abra uma issue no repositório do GitHub.
