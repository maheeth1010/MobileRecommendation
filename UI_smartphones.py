import tkinter as tk
from tkinter import ttk, LEFT, BOTH, CENTER, TOP, X, RIGHT, BOTTOM
from tkinter.ttk import Label, Entry, Frame
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
import seaborn as sns


class ScrollableFrame(ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        canvas = tk.Canvas(self, width=940, height=1040)
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
        self.scrollable_frame = ttk.Frame(canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y", expand=True)


def click_me():
    pm = prMin.get()
    px = prMax.get()
    rad = v.get()
    br = b.get()
    if pm==0 or px==0 or rad==0:
        ttk.Label(frame.scrollable_frame, text="Price Range and Prefrence are Mandatory!!",
                  font=('Arial', 16, 'bold')).pack(side=TOP, ipady=5, anchor='nw')
    brand = "ohoi!!jiraiyaSensei"
    if br == 1: brand = 'iphone'
    elif br == 2: brand = 'oneplus'
    elif br == 3: brand = 'samsung'
    elif br == 4: brand = 'redmi'
    elif br == 5: brand = 'realme'
    df = pd.read_csv('PrefsAdded.csv')

    loc = -4
    noClusters = 3
    if rad == 1:
        loc = -4
    elif rad == 2:
        loc = -2
        noClusters = 2
    elif rad == 3:
        loc = -1
    elif rad == 4:
        loc = -3
    X = df.iloc[:, [2, loc]].values
    kmeans = KMeans(n_clusters=noClusters, init='k-means++')
    y_kmeans = kmeans.fit_predict(X)
    models = []
    index = 0
    for i in df['Model']:
        models.append([X[index][1], X[index][0], y_kmeans[index], i])
        index += 1
    df.set_index('Model', inplace=True)
    s1 = []
    s2 = []
    s3 = []
    for i in models:
        if i[2] == 0:
            s1.append(i)
    for i in models:
        if i[2] == 1:
            s2.append(i)
    for i in models:
        if i[2] == 2:
            s3.append(i)
    m1 = sorted(s1, reverse=True)[0][0]
    m2 = sorted(s2, reverse=True)[0][0]
    if len(s3) != 0: m3 = sorted(s3, reverse=True)[0][0]
    order = []
    if len(s3) != 0:
        m = max(m1, max(m2, m3))
        if m == m1:
            order.append(0)
            if m2 >= m3:
                order.append(1)
                order.append(2)
            else:
                order.append(2)
                order.append(1)
        elif m == m2:
            order.append(1)
            if m1 >= m3:
                order.append(0)
                order.append(2)
            else:
                order.append(2)
                order.append(0)
        elif m == m3:
            order.append(2)
            if m1 >= m2:
                order.append(0)
                order.append(1)
            else:
                order.append(1)
                order.append(0)
    else:
        m = max(m1, m2)
        if m == m1:
            order.append(0)
            order.append(1)
        else:
            order.append(1)
            order.append(0)
    # print(order)
    prn = pm
    prx = px
    phones = []
    bests = []
    if prn >= prx:
        ttk.Label(frame.scrollable_frame,
                  text="Are you cheating me?!",font=('Arial', 14, 'bold')).pack(side=TOP, ipady=5, anchor='center')
        Label(frame.scrollable_frame, text="").pack(side=TOP, ipady=5, anchor='center')
        Label(frame.scrollable_frame, text="").pack(side=TOP, ipady=5, anchor='center')
        Label(frame.scrollable_frame, text="").pack(side=TOP, ipady=5, anchor='center')
        Label(frame.scrollable_frame, text="").pack(side=TOP, ipady=5, anchor='center')
        Label(frame.scrollable_frame, text="").pack(side=TOP, ipady=5, anchor='center')
        Label(frame.scrollable_frame, text="").pack(side=TOP, ipady=5, anchor='center')
        Label(frame.scrollable_frame, text="").pack(side=TOP, ipady=5, anchor='center')
        Label(frame.scrollable_frame, text="").pack(side=TOP, ipady=5, anchor='center')
        Label(frame.scrollable_frame, text="").pack(side=TOP, ipady=5, anchor='center')
        Label(frame.scrollable_frame, text="").pack(side=TOP, ipady=5, anchor='center')
        Label(frame.scrollable_frame, text="").pack(side=TOP, ipady=5, anchor='center')
    else:
        ttk.Label(frame.scrollable_frame, text="Legend:", font=('Arial', 12, 'bold')).pack(side=TOP, ipady=5,
                                                                                           anchor='center')
        ttk.Label(frame.scrollable_frame, text="Best Phones in your preference and price range:\n"
                                               "This means that phones which are falling in your Price range with your "
                                               "wished preferences satisfying the best.",
                  font=('Arial', 10, 'bold')).pack(side=TOP, ipady=5, anchor='nw')
        ttk.Label(frame.scrollable_frame, text="Best phones in your preference:\n"
                                               "This means that phones which are not falling in your Price range but have "
                                               "your "
                                               "wished preferences satisfying the best.",
                  font=('Arial', 8)).pack(side=TOP, ipady=5, anchor='nw')
        # Good Phones in your preference and price range:
        ttk.Label(frame.scrollable_frame, text="Good Phones in your preference and price range:\n"
                                               "This means that phones which are not falling in your Price range but have "
                                               "your "
                                               "wished preferences satisfying the in a good manner.",
                  font=('Arial', 10, 'bold')).pack(side=TOP, ipady=5, anchor='nw')
        ttk.Label(frame.scrollable_frame, text="Good Phones in your preference:\n"
                                               "This means that phones which are not falling in your Price range but have "
                                               "your "
                                               "wished preferences satisfying the in a good manner.",
                  font=('Arial', 8)).pack(side=TOP, ipady=5, anchor='nw')
        ttk.Label(frame.scrollable_frame, text="Moderate Phones in your preference and price range:\n"
                                               "This means that phones which are not falling in your Price range but have "
                                               "your "
                                               "wished preferences satisfying to some extent only.",
                  font=('Arial', 10, 'bold')).pack(side=TOP, ipady=5, anchor='nw')
        ttk.Label(frame.scrollable_frame, text="Moderate Phones in your preference:\n"
                                               "This means that phones which are not falling in your Price range but have "
                                               "your "
                                               "wished preferences satisfying to some extent only.",
                  font=('Arial', 8)).pack(side=TOP, ipady=5, anchor='nw')
        ttk.Label(frame.scrollable_frame,
                  text="Note: Brand preference is reflected as weight of the text in describing "
                       "the phone (Highlighted in BOLD).").pack(side=TOP, ipady=5, anchor='center')
        index = 0
        for k in order:
            if k == 0:
                # if index == 0: phones.append('Best in this range')
                s1 = sorted(s1, reverse=True)
                no = 0
                for i in s1:
                    if prn <= i[1] <= prx:
                        no += 1
                        # string = i.split(' ').join(' \n')
                        # i = [str(j) for j in i]
                        # i = '\n'.join(i)
                        phones.append(i)
                        # ttk.Label(frame.scrollable_frame, text=i).pack(side=TOP, ipady=5, anchor='nw')
                        # print(i)
                        if no >= 10: break
                        bests.append(s1[-1])
                        bests.append(s1[-2])
                        bests.append(s1[-3])
                        bests.append(s1[-4])
                        bests.append(s1[-5])
            elif k == 1:
                s2 = sorted(s2, reverse=True)
                no = 0
                for i in s2:
                    if prn <= i[1] <= prx:
                        no += 1
                        # print(i)
                        # i = [str(j) for j in i]
                        # i = '\n'.join(i)
                        phones.append(i)
                        # ttk.Label(frame.scrollable_frame, text=i).pack(side=TOP, ipady=5, anchor='nw')
                        if no >= 10: break
                        bests.append(s2[-1])
                        bests.append(s2[-2])
                        bests.append(s2[-3])
                        bests.append(s2[-4])
                        bests.append(s2[-5])
            elif k == 2:
                s3 = sorted(s3, reverse=True)
                no = 0
                for i in s3:
                    if prn <= i[1] <= prx:
                        no += 1
                        # print(i)
                        # i = [str(j) for j in i]
                        # i = '\n'.join(i)
                        phones.append(i)
                        # ttk.Label(frame.scrollable_frame, text=i).pack(side=TOP, ipady=5, anchor='nw')
                        if no >= 10: break
                        bests.append(s3[-1])
                        bests.append(s3[-2])
                        bests.append(s3[-3])
                        bests.append(s3[-4])
                        bests.append(s3[-5])
    count0 = 0
    count1 = 0
    count2 = 0
    for i in phones:
        if i[2] == order[0]: count0 += 1
        elif i[2] == order[1]: count1 += 1
        elif len(order)==3 and i[2] == order[2]: count2 += 1
    set0 = 0
    set1 = 0
    set2 = 0
    for i in phones:
        if i[2] == order[0] and count0 > 0 and set0 == 0:
            ttk.Label(frame.scrollable_frame, text="Best Phones in your preference and price range:",
                      font=('Arial', 14, 'bold')).pack(side=TOP, ipady=5, anchor='nw')
            set0 = 1
        elif i[2] == order[1] and count1 > 0 and set1 == 0:
            ttk.Label(frame.scrollable_frame, text="Best phones in your preference:",
                      font=('Arial', 12, 'bold')).pack(side=TOP, ipady=5, anchor='nw')
            for l in range(5):
                mod = str(bests[l][3])
                j = [str(k) for k in bests[l]]
                j = '\n'.join(j)
                pr = ""
                pr = "Model: "+str(mod)+"\n"
                # print(df.loc[mod]['Price'].tolist())
                li = df.loc[mod]['Price'].tolist()
                # print(type(li))
                if isinstance(li, list):
                # try:
                    pr += "Price: Rs." + str(df.loc[mod]['Price'].tolist()[0]) + "\n"
                    pr += "ROM: " + str(df.loc[mod]['Non-volatile Memory Capacity (converted)'].tolist()[0]) + " GB\n"
                    pr += "RAM: " + str(df.loc[mod]['RAM Capacity (converted)'].tolist()[0]) + " GB\n"
                    pr += "Processor: " + str(df.loc[mod]['Processor'].tolist()[0]) + "\n"
                    pr += "Graphical Controller: " + str(df.loc[mod]['Graphical Controller'].tolist()[0]) + "\n"
                    pr += "Rear Camera: " + str(df.loc[mod]['No. of effective pixels'].tolist()[0]) + " MP\n"
                    pr += "Front Camera: " + str(df.loc[mod]['Secondary No. of pixels'].tolist()[0]) + " MP\n"
                    pr += "Battery Capacity: " + str(df.loc[mod]['Nominal Battery Capacity'].tolist()[0]) + " mAh\n"
                    if brand in pr.lower():
                        ttk.Label(frame.scrollable_frame, text=pr,font=('Arial', 11, 'bold')).pack(side=TOP, ipady=5, anchor='nw')
                    else:
                        ttk.Label(frame.scrollable_frame, text=pr,font=('Arial', 10)).pack(side=TOP, ipady=5, anchor='nw')
                else:
                    pr += "Price: Rs."+str(df.loc[mod]['Price'])+"\n"
                    pr += "ROM: " + str(df.loc[mod]['Non-volatile Memory Capacity (converted)']) + " GB\n"
                    pr += "RAM: " + str(df.loc[mod]['RAM Capacity (converted)']) + " GB\n"
                    pr += "Processor: " + str(df.loc[mod]['Processor']) + "\n"
                    pr += "Graphical Controller: " + str(df.loc[mod]['Graphical Controller']) + "\n"
                    pr += "Rear Camera: " + str(df.loc[mod]['No. of effective pixels']) + " MP\n"
                    pr += "Front Camera: " + str(df.loc[mod]['Secondary No. of pixels']) + " MP\n"
                    pr += "Battery Capacity: " + str(df.loc[mod]['Nominal Battery Capacity']) + " mAh\n"
                    if brand in pr.lower():
                        ttk.Label(frame.scrollable_frame, text=pr, font=('Arial', 11, 'bold')).pack(side=TOP, ipady=5,
                                                                                                    anchor='nw')
                    else:
                        ttk.Label(frame.scrollable_frame, text=pr, font=('Arial', 10)).pack(side=TOP, ipady=5,
                                                                                                    anchor='nw')
            ttk.Label(frame.scrollable_frame, text="Good Phones in your preference and price range:",
                      font=('Arial', 14, 'bold')).pack(side=TOP, ipady=5, anchor='nw')
            set1 = 1

        elif len(order)==3 and i[2] == order[2] and count2 > 0 and set2 == 0:
            ttk.Label(frame.scrollable_frame, text="Good phones in your preference:",
                      font=('Arial', 12, 'bold')).pack(side=TOP, ipady=5, anchor='nw')
            for l in range(5):
                mod = str(bests[l][3])
                j = [str(k) for k in bests[l+5]]
                j = '\n'.join(j)
                li = df.loc[mod]['Price'].tolist()
                # print(type(li))
                pr = ""
                pr = "Model: " + str(mod) + "\n"
                if isinstance(li, list):
                    # try:
                    pr += "Price: Rs." + str(df.loc[mod]['Price'].tolist()[0]) + "\n"
                    pr += "ROM: " + str(df.loc[mod]['Non-volatile Memory Capacity (converted)'].tolist()[0]) + " GB\n"
                    pr += "RAM: " + str(df.loc[mod]['RAM Capacity (converted)'].tolist()[0]) + " GB\n"
                    pr += "Processor: " + str(df.loc[mod]['Processor'].tolist()[0]) + "\n"
                    pr += "Graphical Controller: " + str(df.loc[mod]['Graphical Controller'].tolist()[0]) + "\n"
                    pr += "Rear Camera: " + str(df.loc[mod]['No. of effective pixels'].tolist()[0]) + " MP\n"
                    pr += "Front Camera: " + str(df.loc[mod]['Secondary No. of pixels'].tolist()[0]) + " MP\n"
                    pr += "Battery Capacity: " + str(df.loc[mod]['Nominal Battery Capacity'].tolist()[0]) + " mAh\n"
                    if brand in pr.lower():
                        ttk.Label(frame.scrollable_frame, text=pr, font=('Arial', 11, 'bold')).pack(side=TOP, ipady=5,
                                                                                                    anchor='nw')
                    else:
                        ttk.Label(frame.scrollable_frame, text=pr, font=('Arial', 10)).pack(side=TOP, ipady=5,
                                                                                                    anchor='nw')
                else:
                    pr += "Price: Rs." + str(df.loc[mod]['Price']) + "\n"
                    pr += "ROM: " + str(df.loc[mod]['Non-volatile Memory Capacity (converted)']) + " GB\n"
                    pr += "RAM: " + str(df.loc[mod]['RAM Capacity (converted)']) + " GB\n"
                    pr += "Processor: " + str(df.loc[mod]['Processor']) + "\n"
                    pr += "Graphical Controller: " + str(df.loc[mod]['Graphical Controller']) + "\n"
                    pr += "Rear Camera: " + str(df.loc[mod]['No. of effective pixels']) + " MP\n"
                    pr += "Front Camera: " + str(df.loc[mod]['Secondary No. of pixels']) + " MP\n"
                    pr += "Battery Capacity: " + str(df.loc[mod]['Nominal Battery Capacity']) + " mAh\n"
                    if brand in pr.lower():
                        ttk.Label(frame.scrollable_frame, text=pr, font=('Arial', 11, 'bold')).pack(side=TOP, ipady=5,
                                                                                                    anchor='nw')
                    else:
                        ttk.Label(frame.scrollable_frame, text=pr, font=('Arial', 10)).pack(side=TOP, ipady=5,
                                                                                                    anchor='nw')
            ttk.Label(frame.scrollable_frame, text="Moderate Phones in your preference and price range:",
                      font=('Arial', 14, 'bold')).pack(side=TOP, ipady=5, anchor='nw')
            set2 = 1
        mod = str(i[3])
        i = [str(j) for j in i]
        i = '\n'.join(i)
        li = df.loc[mod]['Price'].tolist()
        # print(type(li))
        pr = ""
        pr = "Model: " + str(mod) + "\n"
        if isinstance(li, list):
            pr += "Price: Rs." + str(df.loc[mod]['Price'].tolist()[0]) + "\n"
            pr += "ROM: " + str(df.loc[mod]['Non-volatile Memory Capacity (converted)'].tolist()[0]) + " GB\n"
            pr += "RAM: " + str(df.loc[mod]['RAM Capacity (converted)'].tolist()[0]) + " GB\n"
            pr += "Processor: " + str(df.loc[mod]['Processor'].tolist()[0]) + "\n"
            pr += "Graphical Controller: " + str(df.loc[mod]['Graphical Controller'].tolist()[0]) + "\n"
            pr += "Rear Camera: " + str(df.loc[mod]['No. of effective pixels'].tolist()[0]) + " MP\n"
            pr += "Front Camera: " + str(df.loc[mod]['Secondary No. of pixels'].tolist()[0]) + " MP\n"
            pr += "Battery Capacity: " + str(df.loc[mod]['Nominal Battery Capacity'].tolist()[0]) + " mAh\n"
            if brand in pr.lower():
                ttk.Label(frame.scrollable_frame, text=pr, font=('Arial', 11, 'bold')).pack(side=TOP, ipady=5,
                                                                                            anchor='nw')
            else:
                ttk.Label(frame.scrollable_frame, text=pr, font=('Arial', 10)).pack(side=TOP, ipady=5,
                                                                                            anchor='nw')
        else:
            pr += "Price: Rs." + str(df.loc[mod]['Price']) + "\n"
            pr += "ROM: " + str(df.loc[mod]['Non-volatile Memory Capacity (converted)']) + " GB\n"
            pr += "RAM: " + str(df.loc[mod]['RAM Capacity (converted)']) + " GB\n"
            pr += "Processor: " + str(df.loc[mod]['Processor']) + "\n"
            pr += "Graphical Controller: " + str(df.loc[mod]['Graphical Controller']) + "\n"
            pr += "Rear Camera: " + str(df.loc[mod]['No. of effective pixels']) + " MP\n"
            pr += "Front Camera: " + str(df.loc[mod]['Secondary No. of pixels']) + " MP\n"
            pr += "Battery Capacity: " + str(df.loc[mod]['Nominal Battery Capacity']) + " mAh\n"
            if brand in pr.lower():
                ttk.Label(frame.scrollable_frame, text=pr, font=('Arial', 11, 'bold')).pack(side=TOP, ipady=5,
                                                                                            anchor='nw')
            else:
                ttk.Label(frame.scrollable_frame, text=pr, font=('Arial', 10)).pack(side=TOP, ipady=5,
                                                                                            anchor='nw')

    ttk.Label(frame.scrollable_frame, text="Moderate phones in your preference:",
              font=('Arial', 12, 'bold')).pack(side=TOP, ipady=5, anchor='nw')
    for l in range(5):
        mod = str(bests[l][3])
        j = [str(k) for k in bests[l+10]]
        j = '\n'.join(j)
        li = df.loc[mod]['Price'].tolist()
        # print(type(li))
        pr = ""
        pr = "Model: " + str(mod) + "\n"
        if isinstance(li, list):
            # try:
            pr += "Price: Rs." + str(df.loc[mod]['Price'].tolist()[0]) + "\n"
            pr += "ROM: " + str(df.loc[mod]['Non-volatile Memory Capacity (converted)'].tolist()[0]) + " GB\n"
            pr += "RAM: " + str(df.loc[mod]['RAM Capacity (converted)'].tolist()[0]) + " GB\n"
            pr += "Processor: " + str(df.loc[mod]['Processor'].tolist()[0]) + "\n"
            pr += "Graphical Controller: " + str(df.loc[mod]['Graphical Controller'].tolist()[0]) + "\n"
            pr += "Rear Camera: " + str(df.loc[mod]['No. of effective pixels'].tolist()[0]) + " MP\n"
            pr += "Front Camera: " + str(df.loc[mod]['Secondary No. of pixels'].tolist()[0]) + " MP\n"
            pr += "Battery Capacity: " + str(df.loc[mod]['Nominal Battery Capacity'].tolist()[0]) + " mAh\n"
            if brand in pr.lower():
                ttk.Label(frame.scrollable_frame, text=pr, font=('Arial', 11, 'bold')).pack(side=TOP, ipady=5,
                                                                                            anchor='nw')
            else:
                ttk.Label(frame.scrollable_frame, text=pr, font=('Arial', 10)).pack(side=TOP, ipady=5,
                                                                                            anchor='nw')
        else:
            pr += "Price: Rs." + str(df.loc[mod]['Price']) + "\n"
            pr += "ROM: " + str(df.loc[mod]['Non-volatile Memory Capacity (converted)']) + " GB\n"
            pr += "RAM: " + str(df.loc[mod]['RAM Capacity (converted)']) + " GB\n"
            pr += "Processor: " + str(df.loc[mod]['Processor']) + "\n"
            pr += "Graphical Controller: " + str(df.loc[mod]['Graphical Controller']) + "\n"
            pr += "Rear Camera: " + str(df.loc[mod]['No. of effective pixels']) + " MP\n"
            pr += "Front Camera: " + str(df.loc[mod]['Secondary No. of pixels']) + " MP\n"
            pr += "Battery Capacity: " + str(df.loc[mod]['Nominal Battery Capacity']) + " mAh\n"
            if brand in pr.lower():
                ttk.Label(frame.scrollable_frame, text=pr, font=('Arial', 11, 'bold')).pack(side=TOP, ipady=5,
                                                                                            anchor='nw')
            else:
                ttk.Label(frame.scrollable_frame, text=pr, font=('Arial', 10)).pack(side=TOP, ipady=5,
                                                                                            anchor='nw')
    # print(bests)
    Label(frame.scrollable_frame, text="").pack(side=TOP, ipady=5, anchor='center')
    Label(frame.scrollable_frame, text="").pack(side=TOP, ipady=5, anchor='center')
    Label(frame.scrollable_frame, text="").pack(side=TOP, ipady=5, anchor='center')
    Label(frame.scrollable_frame, text="").pack(side=TOP, ipady=5, anchor='center')
    Label(frame.scrollable_frame, text="").pack(side=TOP, ipady=5, anchor='center')
    Label(frame.scrollable_frame, text="").pack(side=TOP, ipady=5, anchor='center')
    Label(frame.scrollable_frame, text="").pack(side=TOP, ipady=5, anchor='center')
    Label(frame.scrollable_frame, text="").pack(side=TOP, ipady=5, anchor='center')
    Label(frame.scrollable_frame, text="").pack(side=TOP, ipady=5, anchor='center')
    Label(frame.scrollable_frame, text="").pack(side=TOP, ipady=5, anchor='center')
    Label(frame.scrollable_frame, text="").pack(side=TOP, ipady=5, anchor='center')

#
# def clear():
#     label.config(text="")
def vp_gui():
    root.destroy()
    vp_start_gui()


def vp_start_gui():
    global root
    global frame
    global v
    global b
    global prMin
    global prMax
    root = tk.Tk()
    root.state("zoomed")
    label = ttk.Label()
    # root.geometry('1440x848')
    # root.attributes('-fullscreen', True)
    # w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    # root.geometry("%dx%d+0+0" % (w, h))
    frame = ScrollableFrame(root)
    # frame.pack(side="right", fill=BOTH, anchor='center')
    frame.place(x=100, y=0, width=1400, height=1000, anchor='nw')
    a_label = Label(frame.scrollable_frame, text="Smartphone Data Analysis", font=('Arial', 16, 'bold')).pack(
        anchor='center', ipady=5)
    prMin = tk.IntVar()
    prMax = tk.IntVar()
    Label(frame.scrollable_frame, text='Price range From', font=('Arial', 12, 'bold')).pack(side=TOP, ipady=5, anchor='center')
    e1 = Entry(frame.scrollable_frame, textvariable=prMin).pack(side=TOP, expand=0, ipady=5, anchor='center')
    Label(frame.scrollable_frame, text='Price range To', font=('Arial', 12, 'bold')).pack(side=TOP, ipady=5, anchor='center')
    e2 = Entry(frame.scrollable_frame, textvariable=prMax).pack(side=TOP, ipady=5, anchor='center')


    v = tk.IntVar()
    values = {"Camera Preference": 1,
              "Performance Preference": 2,
              "Display Preference": 3,
              "Battery Preference": 4
              }
    ttk.Label(frame.scrollable_frame, text="What is your preference?", font=('Arial', 12, 'bold')).pack(side=TOP, expand=0, ipady=15)
    count = 1
    ttk.Radiobutton(frame.scrollable_frame, text='Camera', variable=v,
                    value=1).pack(side=TOP, ipady=10)
    ttk.Radiobutton(frame.scrollable_frame, text='Performance', variable=v,
                    value=2).pack(side=TOP, ipady=10)
    ttk.Radiobutton(frame.scrollable_frame, text='Display', variable=v,
                    value=3).pack(side=TOP, pady=10)
    ttk.Radiobutton(frame.scrollable_frame, text='Battery', variable=v,
                    value=4).pack(side=TOP, pady=10)

    ttk.Label(frame.scrollable_frame, text="Brand Preference!", font=('Arial', 12, 'bold')).pack(side=TOP, expand=0, ipady=15)

    b = tk.IntVar()
    ttk.Radiobutton(frame.scrollable_frame, text='Apple', variable=b,
                    value=1).pack(side=TOP, ipady=10)
    ttk.Radiobutton(frame.scrollable_frame, text='Oneplus', variable=b,
                    value=2).pack(side=TOP, ipady=10)
    ttk.Radiobutton(frame.scrollable_frame, text='Samsung', variable=b,
                    value=3).pack(side=TOP, pady=10)
    ttk.Radiobutton(frame.scrollable_frame, text='Xiaomi', variable=b,
                    value=4).pack(side=TOP, pady=10)
    ttk.Radiobutton(frame.scrollable_frame, text='Realme', variable=b,
                    value=5).pack(side=TOP, pady=10)

    action = ttk.Button(frame.scrollable_frame, text="Submit", command=click_me).pack(side=TOP, pady=10)
    ttk.Button(frame.scrollable_frame, text="Refresh", command=vp_gui).pack(side=TOP, pady=10)
    root.mainloop()


if __name__ == '__main__':
    def refresh():
        root.destroy()
        vp_start_gui()

    vp_start_gui()