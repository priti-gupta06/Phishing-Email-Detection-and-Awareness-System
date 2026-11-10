
import re
import pandas as pd

def clean_email(text):
    text = text.lower()

    # Remove URLs
    text = re.sub(r'http\S+|www\S+', '', text)

    # Remove email addresses
    text = re.sub(r'\S+@\S+', '', text)

    # Remove special characters and numbers
    text = re.sub(r'[^a-z\s]', ' ', text)

    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text).strip()

    return text


# Load dataset
data = pd.read_csv("dataset/emails.csv")

# Clean email text
data["cleaned_email"] = data["email_text"].apply(clean_email)

# Display results
print(data[["email_text", "cleaned_email", "label"]].head(10))

# Save cleaned dataset
data.to_csv("dataset/cleaned_emails.csv", index=False)

print("\nEmail preprocessing completed successfully!")
