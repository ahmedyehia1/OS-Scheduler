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
pr_non=[]
pr_pree=[]
SJF_pree=[]
RR=[]
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
    FCFS_arr.clear()
    SJF_non.clear()
    pr_non.clear()
    for i in data_base:
        if algorithm.get()=="FCFS":
            FCFS_arr.append([i, data_base[i]["arrival"], data_base[i]["burst"], data_base[i]["arrival"] + data_base[i]["burst"]])
        elif algorithm.get()=="SJF" and rad_sjf.get()==0 :
            SJF_non.append([i, data_base[i]["arrival"], data_base[i]["burst"], data_base[i]["arrival"] + data_base[i]["burst"]])
        elif algorithm.get() == "SJF" and rad_sjf.get()==1:
            SJF_pree.append([i, data_base[i]["arrival"], data_base[i]["burst"], data_base[i]["remain"]])
        elif algorithm.get()=="Priority" and val.get()=="Nonpreemptive":
            pr_non.append([i, data_base[i]["arrival"], data_base[i]["burst"],data_base[i]["priority"], data_base[i]["arrival"] + data_base[i]["burst"]])
        elif algorithm.get() == "Priority" and val.get() == "Preemptive":
            pr_pree.append([i, data_base[i]["arrival"], data_base[i]["burst"], data_base[i]["remain"],data_base[i]["priority"]])
        elif algorithm.get() == "RR":
            RR.append([i, data_base[i]["arrival"], data_base[i]["burst"]])
 
 
 
 
 
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
    if bool==1:
        try:
            if algorithm.get()=="RR":
                time_val = float(time_entry[0].get())
        except:
            messagebox.showerror("Error", "Please enter valid data ")
 
 
def choose_algorithm():
    global AvgWait
    global rad_sjf
    global SJF_pree
    global pr_non
    if algorithm.get()=="FCFS":
        waiting_FCFS = 0.0
 
        FCFS_arr.sort(key=lambda x: x[1])
        for i in range(1,len(FCFS_arr)):
            if FCFS_arr[i][1]<FCFS_arr[i-1][3]:
                waiting_FCFS += (FCFS_arr[i-1][3]-FCFS_arr[i][1])
                FCFS_arr[i][1]=FCFS_arr[i-1][3]
                FCFS_arr[i][3]=FCFS_arr[i][1]+FCFS_arr[i][2]
        AvgWait = round(waiting_FCFS/len(FCFS_arr), 10)
        plot(FCFS_arr,AvgWait)
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
        for i in range(len(acc)):
            if i !=len(acc)-1:
                SJF_non[int(acc[i]):int(acc[i+1])] = sorted(SJF_non[int(acc[i]):int(acc[i+1])], key=lambda x: x[2])
            else:
                SJF_non[acc[-1]:len(SJF_non)] = sorted(SJF_non[acc[-1]:len(SJF_non)], key=lambda x: x[2])
        x=0
        for k in range(0,len(SJF_non)-1):
            for i in range(k+1,len(SJF_non)):
                if SJF_non[i][1]<=SJF_non[k][3]:
                    ls_indx.append([SJF_non[i],i])
                    x=1
                else:
                    break
            if x==1:
                ls_indx.sort(key=lambda x: x[0][2])
                SJF_non[ls_indx[0][1]],SJF_non[k+1]=SJF_non[k+1],SJF_non[ls_indx[0][1]]
                ls_indx.clear()
            if SJF_non[k+1][1]<SJF_non[k][3]:
                waiting_SJF_non +=SJF_non[k][3]-SJF_non[k+1][1]
                SJF_non[k+1][1]=SJF_non[k][3]
                SJF_non[k+1][3]=SJF_non[k+1][1]+SJF_non[k+1][2]
 
        AvgWait = round(waiting_SJF_non/len(SJF_non), 10)
        plot(SJF_non,AvgWait)
        acc.clear()
        SJF_non.clear()
        data_base.clear()
    elif algorithm.get()=="SJF" and rad_sjf.get()==1:
        # SJF_pree ---> process name , arrivel , burst , remaining
        global SJF_pree
        wait_dict = {}
        for p in SJF_pree:
            wait_dict[p[0]] = [[0, p[1]]]
        # sequence ---> process ,start ,time taken
        seq = list()
        SJF_pree = sorted(SJF_pree, key=lambda x: (x[1], x[2]))
        arrivels = []
        time = 0.0
        for i in range(len(SJF_pree)):
            if SJF_pree[i][1] not in arrivels:
                arrivels.append(SJF_pree[i][1])
 
        time = arrivels.pop(0)
 
        while SJF_pree != []:
            if arrivels != []:
                if time == arrivels[0]:
                    for j in range(len(SJF_pree)):
 
                        if SJF_pree[j][1] < time:
                            SJF_pree[j][1] = round(time, 10)
                        else:
                            break
 
                    SJF_pree = sorted(SJF_pree, key=lambda x: (x[1], x[3]))
                    tmp = arrivels.pop(0)
                elif SJF_pree[0][1] > time:
                    time = arrivels[0]
                elif time + SJF_pree[0][3] > arrivels[0]:  # arrivel + remaining
                    if seq != []:
                        if seq[-1][0] == SJF_pree[0][0]:
                            seq[-1][2] += arrivels[0] - time
                        else:
                            seq.append([SJF_pree[0][0], time, arrivels[0] - time])
                    else:
                        seq.append([SJF_pree[0][0], time, arrivels[0] - time])
                    SJF_pree[0][3] -= arrivels[0] - time
                    time = arrivels[0]
                elif time + SJF_pree[0][3] <= arrivels[0]:
                    if seq != []:
                        if seq[-1][0] == SJF_pree[0][0]:
                            seq[-1][2] += SJF_pree[0][3]
                        else:
                            seq.append([SJF_pree[0][0], time, SJF_pree[0][3]])
                    else:
                        seq.append([SJF_pree[0][0], time, SJF_pree[0][3]])
                    time += SJF_pree[0][3]
                    tmp = SJF_pree.pop(0)
 
            else:
                if seq != []:
                    if seq[-1][0] == SJF_pree[0][0]:
                        seq[-1][2] += SJF_pree[0][3]
                    else:
                        seq.append([SJF_pree[0][0], time, SJF_pree[0][3]])
                time += SJF_pree[0][3]
                tmp = SJF_pree.pop(0)
 
        for i in range(len(seq)):
            seq[i].append(seq[i][1] + seq[i][2])
 
        for p in seq:
            wait_dict[p[0]].append([p[1], p[-1]])
 
        AvgWait = 0.0
        for p in wait_dict:
            for i in range(1, len(wait_dict[p])):
                AvgWait += wait_dict[p][i][0] - wait_dict[p][i - 1][1]
        AvgWait = round(Avg_wait/ len(wait_dict),10)
        plot(seq,AvgWait)
        seq.clear()
        arrivels.clear()
        wait_dict.clear()
    elif algorithm.get() == "Priority" and val.get() == "Nonpreemptive":
        waiting_pr_non = 0.0
        ls_indx = []
        pr_non.sort(key=lambda x: x[1])
        acc = [0]
        k = 0
        for i in range(1, len(pr_non)):
            if pr_non[i][1] != pr_non[acc[k]][1]:
                acc.append(i)
                k += 1
        for i in range(len(acc)):
            if i != len(acc) - 1:
                pr_non[int(acc[i]):int(acc[i + 1])] = sorted(pr_non[int(acc[i]):int(acc[i + 1])], key=lambda x: x[3])
            else:
                pr_non[acc[-1]:len(pr_non)] = sorted(pr_non[acc[-1]:len(pr_non)], key=lambda x: x[3])
        x = 0
        for k in range(0, len(pr_non) - 1):
            for i in range(k + 1, len(pr_non)):
                if pr_non[i][1] <= pr_non[k][4]:
                    ls_indx.append([pr_non[i], i])
                    x = 1
                else:
                    break
            if x == 1:
                ls_indx.sort(key=lambda x: x[0][3])
                pr_non[ls_indx[0][1]], pr_non[k + 1] = pr_non[k + 1], pr_non[ls_indx[0][1]]
                ls_indx.clear()
            if pr_non[k + 1][1] < pr_non[k][4]:
                waiting_pr_non += pr_non[k][4] - pr_non[k + 1][1]
                pr_non[k + 1][1] = pr_non[k][4]
                pr_non[k + 1][4] = pr_non[k + 1][1] + pr_non[k + 1][2]
 
        AvgWait = round(waiting_pr_non / len(pr_non), 10)
        plot(pr_non,AvgWait)
        acc.clear()
        pr_non.clear()
        data_base.clear()
    elif algorithm.get() == "Priority" and val.get() == "Preemptive":
        # pr_pree ---> process name , arrivel , burst , remaining
        global pr_pree
        wait_dict = {}
        for p in pr_pree:
            wait_dict[p[0]] = [[0, p[1]]]
        # sequence ---> process ,start ,time taken
        seq = list()
        pr_pree = sorted(pr_pree, key=lambda x: (x[1], x[-1]))
        arrivels = []
        time = 0.0
        for i in range(len(pr_pree)):
            if pr_pree[i][1] not in arrivels:
                arrivels.append(pr_pree[i][1])
 
        time = arrivels.pop(0)
 
        while pr_pree != []:
            if arrivels != []:
                if time == arrivels[0]:
                    for j in range(len(pr_pree)):
 
                        if pr_pree[j][1] < time:
                            pr_pree[j][1] = round(time, 10)
                        else:
                            break
 
                    pr_pree = sorted(pr_pree, key=lambda x: (x[1], x[-1]))
                    tmp = arrivels.pop(0)
                elif pr_pree[0][1] > time:
                    time = arrivels[0]
                elif time + pr_pree[0][3] > arrivels[0]:
                    if seq != []:
                        if seq[-1][0] == pr_pree[0][0]:
                            seq[-1][2] += arrivels[0] - time
                        else:
                            seq.append([pr_pree[0][0], time, arrivels[0] - time])
                    else:
                        seq.append([pr_pree[0][0], time, arrivels[0] - time])
                    pr_pree[0][3] -= arrivels[0] - time
                    time = arrivels[0]
                elif time + pr_pree[0][3] <= arrivels[0]:
                    if seq != []:
                        if seq[-1][0] == pr_pree[0][0]:
                            seq[-1][2] += pr_pree[0][3]
                        else:
                            seq.append([pr_pree[0][0], time, pr_pree[0][3]])
                    else:
                        seq.append([pr_pree[0][0], time, pr_pree[0][3]])
                    time += pr_pree[0][3]
                    tmp = pr_pree.pop(0)
 
            else:
                if seq != []:
                    if seq[-1][0] == pr_pree[0][0]:
                        seq[-1][2] += pr_pree[0][3]
                    else:
                        seq.append([pr_pree[0][0], time, pr_pree[0][3]])
                time += pr_pree[0][3]
                tmp = pr_pree.pop(0)
 
        for i in range(len(seq)):
            seq[i].append(seq[i][1] + seq[i][2])
    
        for p in seq:
            wait_dict[p[0]].append([p[1], p[-1]])
 
        AvgWait = 0.0
        for p in wait_dict:
            for i in range(1, len(wait_dict[p])):
                AvgWait += wait_dict[p][i][0] - wait_dict[p][i - 1][1]
        AvgWait = round(Avg_wait/ len(wait_dict),10)
        plot(seq, AvgWait)
        seq.clear()
        pr_pree.clear()
        arrivels.clear()
        wait_dict.clear()
    elif algorithm.get() == "RR":
        global RR
        global time_val
        # RR ---> process name , arrivel , remaining = initial burst time
        wait_dict = {}
        for p in RR:
            wait_dict[p[0]] = [[0, p[1]]]
        RR = sorted(RR, key=lambda x: x[1])
        quantum = time_val
        time = 0.0
        RQ = []
        seq = []
        arrivels = []
        for i in range(len(RR)):
            if RR[i][1] not in arrivels:
                arrivels.append(RR[i][1])
        time = arrivels[0]
        flag = False
        while RR != []:
            if arrivels != []:
                if time >= arrivels[0]:
                    while arrivels != [] and time >= arrivels[0]:
                        while RR != [] and RR[0][1] <= arrivels[0]:
                            RQ.append(RR[0])
                            RR.pop(0)
                        arrivels.pop(0)
 
                    if flag == True:
                        if RQ[0][2] != 0:
                            RQ.append(RQ.pop(0))
                        else:
                            RQ.pop(0)
                        flag = False
 
                else:
                    if RQ != []:
                        tmp = min(RQ[0][-1], quantum)
                        # if RQ[0][1] > time :
                        #     time = RQ[0][1]
                        if time + tmp > arrivels[0]:
                            flag = True
                            RQ[0][2] -= tmp
                            seq.append([RQ[0][0], time, time + tmp])
                            time += tmp
                        elif time + tmp <= arrivels[0]:
                            RQ[0][2] -= tmp
                            if RQ[0][2] != 0:
                                seq.append([RQ[0][0], time, time + tmp])
                                RQ.append(RQ.pop(0))
                            else:
                                seq.append([RQ[0][0], time, time + tmp])
                                RQ.pop(0)
                            time += tmp
 
                    else:
                        time = arrivels[0]
 
            if arrivels == []:
                while RQ != []:
                    tmp = min(RQ[0][-1], quantum)
                    seq.append([RQ[0][0], time, time + tmp])
                    time += tmp
                    RQ[0][2] -= tmp
                    if RQ[0][2] == 0:
                        RQ.pop(0)
                    else:
                        RQ.append(RQ.pop(0))
 
        for p in seq:
            wait_dict[p[0]].append([p[1], p[-1]])
 
        Avg_wait = 0.0
        for p in wait_dict:
            for i in range(1, len(wait_dict[p])):
                Avg_wait += wait_dict[p][i][0] - wait_dict[p][i - 1][1]
        AvgWait = round(Avg_wait/ len(wait_dict),10)
        plot(seq, AvgWait)
        RQ.clear()
        wait_dict.clear()
        seq.clear()
        arrivels.clear()
 
def plot(arr,wait):
    fig, gnt = plt.subplots()
    gnt.set_ylim(0, 24)
    gnt.set_xlim(0,arr[-1][-1])
    for i in range(len(arr)):
        gnt.broken_barh([(arr[i][1], arr[i][-1])], (0, 4), facecolors = plt.cm.get_cmap('hsv',len(arr)+1)(int(arr[i][0][1:])), edgecolor="#333")
        plt.text((arr[i][1]+arr[i][-1])/2,2,arr[i][0],ha='center', va='center')
        plt.text(int(arr[-1][-1]/2),21,algorithm.get(),fontsize = 18,ha='center', va='center')
        plt.text(int(arr[-1][-1]/2),18,f"Average waiting time: {wait}",ha='center', va='center')
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