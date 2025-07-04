"""
This script sends a question to an Azure Cognitive Services QnA Maker knowledge base and retrieves the best answer. 
It requires the following:
- An Azure Cognitive Services endpoint URL
- A valid subscription key for the QnA Maker service
- The project name and deployment name of the knowledge base
- The `requests` Python library installed (`pip install requests`)

Replace the placeholders with your specific values before running the script.
"""

"""
curl -X POST "https://mylangsvc.cognitiveservices.azure.com/language/:query-knowledgebases?projectName=my-test&api-version=2021-10-01&deploymentName=production" \
      -H "Ocp-Apim-Subscription-Key: 1YugXmvwrkEd9rKix64zselQYbNXeAMIFFg6x8YMUwFy3YyOqo2qJQQJ99BGACYeBjFXJ3w3AAAaACOGjhrw" \
      -H "Content-Type: application/json" \
       -d "{\"top\":3,\"question\":\"YOUR_QUESTION_HERE\",\"includeUnstructuredSources\":true,\"confidenceScoreThreshold\":\"YOUR_SCORE_THRESHOLD_HERE\",\"answerSpanRequest\":{\"enable\":true,\"topAnswersWithSpan\":1,\"confidenceScoreThreshold\":\"YOUR_SCORE_THRESHOLD_HERE\"},\"filters\":{\"metadataFilter\":{\"logicalOperation\":\"YOUR_LOGICAL_OPERATION_HERE\",\"metadata\":[{\"key\":\"YOUR_ADDITIONAL_PROP_KEY_HERE\",\"value\":\"YOUR_ADDITIONAL_PROP_VALUE_HERE\"}]}}}"

"""

import requests

endpoint = "https://mylangsvc.cognitiveservices.azure.com"
prediction_key = "1YugXmvwrkEd9rKix64zselQYbNXeAMIFFg6x8YMUwFy3YyOqo2qJQQJ99BGACYeBjFXJ3w3AAAaACOGjhrw"
project_name = "my-test"
deployment_name = "production"
question = "How are you?"

# https://mylangsvc.cognitiveservices.azure.com/language/:query-knowledgebases?projectName=my-test&api-version=2021-10-01&deploymentName=production
prediction_url = f"{endpoint}/language/:query-knowledgebases?projectName={project_name}&deploymentName={deployment_name}&api-version=2021-10-01"

headers = {
    "Ocp-Apim-Subscription-Key": prediction_key,
    "Content-Type": "application/json"
}

body = {
    "question": question,
    "top": 1
}

response = requests.post(prediction_url, headers=headers, json=body)

if response.status_code == 200:
    data = response.json()
    if data["answers"]:
        best_answer = data["answers"][0]
        print(f"Q: {question}")
        print(f"A: {best_answer['answer']}")
    else:
        print("No answers found.")
else:
    print(f"Request failed with status code {response.status_code}: {response.text}")
