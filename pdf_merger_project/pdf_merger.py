from PyPDF2 import PdfMerger

n = int(input("Enter how many PDF you want to merge: "))
merger = PdfMerger()
for i in range(0, n):
    file_name = input("Enter your PDF name: ")
    merger.append(file_name)

merged_PDF_name = input("Enter Merged PDF name: ")
merger.write(merged_PDF_name)
merger.close()