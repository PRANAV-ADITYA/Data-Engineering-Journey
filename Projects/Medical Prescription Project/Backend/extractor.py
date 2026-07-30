from pdf2image import convert_from_path
import pytesseract as pc
import numpy as np
import cv2
from PIL import Image
from abc import ABC,abstractmethod
import re




def preprocess_image(img):
    gray=cv2.cvtColor(np.array(img),cv2.COLOR_BGR2GRAY)
    Image.fromarray(gray).show()
    resized = cv2.resize(gray,None,fx=1.5,fy=1.5,interpolation=cv2.INTER_LINEAR)
    processed_image = cv2.adaptiveThreshold(resized,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,61,11)
    return processed_image



def extract(file_path,file_format):
    pages = convert_from_path(file_path)
    document_text = ''

    for page in pages:
        processed_image = preprocess_image(page)
        text = pc.image_to_string(processed_image,lang='eng')
        document_text += '\n'+text
    return document_text


    if file_format=='prescription':
        pass
    elif file_format == 'patient_details':
        pass



class MedicalDocParser(ABC):
    def __init__(self,text):
        self.text = text

    @abstractmethod   
    def parse(self):
        pass

class PrescriptionParser(MedicalDocParser):
    def __init__(self,text):
        MedicalDocParser.__init__(self,text)

    def parse(self):
        return {'patient_name':self.get_field('patient_name'),
                'address':self.get_field('address'),
                'medicines':self.get_field('medicines'),
                'directions':self.get_field('directions'),
                'refill':self.get_field('refill')
                }

    def get_field(self,field_name):
        pattern_dict={
            'patient_name':{'pattern':'Name:(.*)Date','flag':0},
            'patient_address':{'pattern':"Address:(.*)\n",'flag':0},
            'medicines':{'pattern':"Address[^\n]*(.*)Directions",'flag':re.DOTALL},
            'directions':{'pattern':"Directions:(.*)Refill",'flag':re.DOTALL},
            'refill':{'pattern':"Refill:(.*)times",'flag':0},
        }

        pattern_obj = pattern_dict.get(field_name)

        if(pattern_obj):
            match = re.findall(pattern_obj['pattern'],self.text,flags = pattern_obj['flag'])
            if(len(match)>0):
                return match[0].strip()

