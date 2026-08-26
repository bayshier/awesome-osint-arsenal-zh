# -*- coding: utf-8 -*-
"""第二轮应用：全列单元格 + 表头标签 + TOC 显示文本"""
import json, re, glob, os
REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

mapping = {}
for f in sorted(glob.glob('batch_*.zh.json')) + sorted(glob.glob('batch2_*.zh.json')):
    mapping.update(json.load(open(f)))
# 表头与通用标签
mapping.update({
    "Tool": "工具", "Description": "说明", "Install / Link": "安装 / 链接",
    "Type": "类型", "Link": "链接", "Free Tier": "免费档",
    "Link / Onion Address": "链接 / 洋葱地址", "Script": "脚本",
    "What it installs": "安装内容", "Use when": "适用场景",
    "Search Query": "搜索式", "What It Finds": "能查到什么",
    "Resource": "资源", "URL": "网址", "Data Point": "数据点", "How to Find": "怎么查",
    "Free/Paid": "免费/付费", "Free": "免费", "Paid": "付费", "Freemium": "免费增值",
})
print('总映射:', len(mapping))

# 标题映射（去编号/去 emoji），供 TOC 使用
title2zh = {}
for k, v in mapping.items():
    m = re.match(r'^(\d+\.)\s+(.*)$', k)
    if m:
        t_en = re.sub(r'^[^\w\u4e00-\u9fff(]+', '', m.group(2))
        v2 = re.sub(r'^\d+\.\s*', '', v)
        v2 = re.sub(r'^[^\w\u4e00-\u9fff(]+', '', v2)
        title2zh[t_en] = v2

lines = open(REPO + '/README.md').read().split('\n')
cell_hits = toc_hits = sum_hits = 0
for i, line in enumerate(lines):
    # 1) TOC 行：N. [Title](#anchor)
    m = re.match(r'^(\s*\d+\.\s+)\[([^\]]+)\](\(#[^)]*\))\s*$', line)
    if m:
        disp = m.group(2)
        zh = title2zh.get(disp)
        if not zh:
            for t, z in title2zh.items():
                if t.startswith(disp) or disp.startswith(t):
                    zh = z; break
        if zh:
            lines[i] = m.group(1) + '[' + zh + ']' + m.group(3)
            toc_hits += 1
        continue
    # 2) 表格行：任意列
    if re.match(r'^\s*\|', line):
        cells = [c.strip() for c in line.strip().strip('|').split('|')]
        if set(''.join(cells)) <= set('- : '):
            continue
        changed = False
        for j, c in enumerate(cells):
            if c in mapping:
                cells[j] = mapping[c]; changed = True
        if changed:
            indent = re.match(r'^(\s*)', line).group(1)
            lines[i] = indent + '| ' + ' | '.join(cells) + ' |'
            cell_hits += 1
        continue
    # 3) summary 标签整行
    s = line.strip()
    if s.startswith('<summary>') and s in mapping:
        lines[i] = mapping[s]; sum_hits += 1

open(REPO + '/README.md', 'w').write('\n'.join(lines))
print(f'TOC 替换 {toc_hits} 行 | 表格行替换 {cell_hits} | summary 替换 {sum_hits}')
