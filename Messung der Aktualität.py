import time, math
from datetime import date
from datetime import datetime
#t=date.fromisoformat('04.02.2020')
#print (t)
today = date.fromtimestamp(time.time()).strftime("%d.%m.%Y")
#print (today.strftime("%d.%m.%Y"))

#oo="04.02.2020"
#ddd = datetime.strptime(oo, '%d.%m.%Y').date()
#print ((today-ddd).days)
f=open("timeliness.htm","w",encoding="utf-8")

decline={}
with open("decline.txt","r",encoding="utf-8") as file:
    for line in file:
        p=line.strip().split("\t")
        decline[p[0]]=float(p[1])
            
standard={}
first=1
header=[]
with open("standard.txt","r",encoding="utf-8") as file:
    for line in file:
        record=line.strip().split("\t")
        if first==1:
            first=0
            header=record
            continue
        record=line.strip().split("\t")
        standard[record[0]]={}
        
        for i in range(len(record)):
            if header[i] not in decline: continue
            standard[record[0]][header[i]]={}
            if "|" in record[i]:
                g=record[i].split("|")
                for u in g:
                    if "[" in u:
                        w=u.split("[")
                        standard[record[0]][header[i]][w[0]]=w[1][:-1]
                    else:
                        standard[record[0]][header[i]][u]=today
            else:
                standard[record[0]][header[i]][record[i]]=today

assessed_records=0
timeliness_sum=0
first=1
with open("input.txt","r",encoding="utf-8") as file:
    for line in file:
        record=line.strip().split("\t")
        if first==1:
            first=0
            header=record
            f.write("<table border=\"1\"><tr><td><strong>"+"</strong></td><td><strong>".join(header)+"</strong></td><td><strong>Record timeliness</strong></td></tr>\n")
            continue
        timrec=0
        assessed_values=0
        if record[0] not in standard:
            print (record[0]+" not found in standard")
            continue
        
        for i in range(len(record)):
            if header[i] not in decline: continue
            if record[i] in standard[record[0]][header[i]]:
                valuetime=standard[record[0]][header[i]][record[i]]
                age=float((datetime.strptime(today, '%d.%m.%Y').date()-datetime.strptime(valuetime, '%d.%m.%Y').date()).days)/365
                print (age)
                timfield=math.exp(-decline[header[i]]*age)
                timrec+=timfield
                assessed_values+=1
            else:
                print (record[0]+" field "+header[i]+" can not be assessed")

        if timrec>0:
            record_timeliness=timrec/assessed_values
            record_timeliness2=str(round(record_timeliness,2))
        else:
            record_timeliness="NULL"
            record_timeliness2="Not assessed"

        f.write("<tr><td>"+"</td><td>".join(record)+"</td><td>"+str(record_timeliness2)+"</td></tr>\n")

        if record_timeliness!="NULL":
            timeliness_sum+=record_timeliness
            assessed_records+=1
f.write("</table>")            
if assessed_records>0:
    dataset_timeliness = timeliness_sum/assessed_records
    f.write("<br />Overall timeliness: "+str(round(dataset_timeliness,2)))


f.close()


'''


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
f.write("</table>
f.close()

'''
