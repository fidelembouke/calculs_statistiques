# Mean-Variance-Standard Deviation Calculator

Ce projet permet de calculer la moyenne, la variance, l'écart-type, le maximum, le minimum et la somme pour une liste de neuf nombres. Le programme est structuré pour accepter une liste, la convertir en matrice 3x3, et effectuer les calculs de manière efficace, le but étant de renvoyer un dictionnaire contenant la moyenne, la variance, l'écart type, le maximum, le minimum et la somme le long des deux axes et pour la matrice aplatie. Un résultat attendu se préenterait sous cette forme:

{
  'mean': [axis1, axis2, flattened],
  'variance': [axis1, axis2, flattened],
  'standard deviation': [axis1, axis2, flattened],
  'max': [axis1, axis2, flattened],
  'min': [axis1, axis2, flattened],
  'sum': [axis1, axis2, flattened]
}

Ce projet est constitué de 3 fichiers principaux: mean_var_std contient la fonction principale nécessaire aux différents calculs, main.py contient les éléments permettant d'exécuter notre fichier principale et test.module.py est le fichier de test permettant de s'assurer que  les éléments requis concernant le cahier de charge ont bien été respectés.
