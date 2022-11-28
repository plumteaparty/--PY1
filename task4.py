import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename, delimiter=',', new_line='\n'):
    with open(filename) as f:
        table = []
        for i, l in enumerate(f):
            fields = l.strip(new_line).split(delimiter)
            if i == 0:
                heads = fields
                continue

            table.append({})

            for с, _ in enumerate(heads):
                table[-1][heads[с]] = fields[с]
    return table


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
