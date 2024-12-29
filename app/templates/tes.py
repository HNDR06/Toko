import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(to_email, subject, html_content):
    # Informasi akun Gmail pengirim
    from_email = "hendrawanoktavianto786@gmail.com"
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
            server.login(from_email, from_password)  # Login ke Gmail
            server.sendmail(from_email, to_email, msg.as_string())  # Kirim email

        print("Email berhasil dikirim!")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

# Contoh penggunaan
if __name__ == "__main__":
    recipient = "hendrawanoktavianto786@gmail.com"
    subject = "Test Email HTML"
    html_message = """\
    <html>
      <body>
        <h1 style='color:blue;'>Halo!</h1>
        <p>Ini adalah email percobaan dengan format <b>HTML</b>.</p>
      </body>
    </html>
    """
    send_email(recipient, subject, html_message)
