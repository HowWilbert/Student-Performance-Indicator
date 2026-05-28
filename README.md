# Student Performance Predictor

A Machine Learning web application built using Flask that predicts a student's math score based on demographic and academic performance data.

---

# Features

- Predicts student math performance
- User-friendly web interface
- Machine Learning pipeline integration
- Data preprocessing and transformation
- Model training and prediction pipeline
- Flask-based deployment-ready application

---

# Tech Stack

- Python
- Flask
- Scikit-learn
- Pandas
- NumPy
- Matplotlib
- Seaborn
- HTML/CSS

---

# Dataset Information

- **Dataset Source:**  
  https://www.kaggle.com/datasets/spscientist/students-performance-in-exams

- **Dataset Size:**  
  - 1000 Rows
  - 8 Columns

## Features Used

| Feature | Description |
|---|---|
| gender | Male/Female |
| race_ethnicity | Ethnicity group |
| parental_level_of_education | Parent's education level |
| lunch | Standard or Free/Reduced |
| test_preparation_course | Completed or Not |
| reading_score | Reading exam marks |
| writing_score | Writing exam marks |

## Target Variable

- `math_score`

---

# Project Structure

```bash
Student-Performance-Predictor/
│
├── artifacts/                 
├── notebook/                  
├── src/                       
│   ├── components/            
│   ├── pipeline/              
│   ├── exception.py
│   ├── logger.py
│   └── utils.py
│
├── templates/                 
│   ├── index.html
│   └── home.html
│
├── app.py                     
├── requirements.txt
├── setup.py
└── README.md
```

---

# Exploratory Data Analysis (EDA)

## Data Checks Performed

- Missing value analysis
- Duplicate value analysis
- Data type validation
- Statistical analysis
- Feature distribution analysis
- Outlier detection
- Correlation analysis

---

# Key Insights from the Dataset

## General Insights

- No missing values found in the dataset.
- No duplicate values were present.
- The dataset contains:
  - 5 categorical features
  - 3 numerical features

---

## Academic Performance Insights

- Students performed worst in **Maths** compared to Reading and Writing.
- Reading scores showed the best overall performance.
- Most students scored between:
  - 60–80 in Maths
  - 50–80 in Reading/Writing

---

## Gender-Based Insights

- Female students generally performed better overall.
- Male students scored slightly higher in Maths.
- Gender distribution:
  - Female: 52%
  - Male: 48%

---

## Lunch-Based Insights

- Students with **standard lunch** performed better than students with free/reduced lunch.
- Standard lunch positively impacted performance across all subjects.

---

## Test Preparation Insights

- Students who completed the test preparation course scored higher on average.
- Most students did not complete the preparation course.

---

## Parental Education Insights

- Students whose parents had:
  - Master's degree
  - Bachelor's degree
  tended to perform better academically.

- However, parental education was not the dominant factor overall.

---

## Race/Ethnicity Insights

- Group E students achieved the highest average scores.
- Group A students showed the lowest average scores.

---

## Correlation Insights

- Reading, Writing, and Math scores are strongly linearly related.
- Higher reading and writing scores generally indicate higher math performance.

---

# Model Training

Several regression algorithms were trained and evaluated using the dataset.

## Models Used

- Linear Regression
- Lasso Regression
- Ridge Regression
- K-Neighbors Regressor
- Decision Tree Regressor
- Random Forest Regressor
- XGBoost Regressor
- CatBoost Regressor
- AdaBoost Regressor

---

# Model Performance

| Model | R² Score |
|---|---|
| Ridge Regression | 0.8805 |
| Linear Regression | 0.8804 |
| Random Forest Regressor | 0.8542 |
| CatBoost Regressor | 0.8498 |
| AdaBoost Regressor | 0.8474 |
| Lasso Regression | 0.8253 |
| XGBoost Regressor | 0.8250 |
| K-Neighbors Regressor | 0.7763 |
| Decision Tree Regressor | 0.7303 |

---

# Best Performing Model

## Ridge Regression

- **Accuracy:** 88.05%
- Achieved the highest R² Score among all tested models.
- Selected as the final model for deployment.

---

# Installation

## Clone the Repository

```bash
git clone https://github.com/HowWilbert/Student-Performance-Predictor.git
```

---

## Navigate to the Project Directory

```bash
cd Student-Performance-Predictor
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

---

## Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux/Mac

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Running the Application

Run the Flask server:

```bash
python app.py
```

Application will run at:

```bash
http://127.0.0.1:5000
```

---

# Deployment on Render

## Add Gunicorn

```bash
pip install gunicorn
```

---

## Render Start Command

```bash
gunicorn application:app
```

---

# Future Improvements

- Docker support
- Enhanced UI/UX
- Cloud optimization
- Real-time analytics dashboard

---

# Author

## Ansh Bire

- GitHub: https://github.com/HowWilbert

---

# License

This project is open-source and available under the MIT License.