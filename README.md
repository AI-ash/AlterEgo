# 🤖 AlterEgo – Your Custom AI Friend

[![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-FF4B4B?logo=streamlit)](https://streamlit.io/)
[![Python](https://img.shields.io/badge/Made%20with-Python-3776AB?logo=python)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](./LICENSE)
[![Contributions Welcome](https://img.shields.io/badge/PRs-Welcome-blue.svg)](#-contributing)
[![Stars](https://img.shields.io/github/stars/AI-ash/AlterEgo?style=social)](https://github.com/ash333/AlterEgo)

---

AlterEgo is an **AI-powered chatbot** that lets you design and interact with your very own **digital companion**.  
Whether you want a **supportive friend**, a **mentor**, or even a **quirky alter ego** — AlterEgo adapts to your personality.

---

## ✨ Features
✅ **Persona Builder** – Define your AI friend’s name, role & traits  
✅ **Real-Time Chat** – Engage in natural conversations  
✅ **Minimal UI** – Clean & modern interface powered by Streamlit  
✅ **LLM-Powered** – Smart, adaptive & responsive interactions  
✅ **Easy Deployment** – Works seamlessly on Streamlit Cloud or Render  

---

## 🚀 Live Demo
👉 [**Click here to try AlterEgo**](https://alterego.streamlit.app/)  

---

## 📂 Project Structure
```
├── main.py # Core AI logic
├── ui.py # Streamlit UI
├── requirements.txt # Dependencies (pip)
├── uv.lock # Dependencies (uv)
├── .gitignore # Ignored files
└── README.md # Documentation
```


---

## ⚡ Quick Start

### 1️⃣ Clone the repository
```bash
git clone https://github.com/AI-ash/AlterEgo.git
cd AlterEgo
```

### 2️⃣ Create a virtual environment
```bash
python -m venv .venv
source .venv/bin/activate   # Mac/Linux
.venv\Scripts\activate      # Windows
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```
### Or using uv (faster & modern):
```bash
uv sync
```
### 4️⃣ Run the app
```bash
streamlit run ui.py
  ```
### ⚙️ Configuration

# Create a .env file in the root folder and add your API key(s):
```bash
groq_api_key=your_api_key_here
```

## 🖼️ Screenshots

<p align="center">
  <img src="https://envious-scarlet-fksyglvryj.edgeone.app/alterego.png" alt="AlterEgo Screenshot" width="80%"/>
</p>

---

## 🌍 Deployment

### 🔹 Streamlit Cloud
1. Push your repo to GitHub.
2. Go to [Streamlit Cloud](https://share.streamlit.io/).
3. Select `strealit_ui.py` as the entry point.
4. Add your environment variables.

### 🔹 Render
1. Create a **Web Service** on [Render](https://render.com/).
2. Assgin **Build Command**:
   ```bash
   pip install -r requirements.txt
   ```
4. Set **Start Command**:
   ```bash
   streamlit run streamlit_ui.py --server.port $PORT --server.address 0.0.0.0
   ```
5. Add required environment variables.

---

## 🤝 Contributing

We welcome contributions! 🚀  
To contribute:
1. Fork the project 🍴  
2. Create a branch (`feature-xyz`)  
3. Commit changes  
4. Open a Pull Request ✅  

---

## 📜 License
This project is licensed under the **MIT License** – free to use, modify & share.

---

## 👤 Author
**Ashish Sharma**  
🌐 [GitHub](https://github.com/ash333) 

---

⭐ If you like this project, **give it a star** on GitHub — it really helps!  
