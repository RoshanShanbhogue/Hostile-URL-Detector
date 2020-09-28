'''
POINTS TO REMEMBER : - URL shortners, Black/white list ,buttons for CM,check test/train size, plot graph
'''

import csv
import re
from numpy import unicode
import pandas as pd

class Feature_extractor():

    def resultwriter(self, feature, output_dest):
        with open(output_dest, 'a',newline='') as csv_file:
            writer = csv.writer(csv_file)
            try:
                writer.writerow(feature)
            except UnicodeEncodeError:
                pass

    def Tokenise(self, url):
        if url == '':
            return [0, 0, 0]
        token_word = re.split('\W+', url)
        no_ele = sum_len = largest = 0
        for ele in token_word:
            l = len(ele)
            sum_len += l
            if l > 0:
                no_ele += 1

            if largest < l:
                largest = l
        try:
            return [float(sum_len) / no_ele, no_ele, largest]
        except:
            return [0, no_ele, largest]


    def Security_sensitive(self, tokens_words):
        sec_sen_words = ['confirm', 'account', 'banking', 'secure', 'ebayisapi', 'webscr', 'login', 'signin','bank','hdfc','onlinesbi','icici','idbi','paytm','https']
        cnt = 0
        for ele in sec_sen_words:
            if (ele in tokens_words):
                cnt += 1
        return cnt

    def adult_words(self, url):
        url=url.lower()
        bad_words = ['ass','xxx','amateur','sex','porn','adult','fuck','erotic','hentai','naughty','tits','hardcore','dick','milf','bdsm','suck','fake',
        'boob','fap','blowjob','masturbate','video','nude','naked','bare','ero','babe','gay','lesbian','x','cams','big','live','cum','ex','orgasm',
        'orgy','penis','pussy','vagina','dildo','fantasy','18','curvy','teen','mature','busty','pleasure','mate','tube','virgin','69','bang','pound']
        cnt = 0
        for ele in bad_words:
            if (url.find(ele)!=-1):
                cnt += 1
        return cnt


    def count_vowel(self, url):
        count = 0
        for i in url:
            if i=='a'or i=='A'or i=='e'or i=='E'or i=='i' or i=='I'or i=='o'or i=='O' or i=='u' or i=='U':
                count=count+1
        return count

    def adult_to_len(self, url,c):
        return c/len(url)

    def special_to_len(self, url,c):
        return c/len(url)

    def count_digit(self,url):
        count=0
        for i in url:
            if i.isnumeric():
                count+=1
        return count

    def digit_density(self,url,c):
        return c/len(url)

    def Check_IPaddress(self, tokens_words):
        cnt = 0
        for ele in tokens_words:
            if unicode(ele).isnumeric():
                cnt += 1
            else:
                if cnt >= 4:
                    return 1
                else:
                    cnt = 0
        if cnt >= 4:
            return 1
        return 0

    def feature_extract(self, url_input):
        Feature = []
        special_count=[]
        tokens_words = re.split('\W+', url_input)
        Feature.append(url_input)
        Feature.append(len(url_input))
        Feature.append(url_input.count('.'))
        acl= Feature_extractor.Tokenise(self,url_input)
        Feature.append(acl[0])
        Feature.append(acl[1])
        Feature.append(acl[2])
        Feature.append(Feature_extractor.Security_sensitive(self,tokens_words))
        Feature.append(Feature_extractor.Check_IPaddress(self,tokens_words))
        Feature.append(url_input.count('.exe'))
        Feature.append(url_input.count('https://'))
        Feature.append(url_input.count('http://'))
        Feature.append(url_input.count('.rar'))
        Feature.append(url_input.count('.zip'))
        Feature.append(url_input.count('.jpeg'))
        Feature.append(url_input.count('.jpg'))
        Feature.append(url_input.count('.mp4'))
        Feature.append(url_input.count('//'))
        special_count.append(url_input.count('.'))
        special_count.append(url_input.count("/"))
        special_count.append(url_input.count("@"))
        special_count.append(url_input.count("-"))
        special_count.append(url_input.count("?"))
        special_count.append(url_input.count("&"))
        special_count.append(url_input.count("%"))
        special_count.append(url_input.count("!"))
        special_count.append(url_input.count("+"))
        special_count.append(url_input.count("*"))
        special_count.append(url_input.count(","))
        special_count.append(url_input.count("#"))
        special_count.append(url_input.count("_"))
        special_count.append(url_input.count("="))
        special_count.append(url_input.count(" "))
        special_count.append(url_input.count("~"))
        special_count.append(url_input.count(";"))
        special_count.append(url_input.count(":"))
        special_count.append(url_input.count("$"))
        Feature.append(special_count[1])
        Feature.append(special_count[2])
        Feature.append(special_count[3])
        Feature.append(special_count[4])
        Feature.append(special_count[5])
        Feature.append(special_count[6])
        Feature.append(special_count[7])
        Feature.append(special_count[8])
        Feature.append(special_count[9])
        Feature.append(special_count[10])
        Feature.append(special_count[11])
        Feature.append(special_count[12])
        Feature.append(special_count[13])
        Feature.append(special_count[14])
        Feature.append(special_count[15])
        Feature.append(special_count[16])
        Feature.append(special_count[17])
        Feature.append(special_count[18])

        total_special=0
        for i in range(len(special_count)):
            total_special+=special_count[i]

        Feature.append(total_special)
        Feature.append(Feature_extractor.special_to_len(self,url_input,total_special))

        #Feature.append(url_input.count('www.'))
        Feature.append(url_input.count('bit.ly'))
        Feature.append(url_input.count('goo.gl'))
        Feature.append(url_input.count('tinyurl'))
        Feature.append(url_input.count('ow.ly'))
        Feature.append(url_input.count('is.gd'))
        Feature.append(url_input.count('buff.ly'))
        Feature.append(url_input.count('adf.ly'))
        Feature.append(url_input.count('bit.do'))
        Feature.append(url_input.count('mcaf.ee'))
        Feature.append(url_input.count('rebrand.ly'))
        Feature.append(url_input.count('su.pr'))
        Feature.append(url_input.count('polr'))
        Feature.append(url_input.count('bl.ink'))
        Feature.append(url_input.count('moourl'))
        Feature.append(url_input.count('.com'))
        Feature.append(url_input.count('.co'))
        Feature.append(url_input.count('.html'))
        Feature.append(url_input.count('.asp'))
        Feature.append(url_input.count('.aspx'))
        Feature.append(url_input.count('URL'))
        Feature.append(url_input.count('.js'))

        Feature.append(Feature_extractor.count_vowel(self,url_input))
        aw=Feature_extractor.adult_words(self,url_input)
        Feature.append(aw)
        Feature.append(Feature_extractor.adult_to_len(self,url_input,aw))

        num_digits = Feature_extractor.count_digit(self,url_input)
        Feature.append(num_digits)
        Feature.append(Feature_extractor.digit_density(self,url_input,num_digits))

        Feature.append("6")
        # 0.Whitelist=1Million, 1.Malware=11566, 2.Adult=11868, 3.Malicious=46990, 4.Defacement=96274, 5.Phishing=11495, 6.Spam=12000
        print(Feature)
        return Feature


if __name__ == '__main__':
    output_csv='url_features_all.csv'
    print("Extracting features and updating ",output_csv)
    F_e = Feature_extractor()
    df=pd.read_csv("hud_util\datasets\Spam_dataset.csv")
    urls=df.URL
    t=0
    for url in urls:
        t+=1
        F_e.resultwriter(F_e.feature_extract(url),output_csv)
    print("Extraction done (exit or extract from another dataset)",t)