#Conversion de profils SRIM en fichiers tridyn.dat pour Xolotl

Ce script Python permet de convertir un profil d’implantation issu de SRIM (ou TRIM) en un fichier au format tridyn.dat compatible avec l’option fluxDepthProfileFilePath de Xolotl.

📄 Description

Entrée : fichier texte (profil.txt) contenant :

Colonne 1 : profondeur en Ångströms (Å)

Colonne 2 : concentration en atomes/cm³

Sortie : fichier tridyn.dat utilisable directement dans Xolotl.

Le script :

Convertit les profondeurs d’Å en nm.

Trie les données par profondeur croissante.

Normalise le profil de concentration pour que l’aire sous la courbe soit égale à 1.

Ajuste un polynôme d’ordre 15 sur le profil (Xolotl nécessite 15 coefficients).

Écrit un fichier tridyn.dat au format attendu :

<species> <size> <flux_factor>
a0 a1 a2 ... a15 cutoff_nm

📌 Paramètres à modifier

Dans le script, adaptez les variables suivantes à votre cas :

input_file = "profil.txt"   # Nom du fichier SRIM exporté
output_file = "tridyn.dat"  # Nom du fichier de sortie
species = "Xe"              # Espèce implantée (He, Xe, V, I etc.)
size = 1                    # Taille du cluster (1 pour monomère)
flux_factor = 1.0           # Facteur multiplicatif appliqué au flux global
degree = 15                 # Ordre du polynôme (15 recommandé pour Xolotl)

📥 Exemple d’utilisation

Exporter le profil depuis SRIM en 2 colonnes (profondeur, concentration).

Lancer le script :

python convert_srim_to_tridyn.py


Inclure le fichier tridyn.dat dans votre fichier .param Xolotl :

material = UO2
fluxDepthProfileFilePath = tridyn.dat
flux = 1.0e7


⚠️ Remarque sur flux_factor
Ce paramètre multiplie le flux global (flux dans le fichier .param).
Par exemple, si flux = 1e7 et flux_factor = 0.1, le flux effectif pour ce cluster sera 1e6.