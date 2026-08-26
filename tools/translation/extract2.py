# -*- coding: utf-8 -*-
import json, re

mapping = json.load(open('mapping.json'))
lines = open('/Users/radar/Downloads/gitlab127001/awesome-osint-arsenal-zh/README.md').read().split('\n')

LABELS = {'Free','Paid','Freemium','Free/Paid','Tool','Description','Install / Link',
          'Type','Link','Free Tier','Link / Onion Address','Script','What it installs','Use when',
          'Search Query','What It Finds','Resource','URL','Data Point','How to Find'}

def translatable(s):
    s = s.strip()
    if not s or s in mapping or s in LABELS: return False
    if re.fullmatch(r'\*\*[^*]+\*\*', s): return False          # 名称列
    if 'http' in s or s.startswith('[') or s.startswith('`'): return False
    if re.match(r'^@[\w_]+$', s): return False                    # TG 机器人
    if re.fullmatch(r'[\d\W]+', s): return False
    if re.fullmatch(r'(apt|pip3?|pkg|go|gem|npm|docker) install [\w\-./@:]+', s): return False
    if re.fullmatch(r'git clone \S+.*', s): return False
    # 必须含至少一个小写英文词（排除纯名称 Title Case）
    return bool(re.search(r'(?<![A-Za-z])[a-z]{2,}(?![A-Za-z])', s.replace('*','')))

new = {}
for line in lines:
    if not re.match(r'^\s*\|', line): continue
    cells = [c.strip() for c in line.strip().strip('|').split('|')]
    if set(''.join(cells)) <= set('- : '): continue
    for c in cells:
        if translatable(c):
            new[c] = new.get(c, 0) + 1

# summary 折叠标签
for line in lines:
    m = re.match(r'^\s*(<summary><b>.*?</b>[^<]*</summary>)\s*$', line)
    if m and m.group(1) not in mapping:
        new[m.group(1)] = new.get(m.group(1), 0) + 1

out = sorted(new.keys())
BATCH = 175
for i in range(0, len(out), BATCH):
    json.dump(out[i:i+BATCH], open('batch2_%02d.en.json' % (i//BATCH+1), 'w'), ensure_ascii=False, indent=1)
print('第二轮待译:', len(out), '批次数:', (len(out)+BATCH-1)//BATCH)
json.dump(out, open('round2.all.json','w'), ensure_ascii=False, indent=1)
