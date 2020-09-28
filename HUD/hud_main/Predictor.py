import sys
import numpy as np
import joblib
from hud_main.feature_extractor import Feature_extractor as Fe
from hud_util import models

class Predictor():
    prediction=list()
    def hostility_of(self,predicted):
        if predicted == 1:
            return "Malware"
        elif predicted == 2:
            return "Adult" 
        elif predicted == 3:
            return "Malicious" 
        elif predicted == 4:
            return "Defacement"
        elif predicted == 5:
            return "Phishing"      
        elif predicted == 6:
            return "Spam"  
       
    def print_features(self,features):
        lafea=dict()
        label=['URL','Length_of_url','No_of_dots','avg_token_length','token_count','largest_token',
               'sec_sen_word_cnt','IPaddress_presence','exe_in_url','https_in_url','http_in_url',
               'rar_in_url','zip_in_url','jpeg_in_url','jpg_in_url','mp4_in_url','d_slash',	'slash','at',
               'hyphen','question',	'ambersand','percentage','exclaim','plus','asterisk','comma',
               'hash','underscore','equal','blank','tilde',	'semicolon','colon','dollar',
               'special_count','special_density','bit.ly','goog.gl','tinyurl','ow.ly',
               'is.gd','buff.ly','adf.ly','bit.do',	'mcaf.ee','rebrand.ly',	'su.pr','polr',
               'bl.ink','moourl','.com','.co','.html','.asp','.aspx','URL_in_url','js','Vowels',
               'bad_words','bad_density','num_digits','digit_density']
        print("\n",len(label))
        for i in range(len(label)):
            lafea[label[i]] = features[i]
        return lafea

    """ def validate(self,url):
        if len(url)<0 or url.find(".")==0:
            return 0
        else:
            return 1
         """
    def extractor(self,url):
        url_feat=Fe.feature_extract(self,url)
        print("Feature extraction completed successfully") 
        return url_feat
        
    def detect(self, url):
        url_feat=Predictor.extractor(self, url)

        test_url = np.array(url_feat[1:])
        test_url = test_url.astype(np.float64)

        #GNB
        load_model = joblib.load("hud_util/models/SavedModelsA/gnb_model_save.pkl")
        pred1 = load_model.predict(test_url.reshape(1,-1))
        #print("The URL is detected as ",Predictor.hostility_of(self,int(pred1))," by Gaussian Naive Bayes")
        
        #Decision Tree Classifier
        load_model = joblib.load("hud_util/models/SavedModelsA/dtc_model_save.pkl")
        pred2 = load_model.predict(test_url.reshape(1,-1))
        #print("The URL is detected as ",Predictor.hostility_of(self,int(pred2))," by Decision Tree Classifier")
        
        #Random Forest Classifier
        load_model = joblib.load("hud_util/models/SavedModelsA/rfc_model_save.pkl")
        pred3 = load_model.predict(test_url.reshape(1,-1))
        #print("The URL is detected as ",Predictor.hostility_of(self,int(pred3))," by Random Forest Classifier")
        
        #KNN
        load_model = joblib.load("hud_util/models/SavedModelsA/knn_model_save.pkl")
        pred4 = load_model.predict(test_url.reshape(1,-1))
        #print("The URL is detected as ",Predictor.hostility_of(self,int(pred4))," by K-Nearest Neighbours")
        
        #MLPC
        load_model = joblib.load("hud_util/models/SavedModelsA/mlpc_model_save.pkl")
        pred5 = load_model.predict(test_url.reshape(1,-1))
        #print("The URL is detected as ",Predictor.hostility_of(self,int(pred5))," by Multi-Layer Perceptron Classifier")            

        prediction=[Predictor.hostility_of(self,int(pred1)),Predictor.hostility_of(self,int(pred2)),Predictor.hostility_of(self,int(pred3)),Predictor.hostility_of(self,int(pred4)),Predictor.hostility_of(self,int(pred5))]
        return prediction

if __name__ == '__main__':
    pred=Predictor()
    url=input("\nEnter a URL:")
    pred.detect(url)