"""Images for scheduled social posts. Run from the repo root.

  python3 scripts/social/images.py flyer public/demos/starter-sites/flyers/tessel.jpg public/social/2026-10-12/tessel-4x5.jpg
      A portrait flyer on a 1080x1350 canvas (4:5, the tallest shape Instagram takes),
      whole flyer kept, blurred strips of itself at the sides.

  python3 scripts/social/images.py shot https://merakislove.com/demos/tessel/cleanings-exams.html "#price-h" public/social/2026-10-12/tessel-prices.jpg --size 1080x1350
      A screenshot of a live page with the element scrolled near the top.
      Sizes: 1080x1350 for Instagram, 1600x900 for Facebook. Use "top" for the top of the page.
      A demo's home page is /demos/<name>. Its inner pages need the .html ending.

Both write a JPEG and print its size. Neither draws any text of its own.
"""
import sys
from PIL import Image, ImageFilter

def flyer(src, out):
    """Any portrait flyer, kept whole on a 1080x1350 canvas over a blurred copy of itself."""
    im = Image.open(src).convert("RGB")
    w, h = im.size
    if w >= h: sys.exit(f"{src} is {w}x{h}. This is for portrait flyers.")
    k = min(1080 / w, 1350 / h); fw, fh = round(w * k), round(h * k)
    c = max(1080 / w, 1350 / h); cw, ch = round(w * c), round(h * c)
    bg = im.resize((cw, ch)).crop(((cw - 1080) // 2, (ch - 1350) // 2, (cw - 1080) // 2 + 1080, (ch - 1350) // 2 + 1350)).filter(ImageFilter.GaussianBlur(28))
    bg.paste(im.resize((fw, fh), Image.LANCZOS), ((1080 - fw) // 2, (1350 - fh) // 2))
    bg.save(out, quality=88, optimize=True)
    print(out, bg.size)

def busy(im):
    """Share of the picture that is not the single most common color. An empty page scores near zero."""
    small = im.convert("L").resize((270, round(270 * im.height / im.width)))
    hist = small.histogram()
    mode = hist.index(max(hist))
    near = sum(hist[max(0, mode - 6):mode + 7])
    return 1 - near / (small.width * small.height)

def shot(url, selector, out, size):
    from playwright.sync_api import sync_playwright
    w, h = (int(x) for x in size.split("x"))
    # The page is laid out 1.25 times wider than the picture so it reads as a desktop page, then scaled down.
    with sync_playwright() as p:
        b = p.chromium.launch(args=["--hide-scrollbars"])
        ctx = b.new_context(viewport={"width": int(w * 1.25), "height": int(h * 1.25)}, device_scale_factor=0.8, bypass_csp=True)
        pg = ctx.new_page()
        errs = []
        pg.on("pageerror", lambda e: errs.append(str(e)))
        for attempt in range(5):
            del errs[:]
            try:
                resp = pg.goto(url, wait_until="networkidle", timeout=45000)
                # A script chunk that fails to load leaves the page body empty under a working header.
                broken = any("Failed to load chunk" in e for e in errs)
                if resp is not None and resp.status == 200 and not broken: break
                if attempt == 4: sys.exit(f"{url} answered {resp.status if resp else 'nothing'}{', scripts failed to load' if broken else ''}. No image written.")
            except Exception as e:
                if attempt == 4: raise
            pg.wait_for_timeout(3000)
        pg.add_style_tag(content="html{scroll-behavior:auto!important} [data-chat-launch],.mobile-bar,.float-call,.cursor-el{display:none!important}")
        if selector != "top":
            if pg.locator(selector).count() == 0: sys.exit(f"{selector} is not on {url}")
            pg.evaluate("(s)=>{const e=document.querySelector(s);window.scrollTo(0,e.getBoundingClientRect().top+window.scrollY-170)}", selector)
        pg.wait_for_timeout(1500)
        pg.screenshot(path=out + ".png")
        b.close()
    import os
    im = Image.open(out + ".png").convert("RGB").resize((w, h), Image.LANCZOS)
    os.remove(out + ".png")
    filled = busy(im)
    if filled < 0.04: sys.exit(f"The picture of {url} is {filled:.1%} content and the rest is one flat color. The page did not render. No image written.")
    im.save(out, quality=88, optimize=True)
    print(out, im.size)

if __name__ == "__main__":
    a = sys.argv[1:]
    if len(a) == 3 and a[0] == "flyer": flyer(a[1], a[2])
    elif len(a) >= 4 and a[0] == "shot": shot(a[1], a[2], a[3], a[5] if len(a) > 5 and a[4] == "--size" else "1080x1350")
    else: sys.exit(__doc__)
