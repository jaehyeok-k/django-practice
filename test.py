import pdfplumber


pdf = pdfplumber.open("아뱅.pdf")

pnum = len(pdf.pages)

for i in range(pnum):
    p = pdf.pages[i]
    print(p.extract_text())