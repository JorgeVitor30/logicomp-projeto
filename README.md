# Desenvolvido por:

```
Jorge Vitor de Aguiar Lima
Jonatha de Oliveira Targino
```
Um evento vai oferecer k minicursos de uma hora de duração cada. Dessa forma, os organizadores do evento vão definir os horários em slots de uma hora de duração, por exemplo, 8:00-9:00, 9:00-10:00, 10:00-11:00, e assim por diante. Os participantes podem se inscrever em mais de um minicurso. Logo, a organização do evento deseja agendar os horários dos minicursos de forma a atender as inscrições dos participantes, ou seja, minicursos que possuem inscrições de um mesmo participante não podem ser ofertados no mesmo horário.

Por conta das condições mencionadas, os organizadores querem saber se é possível reservar apenas m slots para ofertar todos os cursos respeitando as inscrições dos participantes. Além do número de cursos k e do número de horários m, também já temos acesso ao conjunto P com os pares de cursos com inscrições em comum. Ou seja, se o par (i, j) está em P, então o curso i e o curso j possuem inscrições em comum.

Usando satisfatibilidade da lógica proposicional, você deve criar um programa que, dados como entrada o número de cursos k, o número de slots m e o conjunto P de minicursos com inscrições em comum, determine se é possível agendar m horários diferentes para ofertar os k minicursos de forma que minicursos com participantes em comum não sejam ofertados no mesmo horário. Caso seja possível, seu programa também deve dizer o slot de tempo que cada curso deve ser ofertado.

Veja um exemplo de entrada e de saída a seguir. As primeiras linhas representam a identificação e nome de cada minicurso. Por exemplo, o minicurso de HTML é identificado pelo número 1. Depois temos o número de slots que é 3. Em seguida, os pares de números representam os cursos que possuem alunos em comum. Por exemplo, a linha com 1 2 representa que os minicursos HTML e PHP têm participantes em comum inscritos. Na saída, temos o horário em que cada curso foi definido. Por exemplo, o curso 2 ficou definido no terceiro slot. Seu programa deve funcionar para qualquer entrada que tenha essas informações.
# Entrada:
Minicursos:<br>
1 HTML  <br>
2 PHP   <br>
3 MySQL   <br>
4 Swift   <br>
Slots: 3    <br>
Pares de minicursos com inscrições em comum:  <br>
1 2   <br>
2 3   <br>
2 4   <br>
3 4   <br>
<br>
# Saída: <br> 
O curso HTML ficará no slot de horário 1 <br>
O curso PHP ficará no slot de horário 3 <br>
O curso MySQL ficará no slot de horário 2 <br>
O curso Swift ficará no slot de horário 1 <br>

# Restrições
Use variáveis atômicas da forma X ᶜ,ˢ para representar que o minicurso é ofertado no slot s. Por exemplo, a cláusula ¬(x_1,1 ∧ x_2,1) representa que os cursos 1 e 2 não podem ser realizados juntos no primeiro slot. Dessa forma, você vai construir uma fórmula da lógica proposicional que representa as restrições do problema e, em seguida, vai verificar se essa fórmula é satisfatível. Se a fórmula for satisfatível, a definição dos horários dos minicursos deve ser extraída de uma valoração que deixa a fórmula verdadeira. Veja que, a partir de uma entrada, temos que construir uma fórmula da lógica proposicional que é satisfatível se e somente se for possível usar m slots para ofertar os minicursos respeitando as inscrições em comum. Portanto, se a fórmula for insatisfatível, então não é possível usar apenas m slots. Além disso, se a fórmula for satisfatível, então a valoração que satisfaz a fórmula deve ter as informações necessárias para definir os slots dos minicursos. Você deve construir sua fórmula a partir das restrições descritas em linguagem natural a seguir:

Lógica para Computação Projeto

1. Cada minicurso deve ser ofertado em pelo menos um slot.
2. Cada minicurso deve ser ofertado em no máximo um slot.
3. Minicursos com inscrições em comum não podem ser ofertados no mesmo slot. <br>

A partir dessas restrições, você deve construir uma fórmula que as representa. Observe que as fórmulas que serão construídas dependem da entrada, ou seja, da quantidade de cursos k, da quantidade de slots m e do conjunto P. Em seguida, você deve verificar se essa fórmula é satisfatível. Você deve usar a ferramenta PySAT para criar as fórmulas e verificar a satisfatibilidade.
