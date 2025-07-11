filenames = ['1.Raw Data.txt','2.Reports.txt','3.Presentation.txt']

for item in filenames:
    item= item.replace('.','_',1)
    print(item)