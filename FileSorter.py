import os
import shutil

#FUNCTIONS
def createdir(newDir):
    if not os.path.isdir(newDir):
        os.makedirs(newDir)
    return newDir;
def removeEmpty(directories):
    for dir in directories:
        if (len(os.listdir(dir)) == 0):
            shutil.rmtree(dir)
    return;

#MAIN
print("Sorting Files...")
currentDir = os.getcwd()
videoDir = createdir(currentDir + "/Videos")
pictureDir = createdir(currentDir + "/Pictures")
audioDir = createdir(currentDir + "/Audio")
programDir = createdir(currentDir + "/Programs")
documentDir = createdir(currentDir + "/Documents")
archiveDir = createdir(currentDir + "/Archived")
torrentDir = createdir(currentDir + "/Torrents")
codeDir = createdir(currentDir + "/Code")
directories = [videoDir, pictureDir, audioDir, programDir, documentDir, archiveDir, torrentDir, codeDir]
files = os.listdir(currentDir) #Get files in current folder
for file in files: #Sort files in specific folders
    if(file.lower().endswith(".png") or file.lower().endswith(".jpg") or file.lower().endswith(".gif")or file.lower().endswith(".jpeg")):     #PICTURES
        shutil.move(currentDir + "/" + file, pictureDir + "/" + file)
    elif (file.lower().endswith(".exe") or file.lower().endswith(".jar")):                                 #PROGRAMS
        shutil.move(currentDir + "/" + file, programDir + "/" + file)
    elif (file.lower().endswith(".mp3")  or file.lower().endswith(".waw")):                                    #AUDIO
        shutil.move(currentDir + "/" + file, audioDir + "/" + file)
    elif (file.lower().endswith(".pdf") or file.lower().endswith(".txt")  or file.lower().endswith(".html")
        or file.lower().endswith(".docx") or file.lower().endswith(".odt") or file.lower().endswith(".doc")or file.lower().endswith(".xlsx")or file.lower().endswith(".odp") or file.lower().endswith(".pptx") or file.lower().endswith(".csv")):    #DOCUMENTS
        shutil.move(currentDir + "/" + file, documentDir + "/" + file)
    elif (file.lower().endswith(".mp4") or file.lower().endswith(".wmw") or file.lower().endswith(".avi")
          or file.lower().endswith(".mkv")):          # Video
        shutil.move(currentDir + "/" + file, videoDir + "/" + file)
    elif (file.lower().endswith(".zip") or file.lower().endswith(".rar")
        or file.lower().endswith(".gz") or file.lower().endswith(".iso") or file.lower().endswith(".7z")):    # ARCHIVE
        shutil.move(currentDir + "/" + file, archiveDir + "/" + file)
    elif (file.lower().endswith(".torrent")):                                                               # torrents
        shutil.move(currentDir + "/" + file, torrentDir + "/" + file)
    elif (file.lower().endswith(".py") or file.lower().endswith(".java")):                          # CODE
        if(file != os.path.basename(__file__)):
            shutil.move(currentDir + "/" + file, codeDir + "/" + file)
removeEmpty(directories) #Removes unused folders
print("Sorting Complete")
