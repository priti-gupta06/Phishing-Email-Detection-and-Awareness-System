# Phishing-Email-Detection-and-Awareness-System

## 1. Project Overview

The Phishing Email Detection & Awareness System is a Python-based cybersecurity project designed to identify potentially malicious and suspicious emails.
The system combines Rule-Based Detection and Machine Learning techniques to analyze email content, identify suspicious keywords and links, classify emails, and provide a risk score.
The main objective is to create awareness about phishing attacks and help users recognize potentially dangerous emails.

## 2. Project Objectives

- Identify phishing and legitimate emails.
- Detect suspicious keywords and URLs.
- Apply text preprocessing techniques.
- Train a Machine Learning classification model.
- Calculate an indicative email risk score.
- Provide an easy-to-use web interface.
- Promote cybersecurity awareness.

## 3. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming |
| Pandas | Dataset handling |
| Regular Expressions | Text cleaning and URL detection |
| Scikit-learn | Machine Learning |
| TF-IDF | Text feature extraction |
| Logistic Regression | Email classification |
| Flask | Web application |
| HTML and CSS | Frontend development |
| Pickle | Saving trained model files |
| VS Code | Development environment |
 
## 4. Project Features

1. **Email Preprocessing:** Converts text into lowercase, removes URLs, email addresses, special characters, and unnecessary spaces.
2. **Rule-Based Detection:** Identifies suspicious words such as urgent, verify, password, suspended, and claim.
3. **Machine Learning Classification:** Uses TF-IDF and Logistic Regression to classify email text.
4. **Risk Score:** Generates an indicative risk score using the model probability and rule-based indicators.
5. **Email Analysis Dashboard:** Allows users to enter email messages and view analysis results.
6. **Security Awareness:** Helps users understand common phishing indicators.

## 5. Project Structure

```text
Phishing-Email-Detection-System/
│
├── dataset/
│   ├── emails.csv
│   └── cleaned_emails.csv
│
├── model/
│   ├── phishing_model.pkl
│   └── tfidf_vectorizer.pkl
│
├── templates/
│   └── index.html
│
├── static/
│
├── venv/
│
├── app.py
├── preprocess.py
├── rules.py
├── train_model.py
├── requirements.txt
└── README.md
```

## 6. How the System Works

1. The user enters an email message.
2. The application preprocesses the email text.
3. The Rule-Based Detection module checks suspicious keywords and links.
4. The TF-IDF vectorizer converts email text into numerical features.
5. The Logistic Regression model predicts the email category.
6. The system combines the model and rule-based signals.
7. The dashboard displays the classification, risk score, and suspicious indicators.

## 7. Machine Learning Approach

The project uses:

- TF-IDF (Term Frequency–Inverse Document Frequency) for text feature extraction.
- Logistic Regression for binary classification.
- Training and testing data split for model evaluation.
- Accuracy, Precision, Recall, F1-score, and Confusion Matrix for evaluation.

## 8. Installation and Execution

### Requirements

- Python
- Visual Studio Code
- Required Python libraries

Install the libraries using:

```bash
pip install pandas scikit-learn matplotlib flask nltk seaborn
```

### Run the project

1. Open the project folder in VS Code.
2. Activate the Python virtual environment.
3. Run `preprocess.py`.
4. Run `train_model.py`.
5. Run `app.py`.
6. Open `http://127.0.0.1:5000` in your browser.

## 9. Initial Testing

The initial dataset contains 20 sample email records:

- 10 phishing examples.
- 10 legitimate examples.

The initial model achieved 100% accuracy on its five-email test split.

**Important limitation:** This is a very small demonstration dataset. The result does not establish real-world detection accuracy or reliability. A larger, independently sourced and representative dataset is required for meaningful evaluation.

## 10. Future Enhancements

- Integrate larger real-world phishing email datasets.
- Improve model generalization and evaluation.
- Add email sender and domain analysis.
- Introduce advanced URL analysis.
- Improve false-positive and false-negative detection.
- Add downloadable analysis reports.
- Improve the dashboard and user experience.
- Explore more advanced Machine Learning and NLP techniques.

## 11. Conclusion

This project demonstrates how Python, Machine Learning, text processing, and web development can be combined to create a basic phishing email detection application.
It provided practical experience in cybersecurity concepts, dataset preparation, model training, model evaluation, and Flask application development.
