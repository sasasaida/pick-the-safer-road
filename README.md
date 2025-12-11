# 🚦 Safer Roads: Interactive Accident Risk Game & Explorer

An interactive **Streamlit** app that lets users explore road accident data and play a “Pick the Safer Road” game using a predictive model. This project demonstrates end-to-end **data exploration, model integration, and gamified UI** for predicting accident risk.

---

## 📋 Features

### 1. **Pick the Safer Road Game**

* Users compare **two randomly generated road segments**.
* Each road has features like **speed limit, number of lanes, curvature, road type, lighting, weather, and time of day**.
* A trained machine learning model predicts the **accident risk** for each road.
* Users pick which road they think is safer; the app shows the correct answer and updates their **score**.
* Provides **visual cards** for each road with styled display.

### 2. **Exploratory Data Analysis (EDA)**

* Interactive exploration of the **Kaggle accident dataset** (`train.csv`).
* Preview dataset rows and view **missing values**.
* Inspect **numeric columns** with summary statistics and histograms.
* Explore **categorical columns** with value counts and bar charts.

### 3. **Model Demo**

* A separate page allows users to input road features manually.
* Displays a predicted **accident risk score** for the entered road segment.
* Useful for testing and understanding how the model responds to different road conditions.

---

## 🛠️ Tech Stack

* **Python**
* **Streamlit** for interactive web app and UI
* **Pandas & NumPy** for data handling
* **Matplotlib & Streamlit charts** for visualization
* **Pickle** for loading the trained model

---

## 📂 Project Structure

```
Safer-Roads/
│
├─ data/
│   └─ train.csv            # Kaggle accident dataset
│
├─ utils/
│   └─ ml_utils.py          # Model loading & prediction helpers
│
├─ assets/
│   └─ styles.css           # Custom CSS for game cards
│
├─ 1_eda_explorer.py        # EDA Streamlit page
├─ 2_pick_the_safer_road.py # Main game app
├─ 3_model_demo.py          # Individual road prediction demo
├─ app.py                   # Landing page / hub
└─ README.md
```

---

## ⚡ How to Run

1. Clone the repository.
2. Create a Python virtual environment and install dependencies (`streamlit`, `pandas`, `numpy`, `matplotlib`, etc.).
3. Make sure the `train.csv` dataset is in the `data/` folder and your trained model is accessible via `utils/ml_utils.py`.
4. Run Streamlit apps:

   * Game: `2_pick_the_safer_road.py`
   * EDA: `1_eda_explorer.py`
   * Model demo: `3_model_demo.py`

---

## 🎮 Usage

* **Game Page**: Compare two roads → pick the safer one → see your score.
* **EDA Page**: Explore dataset → select numeric/categorical columns → view charts.
* **Model Demo**: Input road features → predict accident risk.

---

## ✨ UX Highlights

* Score tracker across rounds.
* Styled road cards for clear feature comparison.
* Immediate feedback for user guesses (correct/incorrect).
* Interactive charts and sliders for intuitive exploration.

---

## 🔧 Notes

* Randomly generated roads are **consistent per session** until the next round.
* Game uses a pre-trained model for **risk scoring**.
* Handles missing or extreme values gracefully in the UI.

---

## 📈 Potential Extensions

* Leaderboard to track top scores.
* Explainable feature importance per road prediction.
* Multiplayer mode with simultaneous guesses.

---
* **Kaggle Username:** `saidajahan`
* **Hosted App URL:** `https://pick-the-safer-road-effuegeb9rxn9dxguq5qcd.streamlit.app/`
* **Instructions:** Open the app → explore EDA → play “Pick the Safer Road” → submit guesses to see your score.

---
