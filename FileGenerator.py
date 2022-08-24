import requests,xmltodict,json,os


    

urls=[
'https://ec.europa.eu/food/plant/pesticides/eu-pesticides-database/mrls/?event=mrl.xml&_=1',
'https://ec.europa.eu/food/plant/pesticides/eu-pesticides-database/mrls/?event=mrl.xml&_=2',
'https://ec.europa.eu/food/plant/pesticides/eu-pesticides-database/mrls/?event=mrl.xml&_=3',
'https://ec.europa.eu/food/plant/pesticides/eu-pesticides-database/mrls/?event=mrl.xml&_=4',
'https://ec.europa.eu/food/plant/pesticides/eu-pesticides-database/mrls/?event=mrl.xml&_=5',
'https://ec.europa.eu/food/plant/pesticides/eu-pesticides-database/mrls/?event=mrl.xml&_=6',
'https://ec.europa.eu/food/plant/pesticides/eu-pesticides-database/mrls/?event=mrl.xml&_=7',
'https://ec.europa.eu/food/plant/pesticides/eu-pesticides-database/mrls/?event=mrl.xml&_=8'
]

files=[]

for index,url in enumerate(urls):

#create response object
    r=requests.get(url)
    #we iterate through the list to give a name to each downloaded xml file
    filename = "MRL" + str(index)+ ".xml"    
    
    with open(filename,'wb') as file:
#write a file with each download
        file.write(r.content)
        file.close()

        if file.closed:
    # open the input xml file and read data 
            with open(filename, errors='ignore') as xml_file: 
                
                my_dict = xmltodict.parse(xml_file.read())

                xml_file.close() 
                os.remove(filename)
                
                json_data = json.dumps(my_dict)
                
                # write the json data to output  
                jsonfile="MRL"+str(index)+ ".json"
                with open(jsonfile, "w") as json_file: 
                    json_file.write(json_data) 
                    json_file.close() 