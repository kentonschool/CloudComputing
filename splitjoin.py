import os
import math
import tkinter.filedialog

def splitter(filename,num_accounts):
    try:
        with open(filename,'rb') as f:
            dat = f.read()
            f.close()
            l = len(dat)
    except:
        print('file not found')
        return -1
    
    #identify the extention for later
    originalfilename = filename
    
    dot = filename.rfind(".")
    ext = filename[dot:]
    filename=filename[:dot]

    #split the files
    splitfileslist = []
    
    lastSlash = filename.rfind('/')
    filename = filename[lastSlash+1:]
    for i in range(num_accounts):
        start = math.ceil((l/num_accounts)*i)
        end = math.ceil((l/num_accounts)*(i+1))
        f = dat[start:end]
        #save split file
        with open(filename+str(i)+ext,'wb') as splitfile:
            splitfile.write(f)
            splitfileslist.append(splitfile.name)
            splitfile.close()
            
            
    #remove original file
    os.remove(originalfilename)

    return splitfileslist

def joiner(filename):
    re = bytes()
    
    dot = filename.rfind(".")
    ext = filename[dot:]
    filename=filename[:dot]

    flist = os.listdir()
    num_accounts = 0

    for file in flist:
        if filename == file.replace(ext,'')[:-1]:
            num_accounts += 1
            
    for i in range(num_accounts):
        with open(filename+str(i)+ext,'rb') as infile:
            re += infile.read()
            infile.close()
            #remove the file when we're done
            os.remove(filename+str(i)+ext)

    #write the full binary data to the output file
    file = tkinter.filedialog.asksaveasfile(mode='wb',initialdir="/",initialfile=filename+ext,defaultextension=ext)   
    if file:
        file.write(re)
        file.close()

##    with open(filename+ext,'wb') as outfile:
##        outfile.write(re)
##        outfile.close()
