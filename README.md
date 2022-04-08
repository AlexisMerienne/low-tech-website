# low-tech-website
Un essai pour refaire le site de présentation du groupe de travail CO2 i3s sous un design sobre

Disponible ici : https://i3s-gt-co2.netlify.app

<hr>
#### Quelques chiffres : 
    
    Taille du site actuelle disponible sur le site d'i3S : 2,05 Mo
    
    Taille de cette version :  442 Ko
           - images : 415 Ko
           - fichiers html : 27,84 Ko
           
    Réduction : 1,61 Mo soit 80% du site initiale
   
<hr>

##### Auteur :

    - Alexis Mérienne
    
    
## Documentation : 

    1. Structure du repo
    2. Ajouter / modifier le contenu du site
    3. Deployer le site sur netlify
    

<hr>


### I. Structure du projet





Le projet est composé de deux dossiers principaux : 

    output : qui contient les fichiers de notres site
    src: qui contient la partie nécessaire à la construction du site
    
**output** est le site tel qu'il est déployé sur le serveur : 

    Sa structure est la suivante :
    
        - home.html
        - views
            - actualite.html
            - bilancarbone.html
            - enquete.html
        assets 
            - main.css
            - //toutes les images du site
            
    home.html est le fichier à la racine, il correspond à la page 'à propos' qui présente les membres du groupe CO2
    
    
**src** est le dossier dans lequel on va modifier le contenu du site. Il contient par ailleurs les scripts nécessaire au build. 
    
    Sa structure est la suivante : 
        - content
            - actualites
                - template
                - [ACTUALITE_1].md
                .
                .
                .
                - [ACTUALITE_N].md
            - apropos
                - template
                - content.md
            - bilancarbone
                - template
                - content.md
            - enquete
                - template
                - content.md
        engine
            //Quelques fichiers pythons pour construire le site
        images
            [image_1].jpg
            .
            .
            .
            [image_n].jpg
            
 <hr>
 
 

### II. Modifier / créer le contenu du site

Le contenu est stocké dans le dossier **content** au format Markdown.  
Il y a deux différents cas pour créer du contenu sur le site :

    - Ajouter une actualité
    - Ajouter du texte dans 'à propos', 'bilan carbone', 'enquête'
    
#### A. Ajouter une actualité

    Pour ajouter une actualité, il est nécessaire d'ajouter un fichier Markdown dans le dossier content/actualite en suivant ces indications : 
        - Le nom du fichier est la date de création de celui-ci au format : YYYY_MM_DD.md
        - Le fichier doit strictement avoir la structure spécifiée ci-dessous : 
-
       #### Date : Titre
                
       Le contenu de l'actualité
       
#### B. Ajouter du texte dans dans 'à propos', 'bilan carbone' ou 'enquête'

    Il suffit de modifier les fichier Markdown 'content.md' des dossiers respectifs.
    
    Quelques rappels sur la syntaxes Markdown:
        Pour écrire un titre :  # Gros titre
                                ## Moyen titre
                                ### Petit titre
        Pour ajouter un lien : [mon contenu](le lien)
        
    Pour ajouter une image, il faut l'enregistrer dans le dossier images au format JPEG, puis dans le fichier Markdown, l'ajouter avec la syntaxe suivante :
    
           ![titre de l'image](../assets/monimage.jpeg)
           
    /!\ Il faut spécifier le chemin d'accès :  "../assets/monimage.jpeg". En effet, le script de build va déplacer l'image dans un dossier assets qui sera accessible par les fichie html générés. 
    
    
Un fois que l'on a effectuer tous les changements que l'on souhaite, il faut convertir les fichier Markdown en html. C'est le script **buid.py** qui s'en occupe. 
Il suffit donc de lancer la commande : 

    python build.py

Les dépendances nécessaires sont :

    pip install markdown
    pip install BeautifulSoup
    pip install Pillow
    
<hr>


### III. Déployer sur netlify 

Pour déployer le site, il faut d'abord le construire dans output. Le script **deploy.py** permet met à jour le dossier output avec les nouvelles versions des fichiers html. 

    python deploy.py
    
Dépendances : 

    pip install shutil
    
Enfin, le déploiment sur netlify se fait automatiquement depuis Github à chaque fois que l'on push sur ce repo à la branche ***main***
    
