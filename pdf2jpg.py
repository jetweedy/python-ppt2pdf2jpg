import sys
import os
import glob
import win32com.client


def pdfThumbnail(directory, targetdirectory, filename):
	newname = os.path.splitext(filename)[0] + ".jpg"
	print(directory+filename)
	print(targetdirectory+newname)
	if os.path.exists(directory+filename):
		osCommand = 'magick convert -thumbnail 160x120 "'+directory+filename+'"[0] "'+targetdirectory+newname+'"'
		print(osCommand)
		os.system(osCommand)
	else: 
		print("nope")

def convertPPT2PDF(directory, targetdirectory, filename, formatType = 32):
	powerpoint = win32com.client.Dispatch("Powerpoint.Application")
	powerpoint.Visible = True
	newname = os.path.splitext(filename)[0] + ".pdf"
	print(directory+filename)
	print(targetdirectory+newname)
	deck = powerpoint.Presentations.Open(directory+filename)
	deck.SaveAs(targetdirectory+newname, formatType)
	deck.Close()
	powerpoint.Quit()
	return newname
 
def convertDirectoryPPTtoPDF(pptDirectory,pdfDirectory):
	for file in os.listdir(pptDirectory):
		pdfFile = convertPPT2PDF(pptDirectory, pdfDirectory, file)
		
#convertDirectoryPPTtoPDF("C:\\Users\\jetweedy\\Desktop\\SILS\\ppt2pdf2jpg\\ppt\\", "C:\\Users\\jetweedy\\Desktop\\SILS\\ppt2pdf2jpg\\pdf\\")


def convertDirectoryPDFtoJPG(pdfDirectory,jpgDirectory):
	for file in os.listdir(pdfDirectory):
		print(file);
		pdfThumbnail(pdfDirectory, jpgDirectory, file)

### Can't seem to get this to work
convertDirectoryPDFtoJPG("C:\\Users\\jetweedy\\Desktop\\SILS\\ppt2pdf2jpg\\pdf\\","C:\\Users\\jetweedy\\Desktop\\SILS\\ppt2pdf2jpg\\jpg\\")

