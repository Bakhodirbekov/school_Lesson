from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')


# Haftalik darsliklar ma'lumotlari (bu misol uchun statik, lekin siz uni ma'lumotlar bazasidan olishi kerak)
darslar = {
    'Dushanba': [
        ('Matematika', '9:00', '101-xona'),
        ('Fizika', '10:30', '203-xona'),
        ('Informatika', '12:00', '305-xona'),
        ('Tarbiya', '13:30', '102-xona'),
        ('Tarix', '15:00', '204-xona')
    ],
    'Seshanba': [
        ('Adabiyot', '9:00', '103-xona'),
        ('Tarix', '11:00', '205-xona'),
        ('Kimyo', '12:30', '306-xona'),
        ('Geometriya', '14:00', '104-xona'),
        ('Ona tili', '15:30', '207-xona')
    ],
    'Chorshanba': [
        ('Ingliz tili', '9:00', '108-xona'),
        ('Biologiya', '12:00', '309-xona'),
        ('Jismoniy tarbiya', '13:30', 'Sport zal'),
        ('Fizika', '15:00', '203-xona'),
        ('Kimyo', '16:30', '306-xona')
    ],
    'Payshanba': [
        ('Kimyo', '9:00', '306-xona'),
        ('Geografiya', '10:30', '110-xona'),
        ('Matematika', '12:00', '101-xona'),
        ('Informatika', '13:30', '305-xona'),
        ('Tarix', '15:00', '204-xona')
    ],
    'Juma': [
        ('Matematika', '9:00', '101-xona'),
        ('Informatika', '13:00', '305-xona'),
        ('Biologiya', '14:30', '309-xona'),
        ('Adabiyot', '16:00', '103-xona'),
        ('Geometriya', '17:30', '104-xona')
    ],
    'Shanba': [
        ('Sport', '9:00', 'Sport zal'),
        ('Ona tili', '10:30', '207-xona'),
        ('Jismoniy tarbiya', '12:00', 'Sport zal'),
        ('Kimyo', '13:30', '306-xona'),
        ('Tarix', '15:00', '204-xona')
    ]
}



@app.route('/')
def admin_panel():
    return render_template('admin_panel.html')

@app.route('/user_panel')
def user_panel():
    return render_template('user_panel.html')

@app.route('/darslar/<kun>')
def darslar_kuniga_ko_ra(kun):
    if kun in darslar:
        return render_template('darslar.html', kun=kun, darslar=darslar[kun])
    return "Kun topilmadi", 404

if __name__ == '__main__':
    app.run(debug=True)