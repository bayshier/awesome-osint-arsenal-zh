# -*- coding: utf-8 -*-
"""合并批次映射，应用到 README / tools.json / *.sh，生成中文版文件"""
import json, re, glob, os

SRC = '/tmp/osint-arsenal'
REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# 1) 合并映射
mapping = {}
for f in sorted(glob.glob('batch_*.zh.json')):
    mapping.update(json.load(open(f)))
json.dump(mapping, open('mapping.json','w'), ensure_ascii=False, indent=1)
print('映射条目:', len(mapping))

REPL = {re.escape(k): v for k, v in mapping.items()}

def sub_line(line):
    """整行按已知字符串替换（表格单元格/标题/注释级）"""
    for pat, zh in REPL.items():
        if pat in line:
            line = re.sub(pat, lambda m: zh, line, count=1)
            break
    return line

# 2) README：逐行处理
out = []
stats = {'table':0, 'heading':0, 'comment':0}
for line in open('README.md.orig'):
    raw = line.rstrip('\n')
    m = re.match(r'^(\s*)\|\s*(.+?)\s*\|', raw)
    if m:
        cells = [c.strip() for c in raw.strip().strip('|').split('|')]
        if len(cells) >= 2 and cells[1] in mapping:
            cells[1] = mapping[cells[1]]; stats['table'] += 1
            raw = '| ' + ' | '.join(cells) + ' |' if raw.strip().endswith('|') else raw
            # 保持原有行首缩进
            raw = (m.group(1)) + raw.lstrip()
            # 修正行尾：原行以 | 结尾
            if not raw.rstrip().endswith('|'):
                raw = raw.rstrip() + ' |'
        else:
            raw = sub_line(raw)
    else:
        h = re.match(r'^(#{1,4}\s+)(.*)$', raw)
        if h and h.group(2) in mapping:
            raw = h.group(1) + mapping[h.group(2)]; stats['heading'] += 1
        elif re.match(r'^\s*#\s', raw):
            c = re.match(r'^(\s*#\s?)(.+)$', raw)
            if c.group(2).strip() in mapping:
                raw = c.group(1) + mapping[c.group(2).strip()]; stats['comment'] += 1
    out.append(raw)
open(REPO + '/README.md','w').write('\n'.join(out) + '\n')
print('README:', stats)

# 3) tools.json description
data = json.load(open('tools.json.orig'))
n = 0
for e in data:
    d = e.get('description','')
    if d in mapping:
        e['description'] = mapping[d]; n += 1
json.dump(data, open(REPO + '/tools.json','w'), ensure_ascii=False, indent=1)
print('tools.json 描述已译:', n, '/', len(data))

# 4) 脚本：注释与 echo 整串替换
for f in glob.glob(SRC + '/*.sh'):
    name = os.path.basename(f)
    lines = open(f).read().split('\n')
    res = []
    for line in lines:
        c = re.match(r'^(\s*#\s?)(.+?)\s*$', line)
        if c and c.group(2) in mapping:
            line = c.group(1) + mapping[c.group(2)]
        else:
            e = re.match(r'^(\s*(?:echo|printf)\s+["\'])([^"\']+)(["\'])', line)
            if e and e.group(2) in mapping:
                line = e.group(1) + mapping[e.group(2)] + e.group(3)
        res.append(line)
    open(REPO + '/' + name, 'w').write('\n'.join(res))
print('脚本处理完成')
