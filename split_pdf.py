import pymupdf  # PyMuPDF

doc = pymupdf.open("1.pdf")
out = pymupdf.open()

for page in doc:
    rect = page.rect
    mid = rect.width / 2
    left = pymupdf.Rect(rect.x0, rect.y0, mid, rect.y1)
    right = pymupdf.Rect(mid, rect.y0, rect.x1, rect.y1)
    for clip in (left, right):
        new_page = out.new_page(width=clip.width, height=clip.height)
        new_page.show_pdf_page(new_page.rect, doc, page.number, clip=clip)

out.save("output.pdf")


