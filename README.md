# Poo_trabalho
# Encapsulamento:
 O encapsulamento é uma das principais técnicas que define a programação orientada
a objetos. Se trata de um dos elementos que adicionam segurança à aplicação em uma
programação orientada a objetos pelo fato de esconder as propriedades, criando uma
espécie de caixa preta. <br>
 A maior parte das linguagens orientadas a objetos implementam o encapsulamento
baseado em propriedades privadas, ligadas a métodos especiais chamados getters e
setters, que irão retornar e setar o valor da propriedade, respectivamente. Essa atitude
evita o acesso direto a propriedade do objeto, adicionando uma outra camada de
segurança à aplicação. <br>
 Para fazermos um paralelo com o que vemos no mundo real, temos o encapsulamento
em outros elementos. Por exemplo, quando clicamos no botão ligar da televisão, não
sabemos o que está acontecendo internamente. Podemos então dizer que os métodos
que ligam a televisão estão encapsulados. <br>
# Herança: <br>
 O reuso de código é uma das grandes vantagens da programação orientada a objetos.
Muito disso se dá por uma questão que é conhecida como herança. Essa característica
otimiza a produção da aplicação em tempo e linhas de código. <br>
 Para entendermos essa característica, vamos imaginar uma família: a criança, por
exemplo, está herdando características de seus pais. Os pais, por sua vez, herdam algo
dos avós, o que faz com que a criança também o faça, e assim sucessivamente. O objeto
abaixo na hierarquia irá herdar características de todos os objetos acima dele, seus
“ancestrais”. A herança a partir das características do objeto mais acima é considerada
herança direta, enquanto as demais são consideradas heranças indiretas. Por exemplo,
na família, a criança herda diretamente do pai e indiretamente do avô e do bisavô. <br>
# Polimorfismo: <br>
 Outro ponto essencial na programação orientada a objetos é o chamado polimorfismo.
Na natureza, vemos animais que são capazes de alterar sua forma conforme a
necessidade, e é dessa ideia que vem o polimorfismo na orientação a objetos. Como
sabemos, os objetos filhos herdam as características e ações de seus “ancestrais”.
Entretanto, em alguns casos, é necessário que as ações para um mesmo método seja
diferente. Em outras palavras, o polimorfismo consiste na alteração do funcionamento
interno de um método herdado de um objeto pai. <br>
 Como um exemplo, temos um objeto genérico “Eletrodoméstico”. Esse objeto possui
um método, ou ação, “Ligar()”. Temos dois objetos, “Televisão” e “Geladeira”, que não
irão ser ligados da mesma forma. Assim, precisamos, para cada uma das classes filhas,
reescrever o método “Ligar()”. <br>
Com relação ao polimorfismo, valem algumas observações. Como se trata de um
assunto que está intimamente conectado à herança, entender os dois juntamente é uma
boa ideia. Outro ponto é o fato de que as linguagens de programação implementam o
polimorfismo de maneiras diferentes. O C#, por exemplo, faz uso de método virtuais
(com a palavra-chave virtual) que podem ser reimplementados (com a palavra-chave
override) nas classes filhas. Já em Java, apenas o atributo “@Override” é necessário. <br>
 Esses quatro pilares são essenciais no entendimento de qualquer linguagem orientada
a objetos e da orientação a objetos como um todo. Cada linguagem irá implementar
esses pilares de uma forma, mas essencialmente é a mesma coisa. Apenas a questão da
herança, como comentado, que pode trazer variações mais bruscas, como a presença de
herança múltipla. Além disso, o encapsulamento também é feito de maneiras distintas
nas diversas linguagens, embora os getters e setters sejam praticamente onipresentes.
