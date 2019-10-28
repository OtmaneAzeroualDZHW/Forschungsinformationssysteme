#python 3.7
firstline=1
sl={}
z=0
y=0
stan=[]
coral=[]
with open("input2.txt","r",encoding="utf-8") as file:
    for line in file:
        if firstline==1:
            firstline=0
            continue
        p=line.strip().split("\t")
        stan.append(p[1:])
c=0
firstline=1
f=open("output_consistency.html","w",encoding="utf-8")
with open("input.txt","r",encoding="utf-8") as file:
    for line in file:
        if firstline==1:
            f.write("<table><tr><td>"+line.strip().replace("\t","</td><td>")+"</td><td>Consistency</td></tr>")
            z=len(line.strip().split("\t"))-1
            firstline=0
            continue
        
        bad=0
        al=0
        p=line.strip().split("\t")[1:]
        if len(p)<z: continue
        for xx in range(len(p)):    
            al+=1
            if stan[c][xx]!=p[xx]: bad+=1
        consistency=1.0-(float(bad)/al)
        coral.append(consistency)
                    
            
        f.write("<tr><td>"+line.strip().replace("\t","</td><td>")+"</td><td>"+str(round(consistency,2))+"</td></tr>")
        c+=1

consistencyall=sum(coral)/len(coral)
f.write("</table><br />Overall consistency: "+str(round(consistencyall,2)))
f.close()

