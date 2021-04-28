import re

item_regex = "\d{3}\.\d{3}\.\d{2}"
item_query = re.compile(item_regex)


def try_int(item):
    try:
        return int(item)
    except:
        return None
        
legit_lines = []
current_item = None
with open("input.txt", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        items = line.split()
        
        if len(items) > 0:
            # mark current item.
            first = try_int(items[0])
            if first is None:
                current_item = line                
            else:
                item_count = str(first)
                match = item_query.search(line)
                string_idx, ikea_id = match.start(), match.group()
                desc_len = string_idx - len(str(item_count))
                item_name = line[len(str(item_count)):desc_len].strip()
                output_string = ",".join([ikea_id, item_count, item_name, current_item])                
                legit_lines.append(output_string)

legit_lines.sort()
for line in legit_lines:
    print(line)