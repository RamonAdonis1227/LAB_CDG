# LAB_CDG
Repositório dedicado ao controle de volume dentro do laboratório CDG HUB.

## O que é o CDG HUB?

O CODERS, DEVELOPERS AND GAMERS (CDG) HUB do Inatel é um ambiente especialmente preparado para que alunos da instituição possam se envolver em trabalhos extra-classes de pesquisa, competição e desenvolvimento que estejam diretamente ligados à área de computação

Para isso, o ambiente é composto por uma infraestrutura dinâmica e de ponta para que possa oferecer um ambiente agradável e colaborativo a todos os seus membros. O CDG Hub é formado por dois espaços que podem ser integrados ou utilizados de forma independente, são eles: o HUB DE DESENVOLVIMENTO e o CDG TREINAMENTOS.

## HUB de Desenvolvimento

O HUB DE DESENVOLVIMENTO é capaz de acomodar até 35 pessoas sentadas, possui 10 PC's de grande capacidade gráfica, 2 super servidores para realização de simulações computacionais de alto desempenho, monitores auxiliares HDMI para maior comunidade dos desenvolvedores, armário com 28 notebooks disponíveis para uso, desktops MAC, entre outros. Este espaço não é agendável e está disponível exclusivamente para alunos membros do laboratório.

## CDG Treinamentos

O CDG TREINAMENTOS é capaz de acomodar até 22 pessoas sentadas, possui 2 projetores Wi-fi de alta definição, 3 quadros brancos, uma smart board com conexão em tempo real com tablets, entre outros. Apesar de fazer parte do CDG HUB, este espaço é agendável para qualquer iniciativa que aconteça dentro do Inatel.

## Pilares

Todo este espaço conta com o apoio de professores mestres e doutores especialistas que dão total suporte aos cinco pilares de trabalhos do laboratório, que são:

- Iniciação Científica (Pesquisa);
- Estágio (Desenvolvimento de Software);
- Time de Competição de Programação do Inatel (Code Troopers);
- Times de esportes eletrônicos do Inatel (Inatel e-Sports) e a
- Comunidade Facebook Developer Circle.

Toda a estrutura do laboratório e seus trabalhos estão à disposição para visitação, porém, é necessário o agendamento prévio.

## Proposta

Tendo em vista que em muitos momentos pode acontecer de alguns alunos aumentarem o tom de voz durante suas conversas, ou até mesmo os jogadores do time se alterem com algum acontecimento durante a sessão de treinamentos, foram propostas as seguintes demandas:

- **Código:** Foi proposto ser escrito um código em Python que avalie o volume atual dentro do laboratório, e caso um volume específico definido pelo usuário como volume limite (Threshold) seja ultrapassado pelo volume do laboratório, será emitida uma mensagem de alerta ao pessoal presente no laboratório com fim de que mantenham a moderação e diminuam o volume excessivo que estão causando.

- **Pesquisa:** Foi proposto ser realizada uma pesquisa afim de avaliar as melhores bibliotecas de volume e som com intuito de serem utilizadas posteriormente no código Python que controlaria o volume dentro do laboratório.

- **Objetivo:** O objetivo principal será de controlar o volume dentro do laboratório, em nenhum momento estarei gravando áudios com fins de controle de volume, estarei apenas captando os sons no momento de execução de código e a partir dos decibéis recebidos pelo microfone da máquina e trabalhados no código será feita a avaliação do volume atual no laboratório.

## Código

O código foi desenvolvido com sucesso e com antecedência em relação ao prazo.

### Bibliotecas

Foram utilizadas as seguintes bibliotecas:

- **SoundDevice:** Foi utilizada a biblioteca sounddevice para a captura de áudio.
- **Numpy:** Foi utilizada a biblioteca numpy para a manipulação de arrays.
- **Time:** Foi utilizada a biblioteca time para a manipulação de tempo.
- **Threading:** Foi utilizada a biblioteca threading para a execução de tarefas em Threads.
- **PyGame:** Foi utilizada a biblioteca pygame para a reprodução de áudio.


## Testes

Depois do código concluido e funcionando perfeitamente, foi necessário a condução de testes e experimentações práticas no laboratório:

- **Teste 1:** Foi necessário conduzir testes com fins de determinar os níveis de volumes típicos que ocorrem durante as atividades normais do laboratório.
- **Teste 2:** Foi necessário conduzir testes observatórios para verificar o nível de ruído ambiente do laboratório durante o uso normal, pois esse nível pode variar dependendo de equipamentos em funcionamento, conversas entre as pessoas e demais atividades do laboratório.
- **Teste 3:** Foi necessário conduzir testes que considerem a distância entre a fonte do som e o microfone, pois quanto maior a distância, mais fraco será o sinal de áudio capturado pelo microfone, o que pode influenciar no nível de Threshold escolhido.
- **Teste 4:** Foi necessário conduzir testes para escolha do valor de Threshold, pois um Threshold muito baixo poderia resultar em alertas sonoros frequentes, o que seria pertubador para as pessoas do laboratório, e um Threshold muito alto pode não ser eficaz para controlar o volume em niveis aceitaveis.

## Uso Próprio

Caso você tenha interesse em utilizar o código para uso pessoal, segue algumas dicas para que você tenha facilidade de manuseio:

- **Threshold:** Você pode alterar o limite de volume definido para que o código execute na linha 9 do código, o valor escolhido por mim foi de 40 após a realização de todos os testes, mas você pode alterar para o valor que você tenha interesse em utilizar. Lembrando que esse valor não está em decibéis, é um valor normalizado do áudio para facilitar o trabalho com os volumes capturados pelo microfone!
- **Alerta Sonoro:** Você pode alterar o alerta sonoro para o som que voce tenha interesse em utilizar na linha 26 do código, inicialmente o código vem com o arquivo "Alerta.mp3" definido por padrão, mas basta você adicionar o nome do arquivo que deseja utilizar e colocar o arquivo no mesmo diretório do código que ele será executado quando o valor de Threshold for atingido.
- **Execução:** Inicialmente quando você executa o código, ele ficará executando infinitamente até que você decida que ele deve ser interrompido, a tecla para interrupção do código é "CTRL + C", quando você apertar, o código será interrompido automaticamente. Quando o alerta é emitido, o código continua capturando o áudio ambiente e fazendo a verificação de acordo com o valor de Threshold, porém o alerta só será emitido novamente quando o alerta que está em execução terminar de ser executado, há uma variável fazendo a verificação desse requisito no código.

Divirta-se utilizando o código!!


## Finalização

Foram cumpridas todas as demandas com êxito e antecendência em relação a todos os prazos, o código funcionou perfeitamente e será utilizado no laboratório!

O código [Alerta.py](https://github.com/RamonAdonis1227/LAB_CDG/blob/main/Alerta.py) foi o código desenvolvido com fim de controlar o volume dos usuários presentes no laboratório CDG HUB!


### Autor

- [Ramon Adônis Pereira de Abreu](https://github.com/RamonAdonis1227)


<img src = "https://pbs.twimg.com/media/GMLlfhYXgAAu_KV.jpg:large">
