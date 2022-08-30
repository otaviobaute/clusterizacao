# clusterizacao
Projeto de Clusterização de pontos de interesse

Esse projeto de clusterização de pontos de interesse tem quatro etapas:

1 - Tratar base de dados disponível;
2 - Tiro as médias de alguns intervalos (seg-sex , sab , dom e seg-dom) e faço a clusterização utilizando o método de elbow e o scikit learn para clusterizar meus dados;
3 - Faço o plot das curvas geradas para cada intervalo para verificar se os dados estão coerentes.
4 - Gero um mapa utilizando a biblioteca Folium para analisar o hábito de consumo em torno de cada estabelecimento (ponto de interesse)


Para executar o projeto de clusterizar pontos de interesse e criar uma base de dados que possibilite criar uma camada de inteligência no software ArcGis para atender uma demanda 
do setor que trabalho atualmente precisava construir uma base de dados. Coletei uma quantidade com um fonte interna, mas por não ser volumétricamente suficiente foi 
necessário incrementar essa base com dados coletados do próprio google.

![dados](https://user-images.githubusercontent.com/79414503/187421878-fa0428b1-8338-4e63-b293-367b76c15934.JPG)

Após coletar um número x de dados (estabelecimentos operacionais e seu hábito de consumo) os próximos passos foram descobrir o número ideal de clusters, o que é importante para 
não distribuirmos os dados em muitos clusters desnecessariamente, utilizando para isso um método matemático chamado método de Elbow.

Método de Elbow
![elbow](https://user-images.githubusercontent.com/79414503/187422218-5aa0be64-6938-446c-b27c-448cc3495dbf.JPG)

Como fica na prática a curva de dados que vainos apresentar o n° ideal de clusters
![elbow2](https://user-images.githubusercontent.com/79414503/187422726-50863c8b-e456-4570-b744-4d0104ae3cf2.JPG)

Na sequência utilizei o Kmeans, que é uma ferramenta do Scikit Learn muito utilizada para clusterização para efetuar o clustering e após efetuar o clustering utilizei o Matplotlib para tirar as médias de cada cluster e com isso gerar uma 4 curvas e plotar em um único gráfico. As curvas 
que precisava eram seg-sex, sab, dom e seg-dom.

Curva gerada pelo Matplotlib com os dados dos clusters oriundos da clusterização do recorte do hábito de consumo de seg-sex
![curva-sem](https://user-images.githubusercontent.com/79414503/187423043-c245e295-34b0-4904-97ef-6e6cf27575c3.JPG)

E por fim, antes de encaminhar os dados para criar uma nova camada de inteligência no software ArcGis, decidi gerar meu próprio mapa para validar novamente se os 
dados estavam coerentes e analisar a viabilidade do uso desse mapa.

Mapa gerado utilizando a biblioteca Folium
![maoa-folium](https://user-images.githubusercontent.com/79414503/187423694-86d5a05c-857b-4481-8587-ac8abc2cb252.JPG)


OBSERVAÇÃO:

Esses dados apresentados foram propositalmente descaracterizados para não conterem informações sensíveis e a explicação foi resumida para sintetizar o processo.
