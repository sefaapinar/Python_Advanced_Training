class Class:
  

    def __init__(self,id,branch,name,teacherid) -> None:
        if id is None:
            self.id = 0
        else:
            self.id = id

        
        self.name = name
        self.teacherid = teacherid
        
        