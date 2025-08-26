#change directory
import os
os.chdir(r"C:\Users\pc\Desktop\cluter")

#handle error to create a file
def createifNotExist(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

#move perticular file in specific folder
def move(foldername,files):
    for file in files:
     os.replace(file,f"{foldername}/{file}")

#main content run
if __name__ == "__main__":
    #all files        
    files = os.listdir()
    #create a folder
    createifNotExist("Images")
    createifNotExist("Media")
    createifNotExist("Docs")
    createifNotExist("Others")
    #Seperate image file
    imageExts = ['.png','jpg','.jpng']
    images = [file for file in files if os.path.splitext(file)[1].lower() in imageExts]

    #seperate doc file
    docExts = ['.txt','.doc','.pdf','.docx']
    docs = [file for file in files if os.path.splitext(file)[1].lower() in docExts]

    #seperate media file 
    mediaExt = [".mp4",".mp3",'.flv']
    medias = [file for file in files if os.path.splitext(file)[1].lower() in mediaExt]
    
    #create a folder to collect other files
    others = []
    for file in files:
        ext = os.path.splitext(file)[1].lower()
        if ext not in  mediaExt and  ext not in docExts and ext not in imageExts and os.path.isfile(file):
            others.append(file) 
    #run the move function
    move("Others",others)
    move("Media",medias)
    move("Docs",docs)
    move("Images",images)
