#import os
#import shutil
#
#
#src = '/Users/sasidharreddy/Desktop/train_data/labels/train'
#
#dst = '/Users/sasidharreddy/Desktop/train_data/labels/val'
#
#l = sorted(os.listdir(src))
#print(l[0])
#for i,v in enumerate(l):
#    if(i%5==0):
#        shutil.move(src+'/'+v, dst+'/'+v)
import os
group = os.listdir( '/Users/sasidharreddy/Desktop/train_data/labels/train')
os.chdir('/Users/sasidharreddy/Desktop/train_data/labels/train')
import xml.dom.minidom
for item in group:
    try:
        doc = xml.dom.minidom.parse(item)
        f = open(item.replace('.xml','.txt'),"w")
        def YOLOformula(xmin,ymin,xmax,ymax):
            xcenter = (xmin+xmax)/(2*512)
            ycenter = (ymin+ymax)/(2*512)
            height = (ymax-ymin)/512
            width = (xmax-xmin)/512
            return [0,xcenter,ycenter,width,height]
        
        bbox = doc.getElementsByTagName('bbox')
        
        for i,ele in enumerate(bbox):
            typ = ele.getElementsByTagName('xmin')[0]
            a = int(typ.childNodes[0].data)
            typ = ele.getElementsByTagName('ymin')[0]
            b = int(typ.childNodes[0].data)
            typ = ele.getElementsByTagName('xmax')[0]
            c = int(typ.childNodes[0].data)
            typ = ele.getElementsByTagName('ymax')[0]
            d = int(typ.childNodes[0].data)
            l= YOLOformula(a,b,c,d)
            joint_l = " ".join(map(str,l))
            f.write(joint_l)
            if(i!= len(bbox)):
                f.write('\n')
        f.close()
    except:
         print(item)
        
   