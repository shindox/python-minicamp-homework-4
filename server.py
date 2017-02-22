from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/movie', methods = ['POST'])
def newmovie():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    name = request.form['name']
    year = request.form['year']
    rating = request.form['rating']
    genre = request.form['genre']
    plot = request.form['plot']

    try:
        cursor.execute('INSERT INTO movies(name, year, rating, genre, plot) VALUES (?,?,?,?,?)', (name, year, rating, genre, plot))
        connection.commit()
        message = 'Movie successfully added'
    except:
        connection.rollback()
        message = 'an error occured'
    finally:
        connection.close()
        return message

@app.route('/movies')
def movies():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * from movies')
    moviesList = cursor.fetchall()
    connection.close()
    return jsonify(moviesList)

app.run(debug = True)
