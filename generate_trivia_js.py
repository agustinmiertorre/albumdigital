import json, re

with open('trivia_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

def js_str(s):
    # Escape for JS string
    s = str(s)
    s = s.replace('\\', '\\\\')
    s = s.replace("'", "\\'")
    return s

lines = ['const GRADE_TRIVIAS={']
for grade in sorted(data.keys()):
    gd = data[grade]
    lines.append(f"  '{grade}':" + '{')

    for lang in ['es', 'en']:
        qs = gd[lang]
        lines.append(f"    {lang}:[")
        for q in qs:
            q_str = js_str(q['q'])
            ok_str = js_str(q['ok'])
            ops_str = ','.join(f"'{js_str(op)}'" for op in q['ops'])
            lines.append(f"      {{q:'{q_str}',ok:'{ok_str}',ops:[{ops_str}]}},")
        lines.append("    ],")

    lines.append("  },")

lines.append('};')

with open('trivia_js.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))

print("Generado trivia_js.txt")
# Count questions
for g in sorted(data.keys()):
    print(f"Grado {g}: {len(data[g]['es'])} ES, {len(data[g]['en'])} EN")
