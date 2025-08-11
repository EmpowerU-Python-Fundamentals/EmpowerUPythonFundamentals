from flask import Flask, url_for, request, render_template, redirect
from model import TelephoneBook, Contact, validate_phone_number
app = Flask(__name__)

BOOKS = TelephoneBook()
BOOKS.generate_random_contacts(10)




@app.route("/")
def index():
    return render_template("list_contacts.html", contacts=BOOKS.contacts)

@app.route("/add_contact", methods=["GET", "POST"])
def add_contact():
    """
    Маршрут для додавання нового контакту.
    GET-запит: відображає форму.
    POST-запит: обробляє дані форми і перенаправляє на головну сторінку.
    """
    if request.method == "POST":
        name = request.form["name"]
        phone_number = request.form["phone_number"]
        if not validate_phone_number(phone_number):
            error_message = "Невалідний номер телефону. Будь ласка, введіть у форматі 0XX-XXX-XX-XX."
            return render_template("create_contact.html", error=error_message)
        new_contact = Contact(name, phone_number)
        BOOKS.add_contact(new_contact)
        return redirect("/")
    
    return render_template("create_contact.html")
@app.route("/view_contact/<uuid:contact_id>")
def view_contact(contact_id):
    """
    Маршрут для перегляду деталей одного контакту за його ID.
    """
    contact = BOOKS.find_contact_by_id(contact_id)
    return render_template("contact_info.html", contact=contact)


if __name__ == "__main__":
    app.run(debug=True)