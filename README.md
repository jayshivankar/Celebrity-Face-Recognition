
![Screenshot from 2025-05-10 19-49-51](https://github.com/user-attachments/assets/37dae3ab-3563-4024-8f97-635b8563cf94)


# 🧠 Sports Personality Classification using Machine Learning

This project demonstrates a complete pipeline for building and deploying a **sports personality classification system** using machine learning and computer vision. The classification is restricted to five world-renowned sports figures:

- Maria Sharapova
- LeBron James
- Virat Kohli
- Roger Federer
- Cristiano Ronaldo

The final application is integrated with a simple web interface where users can upload an image, and the model will predict which of the five sports personalities is in the photo.

---


## ⚙️ Technologies & Libraries Used

### 🔧 Backend & Model Development
- **Python 3.x** – Core language
- **Jupyter Notebook** – For model prototyping and visualization
- **NumPy & OpenCV** – Image preprocessing and data cleaning
- **Matplotlib & Seaborn** – Data visualization
- **Scikit-learn** – Model training and evaluation
- **Flask** – Web server to expose the model as an HTTP API

### 🎨 Frontend Development
- **HTML/CSS/JavaScript** – UI design for uploading and displaying image predictions

### 🛠 Development Tools
- **Visual Studio Code / PyCharm** – IDEs for development
- **Jupyter Notebook** – For exploratory data analysis and modeling

---

## 📊 Model Overview

The project includes:
- **Image scraping** from Google using automated scripts to collect training data.
- **Image preprocessing** using OpenCV (resizing, grayscale/RGB conversion, normalization).
- **Exploratory data analysis (EDA)** using Matplotlib and Seaborn.
- **Model training** using Scikit-learn classifiers (e.g., SVM, KNN, Logistic Regression).
- **Evaluation metrics** like accuracy, confusion matrix, and classification reports.
- **Deployment** of the trained model with a Flask server that accepts images and returns predictions.

---

## 🚀 How to Run the Project

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/sports-personality-classifier.git
cd sports-personality-classifier
```
2. Set Up the Environment

Install the required packages:
```bash
pip install -r requirements.txt
```

3. Train the Model
Navigate to the model/ folder and open the Jupyter notebook to:

Load and preprocess the data

Train the model

Save the trained model to disk

4. Run the Flask Server
Navigate to the server/ directory and run:
```bash
python app.py
```

5. Launch the UI
Open the UI/index.html file in your browser. Upload an image to see the predicted personality.

