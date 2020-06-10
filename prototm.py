import hashlib
import os
import glob
import shutil
repcor = True
BLOCKSIZE = 65536
try:
    fichier = input("Quel est le fichier/dossier à analyser? \n")
    if os.path.isdir(fichier):
        os.chdir(fichier)
        for file in glob.glob("*"):
                if os.path.isdir(file):
                        print(file)
                    
                
                else :
                        hasher = hashlib.sha256()
                        with open(file, 'rb') as afile:
                            buf = afile.read(BLOCKSIZE)
                            while len(buf) > 0:
                    
                                hasher.update(buf)
                                buf = afile.read(BLOCKSIZE)
                            mon_hash = open("hash.txt","w")
                            
                            mon_hash.write(hasher.hexdigest())
                            mon_hash.close()
                


            
                            f1=open("hash.txt","r")
                            f2=open("basededonnee.txt","r")

                            for line1 in f1:
                                for line2 in f2:
                                    if line1==line2:
                                        while repcor :
                                            suppr = input("Le fichier",file, "contient un virus, voulez vous supprimez ce fichier? (oui/non)")
                                            if suppr == "oui":
                                                print("Suppression du fichier")
                                                #os.remove(file)
                                                repcor = False
                                                break
                                            if suppr == "non":
                                                print("Fichier conservé")
                                                repcor = False
                                            else:
                                                print("Veuillez écrire oui ou non !")
                                    else :
                                        print(file)

                            f1.close()
                            f2.close()
                            
                    
    else :
                        hasher = hashlib.sha256()
                        with open(fichier, 'rb') as afile:
                            buf = afile.read(BLOCKSIZE)
                            while len(buf) > 0:
                    
                                hasher.update(buf)
                                buf = afile.read(BLOCKSIZE)
                            mon_hash = open("hash.txt","w")
                            
                            mon_hash.write(hasher.hexdigest())
                            mon_hash.close()
                


            
                            f1=open("hash.txt","r")
                            f2=open("basededonnee.txt","r")

                            for line1 in f1:
                                for line2 in f2:
                                    if line1==line2:
                                        while repcor :
                                                suppr = input("Le fichier contient un virus, voulez vous supprimez ce fichier? (oui/non)")
                                                if suppr == "oui":
                                                        print("Suppression du fichier")
                                                        #os.remove(file)
                                                        repcor = False
                                                        break
                                                if suppr == "non":
                                                        print("Fichier conservé")
                                                        repcor = False
                                                else:
                                                        print("Veuillez écrire oui ou non!")
                                    else:
                                        print(fichier)
            
                            f1.close()

                            f2.close()



except FileNotFoundError :
    print("Analyse impossible : Ce fichier/dossier n'existe pas")
    
