# DIO Agent — Mentor de Análise de Vulnerabilidades

> Especialização educacional e defensiva do [DIO Agent](https://github.com/digitalinnovationone/dio-agent): analisa evidências, pergunta pelo contexto antes de ações ativas e orienta correções com impacto, probabilidade e severidade explícitos.

## Sobre a especialização

Este projeto acrescenta ao mentor DIO uma habilidade de AppSec (segurança de aplicações). O agente não deve saltar direto para comandos de exploração. Primeiro distingue revisão estática de código de teste ativo, esclarece autorização e escopo quando necessário e, só então, estrutura a análise, estima o risco e recomenda a correção. A melhoria escolhida é uma matriz consistente de triagem de risco (impacto × probabilidade), acompanhada de validação local e limites de segurança explícitos.

O conteúdo instrui o agente por arquivos Markdown; não há treinamento de modelo. A matriz é uma heurística pedagógica de priorização e **não** substitui CVSS, avaliação formal ou política organizacional.

## O que foi criado ou alterado

- `skills/vulnerability-analysis/SKILL.md` — processo passo a passo, perguntas de escopo/autorização, critérios para CWE e MITRE ATT&CK, correção, validação e formato de saída estável.
- `skills/README.md` — catálogo humano de skills atualizado.
- `agent/knowledge/security-basics.md` — vulnerabilidade, ameaça, risco, CIA, matriz de risco, fundamentos de SQL Injection e boas práticas.
- `agent/persona.md` — responsabilidade e precisão em AppSec incorporadas à persona.
- `AGENTS.md` — conhecimento e skill incluídos no índice principal, com regra explícita de autorização antes de testes ativos.
- `examples/app_vulnerable.py` e `examples/app_secure.py` — versões mínima vulnerável e corrigida do login.
- `examples/demo_db.py` e `tests/test_sql_injection_demo.py` — dados fictícios e testes isolados, apenas SQLite em memória.
- `REPLICACAO_PASSO_A_PASSO.txt` — roteiro detalhado para reproduzir o trabalho e publicar no GitHub.

## Exemplo SQL Injection: testar com segurança

O exemplo não abre servidor, não conecta a uma rede e não usa dados reais. Os testes criam um banco SQLite descartável em memória e mostram o contraste: o login vulnerável aceita uma entrada de laboratório que contorna a verificação; a consulta parametrizada rejeita essa mesma entrada e continua aceitando a conta fictícia válida.

Requisitos: Python 3.9 ou superior. Na raiz do projeto:

```bash
python3 --version
python3 -m unittest discover -s tests -v
```

No Windows, se `python3` não existir, use `py -3` no lugar. Os quatro testes esperados cobrem login válido vulnerável, demonstração local do bypass, login válido corrigido e rejeição de credenciais/entrada inválidas pela versão corrigida. O exemplo usa SHA-256 apenas para não desviar a demonstração; **não** armazene senhas reais com SHA-256. Para produção, use Argon2id, bcrypt ou scrypt, parâmetros apropriados e controles de aplicação adicionais.

## Executar no Hermes

1. Instale e configure o Hermes seguindo a [documentação oficial](https://hermes-agent.nousresearch.com/docs), inclusive provedor/modelo necessários.
2. Abra um terminal **na raiz desta pasta** (`dio-agent-challenge`, onde está `AGENTS.md`).
3. Inicie o harness com o comando `hermes` indicado pela versão instalada.
4. Verifique se o harness carregou as instruções do projeto. Se não carregar `AGENTS.md` automaticamente, forneça explicitamente o contexto/instruções do projeto conforme a documentação do harness.
5. Use os prompts sugeridos abaixo. Faça a análise do exemplo vulnerável; depois peça a revisão de `examples/app_secure.py` e dos testes. O agente deve distinguir análise estática de execução e não alegar testes que não rodou.

### Prompt 1 — análise estática do exemplo vulnerável

```text
Atue como mentor de AppSec e use a skill de análise de vulnerabilidades deste projeto.
Analise estaticamente examples/app_vulnerable.py. É código didático local fornecido
para revisão; não inicie servidor nem acesse rede. Aponte a evidência exata, explique
conceitualmente como a entrada altera a consulta, avalie impacto e probabilidade pela
matriz documentada e derive a severidade. Indique CWE e avalie se MITRE ATT&CK T1190
se aplica ao contexto (não assuma que há aplicação exposta). Recomende a correção e
uma validação local segura. Não afirme que executou testes.
```

### Prompt 2 — validar a versão corrigida

```text
Agora compare examples/app_secure.py com a versão vulnerável e leia
 tests/test_sql_injection_demo.py. Confirme por inspeção se a consulta é parametrizada,
quais testes positivos e negativos cobrem o caso e o que ainda não foi verificado.
Não teste nenhum sistema externo. Se você executar os testes, informe o comando exato
 e o resultado real; não declare a aplicação pronta para produção.
```

### Prompt 3 — verificar que pergunta antes de sugerir comandos

```text
Tenho um servidor Ubuntu de laboratório exposto à internet e quero avaliar sua
segurança. Antes de sugerir qualquer comando ou teste, faça uma pergunta de contexto
por vez para entender propriedade/autorização, ativos e limites do escopo, janela de
execução e impacto permitido. Não faça varredura nem assuma que a palavra laboratório
é autorização suficiente.
```

Na demonstração, registre capturas reais do harness (não prints simulados): (1) análise de `app_vulnerable.py`; (2) a revisão da versão parametrizada; (3) a primeira pergunta de contexto do cenário Ubuntu. Remova tokens, dados pessoais, URLs privadas e qualquer segredo antes de compartilhar. A pasta `evidencias/` pode ser usada para guardar essas capturas localmente.

## Estrutura relevante

```text
AGENTS.md
README.md
REPLICACAO_PASSO_A_PASSO.txt
agent/
  persona.md
  knowledge/
    security-basics.md
skills/
  README.md
  vulnerability-analysis/
    SKILL.md
examples/
  app_vulnerable.py
  app_secure.py
  demo_db.py
tests/
  test_sql_injection_demo.py
```

## Segurança e escopo

Use os exemplos somente em laboratório local. Não execute testes em infraestrutura de terceiros. A skill pede autorização explícita, ativos incluídos/excluídos, janela e limites de impacto antes de ações ativas. Para `T1190`, a associação é condicional a um cenário de exploração de aplicação exposta; a fraqueza de SQL Injection é melhor descrita com a CWE pertinente.

## Publicação

Repositório público da entrega: [github.com/fabiobilac/dio-agent-security-mentor](https://github.com/fabiobilac/dio-agent-security-mentor). O roteiro `REPLICACAO_PASSO_A_PASSO.txt` descreve como reproduzir o projeto e publicar uma cópia em outra conta. Não compartilhe tokens de acesso.

## Referências

- Repositório base: https://github.com/digitalinnovationone/dio-agent
- Hermes Agent: https://hermes-agent.nousresearch.com/docs
- OWASP SQL Injection Prevention Cheat Sheet: https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html
- CWE-89: https://cwe.mitre.org/data/definitions/89.html
- MITRE ATT&CK T1190: https://attack.mitre.org/techniques/T1190/
