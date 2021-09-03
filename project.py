import tkinter as tk
from tkinter import *
from tkinter.ttk import Frame,Button,Style
#from ttk import Frame, Button, Style
from tkinter import messagebox as tkMessageBox
import requests
from io import open
from bs4 import BeautifulSoup
import os
import requests
from urllib.request import urlopen
import re
from textblob import TextBlob
from io import open
from tempfile import NamedTemporaryFile
import shutil
import csv
TITLE_FONT = ("Helvetica", 18, "bold")

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self,borderwidth=1, relief="sunken",
                             width=1600, height=1600)
        container.grid_propagate(False)
        container.pack(side="top", fill="both", expand=True)


        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo,PageThree):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

            frame.configure(bg="#a1dbcd")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

    def get_page(self, classname):
        '''Returns an instance of a page given it's class name as a string'''
        for page in self.frames.values():
            if str(page.__class__.__name__) == classname:
                return page
        return None

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller


        Style().configure("TButton", padding=(0, 5, 0, 5), font='serif 10')

        self.columnconfigure(0, pad=20)
        self.columnconfigure(1, pad=20)
        self.columnconfigure(2, pad=20)
        self.columnconfigure(3, pad=20)

        self.rowconfigure(0, pad=20)
        self.rowconfigure(1, pad=20)
        self.rowconfigure(2, pad=20)
        self.rowconfigure(3, pad=20)
        self.rowconfigure(4, pad=20)

        self.instr1=Label(self,bg='gray12',fg="white" ,width =150,justify=RIGHT, height=6,text="CAREER QUERY")
        self.instr1.configure(font=("Times New Roman", 14, "bold"))
        self.instr1.grid(row=0,column=1, columnspan=4, sticky=W+E)


        self.columnconfigure(0, pad=1)
        self.columnconfigure(1, pad=1)
        self.columnconfigure(2, pad=1)
        self.columnconfigure(3, pad=1)
        self.columnconfigure(4, pad=1)
        self.columnconfigure(6, pad=1)
        self.rowconfigure(0, pad=40)
        self.rowconfigure(1, pad=40)
        self.rowconfigure(2, pad=40)
        self.rowconfigure(3, pad=40)
        self.rowconfigure(4, pad=40)
        self.rowconfigure(6, pad=60)
        self.rowconfigure(10, pad=180)

        self.pack(fill=BOTH, expand=True)


        self.lbl = Label(self, text="TYPE A COMPANY NAME",bg="#a1dbcd")
        self.lbl.configure(font=("Times New Roman", 12, "bold"))
        self.lbl.grid(sticky=W,row=6,column=2, pady=10, padx=5)


        self.text1=Text(self,width=50,height=2)
        self.text1.grid(row=6,column=3,sticky=W)

        #self.text1.insert(0.0,"")
        #self.top1=Label(self,fg="black",text="Search tools for:Android\n\t     Java\n\t            Graphics\n\t        C/C++\n                               Electronics\n\t     CAD\n\t             Networks\n\t            Database",bg="#a1dbcd")
        #self.top1.configure(font=("Times New Roman", 12, "bold"))
        #self.top1.grid(sticky=W,row=3,column=1)

        self.input="jj"

        self.obtn = Button(self, text="SUBMIT",command=self.contains)
        self.obtn.grid(row=10, column=3,columnspan=2,sticky=W)
        self.pack()
    def contains(self):

        self.input = self.text1.get("1.0", "end-1c")
        #print(input)
        if self.input=="":

            print(self.input)
        else:

                self.controller.show_frame("PageOne")
                return


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller


        Style().configure("TButton", padding=(0, 5, 0, 5), font='serif 10')
        self.columnconfigure(0, pad=5)
        self.columnconfigure(1, pad=5)
        self.columnconfigure(2, pad=5)
        self.columnconfigure(3, pad=5)
        self.columnconfigure(4, pad=5)
        self.rowconfigure(0, pad=15)
        self.rowconfigure(1, pad=15)
        self.rowconfigure(2, pad=15)
        self.rowconfigure(3, pad=15)
        self.rowconfigure(4, pad=15)
        self.rowconfigure(18, pad=15)
        self.rowconfigure(46, pad=15)
        self.lbl1 = Label(self, text="",bg="#a1dbcd")
        self.lbl1.grid(sticky=W, row=2, column=1, pady=1, padx=4)
        self.lbl1.configure(font=("Times New Roman",14,"bold"))
        self.lbl2 = Label(self, text="",bg="#a1dbcd")
        self.lbl2.grid(sticky=W, row=2, column=2, pady=1, padx=4)
        self.lbl2.configure(font=("Times New Roman",14))

        #forrtwo big textboxes
        self.tb7 = Text(self, width=50, height=30,font=("Helvetica",11),wrap=WORD)
        self.tb7.grid(row=4, column=0, columnspan=2, sticky=W)
        self.tb8 = Text(self,width=60, height=30,font=("Helvetica",11),wrap=WORD)
        self.tb8.grid(row=4, column=5, columnspan=2, sticky=W)
        #forsmall two textboxes
        self.btn1 = Button(self,text="Graphical Comparison",command=lambda: controller.show_frame("PageTwo"))
        self.btn1.grid(row=18, column=0, sticky=W)

        self.btn2 = Button(self,text="What's Trending",command=lambda: controller.show_frame("PageThree"))

        self.btn2.grid(row=18, column=5, sticky=W)

        #buttons
        self.hbtn = Button(self, text="BACK", command=lambda: controller.show_frame("StartPage"))
        self.hbtn.grid(row=46, column=0, columnspan=2, sticky=W)

        self.obtn = Button(self, text="Click to see result", command=lambda: self.info())
        self.obtn.grid(row=2, column=5, columnspan=2, sticky=W)

    def clean_tweet(tweet):

        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

    def get_tweet_sentiment(tweet):

        # create TextBlob object of passed tweet text
        analysis = TextBlob(PageOne.clean_tweet(tweet))
        # set sentiment
        if analysis.sentiment.polarity > 0:
            return 'positive'
        elif analysis.sentiment.polarity == 0:
            return 'neutral'
        else:
            return 'negative'
    def info(self):
       # print(val)

        startpage = self.controller.get_page("StartPage")
        input = startpage.input

        input=re.sub(r'[\s]+', '-',input)


        self.lbl1.configure(text="YOU SEARCHED FOR:")
        self.lbl2.configure(text=input.title())
        self.tb7.configure(state=NORMAL)
        self.tb8.configure(state=NORMAL)

        self.tb7.delete(1.0,END)
        self.tb8.delete(1.0,END)

        self.scrollbar = Scrollbar(self)  
        self.tb8.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.tb8.yview)
        self.grid()
        self.scrollbar.grid(column=12, row=3, rowspan=2,  sticky=N+S+W)

        baseurl = "https://www.careerbliss.com/"
        # print("Search for a Company")
        count=0
        flag=0
        try:
            url = baseurl + input.title() + "/reviews"
            web = urlopen(url)

        # web2=urllib2.urlopen("https://www.glassdoor.co.in/Reviews/Unisys-Bangalore-Reviews-EI_IE692.0,6_IL.7,16_IM1091.htm")
            soupit = BeautifulSoup(web, 'html.parser')
            scrapeme = soupit.findAll("p", {"class": "comments foggy"})

            with open('/home/home/PycharmProjects/untitled/review.txt', 'w', encoding='utf-8') as f:
                for element in scrapeme:
                    f.write(element.text + '\n')

            f.close()
        except:

            count=count+1


        baseurl = "https://www.indeed.com/cmp/"


        try:
            url = baseurl + input.title() + "/reviews"
            web = urlopen(url)
        # web2=urllib2.urlopen("https://www.glassdoor.co.in/Reviews/Unisys-Bangalore-Reviews-EI_IE692.0,6_IL.7,16_IM1091.htm")
            soupit = BeautifulSoup(web, 'html.parser')
            scrapeme = soupit.findAll("span", {"class": "cmp-review-text"})

            with open('/home/home/PycharmProjects/untitled/review.txt', 'w', encoding='utf-8') as f:
                for element in scrapeme:
                    f.write(element.text + '\n')
                f.close()
        except:

            count=count+1
            

        statinfo = os.stat('/home/home/PycharmProjects/untitled/review.txt')

        if count==2:
            #print("error")
            tkMessageBox.showinfo("CAREER QUERY", "Could not load data for {}".format(input))
            self.controller.show_frame("StartPage")


        elif statinfo.st_size ==0:
            tkMessageBox.showinfo("CAREER QUERY", "Could not load data for {}".format(input))
            self.controller.show_frame("StartPage")

        else:
         with open('/home/home/PycharmProjects/untitled/review.txt','r', encoding='utf-8') as f:
            tweets = []

            for line in f:
                parsed_tweet = {}
                parsed_tweet['text'] = line

                parsed_tweet['sentiment'] = PageOne.get_tweet_sentiment(line)
            # print(parsed_tweet)

            # increment the total count

                if parsed_tweet not in tweets:
                    tweets.append(parsed_tweet)
                else:
                    tweets.append(parsed_tweet)



    # depending on whether the sentiment is positve, negative or neutral, increment the corresponding count
         ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']

         p = round(100 * len(ptweets) / len(tweets))  # for csv file storage

    # percentage of positive tweets
        #print("Positive comments percentage: {} %".format(100 * len(ptweets) / len(tweets)))
         pos="Positive comments : "+ str(p)+" %"

    # picking negative tweets from tweets
         ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']
         nutweets = [tweet for tweet in tweets if tweet['sentiment'] == 'neutral']
         n=round(100 * len(ntweets) / len(tweets),2)
         neg="Negative comments : "+str(n)+" %"
         nu=round(100 * len(nutweets) / len(tweets),2)
         neu="Neutral comments : "+str(nu)+" %"
    # percentage of negative tweets
        #print("Negative comments percentage: {} %".format(100 * len(ntweets) / len(tweets)))
    # percentage of neutral tweets
        #print("Neutral comments percentage: {} %".format(100 * len(nutweets) / len(tweets)))


         self.tb8.insert(END,"Positive reviews:" + '\n')
         for tweet in ptweets:

            self.tb8.insert(END,tweet['text']+'\n')
         self.tb8.insert(END,"-----------------------------------------------------------------------------------------------" + '\n')
    # printing first 5 negative tweets

         self.tb8.insert(END, "Negative reviews:" + '\n')
         for tweet in ntweets[:10]:


            self.tb8.insert(END, tweet['text'] + '\n')

         self.tb8.insert(END, "-----------------------------------------------------------------------------------------------" + '\n')

         self.tb8.insert(END, "Neutral reviews:" + '\n')

         for tweet in nutweets[:10]:

            self.tb8.insert(END, tweet['text'] + '\n')


         self.tb8.insert(END, "------------------------------------------------------------------------------------------------" + '\n')

         self.tb7.insert(END,"" + '\n')
         self.tb7.insert(END,pos+'\n')

         self.tb7.insert(END, neg+'\n')

         self.tb7.insert(END, neu+'\n')

         self.tb7.configure(state=DISABLED)
         self.tb8.configure(state=DISABLED)

         filename = '/home/home/PycharmProjects/untitled/new.csv'
         tempfile = NamedTemporaryFile(mode='w', delete=False)

         fields = ['cmp', 'pos', 'neg', 'neu']

         p=int(p)
         n=int(n)
         nu=int(nu)
         flag = 0
         with open(filename, 'r') as csvfile, tempfile:
             reader = csv.DictReader(csvfile, fieldnames=fields)
             writer = csv.DictWriter(tempfile, fieldnames=fields)
             for row in reader:

                 if row['cmp'] == input.title():
                     flag = 1
                     print('updating row', row['cmp'])
                     row['pos'], row['neg'], row['neu'] = p, n, nu

                 row = {'cmp': row['cmp'], 'pos': row['pos'], 'neg': row['neg'], 'neu': row['neu']}
                 writer.writerow(row)

         shutil.move(tempfile.name, filename)
         if flag == 0:
             l = input.title() + "," + str(p) + "," + str(n) + "," + str(nu)
             f = open("/home/home/PycharmProjects/untitled/new.csv", 'a')

             f.write(l)


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        Style().configure("TButton", padding=(0, 5, 0, 5), font='serif 10')
        self.columnconfigure(0, pad=5)
        self.columnconfigure(1, pad=5)
        self.columnconfigure(2, pad=5)
        self.columnconfigure(3, pad=5)
        self.columnconfigure(4, pad=5)
        self.rowconfigure(0, pad=15)
        self.rowconfigure(1, pad=15)
        self.rowconfigure(2, pad=15)
        self.rowconfigure(3, pad=15)
        self.rowconfigure(4, pad=15)
        self.rowconfigure(18, pad=15)
        self.rowconfigure(46, pad=15)
        self.controller.title("CAREER QUERY")

        #self.pack(fill=BOTH, expand=True)

        self.lbl1 = Label(self, text="TOP TOOLS:",bg="#a1dbcd")
        self.lbl1.grid(sticky=W, row=2, column=1, pady=1, padx=4)
        self.lbl1.configure(font=("Times New Roman", 14, "bold"))
        self.lblj2 = Label(self, text="1.Eclipse",bg="#a1dbcd")
        self.lblj2.grid(sticky=W, row=2, column=2, pady=1, padx=4)
        self.lblj2.configure(font=("Times New Roman", 12))
        self.lblj3 = Label(self, text="2.Netbeans",bg="#a1dbcd")
        self.lblj3.grid(sticky=W, row=2, column=3, pady=1, padx=4)
        self.lblj3.configure(font=("Times New Roman", 12))
        self.lblj4 = Label(self, text="3.IntelliJ IDEA",bg="#a1dbcd")
        self.lblj4.grid(sticky=W, row=2, column=4, pady=1, padx=4)
        self.lblj4.configure(font=("Times New Roman", 12))
        self.lblj5 = Label(self, text="4.JCreator",bg="#a1dbcd")
        self.lblj5.grid(sticky=W, row=2, column=5, pady=1, padx=4)
        self.lblj5.configure(font=("Times New Roman", 12))
        self.hbtn = Button(self, text="BACK", command=lambda: controller.show_frame("StartPage"))
        self.hbtn.grid(row=46, column=0, columnspan=2, sticky=W)
        self.obtn = Button(self, text="SUBMIT", command=lambda: self.info())
        self.obtn.grid(row=46, column=2, columnspan=2, sticky=W)
        self.tb7 = Text(self, width=55, height=20, font=("Helvetica", 11), wrap=WORD)
        self.tb7.grid(row=4, column=0, columnspan=2, sticky=W)
        self.tb8 = Text(self, width=55, height=20, font=("Helvetica", 11), wrap=WORD)
        self.tb8.grid(row=4, column=5, columnspan=2, sticky=W)

        self.tb1 = Text(self, width=55, height=5)
        self.tb1.insert(0.0, "insert tool number to compare here")
        # self.tb1.insert(self,'enter tool number',0)
        self.tb1.grid(row=18, column=0, sticky=W)
        self.tb2 = Text(self, width=55, height=5)
        self.tb2.insert(0.0, "insert tool number to compare here")

        self.tb2.grid(row=18, column=5, sticky=W)

    def info(self):
        # print(val)
        self.tb7.configure(state=NORMAL)
        self.tb8.configure(state=NORMAL)

        self.tb7.delete(1.0, END)
        self.tb8.delete(1.0, END)
        java = {'1': "ECLIPSE\n\n1) Cost : It is free and open source.\n----------------------------------------------------------------------------------------2) Features : It supports many other languages other than JAVA.\n Framework integration like Junit and TestNG and other plugins can be done easily.\n----------------------------------------------------------------------------------------3) Ease of Use : Code Completion\n----------------------------------------------------------------------------------------4) Cons : Eclipse with its plugin eclipseme, is not as up-to-date than Netbeans \n----------------------------------------------------------------------------------------", '2': "NETBEANS\n\n1)Cost : It is free and open source.\n----------------------------------------------------------------------------------------2) Features : Powerful built-in Profiler.\n Natively supports Ant and Maven- no custom built system that only works in the IDE.\n----------------------------------------------------------------------------------------3) Ease of Use : Code completion with JPA and queries.\n----------------------------------------------------------------------------------------4) Cons : Takes up more memory than lighter IDEs.\n----------------------------------------------------------------------------------------", '3': "INTELLIJ\n\n1) Cost : Rs.19,000 to Rs.32,000\n----------------------------------------------------------------------------------------2) Features : A part of debugging process, we often want to evaluate some expression to see its value. With IDEA you don't need to select anything to evaluate .\nYou just put cursor at any place inside your expression (at method hasAttribute in given case) and press Alt+F8. IDEA understands which expression you probably need and shows a dialog window suggesting several possible variants for your expression.\n----------------------------------------------------------------------------------------3) Ease of Use : code inspections, like checkstyle and findbugs, built in and easy to use.\n----------------------------------------------------------------------------------------4) Cons : Expensive.\n----------------------------------------------------------------------------------------", '4': "JCREATOR\n\n1) Cost : Rs.2000 to Rs.5000\n----------------------------------------------------------------------------------------2) Features : Different JDK profiles can be used.\nQuick code writing via project templates.\n----------------------------------------------------------------------------------------3) Ease of Use :  Debugging with an easy, intuitive interface. No command-line prompts necessary.\n----------------------------------------------------------------------------------------4) Cons :  Only available for the Windows operating system, although Wine can be used to run JCreator on Unix systems.\n----------------------------------------------------------------------------------------"}
        point1 = self.tb1.get("1.0", "end-1c")
        point2 = self.tb2.get("1.0", "end-1c")
        if point1 > '4' or point2 > '4':
             tkMessageBox.showinfo("CAREER QUERY", "Please insert correct tool number")
        self.tb7.insert(0.0, java[point1])
        self.tb8.insert(0.0, java[point2])
        self.tb7.configure(state=DISABLED)
        self.tb8.configure(state=DISABLED)
class PageThree(tk.Frame):

        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            self.controller = controller
            Style().configure("TButton", padding=(0, 5, 0, 5), font='serif 10')
            self.columnconfigure(0, pad=5)
            self.columnconfigure(1, pad=5)
            self.columnconfigure(2, pad=5)
            self.columnconfigure(3, pad=5)
            self.columnconfigure(4, pad=5)
            self.rowconfigure(0, pad=15)
            self.rowconfigure(1, pad=15)
            self.rowconfigure(2, pad=15)
            self.rowconfigure(3, pad=15)
            self.rowconfigure(4, pad=15)
            self.rowconfigure(18, pad=15)
            self.rowconfigure(46, pad=15)

            self.lbl1 = Label(self, text="TOP TOOLS:",bg="#a1dbcd")
            self.lbl1.grid(sticky=W, row=2, column=1, pady=1, padx=4)
            self.lbl1.configure(font=("Times New Roman", 14, "bold"))
            self.lbla2 = Label(self, text="1.Autocad",bg="#a1dbcd")
            self.lbla2.grid(sticky=W, row=2, column=2, pady=1, padx=4)
            self.lbla2.configure(font=("Times New Roman", 12))
            self.lbla3 = Label(self, text="2.Solidworks",bg="#a1dbcd")
            self.lbla3.grid(sticky=W, row=2, column=3, pady=1, padx=4)
            self.lbla3.configure(font=("Times New Roman", 12))
            self.lbla4 = Label(self, text="3.VectorWorks",bg="#a1dbcd")
            self.lbla4.grid(sticky=W, row=2, column=4, pady=1, padx=4)
            self.lbla4.configure(font=("Times New Roman", 12))
            self.lbla5 = Label(self, text="4.Draftsight",bg="#a1dbcd")
            self.lbla5.grid(sticky=W, row=2, column=5, pady=1, padx=4)
            self.lbla5.configure(font=("Times New Roman", 12))
            self.hbtn = Button(self, text="BACK", command=lambda:controller.show_frame("StartPage") )
            self.hbtn.grid(row=46, column=0, columnspan=2, sticky=W)
            self.obtn = Button(self, text="SUBMIT", command=lambda: self.info())
            self.obtn.grid(row=46, column=2, columnspan=2, sticky=W)
            self.tb7 = Text(self, width=55, height=20, font=("Helvetica", 11), wrap=WORD)
            self.tb7.grid(row=4, column=0, columnspan=2, sticky=W)
            self.tb8 = Text(self, width=55, height=20, font=("Helvetica", 11), wrap=WORD)
            self.tb8.grid(row=4, column=5, columnspan=2, sticky=W)

            self.tb1 = Text(self, width=55, height=5)
            self.tb1.insert(0.0, "insert tool number to compare here")
            # self.tb1.insert(self,'enter tool number',0)
            self.tb1.grid(row=18, column=0, sticky=W)
            self.tb2 = Text(self, width=55, height=5)
            self.tb2.insert(0.0, "insert tool number to compare here")
            #self.tb2.insert(0.0, "insert here")
            self.tb2.grid(row=18, column=5, sticky=W)

        def info(self):
            # print(val)
            self.tb7.configure(state=NORMAL)
            self.tb8.configure(state=NORMAL)

            self.tb7.delete(1.0, END)
            self.tb8.delete(1.0, END)
            auto = {'1': "AUTOCAD\n\n1) Cost : Rs.15,900\n----------------------------------------------------------------------------------------2) Features : Drawings can be created in 2D or 3D and rotated .\nReduced the design timescales , Reuse of the designs\nThe drawing errors can be corrected easily\nThe drawings can be sent/received via email in seconds\n----------------------------------------------------------------------------------------3) Ease of Use : It is not easy for first-time users to learn the software\n----------------------------------------------------------------------------------------4) Cons : consumes large amounts of the computer processing power\nIt requires high-quality computer hardware that can be costly\nIt requires the advanced manufacturing devices which are very expensive.\n----------------------------------------------------------------------------------------", '2': "SOLIDWORKS\n\n1) Cost : range from Rs. 3,995 to Rs. 8,499.\n----------------------------------------------------------------------------------------2) Features : Faster 2D Drawing Creation \nImproved Large Assembly Performance \nExpanded capabilities for Model Based Definition\n----------------------------------------------------------------------------------------3) Ease of Use : Toolbar is well oriented and simple\nQuick learning is possible.\n----------------------------------------------------------------------------------------4) Cons : Fails to makes detailed drawing using raw data\nImage rendering comes no where near to CATIA or higher versions\n----------------------------------------------------------------------------------------", '3': "VECTORWORKS\n\n1) Cost : $2,595.\n----------------------------------------------------------------------------------------2) Features : It is fully compatible with DWF/DXF/DWG files.\n----------------------------------------------------------------------------------------3) Ease of Use : The program is straightforward to set up and use\n----------------------------------------------------------------------------------------4)Cons : The software requires much computer processing\nsometimes the software does not properly export the DWGs\n----------------------------------------------------------------------------------------", '4': "DRAFTSIGHT\n\n1) Cost : Free.\n----------------------------------------------------------------------------------------2) Features : DraftSight is good for 2D modeling. \nit can save and open DXF and DWG files\noffers macro recording\n----------------------------------------------------------------------------------------3) Ease of Use : it’s good for quick calculations and drawings.\n----------------------------------------------------------------------------------------4) Cons : The free version of DraftSight doesn’t offer much\nit doesn’t run LISP routines and offers no express tools.\n----------------------------------------------------------------------------------------"}
            point1 = self.tb1.get("1.0", "end-1c")
            point2 = self.tb2.get("1.0", "end-1c")
            if point1 > '4' or point2 > '4':
             tkMessageBox.showinfo("CAREER QUERY", "Please insert correct tool number")
            self.tb7.insert(0.0, auto[point1])
            self.tb8.insert(0.0, auto[point2])
            self.tb7.configure(state=DISABLED)
            self.tb8.configure(state=DISABLED)

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
