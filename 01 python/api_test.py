import requests

try:
    response = requests.get(
        "https://api.github.com/repos/codeprassanna/software-and-ai-engineering",
        timeout=10
    )

    response.raise_for_status()

    data = response.json()

    print("Repository:", data["name"])
    print("Stars:", data["stargazers_count"])

except requests.exceptions.Timeout:
    print("The request took too long.")

except requests.exceptions.RequestException as error:
    print("API error:", error)