import nanoid
import uuid

class Thing():
    def __init__(self,name=None,status="New",typeName="Thing"):
        self.uid = uuid.uuid4().hex
        self.nid = nanoid.generate()
        self.status = "New"
        if name == None:
            self.name = "NoName"
        else:
            self.name = name
        self.typeName = typeName
        self.status = status
    
    def use(self,newStatus="Used"):
        print("Used " + self.name + ".")
        self.status = newStatus
    
    def getStatus(self):
        return self.status

    def getUid(self):
        return self.uid
    
    def getNid(self):
        return self.nid
    
    def getType(self):
        return self.typeName
    
    def sayName(self):
        print(self.typeName + " says, \"" + self.Name + "\"")
    
    