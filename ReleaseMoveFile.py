#Moving Different Type of Files Present in Input Folder Directory to Corresponding File Type Folder 
import shutil
import os,sys
import logging

logging.basicConfig(level=logging.DEBUG)


inputDir = "."


docList = []
imageList =[]
tempList=[]
dirF =""
item =0

def MoveFileUtil(File,fileType):
	os.makedirs(fileType,exist_ok=True)
	cur = os.path.dirname(os.path.abspath(File))
	dirF = cur+"\\"+fileType
	logging.info("Directory Name To Move File z::::----"+dirF)
	try:
		shutil.move(File,dirF)
	except:
		global item
		item +=1
		logging.info(str(item)+"Something went wrong for File "+File)


def MoveFile(File,fileType):
	if fileType == ".txt" or fileType == ".pdf" or fileType == ".doc" or fileType==".docx":
		fileType = fileType.replace(".","")
		fileType = fileType.upper()
		docList.append(File)
		MoveFileUtil(File,fileType)

	elif fileType == ".png" or fileType ==".jpeg" or fileType ==".jpg":
		imageList.append(File)
		MoveFileUtil(File,"IMAGE")

	elif fileType == ".py~" or fileType==".swp" or fileType==".py.swp" or fileType==".py.swo":
		tempList.append(File)
		MoveFileUtil(File,"TEMP")

	else:
		#PY Files
		cur = os.path.dirname(os.path.abspath(File))
		dirF = cur


def Start(inpDir):
	for index in os.listdir(inpDir):
		logging.info("IN Start with File ::"+index)
		fl,ext= os.path.splitext(index)
		MoveFile(index,ext)

	print("The Number of Image Files Moved ::"+str(len(imageList)))
	print("The Number of Doc Files Moved ::"+str(len(docList)))
	print("The Number of Temp Files Moved ::"+str(len(tempList)))

if __name__=="__main__":
	Start(inputDir)
