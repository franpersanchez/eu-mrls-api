from fastapi import FastAPI
import json
#import FileGenerator
import re

#This is a free to use API for delivering EU MRLs information
app = FastAPI()

@app.get("/")
async def welcome():
    return {"Welcome":"Welcome to the API for EU Pesticides DataBase!"}

#GETs all the MRLs from a Residue definition. Residue definition (str) must be THE SAME as the one in the the database
@app.get("/mrls/MRLsFullList")
async def fetch_mrls_from_all_products(residue):
    
    #depending on the First letter of the residue, it searches in a specific file
    if re.search(r'^[a-bA-B]', residue):
        fileToRead=open('MRL0.json','r')

    if re.search(r'^[1-9]', residue):
        fileToRead=open('MRL0.json','r')

    if re.search(r'^[cC]', residue):
        fileToRead=open('MRL1.json','r')

    if re.search(r'^[d-eD-E]', residue):
        fileToRead=open('MRL2.json','r')

    if re.search(r'^[fF]', residue):
        fileToRead=open('MRL3.json','r')
    
    if re.search(r'^[g-lG-L]', residue):
        fileToRead=open('MRL4.json','r')

    if re.search(r'^[m-oM-O]', residue):
        fileToRead=open('MRL5.json','r')

    if re.search(r'^[p-qP-Q]', residue):
        fileToRead=open('MRL6.json','r')

    if re.search(r'^[r-zR-Z]', residue):
        fileToRead=open('MRL7.json','r')
        
     
   #with json.load, a Json objt is created from the file
    jsonObjt=json.load(fileToRead)
    for residueL in jsonObjt['Pesticides']['Substances']:
        if residueL['Name'] == residue:
            return  {
                "Products": residueL['Product']}
        
 
    #Responds with information related with only 1 product for a given Residue
@app.get("/mrls/oneProduct")
async def fetch_Mrls_from_one_product(residue, foodCode):
     #depending on the First letter of the residue, it searches in a specific file
    if re.search(r'^[a-bA-B]', residue):
        fileToRead=open('MRL0.json','r')

    if re.search(r'^[1-9]', residue):
        fileToRead=open('MRL0.json','r')

    if re.search(r'^[cC]', residue):
        fileToRead=open('MRL1.json','r')

    if re.search(r'^[d-eD-E]', residue):
        fileToRead=open('MRL2.json','r')

    if re.search(r'^[fF]', residue):
        fileToRead=open('MRL3.json','r')
    
    if re.search(r'^[g-lG-L]', residue):
        fileToRead=open('MRL4.json','r')

    if re.search(r'^[m-oM-O]', residue):
        fileToRead=open('MRL5.json','r')

    if re.search(r'^[p-qP-Q]', residue):
        fileToRead=open('MRL6.json','r')

    if re.search(r'^[r-zR-Z]', residue):
        fileToRead=open('MRL7.json','r')
        
      
   #with json.load, a Json objt is created from the file
    jsonObjt=json.load(fileToRead)
    for residueL in jsonObjt['Pesticides']['Substances']:
        if residueL['Name']== residue:

            for product in residueL['Product']:
                if (product['Product_code']==foodCode):
                    key="MRL_ft"
                    if(key in product):
                        return{
                            "Residue": residueL['Name'],
                            "Product": product['Product_name'],
                            "Product code": product['Product_code'],
                            "MRL": product['MRL'],
                            "Footnotes_MRL": product['MRL_ft']
                        }

                    else:
                        return{
                            "Residue": residueL['Name'],
                            "Product": product['Product_name'],
                            "Product code": product['Product_code'],
                            "MRL": product['MRL'],
                            
                        }
     
@app.get('/ProductsList')
async def list_all_products_and_codes():
    fileToRead=open('MRL0.json','r')
        
    #with json.load, a Json objt is created from the file
    jsonObjt=json.load(fileToRead)
    list=[]
    for thevalues in jsonObjt['Pesticides']['Substances'][0]['Product']:
        list.append({
            "Product_name": thevalues["Product_name"],
            "Product_code": thevalues["Product_code"]
        } )
    return {
        "List of Products": list}


        
        
    
        

        
    
   