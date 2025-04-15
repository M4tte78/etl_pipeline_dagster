# 📊 Dagster ETL - Daily Market Recap

Un pipeline ETL complet utilisant **Dagster**, qui :

✅ Récupère les **prix journaliers** de 50 assets via `yfinance`  
✅ Calcule les **rendements journaliers**  
✅ Agrège les **actualités économiques simulées**  
✅ Génère un **rapport PDF** et une **version HTML interactive**  
✅ Planifie le tout avec **Dagster Schedule**

---

## 🚀 Lancer le projet

### 1. Cloner & installer les dépendances

```bash
git clone <repo-url>
cd etl_pipeline_dagster
python -m venv venv
venv\Scripts\activate       # sur Windows
pip install -r requirements.txt  # ou installer manuellement
```

### 2. Lancer Dagster

```bash
dagster dev
```

Puis ouvrir : http://localhost:3000

---

## ⚙️ Structure des assets

```
daily_prices       ← récupère les prix avec yfinance
daily_returns      ← calcule les rendements
daily_news         ← simule des actus du jour
market_pdf_report  ← génère un PDF avec fpdf + matplotlib
market_html_report ← génère une page HTML interactive
```

---

## 📁 Résultat

- 📄 PDF généré : `daily_market_report.pdf`
- 🌐 Page web : `public/market_report.html`
- 📊 Graphique : `top5_chart.png`

---

## 🔁 Planification

Une exécution automatique est définie via `@Schedule`, tous les jours à 8h UTC.

---

## 🧪 Tests

```bash
pytest tests/
```

---

## ✅ To-do (Bonus)

- [ ] Ajouter une vraie API pour les news
- [ ] Envoyer automatiquement le PDF par e-mail
- [ ] Publier le rapport sur un site statique (GitHub Pages / Netlify)

---
![image](https://github.com/user-attachments/assets/fd23b623-5f19-4786-85ff-74acabedc723)


Développé avec ❤️ par Mattéo Bailly
