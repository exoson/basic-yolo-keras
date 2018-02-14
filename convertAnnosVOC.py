from pgmagick import Image
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
    #if folder == "00":
    #    if splitted[5] not in names:
    #        names+=[splitted[5]]

    if folder != "00":
        continue
    try:
        img = Image("images/" + fname + "jpeg")#continue
        #img.write('images/' + fname + "jpeg")
    except Exception:
        import pdb; pdb.set_trace()
        continue

    with open("annotations/" + fname + "xml", 'w') as f:
        f.write("<annotation verified=\"yes\">\n" +
                "\t<folder>images</folder>\n" +
                "\t<filename>" + fname + "jpeg</filename>\n" +
                "\t<path>./images/" + fname + "</path>\n" +
                "\t<source><database>BTSD</database></source>\n" +
                "\t<size>\n" +
                "\t\t<width>" + str(img.columns()) + "</width>\n" +
                "\t\t<height>" + str(img.rows()) + "</height>\n" +
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
