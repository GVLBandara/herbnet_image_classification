from flask import Flask, request, jsonify
from flask_cors import CORS

from img_classification import classification

app = Flask(__name__)

CORS(app)


@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return jsonify({'error': 'No file found'}), 400

    file = request.files['image']

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    file.save(file.filename)
    output = classification(file.filename)
    print(output)

    if output == 0:
        data = {
            "scientificName": "Senna alata",
            "englishName": "Candle Bush",
            "sinhalaName": "ඇත්තෝර",
            "url": "https://en.wikipedia.org/wiki/Senna_alata"
        }
    elif output == 1:
        data = {
            "scientificName": "Piper longum",
            "englishName": "Long Pepper",
            "sinhalaName": "තිප්පිලි",
            "url": "https://www.easyayurveda.com/2014/11/24/pippali-long-pepper-fruit-uses-dose-side-effects/"
        }
    elif output == 2:
        data = {
            "scientificName": "Acorus calamus",
            "englishName": "Sweet Flag",
            "sinhalaName": "වදකහ",
            "url": "https://www.easyayurveda.com/2015/01/06/vacha-acorus-calamus-uses-research-side-effects-remedy/"
        }
    elif output == 3:
        data = {
            "scientificName": "Stachytarpheta jamaicensis",
            "englishName": "Light blue snakeweed",
            "sinhalaName": "බලු නකුට",
            "url": "https://en.wikipedia.org/wiki/Stachytarpheta_jamaicensis"
        }
    elif output == 4:
        data = {
            "scientificName": "Polyscias fruticosa",
            "englishName": "Ming aralia",
            "sinhalaName": "කෝප්ප කොළ",
            "url": "https://en.wikipedia.org/wiki/Polyscias_fruticosa"
        }
    elif output == 5:
        data = {
            "scientificName": "Paederia foetida",
            "englishName": "Skunk vine",
            "sinhalaName": "ප්‍රසාරිණි",
            "url": "https://www.easyayurveda.com/2013/08/21/paederia-foetida-gandha-prasarini-benefits-usage-dose-side-effects/"
        }
    elif output == 6:
        data = {
            "scientificName": "Cardiospermum halicacabum",
            "englishName": "Balloon vine",
            "sinhalaName": "වැල් පෙනෙල",
            "url": "https://www.easyayurveda.com/2017/12/28/balloon-vine-cardiospermum-halicacabum-karnasphota/"
        }
    elif output == 7:
        data = {
            "scientificName": "Caesalpinia bonduc",
            "englishName": "Grey Nicker",
            "sinhalaName": "කුඹුරු",
            "url": "https://www.easyayurveda.com/2012/12/21/latakaranja-caesalpinia-bonduc-uses-ayurveda-details/"
        }
    else:
        data = {
            "scientificName": "Adhatoda vasica",
            "englishName": "Malabar nut",
            "sinhalaName": "පාවට්ටා",
            "url": "https://www.easyayurveda.com/2014/07/25/vasaka-adhatoda-vasica-uses-side-effects-research/"
        }

    data["id"] = int(output)
    return jsonify(data), 200


if __name__ == "__main__":
    app.run(debug=True)
