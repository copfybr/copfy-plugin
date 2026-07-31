---
description: Mostra se este computador está conectado à Copfy e o que já foi iniciado
---

Mostre o estado da Copfy neste computador, em português do Brasil.

1. Existe `~/.copfy/credentials.json`? Se não, explique que é preciso rodar
   `/copfy:conectar <código>` com um código gerado em
   app.copfy.com.br/solucoes, e pare.
2. Se existe, leia o token de dentro da própria chamada (nunca imprima o
   valor) e chame
   `GET https://app.copfy.com.br/api/method/copfy_access.solucoes.plugin_status`
   com o header `X-Copfy-Token`:
   - PowerShell: `$t = (Get-Content "$HOME\.copfy\credentials.json" -Raw | ConvertFrom-Json).token; Invoke-RestMethod -Uri "https://app.copfy.com.br/api/method/copfy_access.solucoes.plugin_status" -Headers @{ "X-Copfy-Token" = $t }`
   - Mac/Linux: `curl -s -H "X-Copfy-Token: $(python3 -c 'import json,os;print(json.load(open(os.path.expanduser("~/.copfy/credentials.json")))["token"])')" "https://app.copfy.com.br/api/method/copfy_access.solucoes.plugin_status"`
3. Diga quem está conectado e se o acesso às Soluções está ativo.
4. Liste as soluções já iniciadas (pastas em `~/copfy/`) e, para cada uma, o
   passo atual lido do `copfy-estado.json`.
5. Feche lembrando os comandos: `/copfy:solucao <slug>` e `/copfy:continuar`.
