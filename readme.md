<p align="right"><b>Português</b> · <a href="./README-en.md">English</a> · <a href="./README-es.md">Español</a></p>

<img src="./img/banner-pt.jpg" alt="Ladislau Lopes. Desenvolvedor pleno no TJAC. Automatizo o tratamento de dados com Python, Airflow e Docker, e construo chatbots. Rio Branco, Acre." width="100%" />

<p align="right"><a href="https://www.linkedin.com/in/ladislaulopes/"><b>LinkedIn</b></a> · <a href="https://www.instagram.com/ladslopes/"><b>Instagram</b></a></p>

## O que eu faço no TJAC

Desde maio de 2024 sou desenvolvedor pleno no Tribunal de Justiça do Estado do Acre. Construí do zero a plataforma de automação de dados (ETL + RPA) onde rodam os robôs de coleta e tratamento de dados (quais dados, não posso contar). A ideia central é desacoplar orquestração de execução: o Airflow orquestra, o Docker isola, o Selenoid dá o navegador e o GitLab entrega. Um robô novo é só um repositório novo, sem mexer no Airflow. Também desenvolvo chatbots.

<img src="./img/pipeline-pt.svg" alt="Fluxo de trabalho: o Airflow agenda e dispara, o Docker isola cada robô, o Selenoid dá o navegador, o Python coleta, trata e grava, e o Google Chat avisa a equipe. O GitLab CI/CD entrega cada robô com repositório, imagem e deploy próprios." width="100%" />

## Arcade Builder

<a href="https://arcade-config.pages.dev/"><img src="./img/arcade-builder.jpg" alt="Controle arcade montado em 3D no Arcade Builder, com arte no topo e nas laterais" width="100%" /></a>

Um editor que roda no navegador para planejar a arte de um controle arcade antes de mandar fabricar. Você escolhe a caixa e o layout, sobe as artes e vê o controle montado em 3D, com os furos dos botões, do stick e dos parafusos no lugar certo. Comecei porque ia encomendar o meu e não queria imprimir no escuro; o da imagem é ele.

- 9 modelos de caixa e 37 layouts, com checagem se a alavanca cabe na altura da lateral
- Arte, texto e logo arrastados direto no 3D, e cores de botões Sanwa sugeridas a partir da própria arte
- Exporta PNGs em 300 DPI para a gráfica, chapas em DXF e SVG para corte a laser, um vídeo do controle girando e o texto do pedido
- Um único arquivo HTML, sem servidor: three.js, JSZip, MediaRecorder e IndexedDB, e as imagens não saem do seu computador

**[Testar o Arcade Builder no navegador →](https://arcade-config.pages.dev/)**

## Trajetória

| | Instituição | Período |
|:-:|---|---|
| <img src="./img/tjac.png" alt="" width="28" /> | **Tribunal de Justiça do Estado do Acre (TJAC)**<br>Desenvolvedor pleno | mai/2024 – atual |
| <img src="./img/policia-federal.png" alt="" width="28" /> | **Polícia Federal** · [carta de recomendação](https://drive.google.com/file/d/1USAiIS-lYw2fcdw0B1r2d661BG39Q-qp/view?usp=sharing) | fev/2023 – mai/2024 |

## Ferramentas

Python, JavaScript, HTML e CSS, Git e GitLab, Docker, Apache Airflow, Selenium e Selenoid, Google Chat, three.js e Blender.

Estudando agora: TypeScript, NestJS e FastAPI.

<br />

<img src="./img/combo-pt.svg" alt="Controle arcade executando um combo de 9 hits, um golpe por etapa do pipeline: uf4 (Airflow), 4 (Docker), f,F+3 (Selenoid), b1,2 (Python), f3+4,2 (pandas), 2 (PostgreSQL), f,f,F+2+4 (Google Chat)." width="100%" />

<p><a href="https://www.linkedin.com/in/ladislaulopes/">Obrigado por jogar até aqui. Se quiser trocar uma ideia, me chame no LinkedIn.</a></p>

<img src="https://komarev.com/ghpvc/?username=ladislaulopes&label=Visualiza%C3%A7%C3%B5es%20do%20perfil&color=141924&style=flat-square" alt="Visualizações do perfil" />
