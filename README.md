# YOLO_v5
1. The custom dataset folder must have two sub-folders 1)images 2)labels

2. Within each sub-folder two sub-folder 1) train 2) val containing training and validation images in images folder and .txt yolo format defect boundaries and classes have to be specified

# Generating YOLO compatible .txt files for labels
3. .txt files should have the class- 0,1,..which class it belongs to, 0-for binary segmentation followed by x-center y-center height width with a space in between adjacent values.
4. if .xml files for the labels are available, parse_xml_to_txt.py can be used to generate the yolo compatible .txt files 


# custom_data.yaml
download the custom_data.yaml from the repo and edit the path to the train, validation and test(optional) datasets.
edit the number of classes present in the dataset to segmentd and name the classes in names list.
upload this custom_data.yaml in the data sub-folder in YOLO folder.


#dataset used in the notebook
http://bit.ly/zjuleaper
this repo explains how to train Yolo_v5 on custom dataset 

