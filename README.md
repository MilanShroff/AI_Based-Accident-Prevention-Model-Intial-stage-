# 🚧 AI-Based Accident Prevention in MMS

This project is an **AI-powered PPE (Personal Protective Equipment) detection app** designed for **accident prevention**.

It uses a **custom-trained YOLOv8 model** to detect:
- 👷 **Person**
- 🪖 **Helmet**
- 🦺 **Vest**

to help ensure workers follow safety protocols on site.

---

## 📂 Project Structure

```bash
AI_Based-Accident-Prevention-Model/
├── app.py # Streamlit web app
├── best.pt # Trained YOLOv8 model weights
├── requirements.txt # Dependencies
├── README.md # Project overview
```

---

## ⚙️ How It Works

1. **Upload an Image** — Supported formats: `.jpg`, `.jpeg`, `.png`.

2. **Run Detection** — The app uses YOLOv8 to detect people, helmets, and vests.

3. **See Results** — The image is returned with detection boxes and labels.

---

## 🚀 Run This Project Locally

**1️⃣ Clone the repository**

```bash
git clone https://github.com/YourUsername/AI_Based-Accident-Prevention-Model.git
```
2️⃣ Install dependencies
```bash
pip install -r requirements.txt
```
3️⃣ Launch the Streamlit app
```bash
streamlit run app.py
```
☁️ Deploy on Streamlit Cloud
Push this project to GitHub

Go to Streamlit Community Cloud

Connect your repository and select app.py as the main file

Click Deploy

Your app will run live on the web — you can share the link in your project report.

📦 Requirements
requirements.txt should contain:

streamlit
ultralytics
Pillow

📊 Dataset
Name: PPE Dataset for Workplace Safety Computer Vision Project

Used to train a YOLOv8 object detection model to identify people, helmets, and vests.

✨ Future Scope
Integrate CCTV video streams for real-time detection.

Add automatic alerts if PPE is missing.

Extend to detect more safety gear.

