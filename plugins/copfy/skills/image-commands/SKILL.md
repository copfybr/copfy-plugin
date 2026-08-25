---
name: image-commands
description: Escolha e aplique os comandos gratuitos de imagem da Copfy. Use quando o usuário pedir uma recomendação de efeito, quiser conhecer o catálogo ou combinar comandos sem indicar um comando específico.
---

# Comandos de imagem Copfy

Ajude o usuário a escolher entre os 148 comandos gratuitos do plugin e gere ou edite a imagem com a ferramenta nativa disponível. Este catálogo é grátis e não exige autenticação Copfy.

Quando o pedido já trouxer um comando específico, use a skill desse comando. Quando o usuário pedir sugestões ou simplesmente anexar um produto sem escolher efeito, consulte [o catálogo](../../IMAGE_COMMANDS.md) e [a galeria](../../EXAMPLES.md) e recomende automaticamente as três opções mais adequadas.

## Recomendação automática

Primeiro identifique o tipo de produto, material, forma, ângulo disponível, presença de embalagem ou marca e o provável objetivo comercial. Avalie cada candidato por:

1. compatibilidade física ou conceitual com o produto;
2. impacto visual esperado;
3. preservação da identidade e dos textos da referência;
4. clareza do efeito em uma única imagem.

Descarte combinações arbitrárias. Em especial, não recomende engrenagens ou interiores mecânicos para alimentos, calçados e embalagens sem mecanismo, salvo se o usuário pedir uma interpretação surreal. Reserve `/innerworkings` para relógios, máquinas e produtos com mecanismo plausível; use `/layered`, `/exploded`, `/cutaway` ou `/schematic` para construção de calçados e objetos sem motor.

Apresente cada recomendação neste formato, antes de gerar:

```text
/comando — resultado esperado e por que combina com este produto
[imagem de exemplo do comando]
```

Renderize a prévia com `https://raw.githubusercontent.com/copfybr/copfy-plugin/main/plugins/copfy/assets/examples/<comando>.jpg`. Recomende no máximo três comandos e espere a escolha do usuário, a menos que ele tenha pedido explicitamente para você escolher e gerar. Não use as marcas dos exemplos para decidir: elas são apenas demonstrações do efeito.

Atalhos úteis de seleção:

- alimentos: `/productshot`, `/macro`, `/topdown`, `/crosssection`, `/stepbystep`;
- bebidas e embalagens: `/packshot`, `/heroshot`, `/splash`, `/floating`, `/adcreative`;
- moda e calçados: `/lifestyle`, `/layered`, `/exploded`, `/catalog`, `/wormseye`;
- relógios, máquinas e eletrônicos: `/innerworkings`, `/cutaway`, `/explodedview`, `/schematic`, `/diagnostic`;
- mascotes e personagens: `/toyfigure`, `/claymation`, `/diorama`, `/parallelversions`, `/xray` conceitual;
- joias e produtos premium: `/macro`, `/studio`, `/productshot`, `/turntable`, `/restoration`.

Ao receber uma imagem:

- preserve a identidade visual, silhueta, cores e detalhes essenciais da referência;
- selecione o efeito pelo objetivo do usuário, não apenas pelo tipo de arquivo;
- combine comandos somente quando o usuário pedir ou quando a combinação resolver claramente o briefing;
- gere a imagem em vez de devolver apenas um prompt, sempre que houver ferramenta de imagem disponível;
- para mascotes, alimentos e objetos, trate anatomia, radiografia e cortes internos de forma conceitual e não gráfica.

Se não houver imagem nem descrição do assunto, peça uma referência curta.
