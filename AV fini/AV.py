import hashlib
import os
repcor = True
clean = True
BLOCKSIZE = 65536
def hasing(cwd):
    global clean, repcor
    
    hasher = hashlib.sha256()
    with open(str(cwd), 'rb') as afile:
        buf = afile.read(BLOCKSIZE)
        while len(buf) > 0:
                    
            hasher.update(buf)
            buf = afile.read(BLOCKSIZE)
        mon_hash = open("hash.txt","w")
                            
        mon_hash.write(hasher.hexdigest())
        mon_hash.close()
                
            
        f1=open("hash.txt","r")
        f2=open("bdd.txt","r")

        for line1 in f1:
            for line2 in f2:
                if line1==line2:
                    repcor = True
                    clean = False
                    while repcor :
                        suppr = input("Le fichier " + os.path.basename(cwd)+ " contient un virus, voulez vous supprimez ce fichier? (oui/non) \n")
                        if suppr == "oui":
                            print("Suppression du fichier")
                            afile.close()
                            os.remove(cwd)
                            repcor = False
                            break
                        if suppr == "non":
                            print("Fichier conservé")
                            repcor = False
                        else:
                            print("Veuillez écrire oui ou non !")
        f1.close()
        f2.close()

fichier = input("Entrez le chemin du fichier/dossier à analyser? \n")
try:
    if os.path.isdir(fichier):
        for root, directories, filenames in os.walk(fichier):
            for filename in filenames:
        
                path = os.path.dirname(filename)
                cwd = os.path.join(root, filename)
                hasing(cwd)
        if clean == True :
            print("Aucun virus detecté")
    else:
        hasing(fichier)
        if clean == True :
            print("Aucun virus detecté")
    print("Tous les fichiers ont étés traités")
except FileNotFoundError :
    print("Analyse impossible : Ce chemin de fichier/dossier n'existe pas")
