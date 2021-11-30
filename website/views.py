from flask import Blueprint, render_template, url_for, send_file, request

views = Blueprint('views', __name__)


@views.route("/", methods=["POST", "GET"])
def home():
  if request.method == 'POST':
    url = request.form.get("url")
    url += ".mp3?localembed=download"
    # page = requests.get(url).text
    # doc = BeautifulSoup(page, "html.parser")
    # download_button = doc.find(class_="player-download")
    # print(download_button)

    return render_template("home.html", url=url)
  
  return render_template("home.html")
