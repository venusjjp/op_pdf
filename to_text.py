import fitz

def pdf_to_txt(pdf_path, txt_path):
    doc = fitz.open(pdf_path)
    with open(txt_path, "w", encoding="utf-8") as f:
        for i, page in enumerate(doc, start=1):
            text = page.get_text("text")
            f.write(f"\n===== 第 {i} 页 =====\n")
            f.write(text)
            f.write("\n")
    doc.close()
    print(f"完成：{txt_path}")


if __name__ == "__main__":
    pdf_to_txt("output.pdf", "output.txt")