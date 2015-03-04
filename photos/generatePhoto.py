
import os
from PIL import Image

def ecriturePhoto(folderName, output):

	fileOut = open(output, 'w')
	print folderName
	for photo in os.listdir(folderName):
		print folderName+photo
		img = Image.open(folderName+photo)
		fileOut.write("<figure id=\"blue\" class=\"photo\" style=\"display:none\" itemprop=\"associatedMedia\"itemscope itemtype=\"http://schema.org/ImageObject\">\n<a href=\"")
		fileOut.write(folderName+photo)
		fileOut.write("\" itemprop=\"contentUrl\" data-size=\"")
		fileOut.write(str(img.size[0]))
		fileOut.write("x")
		fileOut.write(str(img.size[1]))
		fileOut.write("\">\n <img src=\"")
		fileOut.write(folderName+photo)
		fileOut.write("\"itemprop=\"thumbnail\" alt=\"Image description\"  />\n</a>\n<figcaption></figcaption>\n</figure>\n\n")
		print img.size

	fileOut.close()

ecriturePhoto("../images/CourseCarnaval/", "./Oka.txt")
