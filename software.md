---
layout: page
title: Software
permalink: /software/
---

# SACC - Sistema de Análise de Curto Circuito

_Software de análise de curto circuito em sistemas de potência (Short circuit analysis software)_

[Github Link](https://github.com/vandersonpc/SAAC)

<a href="https://github.com/{{ include.username }}"><span class="icon icon--github">{% include icon-github.svg %}</span><span class="username">{{ include.username }}</span></a>


Programa, baseado nas linguagens de programação Delphi (FrontEnd) e MatLab (BackEnd), capaz de calcular as correntes de curto-circuito e os valores de pós-falta das tensões e correntes em todos os barramentos do sistema, para faltas simétricas e assimétricas. 

Nas instalações elétricas, mesmo nas mais bem projetadas e executadas, ocorrem  faltas que resultam em sobrecorrentes elevadas. Das faltas que podem ocorrer em um sistema de potência as mais comuns são sobrecorrentes ocasionadas por curto-circuitos em algum ponto do sistema. Nessas condições, os dispositivos de proteção devem atuar com rapidez e segurança, isolando as faltas com o mínimo de dano às linhas e aos equipamentos alimentados e, se possível, sem alterar substancialmente o funcionamento global da instalação. 

O software **SACC** é composto por dois módulos: o módulo GUI (Interface gráfica com o usuário) desenvolvido utilizando-se a linguagem de programação **Delphi** e o módulo Run-Time desenvolvido em **Matlab**. O módulo GUI foi concebido com o objetivo de facilitar as ações do usuário em relação a criação e manutenção do sistema sob análise, e criar o arquivo de dados que será lido pelo módulo Run-Time. O módulo GUI é responsável por receber e organizar todas as informações provenientes do usuário tais como, os elementos do sistema e informações dos barramentos, gravar e ler os arquivos gerados para cada sistema sob análise e comunicar-se com o módulo Run-Time, afim de que este realize todos os cálculos necessários. 

Nas imagens abaixo, temos a janela principal  do programa e o fluxograma do módulo **Backend** Run-Time.



### Janela Principal do Programa


![main_window]({{ site.baseurl }}{% link img/main_window.jpg %})

### Fluxograma do módulo Run-Time


![run_time]({{ site.baseurl }}{% link img/run_time.jpg %})
