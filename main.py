
from flask import Flask, render_template, request
import requests
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

# Getting blog posts from API
try:
    response = requests.get("https://api.npoint.io/73078fcf718e3d04cd33", timeout=10)
    response.raise_for_status()
    posts = response.json()

except requests.exceptions.RequestException:
    print("Error while getting blog posts")
    posts = []


app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None

    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
            break

    if requested_post is None:
        return "Post not found", 404

    return render_template("post.html", post=requested_post)


@app.route("/form-entry", methods=["POST"])
def receive_data():

    name = request.form.get('name', '').strip()
    email = request.form.get('email', '').strip()
    phno = request.form.get('phone', '').strip()
    msg = request.form.get('message', '').strip()

    # Checking whether required fields are filled
    if not name or not email or not msg:
        return "Please fill all required fields", 400

    memail = os.getenv("EMAIL_ADDRESS")
    mpassword = os.getenv("EMAIL_PASSWORD")

    if not memail or not mpassword:
        return "Email credentials are missing", 500

    subject = "New Contact Form Message"

    body = f"""
    You received a new message!

    Name: {name}
    Email: {email}
    Phone: {phno}

    Message:
    {msg}
    """

    message = f"Subject: {subject}\n\n{body}"

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:

            connection.starttls()

            connection.login(memail, mpassword)

            connection.sendmail(
                memail,
                memail,
                message
            )

        return "SUCCESSFULLY SENT YOUR MESSAGE"

    except (smtplib.SMTPException, OSError):
        return "Unable to send your message. Please try again later.", 500


if __name__ == "__main__":
    app.run(debug=os.getenv("FLASK_DEBUG") == "1", port=5001)
