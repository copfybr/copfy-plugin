# Plano de teste visual

## Escopo

- 150 comandos únicos.
- Uma geração inicial por comando.
- Uma referência preferida por comando, definida em `IMAGE_TEST_MATRIX.md`.
- Uma nova geração quando o resultado não atingir os critérios mínimos.

## Referências locais

As imagens abaixo são fixtures de QA e não devem ser publicadas dentro do plugin.

| Fixture | Arquivo | Uso principal |
| --- | --- | --- |
| Tênis | `DC077-4-502-1.webp` | engenharia, construção, estrutura e protótipos |
| Red Bull | `br_zr_250ml_ac_zero_country_rgb_packrq-2750_cold_closed_front_com_full.png` | packshot, anúncio, estúdio e ficção científica |
| Rolex | `Rolex_1ct_icedoutromannumeral_1_1970x.jpg` | macro, luxo, arquivo, perícia e desenho técnico |
| Hambúrguer | `Hamburguer-com-Bacon-na-Grelha-1-1024x1024.png` | cortes, câmera e instruções visuais |
| Pizza | `bc53d507c26770e8f294fcbf92ef0864_XL.jpg` | vista superior, panorama, catálogo e infográfico |
| Zé Gotinha | `Ze-gotinha-png-1.webp` | raio X, anatomia conceitual, diagnóstico e laboratório |
| Baianinho | `codex-clipboard-68b0bed3-63c1-4164-a739-811d5c55389a.png` | personagem, toy art, evolução, visão noturna e universos paralelos |

## Critérios de aprovação

1. O tema continua imediatamente reconhecível.
2. O efeito principal do comando é inequívoco sem depender da legenda.
3. Cores, marcas e textos essenciais da referência não são alterados sem necessidade.
4. Interfaces, rótulos e medidas ficam legíveis quando fazem parte do efeito.
5. Anatomia e cortes de mascotes ou alimentos são conceituais e não gráficos.
6. Não há membros extras, geometrias quebradas, embalagem impossível ou artefatos dominantes.

## Estimativa operacional

- Geração inicial das 150 imagens: aproximadamente 6 a 10 horas.
- Revisão visual e registro dos resultados: aproximadamente 2 a 3 horas.
- Reexecução esperada de 15% a 25% dos casos: aproximadamente 1 a 3 horas.
- Total para a bateria completa: aproximadamente 9 a 15 horas.

Um smoke test representativo de 21 comandos, três por categoria original, leva aproximadamente 1,5 a 3 horas.

## Testes do roteador de recomendações

Quando o usuário anexar apenas o produto, o plugin deve mostrar três sugestões com descrição e imagem de exemplo antes de gerar.

| Produto | Candidatos fortes | Rejeições obrigatórias |
| --- | --- | --- |
| Calçado | `/layered`, `/exploded`, `/catalog`, `/lifestyle`, `/wormseye` | `/innerworkings`, salvo pedido surreal explícito |
| Relógio mecânico | `/innerworkings`, `/macro`, `/productshot`, `/turntable`, `/restoration` | efeitos que ocultem completamente o mostrador |
| Lata ou bebida | `/packshot`, `/heroshot`, `/splash`, `/floating`, `/adcreative` | anatomia realista ou engrenagens arbitrárias |
| Hambúrguer ou pizza | `/productshot`, `/topdown`, `/crosssection`, `/macro`, `/stepbystep` | mecanismos industriais dentro do alimento |
| Mascote | `/toyfigure`, `/claymation`, `/diorama`, `/parallelversions`, `/xray` conceitual | anatomia gráfica ou alegação médica |

Critérios do roteador:

1. recomenda no máximo três comandos;
2. explica em uma frase por que cada um combina com o produto;
3. usa a prévia pública correspondente em `assets/examples/`;
4. não gera até a escolha, exceto quando o usuário autorizar escolha e geração automáticas;
5. não usa a marca ou o produto das fixtures como regra de recomendação.
