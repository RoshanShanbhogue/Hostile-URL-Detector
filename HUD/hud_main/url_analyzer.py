import whois
import sys
import pandas as pd
import datetime
from hud_util import datasets

class Url_analysis():
    
    def is_appropriate(self,url):
        points = 0
        bad_words = ['ass','xxx','amateur','sex','porn','adult','fuck','erotic','hentai','naughty','tits','hardcore','dick','milf','bdsm','suck','fake',
            'boob','fap','blowjob','masturbate','video','nude','naked','bare','ero','babe','gay','lesbian','cams','big','live','cum','ex','orgasm',
            'orgy','penis','pussy','vagina','dildo','fantasy','18','curvy','teen','mature','busty','pleasure','mate','tube','virgin','69','bang','pound']
        
        for ele in bad_words:
            if (url.find(ele)!=-1):
                points += 1
        cntx = url.count("x") 
        f_x=0
        if url[0]=='x':
            f_x=1    
        #print (f_x,cntx,points)    
        return f_x,cntx,points
    
    def is_short(self,url):
        points = 0
        short_words = ['bit.ly','goo.gl','tinyurl','ow.ly','is.gd','buff.ly','adf.ly',
                       'bit.do','mcaf.ee','rebrand.ly','su.pr','polr','bl.ink','moourl']
        
        for ele in short_words:
            if (url.find(ele)!=-1):
                points = 1          
        return points
        

    def url_validate(self,url,info):      
        if info.domain_name == None:
            return 0
        else:
            return 1
    
    def in_top(self,url,info):
        flag = 0
        d = info
        
        dom = d.domain_name
        if dom == None:
            return 0
        if len(dom)==2:
            dom=dom[0].lower()
        else:
            dom=str(dom).lower()
        print(dom)    
        wl = pd.read_csv("hud_util/datasets/top1m.csv") 
        urls = wl.URL
        r = 0
        for urlgood in urls:
            r += 1
            if urlgood == dom and flag == 0:
                flag = 1  
                break
        if flag == 1:        
            return flag,r
        else:
            return flag,r
    
    def exp_url(self,url,info):
        domain = info   
        dom = domain.domain_name
        if dom == None:
            return 0
        exp=str(domain.expiration_date)
        ex=str(exp)
        #print(ex)
        if ex[0].isnumeric(): 
            exp_year = int(ex[0:4])     
        else:     
            exp_year = int(ex[19:23])     
        this_year = int(datetime.date.today().year)
        return(exp_year-this_year)
        
if __name__ == '__main__':    
    url = input("Enter a url:")  
    info = whois.whois(url)
    ua_object = Url_analysis()
    if ua_object.url_validate(url,info):
        print("The Domain of the input URL is valid")
        pass
    else:
        sys.exit("The input URL is invalid")
    t,ra = ua_object.in_top(url,info)    
    if t:
        print("The domain of URL is present in Alexa top 1 million websites dataset ranked {}".format(ra))
    else:
        print("The domain is not widely recognized")
    
    if ua_object.exp_url(url,info)<1:
        print("The domain entered expires soon or is already expired")
    else:
        print("The domain is healthy and does not expire soon") 
    fx,cx,ad = ua_object.is_appropriate(url)
    if ad > 0 and (cx >=3 or fx==1):
        print("The URL input may contain inappropriate themed / adult content")