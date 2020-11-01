import csv
import re

source = "C:\\Users\\brwor_x1n5u6n\\Downloads\\OPCOES.tsv"

destination = "C:\\Users\\brwor_x1n5u6n\\Downloads\\OPCOES_RESULT.tsv"

destination_sort = "C:\\Users\\brwor_x1n5u6n\\Downloads\\OPCOES_RESULT_SORT.tsv"

def extract_tsv(filename, encoding='utf-8'):
  with open(filename, encoding=encoding) as tsvfile:
    reader = csv.reader(tsvfile, delimiter='\t')
    rows = []
    for row in reader:      
      rows.append(row)
    return rows

def write_tsv(filename, rows, mode='w', encoding='utf-8', newline=''):
  with open(filename, mode=mode, encoding=encoding, newline=newline) as _file:
    employee_writer = csv.writer(_file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for row in rows:
      employee_writer.writerow(row)
  
def normalize_rows(rows, has_header = True):
  # result = [rows[0]] if has_header else []
  # rows_data = rows[1 if has_header else 0:]
  result = []
  rows_data = rows
  for row in rows_data:
    new_row = []
    for col in row:
      col = col.strip()
      col = re.sub(' +', ' ', col)
      new_row.append(col)        
    result.append(new_row)        
  return result

def translate_header(rows, translation_map):  
  header = rows[0]
  new_header = []
  for col in header:
    translation = translation_map[col]
    new_header.append(translation)
  rows[0] = new_header
  return rows

rows = extract_tsv(source)

rows = normalize_rows(rows)

translation_map = {
  "Data Negócio":	"date",
  "":	"blank",
  "C/V":	"action",	
  "Mercado":	"market",
  "Prazo":	"duedate",	
  "Código":	"code",	
  "Especificação do Ativo":	"specification",	
  "Quantidade":	"amount",	
  "Preço (R$)":	"price",	
  "Valor Total (R$)":	"total"
}

rows = translate_header(rows, translation_map)

write_tsv(destination, rows)

data = rows[1:]

sorted_list = sorted(data, key=lambda row: data[5], reverse=True)

write_tsv(destination_sort, sorted_list)

# print(f"file: {rows}")

