import read_pdf
import load_pdfs

if __name__ == '__main__':
    foldername, filenames = load_pdfs.getFileNames()
    try:
    	print(read_pdf.extract_text_from_pdf(foldername+'/'+filenames[0]))
    except:
    	print("No papers in /papers yet")