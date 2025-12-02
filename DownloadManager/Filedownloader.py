import requests

url = "https://raw.githubusercontent.com/sharmadhiraj/free-json-datasets/master/datasets/nobel-prize-winners-by-year.json"
output_file = "/Users/arun/Desktop/DEP/Data/Sourcedata/nobel.json"

response = requests.get(url)

if response.status_code == 200:
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(response.text)  # <-- fixed indentation
    print("File downloaded successfully:", output_file)
else:
    print("Failed to download. Status code:", response.status_code)
