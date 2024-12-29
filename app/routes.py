from app import app
from flask import render_template,jsonify,request
import requests as req
from app.models.product import Product 
import logging
import pandas as pd

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

@app.route('/')
@app.route('/home')
def home():
    temp = "tes"
    products=[]
    r=req.get('https://fakestoreapi.com/products')
    for product in r.json():
        if temp != product['category']:
            temp = product['category']
            products.append(
             Product(
                id=product['id'],
                title=product['title'],
                price=product['price'],
                description=product['description'],
                category=product['category'],
                image=product['image']
            )
        )
    return render_template("home.html",products=products)

@app.route('/kategori')
def kategori():
    temp = "tes"
    products=[]
    r=req.get('https://fakestoreapi.com/products')
    for product in r.json():
        if temp != product['category']:
            temp = product['category']
            products.append(
             Product(
                id=product['id'],
                title=product['title'],
                price=product['price'],
                description=product['description'],
                category=product['category'],
                image=product['image']
            )
        )
    return render_template("kategori.html", products=products)

@app.route('/produk', methods=['GET'])
def produk():
    kategori = request.args.get('kategori')
    products=[]
    r=req.get('https://fakestoreapi.com/products')
    x=r.json()

    if kategori:
        for product in x:
            if product['category'] == kategori:
                products.append(
                Product(
                    id=product['id'],
                    title=product['title'],
                    price=product['price'],
                    description=product['description'],
                    category=product['category'],
                    image=product['image']
                    )
                    )
    else :
        kategori = "All Produk"
        for product in x:
            products.append(
            Product(
                id=product['id'],
                title=product['title'],
                price=product['price'],
                description=product['description'],
                category=product['category'],
                image=product['image']
            )
            )
    app.logger.info(kategori)
    return render_template("produk.html", products=products,kategori=kategori)

@app.route('/contact')
def contact():
    return render_template("kontak.html")

@app.route('/product/<int:product_id>', methods=['GET'])
def get_product(product_id):

    r=req.get(f'https://fakestoreapi.com/products/{product_id}')
    product=r.json()
    return render_template('detail_produk.html',product=product)

@app.route('/sendemail', methods=['POST'])
def send_email():
    from_email = request.form['from_email']
    subject = request.form['subject']
    html_content = request.form['html_content']

    # Informasi akun Gmail pengirim
    to_email = "hendrawanoktavianto786@gmail.com"
    from_password = "krzvremketptrogb"  # Gunakan App Password jika 2FA aktif

    # Membuat pesan email
    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = from_email
    msg["To"] = to_email

    # Menambahkan konten HTML
    html_part = MIMEText(html_content, "html")
    msg.attach(html_part)

    try:
        # Menghubungkan ke server Gmail
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()  # Memulai koneksi aman
            server.login(to_email, from_password)  # Login ke Gmail
            server.sendmail(from_email, to_email, msg.as_string())  # Kirim email

        message = "Email berhasil dikirim!"
    except Exception as e:
        message = "Terjadi kesalahan: {e}"

    return render_template("kontak.html", message=message)


@app.route('/about')

def about():
    profile={
        'name' : 'Hendrawan Oktavianto',
        'email':'hendrawanoktavianto786@gmail.com',
        'photo':'image2.png',
    }
    return render_template('profile.html', title='Home', profile=profile)
