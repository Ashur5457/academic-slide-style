---
name: academic-slide-style
description: House style for academic talks in English or Traditional Chinese (學術簡報風格): burgundy title bar, grey and bright-red emphasis, thin bottom line with a large page number, and a cover schematic drawn from the talk's own content. Use whenever making or restyling an academic, research, lab meeting or conference slide deck, 學術簡報, 研究報告簡報 or 論文分享簡報, unless the user names another template.
---

# Academic slide style / 學術簡報風格

Decks may be in English or Traditional Chinese; write in the language the user asks for. Both use the same layout. Fonts: Arial for Latin, Microsoft JhengHei for CJK.

簡報可用英文或繁體中文，依使用者指定的語言撰寫，版面相同。字型：英數 Arial，中文微軟正黑體。

If the `paper-discussion-slides` skill is available, follow its workflow (define the problem, budget by key points, progressive builds). This skill replaces its template and its full spoken script.

## Speaker notes / 備忘稿

Every slide gets short cue notes, not a full script, because the notes area in presenter view is small. Two lines, each about 60 characters at most:

```
Cues: keywords | key numbers | term to explain
How: the order to walk through, analogy or question, what to point at
```

每張投影片都附摘要式備忘稿，不寫完整講稿，因為簡報者畫面的備忘稿空間有限。兩行為主，每行約 60 字內：

```
提示：關鍵字｜關鍵數字｜要解釋的名詞
講法：講解順序、比喻或提問、要指哪裡
```

Estimate time from key points (about 1 to 1.5 minutes per page), not from note length. Exact numbers the speaker may need belong in the cues.

## Palette / 配色

| Use 用途 | Colour 色碼 |
|---|---|
| Title bar, bottom line, main series, cover and section titles 標題列、底線、主要資料、封面與轉場標題 | Burgundy 酒紅 `#722F42` |
| Short rule, filled parts of the icon 短色條、圖示填色 | Bright red 亮紅 `#E5495A` |
| Emphasis text, compared series 強調文字、比較資料 | Deeper red 深亮紅 `#D92B45` |
| Pale panels, callout fill 淺底、提示框底 | Light grey 淺灰 `#F2F2F2` |
| Callout and highlight frames 提示框與標示框 | Dark grey 深灰 `#5A5A5A` |
| Arrows 箭頭 | Grey 中灰 `#8C8C8C` |
| Control series 對照資料 | Grey 淺灰 `#BDBDBD` |
| Secondary text, page number 次要文字、頁碼 | Grey 中灰 `#6E6E6E` |
| Body text 內文 | Dark brown-black 深褐黑 `#2E1A1A` |

Do not add a third hue such as blue, gold or purple. Vary the reds and greys instead. Figures taken from a paper keep their own colours; figures drawn for the talk use this palette.

不要加入藍、金、紫等第三色相，用紅色和灰色的深淺變化。論文原圖保留原色，自己畫的圖用這組配色。

## Layout / 版面

- **Content page:** full-width burgundy bar at the top with a white bold title, written as a conclusion. Content in the white area. A thin burgundy line runs along the bottom, with a large bold grey page number above its right end.
- **No footer text:** no deck title, credit or take-away band. Sources sit next to the figure they belong to, and the presenter is on the cover.
- **Pale panels:** text that needs to stand out sits on light grey, above or below the figures.
- **Emphasis:** light grey box, bright-red bold text, dark grey frame, connected by a grey arrow to what it explains.
- **Cover:** white. Title in burgundy, short red rule, subtitle, presenter and date on the left; the talk's schematic on the right.
- **Section page:** white. Large pale number, burgundy title, short red rule, one line of text; the same schematic on the right.

## Cover schematic / 封面示意圖

Read the whole talk first, then draw one schematic that tells its central story or question. Do not use a generic icon or a stock motif.

先讀完整份簡報，再畫一張表達核心故事或問題的示意圖，不要用通用圖示。

- Show the argument as two to four objects with arrows, for example what was trained, what it is asked about, and the open question.
- Line art in burgundy, consistent stroke, rounded corners, red fill on only the parts that matter. At most a few short labels.
- Reuse the same schematic on section pages.

## Building / 製作

Add `scripts/` to `sys.path`, then:

```python
from style_kit import *

prs = new_deck()
fig, ax = icon_canvas()            # 1000 x 900, transparent; draw the schematic here
icon = save_icon(fig, "icon.png")
cover(prs, ["Title line 1", "Title line 2"], "Subtitle", "Presenter", "Date", icon, alt="what the schematic shows")
section(prs, "01", "Section title", "One line", icon)
s = page(prs, "The title states the conclusion", 1)   # content area: x 72-1848, y 130-1040
notes(s, "Cues: ...\nHow: ...")
prs.save("deck.pptx")
```

`slide_kit.py` provides `text`, `rect`, `callout`, `frame`, `block`, `bullets`, `block_arrow`, `arc_arrow`, `dim_area`, `hide`, `hbars`, `picture`, `sub` and `notes`, already set to this palette. `python scripts/sample_deck.py en` or `zh` writes a sample.

Render every slide and look at it before handing over. Keep titles to one line: about 33 CJK characters at the default size.

## Check / 檢查

- [ ] Cover schematic comes from this talk's content
- [ ] Only burgundy, red and grey in anything drawn for the talk
- [ ] No text in the footer apart from the page number
- [ ] Callouts are light grey, red text, dark grey frame, with an arrow
- [ ] Every slide has short cue notes (cues and how to say it), not a full script
- [ ] Titles are conclusions and fit on one line
- [ ] In Chinese decks every term has its proper name and a plain explanation on first use
