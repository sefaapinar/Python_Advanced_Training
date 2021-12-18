class Lesson:
  

    def __init__(self,id,branch,name) -> None:
        if id is None:
            self.id = 0
        else:
            self.id = id

        self.branch= branch
        self.name = name
  
        
        