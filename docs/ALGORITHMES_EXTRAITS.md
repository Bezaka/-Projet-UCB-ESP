# Extraction des Algorithmes UCB et EXP3

## 1. ALGORITHME UCB1 (Upper Confidence Bound)

### Formule Principale
**Indice de confiance supérieur (UCB) :**

$$I_i(n) = \hat{\mu}_i + \sqrt{\frac{2\ln(n)}{n_i}}$$

Où :
- $\hat{\mu}_i$ = moyenne estimée des récompenses du bras $i$
- $n$ = nombre total d'itérations
- $n_i$ = nombre de fois où le bras $i$ a été sélectionné
- Le terme $\sqrt{\frac{2\ln(n)}{n_i}}$ représente l'intervalle de confiance

### Paramètres Clés
- **k** : nombre de bras (stratégies disponibles)
- **n** : nombre total d'itérations
- **$n_i$** : compteur du bras sélectionné
- **$\hat{\mu}_i$** : moyenne estimée des récompenses du bras $i$
- **$G_n$** : gain cumulé

### Étapes de l'Algorithme

1. **Initialisation** : Mesurer chaque bras au moins une fois

2. **Boucle principale** : Tant que le seuil n'est pas atteint (TH_n × n)

3. **Pour chaque bras i** (de 1 à k) :

4. **Calculer l'UCB** : 
   $$I_i(n) = \hat{\mu}_i + \sqrt{\frac{2\ln(n)}{n_i}}$$

5. **Sélectionner le bras optimal** : 
   $$j = \arg\max_i(I_i(n))$$
   (Le bras avec le plus grand indice UCB)

6. **Observer la récompense** : 
   $$r_j = \text{reward}(j)$$

7. **Mettre à jour la moyenne estimée** du bras choisi :
   $$\hat{\mu}_j(n) = \hat{\mu}_{j}(n-1) + \frac{1}{n_j}(r_j - \hat{\mu}_{j}(n-1))$$

8. **Mettre à jour le gain cumulé** :
   $$G_n = G_{n-1} + r_j$$

9. **Incrémenter le compteur du bras sélectionné** :
   $$n_j = n_j + 1$$

10. **Incrémenter le nombre total d'itérations** :
    $$n = n + 1$$

---

## 2. ALGORITHME EXP3 (Exponential-weight algorithm for Exploration and Exploitation)

### Formule Principale

**Mise à jour des poids :**

$$w_a^{(t+1)} = w_a^{(t)} \exp\left(\eta \frac{\hat{r}_a^{(t)}}{K \cdot p_a^{(t)}}\right)$$

**Distribution des stratégies :**

$$p_a^{(t+1)} = \frac{1}{K+1} + \left(1 - \frac{1}{K}\right) \frac{w_a^{(t+1)}}{\sum_{a' \in A} w_{a'}^{(t+1)}}$$

### Paramètres Clés
- **A** : ensemble des stratégies/actions disponibles
- **K** : nombre d'actions disponibles (|A|)
- **$w_a(t)$** : poids de la stratégie $a$ à l'instant $t$
- **$p_a(t)$** : probabilité de sélectionner la stratégie $a$ à l'instant $t$
- **T** : nombre total d'itérations
- **e** : base du logarithme naturel (≈ 2.7182)
- **$\eta$** : taux d'apprentissage (learning rate)

### Calcul du Taux d'Apprentissage

$$\eta = \min\left\{1, \sqrt{\frac{\log(K)}{(K-1)T}}\right\}$$

### Étapes de l'Algorithme

1. **Initialisation** :
   - Sélectionner une stratégie $a_j \in A$ pour chaque dispositif $j$
   - Initialiser les poids : $w_a^{(0)} = 1$ pour tout $a \in A$
   - Initialiser pour chaque dispositif $j$ : nombre $N_j$ et distribution uniforme des stratégies
   - Calculer le taux d'apprentissage :
     $$\eta = \min\left\{1, \sqrt{\frac{\log(K)}{(K-1)T}}\right\}$$

2. **Pour chaque instant $t = 1$ à $T$** :

3. **Initialisation de l'itération courante**

4. **Pour chaque dispositif terminal $j$** :

   a. **À l'instant $t$, tirer une stratégie** $a \in A$ selon la distribution $p_a^{(t)}$

   b. **Si transmission réussie** :
      
      - **Recevoir la récompense** :
        $$r_a^{(t)} = \begin{cases} 1 & \text{si un ACK est reçu} \\ 0 & \text{sinon} \end{cases}$$

      - **Mettre à jour les poids** :
        $$w_a^{(t+1)} = w_a^{(t)} \exp\left(\eta \frac{\hat{r}_a^{(t)}}{K \cdot p_a^{(t)}}\right)$$

      - **Mettre à jour la distribution des stratégies** :
        $$p_a^{(t+1)} = \frac{1}{K+1} + \left(1 - \frac{1}{K}\right) \frac{w_a^{(t+1)}}{\sum_{a' \in A} w_{a'}^{(t+1)}}$$

---

## 3. COMPARAISON ENTRE UCB ET EXP3

| Critère | UCB1 | EXP3 |
|---------|------|------|
| **Type d'algorithme** | Déterministe (greedy + optimisme) | Probabiliste (exploration-exploitation) |
| **Sélection du bras** | Sélection déterministe du max UCB | Tirage aléatoire selon distribution |
| **Exploration** | Via l'intervalle de confiance $\sqrt{\frac{2\ln(n)}{n_i}}$ | Via la distribution probabiliste uniforme partielle |
| **Exploitation** | Favorise les bras avec haute moyenne | Favorise les stratégies avec hauts poids |
| **Mise à jour** | Moyenne empirique simple | Poids exponentiels (multiplicatif) |
| **Complexité** | Faible complexité computationnelle | Complexité modérée (calcul exponentiel) |
| **Convergence** | Regret logarithmique optimal | Regret théoriquement borné en $O(\sqrt{T \log K})$ |
| **Adaptation** | Lente adaptation aux changements | Adaptation plus rapide via poids exponentiels |
| **Contexte d'utilisation** | Stationnaire, exploration progressive | Dynamique, sensible aux récompenses récentes |
| **Initialisation** | Chaque bras testé au moins une fois | Poids uniformes, distribution initiale uniforme |

### Différences Clés

1. **Stratégie d'exploration-exploitation** :
   - **UCB** : Optimiste - ajoute un bonus d'exploration décroissant aux bras sous-explorés
   - **EXP3** : Probabiliste - maintient une distribution de probabilité sur toutes les actions

2. **Déterminisme** :
   - **UCB** : Complètement déterministe (sauf en cas d'égalité)
   - **EXP3** : Stochastique, utilise des tirages aléatoires

3. **Sensibilité aux récompenses** :
   - **UCB** : Utilise la moyenne empirique (historique complet)
   - **EXP3** : Donne plus de poids aux récompenses récentes (exponentiel)

4. **Taux d'apprentissage** :
   - **UCB** : Pas de paramètre de taux d'apprentissage, adaptatif naturellement
   - **EXP3** : Taux d'apprentissage $\eta$ qui dépend de T et K

5. **Applicabilité** :
   - **UCB** : Problèmes stationnaires, contextes avec peu de récompenses
   - **EXP3** : Environnements adversariels, comportement d'exploration adaptatif nécessaire

---

## Notes Mathématiques

### UCB - Justification Théorique
L'indice UCB $(I_i)$ combine deux termes :
1. **Exploitation** : $\hat{\mu}_i$ (moyenne estimée)
2. **Exploration** : $\sqrt{\frac{2\ln(n)}{n_i}}$ (confiance dans les bras peu testés)

Ce compromis garantit un regret cumulatif de $O(\ln n)$ en moyenne.

### EXP3 - Justification Théorique
EXP3 utilise des poids exponentiels pour donner plus d'importance aux stratégies performantes :
- Le facteur $\eta$ contrôle la vitesse d'adaptation
- La probabilité minimale $\frac{1}{K+1}$ garantit l'exploration continue
- Le regret est borné en $O(\sqrt{TK \ln K})$ contre un adversaire arbitraire

