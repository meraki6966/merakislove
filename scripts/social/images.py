"""Images for scheduled social posts. Run from the repo root.

  python3 scripts/social/images.py flyer public/demos/starter-sites/flyers/tessel.jpg public/social/2026-10-12/tessel-4x5.jpg
      A portrait flyer on a 1080x1350 canvas (4:5, the tallest shape Instagram takes),
      whole flyer kept, blurred strips of itself at the sides.

  python3 scripts/social/images.py shot https://merakislove.com/demos/tessel/cleanings-exams.html "#price-h" public/social/2026-10-12/tessel-prices.jpg --size 1080x1350
      A screenshot of a live page with the element scrolled near the top.
      Sizes: 1080x1350 for Instagram, 1600x900 for Facebook. Use "top" for the top of the page.
      A demo's home page is /demos/<name>. Its inner pages need the .html ending.

      Add --zoom 1.0 for larger text (the page is laid out at the picture's own width), and --offset N to
      change how far below the top of the picture the element sits (170 unless told otherwise).
      Add --date 2026-10-16T17:10:00Z when the page counts down from today (Tallybrook's deadlines,
      an open or closed sign), so the picture shows what the page will say when the post publishes.

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

CLOCK = """(()=>{const R=Date,off=new R('%s').getTime()-R.now();class D extends R{constructor(...a){if(a.length===0)super(R.now()+off);else super(...a)}static now(){return R.now()+off}}window.Date=D})()"""

def shot(url, selector, out, size, when=None, zoom=1.25, offset=170):
    from playwright.sync_api import sync_playwright
    w, h = (int(x) for x in size.split("x"))
    # The page is laid out wider than the picture (zoom, 1.25 unless told otherwise) so it reads as a desktop page, then scaled down.
    with sync_playwright() as p:
        b = p.chromium.launch(args=["--hide-scrollbars"])
        ctx = b.new_context(viewport={"width": int(w * zoom), "height": int(h * zoom)}, device_scale_factor=1 / zoom, bypass_csp=True)
        pg = ctx.new_page()
        # A page that counts down from today is pictured as it will read on the day the post publishes.
        if when: pg.add_init_script(CLOCK % when)
        errs = []; lost = []
        from urllib.parse import urlparse
        host = urlparse(url).netloc
        # A stylesheet that fails to load leaves a full page of unstyled text, which the flat color check cannot see.
        def missing(kind, u):
            if kind == "stylesheet" or (kind in ("script", "font", "image") and urlparse(u).netloc == host): lost.append(f"{kind} {u}")
        pg.on("pageerror", lambda e: errs.append(str(e)))
        pg.on("requestfailed", lambda r: missing(r.resource_type, r.url))
        pg.on("response", lambda r: missing(r.request.resource_type, r.url) if r.status >= 400 else None)
        for attempt in range(5):
            del errs[:]; del lost[:]
            try:
                resp = pg.goto(url, wait_until="networkidle", timeout=45000)
                # A script chunk that fails to load leaves the page body empty under a working header.
                broken = any("Failed to load chunk" in e for e in errs) or bool(lost)
                if resp is not None and resp.status == 200 and not broken: break
                if attempt == 4: sys.exit(f"{url} answered {resp.status if resp else 'nothing'}{', and parts of the page failed to load: ' + '; '.join((lost or errs)[:3]) if broken else ''}. No image written.")
            except Exception as e:
                if attempt == 4: raise
            pg.wait_for_timeout(3000)
        pg.add_style_tag(content="html{scroll-behavior:auto!important} [data-chat-launch],.mobile-bar,.float-call,.cursor-el{display:none!important}")
        if selector != "top":
            if pg.locator(selector).count() == 0: sys.exit(f"{selector} is not on {url}")
            pg.evaluate("([s,o])=>{const e=document.querySelector(s);window.scrollTo(0,e.getBoundingClientRect().top+window.scrollY-o)}", [selector, offset])
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
    elif len(a) >= 4 and a[0] == "shot":
        opt = dict(zip(a[4::2], a[5::2]))
        shot(a[1], a[2], a[3], opt.get("--size", "1080x1350"), opt.get("--date"), float(opt.get("--zoom", 1.25)), int(opt.get("--offset", 170)))
    else: sys.exit(__doc__)
