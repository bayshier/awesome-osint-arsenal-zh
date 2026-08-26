# -*- coding: utf-8 -*-
"""提取三处可译唯一字符串：README 表格描述列与标题、tools.json description、脚本注释与 echo"""
import json, re, glob, os

SRC = '/tmp/osint-arsenal'
strings = {}   # en -> [来源...]

def add(s, src):
    s = s.strip()
    if not s or len(s) < 3: return
    # 纯数字/符号/网址/单命令不译
    if re.fullmatch(r'[\w\-./:#%\[\]`|>+~$@=&?—–\s]*', s) and not re.search(r'[a-zA-Z]{3,}\s+[a-zA-Z]{3,}', s):
        return
    strings.setdefault(s, [])
    if src not in strings[s]: strings[s].append(src)

# 1) README：表格第 2 列 + 标题文本
for line in open('README.md.orig'):
    line = line.rstrip('\n')
    m = re.match(r'^(\s*)\|\s*(.+?)\s*\|', line)
    if m:
        cells = [c.strip() for c in line.strip().strip('|').split('|')]
        if len(cells) >= 2 and not set(cells[0]) <= set('- :'):
            desc = cells[1].strip('`')
            if 'http' not in desc and not desc.startswith('['):
                add(desc, 'readme-table')
    h = re.match(r'^#{1,4}\s+(.*)$', line)
    if h: add(h.group(1), 'readme-heading')

# 2) tools.json description
for e in json.load(open('tools.json.orig')):
    add(e.get('description',''), 'tools.json')

# 3) 脚本注释与 echo
for f in glob.glob(SRC + '/*.sh'):
    name = os.path.basename(f)
    for line in open(f):
        line = line.rstrip('\n')
        c = re.match(r'^\s*#\s?(.+)$', line)
        if c and not c.group(1).startswith('!'):
            add(c.group(1), name)
        e = re.match(r'^\s*(?:echo|printf)\s+["\']([^"\']+)["\']', line)
        if e: add(e.group(1), name)

out = sorted(strings.keys(), key=lambda s: (-len(strings[s]), s))
json.dump({'count': len(out),
           'strings': out,
           'sources': {k: v for k, v in strings.items()}},
          open('strings.json','w'), ensure_ascii=False, indent=1)
# 生成待译批次文件（每批 150 条）
BATCH = 150
for i in range(0, len(out), BATCH):
    n = i // BATCH + 1
    json.dump(out[i:i+BATCH], open('batch_%02d.en.json' % n, 'w'), ensure_ascii=False, indent=1)
print('唯一字符串:', len(out), '| 批次数:', (len(out)+BATCH-1)//BATCH)
import collections
c = collections.Counter(tuple(v) for v in strings.values())
for k, v in c.most_common(8): print(' 来源', k, ':', v)
