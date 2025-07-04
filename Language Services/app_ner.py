"""
This script demonstrates how to use Azure's Text Analytics API to perform Named Entity Recognition (NER) on a set of documents. 
It requires the `azure-ai-textanalytics` and `azure-core` Python packages. 
You need to provide your Azure Text Analytics endpoint and key as placeholders.

Requirements:
- Install the required packages: `pip install azure-ai-textanalytics`
- Replace `<your_endpoint>` and `<your_key>` with your Azure Text Analytics endpoint and key.
"""

from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

# Endpoint and API Key for Azure Text Analytics
# Replace these with your actual endpoint and key
endpoint = "https://mylangsvc.cognitiveservices.azure.com/"
key = "1YugXmvwrkEd9rKix64zselQYbNXeAMIFFg6x8YMUwFy3YyOqo2qJQQJ99BGACYeBjFXJ3w3AAAaACOGjhrw"

documents = [
    "Microsoft was founded by Bill Gates and Paul Allen in 1975. Its headquarters are located in Redmond, Washington.",
    "The Eiffel Tower, located in Paris, France, was designed by Gustave Eiffel and completed in 1889.",
    "John was prescribed 500 mg of Ibuprofen by Dr. Smith at Mayo Clinic."
]

credential = AzureKeyCredential(key)
client = TextAnalyticsClient(endpoint=endpoint, credential=credential)

response = client.recognize_entities(documents=documents)

for idx, doc in enumerate(response):
    print(f"\nText: {documents[idx]}")
    if not doc.is_error:
        print("\n\nNamed Entities:")
        for entity in doc.entities:
            print(f" - {entity.text} ({entity.category}, Confidence: {entity.confidence_score:.2f})")
    else:
        print(f"Error: {doc.error}")
