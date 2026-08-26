# 翻译进度（中断恢复用）

- [x] 原始文件下载 /tmp/osint-arsenal + 备份到 tools/translation/*.orig
- [x] 仓库骨架 + LICENSE + NOTICE + logo
- [x] extract.py 提取唯一字符串 → strings.json（README 表格描述 + tools.json description + 脚本注释/echo）
- [ ] 分批翻译：batch_01.json ... batch_NN.json（每批约 150 条，格式 {"en": "zh"}）
- [ ] apply.py 应用映射 → 生成中文版 README.md / tools.json / *.sh（命令与链接不动）
- [ ] 散文部分人工翻译（标题、徽章、安装指南、免责声明、TOC）
- [ ] 校验：JSON 可解析、表格行列数一致、链接数量一致、bash -n 全部通过
- [ ] 提交推送 GitHub（bayshier/awesome-osint-arsenal-zh）
