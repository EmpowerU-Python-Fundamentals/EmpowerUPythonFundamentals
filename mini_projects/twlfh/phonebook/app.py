from flask import Flask, render_template, request, redirect, session, url_for, flash
from dotenv import load_dotenv
from flask_bootstrap import Bootstrap
import pandas as pd
import os

load_dotenv()

app = Flask(__name__)
Bootstrap(app)
app.secret_key = os.getenv('SECRET_KEY')

UPLOADS_FOLDER = 'uploads'
os.makedirs(UPLOADS_FOLDER, exist_ok=True)

admins = {
    'admin': 'qwerty'
}


@app.route('/')
@app.route('/phonebook')

def phonebook():
    grouped_data = []
    filepath = os.path.join(UPLOADS_FOLDER, 'phonebook.xlsx')

    columns = ['Посада', 'ПІБ', 'Внутрішній номер', 'Домашній номер', 'Мобільний номер', 'Поштова скринька']

    if os.path.exists(filepath):
        df = pd.read_excel(filepath, header=None)

        df = df.dropna(how='all')

        current_department = None
        current_rows = []

        for _, row in df.iterrows():
            row_list = list(row.fillna(''))

            if row_list[0] and not any(row_list[1:]):
                if current_department and current_rows:
                    grouped_data.append({'department': current_department, 'rows': current_rows})
                current_department = row_list[0]
                current_rows = []
            elif current_department and row_list[0] and row_list[0] not in columns:
                current_rows.append(row_list)

        if current_department and current_rows:
            grouped_data.append({'department': current_department, 'rows': current_rows})

    return render_template('phonebook.html', grouped_data=grouped_data)

@app.route('/admin', methods = ['GET', 'POST'])
def admin():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username in admins and admins[username] == password:
            session['admin_logged_in'] = True
            return redirect(url_for('upload'))
        else:
            flash('Неправильний логін або пароль')

    return render_template('admin.html')

@app.route('/admin/upload', methods = ['GET', 'POST'])
def upload():
    if 'admin_logged_in' not in session or not session.get('admin_logged_in'):
        flash('У доступі відмовлено. Будь ласка авторизуйтесь.')
        return redirect(url_for('admin'))
    if request.method == 'POST':
         file = request.files.get('phonebook')
         if file and file.filename != '':
            filepath = os.path.join(UPLOADS_FOLDER, 'phonebook.xlsx')
            file.save(filepath)
            flash('Файл успішно завантажено')
            return redirect(url_for('phonebook'))

    return render_template('upload.html')










if __name__ == '__main__':
    app.run(debug=True)