# Copfy · plugin de IA

Plugin oficial da Copfy com três conjuntos de recursos:

- **151 comandos gratuitos de imagem**, sem conta Copfy: raio X, blueprint, Meta Ads, Sell Ads, outdoor anamórfico 3D, fotografia de produto, câmera, miniaturas, diagramas e protótipos.
- **Copywriting e cartas de vendas**: uma skill para páginas completas e outra para o método M98 da Copfy.
- **Soluções Copfy**, que conectam sua conta e implementam sistemas de IA passo a passo.

O pacote possui manifests para Claude Code e Codex no aplicativo desktop.
No Codex, ele conecta diretamente ao MCP de Soluções da Copfy, com OAuth 2.1
e PKCE para acessar a conta do aluno.

## Instalação no Codex (aplicativo desktop)

Use o Codex no aplicativo instalado no computador. Abra **Plugins**, adicione
o marketplace `copfybr/copfy-plugin` e instale **Copfy**. Se já instalou uma
versão anterior, sincronize o marketplace e reinstale o plugin para receber
a configuração atual.

Depois da instalação, abra uma **nova conversa no Codex** e peça:

> Use o plugin Copfy para implementar a solução atendimento-whatsapp.

Quando o Codex solicitar autenticação, abra o link de autorização da Copfy,
entre em `app.copfy.com.br` com a **conta que tem acesso ao Copfy HUB** e clique
em **Permitir**, depois em **Voltar ao Codex** para concluir. Mantenha o Codex
aberto durante essa etapa e volte à conversa depois de concluir. A conta do
ChatGPT pode usar outro e-mail.

O login pode ser solicitado durante a instalação ou ao usar uma Solução.
Se ele não aparecer e a Solução pedir autenticação, abra as configurações de
**MCP** do Codex e autentique o servidor **copfy**. O login não usa código de
pareamento nem o comando `/copfy:conectar`.

O plugin deste repositório usa um servidor MCP próprio e funciona no
**aplicativo desktop**. Esse pacote não conecta as Soluções pelo site
`chatgpt.com` no navegador. A integração pelo navegador depende de um app
disponível para a sua conta no diretório do ChatGPT.

As 151 skills visuais e as skills de copywriting continuam disponíveis sem
conta Copfy. As ferramentas das Soluções exigem autenticação e acesso ao HUB.
O plugin não referencia um app de desenvolvedor de outra conta.

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

No Codex desktop, siga o fluxo OAuth descrito acima e peça ao plugin Copfy
para listar, implementar ou retomar uma solução. O plugin consulta o catálogo,
obtém o método e salva ou lê o progresso pelas ferramentas MCP.

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
