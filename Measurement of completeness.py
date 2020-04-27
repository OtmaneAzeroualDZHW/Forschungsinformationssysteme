#python 3.7
firstline=1
sl={}
z=0
al=0
ali=0
y=0
f=open("output_completeness.html","w",encoding="utf-8")
with open("input.txt","r",encoding="utf-8") as file:
    for line in file:
        if firstline==1:
            f.write("<table><tr><td>"+line.strip().replace("\t","</td><td>")+"</td><td>Tuple completeness</td></tr>")
            z=len(line.strip().split("\t"))-1
            firstline=0
            continue
        
        p=line.strip().split("\t")
        if len(p)<z: continue
        y+=1
        s=-2
        i=0
        u=0
        for pp in p:
            s+=1
            if u>0: al+=1
            u+=1
            if pp=="NULL":
                i+=1
                ali+=1
                sl[s]=sl.get(s,0)+1
                
        completeness=1.0-(i*0.25)
        f.write("<tr><td>"+line.strip().replace("\t","</td><td>")+"</td><td>"+str(round(completeness,2))+"</td></tr>")
    vr=[]
    
    for xx in range(z):
        if xx in sl: vr.append(str(round(1.0-float(sl[xx])/y,2)))
        else: vr.append("1.0")
    vr.append(str(round(1.0-float(ali)/al,2)))
    f.write("<tr><td>Column completeness</td><td>"+"</td><td>".join(vr)+"</td></tr></table>")
f.close()

