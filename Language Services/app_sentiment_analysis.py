"""
This script demonstrates how to use Azure's Text Analytics API to analyze the sentiment of text documents. 
It requires the `azure-ai-textanalytics` and `azure-core` Python packages. 
You need to provide your Azure Text Analytics endpoint and API key as placeholders.

Requirements:
- Install the required packages: `pip install azure-ai-textanalytics azure-core`
- Replace `<your_endpoint>` and `<your_api_key>` with your Azure Text Analytics endpoint and API key.
"""

from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

# Endpoint and API Key for Azure Text Analytics
# Replace these with your actual endpoint and key
endpoint = "https://mylangsvc.cognitiveservices.azure.com/"
key = "1YugXmvwrkEd9rKix64zselQYbNXeAMIFFg6x8YMUwFy3YyOqo2qJQQJ99BGACYeBjFXJ3w3AAAaACOGjhrw"

documents = [
    "I had a wonderful experience with the customer support team. They were friendly, helpful, and resolved my issue quickly. I will definitely recommend this service to others.",
    "The product quality is excellent, but the delivery was delayed and the packaging was damaged.",
    "I am extremely disappointed with the service. The staff was rude, and my problem is still unresolved."
]

credential = AzureKeyCredential(key)
client = TextAnalyticsClient(endpoint=endpoint, credential=credential)

response = client.analyze_sentiment(documents=documents)

for idx, doc in enumerate(response):
    if not doc.is_error:
        print(f"\nText: {documents[idx]}")
        print(f"\n\nSentiment: {doc.sentiment}")
        print(f"Confidence Scores: Positive={doc.confidence_scores.positive:.2f}, Neutral={doc.confidence_scores.neutral:.2f}, Negative={doc.confidence_scores.negative:.2f}")
    else:
        print(f"Error analyzing document {idx + 1}: {doc.error}")
