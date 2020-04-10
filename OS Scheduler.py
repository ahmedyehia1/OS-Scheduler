from tkinter import *
from tkinter import messagebox 
import matplotlib.pyplot as plt 
import numpy

data_base = {}
arrival=[]
burst=[]
priority=[]
processes=[]
P=[]
time_entry=[]
time_val=0.0
FCFS_arr=[]
SJF_non=[]
RR=[]
RQ=[]
def onFrameConfigure(canvas):
    canvas.configure(scrollregion=canvas.bbox("all"))

def create_data():
    global canvas
    global frame
    canvas = Canvas(root, borderwidth=0, background="#e3e3e3")
    frame = Frame(canvas, background="#e3e3e3")
    vsb = Scrollbar(root, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=vsb.set)
    vsb.grid(row=5, column=1, sticky="ns")
    canvas.grid(row=5, column=0)
    canvas.create_window((10, 10), window=frame, anchor="nw")
    frame.bind("<Configure>", lambda event, canvas=canvas: onFrameConfigure(canvas))

    label_3 = Label(frame, text="Processes",background="#e3e3e3")
    label_3.grid(row=4, column=0)
    label_4 = Label(frame, text="Arival Time",background="#e3e3e3")
    label_4.grid(row=4, column=1)
    label_5 = Label(frame, text="Burst Time",background="#e3e3e3")
    label_5.grid(row=4, column=2)

    for i in range(int(input.get())):
        arrival.append(Entry(frame, width=10))
        burst.append(Entry(frame, width=10))
        processes.append(Label(frame, text="P" + str(i),background="#e3e3e3"))
        P.append("P"+str(i))
        data_base.setdefault(P[i])


def submit():
  try:
    global time_val
    global val
    global rad_sjf
    if algorithm.get()=="FCFS":
        k=0
        for i in P:
            data_base[i]={"arrival":float(arrival[k].get()),
                          "burst":float(burst[k].get())}
            k+=1
    elif algorithm.get()=="SJF":
        k=0
        for i in P:
            data_base[i]={"arrival":float(arrival[k].get()),"burst":float(burst[k].get()),"type":val.get(),"remain":float(burst[k].get())}
            k+=1
    elif algorithm.get()=="Priority":
        k=0
        if val.get() == "Preemptive":
            time_slice(1)
        for i in P:
            data_base[i] = {"arrival": float(arrival[k].get()),
                           "burst": float(burst[k].get()),
                           "type":val.get(),
                           "remain":float(burst[k].get()),
                           "priority":float(priority[k].get())}
            k+=1
    elif algorithm.get() == "RR":
        k=0
        time_slice(1)
        for i in P:
            data_base[i] = {"arrival": float(arrival[k].get()),
                           "burst": float(burst[k].get()),
                            "remain":float(burst[k].get())}
            k+=1
    for i in data_base:
        if algorithm.get()=="FCFS":
            FCFS_arr.append([i, data_base[i]["arrival"], data_base[i]["burst"], data_base[i]["arrival"] + data_base[i]["burst"]])
        elif algorithm.get()=="SJF":
            SJF_non.append([i, data_base[i]["arrival"], data_base[i]["burst"], data_base[i]["arrival"] + data_base[i]["burst"]])
        elif algorithm.get()=="RR":
            FCFS_arr.append([i, data_base[i]["arrival"], data_base[i]["burst"],data_base[i]["remain"], data_base[i]["arrival"] + data_base[i]["burst"]])



    '''print(time_val)
    print(data_base)
    print(rad_sjf.get())'''
    choose_algorithm()
  except ValueError:
      messagebox.showerror("Error","Please enter valid data ")



def done_1():
  try:
    create_data()
    for i in range(int(input.get())):
        processes[i].grid(row=5+i,column=0)
        arrival[i].grid(row=5 + i, column=1)
        burst[i].grid(row=5 + i, column=2)
  except ValueError:
     messagebox.showerror("Error","Please enter valid data ")

def clear():
    processes.clear()
    arrival.clear()
    burst.clear()
    data_base.clear()
    P.clear()
    FCFS_arr.clear()
    SJF_non.clear()
    canvas.delete("all")
    for i in range(int(input.get())):
        label = Label(root, text="                      ",bg="#e3e3e3")
        label.grid(row=5 + i, column=0)
        labell = Label(root, text="                      ",bg="#e3e3e3")
        labell.grid(row=5 + i, column=1)
        label_a = Label(root, text="                      ",bg="#e3e3e3")
        label_a.grid(row=5 + i, column=2)
        label_b = Label(root, text="                      ",bg="#e3e3e3")
        label_b.grid(row=5 + i, column=3)

def done_2(mode):
    global val
    val = StringVar()
    val.set("Nonpreemptive")
    rb_1 = Radiobutton(root, text="Preemptive", variable=val, value="Preemptive", command=lambda: radio(val.get()),background="#e3e3e3")
    rb_2 = Radiobutton(root, text="Nonpreemptive", variable=val, value="Nonpreemptive", command=lambda: radio(val.get()),background="#e3e3e3")
    label_6 = Label(frame, text="Priority",background="#e3e3e3")
    if mode == "Priority":
        rb_1.grid(row=2, column=0)
        rb_2.grid(row=2, column=1)
        label_6.grid(row=4, column=3)
        for i in range(int(input.get())):
            priority.append(Entry(frame, width=10))
            priority[i].grid(row=5 + i, column=3)
    elif mode == "FCFS":
        del_pr()
    elif mode == "RR":
        del_pr()
        time_slice(0)
        label_q = Label(root, text="Time Slice",background="#e3e3e3").grid(row=2, column=0)

    else:
        del_pr()
        global rad_sjf
        rad_sjf=IntVar()
        rb_1 = Radiobutton(root, text="Preemptive", variable=rad_sjf, value=1,background="#e3e3e3")
        rb_2 = Radiobutton(root, text="Nonpreemptive", variable=rad_sjf, value=0,background="#e3e3e3")
        rb_1.grid(row=2, column=0)
        rb_2.grid(row=2, column=1)

def radio(val):
    label_7 = Label(root, text="Time Slice",background="#e3e3e3")
    label_b = Label(root, text="                      ",bg="#e3e3e3")
    label_c = Label(root, text="                      ",bg="#e3e3e3")
    if val == "Preemptive":
        label_7.grid(row=3, column=0)
        time_slice(0)
    else:
        label_b.grid(row=3, column=0)
        label_c.grid(row=3, column=1)

def del_pr():
    priority.clear()
    label = Label(root, text="                                      ",bg="#e3e3e3")
    label.grid(row=2, column=0)
    label_x = Label(root, text="                                    ",bg="#e3e3e3")
    label_x.grid(row=2, column=1)
    label_y = Label(root, text="                                    ",bg="#e3e3e3")
    label_y.grid(row=3, column=0)
    label_z = Label(root, text="                                    ",bg="#e3e3e3")
    label_z.grid(row=3, column=1)
    label_p = Label(frame, text="                                    ",bg="#e3e3e3")
    label_p.grid(row=4, column=3)
    for i in range(int(input.get())):
        label_c = Label(frame, text="                      ",bg="#e3e3e3")
        label_c.grid(row=5 + i, column=3)

def time_slice(bool):
    global time_val
    if bool ==0:
        time_entry.clear()
        time_entry.append(Entry(root, width=10))
        time_entry.append(Entry(root, width=10))
        if algorithm.get()=="RR":
            time_entry[0].grid(row=2,column=1)
        else:
            time_entry[1].grid(row=3, column=1)
    if bool==1:
        try:
            if algorithm.get()=="RR":
                time_val = float(time_entry[0].get())
            else: time_val = float(time_entry[1].get())
        except:
            messagebox.showerror("Error", "Please enter valid data ")


def color(num):
    data = dict()
    for i in range(0,num):
        red = int(255-255*i/num) if int(255-255*i/num) >= 0 else 0
        green = int(255*i/num) if int(255*i/num) <= 255 else 255
        data[i] = "#" + "%0.2X" % red + "%0.2X" % green + "00"
    for i in range(0,num):
        green = int(255-255*i/num) if int(255-255*i/num) >= 0 else 0
        blue = int(255*i/num) if int(255*i/num) <= 255 else 255
        data[num+i] = "#00" + "%0.2X" % green + "%0.2X" % blue
    return data
# data_base[i]={"arrival":float(arrival[k].get()),"burst":float(burst[k].get()),"type":val.get(),"remain":float(burst[k].get())}
def choose_algorithm():
    global AvgWait
    global rad_sjf
    if algorithm.get()=="FCFS":
        waiting_FCFS = 0.0

        FCFS_arr.sort(key=lambda x: x[1])
        #print(FCFS_arr)
        for i in range(1,len(FCFS_arr)):
            if FCFS_arr[i][1]<FCFS_arr[i-1][3]:
                waiting_FCFS += (FCFS_arr[i-1][3]-FCFS_arr[i][1])
                FCFS_arr[i][1]=FCFS_arr[i-1][3]
                FCFS_arr[i][3]=FCFS_arr[i][1]+FCFS_arr[i][2]
        AvgWait=waiting_FCFS/len(FCFS_arr)
        print(FCFS_arr)
        plot(FCFS_arr)
        FCFS_arr.clear()
        data_base.clear()
    elif algorithm.get()=="SJF" and rad_sjf.get()==0:
        waiting_SJF_non=0.0
        ls_indx=[]
        SJF_non.sort(key=lambda x: x[1])
        acc = [0]
        k=0
        for i in range(1,len(SJF_non)):
            if SJF_non[i][1]!=SJF_non[acc[k]][1]:
                acc.append(i)
                k+=1
        print(acc)
        for i in range(len(acc)):
            if i !=len(acc)-1:
                SJF_non[int(acc[i]):int(acc[i+1])] = sorted(SJF_non[int(acc[i]):int(acc[i+1])], key=lambda x: x[2])
            else:
                SJF_non[acc[-1]:len(SJF_non)] = sorted(SJF_non[acc[-1]:len(SJF_non)], key=lambda x: x[2])
        #print(SJF_non)

        for k in range(0,len(SJF_non)-1):
            for i in range(k+1,len(SJF_non)):
                if SJF_non[i][1]<=SJF_non[k][3]:
                    ls_indx.append([SJF_non[i],i])
                else:
                    break
            ls_indx.sort(key=lambda x: x[0][2])
            SJF_non[ls_indx[0][1]],SJF_non[k+1]=SJF_non[k+1],SJF_non[ls_indx[0][1]]
            ls_indx.clear()
            if SJF_non[k+1][1]<SJF_non[k][3]:
                waiting_SJF_non +=SJF_non[k][3]-SJF_non[k+1][1]
                SJF_non[k+1][1]=SJF_non[k][3]
                SJF_non[k+1][3]=SJF_non[k+1][1]+SJF_non[k+1][2]

        AvgWait=waiting_SJF_non/len(SJF_non)
        print(SJF_non)
        print(AvgWait)
        plot(SJF_non)
        acc.clear()
        SJF_non.clear()
        data_base.clear()
    elif algorithm.get()=="RR":
         #process / initial / remain / finish
         #time spend in the ready queue
         FCFS_arr.sort(key=lambda x: x[1])
         waiting_rr=0.0
         flag=0
         acc = [0]
         k = 0
         for i in range(1, len(FCFS_arr)):
             if FCFS_arr[i][1] != FCFS_arr[acc[k]][1]:
                 acc.append(i)
                 k += 1
         print(acc)
         #FCFS_arr.clear()
         #acc.clear()
         for i in range(len(acc)-1):
             if i != len(acc) - 1:
                 RQ.append(FCFS_arr[int(acc[i]):int(acc[i + 1])])
                 #zabat time
                 for k in range(len(RQ)):
                     if RQ[k][2]<=time_val:
                         RQ[k][4]=RQ[k][2]+RQ[k][1]
                     else:
                         RQ[k][4]=time_val+RQ[k][1]
                         RQ[k][2]=time_val
                 #build RR and modify RQ
                 for k in range(len(RQ)):
                     if RQ[k][2] <= time_val:
                         RR.append(RQ[k])
                         del RQ[0]
                     else:
                         RQ[k][4] = time_val + RQ[k][1]
                         RQ[k][2] = time_val
                         RR.append(RQ[k])
                         temp=RQ[0]
                         del RQ[0]
                         if FCFS_arr[int(acc[i + 1])][1] <=RR[-1][4]:
                            
                         RQ.append(temp)


             else:
                 RQ.append(FCFS_arr[int(acc[-1]):])


         























def plot(arr):
    n = arr[-1][-1]
    fig, gnt = plt.subplots()  
    gnt.set_ylim(0, 25) 
    gnt.set_xlim(0, n)
    gnt.set_xticks(numpy.arange(0.0,n,0.1))
    data = color(int(n))

    for i in range(len(arr)):
        gnt.broken_barh([(arr[i][1], arr[i][2])], (0, 4), facecolors = data[i])
        plt.text((arr[i][1]+arr[i][-1])/2,2,arr[i][0],ha='center', va='center')
    plt.show()


root = Tk()
root.geometry("650x350")
root.title('OS_Algorithms')
root.configure(background="#e3e3e3")


# create a lable widget
label_1 = Label(root, text="Number of processes:",background="#e3e3e3")
label_1.grid(row=0, column=0, padx=10)

# create an input widget
input = Entry(root)
input.grid(row=0, column=1)



# create dropdown menu
algorithm = StringVar()
algorithm.set("Choose Algorithm")
drop = OptionMenu(root, algorithm, "FCFS", "SJF", "RR", "Priority").grid(row=1, column=0)


# done_1 btn
btn = Button(root, text="Done", command=done_1,bg="#e3e3e3")
btn.grid(row=0, column=3)
# clear btn
btn_1 = Button(root, text="Clear Processes", command=clear,bg="#e3e3e3")
btn_1.grid(row=0, column=4)

# done_2
btn_2 = Button(root, text="Done", command=lambda : done_2(algorithm.get()),background="#e3e3e3")
btn_2.grid(row=1, column=1)

# submit
btn_3=Button(root,text="Submit",command=submit,background="#e3e3e3")
btn_3.grid(row=1,column=3)



root.mainloop()
