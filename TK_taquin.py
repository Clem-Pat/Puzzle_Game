nombre_de_cases = 16    #4,9 ou 16


import tkinter as tk
import random  
import time
import math

app = tk.Tk()
app.title("Taquin")
app.minsize(1270,800)
app.resizable(width=True, height=True)
app.geometry("800x645+0+0")
app.configure(bg = "light blue")
Frame = tk.Frame(app, bg='navy')


nbre_de_coups = 0
running=True
nombre_de_cases_par_ligne = int(math.sqrt(nombre_de_cases))

coord_y='échelle'

if nombre_de_cases == 16:
    coord_y=75
    
elif nombre_de_cases == 9:
    coord_y=125

elif nombre_de_cases == 4:
    coord_y=180

else:
    print('dimensions erreur')
    app.destroy


class GameButton2(tk.Button):
    """classe de boutons dans la frame de jeu"""
    
    def __init__(self,id):
        tk.Button.__init__(self,app)
        
        self.id = id
        
        if self.id==-1:
            self.config(text='GAGNE', width=12, height=2, bg="red",fg='black',font="GROBOLD.ttf 40",      
                relief=tk.RAISED, cursor = 'hand2',command=app.destroy)

class GameButton(tk.Button):
    """classe de boutons dans la frame de jeu"""
    
    def __init__(self,id):
        tk.Button.__init__(self,Frame)
        
        self.id = id
        self.state = 'plein'
        
        if self.id in list(range(nombre_de_cases+1)):
            self.config(text=i, width=6, height=2, bg="blue",fg='black',font="GROBOLD.ttf 30",      
                relief=tk.RAISED, cursor = 'hand2',command=self.lancement)
        
    
    def changer(self,event):
        '''change la couleur lorsqu'on passe au dessus du bouton'''
        try:
            if B_gagner['bg']=='red':
                B_gagner.configure(bg='pink')
            elif B_gagner['bg']=='pink':
                B_gagner.configure(bg='red')
        except:
            pass
            
        
    def gagner(self):
        global running
        
        Liste_label[0].destroy()
        Liste_label[1].destroy()
        
        B_gagner.place(x=800,y=200)
        B_gagner.bind("<Enter>", self.changer)
        B_gagner.bind("<Leave>", self.changer)
        
        running=False
        
    def test(self):
        #création de la liste des id:
        liste_id=[]
        for i in range(len(Liste_boutons_prime)):
            for j in range(len(Liste_boutons_prime[i])):
                if Liste_boutons_prime[i][j].state=='plein':
                    liste_id.append(Liste_boutons_prime[i][j].id)
        if liste_id==L_fin and Liste_boutons[nombre_de_cases-1].state=='vide':
            self.gagner()
        else:
            pass
        
        
    def lancement(self):
        global nbre_de_coups
                
        if self.state == 'plein' and running==True:
            
            for i in range(len(L)//nombre_de_cases_par_ligne):
                try :
                    emplacement = Liste_boutons_prime[i].index(self)
                    indice=i
                except:
                    pass

            # on a donc self = Liste_boutons_prime[indice][emplacement]
            
            try:
                if Liste_boutons_prime[indice][emplacement+1].state == 'vide':
                    nbre_de_coups+=1
                    Liste_boutons_prime[indice][emplacement].config(text='',bg='light blue')
                    Liste_boutons_prime[indice][emplacement].state='vide'
                    Liste_boutons_prime[indice][emplacement+1].config(
                    text=Liste_boutons_prime[indice][emplacement].id,bg='blue')
                    Liste_boutons_prime[indice][emplacement+1].state='plein'
                    Liste_boutons_prime[indice][emplacement+1].id=Liste_boutons_prime[indice][emplacement].id
            
            except:
                pass
                
            try:
                if Liste_boutons_prime[indice][emplacement-1].state == 'vide':
                    nbre_de_coups+=1
                    Liste_boutons_prime[indice][emplacement].config(text='',bg='light blue')
                    Liste_boutons_prime[indice][emplacement].state='vide'
                    Liste_boutons_prime[indice][emplacement-1].config(
                    text=Liste_boutons_prime[indice][emplacement].id,bg='blue')
                    Liste_boutons_prime[indice][emplacement-1].state='plein'
                    Liste_boutons_prime[indice][emplacement-1].id=Liste_boutons_prime[indice][emplacement].id
                    
            except:
                pass
                
            try:
                if Liste_boutons_prime[indice+1][emplacement].state == 'vide':
                    nbre_de_coups+=1
                    Liste_boutons_prime[indice][emplacement].config(text='',bg='light blue')
                    Liste_boutons_prime[indice][emplacement].state='vide'
                    Liste_boutons_prime[indice+1][emplacement].config(
                    text=Liste_boutons_prime[indice][emplacement].id,bg='blue')
                    Liste_boutons_prime[indice+1][emplacement].state='plein'
                    Liste_boutons_prime[indice+1][emplacement].id=Liste_boutons_prime[indice][emplacement].id
                    
            except:
                pass
                
            try:
                if Liste_boutons_prime[indice-1][emplacement].state == 'vide':
                    nbre_de_coups+=1
                    Liste_boutons_prime[indice][emplacement].config(text='',bg='light blue')
                    Liste_boutons_prime[indice][emplacement].state='vide'
                    Liste_boutons_prime[indice-1][emplacement].config(
                    text=Liste_boutons_prime[indice][emplacement].id,bg='blue')
                    Liste_boutons_prime[indice-1][emplacement].state='plein'
                    Liste_boutons_prime[indice-1][emplacement].id=Liste_boutons_prime[indice][emplacement].id
                    
            except:
                pass
                
        else:
            pass
            
        Label.config(text="Nombre de coups : {}".format(nbre_de_coups))
        Label.place(x=800, y=400)
        
        self.test()


class GameLabel(tk.Label):
    
    def __init__(self,id):
        tk.Label.__init__(self,app)
        
        self.id = id
        
        if self.id == 0:
            self.config(bg='light blue',fg='red',font='Arial 30 bold')
        elif self.id == 1:
            self.config(text='Puzzle - Taquin',bg='light blue',fg='blue',font='Arial 30 bold')
        elif self.id == 2:
            self.config(text="Remettez les pièces dans l'ordre",
            bg='light blue',fg='black',font='Arial 15')
            
        
        
## Création des listes
L = [i for i in range(1,nombre_de_cases+1)] 

L_debut = [i for i in range(1,nombre_de_cases)] 
n=random.randint(0,1000)
for i in range(2*n):
    alpha=random.randint(0,len(L_debut)-1)
    beta=random.randint(0,len(L_debut)-1)
    while beta==alpha:
        beta=random.randint(0,len(L_debut)-1)
    tempo=L_debut[alpha]
    L_debut[alpha]=L_debut[beta]
    L_debut[beta]=tempo
    
L_debut.append(0)

L_fin = [i for i in range(1,nombre_de_cases)] 

# création de Lprime:
Lprime = [[]]*(len(L)//nombre_de_cases_par_ligne)
for j in range(1,(len(L)//nombre_de_cases_par_ligne)+1):
    for i in range(len(L)+1):
        if i>nombre_de_cases_par_ligne*(j-1) and i<=nombre_de_cases_par_ligne*j:
            Lprime[j-1] = Lprime[j-1] + [i]

#création de Liste_boutons analogue à L 
Liste_boutons=[]
for i in L_debut:
    bouton = GameButton(i)
    Liste_boutons.append(bouton)
    
#création de Liste_boutons_prime  analogue à Lprime
Liste_boutons_prime = [[]]*(len(Lprime))
for j in range(1,len(Lprime)+1):
    for i in range(1,len(L)+1):
        if i>nombre_de_cases_par_ligne*(j-1) and i<=nombre_de_cases_par_ligne*j:
            Liste_boutons_prime[j-1] = Liste_boutons_prime[j-1] + [Liste_boutons[i-1]]
nombre_de_lignes = len(Liste_boutons_prime)


B_gagner=GameButton2(-1)
Label = GameLabel(0)
Liste_label=[]
Liste_label.append(GameLabel(1))
Liste_label.append(GameLabel(2))

def main():
    Liste_label[0].place(x=820,y=200)
    Liste_label[1].place(x=820,y=300)
        
    Liste_boutons[nombre_de_cases-1].config(text='',
    bg="light blue")
    Liste_boutons[nombre_de_cases-1].state = 'vide'
    
    for i in range(len(Lprime)):
        for j in range(len(L)//len(Lprime)):
            Liste_boutons_prime[i][j].grid(row=i,column=j, padx=2, pady=2)
    
    Frame.place(x=100,y=coord_y)
    app.mainloop()




if __name__=="__main__":
    main()