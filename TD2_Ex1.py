######## Exercice 1

class Fraction:
    def __init__(self,num,denom):
        self.num=num
        self.denom=denom
        if denom==0 :
            raise ValueError
    def display(self):
        return f"my fraction is : {self.num}/{self.denom}"
    def add(self,self_bis):
        denom_add=self.denom*self_bis.denom
        num_add=self.num*self_bis.denom + self_bis.num*self.denom
        return Fraction(num_add,denom_add)

if __name__=='__main__':   
    disfra1=Fraction(3,4)
    disfra2=Fraction(3,4)
    print(disfra1.display())
    print(disfra1.add(disfra2).display())
######## Exercice 2
    
