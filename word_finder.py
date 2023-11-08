import random
class WordFinder:
    def __init__(self,path):
        self.path = path    
        file = open(self.path,'r')
        self.word_lists = []
        for line in file.readlines():
            self.word_lists.append(line)
        num=len(self.word_lists)    
        print(f" {num} words read")    
    def random(self):
        word=random.choice(self.word_lists).strip()
        return word
            
    def print_word(self):
        for word in self.word_lists:
            word = word.strip()
            return word
        
class SpecialWordFinder(WordFinder):
    def __init__(self, path):
        super().__init__(path)
        file = open(self.path,'r')
        self.word_lists = []
        for line in file.readlines():
            if line.strip() and not line.startswith('#'):
                self.word_lists.append(line)
        
   
        
               




