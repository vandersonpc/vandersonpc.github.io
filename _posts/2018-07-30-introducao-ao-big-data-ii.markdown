---
layout: post
title: "Introdução ao Big Data II"
date: 2018-07-30
author: Vanderson Pimenta
tags:
  - Bigdata 
category: bigdata
blog: true
---

No [primeiro]({{ site.url }}{% link _posts/2018-07-28-introducao-ao-big-data-i.markdown %}) artigo tratamos dos conceitos de dado, infomração e conhecimento. Nesse segundo artigo trataremos da história da análise de dados, e como esse conceito evoluiu ao passar do tempo.

## Histórico

O primeiro conceito que surgiu sobre o uso da análise de dados com o objetivo de melhorar a tomada de decisão, foi **Business Intelligence** que surgiu em meados dos anos 90. Em seguida, a partir dos anos 2000, surgiu o conceito de **Business Analytics**. E a partir de 2007 temos o conceito de **Big Data**.

Vale ressaltar que pode haver composição entre esses termos, como por exemplo **Big Data Analytics**.

Todos esses conceitos são sistemas de informação, que possuem como objetivo comum, apoiar a tomada de decisão e melhorar o desempenho organizacional. Por essa razão são comumente chamos de ***Decision Support Systems*** ou Sistemas de Apoio a Decisão.

## Business Intelligence

**Business Inteligence** é uma metodologia de coleta, organização, análise, compartilhamento e monitoramento de informações, com o objetivo de prover suporte a gestão de negócios. É o conjunto de teorias, metodologias, processos, estruturas e tecnologias que transformam uma grande quantidade de dados brutos em informação útil para tomadas de decisões estratégicas. 

Após a coleta, os dados provenientes de diversas fontes são integrados e armazenados nos **Data WareHouses** (armazém de dados). Então a esse armazém de dados são aplicadas as técnicas de **Business Intelligence** com o objetivo de verificar os objetivo da organização.

![business_intelligence]({{ site.baseurl }}{% link img/bi.png %})

Uma das limitações do **Business Intelligence** é que seus benefícios são vistos apenas ao final do processo, pois somente relata os acontecimentos, uma vez que não prevê acontecimentos.

## Business Analytics

**Business Analytics** é um conjunto de abordagens, procedimentos, técnicas e ferramentas, que busca além de descrever o comportamento, tenta prever os acontecimentos. Para isso faz uma exploração interativa dos dados, com enfâse em **análise estatitica**, **análise quantitativa**, **mineração de dados**, **modelagem preditiva** e outras ténicas com o objetivo de identificar tendências e extrair conhecimento das informações analizadas.. 

O Business Analytics tem como objetivo descrever e prever ações. Enquanto o foco do **Business Intelligence** é **gerir** o negócio através dos dados, o foco do **Business Analytics** é **adaptar** ou mesmo **mudar** o negócio em função dos dados.

## Big Data

**Big Data** basicamente é um termo que faz referência a um grande volume de dados. Ou seja, se refere a coleta e interpretação de um conjunto massivo de dados. Utiliza técnicas avançadas de **gerenciamento**, **análise** e **visualização de dados**.

Nos próximos artigos exploraremos o **Big Data** com mais detalhes.

## Técnicas relaciondas à análise de dados

As técnias relacionadas à análise de dados podem ser categorizadas em três tipos principais: **descritiva**, **prescritiva** e **preditiva**.

![tecnica-analise]({{ site.url }}{% link img/tecnicas-analise.jpg %})

*fonte: http://forums.bsdinsight.com/threads/descriptive-predictive-and-prescriptive-analytics-explained.41558/*

* **Descritiva**: Utiliza a agregação e mineração de dados para descrever e sumarizar eventos passados, e reponder "**O que aconteceu?**"
* **Preditiva**: Utiliza modelos estatísticos e técnicas de previsão com o objetivo de entender o futuro através da análise dados recentes e históricos, para prever dados futuros, e reponder "**O que pode acontecer? Quais as tendências?**"
* **Prescritiva**: Utiliza técnicas de otimização e algorítmos de simulação para transformar os dados em ações recomendadas, e reponder "**O que fazer?**" 

![analytics-triangle]({{ site.url }}{% link img/analytic-triangle.jpg %})

*fonte: http://danalytix.blogspot.com/2013/01/business-analytics-defined.html*

Além dessas três principais técnicas, existem duas  novas definições que começam a ser utilizadas na literatura. São elas: **diagnóstica** e **cognitiva**.

* **Diagnóstica**: É um complemento da técnica descritiva, e busca saber o "**por que aconteceu?**"
* **Cognitiva**: É uma técnica que utiliza otimizações automatizadas e soluções que aprendem com o tempo (aprendizado de máquina). 

Abaixo uma imagem que sumariza o que vimos até aqui.

![analytics-summary]({{ site.url }}{% link img/analytics-summary.png %})

*fonte: http://www.supplychainshaman.com/new-technologies/infors-acquistion-of-gt-nexus-if-i-had-a-magic-wand/*

Obrigado e até o próximo artigo! Paz!!