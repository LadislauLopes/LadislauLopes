<p align="right"><a href="./readme.md">Português</a> · <a href="./README-en.md">English</a> · <b>Español</b></p>

<img src="./img/banner-es.jpg" alt="Ladislau Lopes. Desarrollador semi-senior en el TJAC. Automatizo el tratamiento de datos con Python, Airflow y Docker, y construyo chatbots. Rio Branco, Acre, Brasil." width="100%" />

<p align="right"><a href="https://www.linkedin.com/in/ladislaulopes/"><b>LinkedIn</b></a> · <a href="https://www.instagram.com/ladslopes/"><b>Instagram</b></a></p>

## Qué hago en el TJAC

Desde mayo de 2024 soy desarrollador semi-senior en el Tribunal de Justicia del Estado de Acre, Brasil. Construí desde cero la plataforma de automatización de datos (ETL + RPA) donde corren los robots de recolección y tratamiento de datos (no puedo contar cuáles). La idea central es desacoplar la orquestación de la ejecución: Airflow orquesta, Docker aísla, Selenoid da el navegador y GitLab entrega. Un robot nuevo es solo un repositorio nuevo, sin tocar Airflow. También desarrollo chatbots.

<img src="./img/pipeline-es.svg" alt="Flujo de trabajo: Airflow agenda y dispara, Docker aísla cada robot, Selenoid da el navegador, Python recolecta, trata y carga, y Google Chat avisa al equipo. GitLab CI/CD entrega cada robot con su repositorio, imagen y deploy." width="100%" />

## Arcade Builder

<a href="https://arcade-config.pages.dev/"><img src="./img/arcade-builder.jpg" alt="Control arcade montado en 3D en Arcade Builder, con arte en la parte superior y en los laterales" width="100%" /></a>

Un editor que funciona en el navegador para planificar el arte de un control arcade antes de mandarlo a fabricar. Eliges la caja y el layout, subes tus artes y ves el control montado en 3D, con los agujeros de los botones, del stick y de los tornillos en su lugar. Lo empecé porque iba a encargar el mío y no quería imprimir a ciegas; el de la imagen es ese.

- 9 modelos de caja y 37 layouts, con verificación de que la palanca cabe en la altura del lateral
- Arte, texto y logo arrastrados directamente sobre el 3D, y colores de botones Sanwa sugeridos a partir del propio arte
- Exporta PNG en 300 DPI para imprenta, placas en DXF y SVG para corte láser, un video del control girando y el texto del pedido
- Un único archivo HTML, sin servidor: three.js, JSZip, MediaRecorder e IndexedDB, y tus imágenes no salen de tu computadora

**[Probar Arcade Builder en el navegador →](https://arcade-config.pages.dev/)**

## Trayectoria

| | Institución | Período |
|:-:|---|---|
| <img src="./img/tjac.png" alt="" width="28" /> | **Tribunal de Justicia del Estado de Acre (TJAC)**<br>Desarrollador semi-senior | may/2024 – actualidad |
| <img src="./img/policia-federal.png" alt="" width="28" /> | **Policía Federal de Brasil** · [carta de recomendación](https://drive.google.com/file/d/1USAiIS-lYw2fcdw0B1r2d661BG39Q-qp/view?usp=sharing) | feb/2023 – may/2024 |

## Herramientas

Python, JavaScript, HTML y CSS, Git y GitLab, Docker, Apache Airflow, Selenium y Selenoid, Google Chat, three.js y Blender.

Estudiando ahora: TypeScript, NestJS y FastAPI.

<br />

<img src="./img/combo-es.svg" alt="Control arcade ejecutando un combo de 9 hits, un golpe por etapa del pipeline: uf4 (Airflow), 4 (Docker), f,F+3 (Selenoid), b1,2 (Python), f3+4,2 (pandas), 2 (PostgreSQL), f,f,F+2+4 (Google Chat)." width="100%" />

<p><a href="https://www.linkedin.com/in/ladislaulopes/">Gracias por jugar hasta aquí. Si quieres conversar, escríbeme por LinkedIn.</a></p>

<img src="https://komarev.com/ghpvc/?username=ladislaulopes&label=Visitas%20al%20perfil&color=141924&style=flat-square" alt="Visitas al perfil" />
