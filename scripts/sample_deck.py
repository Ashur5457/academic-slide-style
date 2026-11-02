"""Sample deck of the style: python sample_deck.py en|zh [out.pptx]. Placeholder content only."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from style_kit import *
from matplotlib.patches import Circle

lang = sys.argv[1] if len(sys.argv) > 1 else "en"
out = sys.argv[2] if len(sys.argv) > 2 else f"sample_{lang}.pptx"
T = {
    "en": dict(title=["Title of the talk", "in at most two lines"], sub="Subtitle or meeting name", name="Your Name", date="2026-01-01 | Affiliation",
               sec="Section title", sec_sub="One line on this part", page="The title states the conclusion", a="Input", b="Output",
               items=["Keywords and numbers on the slide", "Cues for the speaker go in the notes"], call=["The one point", "to remember"], script="Cues: keywords | key numbers\nHow: order, analogy, what to point at"),
    "zh": dict(title=["簡報標題放在這裡", "最多兩行"], sub="副標題或會議名稱", name="報告人", date="2026-01-01｜單位",
               sec="章節名稱", sec_sub="一句話說明這一部分", page="標題寫成一句結論", a="輸入", b="輸出",
               items=["投影片只放關鍵字和數字", "提示和講法寫在備忘稿"], call=["這一頁", "要記住的重點"], script="提示：關鍵字｜關鍵數字\n講法：講解順序、比喻、要指哪裡"),
}[lang]


def icon(path):
    """example only: every real talk gets its own schematic, drawn from its content"""
    fig, ax = icon_canvas()
    ink, acc = "#" + WINE, "#" + BRIGHT
    rbox(ax, 90, 320, 280, 260, 28, fc="white", ec=ink, lw=4.5)
    rbox(ax, 120, 450, 220, 100, 10, fc=acc, ec="none")
    rbox(ax, 630, 320, 280, 260, 28, fc="white", ec=ink, lw=4.5)
    ax.add_patch(Circle((770, 450), 70, fc=acc, ec="none"))
    ax.plot([400, 590], [450, 450], color=ink, lw=4.5, solid_capstyle="round")
    ax.plot([560, 594, 560], [425, 450, 475], color=ink, lw=4.5, solid_capstyle="round", solid_joinstyle="round")
    ax.text(230, 650, T["a"], fontsize=20, color="#" + TEXT, ha="center", va="center", fontweight="bold")
    ax.text(770, 650, T["b"], fontsize=20, color="#" + TEXT, ha="center", va="center", fontweight="bold")
    return save_icon(fig, path)


prs = new_deck()
ic = icon(os.path.splitext(os.path.abspath(out))[0] + "_icon.png")
notes(cover(prs, T["title"], T["sub"], T["name"], T["date"], ic), T["script"])
notes(outline(prs, [("01", T["sec"], T["sec_sub"]), ("02", T["sec"], T["sec_sub"])], answer=T["call"][0]), T["script"])
notes(section(prs, "01", T["sec"], T["sec_sub"], ic), T["script"])
s = page(prs, T["page"], 2)
block(s, 72, 150, 860, 470, T["a"], T["items"], size=30)
callout(s, 1380, 280, T["call"], anchor="c")
frame(s, 1150, 520, 460, 120)
block_arrow(s, 1352, 454, 56, 62, "down")
notes(s, T["script"])
prs.save(out)
print(out)
