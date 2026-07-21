#!/usr/bin/env python3
"""Add SA5-ready prep slides to W3L2: shade/grids, vertical number line, +/- , applied."""
from pathlib import Path
import re
import html as H

ROOT = Path(__file__).resolve().parents[1]
HTML_PATH = ROOT / 'year5_maths_unit3_lessons_and_assessments(1).html'

TAG = "There's only one way to improve anything — practice!"


def F(n, d):
    return f'<span class="fraction"><span>{n}</span><span>{d}</span></span>'


def drawer(answer):
    return (
        '<div class="answer-drawer"><button class="answer-close" type="button">×</button>'
        f'<div class="answer-kicker">REVEALED ANSWER</div>'
        f'<div class="answer-content">{answer}</div></div>'
    )


def section(eyebrow, mode, mode_class, mins, title, body, answer, notes):
    return f'''<section class="slide" data-lesson="W3L2" data-week="3" data-mins="{mins}" data-mode="{mode}" data-notes="{H.escape(notes)}">
<div class="slide-topline"><div class="eyebrow">{eyebrow}</div><div class="mode-chip {mode_class}">{mode}</div></div>
<h1>{title}</h1><div class="slide-body">{body}</div>{drawer(answer)}</section>'''


def rect4(shaded):
    cells = ''.join(
        f'<span class="shade-cell{" on" if i < shaded else ""}"></span>' for i in range(4)
    )
    return f'<div class="shade-rect parts-4">{cells}</div>'


def grid100(shaded_count):
    # show empty grid for students to imagine shading; optional preview class for teacher reveal via answer
    cells = ''.join('<span></span>' for _ in range(100))
    return f'<div class="hundredths-grid" style="--shade:{shaded_count}">{cells}</div>'


CSS = r'''
.sa5-pair{display:grid;grid-template-columns:1fr 1fr;gap:18px;height:100%;align-items:stretch}
.sa5-card{background:#f6fbfc;border:2px solid #d5e5ea;border-radius:20px;padding:14px 16px;display:flex;flex-direction:column;gap:10px;min-height:0}
.sa5-card h3{margin:0;font-size:clamp(18px,1.6vw,24px)}
.sa5-card .ask{font-size:clamp(16px,1.35vw,20px);font-weight:800;line-height:1.3}
.shade-rect{display:grid;gap:4px;width:100%;max-width:280px;margin:8px auto;aspect-ratio:2.4/1;border:3px solid var(--ink);border-radius:8px;overflow:hidden;background:white}
.shade-rect.parts-4{grid-template-columns:repeat(4,1fr)}
.shade-cell{background:#fff;border-right:2px solid var(--ink)}
.shade-cell:last-child{border-right:0}
.shade-cell.on{background:#75c98c}
.hundredths-grid{display:grid;grid-template-columns:repeat(10,1fr);grid-template-rows:repeat(10,1fr);width:min(42vw,260px);aspect-ratio:1;margin:6px auto;border:3px solid var(--ink);background:white}
.hundredths-grid span{border:1px solid #c5d5dc;background:#fff}
.pv-chart{width:100%;max-width:100%;margin:10px 0 0;border-collapse:collapse;table-layout:fixed;background:#fff;border:3px solid var(--ink);border-radius:12px;overflow:hidden}
.pv-chart th{background:#17364d;color:#fff;text-align:center;padding:10px 6px;font-weight:900;font-size:14px;border:1px solid #0f2433;width:33.33%}
.pv-chart td{height:72px;border:1px solid #d5e5ea;background:#fff;text-align:center;font-size:28px;font-weight:900;vertical-align:middle}
.sa5-pair.pv-three{grid-template-columns:repeat(3,minmax(0,1fr))!important;height:auto;align-items:start}
.vline-wrap{display:grid;grid-template-columns:1fr 120px 1fr;gap:10px;height:calc(100% - 40px);align-items:stretch}
.vline-side{border:2px dashed #d5e4e9;border-radius:18px;background:#fbfefe;position:relative;min-height:280px}
.vline-side .cap{position:absolute;top:10px;left:12px;font-size:13px;font-weight:900;letter-spacing:.08em;text-transform:uppercase;color:var(--blue)}
.vline{position:relative;height:100%;min-height:280px;display:flex;justify-content:center}
.vline .track{position:relative;width:4px;height:100%;background:var(--ink);border-radius:4px}
.vline .track:before,.vline .track:after{content:"";position:absolute;left:50%;transform:translateX(-50%);width:0;height:0;border-left:7px solid transparent;border-right:7px solid transparent}
.vline .track:before{top:-2px;border-bottom:12px solid var(--ink)}
.vline .track:after{bottom:-2px;border-top:12px solid var(--ink)}
.vline .tick{position:absolute;left:50%;width:16px;height:2px;background:var(--ink);transform:translateX(-50%)}
.vline .lab{position:absolute;right:calc(50% + 14px);transform:translateY(-50%);font-weight:900;font-size:18px}
.fluency-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:10px}
.fluency-grid div{background:#f6fbfc;border:2px solid #d5e5ea;border-radius:16px;padding:14px;font-size:clamp(18px,1.6vw,24px);font-weight:900;text-align:center}
.apply-box{background:#fff8e6;border:2px solid #f0d48a;border-radius:18px;padding:14px 16px;font-size:clamp(16px,1.4vw,20px);line-height:1.35;font-weight:700}
.apply-table{width:100%;border-collapse:collapse;margin-top:10px;font-size:16px}
.apply-table th,.apply-table td{border:2px solid #d5e5ea;padding:8px 10px;text-align:left}
.apply-table th{background:#17364d;color:#fff}
'''


def vline_html():
    # ticks: 0 to 2.3 in tenths = 24 positions from bottom
    ticks = []
    for i in range(0, 24):
        pct = 100 - (i / 23) * 100
        major = i % 10 == 0
        w = 22 if major else 12
        ticks.append(f'<span class="tick" style="top:{pct}%;width:{w}px"></span>')
        if major and i <= 20:
            lab = str(i // 10)
            ticks.append(f'<span class="lab" style="top:{pct}%">{lab}</span>')
    return f'''<div class="vline-wrap">
<div class="vline-side"><div class="cap">Fractions below</div></div>
<div class="vline"><div class="track">{''.join(ticks)}</div></div>
<div class="vline-side"><div class="cap">Decimals above</div></div>
</div>'''


def build_slides():
    slides = []

    # 1 Shade fractions
    body = f'''<div class="sa5-pair">
<div class="sa5-card"><h3>Shade {F(1,4)}</h3>{rect4(0)}<p class="ask">Shade exactly one of four equal parts.</p></div>
<div class="sa5-card"><h3>Shade {F(3,4)}</h3>{rect4(0)}<p class="ask">Shade three of four equal parts. Which is greater?</p></div>
</div>'''
    slides.append(section(
        'SA5 PREP · SHADE FRACTIONS', 'NOTEBOOK', 'mode-notebook', '6',
        'Shade and compare',
        body,
        f'{F(3,4)} is greater than {F(1,4)} — more equal parts of the same whole are shaded.',
        'Students shade in books or on mini-whiteboards. CFU: How do you know 3/4 is greater without counting pizza toppings?'
    ))

    # 2 Hundredths grids
    body = f'''<div class="sa5-pair">
<div class="sa5-card"><h3>Shade 0.40</h3>{grid100(0)}<p class="ask">40 hundredths — shade 40 small squares.</p></div>
<div class="sa5-card"><h3>Shade 0.04</h3>{grid100(0)}<p class="ask">4 hundredths — shade 4 small squares. Which is greater?</p></div>
</div>'''
    slides.append(section(
        'SA5 PREP · HUNDREDTHS GRIDS', 'NOTEBOOK', 'mode-notebook', '7',
        'Decimals on a hundredths grid',
        body,
        '0.40 is greater than 0.04. More digits does not mean larger — 40 hundredths &gt; 4 hundredths.',
        'Classic SA5 trap. Have students say both aloud: forty hundredths vs four hundredths.'
    ))

    # 3 Place value charts
    def chart():
        return (
            '<table class="pv-chart" aria-label="Place value chart">'
            '<thead><tr><th>Ones</th><th>Tenths</th><th>Hundredths</th></tr></thead>'
            '<tbody><tr><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr></tbody>'
            '</table>'
        )
    labels = [
        'a. 56 hundredths',
        'b. One and 5 hundredths',
        'c. Seven and 63 hundredths',
    ]
    cards = ''.join(f'<div class="sa5-card"><h3>{t}</h3>{chart()}</div>' for t in labels)
    body = f'<div class="sa5-pair pv-three">{cards}</div>'
    slides.append(section(
        'SA5 PREP · PLACE VALUE', 'NOTEBOOK', 'mode-notebook', '6',
        'Build each number',
        body,
        'a) 0.56 &nbsp; b) 1.05 &nbsp; c) 7.63',
        'Circulate for the classic error: writing 56 hundredths as 56.0 or 5.6.'
    ))

    # 4 Order decimals (assessment list)
    body = '''<p class="ask" style="margin-bottom:10px">Order from <b>smallest to greatest</b>:</p>
<div class="fluency-grid">
<div>2.21</div><div>0.02</div><div>2.22</div><div>1.25</div><div>1.02</div><div>0.50</div>
</div>
<div class="annotation-board" style="margin-top:12px;min-height:160px"></div>'''
    slides.append(section(
        'SA5 PREP · ORDER DECIMALS', 'NOTEBOOK', 'mode-notebook', '6',
        'Smallest to greatest',
        body,
        '0.02 , 0.50 , 1.02 , 1.25 , 2.21 , 2.22',
        'Same set family as SA5 Q6. Line up points; compare left to right.'
    ))

    # 5 Vertical number line — decimals
    body = f'''<p class="ask" style="margin-bottom:8px">Label these <b>decimals to the right</b> of the number line (SA5 sheet style): 0.5, 1.2, 0.2, 1.5, 2.1, 0.8</p>
{vline_html()}'''
    slides.append(section(
        'SA5 PREP · NUMBER LINE', 'NOTEBOOK', 'mode-notebook', '8',
        'Decimals on the vertical line',
        body,
        'Each small tick = 0.1. Check 0.5 midway 0→1; 1.5 midway 1→2; 2.1 one tick above 2.',
        'Match the assessment sheet: vertical, tenths. Students annotate on the right side.'
    ))

    # 6 Vertical number line — fractions
    fracs = f'{F(5,10)}, {F(14,10)}, {F(6,5)}, 1 {F(2,5)}, 2 {F(1,10)}, 2 {F(3,10)}'
    body = f'''<p class="ask" style="margin-bottom:8px">Label these <b>fractions to the left</b> (convert first if needed): {fracs}</p>
{vline_html()}'''
    slides.append(section(
        'SA5 PREP · NUMBER LINE', 'NOTEBOOK', 'mode-notebook', '8',
        'Fractions on the vertical line',
        body,
        f'{F(5,10)}=0.5; {F(14,10)}=1.4; {F(6,5)}=1.2; 1 {F(2,5)}=1.4; 2 {F(1,10)}=2.1; 2 {F(3,10)}=2.3',
        'Force conversion to tenths/decimals before placing. Same skill as SA5 Q8.'
    ))

    # 7 Jill reasoning
    body = f'''<div class="apply-box">Jill placed <b>3 {F(2,8)}</b>, <b>3 {F(1,2)}</b> and <b>4 {F(3,4)}</b> on a number line from 3 to 5.<br>
Is Jill correct? How do you know?</div>
<div class="annotation-board" style="margin-top:12px;min-height:220px"></div>'''
    slides.append(section(
        'SA5 PREP · REASONING', 'TALK', 'mode-talk', '7',
        'Is Jill correct?',
        body,
        f'Convert: 3 {F(2,8)}=3.25; 3 {F(1,2)}=3.5; 4 {F(3,4)}=4.75. Check order and spacing on 3→5.',
        'Demand a written “because”. Related denominators + mixed numerals.'
    ))

    # 8 Fraction +/- fluency
    items = [
        f'{F(3,5)} + {F(1,5)} =', f'{F(4,10)} + {F(5,10)} =',
        f'{F(5,6)} − {F(2,6)} =', f'{F(8,10)} − {F(3,10)} =',
        f'{F(11,12)} − {F(5,12)} =', f'{F(2,8)} + {F(3,8)} =',
        f'{F(1,4)} + {F(2,4)} =', f'{F(7,10)} − {F(2,10)} =',
    ]
    body = '<div class="fluency-grid">' + ''.join(f'<div>{x}</div>' for x in items) + '</div>'
    slides.append(section(
        'SA5 PREP · FLUENCY', 'NOTEBOOK', 'mode-notebook', '8',
        'Same-denominator + and −',
        body,
        f'{F(4,5)}; {F(9,10)}; {F(3,6)}={F(1,2)}; {F(5,10)}={F(1,2)}; {F(6,12)}={F(1,2)}; {F(5,8)}; {F(3,4)}; {F(5,10)}={F(1,2)}',
        'Exact SA5 Q12 family. Keep denominators unchanged; only combine numerators.'
    ))

    # 9 Related denominators / fabric
    body = f'''<div class="apply-box">Georgie needs <b>2 {F(4,10)}</b> metres of the same-coloured fabric.<br>
She has: green <b>2 {F(1,5)}</b> · red <b>2 {F(1,2)}</b> · blue <b>2 {F(3,5)}</b>.<br>
What could Georgie use? Show working.</div>
<div class="annotation-board" style="margin-top:12px;min-height:200px"></div>'''
    slides.append(section(
        'SA5 PREP · RELATED FRACTIONS', 'NOTEBOOK', 'mode-notebook', '8',
        'Fabric lengths',
        body,
        f'Need 2 {F(4,10)}=2 {F(2,5)}. Green 2 {F(1,5)} too short; red 2 {F(1,2)}=2 {F(5,10)} enough; blue 2 {F(3,5)}=2 {F(6,10)} enough. Red or blue.',
        'Related denominators (fifths/tenths/halves). Convert before comparing.'
    ))

    # 10 Swimming applied
    rows = ''.join(
        f'<tr><td>{n}</td><td>{t}</td></tr>'
        for n, t in [
            ('Sarah', '39.45'), ('Mana', '39.55'), ('Sam', '39.58'),
            ('Darcy', '39.6'), ('Piper', '39.05'), ('Ali', '39.01'),
        ]
    )
    body = f'''<div class="apply-box">Swimmers faster than <b>39 {F(1,2)}</b> seconds go to the regional final. Who goes? Show working.</div>
<table class="apply-table"><tr><th>Swimmer</th><th>Time (s)</th></tr>{rows}</table>
<div class="annotation-board" style="margin-top:10px;min-height:140px"></div>'''
    slides.append(section(
        'SA5 PREP · APPLY', 'NOTEBOOK', 'mode-notebook', '8',
        'Faster than 39½ seconds',
        body,
        f'39 {F(1,2)}=39.5. Faster means &lt; 39.5 → Sarah 39.45, Piper 39.05, Ali 39.01.',
        'Convert the mixed numeral first. Faster = smaller time.'
    ))

    return ''.join(slides)


SA5_HW = [
    (f'Shade meaning of {F(1,4)} (how many of 4?)', '1 of 4'),
    (f'Shade meaning of {F(3,4)}', '3 of 4'),
    ('Which is greater: 0.40 or 0.04?', '0.40'),
    ('56 hundredths as a decimal', '0.56'),
    ('One and 5 hundredths as a decimal', '1.05'),
    ('Seven and 63 hundredths as a decimal', '7.63'),
    ('Order: 0.02, 1.02, 0.50 (smallest→greatest)', '0.02, 0.50, 1.02'),
    ('Order: 2.21, 2.22, 1.25', '1.25, 2.21, 2.22'),
    (f'{F(3,5)} + {F(1,5)} =', '4/5'),
    (f'{F(4,10)} + {F(5,10)} =', '9/10'),
    (f'{F(5,6)} − {F(2,6)} =', '3/6 = 1/2'),
    (f'{F(8,10)} − {F(3,10)} =', '5/10 = 1/2'),
    (f'{F(11,12)} − {F(5,12)} =', '6/12 = 1/2'),
    (f'2 {F(4,10)} = ? fifths mixed', '2 2/5'),
    (f'Is 2 {F(1,5)} enough for 2 {F(4,10)}?', 'No'),
    ('39.45 ? 39.5 (faster/slower time)', 'Faster'),
    ('Which is greater: 0.40 or 0.04?', '0.40'),  # rep
    (f'{F(3,5)} + {F(1,5)} =', '4/5'),  # rep
    ('56 hundredths as a decimal', '0.56'),  # rep
    ('Order: 0.02, 1.02, 0.50 (smallest→greatest)', '0.02, 0.50, 1.02'),  # rep
]


def hw_html(items, with_answers=False):
    cls = 'hw20 answers' if with_answers else 'hw20'
    parts = []
    for i, (q, a) in enumerate(items, 1):
        if with_answers:
            parts.append(
                f'<div class="hq"><span class="n">{i}</span><span>{q}</span>'
                f'<span class="ans">{H.escape(a)}</span></div>'
            )
        else:
            parts.append(f'<div class="hq"><span class="n">{i}</span><span>{q}</span></div>')
    return f'<div class="{cls}">{"".join(parts)}</div>'


def make_homework():
    notes = H.escape(
        'SA5 eve practice — 20 reps. Mark together on W3L3 slide 2 before the assessment starts.'
    )
    due = 'Due SA5 Session 1 · answers unlocked in W3L3 · slide 2'
    return f'''<section class="slide" data-lesson="W3L2" data-week="3" data-mins="3" data-mode="NOTEBOOK" data-notes="{notes}">
<div class="slide-topline"><div class="eyebrow">HOMEWORK · 20 PRACTICE</div><div class="mode-chip mode-notebook">NOTEBOOK</div></div>
<h1>Tonight’s practice</h1><div class="slide-body">
<p class="hw-tagline">{H.escape(TAG)}</p>
<div class="due-pill">{H.escape(due)}</div>
{hw_html(SA5_HW, False)}
</div></section>'''


def make_answers_w3l3():
    notes = H.escape('Mark W3L2 SA5 prep homework (~5 min), then begin Session 1.')
    return f'''<section class="slide" data-lesson="W3L3" data-week="3" data-mins="5" data-mode="TEAMS" data-notes="{notes}">
<div class="slide-topline"><div class="eyebrow">HOMEWORK ANSWERS · W3L2</div><div class="mode-chip mode-teams">TEAMS</div></div>
<h1>Mark last night’s practice</h1><div class="slide-body">
<p class="hw-tagline">{H.escape(TAG)}</p>
<div class="mark-banner">Tick / fix — then you are ready for SA5.</div>
{hw_html(SA5_HW, True)}
</div></section>'''


def main():
    html = HTML_PATH.read_text()

    if '.sa5-pair{' not in html:
        html = html.replace('.diff-strip{', CSS + '.diff-strip{', 1)
        print('CSS added')

    # Update W3L2 intention if present
    intent = re.search(
        r'(<section class="slide[^"]*"[^>]*data-lesson="W3L2"[^>]*>\s*'
        r'<div class="slide-topline"><div class="eyebrow">LEARNING INTENTION</div>.*?</section>)',
        html,
        re.S,
    )
    if intent:
        new_intent = '''<section class="slide" data-lesson="W3L2" data-week="3" data-mins="2" data-mode="WATCH" data-notes="Read success criteria aloud. Today is SA5 dress-rehearsal.">
<div class="slide-topline"><div class="eyebrow">LEARNING INTENTION</div><div class="mode-chip mode-watch">WATCH</div></div>
<h1>Today’s target</h1><div class="slide-body"><div class="target-layout"><div class="target-card"><div class="target-icon">🧩</div>
<h2>We are learning to…</h2>
<p>prepare for SA5: shade, place value, order on a number line, add/subtract fractions, and explain.</p>
<div class="vocab-row"><span>shade</span><span>hundredths</span><span>order</span><span>related</span><span>explain</span></div>
</div><div class="success-card"><h2>I’ll know I’ve got it when I can…</h2>
<ul>
<li>shade fractions and hundredths grids accurately</li>
<li>place decimals and fractions on a vertical tenths line</li>
<li>add/subtract same-denominator fractions fluently</li>
<li>solve a mixed-number compare/apply problem and justify</li>
</ul></div></div></div></section>'''
        html = html.replace(intent.group(1), new_intent, 1)
        print('intention updated')

    # Fix watch-out trap to SA5-relevant
    wo = re.search(
        r'(<section class="slide[^"]*"[^>]*data-lesson="W3L2"[^>]*>\s*'
        r'<div class="slide-topline"><div class="eyebrow">WATCH OUT</div>.*?</section>)',
        html,
        re.S,
    )
    if wo:
        new_wo = section(
            'WATCH OUT', 'WATCH', 'mode-watch', '5',
            'Common trap',
            '''<div class="whiteboard-question">Trap: “0.04 is larger than 0.40 because it has a 4 in the hundredths and looks busier.”</div>
<div class="annotation-board"></div>
<div class="board-hints"><span>Say the places aloud</span><span>Shade both on a hundredths grid</span><span>Line up the points</span></div>''',
            '0.40 &gt; 0.04. Forty hundredths is ten times four hundredths.',
            'This is the SA5 Q3–4 trap. Annotate a grid comparison.'
        )
        # section() already wraps answer drawer; but uses WATCH OUT eyebrow - good
        html = html.replace(wo.group(1), new_wo, 1)
        print('watch-out updated')

    # Remove previously inserted SA5 PREP slides (idempotent)
    while True:
        m = re.search(
            r'<section class="slide[^"]*"[^>]*data-lesson="W3L2"[^>]*>\s*'
            r'<div class="slide-topline"><div class="eyebrow">SA5 PREP[^<]*</div>.*?</section>',
            html,
            re.S,
        )
        if not m:
            break
        html = html[: m.start()] + html[m.end() :]
        print('removed old SA5 prep slide')

    # Insert new slides after WATCH OUT
    wo2 = re.search(
        r'(<section class="slide[^"]*"[^>]*data-lesson="W3L2"[^>]*>\s*'
        r'<div class="slide-topline"><div class="eyebrow">WATCH OUT</div>.*?</section>)',
        html,
        re.S,
    )
    if not wo2:
        raise SystemExit('WATCH OUT not found')
    block = build_slides()
    html = html[: wo2.end()] + block + html[wo2.end() :]
    print('inserted', block.count('SA5 PREP'), 'prep markers /', block.count('<section'), 'sections')

    # Replace W3L2 homework
    hw = re.search(
        r'<section class="slide[^"]*"[^>]*data-lesson="W3L2"[^>]*>\s*'
        r'<div class="slide-topline"><div class="eyebrow">HOMEWORK[^<]*</div>.*?</section>',
        html,
        re.S,
    )
    if hw:
        html = html[: hw.start()] + make_homework() + html[hw.end() :]
        print('homework replaced')

    # Replace W3L3 homework answers for W3L2 (or insert at slide 2)
    # Remove existing HOMEWORK ANSWERS · W3L2 on W3L3
    while True:
        m = re.search(
            r'<section class="slide[^"]*"[^>]*data-lesson="W3L3"[^>]*>.*?'
            r'HOMEWORK ANSWERS · W3L2.*?</section>',
            html,
            re.S,
        )
        if not m:
            break
        html = html[: m.start()] + html[m.end() :]
        print('removed old W3L3 answers')

    first = re.search(
        r'<section class="slide[^"]*"[^>]*data-lesson="W3L3"[^>]*>.*?</section>',
        html,
        re.S,
    )
    if first:
        html = html[: first.end()] + make_answers_w3l3() + html[first.end() :]
        print('W3L3 slide-2 answers inserted')

    # Stronger exit ticket for W3L2
    ex = re.search(
        r'(<section class="slide[^"]*"[^>]*data-lesson="W3L2"[^>]*>\s*'
        r'<div class="slide-topline"><div class="eyebrow">CHECK FOR UNDERSTANDING</div>.*?</section>)',
        html,
        re.S,
    )
    if ex:
        new_ex = f'''<section class="slide" data-lesson="W3L2" data-week="3" data-mins="5" data-mode="NOTEBOOK" data-notes="Exit = mini-SA5. Collect and sort for tomorrow’s groups.">
<div class="slide-topline"><div class="eyebrow">CHECK FOR UNDERSTANDING</div><div class="mode-chip mode-notebook">NOTEBOOK</div></div>
<h1>Exit ticket</h1><div class="slide-body"><div class="exit-grid">
<div class="mini-question"><span class="question-number">1</span><div class="question-text">Which is greater: 0.40 or 0.04? Why?</div></div>
<div class="mini-question"><span class="question-number">2</span><div class="question-text">{F(3,5)} + {F(1,5)} = ?</div></div>
</div>
<div class="tomorrow-line">Tomorrow: SA5 Session 1 — bring calm strategies and clear working.</div>
<div class="response-strip">Write in your notepad. Hold it up when asked.</div>
</div>{drawer('1) 0.40 — forty hundredths &gt; four hundredths. 2) 4/5')}</section>'''
        html = html.replace(ex.group(1), new_ex, 1)
        print('exit updated')

    HTML_PATH.write_text(html)

    # verify
    html2 = HTML_PATH.read_text()
    print('\nW3L2 slides:')
    for i, s in enumerate(
        re.finditer(r'<section class="slide[^"]*"[^>]*data-lesson="W3L2"[^>]*>.*?</section>', html2, re.S),
        1,
    ):
        eb = re.search(r'class="eyebrow">([^<]+)', s.group(0))
        h1 = re.search(r'<h1>(.*?)</h1>', s.group(0))
        print(f'{i:2}. {eb.group(1)[:40] if eb else "?":40} | {re.sub("<[^>]+>","", h1.group(1) if h1 else "")[:42]}')
    print('W3L3 slide 2:', end=' ')
    secs = list(re.finditer(r'<section class="slide[^"]*"[^>]*data-lesson="W3L3"[^>]*>.*?</section>', html2, re.S))
    if len(secs) >= 2:
        eb = re.search(r'class="eyebrow">([^<]+)', secs[1].group(0))
        print(eb.group(1) if eb else '?')


if __name__ == '__main__':
    main()
