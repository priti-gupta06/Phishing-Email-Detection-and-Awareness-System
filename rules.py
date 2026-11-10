import re

# Suspicious words commonly found in phishing emails
SUSPICIOUS_WORDS = [
    "urgent",
    "verify",
    "password",
    "suspended",
    "blocked",
    "immediately",
    "winner",
    "lottery",
    "claim",
    "free",
    "click here",
    "bank account",
    "prize",
    "refund",
    "confirm"
]


def detect_phishing(email_text):

    text = email_text.lower()

    found_words = []

    # Check suspicious words
    for word in SUSPICIOUS_WORDS:
        if word in text:
            found_words.append(word)

    # Check suspicious links
    links = re.findall(r'https?://\S+|www\.\S+', text)

    # Calculate risk score
    score = len(found_words) * 10

    if links:
        score += 20

    # Maximum score is 100
    score = min(score, 100)

    # Classify email
    if score >= 30:
        result = "PHISHING"
    else:
        result = "LEGITIMATE"

    return {
        "result": result,
        "risk_score": score,
        "suspicious_words": found_words,
        "suspicious_links": links
    }


# Test the detection system
sample_email = "URGENT! Your bank account is suspended. Verify your password immediately!"

output = detect_phishing(sample_email)

print("Email Classification:", output["result"])
print("Risk Score:", output["risk_score"], "%")
print("Suspicious Words:", output["suspicious_words"])
print("Suspicious Links:", output["suspicious_links"])