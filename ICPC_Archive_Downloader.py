import requests, PyPDF2, os

startID = input('Enter first problem ID to download: ')
endID = input('Enter last problem ID to download: ')

n = int(startID)
m = int(endID)

pdfFiles = []
for i in range(n,m+1):
    url = 'https://icpcarchive.ecs.baylor.edu/external/' + str(i)[:2] + '/' + str(i)+ '.pdf'
    res = requests.get(url)
    try:
        res.raise_for_status()
        newfilename = str(i) + '_temp.pdf'
        pdfFiles.append(newfilename)
        print('Problem ' + str(i) + ' has been downloaded')
        out = open(newfilename, 'wb')
        for c in res.iter_content(100000):
            out.write(c)
        out.close()
    except Exception as exc:
        print('There was a problem downloading problem %s : %s' %(str(i), exc))

if len(pdfFiles) > 0:
    pdfWriter = PyPDF2.PdfFileWriter()

    pdfFiles.sort(key=str.lower)
        
    for filename in pdfFiles:        
        pdfFileObj = open(filename, 'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        # print ('Adding ' + filename)

        for pageNum in range(pdfReader.numPages):
            pageObj = pdfReader.getPage(pageNum)
            pdfWriter.addPage(pageObj)
        


    outname = input('Input combined pdf filename: ')
    outname = outname + '.pdf'
    pdfOutputFile = open(outname, 'wb')
    pdfWriter.write(pdfOutputFile)
    pdfOutputFile.close()

    pdfFileObj.close()

    for filename in pdfFiles:
        os.unlink(filename)
    print("pdf file creation complete!")
else:
    print("No files were downloaded")
