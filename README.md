# low-tech-website
Un essai pour refaire le site de présentation du groupe de travail CO2 i3s sous un design sobre

##### Auteur :

    - Alexis Mérienne
    
    
### Documentation : 

    1. Structure du repo
    2. Ajouter / modifier le contenu du site
    3. Deployer le site sur netlify
    
    
#### I. Structure du projet


Le projet est composé de deux dossiers principaux : 

    output : qui contient les fichiers de notres site
    src: qui contient la partie nécessaire à la construction du site
    
 Output est le site tel qu'il est déployer sur le serveur : 

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
    
    
src est le dossier dans lequel on va modifier le contenu du site. Il contient par ailleurs les scripts nécessaire au build. 
    
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
            
            
                

    
