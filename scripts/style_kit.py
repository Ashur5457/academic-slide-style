"""House style for academic talks: burgundy title bar, grey and bright-red emphasis, thin bottom line with a large page number.

Works for English and Traditional Chinese decks (Arial + Microsoft JhengHei). Coordinates are on the 1920 x 1080 canvas of slide_kit.
Content area of a page: x 72-1848, y 130-1040.
"""
import logging
import os
import matplotlib
matplotlib.use("Agg")
logging.getLogger("matplotlib.font_manager").setLevel(logging.ERROR)
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from slide_kit import *

WINE, BRIGHT, RED_TEXT = "722F42", "E5495A", "D92B45"
LIGHT, MID, DARK, BAR_GRAY, ARROW = "F2F2F2", "6E6E6E", "5A5A5A", "BDBDBD", "8C8C8C"
TEXT, BIG_NO = "2E1A1A", "E6E6E6"
ICON_FONT = ["Microsoft JhengHei", "Noto Sans CJK TC", "DejaVu Sans"]


def page(prs, title, n):
    """content page; build steps of one concept pass the same n"""
    s = blank_slide(prs)
    chrome(s, title, footer=False)
    rect(s, 0, 1062, 1920, 18, fill=WINE, radius=0)
    text(s, 1740, 985, 120, 72, str(n), size=44, color=MID, bold=True, align="r", anchor="m")
    return s


def outline(prs, items, answer=None, title="Outline", n=1):
    """items: (number, section name, one line); answer: optional sentence in a callout below the rows"""
    s = page(prs, title, n)
    for i, (no, name, sub_) in enumerate(items):
        y = 150 + i * 150
        rect(s, 72, y, 1776, 132, fill=LIGHT)
        text(s, 100, y, 130, 132, no, size=46, bold=True, color=RED_TEXT, anchor="m")
        text(s, 240, y, 640, 132, name, size=32, bold=True, color=WINE, anchor="m")
        text(s, 880, y, 950, 132, sub_, size=27, color=TEXT, anchor="m")
    if answer:
        callout(s, 960, 150 + len(items) * 150 + 10, [answer], size=28, anchor="c")
    return s


def cover(prs, title_lines, subtitle, name, date, icon, alt="", title_size=50):
    s = blank_slide(prs)
    text(s, 110, 300, 1000, 220, title_lines, size=title_size, color=WINE, bold=True, anchor="m")
    rect(s, 110, 545, 120, 8, fill=BRIGHT, radius=0)
    text(s, 110, 585, 1000, 60, subtitle, size=28, color=MID)
    text(s, 110, 740, 1000, 50, name, size=30, color=TEXT)
    text(s, 110, 800, 1000, 46, date, size=22, color=MID)
    picture(s, icon, 1130, 210, 700, 630, alt=alt)
    return s


def section(prs, no, title, sub, icon, alt=""):
    s = blank_slide(prs)
    text(s, 110, 150, 700, 280, no, size=170, color=BIG_NO, bold=True, anchor="m")
    text(s, 110, 450, 1000, 100, title, size=56, color=WINE, bold=True, anchor="m")
    rect(s, 110, 570, 120, 8, fill=BRIGHT, radius=0)
    text(s, 110, 605, 1000, 60, sub, size=30, color=MID)
    picture(s, icon, 1140, 240, 680, 612, alt=alt)
    return s


def icon_canvas():
    """1000 x 900 drawing area for the talk's schematic, transparent background"""
    plt.rcParams["font.family"] = ICON_FONT
    fig = plt.figure(figsize=(5, 4.5), dpi=400)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 1000)
    ax.set_ylim(900, 0)
    ax.axis("off")
    return fig, ax


def rbox(ax, x, y, w, h, r, **k):
    ax.add_patch(FancyBboxPatch((x + r, y + r), w - 2 * r, h - 2 * r, boxstyle=f"round,pad={r},rounding_size={r}", joinstyle="round", **k))


def save_icon(fig, path):
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    fig.savefig(path, transparent=True)
    plt.close(fig)
    return path
