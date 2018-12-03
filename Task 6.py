import csv 
with open('inputs.csv','w',newline='') as fp:
    #inputs=[]
    fieldnames = ['Name','Email','Mobile','Unviersty','Major']
    a= csv.DictWriter(fp, fieldnames=fieldnames)
    
    
    a.writeheader()
    

    
    a.writerows({'Name' : 'mariam'})
    a.writerow({'Name' : 'rana'})
    a.writerow({'Email' : 'mariam123@yahoo.com'})
    a.writerow({'Email' : 'rana22@gmail.com'})
    a.writerow({'Mobile' : '0102020393'})
    a.writerow({'Mobile' : '0102339944'})
    a.writerow({'Unviersty' : 'cairo'})
    a.writerow({'Unviersty' : 'ain-shams'})
    a.writerow({'Major' : 'CESS'})
    a.writerow({'Major' : 'CESS'})
    

      



   
