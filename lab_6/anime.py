from flask import Flask
from jikanpy import Jikan

jikan = Jikan()
app = Flask(__name__)

j = jikan.anime(54595, extension='episodes')

@app.route('/')
def home():
    output = "<h1>Список епізодів аніме:</h1>"
    for episode in j["data"]: 
        output += f"<p><b>Епізод {episode['mal_id']}:</b> {episode['title']} (Оцінка: {episode['score']})</p>"
    return output

if __name__ == '__main__':
    app.run(debug=True)