from flask import Flask, render_template, request, redirect, abort
from models import db, EmployeeModel

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return redirect('/data/create')

@app.route('/data/create', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('createpage.html')

    if request.method == 'POST':
        employee_id = request.form['employee_id']
        existing_employee = EmployeeModel.query.filter_by(employee_id=employee_id).first()
        if existing_employee:
            return "Employee with this ID already exists", 400

        name = request.form['name']
        age = request.form['age']
        position = request.form['position']
        employee = EmployeeModel(employee_id=employee_id, name=name, age=age, position=position)
        db.session.add(employee)
        db.session.commit()
        return redirect('/data')

@app.route('/data')
def retrieve_list():
    employees = EmployeeModel.query.all()
    return render_template('datalist.html', employees=employees)

@app.route('/data/<int:id>', methods=['GET'])
def view_employee(id):
    employee = EmployeeModel.query.get(id)
    if not employee:
        abort(404)
    return render_template('view.html', employee=employee)

@app.route('/data/<int:id>/delete', methods=['POST'])
def delete_employee(id):
    employee = EmployeeModel.query.get(id)
    if not employee:
        abort(404)
    db.session.delete(employee)
    db.session.commit()
    return redirect('/data')

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
