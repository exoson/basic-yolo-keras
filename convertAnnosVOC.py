import os.path
from PIL import Image
import cv2


def draw_boxes(img, coords):
    img = cv2.rectangle(img,
                        (int(float(coords[0])),
                         int(float(coords[1]))),
                        (int(float(coords[2])),
                         int(float(coords[3]))), (0, 255, 0), 3)
    return img


file_name = "BelgiumTSD_annotations/BTSD_training_GT.txt"

annos = open(file_name, 'r')

content = annos.readlines()


names=[]
for line in content:
    splitted = line.split(';')
    splitted_name = splitted[0].split('/')
    folder = splitted_name[0]
    coords = splitted[1:5]
    fname = splitted_name[1][:-3]

    img = Image.open("images/" + fname + "jpg")#continue
    full_name = "annotations/" + fname + "xml"

    if os.path.isfile(full_name):
        with open(full_name, 'r') as f:
            content = f.readlines()
        content.insert(-1,
                       "\t<object>\n" +
                       "\t\t<name>" + splitted[5] + "</name>\n" +
                       "\t\t<pose>Unspecified</pose>\n" +
                       "\t\t<truncated>0</truncated>\n" +
                       "\t\t<difficult>0</difficult>\n" +
                       "\t\t<bndbox>\n" +
                       "\t\t\t<xmin>" + coords[0] + "</xmin>\n" +
                       "\t\t\t<ymin>" + coords[1] + "</ymin>\n" +
                       "\t\t\t<xmax>" + coords[2] + "</xmax>\n" +
                       "\t\t\t<ymax>" + coords[3] + "</ymax>\n" +
                       "\t\t</bndbox>\n" +
                       "\t</object>\n")
        with open(full_name, 'w') as f:
            f.write("".join(content))
    else:
        with open(full_name, 'w') as f:
            f.write("<annotation verified=\"yes\">\n" +
                    "\t<folder>images</folder>\n" +
                    "\t<filename>" + fname + "jpg</filename>\n" +
                    "\t<path>./images/" + fname + "</path>\n" +
                    "\t<source><database>BTSD</database></source>\n" +
                    "\t<size>\n" +
                    "\t\t<width>" + str(img.size[0]) + "</width>\n" +
                    "\t\t<height>" + str(img.size[1]) + "</height>\n" +
                    "\t\t<depth>" + str(3) + "</depth>\n" +
                    "\t</size>\n" +
                    "\t<segmented>0</segmented>\n" +
                    "\t<object>\n" +
                    "\t\t<name>" + splitted[5] + "</name>\n" +
                    "\t\t<pose>Unspecified</pose>\n" +
                    "\t\t<truncated>0</truncated>\n" +
                    "\t\t<difficult>0</difficult>\n" +
                    "\t\t<bndbox>\n" +
                    "\t\t\t<xmin>" + coords[0] + "</xmin>\n" +
                    "\t\t\t<ymin>" + coords[1] + "</ymin>\n" +
                    "\t\t\t<xmax>" + coords[2] + "</xmax>\n" +
                    "\t\t\t<ymax>" + coords[3] + "</ymax>\n" +
                    "\t\t</bndbox>\n" +
                    "\t</object>\n" +
                    "</annotation>")
print names
