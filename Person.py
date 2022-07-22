import json
import os

class Person:
    
    def __init__(self,id,name,lastName,nationalityId):
        self.id = id
        self.name = name
        self.lastName = lastName
        self.nationalityId = nationalityId
        self.eMail = name.lower() + '.' + lastName.lower() + '@company.com'
    
    def addPerson(self):
        
        personList = []
        person_dict = {
            'id': self.id,
            'name': self.name,
            'lastName': self.lastName,
            'nationalityId': self.nationalityId,
            'e-mail': self.eMail
        }
        
        if not os.path.isfile('person_data.json'):
            personList.append(person_dict)
            with open('person_data.json','w') as file:
                file.write(json.dumps(personList, indent=2))
        else:
            with open('person_data.json') as fp:
                data = json.load(fp)
            data.append(person_dict)
            with open('person_data.json','w') as fw:
                fw.write(json.dumps(data, indent=2))
                
        print(f'{self.nationalityId} kimlik numaralı kayıt eklendi')        

        
    def personList():
        print(("personel listesi").title())
        
        with open('person_data.json') as file:
            data = json.load(file)
            for d in data:
                print(d)
    
    def findPerson(id_):
        if not os.path.isfile('person_data.json'):
            print('Dosya bulunamadı ...')
        else:
            with open('person_data.json') as file:
                data = json.load(file)
            for dt in data:
                if dt["id"] == id_:
                    print("Kayıt bulundu : ")
                    print(dt)
                    break
            print(f"{id_} id'li kayıt dosyada bulunamadı ...")
    
    def updatePerson(id, name, lastName, nationalityId):
        with open('person_data.json') as file:
            data = json.load(file)
            for i in data:
                if i["id"] == id:
                    new_data = i
                    data.remove(i)
                    new_data = {"id": id, "name": name, "lastName": lastName, "nationalityId": nationalityId, "e-mail": name.lower() + '.' + lastName.lower() + '@company.com'}
                    data.append(new_data)
                    with open('person_data.json', 'w') as fu:
                        fu.write(json.dumps(data, indent=2))
            print("Kayıt Güncellendi") 
      
Person.updatePerson(1, "Cristiano", "Ronaldo", "CR07")