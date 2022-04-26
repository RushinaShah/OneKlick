from flask import Flask, render_template, request
from pymysql import connections

app = Flask(__name__)

db_conn = connections.Connection(
    host="localhost",
    port=3306,
    user="user",
    password="password",
    db="db"
)

@app.route("/", methods=['GET', 'POST'])
def index():
	return render_template('index.html')

@app.route("/checkout", methods=['GET'])
def checkout():
    return render_template("checkout.html")

@app.route("/contact", methods=['GET',])
def contact():
    return render_template("contact.html")

@app.route("/shop", methods=['GET',])
def shop():
    return render_template("shop.html")

@app.route("/single_product", methods=['GET',])
def single_product():
    return render_template("single-product-details.html")

@app.route('/result',methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        form_data = request.form
        first_name = form_data['First Name']
        last_name = form_data['Last Name']
        address = form_data['Address']
        pin = form_data['PIN']
        city = form_data['City']
        state = form_data['State']
        contact = form_data['Contact'] if form_data['Contact'] else None
        email = form_data['Email']

        insert_sql = "INSERT INTO db.users (first_name, last_name, address, pin, city, state, contact, email) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        cursor = db_conn.cursor()

        try:

            cursor.execute(insert_sql, (
                first_name, last_name, address, pin,
                city, state, contact, email
            ))
            db_conn.commit()
        except Exception as e:
            print(str(e))

        finally:
            cursor.close()
        return render_template("result.html",result = result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

