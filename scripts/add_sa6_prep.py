#!/usr/bin/env python3
"""Add SA6-ready prep to W6L3 (mult/div) and W6L4 (data/scale/graphs) — parallel skills, not assessment copies."""
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


def sec(lesson, week, eyebrow, mode, mode_class, mins, title, body, answer, notes):
    return f'''<section class="slide" data-lesson="{lesson}" data-week="{week}" data-mins="{mins}" data-mode="{mode}" data-notes="{H.escape(notes)}">
<div class="slide-topline"><div class="eyebrow">{eyebrow}</div><div class="mode-chip {mode_class}">{mode}</div></div>
<h1>{title}</h1><div class="slide-body">{body}</div>{drawer(answer)}</section>'''


CSS = r'''
.sa6-chain{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin-top:10px}
.sa6-chain .step{background:#e1f8f4;border:2px solid #9ad9d0;border-radius:18px;padding:14px;text-align:center;font-weight:900;font-size:clamp(16px,1.4vw,20px);line-height:1.35}
.sa6-chain .step b{display:block;font-size:12px;letter-spacing:.08em;text-transform:uppercase;color:var(--blue);margin-bottom:6px}
.data-table{width:100%;border-collapse:collapse;margin-top:8px;font-size:clamp(15px,1.3vw,18px)}
.data-table th,.data-table td{border:2px solid #d5e5ea;padding:8px 10px;text-align:left}
.data-table th{background:#17364d;color:#fff}
.data-table tr.you td{background:#fff8e6;font-weight:800}
.graph-pick{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-top:10px}
.graph-pick .sa5-card{min-height:180px}
.eq-box{font-size:clamp(26px,2.4vw,40px);font-weight:1000;text-align:center;padding:18px;background:#f6fbfc;border:2px solid #d5e5ea;border-radius:18px;margin:10px 0}
'''


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


def make_hw(lesson, week, due, items, notes):
    return f'''<section class="slide" data-lesson="{lesson}" data-week="{week}" data-mins="3" data-mode="NOTEBOOK" data-notes="{H.escape(notes)}">
<div class="slide-topline"><div class="eyebrow">HOMEWORK · 20 PRACTICE</div><div class="mode-chip mode-notebook">NOTEBOOK</div></div>
<h1>Tonight’s practice</h1><div class="slide-body">
<p class="hw-tagline">{H.escape(TAG)}</p>
<div class="due-pill">{H.escape(due)}</div>
{hw_html(items, False)}
</div></section>'''


def make_ans(lesson_for, from_lesson, week, items, notes):
    return f'''<section class="slide" data-lesson="{lesson_for}" data-week="{week}" data-mins="5" data-mode="TEAMS" data-notes="{H.escape(notes)}">
<div class="slide-topline"><div class="eyebrow">HOMEWORK ANSWERS · {from_lesson}</div><div class="mode-chip mode-teams">TEAMS</div></div>
<h1>Mark last night’s practice</h1><div class="slide-body">
<p class="hw-tagline">{H.escape(TAG)}</p>
<div class="mark-banner">Tick / fix in books — celebrate improvement through practice.</div>
{hw_html(items, True)}
</div></section>'''


# Parallel (NOT SA6) homework banks
HW_W6L3 = [
    ('42 drips each minute. Drips in 5 minutes?', '210'),
    ('A tap drips 180 times in an hour. Times in 4 hours?', '720'),
    ('720 drips over 8 minutes. Drips each minute?', '90'),
    ('One tap: 115 drips/hour. Drips in 24 hours?', '2760'),
    ('1656 drips. If 69 per minute, how many minutes?', '24'),
    ('Solve: 64 × ___ = 1472', '23'),
    ('A faster tap drips twice as fast as 95/hour. Faster tap in 18 hours?', '3420'),
    ('Solve: (124 × 6) ÷ ___ = 93', '8'),
    ('36 × 40', '1440'), ('214 × 15', '3210'),
    ('936 ÷ 6', '156'), ('484 ÷ 4', '121'),
    ('42 drips/min × 5 min', '210'),  # rep
    ('180/hour × 4 hours', '720'),
    ('720 ÷ 8', '90'),
    ('115 × 24', '2760'),
    ('1656 ÷ 69', '24'),
    ('64 × ___ = 1472', '23'),
    ('95×2×18', '3420'),
    ('(124 × 6) ÷ ___ = 93', '8'),
]

HW_W6L4 = [
    ('3-min intervals in 1 hour?', '20'),
    ('3-min intervals in 24 hours?', '480'),
    ('24 × 60 ÷ 3 = ?', '480'),
    ('If 22 mL in 3 min, ≈ mL in 24 h?', '10560 mL'),
    ('10560 mL = ? L', '10.56 L'),
    ('If 40 mL in 3 min, ≈ mL in 24 h?', '19200 mL'),
    ('19200 mL = ? L', '19.2 L'),
    ('Better unit for 45 mL drip sample: mL or L?', 'mL'),
    ('Better unit for 24-hour wastage ~15 L: mL or L?', 'L'),
    ('Name a graph for comparing people\'s 3-min amounts', 'Bar / column'),
    ('Name a graph for wastage building over a day', 'Line graph'),
    ('Why might two taps give different 3-min totals?', 'Drip rate differs'),
    ('3-min intervals in 24 hours?', '480'),  # rep
    ('22 mL × 480', '10560 mL'),
    ('40 mL × 480', '19200 mL'),
    ('10560 mL = ? L', '10.56 L'),
    ('Bar or line for comparing classmates?', 'Bar'),
    ('Bar or line for change over 24 hours?', 'Line'),
    ('Plan: collect → ? → calculate', 'Represent / graph'),
    ('24 × 60 ÷ 3 = ?', '480'),
]


def slides_w6l3():
    out = []
    # 1 mult 1-digit context
    body = '''<div class="apply-box">A tap drips <b>42</b> times each minute. How many drips in <b>5</b> minutes? Show an efficient strategy.</div>
<div class="annotation-board" style="margin-top:12px;min-height:220px"></div>'''
    out.append(sec('W6L3', '6', 'SA6 PREP · × FLUENCY', 'NOTEBOOK', 'mode-notebook', '6',
        'Drips in a short burst', body, '42 × 5 = 210 drips.',
        'Parallel to SA6 short mult — different numbers.'))

    # 2 scale hours
    body = '''<div class="apply-box">The tap drips <b>180</b> times in one hour. How many times in <b>4</b> hours?</div>
<div class="annotation-board" style="margin-top:12px;min-height:220px"></div>'''
    out.append(sec('W6L3', '6', 'SA6 PREP · × FLUENCY', 'NOTEBOOK', 'mode-notebook', '5',
        'Scale up by hours', body, '180 × 4 = 720 drips.',
        '× tens/friendly numbers; not SA6’s 240×3.'))

    # 3 division rate
    body = '''<div class="apply-box">There were <b>720</b> drips over <b>8</b> minutes. How many drips each minute?</div>
<div class="annotation-board" style="margin-top:12px;min-height:220px"></div>'''
    out.append(sec('W6L3', '6', 'SA6 PREP · ÷ FLUENCY', 'NOTEBOOK', 'mode-notebook', '6',
        'Find the per-minute rate', body, '720 ÷ 8 = 90 drips per minute.',
        'Division as rate — different from SA6 648÷6.'))

    # 4 24-hour mult
    body = '''<div class="apply-box">One tap drips <b>115</b> times every hour. How many drips in <b>24</b> hours?</div>
<div class="annotation-board" style="margin-top:12px;min-height:220px"></div>'''
    out.append(sec('W6L3', '6', 'SA6 PREP · × 2-DIGIT', 'NOTEBOOK', 'mode-notebook', '8',
        'A full day of drips', body, '115 × 24 = 2760. (e.g. 115×20 + 115×4)',
        '3-digit × 2-digit — not SA6’s 128×24.'))

    # 5 unknown minutes
    body = '''<div class="apply-box">There were <b>1656</b> drips in total. If each minute had <b>69</b> drips, how many minutes was the tap watched?</div>
<div class="annotation-board" style="margin-top:12px;min-height:200px"></div>'''
    out.append(sec('W6L3', '6', 'SA6 PREP · ÷ FLUENCY', 'NOTEBOOK', 'mode-notebook', '6',
        'How long was it dripping?', body, '1656 ÷ 69 = 24 minutes.',
        'Inverse of equal groups — new numbers.'))

    # 6 unknown factor
    body = '''<div class="eq-box">64 × ___ = 1472</div>
<div class="annotation-board" style="min-height:200px"></div>'''
    out.append(sec('W6L3', '6', 'SA6 PREP · UNKNOWN', 'NOTEBOOK', 'mode-notebook', '6',
        'Find the missing factor', body, '1472 ÷ 64 = 23, so 64 × 23 = 1472.',
        'Unknowns skill — parallel numbers only.'))

    # 7 twice as fast multi-step
    body = '''<div class="apply-box">Your tap drips <b>95</b> times every hour. Another tap drips <b>twice as fast</b>. How many drops would the faster tap produce in <b>18</b> hours?</div>
<div class="annotation-board" style="margin-top:12px;min-height:200px"></div>'''
    out.append(sec('W6L3', '6', 'SA6 PREP · MULTI-STEP', 'NOTEBOOK', 'mode-notebook', '8',
        'Twice as fast', body, 'Faster rate 190/hour. 190 × 18 = 3420 drips.',
        'Same structure as SA6 “twice as fast” — different values.'))

    # 8 two-step unknown
    body = '''<div class="eq-box">(124 × 6) ÷ ___ = 93</div>
<div class="annotation-board" style="min-height:200px"></div>'''
    out.append(sec('W6L3', '6', 'SA6 PREP · UNKNOWN', 'NOTEBOOK', 'mode-notebook', '7',
        'Work the brackets first', body, '124 × 6 = 744. 744 ÷ ___ = 93 → ___ = 8.',
        'Order of operations / unknown — not the SA6 equation.'))

    return ''.join(out)


def slides_w6l4():
    out = []
    # 1 units
    body = '''<div class="fluency-grid">
<div>Sample jar shows ~55 mL — unit?</div>
<div>24-hour total ~12 L — unit?</div>
<div>Write 2500 mL in litres</div>
<div>Write 0.8 L in millilitres</div>
</div>
<div class="annotation-board" style="margin-top:12px;min-height:140px"></div>'''
    out.append(sec('W6L4', '6', 'SA6 PREP · UNITS', 'NOTEBOOK', 'mode-notebook', '5',
        'Sensible units', body,
        'mL for small samples; L for day totals. 2500 mL = 2.5 L; 0.8 L = 800 mL.',
        'Choosing units — not assessment wording.'))

    # 2 the 480 chain
    body = '''<div class="apply-box">Why do we multiply a <b>3-minute</b> amount by <b>480</b> to estimate <b>24 hours</b>?</div>
<div class="sa6-chain">
<div class="step"><b>Step 1</b>1 hour = 60 min<br>60 ÷ 3 = <b>20</b></div>
<div class="step"><b>Step 2</b>24 hours<br>24 × 20 = <b>480</b></div>
<div class="step"><b>Step 3</b>3-min amount × 480<br>= day estimate</div>
</div>
<div class="annotation-board" style="margin-top:10px;min-height:140px"></div>'''
    out.append(sec('W6L4', '6', 'SA6 PREP · SCALE', 'WATCH', 'mode-watch', '7',
        'The 3-minute → 24-hour bridge', body,
        '24 × 60 ÷ 3 = 480 groups of 3 minutes in a day.',
        'Teach the chain once clearly — students will use THEIR drip on SA6.'))

    # 3 practise scale with practice figure
    body = '''<div class="apply-box">Practice sample (not your SA6 tap): <b>22 mL</b> collected in 3 minutes.<br>
Estimate wastage in 24 hours. Give the answer in mL and in L.</div>
<div class="annotation-board" style="margin-top:12px;min-height:200px"></div>'''
    out.append(sec('W6L4', '6', 'SA6 PREP · SCALE', 'NOTEBOOK', 'mode-notebook', '7',
        'Scale a practice sample', body,
        '22 × 480 = 10 560 mL = 10.56 L.',
        'Rehearse the method; SA6 uses their own measurement.'))

    # 4 class table (different names/values)
    rows = ''.join(
        f'<tr><td>{n}</td><td>{v}</td></tr>'
        for n, v in [
            ('Ari', '38 mL'), ('Ben', '72 mL'), ('Cara', '110 mL'),
            ('Drew', '155 mL'), ('Eve', '41 mL'), ('Finn', '50 mL'),
        ]
    )
    body = f'''<div class="apply-box">Practice class data (different from SA6). Add a classmate row and a “you” row in your book.</div>
<table class="data-table"><tr><th>Person</th><th>Water in 3 minutes</th></tr>{rows}
<tr class="you"><td>Classmate</td><td></td></tr>
<tr class="you"><td>You (practice)</td><td></td></tr>
</table>'''
    out.append(sec('W6L4', '6', 'SA6 PREP · DATA', 'NOTEBOOK', 'mode-notebook', '6',
        'Build a comparison table', body,
        'Tables need clear labels and consistent units (mL).',
        'Same table skill — fictional data, not Sam/Fred/Sally.'))

    # 5 graph choice
    body = '''<div class="graph-pick">
<div class="sa5-card"><h3>Graph A — compare people</h3><p class="ask">Which type best compares each person’s 3-minute total?</p><div class="annotation-board" style="min-height:120px;margin-top:8px"></div></div>
<div class="sa5-card"><h3>Graph B — change over time</h3><p class="ask">Which type best shows wastage building across 24 hours?</p><div class="annotation-board" style="min-height:120px;margin-top:8px"></div></div>
</div>'''
    out.append(sec('W6L4', '6', 'SA6 PREP · GRAPHS', 'TALK', 'mode-talk', '6',
        'Two graphs, two jobs', body,
        'Compare people → bar/column. Change over a day → line graph. Titles, axes, units matter.',
        'SA6 needs two different graph types — rehearse the why.'))

    # 6 sketch bar from practice table
    body = '''<div class="apply-box">Using the practice table, sketch a <b>bar graph</b> of the six named results. Label axes and units.</div>
<div class="annotation-board" style="margin-top:12px;min-height:260px"></div>'''
    out.append(sec('W6L4', '6', 'SA6 PREP · GRAPHS', 'NOTEBOOK', 'mode-notebook', '8',
        'Sketch one graph', body,
        'Bars for Ari→Finn; vertical axis in mL; title e.g. “Water collected in 3 minutes”.',
        'Open board — kids draw; digital graph comes later on SA6.'))

    # 7 investigation checklist
    body = '''<div class="fluency-grid">
<div>□ Measure 3 minutes carefully</div>
<div>□ Record in mL</div>
<div>□ Scale with ×480</div>
<div>□ Convert to L if sensible</div>
<div>□ Table with labels</div>
<div>□ Two different graphs</div>
<div>□ Show efficient working</div>
<div>□ Check unknowns with inverse</div>
</div>
<div class="tomorrow-line" style="margin-top:12px">Next: SA6 Session 1 — collect your own drip data.</div>'''
    out.append(sec('W6L4', '6', 'SA6 PREP · READY', 'WATCH', 'mode-watch', '4',
        'Investigation checklist', body,
        'Students self-check the list before Session 1.',
        'Calm launch into SA6 — process, not answers.'))

    return ''.join(out)


def replace_intention(html, lesson, new_sec):
    pat = re.compile(
        rf'(<section class="slide[^"]*"[^>]*data-lesson="{lesson}"[^>]*>\s*'
        rf'<div class="slide-topline"><div class="eyebrow">LEARNING INTENTION</div>.*?</section>)',
        re.S,
    )
    if pat.search(html):
        return pat.sub(new_sec, html, count=1), True
    return html, False


def replace_watchout(html, lesson, new_sec):
    pat = re.compile(
        rf'(<section class="slide[^"]*"[^>]*data-lesson="{lesson}"[^>]*>\s*'
        rf'<div class="slide-topline"><div class="eyebrow">WATCH OUT</div>.*?</section>)',
        re.S,
    )
    if pat.search(html):
        return pat.sub(new_sec, html, count=1), True
    return html, False


def insert_after_watchout(html, lesson, block):
    m = re.search(
        rf'(<section class="slide[^"]*"[^>]*data-lesson="{lesson}"[^>]*>\s*'
        rf'<div class="slide-topline"><div class="eyebrow">WATCH OUT</div>.*?</section>)',
        html,
        re.S,
    )
    if not m:
        raise SystemExit(f'WATCH OUT missing for {lesson}')
    return html[: m.end()] + block + html[m.end() :]


def strip_prep(html, lesson):
    while True:
        m = re.search(
            rf'<section class="slide[^"]*"[^>]*data-lesson="{lesson}"[^>]*>\s*'
            rf'<div class="slide-topline"><div class="eyebrow">SA6 PREP[^<]*</div>.*?</section>',
            html,
            re.S,
        )
        if not m:
            break
        html = html[: m.start()] + html[m.end() :]
    return html


def replace_hw(html, lesson, new_hw):
    pat = re.compile(
        rf'<section class="slide[^"]*"[^>]*data-lesson="{lesson}"[^>]*>\s*'
        rf'<div class="slide-topline"><div class="eyebrow">HOMEWORK · 20 PRACTICE</div>.*?</section>',
        re.S,
    )
    if not pat.search(html):
        print('NO HW', lesson)
        return html
    return pat.sub(new_hw, html, count=1)


def replace_ans(html, lesson_for, from_lesson, new_ans):
    pat = re.compile(
        rf'<section class="slide[^"]*"[^>]*data-lesson="{lesson_for}"[^>]*>\s*'
        rf'<div class="slide-topline"><div class="eyebrow">HOMEWORK ANSWERS · {from_lesson}</div>.*?</section>',
        re.S,
    )
    if pat.search(html):
        return pat.sub(new_ans, html, count=1), True
    # insert as slide 2
    first = re.search(
        rf'<section class="slide[^"]*"[^>]*data-lesson="{lesson_for}"[^>]*>.*?</section>',
        html,
        re.S,
    )
    if not first:
        print('NO lesson', lesson_for)
        return html, False
    return html[: first.end()] + new_ans + html[first.end() :], True


def replace_exit(html, lesson, new_sec):
    pat = re.compile(
        rf'<section class="slide[^"]*"[^>]*data-lesson="{lesson}"[^>]*>\s*'
        rf'<div class="slide-topline"><div class="eyebrow">CHECK FOR UNDERSTANDING</div>.*?</section>',
        re.S,
    )
    if pat.search(html):
        return pat.sub(new_sec, html, count=1)
    return html


def main():
    assert len(HW_W6L3) == 20 and len(HW_W6L4) == 20
    html = HTML_PATH.read_text()

    if '.sa6-chain{' not in html:
        html = html.replace('.diff-strip{', CSS + '.diff-strip{', 1)
        print('CSS added')

    # --- W6L3 ---
    html = strip_prep(html, 'W6L3')
    intent3 = sec(
        'W6L3', '6', 'LEARNING INTENTION', 'WATCH', 'mode-watch', '2',
        'Today’s target',
        '''<div class="target-layout"><div class="target-card"><div class="target-icon">💧</div>
<h2>We are learning to…</h2>
<p>use efficient multiplication and division (including unknowns) in drip-rate stories.</p>
<div class="vocab-row"><span>rate</span><span>efficient</span><span>unknown</span><span>inverse</span></div>
</div><div class="success-card"><h2>I’ll know I’ve got it when I can…</h2>
<ul>
<li>× and ÷ large numbers with clear working</li>
<li>solve missing-number equations</li>
<li>handle multi-step “twice as fast” problems</li>
<li>check with the inverse</li>
</ul></div></div>''',
        '',
        'SA6 fluency dress-rehearsal — different numbers to the assessment.',
    )
    # intention has empty answer drawer - remove drawer if answer empty
    intent3 = intent3.replace(drawer(''), '')
    html, ok = replace_intention(html, 'W6L3', intent3)
    print('W6L3 intention', ok)

    wo3 = sec(
        'W6L3', '6', 'WATCH OUT', 'WATCH', 'mode-watch', '5',
        'Common trap',
        '''<div class="whiteboard-question">Trap: “I multiplied the hours, but forgot the drip rate had already changed (e.g. twice as fast).”</div>
<div class="annotation-board"></div>
<div class="board-hints"><span>Underline the rate</span><span>Adjust rate first</span><span>Then × hours</span></div>''',
        'Change the rate before scaling time. Annotate a two-step chain.',
        'Multi-step trap — not an assessment quote.',
    )
    html, ok = replace_watchout(html, 'W6L3', wo3)
    print('W6L3 watchout', ok)

    html = insert_after_watchout(html, 'W6L3', slides_w6l3())
    print('W6L3 prep inserted', slides_w6l3().count('<section'))

    html = replace_hw(
        html, 'W6L3',
        make_hw('W6L3', '6', 'Due W6L4 · answers on slide 2', HW_W6L3,
                '20 parallel fluency items — not SA6 numbers.'),
    )
    html = replace_exit(
        html, 'W6L3',
        sec('W6L3', '6', 'CHECK FOR UNDERSTANDING', 'NOTEBOOK', 'mode-notebook', '5',
            'Exit ticket',
            f'''<div class="exit-grid">
<div class="mini-question"><span class="question-number">1</span><div class="question-text">115 drips/hour. How many in 24 hours?</div></div>
<div class="mini-question"><span class="question-number">2</span><div class="question-text">64 × ___ = 1472</div></div>
</div>
<div class="tomorrow-line">Tomorrow: measurement, data and graphs for the investigation.</div>
<div class="response-strip">Show working. Hold up when asked.</div>''',
            '1) 2760  2) 23',
            'Quick check of ×24 and unknown factor.'),
    )

    html, ok = replace_ans(
        html, 'W6L4', 'W6L3',
        make_ans('W6L4', 'W6L3', '6', HW_W6L3, 'Mark W6L3 fluency homework, then continue.'),
    )
    print('W6L4 answers from W6L3', ok)

    # --- W6L4 ---
    html = strip_prep(html, 'W6L4')
    intent4 = sec(
        'W6L4', '6', 'LEARNING INTENTION', 'WATCH', 'mode-watch', '2',
        'Today’s target',
        '''<div class="target-layout"><div class="target-card"><div class="target-icon">📊</div>
<h2>We are learning to…</h2>
<p>plan the drip investigation: units, the ×480 scale, tables and two graph types.</p>
<div class="vocab-row"><span>sample</span><span>×480</span><span>table</span><span>bar</span><span>line</span></div>
</div><div class="success-card"><h2>I’ll know I’ve got it when I can…</h2>
<ul>
<li>explain why we multiply by 480</li>
<li>scale a 3-minute sample to 24 hours</li>
<li>choose sensible units (mL / L)</li>
<li>match graph type to the question</li>
</ul></div></div>''',
        '',
        'Investigation dress-rehearsal.',
    ).replace(drawer(''), '')
    html, ok = replace_intention(html, 'W6L4', intent4)
    print('W6L4 intention', ok)

    wo4 = sec(
        'W6L4', '6', 'WATCH OUT', 'WATCH', 'mode-watch', '5',
        'Common trap',
        '''<div class="whiteboard-question">Trap: “I multiplied my 3-minute amount by 24 because there are 24 hours.”</div>
<div class="annotation-board"></div>
<div class="board-hints"><span>3 min → hour?</span><span>Hours → day</span><span>20 × 24 = 480</span></div>''',
        'Multiply by 480 (groups of 3 minutes in a day), not by 24.',
        'The classic scale error — annotate the chain.',
    )
    html, ok = replace_watchout(html, 'W6L4', wo4)
    print('W6L4 watchout', ok)

    html = insert_after_watchout(html, 'W6L4', slides_w6l4())
    print('W6L4 prep inserted')

    html = replace_hw(
        html, 'W6L4',
        make_hw('W6L4', '6', 'Due SA6 Session 1 · answers on W7L1 slide 2', HW_W6L4,
                'Scale + graphs prep — parallel skills only.'),
    )
    html = replace_exit(
        html, 'W6L4',
        sec('W6L4', '6', 'CHECK FOR UNDERSTANDING', 'NOTEBOOK', 'mode-notebook', '5',
            'Exit ticket',
            '''<div class="exit-grid">
<div class="mini-question"><span class="question-number">1</span><div class="question-text">Why multiply a 3-minute sample by 480?</div></div>
<div class="mini-question"><span class="question-number">2</span><div class="question-text">22 mL in 3 min → mL in 24 h?</div></div>
</div>
<div class="tomorrow-line">Tomorrow: SA6 Session 1 — collect your own drip data.</div>
<div class="response-strip">Explain in a sentence + calculation.</div>''',
            '1) 480 groups of 3 min in 24 h. 2) 22 × 480 = 10 560 mL.',
            'Must hear the 480 explanation.'),
    )

    html, ok = replace_ans(
        html, 'W7L1', 'W6L4',
        make_ans('W7L1', 'W6L4', '7', HW_W6L4, 'Mark W6L4 prep, then begin SA6 Session 1.'),
    )
    print('W7L1 answers from W6L4', ok)

    # Scrub accidental SA6 fingerprints in prep eyebrows only - check whole W6L3/4
    HTML_PATH.write_text(html)

    html2 = HTML_PATH.read_text()
    for L in ['W6L3', 'W6L4']:
        print(f'\n==== {L}')
        for i, s in enumerate(
            re.finditer(rf'<section class="slide[^"]*"[^>]*data-lesson="{L}"[^>]*>.*?</section>', html2, re.S),
            1,
        ):
            eb = re.search(r'class="eyebrow">([^<]+)', s.group(0))
            print(f'{i:2}. {eb.group(1) if eb else "?"}')

    chunk = ''.join(
        m.group(0)
        for L in ['W6L3', 'W6L4']
        for m in re.finditer(rf'<section class="slide[^"]*"[^>]*data-lesson="{L}"[^>]*>.*?</section>', html2, re.S)
    )
    fingerprints = ['37 drops', '240 times', '648 drops', '128 times', '1872', '1638',
                    '172 times', '156 x 8', 'Sam:', 'Fred:', 'Sally:', 'Lisa:']
    print('\nFingerprints:')
    for f in fingerprints:
        print(f'  {f}: {chunk.count(f)}')


if __name__ == '__main__':
    main()
