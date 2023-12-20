import pandas as pd

# Lire le fichier Excel
donnees = pd.read_excel("C:/Users/julien.martinache/Downloads/bdd (1).xlsx")



# Calculer le nombre de lignes non nulles dans le DataFrame 'donnees'
nombre_lignes_non_nulles = donnees.dropna().shape[0]



colonnes_a_supprimer = ['fnlwgt', 'education-num']
donnees = donnees.drop(columns=colonnes_a_supprimer)





donnees = donnees[~((donnees['sex'] == 'Female') & (donnees['relationship'] == 'Husband'))]
donnees = donnees[~((donnees['sex'] == 'Male') & (donnees['relationship'] == 'Wife'))]




import pandas as pd

# Définir les bornes des tranches
bornes_tranches = [-float('inf'), 17, 26, 33, 41, 50, float('inf')]

# Définir les labels des tranches
tranches_labels = ['< 17', '[17,26[', '[26,33[', '[33, 41[', '[41,50[', '>50]']

# Utiliser pd.cut pour attribuer les labels aux tranches
donnees['tranches_age'] = pd.cut(donnees['age'], bins=bornes_tranches, labels=tranches_labels, right=False)


# Appliquer la condition et créer une nouvelle colonne 'hours-per-week-category'
donnees['hours-per-week'] = donnees['hours-per-week'].apply(lambda x: '>40' if x > 40 else '<40')




# Supposons que 'bdd' est votre DataFrame et 'capital-gain' est la colonne à modifier

# Utiliser apply avec une fonction lambda pour appliquer la condition
donnees['capital-gain'] = donnees['capital-gain'].apply(lambda x: 'gain' if x > 0 else 'pas_gain')




# Supposons que 'donnees' est votre DataFrame

# Utiliser apply avec une fonction lambda pour appliquer la condition et remplacer les valeurs dans la colonne 'capital-loss'
donnees['capital-loss'] = donnees['capital-loss'].apply(lambda x: 'perte' if x > 0 else 'pas_perte')




import pandas as pd

# Supposons que 'donnees' est votre DataFrame

# Remplacer toutes les valeurs positives dans 'workclass' par 'self_worker'
donnees['workclass'][(donnees['workclass'] == " Self-emp-not-inc") | (donnees['workclass'] == " Self-emp-inc")] = "self_worker"
donnees['workclass'][(donnees['workclass'] == "Never-worked") | (donnees['workclass'] == "Without-pay") | (donnees['workclass'] == "?") ] = "other"
donnees['workclass'][(donnees['workclass'] == " State-gov") | (donnees['workclass'] == " Federal-gov") | (donnees['workclass'] == " Local-gov")] = "gov"




donnees['occupation'][(donnees['occupation'] == " Exec-managerial") | (donnees['occupation'] == " Prof-specialty")] = "qualification_haute"
donnees['occupation'][(donnees['occupation'] == " Tech-support") | (donnees['occupation'] == " Adm-clerical") | (donnees['occupation'] == " Machine-op-inspct")| (donnees['occupation'] == " Farming-fishing") | (donnees['occupation'] == " Transport-moving") | (donnees['occupation'] == " Sales")] = "qualification_moyenne"
donnees['occupation'][(donnees['occupation'] == " Craft-repair") | (donnees['occupation'] == " Other-service") | (donnees['occupation'] == " Handlers-cleaners")| (donnees['occupation'] == " Priv-house-serv") | (donnees['occupation'] == " Protective-serv") | (donnees['occupation'] == " Armed-Forces")] = "qualification_faible"
donnees['occupation'][(donnees['occupation'] == " ?")] = "Autre catégorie"

donnees['education'][(donnees['education'] == " 11th") | (donnees['education'] == " HS-grad") | (donnees['education'] == " Some-college")| (donnees['education'] == " 9th") | (donnees['education'] == " 7th-8th") | (donnees['education'] == " 12th") | (donnees['education'] == " 5th-6th") | (donnees['education'] == " Preschool") | (donnees['education'] == " 1st-4th")| (donnees['education'] == " 10th")] = "primaire_secondaire"

donnees['education'][(donnees['education'] == " Bachelors") | (donnees['education'] == " Masters") | (donnees['education'] == " Doctorate")  | (donnees['education'] == " Prof-school")] = "niveau_superieur"

donnees['marital-status'][(donnees['marital-status'] == " Married-civ-spouse") | (donnees['marital-status'] == " Never-married") | (donnees['marital-status'] == " Married-spouse-absent")  | (donnees['marital-status'] == " Married-AF-spouse")] = "married"











