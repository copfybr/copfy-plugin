# Copfy · plugin de IA

Plugin oficial da Copfy com três conjuntos de recursos:

- **151 comandos gratuitos de imagem**, sem conta Copfy: raio X, blueprint, Meta Ads, Sell Ads, outdoor anamórfico 3D, fotografia de produto, câmera, miniaturas, diagramas e protótipos.
- **Copywriting e cartas de vendas**: uma skill para páginas completas e outra para o método M98 da Copfy.
- **Soluções Copfy**, que conectam sua conta e implementam sistemas de IA passo a passo.

O pacote possui manifests para Claude Code, ChatGPT e Codex. Além das skills,
ele conecta a integração oficial da Copfy ao MCP de Soluções, com OAuth 2.1 e
PKCE para acessar a conta do aluno.

## Instalação no ChatGPT

No ChatGPT Codex, abra **Configurações → Plugins → Adicionar marketplace** e
adicione o repositório `copfybr/copfy-plugin`. Na fonte **Pessoal**, abra
**Copfy** e clique em **Instalar**.

A instalação abre automaticamente `app.copfy.com.br`. Entre na conta do Copfy
HUB, clique em **Permitir** e depois em **Abrir ChatGPT**. Em um chat de qualquer
projeto, mencione `@Copfy` e peça, por exemplo, “chamar a solução
atendimento-whatsapp”. **No ChatGPT Codex não existe código de pareamento.**

O MCP expõe ferramentas para listar comandos visuais e skills, consultar as
Soluções, obter o método e salvar ou retomar o progresso. As 151 skills visuais
continuam gratuitas e podem ser listadas sem login; o OAuth é usado apenas nas
ferramentas ligadas à conta.

## Instalação no Claude Code

```text
/plugin marketplace add copfybr/copfy-plugin
/plugin install copfy@copfy-plugin
/reload-plugins
```

## Comandos gratuitos de imagem

Anexe uma imagem e invoque uma skill do plugin. No Claude Code, por exemplo:

```text
/copfy:xray
/copfy:blueprint
/copfy:productshot
/copfy:diorama
/copfy:thermal
/copfy:3dbillboard
/copfy:metaads
/copfy:sellads
```

Também é possível acrescentar o assunto ou combinar dois efeitos:

```text
/copfy:xray meu tênis
/copfy:productshot esta lata, fundo escuro
/copfy:blueprint + /copfy:neon esta máquina
```

Veja a [lista completa](plugins/copfy/IMAGE_COMMANDS.md) ou navegue pela [galeria com 151 exemplos](plugins/copfy/EXAMPLES.md).

Se a pessoa apenas anexar o produto, sem escolher um comando, a skill `image-commands` analisa formato, material, categoria e potencial visual, mostra os três efeitos mais adequados com suas imagens de exemplo e espera a escolha antes de gerar. Combinações incompatíveis — como engrenagens dentro de um calçado sem mecanismo — são descartadas pelo roteador.

Todos os 151 comandos possuem descrição operacional própria e pelo menos uma imagem de exemplo pública. `/3dbillboard` e `/metaads` incluem demonstrações com tênis e lata; `/sellads` cria uma peça mais orientada à venda sem fabricar oferta ou prova. Esse catálogo pertence ao **free tier** e não pede login nem código de pareamento.

## Copywriting e cartas de vendas

A skill `carta-de-vendas` cria a copy, o arco de 9 dobras e a direção visual de uma landing page de conversão. A skill `copy98` aplica o método M98 da Copfy em cartas, VSLs, anúncios, headlines, e-mails e mensagens de oferta.

Elas podem funcionar juntas: `copy98` constrói o argumento em 7 gatilhos e `carta-de-vendas` transforma esse argumento numa página completa. As duas preservam preço, prova, garantia e urgência reais, sem fabricar alegações comerciais.

## Soluções Copfy

No ChatGPT Codex, siga o fluxo OAuth descrito acima: instale o plugin, clique em
**Permitir** na tela do Copfy HUB e chame `@Copfy`. Não gere código e não use o
comando `/copfy:conectar` nesse caminho.

No Claude Code, o fluxo continua usando o código exibido em **Implementar
agora**:

```text
/copfy:conectar COPFY-XXXXXXXX
/copfy:solucao atendimento-whatsapp
```

Use `/copfy:continuar` para retomar uma implementação e `/copfy:status` para acompanhar o progresso.

O conteúdo completo das soluções é entregue pela plataforma da Copfy e exige uma conta com acesso. Os comandos de imagem deste repositório são gratuitos e não exigem autenticação.

## Desenvolvimento

As skills de imagem são geradas a partir do catálogo mantido em `plugins/copfy/scripts/generate_image_skills.py`:

```text
python plugins/copfy/scripts/generate_image_skills.py
```

A matriz de QA escolhe uma das referências de produto ou mascote para cada comando e fica em `plugins/copfy/tests/IMAGE_TEST_MATRIX.md`. As imagens usadas nos testes não são distribuídas no plugin.

## Suporte

Fale com o Copi no WhatsApp da Copfy ou escreva para lucas@copfy.com.br.
