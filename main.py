import read_pdf
import load_pdfs

if __name__ == '__main__':
    foldername, filenames = load_pdfs.getFileNames()
    print(read_pdf.extract_text_from_pdf(foldername+'/'+filenames[0]))