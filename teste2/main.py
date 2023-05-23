import tabula
import csv
import zipfile
import os

# using the pdf that we download 
# with the script of the first test
pdf_path = 'anexo1.pdf'

# convert the table into a csv file
tabula.convert_into(pdf_path, 'table.csv', output_format='csv', pages='all')

# removing the description of table
# that are already in the first line
desc_row = ['PROCEDIMENTO', 'RN\n(alteração)', 'VIGÊNCIA', 'OD', 'AMB', 'HCO', 'HSO', 'REF', 'PAC', 'DUT', 'SUBGRUPO', 'GRUPO', 'CAPÍTULO']

in_file = open("table.csv", "r")
with open("main_table.csv", "w", newline="") as csvfile:

    in_csv = csv.reader(in_file)
    out_csv = csv.writer(csvfile)

    for row_number, row in enumerate(in_csv):
        # doing a new file that doenst 
        # have the description row
        # more than once
        if row != desc_row or row_number == 0: 
            row_aux = []
            # desafio bonus
            for r in row:
                if(r == 'AMB'): 
                    print("substituir por Seg. Ambulatorial")
                    r = 'Seg. Ambulatorial'
                    
                if(r == 'OD'):
                    print("substituir por Seg. Odontologica")
                    r ='Seg. Odontologica'
                
                row_aux.append(r)
                    
            out_csv.writerow(row_aux)

# closing the file
in_file.close()


# Creating the zip file
meu_nome = 'Felipe_Teles'
zip = zipfile.ZipFile(f'Teste_{meu_nome}.zip', 'w', zipfile.ZIP_DEFLATED)

zip.write("main_table.csv")

# deleting the unused files
os.remove("table.csv")
os.remove("main_table.csv")