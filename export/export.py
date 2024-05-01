import json
import csv

def flatten_dict(d, parent_key='', sep='.'):
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

def export_to_csv(data, filename):
    keys = set()
    for entry in data:
        flattened_entry = flatten_dict(entry)
        keys.update(flattened_entry.keys())
    
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        
        writer.writerow(keys)
        
        for entry in data:
            flattened_entry = flatten_dict(entry)
            row = []
            for key in keys:
                value = flattened_entry.get(key, '')
                if isinstance(value, dict):
                    value = json.dumps(value)
                row.append(str(value))
            writer.writerow(row)
