from flask import Blueprint, render_template, url_for, current_app, g, request, redirect
from .database import get_db

fifth = Blueprint('fifth', __name__, static_folder='static', template_folder='templates')

@fifth.teardown_app_request
def close_db(error):
    if hasattr(g, 'fifth_db'):
        g.fifth_db.close()

@fifth.route("/", methods=['GET', 'POST'])
def home():
    message = 'This home page is from the fifth module'
    return render_template('fifth/home.html', message=message)

# this example opens a db and reads some stuff
@fifth.route('/hello', methods=['GET', 'POST'])
def hello():
    message = 'This message was from the view'
    db = get_db()
    cur = db.cursor()
    sql = 'select id, country_name, city_name, population, area, currency, continent, time_zone, language from countries'
    cur.execute(sql)
    data = cur.fetchall()
    return render_template('fifth/hello.html', message=message, countries=data)

# edit form for a country.
@fifth.route('/edit/<cid>', methods=['GET', 'POST'])
def edit(cid):
    db = get_db()
    cur = db.cursor()
    country_id = int(cid)

    if request.method == 'POST':
        # collect field values and update.
        country = {
            'country_name': request.form['country_name'],
            'city_name': request.form['city_name'],
            'population': int(request.form['population']),
            'area': int(request.form['area']),
            'currency': request.form['currency'],
            'continent': request.form['continent'],
            'time_zone': request.form['time_zone'],
            'language': request.form['language']
        }
        sqlvalues = list(country.values())
        sqlvalues.append(country_id)
        sql = '''
            update countries set country_name = ?, city_name = ?, population = ?,
                area = ?, currency = ?, continent = ?, time_zone = ?, language = ?
            where id = ?
        '''
        cur.execute(sql, sqlvalues)
        db.commit()
        return redirect(url_for('fifth.hello'))

    sql = '''
        select id, country_name, city_name, population, area, currency, continent,
        time_zone, language from countries where id = ?
    '''
    cur.execute(sql, [country_id])
    data = cur.fetchone()

    return render_template('fifth/edit.html', country=data)
