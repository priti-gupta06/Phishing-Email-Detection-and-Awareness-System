from flask import Flask, render_template, request
import pickle

from rules import detect_phishing
from preprocess import clean_email

app = Flask(__name__)

# Load trained ML model
with open("model/phishing_model.pkl", "rb") as file:
    model = pickle.load(file)

# Load TF-IDF vectorizer
with open("model/tfidf_vectorizer.pkl", "rb") as file:
    vectorizer = pickle.load(file)


@app.route("/", methods=["GET", "POST"])
def home():

    result = None

    if request.method == "POST":

        email_text = request.form.get("email", "").strip()

        if email_text:

            # Clean email
            cleaned_email = clean_email(email_text)

            # ML prediction
            email_vector = vectorizer.transform([cleaned_email])
            prediction = model.predict(email_vector)[0]

            probability = model.predict_proba(email_vector)[0][1]
            ml_score = round(probability * 100)

            # Rule-based detection
            rule_result = detect_phishing(email_text)

            # Combine both signals
            risk_score = max(ml_score, rule_result["risk_score"])

            if prediction == 1 or rule_result["result"] == "PHISHING":
                classification = "PHISHING"
            else:
                classification = "LEGITIMATE"

            result = {
                "classification": classification,
                "risk_score": risk_score,
                "suspicious_words": rule_result["suspicious_words"],
                "suspicious_links": rule_result["suspicious_links"]
            }

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)