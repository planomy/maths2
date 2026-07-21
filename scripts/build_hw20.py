#!/usr/bin/env python3
"""Rebuild maths2 homework as 20 repetitive questions; answers on next lesson slide 2."""
from pathlib import Path
import re
import html as H

ROOT = Path(__file__).resolve().parents[1]
HTML_PATH = ROOT / 'year5_maths_unit3_lessons_and_assessments(1).html'

TEACH = [
    'W2L1', 'W2L2', 'W2L3', 'W2L4', 'W3L1', 'W3L2',
    'W4L1', 'W4L2', 'W4L3', 'W4L4', 'W5L1', 'W5L2',
    'W5L3', 'W5L4', 'W6L1', 'W6L2', 'W6L3', 'W6L4',
]
NEXT = {a: b for a, b in zip(TEACH, TEACH[1:])}
NEXT['W3L2'] = 'W3L3'
NEXT['W6L4'] = 'W7L1'

TAG = "There's only one way to improve anything — practice!"


def F(n, d):
    return f'<span class="fraction"><span>{n}</span><span>{d}</span></span>'


def week_num(lesson):
    return re.match(r'W(\d+)', lesson).group(1)


BANKS = {
    'W2L1': [
        (f'{F(1,2)} = ?/4', '2/4'), (f'{F(1,2)} = ?/6', '3/6'),
        (f'{F(1,2)} = ?/8', '4/8'), (f'{F(1,2)} = ?/10', '5/10'),
        (f'{F(1,3)} = ?/6', '2/6'), (f'{F(1,3)} = ?/9', '3/9'),
        (f'{F(1,4)} = ?/8', '2/8'), (f'{F(1,4)} = ?/12', '3/12'),
        (f'{F(2,3)} = ?/6', '4/6'), (f'{F(2,3)} = ?/12', '8/12'),
        (f'{F(3,4)} = ?/8', '6/8'), (f'{F(3,5)} = ?/10', '6/10'),
        (f'Are {F(2,4)} and {F(1,2)} equivalent?', 'Yes'),
        (f'Are {F(2,5)} and {F(4,8)} equivalent?', 'No'),
        (f'Are {F(3,6)} and {F(1,2)} equivalent?', 'Yes'),
        (f'Are {F(2,3)} and {F(4,6)} equivalent?', 'Yes'),
        (f'{F(1,2)} = ?/4', '2/4'), (f'{F(1,2)} = ?/8', '4/8'),
        (f'{F(2,3)} = ?/6', '4/6'),
        (f'Are {F(3,6)} and {F(1,2)} equivalent?', 'Yes'),
    ],
    'W2L2': [
        (f'Convert {F(7,4)} to mixed.', '1 3/4'),
        (f'Convert {F(5,3)} to mixed.', '1 2/3'),
        (f'Convert {F(11,4)} to mixed.', '2 3/4'),
        (f'Convert {F(9,2)} to mixed.', '4 1/2'),
        (f'Convert {F(8,5)} to mixed.', '1 3/5'),
        (f'Convert {F(10,3)} to mixed.', '3 1/3'),
        (f'Convert {F(13,5)} to mixed.', '2 3/5'),
        (f'Convert {F(17,5)} to mixed.', '3 2/5'),
        (f'Convert 1 {F(1,4)} to improper.', '5/4'),
        (f'Convert 2 {F(1,3)} to improper.', '7/3'),
        (f'Convert 3 {F(1,2)} to improper.', '7/2'),
        (f'Convert 1 {F(2,5)} to improper.', '7/5'),
        (f'Convert 2 {F(3,4)} to improper.', '11/4'),
        (f'Convert 4 {F(1,5)} to improper.', '21/5'),
        (f'Convert {F(7,4)} to mixed.', '1 3/4'),
        (f'Convert {F(5,3)} to mixed.', '1 2/3'),
        (f'Convert 1 {F(1,4)} to improper.', '5/4'),
        (f'Convert 2 {F(1,3)} to improper.', '7/3'),
        (f'Which is larger: {F(7,4)} or 1 {F(1,2)}?', '7/4'),
        (f'Is {F(9,4)} more than 2?', 'Yes (2 1/4)'),
    ],
    'W2L3': [
        ('Value of the 6 in 4.206?', '6 thousandths'),
        ('Value of the 2 in 4.206?', '2 tenths'),
        ('Value of the 0 in 4.206?', '0 hundredths'),
        ('Write “four and two hundred and six thousandths”.', '4.206'),
        ('Write “nine and forty-two thousandths”.', '9.042'),
        ('Write “three and five tenths”.', '3.5'),
        ('Write “six and eight hundredths”.', '6.08'),
        ('Write “two and fifteen thousandths”.', '2.015'),
        ('What is the value of 7 in 5.273?', '7 hundredths'),
        ('What is the value of 3 in 5.273?', '3 thousandths'),
        ('Order from smallest: 0.4, 0.04, 0.004', '0.004, 0.04, 0.4'),
        ('Is 0.50 equal to 0.5?', 'Yes'),
        ('Is 0.50 equal to 0.05?', 'No'),
        ('Write 0.7 as thousandths.', '0.700'),
        ('Value of the 6 in 4.206?', '6 thousandths'),
        ('Write “nine and forty-two thousandths”.', '9.042'),
        ('What is the value of 7 in 5.273?', '7 hundredths'),
        ('Is 0.50 equal to 0.5?', 'Yes'),
        ('Write “six and eight hundredths”.', '6.08'),
        ('Order from smallest: 0.4, 0.04, 0.004', '0.004, 0.04, 0.4'),
    ],
    'W2L4': [
        ('Larger: 0.3 or 0.8?', '0.8'), ('Larger: 0.6 or 0.59?', '0.6'),
        ('Larger: 0.408 or 0.48?', '0.48'), ('Larger: 5.099 or 5.1?', '5.1'),
        ('Larger: 3.07 or 3.7?', '3.7'), ('Larger: 0.09 or 0.1?', '0.1'),
        ('Order: 0.4, 0.04, 0.44', '0.04, 0.4, 0.44'),
        ('Order: 1.2, 1.02, 1.20', '1.02, 1.2 = 1.20'),
        ('Rewrite 0.4 with 2 d.p.', '0.40'), ('Rewrite 0.7 with 3 d.p.', '0.700'),
        ('Larger: 0.408 or 0.48?', '0.48'), ('Larger: 5.099 or 5.1?', '5.1'),
        ('Larger: 3.07 or 3.7?', '3.7'), ('Larger: 0.6 or 0.59?', '0.6'),
        ('True/False: more digits always means larger.', 'False'),
        ('Compare 2.30 and 2.3', 'Equal'),
        ('Larger: 0.09 or 0.1?', '0.1'), ('Order: 0.4, 0.04, 0.44', '0.04, 0.4, 0.44'),
        ('Larger: 0.3 or 0.8?', '0.8'), ('Rewrite 0.4 with 2 d.p.', '0.40'),
    ],
    'W3L1': [
        ('25% as a decimal', '0.25'), ('50% as a decimal', '0.5'),
        ('10% as a decimal', '0.1'), ('75% as a decimal', '0.75'),
        ('20% as a decimal', '0.2'), ('5% as a decimal', '0.05'),
        ('0.25 as a %', '25%'), ('0.5 as a %', '50%'), ('0.1 as a %', '10%'),
        ('25% as a fraction /100', '25/100 = 1/4'),
        ('50% as a fraction', '50/100 = 1/2'),
        ('Larger: 0.7 or 65%?', '0.7'), ('Larger: 40% or 0.45?', '0.45'),
        ('65% as a decimal', '0.65'), ('65% as /100', '65/100'),
        ('25% as a decimal', '0.25'), ('50% as a decimal', '0.5'),
        ('0.25 as a %', '25%'), ('Larger: 0.7 or 65%?', '0.7'),
        ('10% as a decimal', '0.1'),
    ],
    'W3L2': [
        ('Order: 2.21, 0.02, 1.25, 1.02', '0.02, 1.02, 1.25, 2.21'),
        ('Before comparing decimals, I should…', 'Line up points / equal places'),
        (f'Shade {F(3,4)} of a bar — first step?', 'Split into 4 equal parts'),
        ('Command word “order” means…', 'Arrange by size'),
        ('Command word “explain” means…', 'Give a reason / justify'),
        ('0.5 = ?%', '50%'), (f'0.5 = ? as a half', '1/2'),
        ('Larger: 0.08 or 0.8?', '0.8'), (f'{F(1,2)} = ?/8', '4/8'),
        ('Order: 0.9, 0.09, 0.99', '0.09, 0.9, 0.99'),
        ('Write 3/10 as a decimal', '0.3'),
        ('Write 0.03 as a fraction /100', '3/100'),
        ('Order: 2.21, 0.02, 1.25, 1.02', '0.02, 1.02, 1.25, 2.21'),
        ('Larger: 0.08 or 0.8?', '0.8'), (f'{F(1,2)} = ?/8', '4/8'),
        ('0.5 = ?%', '50%'), ('Write 3/10 as a decimal', '0.3'),
        ('Command word “order” means…', 'Arrange by size'),
        ('Before comparing decimals, I should…', 'Line up points / equal places'),
        ('Write 0.03 as a fraction /100', '3/100'),
    ],
    'W4L1': [
        ('6 × 15 (split)', '90'), ('7 × 12 (split)', '84'),
        ('8 × 13 (split)', '104'), ('9 × 14 (split)', '126'),
        ('6 × 23 (split)', '138'), ('4 × 76 (split)', '304'),
        ('5 × 28 (split)', '140'), ('7 × 21 (split)', '147'),
        ('8 × 25 (split)', '200'), ('6 × 15 (split)', '90'),
        ('7 × 12 (split)', '84'), ('6 × 23 (split)', '138'),
        ('4 × 76 (split)', '304'), ('8 × 13 (split)', '104'),
        ('9 × 14 (split)', '126'), ('Name the property used in split.', 'Distributive'),
        ('23 = 20 + ?', '3'), ('15 = 10 + ?', '5'),
        ('5 × 28 (split)', '140'), ('7 × 21 (split)', '147'),
    ],
    'W4L2': [
        ('2437 × 4', '9748'), ('1305 × 3', '3915'), ('2506 × 2', '5012'),
        ('4012 × 5', '20060'), ('3120 × 4', '12480'), ('4305 × 6', '25830'),
        ('1111 × 7', '7777'), ('2008 × 4', '8032'), ('1520 × 5', '7600'),
        ('Estimate 2437 × 4', '~9600–10000'),
        ('Estimate 4305 × 6', '~24000–27000'),
        ('2437 × 4', '9748'), ('4305 × 6', '25830'), ('1305 × 3', '3915'),
        ('2506 × 2', '5012'), ('3120 × 4', '12480'), ('1111 × 7', '7777'),
        ('2008 × 4', '8032'), ('1520 × 5', '7600'), ('4012 × 5', '20060'),
    ],
    'W4L3': [
        ('36 × 40', '1440'), ('27 × 30', '810'), ('45 × 20', '900'),
        ('18 × 50', '900'), ('24 × 60', '1440'), ('33 × 40', '1320'),
        ('86 × 700', '60200'), ('25 × 300', '7500'), ('42 × 200', '8400'),
        ('36 × 4 then ×10', '144 → 1440'), ('27 × 3 then ×10', '81 → 810'),
        ('36 × 40', '1440'), ('27 × 30', '810'), ('86 × 700', '60200'),
        ('45 × 20', '900'), ('24 × 60', '1440'), ('25 × 300', '7500'),
        ('True/False: “add a zero” needs place-value meaning.', 'True'),
        ('42 × 200', '8400'), ('33 × 40', '1320'),
    ],
    'W4L4': [
        ('23 × 14 (area)', '322'), ('12 × 15 (area)', '180'),
        ('25 × 12 (area)', '300'), ('16 × 13 (area)', '208'),
        ('27 × 16 (area)', '432'), ('18 × 14 (area)', '252'),
        ('21 × 15 (area)', '315'), ('24 × 11 (area)', '264'),
        ('13 × 17 (area)', '221'),
        ('Partial products for 23 × 14: name one', 'e.g. 20×10=200'),
        ('23 × 14 (area)', '322'), ('27 × 16 (area)', '432'),
        ('12 × 15 (area)', '180'), ('25 × 12 (area)', '300'),
        ('16 × 13 (area)', '208'), ('18 × 14 (area)', '252'),
        ('21 × 15 (area)', '315'), ('24 × 11 (area)', '264'),
        ('13 × 17 (area)', '221'),
        ('How many rectangles in a 2-split × 2-split model?', '4'),
    ],
    'W5L1': [
        ('128 × 24', '3072'), ('215 × 13', '2795'), ('106 × 25', '2650'),
        ('214 × 35', '7490'), ('132 × 16', '2112'), ('240 × 15', '3600'),
        ('111 × 22', '2442'), ('150 × 14', '2100'), ('203 × 12', '2436'),
        ('Ones digit of 24 means ×?', '×4'),
        ('Tens digit of 24 means ×?', '×20'),
        ('128 × 24', '3072'), ('214 × 35', '7490'), ('215 × 13', '2795'),
        ('106 × 25', '2650'), ('132 × 16', '2112'), ('240 × 15', '3600'),
        ('111 × 22', '2442'), ('150 × 14', '2100'), ('203 × 12', '2436'),
    ],
    'W5L2': [
        ('48 bottles × 26 boxes?', '1248 bottles'),
        ('15 rows × 24 seats?', '360 seats'),
        ('8 packs × 125 stickers?', '1000 stickers'),
        ('12 × 35 = ?', '420'),
        ('Does “altogether” always mean add?', 'No — read the story'),
        ('Equal groups → which operation?', 'Multiplication'),
        ('Why cross out irrelevant facts?', 'They don’t change the maths'),
        ('48 × 26', '1248'), ('15 × 24', '360'), ('8 × 125', '1000'),
        ('12 × 35', '420'), ('30 × 18', '540'), ('25 × 16', '400'),
        ('48 × 26', '1248'), ('15 × 24', '360'), ('12 × 35', '420'),
        ('Equal groups → which operation?', 'Multiplication'),
        ('8 × 125', '1000'), ('30 × 18', '540'), ('25 × 16', '400'),
    ],
    'W5L3': [
        ('Unit for classroom length?', 'metres'),
        ('Unit for pencil length?', 'centimetres'),
        ('Unit for road trip?', 'kilometres'),
        ('Unit for a raindrop?', 'millilitres'),
        ('Unit for a dog’s mass?', 'kilograms'),
        ('Unit for a bottle of water?', 'mL or L'),
        ('Pool volume — mL or L?', 'L (or kL)'),
        ('Pencil — km or cm?', 'cm'),
        ('Sensible unit for a tap drip session?', 'mL'),
        ('Attribute first means…', 'What are we measuring?'),
        ('Unit for classroom length?', 'metres'),
        ('Unit for road trip?', 'kilometres'),
        ('Unit for a raindrop?', 'millilitres'),
        ('Pool volume — mL or L?', 'L (or kL)'),
        ('Unit for a bottle of water?', 'mL or L'),
        ('Pencil — km or cm?', 'cm'),
        ('Unit for a dog’s mass?', 'kilograms'),
        ('Unit for pencil length?', 'centimetres'),
        ('Sensible unit for a tap drip session?', 'mL'),
        ('Attribute first means…', 'What are we measuring?'),
    ],
    'W5L4': [
        ('2.4 L = ? mL', '2400 mL'), ('0.5 L = ? mL', '500 mL'),
        ('1.25 L = ? mL', '1250 mL'), ('750 mL = ? L', '0.75 L'),
        ('250 mL = ? L', '0.25 L'), ('1000 mL = ? L', '1 L'),
        ('135 mL ? 0.2 L (more/less)', 'Less (0.2 L = 200 mL)'),
        ('3 L at 50% full ≈ ?', '1.5 L'), ('Half of 1 L jug = ?', '500 mL'),
        ('Read scale: need capacity + ?', 'Interval / marks'),
        ('2.4 L = ? mL', '2400 mL'), ('0.5 L = ? mL', '500 mL'),
        ('750 mL = ? L', '0.75 L'), ('1.25 L = ? mL', '1250 mL'),
        ('250 mL = ? L', '0.25 L'), ('1000 mL = ? L', '1 L'),
        ('135 mL ? 0.2 L (more/less)', 'Less (0.2 L = 200 mL)'),
        ('Half of 1 L jug = ?', '500 mL'), ('3 L at 50% full ≈ ?', '1.5 L'),
        ('Read scale: need capacity + ?', 'Interval / marks'),
    ],
    'W6L1': [
        ('936 ÷ 6', '156'), ('484 ÷ 4', '121'), ('725 ÷ 5', '145'),
        ('846 ÷ 6', '141'), ('963 ÷ 3', '321'), ('1872 ÷ 8', '234'),
        ('640 ÷ 5', '128'), ('504 ÷ 7', '72'), ('816 ÷ 4', '204'),
        ('Check: 156 × 6 = ?', '936'),
        ('Split idea for ÷6 uses parts that are…', 'Friendly multiples of 6'),
        ('936 ÷ 6', '156'), ('484 ÷ 4', '121'), ('725 ÷ 5', '145'),
        ('846 ÷ 6', '141'), ('640 ÷ 5', '128'), ('504 ÷ 7', '72'),
        ('816 ÷ 4', '204'), ('963 ÷ 3', '321'), ('Check: 156 × 6 = ?', '936'),
    ],
    'W6L2': [
        ('257 ÷ 8 (buses seat 8) → buses needed?', '33 buses (round up)'),
        ('100 ÷ 6 exact?', '16 r4'), ('648 ÷ 6', '108'),
        ('100 ÷ 6 leftover-apples story → leftover?', '4'),
        ('Does remainder always round up?', 'No — depends on context'),
        ('30 ÷ 4', '7 r2'), ('50 ÷ 7', '7 r1'), ('90 ÷ 8', '11 r2'),
        ('Inverse check for 108 × 6', '648'),
        ('257 ÷ 8 quotient only?', '32 r1'),
        ('648 ÷ 6', '108'), ('100 ÷ 6 exact?', '16 r4'), ('30 ÷ 4', '7 r2'),
        ('50 ÷ 7', '7 r1'), ('90 ÷ 8', '11 r2'),
        ('Does remainder always round up?', 'No — depends on context'),
        ('257 ÷ 8 (buses seat 8) → buses needed?', '33 buses (round up)'),
        ('Inverse check for 108 × 6', '648'),
        ('100 ÷ 6 leftover-apples story → leftover?', '4'),
        ('257 ÷ 8 quotient only?', '32 r1'),
    ],
    'W6L3': [
        ('128 × 24', '3072'), ('936 ÷ 6', '156'), ('36 × 40', '1440'),
        ('214 × 35', '7490'), ('648 ÷ 6', '108'), ('23 × 14', '322'),
        ('Estimate 398 × 60 ≈ ?', '~24000'), ('344 × 36 drips?', '12384'),
        ('Efficient means…', 'Accurate + clear + sensible'),
        ('128 × 24', '3072'), ('936 ÷ 6', '156'), ('36 × 40', '1440'),
        ('214 × 35', '7490'), ('648 ÷ 6', '108'), ('23 × 14', '322'),
        ('Estimate 398 × 60 ≈ ?', '~24000'), ('344 × 36 drips?', '12384'),
        ('Match strategy to numbers — true/false?', 'True'),
        ('Efficient means…', 'Accurate + clear + sensible'),
        ('36 × 40', '1440'),
    ],
    'W6L4': [
        ('3-min intervals in 1 hour?', '20'),
        ('3-min intervals in 24 hours?', '480'),
        ('24 × 60 ÷ 3 = ?', '480'),
        ('If 15 mL / 3 min, ≈ mL / day?', '7200 mL'),
        ('7200 mL = ? L', '7.2 L'),
        ('Graph type for wastage over time?', 'Line graph'),
        ('Graph for categories (tap vs shower)?', 'Bar / column'),
        ('Why 100 mL scale jumps can hide changes?', 'Small differences look lost'),
        ('3-min intervals in 24 hours?', '480'),
        ('24 × 60 ÷ 3 = ?', '480'),
        ('If 15 mL / 3 min, ≈ mL / day?', '7200 mL'),
        ('7200 mL = ? L', '7.2 L'),
        ('3-min intervals in 1 hour?', '20'),
        ('Graph type for wastage over time?', 'Line graph'),
        ('Graph for categories (tap vs shower)?', 'Bar / column'),
        ('Plan: collect → ? → calculate', 'Represent / graph'),
        ('If 10 mL / 3 min, ≈ mL / day?', '4800 mL'),
        ('4800 mL = ? L', '4.8 L'),
        ('Why 100 mL scale jumps can hide changes?', 'Small differences look lost'),
        ('Plan: collect → ? → calculate', 'Represent / graph'),
    ],
}


def hw_questions_html(items, with_answers=False):
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


def make_homework(lesson, items):
    week = week_num(lesson)
    nxt = NEXT.get(lesson)
    due = f'Due next lesson · answers unlocked in {nxt} · slide 2' if nxt else 'Due next lesson'
    notes = H.escape(
        'Students complete all 20 in books. Repetition is deliberate. '
        'Do not reveal answers tonight — mark together next lesson on slide 2.'
    )
    return f'''<section class="slide" data-lesson="{lesson}" data-week="{week}" data-mins="3" data-mode="NOTEBOOK" data-notes="{notes}">
<div class="slide-topline"><div class="eyebrow">HOMEWORK · 20 PRACTICE</div><div class="mode-chip mode-notebook">NOTEBOOK</div></div>
<h1>Tonight’s practice</h1><div class="slide-body">
<p class="hw-tagline">{H.escape(TAG)}</p>
<div class="due-pill">{H.escape(due)}</div>
{hw_questions_html(items, False)}
</div></section>'''


def make_answers(lesson_for, from_lesson, items):
    week = week_num(lesson_for)
    notes = H.escape(
        f'Mark {from_lesson} homework together (~5 min). Cold-call a few explanations, then continue today’s lesson.'
    )
    return f'''<section class="slide" data-lesson="{lesson_for}" data-week="{week}" data-mins="5" data-mode="TEAMS" data-notes="{notes}">
<div class="slide-topline"><div class="eyebrow">HOMEWORK ANSWERS · {from_lesson}</div><div class="mode-chip mode-teams">TEAMS</div></div>
<h1>Mark last night’s practice</h1><div class="slide-body">
<p class="hw-tagline">{H.escape(TAG)}</p>
<div class="mark-banner">Tick / fix in books — celebrate improvement through practice.</div>
{hw_questions_html(items, True)}
</div></section>'''


def main():
    for k, v in BANKS.items():
        assert len(v) == 20, (k, len(v))

    html = HTML_PATH.read_text()

    css = r'''
.hw-tagline{font-size:clamp(18px,1.7vw,26px);font-weight:1000;color:var(--teal);margin:0 0 10px;letter-spacing:-.3px;line-height:1.2}
.hw20{display:grid;grid-template-columns:1fr 1fr;gap:8px 14px;max-height:calc(100% - 78px);overflow:auto;padding-right:4px}
.hw20 .hq{background:#f6fbfc;border:2px solid #d5e5ea;border-radius:14px;padding:8px 10px;font-size:clamp(14px,1.2vw,17px);font-weight:800;line-height:1.25;display:flex;gap:8px;align-items:flex-start}
.hw20 .hq span.n{flex:none;width:26px;height:26px;border-radius:50%;background:var(--yellow);display:grid;place-items:center;font-size:12px}
.hw20.answers .hq{background:#e8f7ed;border-color:#b7e0c3}
.hw20 .ans{color:var(--teal);font-weight:900;margin-left:auto;text-align:right;max-width:45%}
.mark-banner{margin-top:8px;margin-bottom:8px;padding:10px 14px;background:#fff3c8;border-radius:14px;font-weight:800;font-size:16px}
'''
    if '.hw-tagline{' not in html:
        html = html.replace('.diff-strip{', css + '.diff-strip{', 1)
        print('CSS added')
    else:
        # refresh css block lightly if present — skip
        print('CSS already present')

    # Replace homework slides
    for lesson, items in BANKS.items():
        m = re.search(
            rf'<section class="slide[^"]*"[^>]*data-lesson="{lesson}"[^>]*>\s*'
            rf'<div class="slide-topline"><div class="eyebrow">HOMEWORK[^<]*</div>.*?</section>',
            html,
            re.S,
        )
        if not m:
            print('NO HW', lesson)
            continue
        html = html[: m.start()] + make_homework(lesson, items) + html[m.end() :]
        print('HW', lesson)

    # Remove old answer slides
    for lesson in set(NEXT.values()):
        while True:
            m = re.search(
                rf'<section class="slide[^"]*"[^>]*data-lesson="{lesson}"[^>]*>.*?'
                rf'HOMEWORK ANSWERS.*?</section>',
                html,
                re.S,
            )
            if not m:
                break
            html = html[: m.start()] + html[m.end() :]
            print('removed answers', lesson)

    # Insert answers as slide 2 (after first section) of next lesson
    for prev, nxt in NEXT.items():
        m = re.search(
            rf'<section class="slide[^"]*"[^>]*data-lesson="{nxt}"[^>]*>.*?</section>',
            html,
            re.S,
        )
        if not m:
            print('NO first slide', nxt)
            continue
        ans = make_answers(nxt, prev, BANKS[prev])
        html = html[: m.end()] + ans + html[m.end() :]
        print(f'answers {prev} -> {nxt} slide 2')

    HTML_PATH.write_text(html)

    # verify
    html2 = HTML_PATH.read_text()
    for L in ['W2L1', 'W2L2', 'W7L1']:
        print('\n====', L)
        for i, s in enumerate(
            re.finditer(
                rf'<section class="slide[^"]*"[^>]*data-lesson="{L}"[^>]*>.*?</section>',
                html2,
                re.S,
            ),
            1,
        ):
            eb = re.search(r'class="eyebrow">([^<]+)', s.group(0))
            print(f'{i}. {eb.group(1) if eb else "?"}')
    print('tagline', html2.count(TAG))
    print('hw20', html2.count('class="hw20"'))
    print('hw20 answers', html2.count('hw20 answers'))


if __name__ == '__main__':
    main()
