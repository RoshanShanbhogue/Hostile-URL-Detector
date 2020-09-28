import tkinter as tk
from tkinter import ttk
from tkinter import *
from ttkthemes import themed_tk as thtk
from tkinter import Menu
from tkinter import Frame, Scrollbar, filedialog, messagebox
import tkinter.messagebox as tkMessageBox
from tkinter import font as tkFont

import webbrowser
import whois
import time
from os import path
import socket
import csv
import datetime
from PIL import Image, ImageTk
import pandas as pd


class Print_analysis():

    result_data = list()

    def valid_url(self,url):
        info ={}
        valid = 1
        try:
            info = whois.whois(url)
        except whois.parser.PywhoisError:
            valid = 0
        except UnicodeError:
            valid = 0
        if info['domain_name'] == None:
            valid = 0
        if valid == 0 or url.count(" ")==len(url) or url.count(".")==0:
            tkMessageBox.showerror("INVALID URL", "Please check the URL entered")
            return 0
        else:
            return info

    def on_exit(self):
        if(messagebox.askokcancel("Quit", "Do you want to quit?")):
            root.destroy()

    def is_short(self,url):
        short = 0
        if ua.is_short(self,url):
            short = 1
        if short == 0:
            return False
        else:
            tkMessageBox.showwarning("URL Analysis predection : ","a URL shortner detected")
            tkMessageBox.showerror("WARNING", "The URL maybe under a Phishing attack, proceed with atmost caution !! ")
            Print_analysis.Open_browser(self, url, "Still want to visit URL ?")
            return True

    def exit_app(self):
        proceed = tkMessageBox.askquestion("Close", "Exit the application?")
        if proceed =='yes':
            root.destroy()


    def about(self):
        #Tips
        tkMessageBox.showinfo("About the methodology:","Here, WHOIS module is used and after necessary processing, details like \n1.Validity\n2.Expiry date\n3.Domain name \ncan be acquired.(Requires active internet connection)\n\nWe have TOP 1 Million websites dataset released by majestic million blog which is used as a point of reference\nAs this dataset contains adult websites too, we developed a keyword based identification method in which we researched and put together a list of words which may appear in an adult/porn URL. This list acts as a filter of adult websites and warns the user.")

    def tips(self):
        #Tips
        tkMessageBox.showinfo("Tips:","1. Type or paste the URL in the field and submit.\n2.A stable internet connection is required.\n3.Repeated submission of URLs may result in connection failure, a break of few seconds is recommended after each query.")

    def safe_url(self,url):
        tkMessageBox.showinfo("URL Analysis predection : ", "The URL \"" + url + "\" is safe to visit")
        proceed = tkMessageBox.askquestion("Redirect", "Open the URL in browser ?\n(Proceed with caution)")
        if proceed =='yes':
            webbrowser.open(url=url,new=1)

    def Open_browser(self, url, msg):
        proceed = tkMessageBox.askquestion("Redirect", msg)
        if proceed =='yes':
            webbrowser.open(url=url,new=1)

    def open_graphify(self):
        proceed = tkMessageBox.askquestion("Redirect", "View in interactive mode?")
        if proceed =='yes':
            mcg.graphify()

    def open_graphit(self):
        proceed = tkMessageBox.askquestion("Redirect", "View in interactive mode?")
        if proceed =='yes':
            mcg.graphIt()

    # def f1display(self):
    #     window = Toplevel()
    #     f1timg = PhotoImage(file=r'hud_util\icons\f1table.png')
    #     f1t = tk.Button(window, image = f1timg, command=mcg.graphify, borderwidth=0)
    #     f1t.grid(row=0,column=0,padx=10)
    #     f1t.config(activebackground = 'lightpink', state=DISABLED)


    # def recalldisplay(self):
    #     novi = Toplevel()
    #     canvas = Canvas(novi, width = 800, height = 320)
    #     canvas.pack(expand = YES, fill = BOTH, sticky=NW)
    #     gif1 = PhotoImage(file=r'hud_util\icons\recalltable.png')
    #     #image not visual
    #     canvas.create_image(800, 320, image = gif1)
    #     canvas.gif1 = gif1
    
    def add_image(self,img):
        T.config(state=NORMAL)
        T.delete('1.0',tk.END)
        T.image_create(tk.END, image = img)
        T.config(state=DISABLED, background = 'white')

    def display_g1(self,img):
        Print_analysis.add_image(self,img)
        Print_analysis.open_graphify(self)

    def display_g2(self,img):
        Print_analysis.add_image(self,img)
        Print_analysis.open_graphit(self)


    ######################################################################################################################################
    #                                         TAB 1
    ######################################################################################################################################

    ######################################################################################################################################
    #                                         STAGE 1
    ######################################################################################################################################

    def Url_analysis_stage1(self,url):
    
        stage1_data = ""
        curr_date=datetime.datetime.now()

        if Print_analysis.is_short(self,url):
            Print_analysis.result_data.append(url)
            stage1_data = "SHORT URL"
            Print_analysis.result_data.append(stage1_data)
            Print_analysis.result_data.append("---")
            Print_analysis.result_data.append(curr_date.strftime("%x-%X"))
            Print_analysis.write_history(self)
            Print_analysis.history_table(self)

        else:
            # Print_analysis.valid_url(self,url)
            info = Print_analysis.valid_url(self,url)
            validity = ua.url_validate(self,url,info)
            checks = 0
            years_to_expire = ua.exp_url(self,url,info)
            print(ua.is_appropriate(self,url))
            fx,cx,ad = ua.is_appropriate(self,url)
            Print_analysis.result_data.append(url)
            stage1_data = "---"

            # Process box during analysis
            scrollbar = Scrollbar(tab1)
            scrollbar.grid(column=2,row=5,sticky='wns')
            #scrollbar.pack(side=RIGHT, fill=Y)

            T = tk.Text(tab1, height=20, width=94,font=("Roboto", 10),yscrollcommand = scrollbar.set)
            T.grid(column=1,row=5)
            scrollbar.config( command = T.yview )

            T.insert(tk.END, "COMMENCING STAGE-1 ANALYSIS.......")
            T.tag_add("s1", "1.0","1.34")
            T.tag_config("s1",foreground = 'blue')
            root.update()
            time.sleep(1.0)
            root.update()

            #Validate the URL
            T.insert(tk.END, "\n\nValidating the input URL.......")
            if validity == 1:
                checks += 1
                T.insert(tk.END, "\nThe domain of the input URL is valid.")
                T.tag_add("val", "4.31", "4.36")
                T.tag_config("val",foreground = 'green', underline=1)
                #Print_analysis.result_data.append("Valid")
                stage1_data += " | VALID"
                bar['value'] = 20
                root.update()
                time.sleep(1.0)

                #Check in Majestic Million Dataset
                T.insert(tk.END, "\n\nChecking for URL in Majestic Million websites dataset.......")
                top,rank =  ua.in_top(self,url,info)

                if top:
                    checks += 1
                    T.insert(tk.END, "\nThe domain of URL is present in Majestic Million dataset and is ranked {}".format(rank))
                    T.tag_add("mm", "7.14", "7.28")
                    T.tag_config("mm",foreground = 'green', underline=1)
                    #Print_analysis.result_data.append("{}".format(rank))
                    stage1_data += " | {}".format(rank)
                else:
                    T.insert(tk.END, "\nThe domain of URL is not present in Majestic Million dataset.")
                    T.tag_add("mm", "7.14", "7.32")
                    T.tag_config("mm", foreground="red", underline=1)
                    #Print_analysis.result_data.append("---")
                    stage1_data += " | ---"

                bar['value'] = 40
                root.update()
                time.sleep(1.0)

                #Check Expiry
                T.insert(tk.END, "\n\nChecking for URL expiry information.......")
                if years_to_expire < 1:
                    T.insert(tk.END, "\nThe URL entered expires soon or is already expired.")
                    T.tag_add("exp", "10.16", "10.50")
                    T.tag_config("exp",foreground = 'red', underline=1)
                    #Print_analysis.result_data.append("expires soon/expired")
                    stage1_data += " | expires soon/expired"
                else:
                    checks += 1
                    T.insert(tk.END, "\nThe URL is online and does not expire soon.")
                    T.tag_add("exp", "10.4", "10.42")
                    T.tag_config("exp", foreground="green", underline=1)
                    #Print_analysis.result_data.append("Running")
                    stage1_data += " | Running"

                bar['value'] = 60
                root.update()
                time.sleep(1.0)

                #Check for inappropriate content
                T.insert(tk.END, "\n\nChecking URL for inappropriate content.......")
                if fx==1 or ad > 0 or cx >= 3 :
                    T.insert(tk.END, "\nThe URL input may contain adult themed content.")
                    T.tag_add("apt", "13.26", "13.46")
                    T.tag_config("apt",foreground = 'red', underline=1)
                    stage1_data += " | May be Adult"
                else:
                    checks += 1
                    T.insert(tk.END, "\nThe URL input may not contain adult themed content.")
                    T.tag_add("apt", "13.18", "13.35")
                    T.tag_config("apt",foreground = 'green', underline=1)
                    stage1_data += " | Not Adult"

                #T.config(state=DISABLED) #Make log window un-editable

                bar['value'] = 80
                root.update()
                time.sleep(1.0)
                T.yview_pickplace("end")
                bar['value'] = 100
                root.update()

                if checks == 4 :
                    Print_analysis.safe_url(self,url)
                    stage1_data += " | GOOD"
                    Print_analysis.result_data.append(stage1_data)
                    Print_analysis.result_data.append("---")
                    Print_analysis.result_data.append(curr_date.strftime("%x-%X"))
                    Print_analysis.write_history(self)
                    Print_analysis.history_table(self)
                    T.config(state=DISABLED)

                elif checks < 1:
                    tkMessageBox.showwarning("URL Analysis predection : ", "The URL \"" + url + "\" is dead or hostile, visit not recommended ")
                    stage1_data += " | BAD"
                    Print_analysis.result_data.append(stage1_data)
                    Print_analysis.result_data.append("---")
                    Print_analysis.result_data.append(curr_date.strftime("%x-%X"))
                    Print_analysis.write_history(self)
                    Print_analysis.history_table(self)
                    T.config(state=DISABLED)
                    Print_analysis.Open_browser(self, url, "Still want to visit URL ?")

                else:
                    proceed = tkMessageBox.askquestion("Redirect", "Not all checks were passed\n\nProceed to Stage-2 Analysis ?")
                    if proceed == 'yes':
                        stage1_data += " | BAD"
                        Print_analysis.result_data.append(stage1_data)
                        Print_analysis.Url_analysis_stage2(self,url,T)  #visiting stage_2
                        Print_analysis.result_data.append(curr_date.strftime("%x-%X"))
                        Print_analysis.write_history(self)
                        Print_analysis.history_table(self)
                        T.yview_pickplace("end")
                    else:
                        stage1_data += " | BAD"
                        Print_analysis.result_data.append(stage1_data)
                        Print_analysis.result_data.append("---")
                        Print_analysis.result_data.append(curr_date.strftime("%x-%X"))
                        Print_analysis.write_history(self)
                        Print_analysis.history_table(self)
            else:
                T.insert(tk.END, "\nThe domain of the input URL is invalid.")
                T.tag_add("val", "4.31", "4.38")
                T.tag_config("val",foreground = 'red', underline=1)
                stage1_data += " | INVALID"
                Print_analysis.result_data.append(stage1_data)
                Print_analysis.result_data.append("---")
                Print_analysis.result_data.append(curr_date.strftime("%x-%X"))
                Print_analysis.write_history(self)
                Print_analysis.history_table(self)


    ######################################################################################################################################
    #                                         STAGE 2
    ######################################################################################################################################

    def Url_analysis_stage2(self,url,T):

        T.insert(tk.END, "\n\n\nCOMMENCING STAGE-2 ANALYSIS.......")
        T.tag_add("s2", "16.0","16.34")
        T.tag_config("s2",foreground = 'blue')
        time.sleep(1.0)
        root.update()
        T.insert(tk.END, "\n\nPerformming Feature Extraction on the input URL.......")
        url_feat=pred.extractor(self,url)
        T.insert(tk.END,"\nFeature extraction completed.......")

        root.update()
        bar['value']=20
        time.sleep(1.0)

        root.update()
        bar['value']=40
        root.update()
        time.sleep(1.0)

        T.insert(tk.END, "\n\nProceeding with input URL classification\n")
        prediction=pred.detect(self, url)
        bar['value']=50
        T.yview_pickplace("end")
        root.update()
        time.sleep(1.0)

        T.insert(tk.END, "\nGaussian Naive Bayes has predicted the url to be : "+prediction[0].upper()+"\n")
        T.tag_add("gnb", "8.51", "8.60")
        T.tag_config("gnb",foreground = 'red', underline=1)
        bar['value']=60
        T.yview_pickplace("end")
        root.update()
        time.sleep(1.0)

        T.insert(tk.END, "\nDecision Tree Classifier has predicted the url to be : "+prediction[1].upper()+"\n")
        T.tag_add("dtc", "10.55", "10.64")
        T.tag_config("dtc",foreground = 'red', underline=1)
        bar['value']=70
        T.yview_pickplace("end")
        root.update()
        time.sleep(1.0)

        T.insert(tk.END, "\nRandom Forest Classifier has predicted the url to be : "+prediction[2].upper()+"\n")
        T.tag_add("rfc", "12.55", "12.65")
        T.tag_config("rfc",foreground = 'red', underline=1)
        bar['value']=80
        T.yview_pickplace("end")
        root.update()
        time.sleep(1.0)

        '''T.insert(tk.END, "\nK Nearest Naighbors has predicted the url to be : "+prediction[3].upper()+"\n")
        T.tag_add("knn", "14.50", "14.59")
        T.tag_config("knn",foreground = 'red', underline=1)
        bar['value']=90
        T.yview_pickplace("end")
        root.update()
        time.sleep(1.0)'''

        T.insert(tk.END, "\nMulti-Layer Perceptron Classifier has predicted the url to be : "+prediction[3].upper())
        T.tag_add("mlpc", "16.63", "16.73")
        T.tag_config("mlpc",foreground = 'red', underline=1)
        bar['value']=100
        root.update()
        T.yview_pickplace("end")

        tkMessageBox.showwarning("URL Stage-2 Analysis predection : ", "The URL\" " + url + "\" is predicted to be "+prediction[2].upper())
        Print_analysis.result_data.append(prediction[2].upper())
        Print_analysis.Open_browser(self, url, "Do you still want to proceed ?")

        T.config(state=DISABLED) #Make log window un-editable



    ######################################################################################################################################
    #                                         TAB 2
    ######################################################################################################################################

    """ def Detailed_accuracy(self,url):
        scrollbar = Scrollbar(tab2)
        scrollbar.grid(column=2,row=3,sticky='wns')
        #scrollbar.pack(side=RIGHT, fill=Y)
        T = tk.Text(tab2, height=20, width=80,font=("Arial", 10),yscrollcommand = scrollbar.set)
        T.grid(column=1,row=3)
        scrollbar.config( command = T.yview )

        T.insert(tk.END,"Detailed accuracy of models : \n")
        T.insert(tk.END,"\nLoading Models.......")
        root.update()

        GNBm.loadGNB()
        bar2['value']=10
        root.update()

        DTCm.loadDTC()
        bar2['value']=20
        root.update()

        RFCm.loadRFC()
        bar2['value']=30
        root.update()

        KNNm.loadKNN()
        bar2['value']=40
        root.update()

        MLPCm.loadMLPC()
        T.insert(tk.END,"\nModels Loaded.......")
        bar2['value']=50
        root.update()

        T.yview_pickplace("end")

        T.insert(tk.END,"\nLoading Accuracy Metrics.......")
        time.sleep(1.0)
        T.insert(tk.END,"\nAccuracy Metrics Loaded.......")
        T.insert(tk.END,"\n\nGaussian Naive Bayes' hostility wise precision:"+"\n    Malware : "+str(GNBm.cr[0]*100)[0:6]+"\n    Adult : "+str(GNBm.cr[1]*100)[0:6]+"%\n    Malicious : "+str(GNBm.cr[2]*100)[0:6]+"%\n    Defacement : "+str(GNBm.cr[3]*100)[0:6]+"%\n    Phishing : "+str(GNBm.cr[4]*100)[0:6]+"%\n    Spam : "+str(GNBm.cr[5]*100)[0:6]+"%")
        bar2['value']=60
        root.update()

        time.sleep(1.0)
        T.yview_pickplace("end")
        T.insert(tk.END,"\n\nDecision Tree Classifier's hostility wise precision:"+"\n    Malware : "+str(DTCm.cr[0]*100)[0:6]+"\n    Adult : "+str(DTCm.cr[1]*100)[0:6]+"%\n    Malicious : "+str(DTCm.cr[2]*100)[0:6]+"%\n    Defacement : "+str(DTCm.cr[3]*100)[0:6]+"%\n    Phishing : "+str(DTCm.cr[4]*100)[0:6]+"%\n    Spam : "+str(DTCm.cr[5]*100)[0:6]+"%")
        bar2['value']=70
        root.update()

        time.sleep(1.0)
        T.yview_pickplace("end")
        T.insert(tk.END,"\n\nRandon Forest Classifier's hostility wise precision:"+"\n    Malware : "+str(RFCm.cr[0]*100)[0:6]+"\n    Adult : "+str(RFCm.cr[1]*100)[0:6]+"%\n    Malicious : "+str(RFCm.cr[2]*100)[0:6]+"%\n    Defacement : "+str(RFCm.cr[3]*100)[0:6]+"%\n    Phishing : "+str(RFCm.cr[4]*100)[0:6]+"%\n    Spam : "+str(RFCm.cr[5]*100)[0:6]+"%")
        bar2['value']=80
        root.update()

        time.sleep(1.0)
        T.yview_pickplace("end")
        T.insert(tk.END,"\n\nK-Nearest Neighbours' hostility wise precision:"+"\n    Malware : "+str(KNNm.cr[0]*100)[0:6]+"\n    Adult : "+str(KNNm.cr[1]*100)[0:6]+"%\n    Malicious : "+str(KNNm.cr[2]*100)[0:6]+"%\n    Defacement : "+str(KNNm.cr[3]*100)[0:6]+"%\n    Phishing : "+str(KNNm.cr[4]*100)[0:6]+"%\n    Spam : "+str(KNNm.cr[5]*100)[0:6]+"%")
        bar2['value']=90
        root.update()

        time.sleep(1.0)
        T.yview_pickplace("end")
        T.insert(tk.END,"\n\nMulti-Layer Perceptron Classifier's hostility wise precision:"+"\n    Malware : "+str(MLPCm.cr[0]*100)[0:6]+"\n    Adult : "+str(MLPCm.cr[1]*100)[0:6]+"%\n    Malicious : "+str(MLPCm.cr[2]*100)[0:6]+"%\n    Defacement : "+str(MLPCm.cr[3]*100)[0:6]+"%\n    Phishing : "+str(MLPCm.cr[4]*100)[0:6]+"%\n    Spam : "+str(MLPCm.cr[5]*100)[0:6]+"%")
        bar2['value']=100
        root.update()
        T.yview_pickplace("end")

        T.config(state=DISABLED) #Make log window un-editable
        """


    ######################################################################################################################################
    #                                         TAB 3
    ######################################################################################################################################

    def depCheck(self):
        
        success=tk.PhotoImage(file=r'hud_util\icons\tick.png')
        fail=tk.PhotoImage(file=r'hud_util\icons\caution.png')
        internet = 1
        try:
            info = whois.whois("google.com")
        except socket.gaierror:
            internet = 0

        #checking for internet connection.
        if internet == 0:
            ttk.Label(tab3,text = "FAIL",foreground = "red",font=("Ariel", 15) ).grid(row=2, column=4,sticky="w")
            # img = ImageTk.PhotoImage(Image.open("True1.gif"))
            # panel = Label(root, image = img)
        else:  
            ttk.Label(tab3, text = "OK..",foreground = "green",font=("Ariel", 15) ).grid(row=2, column=4,sticky="w")  

        #Checking models are present.
        if path.exists("hud_util/models/SavedModelsA/gnb_model_save.pkl") and path.exists("hud_util/models/SavedModelsA/dtc_model_save.pkl") and path.exists("hud_util/models/SavedModelsA/rfc_model_save.pkl") and path.exists("hud_util/models/SavedModelsA/knn_model_save.pkl") and path.exists("hud_util/models/SavedModelsA/mlpc_model_save.pkl"):
            ttk.Label(tab3, text = "OK..",foreground = "green",font=("Ariel", 15) ).grid(row=3, column=4,sticky="w")
        else:
            ttk.Label(tab3, text = "FAIL",foreground = "red",font=("Ariel", 15) ).grid(row=3, column=4,sticky="w") 

        #Checking of the url dataset is present.
        if path.exists("hud_util/datasets/url_features_all.csv"):       
            ttk.Label(tab3, text = "OK..",foreground = "green",font=("Ariel", 15) ).grid(row=4, column=4,sticky="w")
        else:
            ttk.Label(tab3, text = "FAIL",foreground = "red",font=("Ariel", 15) ).grid(row=4, column=4,sticky="w") 

        #Chewcking if majestic million dataset is present.
        if path.exists("hud_util/datasets/top1m.csv"):       
            ttk.Label(tab3, text = "OK..",foreground = "green",font=("Ariel", 15) ).grid(row=5, column=4,sticky="w")
        else:
            ttk.Label(tab3, text = "FAIL",foreground = "red",font=("Ariel", 15) ).grid(row=5, column=4,sticky="w")

        #Checking if necessary programs are present.
        if path.exists("hud_util/feature_extractor.py") and path.exists("hud_main/feature_extractor.py"):
            ttk.Label(tab3, text = "OK..",foreground = "green",font=("Ariel", 15) ).grid(row=6, column=4,sticky="w")
        else:
            ttk.Label(tab3, text = "FAIL",foreground = "red",font=("Ariel", 15) ).grid(row=6, column=4,sticky="w")

        if path.exists("hud_mslg/Model_loader.py") and  path.exists("hud_mslg/Model_comparision_graph.py"): 
            ttk.Label(tab3, text = "OK..",foreground = "green",font=("Ariel", 15) ).grid(row=7, column=4,sticky="w")
        else:
            ttk.Label(tab3, text = "FAIL",foreground = "red",font=("Ariel", 15) ).grid(row=7, column=4,sticky="w")


    ######################################################################################################################################
    #                                         TAB 4
    ######################################################################################################################################

    def write_history(self):
        with open("hud_util/datasets/history.csv", 'a',newline='') as csv_file:
            writer = csv.writer(csv_file)
            try:
                writer.writerow(Print_analysis.result_data)
                Print_analysis.result_data.clear()
            except UnicodeEncodeError:
                pass
    
    def history_table(self):
        tree.delete(*tree.get_children())
        with open('hud_util/datasets/history.csv') as f:
            reader = csv.DictReader(f, delimiter=',')
            for row in reader:
                tree.insert("", tk.END, values=(row['URL'], row['stage_1'], row['stage_2'], row['pred_date']))

    def clear_history(self):
        data = pd.read_csv("hud_util/datasets/history.csv", index_col ='URL')
        data = data.drop(data.index[0 : data.shape[0]+1])
        #data.drop(inplace = True)
        data.to_csv("hud_util/datasets/history.csv")
        pa.history_table()



######################################################################################################################################
#                                         MAIN
######################################################################################################################################

if __name__ == '__main__':
    pa = Print_analysis()
    
    root = thtk.ThemedTk()
    root.resizable(False, False) #not resizable along y/x-axis
    logo = tk.PhotoImage(file=r"hud_util\icons\logo.png")
    root.iconphoto(False,logo)
    root.geometry('825x520')
    root.get_themes()
    root.set_theme("breeze")
    root.config(background = 'white')
    root.title('HUD -  Hostile URL Detector')    #displayed on the title bar of GUI window

    # Creating Menubar
    menubar = Menu(root)
    # Adding File Menu
    file = Menu(menubar, tearoff = 0)
    menubar.add_cascade(label ='File', menu = file)
    file.add_command(label ='Exit', command = pa.exit_app)
    # Adding Help Menu
    help_ = Menu(menubar, tearoff = 0)
    menubar.add_cascade(label ='Help', menu = help_)
    help_.add_command(label ='Usage Tips', command = pa.tips)
    help_.add_command(label ='About', command = pa.about)
    # display Menu
    root.config(menu = menubar)

    #using style to create tabbed GUI
    style = ttk.Style(root)
    style.configure('lefttab.TNotebook', tabposition='wn')
    tab_control = ttk.Notebook(root, style='lefttab.TNotebook')
    #creating tabs
    #tab0 = ttk.Frame(tab_control)
    tab1 = ttk.Frame(tab_control)
    tab2 = ttk.Frame(tab_control)
    tab3 = ttk.Frame(tab_control)
    tab4 = ttk.Frame(tab_control)

    #tab icons
    #prof_img0 = tk.PhotoImage(file=r'')
    prof_img1 = tk.PhotoImage(file=r'hud_util\icons\Zoom-icon32.png')
    prof_img2 = tk.PhotoImage(file=r'hud_util\icons\Analytics-2-icon32.png')
    prof_img3 = tk.PhotoImage(file=r'hud_util\icons\Check-icon32.png')
    prof_img4 = tk.PhotoImage(file=r'hud_util\icons\Diary-icon32.png')
    banner = tk.PhotoImage(file=r'hud_util\icons\Banner3.png')

    #Adding banner to Root
    ttk.Label(root,image=banner).grid(row=0,column=0,columnspan = 4, sticky = "we")

    #adding tab1 to GUI
    tab_control.add(tab1, text='Predict with Machine Learning', image= prof_img1)
    #adding tab2 to GUI
    tab_control.add(tab2, text='Detailed report of prediction', image= prof_img2)
    #adding tab3 to GUI
    tab_control.add(tab3, text='Detailed report of prediction', image= prof_img3)
    #adding tab4 to GUI
    tab_control.add(tab4, text='History of predictions', image= prof_img4)
    #adding tab0 to GUI
    #tab_control.add(tab0, text='Home', image= prof_img0)

    tab_control.grid(row=1, column=0, sticky="wn")

    #Heading on tab1
    #ttk.Label(tab1, text = "HOSTILE URL DETECTOR",foreground = "coral",font=("Audiowide", 20, 'bold') ).grid(row=0, column=1)
    #Heading on tab2
    ttk.Label(tab2, text = "PERFORMANCE ANALYSIS",foreground = "gray",font=("Audiowide", 20, 'bold') ).grid(row=0, column=1, columnspan=3)
    #Heading on tab3
    ttk.Label(tab3, text = "DEPENDENCY CHECKER ",foreground = "gray",font=("Audiowide", 20, 'bold') ).grid(row=0, column=2, columnspan=3)
    #Heading on tab4
    ttk.Label(tab4, text = "HISTORY OF PREDICTIONS ",foreground = "gray",font=("Audiowide", 20, 'bold') ).grid(row=0, column=0)

    #Enter URL
    ttk.Label(tab1, text="URL:", font=("Roboto", 12, 'italic')).grid(row=1, column=0, padx=2)
    n1 = ttk.Entry(tab1, width=93)
    n1.grid(row=1, column=1)
    ttk.Label(tab1).grid(row=2, column=0) #for 2nd row to be empty in tab1
    root.bind("<Return>", lambda event: pa.Url_analysis_stage1(n1.get() ))

    #Process Box on Tab-1
    T = tk.Text(tab1, height=20, width=94,font=("Roboto", 10))
    T.grid(column=1,row=5)
    T.insert(tk.END,"WAITING FOR USER INPUT........")
    T.tag_add("wm1", "1.0","1.34")
    T.tag_config("wm1",foreground = 'indigo',font=("Roboto", 13,'bold'))
    T.insert(tk.END,"\n\nThe URL goes through two stages :\n     Stage 1 : Pre - Analysis.\n     Stage 2 : Machine Learning Prediction.")

    T.config(state=DISABLED, background = 'white')

    ttk.Label(tab1).grid(row=7,column=1,padx=60) #for last row to be empty on tab1
    ttk.Label(tab1).grid(row=0,column=2,padx=13) #for 2nd column to be empty on tab1
    ttk.Label(tab2).grid(row=0,column=0,padx=10) #for 1st column to be empty on tab2
    ttk.Label(tab2).grid(row=2, column=0) #for 2nd row to be empty on tab2

    #Display Box on Tab-2
    T = tk.Text(tab2, height=23, width=70,font=("Roboto", 8))
    T.grid(column=3,row=2, rowspan = 4)
    # T.insert(tk.END,"THIS IS THE VISULAIZTION BOX")
    # T.tag_add("wm2", "1.0","2.70")
    # T.tag_config("wm2", font=("Roboto", 12,'bold'))
    # T.insert(tk.END,"\nclick the one of the buttons to get started")
    T.config(state=DISABLED)

    #Progrees Bar
    style = ttk.Style()
    style.configure("Horizontal.TProgressbar", background='black', thickness=50)
    bar = ttk.Progressbar(tab1, length=660, style='Horizontal.TProgressbar')
    #bar2 = ttk.Progressbar(tab2, length=565, style='Horizontal.TProgressbar')
    bar.grid(column=1, row=6)
    #bar2.grid(column=1, row=4)

    #Tab-2

    #Button frame on Tab-2
    # but_frame = ttk.Frame(tab2)
    # but_frame.grid(row=3,column=1, columnspan = 3)

    robo16 = tkFont.Font(family='Roboto', size=16)

    #Generate Detailed report
    # gdr = ttk.Button(but_frame, text="Detailed\nReport", command=lambda: pa.Detailed_accuracy(n1.get()))
    # gdr.grid(row=0,column=0,padx=10,sticky=W)
    # gdr.config(width=12)

    #ttk.Label(tab2).grid(row=0, column=0) #for 2nd row to be empty on tab2
    ttk.Label(tab2).grid(row=1, column=1) #for 2nd row to be empty on tab2

    #Generate accuracy graph
    img1 = tk.PhotoImage(file = "hud_util\icons\mvsgraph.png")
    gagimg = tk.PhotoImage(file=r'hud_util\icons\MVA.png')
    gag = tk.Button(tab2, image = gagimg, command = lambda:pa.display_g1(img1), borderwidth=0)
    gag.grid(row=3,column=1,padx=10)
    gag.config(activebackground = 'white')

    #ttk.Label(tab2).grid(row=3, column=1) #for 2nd row to be empty on tab2

    #Generate accuracy metrics graph
    img2 = tk.PhotoImage(file = "hud_util\icons\mvagraph.png")
    gamgimg = tk.PhotoImage(file=r'hud_util\icons\DPG.png')
    gamg = tk.Button(tab2, image=gamgimg, command = lambda:pa.display_g2(img2), borderwidth=0)
    gamg.grid(row=2,column=1,padx=10)
    gamg.config(activebackground = 'white')

    #ttk.Label(tab2).grid(row=5, column=0) #for 4th row to be empty on tab2

    #Generate accuracy metrics graph
    img3 = tk.PhotoImage(file =r'hud_util\icons\f1table.png')
    f1img = tk.PhotoImage(file=r'hud_util\icons\F1ST.png')
    f1 = tk.Button(tab2, image=f1img, command = lambda:pa.add_image(img3), borderwidth=0)
    f1.grid(row=4,column=1,padx=10)
    f1.config(activebackground = 'lightpink')
    
   # ttk.Label(tab2).grid(row=7, column=1) #for 4th row to be empty on tab2

    #Generate accuracy metrics graph
    img4 = tk.PhotoImage(file =r'hud_util\icons\recalltable.png')
    recallimg = tk.PhotoImage(file=r'hud_util\icons\RST.png')
    recall = tk.Button(tab2, image=recallimg, command = lambda:pa.add_image(img4), borderwidth=0)
    recall.grid(row=5,column=1,padx=10)
    recall.config(activebackground = 'lightpink')

    #Generate confusion matrix
    # gcm = ttk.Button(but_frame, text="Confusion\nMatrix")
    # gcm.grid(row=6,column=0,padx=10)
    # gcm.config(width=12)
    
    
    # Tab-3
    ttk.Label(tab3).grid(row=0,column=0,padx=80,pady=20) #for 1st column to be empty on tab3
    ttk.Label(tab3).grid(row=1,column=0,padx=10) #for 1st row to be empty on tab3
    ttk.Label(tab3, text = "Internet access",foreground = "blue",font=("Roboto", 15, 'italic') ).grid(row=2, column=2,sticky="w")
    ttk.Label(tab3, text = "Machine learning models",foreground = "blue",font=("Roboto", 15, 'italic') ).grid(row=3, column=2,sticky="w")
    ttk.Label(tab3, text = "Training datasets",foreground = "blue",font=("Roboto", 15, 'italic') ).grid(row=4, column=2,sticky="w")
    ttk.Label(tab3, text = "Top-1m dataset",foreground = "blue",font=("Roboto", 15, 'italic') ).grid(row=5, column=2,sticky="w")
    ttk.Label(tab3, text = "Feature extractors",foreground = "blue",font=("Roboto", 15, 'italic') ).grid(row=6, column=2,sticky="w")
    ttk.Label(tab3, text = "Graph generator",foreground = "blue",font=("Roboto", 15, 'italic') ).grid(row=7, column=2,sticky="w")

    ttk.Label(tab3, text = " -- ",foreground = "blue",font=("Roboto", 15, 'italic') ).grid(row=2, column=3,sticky="w")
    ttk.Label(tab3, text = " -- ",foreground = "blue",font=("Roboto", 15, 'italic') ).grid(row=3, column=3,sticky="w")
    ttk.Label(tab3, text = " -- ",foreground = "blue",font=("Roboto", 15, 'italic') ).grid(row=4, column=3,sticky="w")
    ttk.Label(tab3, text = " -- ",foreground = "blue",font=("Roboto", 15, 'italic') ).grid(row=5, column=3,sticky="w")
    ttk.Label(tab3, text = " -- ",foreground = "blue",font=("Roboto", 15, 'italic') ).grid(row=6, column=3,sticky="w")
    ttk.Label(tab3, text = " -- ",foreground = "blue",font=("Roboto", 15, 'italic') ).grid(row=7, column=3,sticky="w")

    ttk.Label(tab3).grid(row=8, column=0)
    chk = ttk.Button(tab3, text="Run checker", command=pa.depCheck)
    chk.grid(row=9,column=2,sticky='e')


    # Tab-4

    style = ttk.Style()
    style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('Calibri', 11)) # Modify the font of the body
    style.configure("mystyle.Treeview.Heading", font=('Calibri', 13,'bold')) # Modify the font of the headings

    tree = ttk.Treeview(tab4, style="mystyle.Treeview")

    tree["columns"]=("#1","#2","#3","#4")

    tree.column("#0", width=0, minwidth=0, stretch=tk.NO)
    tree.column("#1", width=200, minwidth=50, stretch=tk.NO)
    tree.column("#2", width=275, minwidth=50, stretch=tk.NO)
    tree.column("#3", width=135, minwidth=50, stretch=tk.NO, anchor=tk.N)
    tree.column("#4", width=155, minwidth=50, stretch=tk.NO, anchor=tk.N)

    tree.heading("#1",text="URL",anchor=tk.N)
    tree.heading("#2", text="STAGE-1",anchor=tk.N)
    tree.heading("#3", text="STAGE-2",anchor=tk.N)
    tree.heading("#4", text="PREDICTION DATE",anchor=tk.N)

    tree.grid(row=2,column=0)

    pa.history_table()

    #Clear History
    clsh = ttk.Button(tab4, text="Clear History", command=pa.clear_history)
    clsh.grid(row=5,column=0,padx=10)
    clsh.config(width=30)

    #Stage-1 help
    ttk.Label(tab4, text = "*The Stage-1 column is divided into subcolumns as follows: Short_URL? | Valid? | Rank? | Expired? | Adult Content? | Good/Bad.",foreground = "brown",font=("Roboto", 10, 'underline') ).grid(row=7, column=0,columnspan = 4,sticky="w",pady=10)

    root.protocol("WM_DELETE_WINDOW", pa.on_exit)
    root.mainloop()