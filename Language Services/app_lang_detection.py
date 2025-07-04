from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
import json

# Endpoint
endpoint = "https://mylangsvc.cognitiveservices.azure.com/"
key = "1YugXmvwrkEd9rKix64zselQYbNXeAMIFFg6x8YMUwFy3YyOqo2qJQQJ99BGACYeBjFXJ3w3AAAaACOGjhrw"


input_texts = [
    "Bonjour tout le monde, je suis ravi de vous rencontrer.",
    "Hola, ¿cómo estás?",
  "مرحباً، كيف حالك؟",
  "ఎలా ఉన్నావు?"
]
credential = AzureKeyCredential(key)
client = TextAnalyticsClient(endpoint=endpoint, credential=credential)


response = client.detect_language(documents=input_texts)


print(json.dumps([doc.__dict__ for doc in response], indent=2, default=str))

for idx, doc in enumerate(response):
    if not doc.is_error:
        print(f"Text: {input_texts[idx]}")
        print(f"Detected Language: {doc.primary_language.name} (ISO: {doc.primary_language.iso6391_name}, Confidence: {doc.primary_language.confidence_score:.2f})\n")
    else:
        print(f"Error detecting language for doc {idx + 1}: {doc.error}")
