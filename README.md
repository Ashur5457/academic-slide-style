# academic-slide-style

An Agent Skill for academic talks, for Claude Code and Codex in English or Traditional Chinese: burgundy title bar, bright-red and grey emphasis, a thin bottom line with a large page number, a cover schematic drawn from the talk's own content, and short cue notes for presenter view.

學術簡報 Agent Skill，Claude Code 和 Codex 都能用，支援英文和繁體中文：酒紅標題列、亮紅與灰階強調、底部細線配大頁碼、依簡報內容設計的封面示意圖，以及適合簡報者畫面的摘要式備忘稿。

| English | 繁體中文 |
|---|---|
| ![English sample](assets/preview_en.png) | ![中文範例](assets/preview_zh.png) |

## Install / 安裝

Both tools read the same `SKILL.md` (the Agent Skills format), so one copy serves both. Requires `python-pptx`, `pillow` and `matplotlib`.

兩個工具讀同一份 `SKILL.md`（Agent Skills 格式），一份就能共用。需要 `python-pptx`、`pillow`、`matplotlib`。

**Claude Code**

```bash
git clone https://github.com/Ashur5457/academic-slide-style.git ~/.claude/skills/academic-slide-style
```

Call it with `/academic-slide-style`, or ask for an academic deck. 用 `/academic-slide-style` 呼叫，或直接要求做學術簡報。

**Codex** (CLI, IDE extension, app)

```bash
git clone https://github.com/Ashur5457/academic-slide-style.git ~/.agents/skills/academic-slide-style
```

Call it with `$academic-slide-style` or pick it from `/skills`. For a single project, clone into `.agents/skills/` in that repo. `agents/openai.yaml` only sets the display name and lets Codex pick the skill on its own.

用 `$academic-slide-style` 呼叫，或從 `/skills` 選。只給單一專案用時，clone 到該 repo 的 `.agents/skills/`。`agents/openai.yaml` 只設定顯示名稱，並允許 Codex 自動選用。

**Both from one copy / 一份給兩邊用**

Keep the clone in `~/.claude/skills` and link it for Codex, which follows symlinked skill folders:

保留 `~/.claude/skills` 那份，再連結給 Codex（Codex 會跟隨連結的 skill 資料夾）：

```bash
mkdir -p ~/.agents/skills
ln -s ~/.claude/skills/academic-slide-style ~/.agents/skills/academic-slide-style
```

On Windows, use a directory junction instead (`mklink /J "%USERPROFILE%\.agents\skills\academic-slide-style" "%USERPROFILE%\.claude\skills\academic-slide-style"` in cmd, after creating `%USERPROFILE%\.agents\skills`). 在 Windows 改用 cmd 的 `mklink /J`（先建立 `%USERPROFILE%\.agents\skills`）。

**Sample decks / 範例**

```bash
python scripts/sample_deck.py en
python scripts/sample_deck.py zh
```

## Credits and licence / 來源與授權

MIT, see [LICENSE](LICENSE). `scripts/slide_kit.py` is adapted from [paper-sharing-skills](https://github.com/Ashur5457/paper-sharing-skills) by whats2000, MIT, see [LICENSE-slide_kit](LICENSE-slide_kit). The layout builds on the workflow of its `paper-discussion-slides` skill.
