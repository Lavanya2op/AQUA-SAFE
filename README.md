# 💧 AQUA SAFE

### AI-Based *Naegleria fowleri* Risk Prediction System Using Water Quality Parameters

AQUA SAFE is a machine learning-based risk prediction system designed to estimate the potential presence of *Naegleria fowleri* in water based on important water quality parameters.

The system analyzes factors such as temperature, turbidity, dissolved oxygen, nitrate levels, and contaminant concentration to provide a risk prediction through an interactive Streamlit interface.

> **Note:** AQUA SAFE is an educational and predictive machine learning project. Its predictions should not be treated as a substitute for laboratory testing or professional water-quality assessment.

---

## 📌 About the Project

*Naegleria fowleri*, commonly known as the "brain-eating amoeba," is a free-living organism that can be found in certain warm freshwater environments.

AQUA SAFE explores how machine learning can be applied to environmental data to identify patterns associated with potential risk.

The project takes water-quality parameters as input, processes them using a trained machine learning model, and generates a risk prediction through a user-friendly web interface.

---

## ✨ Features

- 💧 Water quality-based risk prediction
- 🤖 Machine learning classification model
- 🌡️ Temperature-based analysis
- 🌫️ Turbidity analysis
- 🧪 Contaminant-level analysis
- 🫧 Dissolved oxygen analysis
- 🧬 Nitrate-level analysis
- 📊 Interactive Streamlit interface
- 🔄 Dynamic input parameters
- 📈 Data-driven risk assessment

---

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Pandas | Data processing |
| NumPy | Numerical computation |
| Scikit-learn | Machine learning |
| Random Forest | Classification model |
| Joblib | Model and scaler serialization |
| Streamlit | Web application interface |
| Jupyter Notebook | Model development and experimentation |
| Matplotlib | Data visualization |
| Seaborn | Exploratory data analysis |

---

## 📊 Input Parameters

AQUA SAFE uses multiple water-quality parameters for prediction.

| Parameter | Description |
|---|---|
| Water Source Type | Type/source of the water |
| Contaminant Level (ppm) | Concentration of contaminants |
| Turbidity (NTU) | Measurement of water clarity |
| Dissolved Oxygen (mg/L) | Amount of dissolved oxygen in water |
| Nitrate Level (mg/L) | Concentration of nitrates |
| Temperature (°C) | Water temperature |

These parameters are processed by the machine learning model to generate the final risk prediction.

---

## 🤖 Machine Learning Model

A **Random Forest Classifier** is used as the primary machine learning model.

Random Forest was selected because it can handle multiple input features and capture nonlinear relationships between water-quality parameters and the target classification.

### Machine Learning Workflow

```text
Water Quality Dataset
        ↓
Data Collection
        ↓
Data Cleaning
        ↓
Exploratory Data Analysis
        ↓
Feature Selection
        ↓
Data Preprocessing
        ↓
Feature Scaling
        ↓
Model Training
        ↓
Random Forest Classifier
        ↓
Model Evaluation
        ↓
Model Serialization
        ↓
Streamlit Application
        ↓
Risk Prediction
```

---

## 📂 Project Structure

```text
AQUA-SAFE/
│
├── app.py
├── model.pkl
├── scaler.pkl
├── requirements.txt
├── README.md
│
├── data/
│   └── dataset.csv
│
├── notebooks/
│   └── model_training.ipynb
│
└── assets/
    └── screenshots/
```

> The exact structure may vary depending on the files included in the repository.

---

## 🚀 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/AQUA-SAFE.git
```

### 2. Navigate to the Project

```bash
cd AQUA-SAFE
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

On macOS/Linux:

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Streamlit Application

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 🖥️ Application Workflow

The user enters the required water-quality parameters through the Streamlit interface.

```text
User Input
    ↓
Water Quality Parameters
    ↓
Data Preprocessing
    ↓
Trained Random Forest Model
    ↓
Prediction
    ↓
Risk Result
```

The interface is designed to make the prediction process simple and accessible without requiring the user to interact directly with the machine learning model.

---

## 🎯 Project Objectives

The primary objectives of AQUA SAFE are:

- To explore the application of machine learning in environmental monitoring.
- To analyze relationships between water-quality parameters and potential risk.
- To develop a predictive classification system.
- To provide an interactive interface for users.
- To demonstrate the complete machine learning pipeline from data preprocessing to deployment.

---

## 📈 Model Development

The model development process includes:

1. Data collection
2. Data preprocessing
3. Exploratory data analysis
4. Feature selection
5. Data transformation/scaling
6. Training the Random Forest classifier
7. Model evaluation
8. Saving the trained model using Joblib
9. Integrating the model with Streamlit

The trained model and preprocessing components can be loaded by the application to make predictions without retraining the model every time.

---

## 🔮 Future Scope

Future versions of AQUA SAFE could include:

- 🌐 Integration with real-time water-quality sensors
- 📡 IoT-based water monitoring
- 🗺️ Geographic risk mapping
- 📊 Real-time environmental dashboards
- 🤖 Comparison of multiple machine learning algorithms
- 📱 Mobile application integration
- ☁️ Cloud-based deployment
- 📈 Larger and more diverse datasets
- 🔔 Automated alerts for potentially high-risk conditions

---

## ⚠️ Disclaimer

AQUA SAFE is developed as an academic and machine learning project for educational and research purposes.

The system provides **model-based risk predictions**, not medical, environmental, or laboratory confirmation. Actual detection of *Naegleria fowleri* requires appropriate laboratory testing and professional assessment.

---

## 👩‍💻 Author

**Lavanya Rathi**

B.Tech Computer Science  
MIT ADT University, Pune
