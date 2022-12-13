# Logo

Logo é uma linguagem de programação orientada para a educação, desenvolvida em 1967 por Wally Feurzeig, Seymour Papert, and Cynthia Solomon. Um dos aspectos da linguagem é a possibilidade de utilizar um modo onde uma tartaruga recebe comandos e desenha o resultado desses comandos na tela.

Dada uma linguagem de programação, baseada em um subset da linguagem Logo, com os seguintes comandos:

```
    - FO <num> | FORWARD <num> : Move a caneta à frente, numa distância de <num> pixels.
    - BK <num> | BACKWARD <num> : Move a caneta para trás, numa distância de <num> pixels.
    - RIGHT <angle> | RT <angle> : Gira a caneta <angle> graus à direita.
    - LEFT <angle> | LT <angle> : Gira a caneta <angle> graus à esquerda.
    - PENUP | PU : Não desenha enquanto move a caneta.
    - PENDOWN | PD : Desenha enquanto move a caneta.
    - WIPECLEAN | WC : Apaga a tela de desenho
    - CLEARSCREEN | CS : Apaga a tela e posiciona a caneta na posição central da tela (0,0) e angulo 0
    - HOME : Move a caneta para a posição original
    - SETXY <x> <y> : Posiciona a caneta na posição (<x>,<y>)
    - XCOR : Valor da coordenada atual de X
    - YCOR : Valor da coordenada atual de Y
    - HEADING : Valor atual do angulo da tartaruga (0 aponta para direita, 90 para cima)
    - RANDOM : Retorna um número randomico, inteiro, de 0 a 9.
    - IF ( <condition> ) THEN <body> END : Executa <body> se a condição for verdadeira.
    - IF ( <condition> ) THEN <body_true> ELSE <body_false> END : Executa <body_true> se a condição for verdadeira, senão executa <body_false> 
    - WHILE ( <condition> ) <body> END
    - PRINT <data> : Imprime os dados em <data> no console
    - TYPEIN : Lê um dado do console
    - TO <id> <optional_ars> <body> END : Define uma nova primitiva.
```

Ao definir uma nova primitiva com o comando 'TO', <id> que aceita os parâmetros definidos em <optional_args>. Os comandos executados pela nova primitiva são definidos em <body>. Cada parâmetro é definido por ':<id>' (dois pontos seguidos de um identificador). Os valores dos parâmetros são acessados com ':<id>', o mesmo formato da declaração do parâmetro.


Por exemplo, o seguinte programa em Logo, desenha um quadrado com arestas de tamanho 30 na posição (20, 20):

-----

```
TO SQUARE :length
    FORWARD :length
    RIGHT 90
    FORWARD :length
    RIGHT 90
    FORWARD :length
    RIGHT 90
    FORWARD :length
    RIGHT 90
END

SETXY 20 20
SQUARE 30
```

## Expressões aritméticas e Variáveis

A linguagem deve prover suporte para as operações de adição, subtração, multiplicação, divisão e potenciação, além da possibilidade de armazenar valores em variáveis. As operações só são definidas para valores numéricos, sendo sempre realizadas com ponto flutuante. 

As variáveis não precisam ter uma declaração explícita, mas devem ser inicializadas no seu primeiro uso.


## Expressões Booleanas

As condições dos comandos IF e WHILE (ou as expressões booleanas cujo resultado é armazenado em variáveis), permitem o uso dos operadores relacionais '>', '<', '>=', '<=', '==' (igual), e '<>' (diferente). Os operadores '==' e '<>' tem menor prioridade em relação aos outros.

Os operadores booleanos NOT, AND e OR devem ser suportados e estão listados em ordem de prioridade.

Assim como nas expressões aritméticas, o uso de parenteses "()" inverte a prioridade da expressão.

