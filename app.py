from flask import Flask, render_template
from markupsafe import escape



app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/a-hluti")
def ahluti():
    return render_template('kennitala.html')

@app.route("/k-tala/<kt>")
def ktalan(kt):
    summa=0
    for item in kt:
        summa = summa + int(item)
    return render_template('ktsum.html',kt=kt,summa=summa)

@app.route("/b-hluti")
def bhluti():
    return render_template('frettir.html', frettir=frettir)

frettir = [
    ["0","Maðurinn man ekki hvað hann heitir","Það var maður niðrí Lágmúla sem mundi ekki hvað hann heitir. Það labbaði annar maður inn í vörugeymsluna og sagði 'hvað heitiru?'. maðurinn svaraði 'My name Jeff'. Það sem hafði gerst var að maðurinn gleymdi hvernig á að tala íslensku(hann skildi hana enþá) og hann gleymdi nafninu sínu fyrir utan að hann viss að 'Jeff' væri nafn svo hann sagði að það væri nafnið hans. sá maður er ég","Jeff Mwangi"],
    ["1","Köttur fastur upp í tré","Köttur að nafninu Grétar festist uppi í tré í miðbæ Reykjavíkur. Hann hafði fundið lykt af nýbökuðu Lasagna og hafði ákveðið að klifra upp tréð fyrir utan gluggann þar sem Lasagnað hafði verið búið til. Eins og sést hér á myndinni gekk það ekki vel og Grétar festist. Það að koma Grétari úr trénu var samt erfiðara sagt en gert vegna þess að hann myndi ekki fara án þess að fá smá bita af Lasagnanu, sem honum var gefið að lokum.","Þráinn Gunnlaugsson"],
    ["2","Er Þriðja heimstyrjöldinn að byrja????","Það er haldið að bandaríkinn gætu hafað byrjar þriðju heimsstyrjöldina. Það var gólf leikur milli forseta bandaríkjanna og forseta kína. Forseti bandaríkjanna vann leikinn auðveldlega lol og rústaði þessum kína manni. Forseti kína eftir þetta tap gerði stórt rant á twitter um hann og hótaði sprengjum. ","Jónas Jón Jónatansson"],
    ["3","Bílslys á reykjarvíkurveginum við miklubraut","Núna í morgun var bílslys á reykjarvíkurveginum við miklubraut. Það gerðist vegna bílstjóri var í símanum sínum og fór yfir á rauðu ljósi. Sá maður var að setja heimsmet í símatölvuleiknum Geometry dash á meðan hann var að keyra. það voru 3 meiddir í slysinu og þau eru öll upp á spítala. ef þú vilt sjá fyrra heimsmet hjá manninum Þá geturu horft á það hér:https://www.youtube.com/watch?v=TYU-G-MQ3dY","Kári Trevor"]
]
@app.route("/frett/<int:id>")
def news(id):
    return render_template('frett.html', frett=frettir[id],nr=id)

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'Blessaður %s' % escape(username)

@app.errorhandler(404)
def pagenotfound(error):
    return render_template('pagenotfound.html'), 404

@app.errorhandler(500)
def servererror(error):
    return render_template('servererror.html'), 500

if __name__ == '__main__':
    app.run(debug=False, use_reloader=True)