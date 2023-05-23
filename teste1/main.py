import requests
from bs4 import BeautifulSoup
import zipfile
import os

# Config stuffs
url = 'https://www.gov.br/ans/pt-br/assuntos/consumidor/o-que-o-seu-plano-de-saude-deve-cobrir-1/o-que-e-o-rol-de-procedimentos-e-evento-em-saude'
header = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"}

# Initializing the scrapper object
site = requests.get(url, headers=header)
soup = BeautifulSoup(site.content,'html.parser')

# Find the target that 
# we want to download 
# using as the filter
# the type of element
# and after the content
elements = soup.find_all('a', {'class': 'internal-link'})
download_links = []
for el in elements:
    if 'Anexo' in el['href'] and 'pdf' in el['href']:
        download_links.append(el['href'])
        
        
# Creating the zip file
zip = zipfile.ZipFile('anexos.zip', 'w', zipfile.ZIP_DEFLATED)

# Downloading as a PDF file
# with a count to handle
# naming file
aux = 1
for link in download_links:
    print(f'Anexo {aux}:')
    print(link)
    print()
    
    path = f'anexo{aux}.pdf'
    
    with open(path, 'wb') as f:
        f.write(requests.get(link).content)
        
    # Afeter insert the file on zip
    # we remove it from system
    zip.write(path)
    os.remove(path)
    aux += 1