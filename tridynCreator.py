import numpy as np

# === Paramètres ===
input_file = "profil.txt"   # ton fichier SRIM exporté
output_file = "tridyn.dat"
species = "Xe"              # type de cluster
size = 1                    # taille du cluster
flux_factor = 1.0           # facteur de flux
degree = 15                 # ordre du polynôme

# Lecture du fichier (Å, atome/cm3)
data = np.loadtxt(input_file)
depth_nm = data[:,0] * 0.1  # conversion Å → nm
conc = data[:,1]

# Tri par profondeur
order = np.argsort(depth_nm)
depth_nm = depth_nm[order]
conc = conc[order]

# Normalisation
area = np.trapezoid(conc, depth_nm)
conc_norm = conc / area if area != 0 else conc

# Ajustement polynôme (numpy.polyfit donne en ordre décroissant)
coeff_desc = np.polyfit(depth_nm, conc_norm, degree)
coeff_asc = coeff_desc[::-1]  # inversion pour ordre croissant

# Cutoff (ici profondeur max du fichier)
cutoff_nm = depth_nm.max()

# Écriture du fichier tridyn.dat
with open(output_file, "w") as f:
    f.write(f"{species} {size} {flux_factor}\n")
    coeff_str = " ".join(f"{c:.10e}" for c in coeff_asc)
    f.write(f"{coeff_str} {cutoff_nm:.2f}\n")

print(f"Fichier {output_file} généré.")
