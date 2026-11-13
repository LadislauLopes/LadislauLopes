"""Gera os SVGs animados do README: pipeline-<idioma>.svg e combo-<idioma>.svg.

As fontes vão embutidas (subconjunto da Space Grotesk em woff2), porque SVG
dentro de <img> no GitHub não carrega fonte externa.

Uso, da raiz do repositório (precisa de fonttools e brotli):
    python3 img/src/anim.py img
"""
import base64, html, pathlib, subprocess, sys, tempfile

OUT = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "img")
OUT.mkdir(parents=True, exist_ok=True)
FONT_DIR = pathlib.Path("/usr/share/fonts/truetype/space-grotesk-zorin-os")
PYFTSUBSET = sys.argv[2] if len(sys.argv) > 2 else "pyftsubset"

GROUND, FIELD, INK, SOFT, ACCENT, PAPER, BAR = "#141924", "#232b3d", "#f2e9dc", "#b9b2a6", "#e8762e", "#efe6d6", "#ddd2bf"

# Ordem real da Stack-ETL (ARQUITETURA.md): o Airflow agenda e dispara, o Docker
# isola cada robô num contêiner, o Selenoid dá o navegador, o robô em Python
# coleta/trata/grava e o Google Chat avisa sucesso ou falha. O GitLab CI/CD
# builda e entrega cada robô. Nada de nomes de sistemas, hosts ou bancos.
L = {
    "pt": dict(nodes=[("Airflow", ["agenda e", "dispara"]), ("Docker", ["isola cada", "robô"]), ("Selenoid", ["dá o", "navegador"]),
                      ("Python", ["coleta, trata", "e grava"]), ("Google Chat", ["avisa a", "equipe"])],
               bar=("GitLab CI/CD", "cada robô tem repositório, imagem e deploy próprios"),
               hits=("acerto", "acertos"), done="Combo completo: do agendamento ao aviso no chat.",
               title_pipe="Fluxo animado: Airflow agenda e dispara, Docker isola cada robô, Selenoid dá o navegador, Python coleta, trata e grava, Google Chat avisa a equipe. GitLab CI/CD entrega cada robô.",
               title_combo="Controle arcade executando um combo de 9 hits: uf4 (Airflow), 4 (Docker), f,F+3 (Selenoid), b1,2 (Python), f3+4,2 (pandas), 2 (PostgreSQL), f,f,F+2+4 (Google Chat)."),
    "en": dict(nodes=[("Airflow", ["schedules,", "triggers"]), ("Docker", ["isolates", "each bot"]), ("Selenoid", ["provides the", "browser"]),
                      ("Python", ["collects, cleans,", "loads"]), ("Google Chat", ["alerts the", "team"])],
               bar=("GitLab CI/CD", "every bot has its own repo, image and deploy"),
               hits=("hit", "hits"), done="Combo complete: from schedule to chat alert.",
               title_pipe="Animated workflow: Airflow schedules and triggers, Docker isolates each bot, Selenoid provides the browser, Python collects, cleans and loads, Google Chat alerts the team. GitLab CI/CD ships every bot.",
               title_combo="Arcade controller performing a 9-hit combo: uf4 (Airflow), 4 (Docker), f,F+3 (Selenoid), b1,2 (Python), f3+4,2 (pandas), 2 (PostgreSQL), f,f,F+2+4 (Google Chat)."),
    "es": dict(nodes=[("Airflow", ["agenda y", "dispara"]), ("Docker", ["aísla cada", "robot"]), ("Selenoid", ["da el", "navegador"]),
                      ("Python", ["recolecta, trata", "y carga"]), ("Google Chat", ["avisa al", "equipo"])],
               bar=("GitLab CI/CD", "cada robot tiene su repositorio, imagen y deploy"),
               hits=("golpe", "golpes"), done="Combo completo: de la agenda al aviso en el chat.",
               title_pipe="Flujo animado: Airflow agenda y dispara, Docker aísla cada robot, Selenoid da el navegador, Python recolecta, trata y carga, Google Chat avisa al equipo. GitLab CI/CD entrega cada robot.",
               title_combo="Control arcade ejecutando un combo de 9 hits: uf4 (Airflow), 4 (Docker), f,F+3 (Selenoid), b1,2 (Python), f3+4,2 (pandas), 2 (PostgreSQL), f,f,F+2+4 (Google Chat)."),
}


def font_face(weight, ttf, text):
    with tempfile.TemporaryDirectory() as d:
        out = pathlib.Path(d) / "f.woff2"
        subprocess.run([PYFTSUBSET, str(FONT_DIR / ttf), f"--text={text}", "--flavor=woff2",
                        f"--output-file={out}", "--layout-features=kern,liga"], check=True)
        b64 = base64.b64encode(out.read_bytes()).decode()
    return f"@font-face{{font-family:SG;font-weight:{weight};src:url(data:font/woff2;base64,{b64}) format('woff2')}}"


def fonts(text):
    chars = "".join(sorted(set(text + "0123456789 ")))
    return font_face(400, "SpaceGrotesk-Regular.ttf", chars) + font_face(700, "SpaceGrotesk-Bold.ttf", chars)


def esc(s):
    return html.escape(s, quote=True)


REDUCED = "@media (prefers-reduced-motion:reduce){*{animation:none!important}}"


# ---------------------------------------------------------------- pipeline
def pipeline(t):
    n = len(t["nodes"])
    W, PAD, AW, NH, Y = 1200, 40, 34, 150, 40
    NW = (W - 2 * PAD - (n - 1) * AW) / n
    T = 7  # segundos por volta
    step = 80 / n  # % da volta para cada etapa; os 20% finais acendem a faixa do GitLab
    css, body = [], []
    for i, (name, lines) in enumerate(t["nodes"]):
        x = PAD + i * (NW + AW)
        on, off = round(step * i), round(step * i + step - 3)
        css.append(f"@keyframes n{i}{{0%,{on}%{{fill:{GROUND}}}{on+2}%,{off}%{{fill:{ACCENT}}}{off+3}%,100%{{fill:{GROUND}}}}}"
                   f"@keyframes t{i}{{0%,{on}%{{fill:{INK}}}{on+2}%,{off}%{{fill:{GROUND}}}{off+3}%,100%{{fill:{INK}}}}}"
                   f".n{i}{{animation:n{i} {T}s infinite}}.t{i}{{animation:t{i} {T}s infinite}}")
        sub = "".join(f'<tspan x="{x+18:.0f}" dy="{0 if k == 0 else 25}">{esc(l)}</tspan>' for k, l in enumerate(lines))
        body.append(f'<rect class="n{i}" x="{x:.0f}" y="{Y}" width="{NW:.0f}" height="{NH}" fill="{GROUND}"/>'
                    f'<text class="t{i}" x="{x+18:.0f}" y="{Y+56}" font-weight="700" font-size="26" letter-spacing="-.5" fill="{INK}">{esc(name)}</text>'
                    f'<text class="t{i}" x="{x+18:.0f}" y="{Y+92}" font-size="20" fill="{INK}" opacity=".9">{sub}</text>')
        if i < n - 1:
            ax, ay = x + NW, Y + NH / 2
            body.append(f'<rect x="{ax+5:.0f}" y="{ay-2}" width="{AW-18}" height="4" fill="{GROUND}"/>'
                        f'<path d="M{ax+AW-14:.0f} {ay-9}L{ax+AW-3:.0f} {ay}L{ax+AW-14:.0f} {ay+9}Z" fill="{GROUND}"/>')
            s0, e0 = round(step * i + step - 4), round(step * i + step + 1)
            css.append(f"@keyframes d{i}{{0%,{s0}%{{opacity:0;transform:translateX(0)}}{s0+1}%{{opacity:1}}{e0-1}%{{opacity:1}}{e0}%,100%{{opacity:0;transform:translateX({AW-8}px)}}}}"
                       f".d{i}{{opacity:0;animation:d{i} {T}s infinite linear}}")
            body.append(f'<rect class="d{i}" x="{ax-2:.0f}" y="{ay-6}" width="12" height="12" fill="{ACCENT}"/>')
    by = Y + NH + 16
    css.append(f"@keyframes bar{{0%,80%{{fill:{BAR}}}83%,95%{{fill:#f3b98f}}98%,100%{{fill:{BAR}}}}}.bar{{animation:bar {T}s infinite}}")
    body.append(f'<rect class="bar" x="{PAD}" y="{by}" width="{W-2*PAD}" height="64" fill="{BAR}"/>'
                f'<text x="{PAD+18}" y="{by+41}" font-size="23" fill="{GROUND}"><tspan font-weight="700" font-size="25">{esc(t["bar"][0])}</tspan>'
                f'<tspan dx="14">{esc(t["bar"][1])}</tspan></text>')
    H = by + 64 + 40
    text = "".join(nm + "".join(v) for nm, v in t["nodes"]) + "".join(t["bar"])
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img">'
            f'<title>{esc(t["title_pipe"])}</title><style>{fonts(text)}text{{font-family:SG,sans-serif}}{"".join(css)}{REDUCED}</style>'
            f'<rect width="{W}" height="{H}" fill="{PAPER}"/>{"".join(body)}</svg>')


# ---------------------------------------------------------------- combo
def arrow(cx, cy, angle, color):
    # seta desenhada (a fonte não tem ↘), apontando para baixo e girada
    return (f'<g transform="translate({cx} {cy}) rotate({angle})">'
            f'<rect x="-3" y="-13" width="6" height="16" fill="{color}"/>'
            f'<path d="M-10 1L10 1L0 14Z" fill="{color}"/></g>')


# Combo na notação numérica de 4 botões (1 e 2 em cima, 3 e 4 embaixo).
# Cada grupo de inputs é uma etapa da Stack-ETL, na ordem real de execução.
# (tempo em s, direção da alavanca ou None, botões apertados)
COMBO = [
    # notação,      etapa,         papel,      eventos
    ("uf4",         "Airflow",     "launcher", [(0.50, "uf", []), (0.62, None, [4])]),
    ("4",           "Docker",      "juggle",   [(0.80, "n", []), (1.15, None, [4])]),
    ("f,F+3",       "Selenoid",    "juggle",   [(1.60, "f", []), (1.72, "n", []), (1.82, "f", []), (1.95, None, [3]), (2.20, "n", [])]),
    ("b1,2",        "Python",      "juggle",   [(2.60, "b", []), (2.72, None, [1]), (2.85, "n", []), (3.00, None, [2])]),
    ("f3+4,2",      "pandas",      "juggle",   [(3.50, "f", []), (3.62, None, [3, 4]), (3.75, "n", []), (3.92, None, [2])]),
    ("2",           "PostgreSQL",  "juggle",   [(4.40, None, [2])]),
    ("f,f,F+2+4",   "Google Chat", "ender",    [(4.90, "f", []), (5.00, "n", []), (5.10, "f", []), (5.20, "n", []), (5.30, "f", []), (5.45, None, [2, 4]), (5.70, "n", [])]),
]
CT, CEND = 12.0, 10.8  # duração da volta e quando o combo some
DIRS = {"n": (0, 0), "u": (0, -22), "uf": (16, -16), "f": (22, 0), "b": (-22, 0), "d": (0, 22), "df": (16, 16)}


def pc(t):
    return f"{t / CT * 100:.2f}%"


def combo(t):
    W = 1200
    H = 500
    css, body = [], []
    hits = [ev[0] for g in COMBO for ev in g[3] if ev[2]]  # instantes com golpe
    first_hit = [next(ev[0] for ev in g[3] if ev[2]) for g in COMBO]
    top = 40

    # --- controle
    PX, PY, PW, PH = 40, top, 520, 290
    body.append(f'<rect x="{PX}" y="{PY}" width="{PW}" height="{PH}" fill="{FIELD}"/>')
    for sx, sy in [(PX+16, PY+16), (PX+PW-16, PY+16), (PX+16, PY+PH-16), (PX+PW-16, PY+PH-16)]:
        body.append(f'<circle cx="{sx}" cy="{sy}" r="4" fill="{GROUND}"/>')
    SX, SY = 150, PY + 150
    body.append(f'<circle cx="{SX}" cy="{SY}" r="54" fill="{GROUND}"/><circle cx="{SX}" cy="{SY}" r="14" fill="#0c0f16"/>')
    moves = [(ev[0], ev[1]) for g in COMBO for ev in g[3] if ev[1]]
    kf, prev = ["0%{transform:translate(0px,0px)}"], "n"
    for tt, d in moves:
        px, py = DIRS[prev]; dx, dy = DIRS[d]
        kf.append(f"{pc(tt-0.04)}{{transform:translate({px}px,{py}px)}}{pc(tt)}{{transform:translate({dx}px,{dy}px)}}")
        prev = d
    kf.append("100%{transform:translate(0px,0px)}")
    css.append(f"@keyframes stick{{{''.join(kf)}}}.stick{{animation:stick {CT}s infinite linear}}")
    body.append(f'<g class="stick"><rect x="{SX-5}" y="{SY-6}" width="10" height="12" fill="#0c0f16"/>'
                f'<circle cx="{SX}" cy="{SY}" r="34" fill="{PAPER}"/><circle cx="{SX-10}" cy="{SY-10}" r="9" fill="#fffaf0"/></g>')
    # botões: Vewlix de 8; 1 e 2 em cima, 3 e 4 embaixo, o resto apagado
    xs = [272, 340, 410, 480]
    pos = {1: (xs[0], PY+128), 2: (xs[1], PY+110), 3: (xs[0], PY+204), 4: (xs[1], PY+186)}
    unused = [(xs[2], PY+110), (xs[3], PY+120), (xs[2], PY+186), (xs[3], PY+196)]
    for bx, by in unused:
        body.append(f'<circle cx="{bx}" cy="{by}" r="31" fill="{GROUND}"/><circle cx="{bx}" cy="{by}" r="25" fill="#353d52"/>')
    color = {n: PAPER for n in (1, 2, 3, 4)}  # todos iguais em repouso; laranja só quando aperta
    ring = 0
    for n, (bx, by) in pos.items():
        presses = [ev[0] for g in COMBO for ev in g[3] if n in ev[2]]
        kf = [f"0%{{transform:scale(1);fill:{color[n]}}}"]
        for tt in presses:
            kf.append(f"{pc(tt-0.03)}{{transform:scale(1);fill:{color[n]}}}{pc(tt)},{pc(tt+0.12)}{{transform:scale(.84);fill:{ACCENT}}}{pc(tt+0.2)}{{transform:scale(1);fill:{color[n]}}}")
            css.append(f"@keyframes g{ring}{{0%,{pc(tt-0.01)}{{opacity:0;transform:scale(1)}}{pc(tt)}{{opacity:.9;transform:scale(1)}}{pc(tt+0.35)},100%{{opacity:0;transform:scale(1.9)}}}}"
                       f".g{ring}{{opacity:0;transform-box:fill-box;transform-origin:center;animation:g{ring} {CT}s infinite linear}}")
            body.append(f'<circle class="g{ring}" cx="{bx}" cy="{by}" r="27" fill="none" stroke="{ACCENT}" stroke-width="5"/>')
            ring += 1
        kf.append(f"100%{{transform:scale(1);fill:{color[n]}}}")
        css.append(f"@keyframes k{n}{{{''.join(kf)}}}.k{n}{{transform-box:fill-box;transform-origin:center;animation:k{n} {CT}s infinite linear}}")
        body.append(f'<circle cx="{bx}" cy="{by}" r="31" fill="{GROUND}"/><circle class="k{n}" cx="{bx}" cy="{by}" r="25" fill="{color[n]}"/>'
                    f'<text x="{bx}" y="{by+8}" text-anchor="middle" font-weight="700" font-size="22" fill="{GROUND}">{n}</text>')

    def window(cls, a, b):
        css.append(f"@keyframes {cls}{{0%,{pc(a-0.01)}{{opacity:0}}{pc(a)},{pc(b-0.01)}{{opacity:1}}{pc(b)},100%{{opacity:0}}}}.{cls}{{opacity:0;animation:{cls} {CT}s infinite linear}}")

    # --- contador de hits
    RX = 620
    cy = 140
    for k, tt in enumerate(hits):
        window(f"c{k}", tt, hits[k+1] if k + 1 < len(hits) else CEND)
        body.append(f'<text class="c{k}" x="{RX}" y="{cy}" font-weight="700" font-size="120" letter-spacing="-5" fill="{ACCENT}">{k+1}</text>')
    window("w1", hits[0], hits[1]); window("w2", hits[1], CEND)
    body.append(f'<text class="w1" x="{RX+100}" y="{cy}" font-weight="700" font-size="40" fill="{INK}">hit</text>'
                f'<text class="w2" x="{RX+100}" y="{cy}" font-weight="700" font-size="40" fill="{INK}">hits</text>')

    # lista de golpes: notação, etapa e papel; acende quando o grupo acerta
    for k, (nota, etapa, papel, _) in enumerate(COMBO):
        y = 200 + k * 38
        a = first_hit[k]
        css.append(f"@keyframes l{k}{{0%,{pc(a-0.01)}{{fill:#4a5268}}{pc(a)},{pc(CEND)}{{fill:{ACCENT}}}{pc(CEND+0.4)},100%{{fill:#4a5268}}}}.l{k}{{animation:l{k} {CT}s infinite linear}}"
                   f"@keyframes e{k}{{0%,{pc(a-0.01)}{{fill:#4a5268}}{pc(a)},{pc(CEND)}{{fill:{INK}}}{pc(CEND+0.4)},100%{{fill:#4a5268}}}}.e{k}{{animation:e{k} {CT}s infinite linear}}")
        body.append(f'<text class="l{k}" x="{RX}" y="{y}" font-weight="700" font-size="24" fill="{ACCENT}">{esc(nota)}</text>'
                    f'<text class="e{k}" x="{RX+165}" y="{y}" font-size="24" fill="{INK}">{esc(etapa)}</text>')
    dy = 470
    window("done", hits[-1] + 0.5, CEND)
    body.append(f'<text class="done" x="{RX}" y="{dy}" font-size="21" fill="{ACCENT}">{esc(t["done"])}</text>')

    text = ("".join(c[0] + c[1] + c[2] for c in COMBO) + "hits" + t["done"])
    reduced = "@media (prefers-reduced-motion:reduce){" + f".c{len(hits)-1},.w2,.done" + "{opacity:1!important}}"
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img">'
            f'<title>{esc(t["title_combo"])}</title><style>{fonts(text)}text{{font-family:SG,sans-serif}}{"".join(css)}{REDUCED}{reduced}</style>'
            f'<rect width="{W}" height="{H}" fill="{GROUND}"/>{"".join(body)}</svg>')


for k, t in L.items():
    (OUT / f"pipeline-{k}.svg").write_text(pipeline(t))
    (OUT / f"combo-{k}.svg").write_text(combo(t))
    print(k, "ok")
