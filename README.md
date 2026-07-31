# Copfy · plugin do Claude Code

Plugin oficial das **Soluções Copfy**: sistemas de IA (atendimento no
WhatsApp, notas fiscais automáticas, criativos de anúncio e outros) que você
implementa no seu próprio computador, passo a passo, com o Claude Code
executando junto.

## Instalação

Dentro do Claude Code:

```
/plugin marketplace add copfybr/copfy-plugin
/plugin install copfy@copfy-plugin
/reload-plugins
```

O `/reload-plugins` ativa o plugin na conversa que já está aberta. Sem ele,
os comandos só aparecem quando você abrir o Claude Code de novo.

## Uso

1. Acesse uma solução em [app.copfy.com.br/solucoes](https://app.copfy.com.br/solucoes)
   e gere seu código de pareamento no painel "Implementar agora".
2. No terminal:

```
/copfy:conectar COPFY-XXXXXXXX
/copfy:solucao atendimento-whatsapp
```

3. Parou no meio? `/copfy:continuar` retoma de onde você estava, e
   `/copfy:status` mostra o que já foi feito.

Os comandos levam o prefixo `copfy:` porque o Claude Code sempre nomeia
comandos de plugin assim, pra dois plugins nunca brigarem pelo mesmo nome.

O conteúdo das soluções é entregue pela plataforma da Copfy e exige uma conta
com acesso à área de Soluções. Este repositório contém apenas o plugin.

## Suporte

Fale com o Copi no WhatsApp da Copfy, ou escreva pra lucas@copfy.com.br.
