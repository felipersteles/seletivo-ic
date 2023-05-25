from flask import Flask
import csv

app = Flask(__name__)

# FINDING WORLD ---------------------------------

def find_word(word):
    in_file = open("table1.csv", "r")
    in_csv = csv.reader(in_file)
    
    finded = []
    
    for row_number, row in enumerate(in_csv):
        for r in row:
            if word in r :
                finded.append(str(row))


    # closing the file
    in_file.close()  
    return finded
    
# SERVER -----------------------------------
@app.route('/<word>')
def home(word):
    
    return find_word(word)

if __name__ == '__main__':
    app.run(debug=True)
