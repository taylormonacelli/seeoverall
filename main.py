import pandas

url = "https://docs.cilium.io/en/stable/operations/system_requirements/#firewall-rules"
tables = pandas.read_html(url)
dataframes = []

for i, table in enumerate(tables):
    if not table.empty:
        dataframes.append(table)

json_data = [df.to_json(orient="records", indent=2) for df in dataframes]

for i, json_str in enumerate(json_data, 1):
    with open(f"table_{i}.json", "w") as file:
        file.write(json_str)
        print(f"Table {i} JSON data written to file.")
