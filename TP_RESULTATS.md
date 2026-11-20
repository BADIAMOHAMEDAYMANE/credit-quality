# Résultats du TP — Qualité du code et tests unitaires

## Exercice 1 — Tableau de comparaison

| Indicateur | Avant | Après |
|---|---|---|
| Problèmes de fiabilité | À renseigner avec la capture SonarQube | À renseigner après relance |
| Problèmes de sécurité | À renseigner avec la capture SonarQube | À renseigner après relance |
| Problèmes de maintenabilité | Imports inutiles, duplication, fonction dupliquée | Imports inutiles retirés, duplicata retiré |
| Duplication | `calculate_risk` et `calculate_risk2` dupliquées | Aucune duplication dans `credit.py` |
| Quality Gate | À renseigner après analyse | À renseigner après relance |

## Exercice 1 — Questions

1. **Bug / Code Smell** : un bug peut produire un comportement incorrect ou une défaillance à l'exécution. Un Code Smell est une faiblesse de conception ou de maintenance qui ne provoque pas forcément une erreur immédiate.
2. **Coût de la duplication** : modifier un comportement nécessite plusieurs changements synchronisés; les risques d'oubli, d'incohérence et de régression augmentent.
3. **Rôle du Quality Gate** : appliquer automatiquement des seuils de qualité pour décider si le projet est acceptable ou non.
4. **SonarScanner / SonarQube for IDE** : SonarScanner réalise une analyse centralisée du projet sur SonarQube Cloud. SonarQube for IDE analyse directement les fichiers ouverts dans VS Code.
5. **Pourquoi relancer l'analyse** : vérifier que les corrections ont réellement supprimé les problèmes et que aucune nouvelle anomalie n'a été introduite.

## Exercice 2 — Tests ajoutés

Les tests couvrent les cas normaux, les revenus nul et négatif, la dette nulle et les seuils exacts de 0,3 et 0,6.

## Exercice 2 — Questions

1. `assert` vérifie qu'une valeur obtenue respecte le résultat attendu; une condition fausse fait échouer le test.
2. PASS signifie que toutes les assertions du test sont vraies. FAIL signifie qu'au moins une assertion échoue ou que le test rencontre une erreur.
3. Les valeurs limites permettent de tester la bonne application des opérateurs stricts ou inclusifs et les seuils de décision.
4. Non, une couverture à 100 % montre que les lignes sont exécutées, pas que tous les scénarios, erreurs ou assertions sont pertinents.
5. pytest exécute les tests unitaires et vérifie le comportement. SonarQube analyse statiquement la qualité, les anomalies, la dette technique et les seuils de qualité.

## Exercice 2 — Partie C : détection d'erreurs

Après remplacement de `> 0.6` par `> 0.8`, le test avec 700 de dette échoue : la fonction retourne `MEDIUM` au lieu de `HIGH`. Le test à 400 reste `MEDIUM`, et le seuil exact de 0,6 reste `MEDIUM`, donc ils ne détectent pas tous les seuils incorrects. Ce résultat montre qu'un test supplémentaire au-dessus de 0,8 (par exemple 900) permettrait de vérifier aussi complètement le nouveau seuil.
