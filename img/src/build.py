"""Gera os banners do README em PT, EN e ES (o pipeline e o combo animados estão em anim.py).

Edite os textos em L e rode, da raiz do repositório:
    python3 img/src/build.py /tmp/readme-html file://$PWD/img/src/lofi.jpg
    PLAYWRIGHT=<caminho>/node_modules/playwright node img/src/shoot.cjs /tmp/readme-html /tmp/readme-png
    # banner: convert banner-pt.png -strip -quality 84 -interlace Plane img/banner-pt.jpg
Fonte: Space Grotesk (instalada no sistema). Paleta tirada da ilustração lo-fi.
"""
import pathlib, sys

OUT = pathlib.Path(sys.argv[1])
LOFI = sys.argv[2]
OUT.mkdir(parents=True, exist_ok=True)

TOKENS = """
:root{--ground:#141924;--field:#1d2433;--ink:#f2e9dc;--soft:#b9b2a6;--accent:#e8762e;--paper:#efe6d6;--navy:#141924}
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:'Space Grotesk',sans-serif;-webkit-font-smoothing:antialiased}
"""

L = {
 "pt": dict(role="Desenvolvedor pleno no TJAC.",
            line="Automatizo o tratamento de dados com Python, Airflow e Docker, e construo chatbots.",
            place="Rio Branco, Acre",
            nodes=[("Selenoid","coleta"),("Python","trata"),("Airflow","orquestra"),("Google Chat","chatbot e avisos")],
            ci=("Docker + GitLab","tudo roda em contêineres, versionado e publicado pelo GitLab")),
 "en": dict(role="Mid-level developer at TJAC.",
            line="I automate data processing with Python, Airflow and Docker, and I build chatbots.",
            place="Rio Branco, Acre, Brazil",
            nodes=[("Selenoid","collects"),("Python","processes"),("Airflow","orchestrates"),("Google Chat","chatbot, alerts")],
            ci=("Docker + GitLab","everything runs in containers, versioned and shipped through GitLab")),
 "es": dict(role="Desarrollador semi-senior en el TJAC.",
            line="Automatizo el tratamiento de datos con Python, Airflow y Docker, y construyo chatbots.",
            place="Rio Branco, Acre, Brasil",
            nodes=[("Selenoid","recolecta"),("Python","trata"),("Airflow","orquesta"),("Google Chat","chatbot y avisos")],
            ci=("Docker + GitLab","todo corre en contenedores, versionado y publicado con GitLab")),
}

for k, t in L.items():
    banner = f"""<!doctype html><html><head><meta charset="utf-8"><style>{TOKENS}
body{{width:1200px;height:440px;background:var(--ground);display:grid;grid-template-columns:600px 600px;overflow:hidden}}
.txt{{padding:48px 0 44px 56px;display:flex;flex-direction:column;justify-content:space-between;color:var(--ink)}}
h1{{font-size:112px;font-weight:700;letter-spacing:-.045em;line-height:.9}}
h1 span{{display:block}}
.role{{margin-top:8px;font-size:26px;font-weight:500;letter-spacing:-.01em;line-height:1.3;max-width:500px}}
.role b{{color:var(--accent);font-weight:500}}
.line{{font-size:22px;line-height:1.4;color:var(--soft);max-width:536px;margin-top:12px}}
.place{{margin-top:14px;font-size:22px;color:var(--soft)}}
.pic{{background:url('{LOFI}') 58% 50%/cover no-repeat}}
</style></head><body>
<div class="txt"><h1><span>Ladislau</span><span>Lopes</span></h1>
<div><p class="role"><b>{t['role']}</b></p><p class="line">{t['line']}</p></div>
<p class="place">{t['place']}</p></div>
<div class="pic"></div></body></html>"""
    (OUT / f"banner-{k}.html").write_text(banner)


print("ok")
