# Fundamentos de segurança da informação e AppSec

Este arquivo fornece vocabulário e critérios de triagem ao DIO Agent. Ele complementa, mas não substitui, evidências do sistema, políticas organizacionais ou uma avaliação formal.

## Conceitos essenciais

- **Vulnerabilidade:** fraqueza em software, configuração, processo ou desenho que pode ser explorada.
- **Ameaça:** agente, evento ou condição capaz de explorar uma fraqueza.
- **Risco:** possibilidade de uma ameaça explorar uma vulnerabilidade e causar impacto. Para triagem neste projeto, usamos impacto × probabilidade; isso é uma heurística simples, não um cálculo financeiro nem CVSS.
- **Exploração:** uso de uma fraqueza para obter um efeito. Uma demonstração em laboratório não prova que um alvo real seja vulnerável.
- **Mitigação:** controle que reduz probabilidade ou impacto. **Correção/remediação** elimina ou reduz a causa da falha.
- **CWE:** catálogo de tipos de fraqueza. Exemplo: CWE-89 descreve a neutralização imprópria de elementos especiais usados em comandos SQL (SQL Injection).
- **MITRE ATT&CK:** base de conhecimento de táticas e técnicas observadas em comportamentos adversários. É preciso justificar uma associação pelo cenário; ATT&CK não é um catálogo de vulnerabilidades.

## Tríade CIA

A tríade CIA organiza três propriedades que podem sofrer impacto:

- **Confidencialidade (C):** somente pessoas e sistemas autorizados conseguem acessar a informação.
- **Integridade (I):** dados e sistemas permanecem corretos e só mudam de forma autorizada.
- **Disponibilidade (A):** serviços e dados estão acessíveis quando necessários.

Uma falha pode afetar uma ou várias propriedades. Explique quais dados/serviços estão em risco e não assuma impacto máximo sem evidência.

## Matriz de triagem deste projeto

Avalie cada dimensão de 1 a 5 e justifique com contexto observável.

### Impacto

1. **Muito baixo:** efeito limitado, reversível e sem dados ou serviço relevante afetado.
2. **Baixo:** dano restrito a uma funcionalidade ou informação de baixa sensibilidade.
3. **Moderado:** exposição ou alteração relevante, ou interrupção limitada de serviço.
4. **Alto:** dados sensíveis, privilégio importante ou serviço crítico podem ser afetados.
5. **Muito alto:** comprometimento amplo, dados altamente sensíveis, controle administrativo ou interrupção severa plausível.

### Probabilidade

1. **Rara:** múltiplas condições improváveis e controles fortes reduzem bastante a possibilidade.
2. **Improvável:** exige condições específicas ou acesso limitado.
3. **Possível:** condições realistas, mas existem barreiras relevantes.
4. **Provável:** falha alcançável e controles insuficientes; exploração plausível no contexto.
5. **Quase certa:** exposição e condições favoráveis foram demonstradas; use somente com evidência robusta.

### Produto e faixas de severidade

`pontuação de triagem = impacto × probabilidade` (intervalo de 1 a 25):

| Produto | Severidade de triagem |
|---------|------------------------|
| 1–4 | Baixa |
| 5–9 | Moderada |
| 10–16 | Alta |
| 17–25 | Crítica |

Declare os dois valores, o produto, a faixa e as suposições. Uma probabilidade baixa pode decorrer de falta de contexto, não de uma prova de que a falha é difícil de explorar. Esta matriz serve para priorização pedagógica e não equivale a CVSS, SLA ou política corporativa.

## Exemplo didático: SQL Injection

Montar uma consulta SQL concatenando entrada não confiável mistura dados com instruções. Consultas parametrizadas mantêm os valores de entrada separados do comando SQL e são a correção prioritária. Validação de entrada, mensagens de erro genéricas, privilégio mínimo da conta de banco e testes automatizados são camadas complementares; filtros de caracteres não substituem parametrização.

- **CWE:** CWE-89 pode descrever a fraqueza.
- **MITRE ATT&CK:** T1190, *Exploit Public-Facing Application*, só deve ser mencionado quando o cenário envolver exploração de aplicação exposta a partir da rede. A técnica descreve o comportamento do adversário e não significa que qualquer SQL Injection tenha sido explorada nem é sinônimo da CWE.
- **Boas práticas adicionais:** armazenar senhas com algoritmo próprio para senhas (por exemplo, Argon2id, bcrypt ou scrypt), usar segredos fora do código, limitar privilégios do banco, aplicar atualizações e registrar eventos sem registrar credenciais ou dados sensíveis.

## Princípios defensivos

1. **Menor privilégio:** cada usuário, serviço e processo recebe apenas as permissões necessárias.
2. **Defesa em profundidade:** controles independentes reduzem o risco quando uma camada falha.
3. **Secure by design:** reduzir a causa no desenho e no código, não depender apenas de detecção.
4. **Validação segura:** testar apenas ativos próprios/autorizados, com escopo, janela e impacto permitido definidos.
5. **Evidência e honestidade:** separar fato, hipótese e recomendação; dizer o que não foi testado.
6. **Segredos e privacidade:** não pedir, expor ou incluir credenciais, tokens, dados pessoais ou dados reais em exemplos.
7. **Aprendizado:** demonstrar falhas apenas em laboratório isolado e explicar a correção junto com o risco.

## Referências

- OWASP Cheat Sheet Series — SQL Injection Prevention: https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html
- MITRE CWE-89: https://cwe.mitre.org/data/definitions/89.html
- MITRE ATT&CK T1190: https://attack.mitre.org/techniques/T1190/
- OWASP Top 10: https://owasp.org/www-project-top-ten/
