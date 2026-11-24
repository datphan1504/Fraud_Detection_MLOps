import streamlit as st

def about_me_page():
    # Title
    st.title("👨‍💻 About Me - Phan Đạt (datphan1504)")

    # Intro
    st.markdown("""
    Hi! I'm **Phan Đạt**, a passionate **AI/ML Engineer** with expertise in building **end-to-end machine learning products** 
    and specializing in **Generative AI, MLOps, Financial ML, and Deep Learning**.  
    
    
    I enjoy transforming ideas into production-ready solutions using modern AI tools and frameworks.
    
    ---
    """)

    # Technical Skills
    st.subheader("⚡ Technical Skills")
    st.markdown("""
    - **Languages:** Python, SQL, C++  
    - **Developer Tools:** FastAPI, Flask, Docker, Git, PostgreSQL, MongoDB  
    - **ML & Data Science:** Machine Learning & Deep Learning Algorithms, Credit Risk & Fraud Detection,  
      PyTorch, TensorFlow, Scikit-learn, Imbalanced-learn, NLP, RAG, LangChain, LangGraph, Vector Databases, OpenCV  
    - **MLOps & Cloud:** Docker, MLflow, DVC, Kubernetes, Prometheus, Grafana, CI/CD (GitHub Actions)
    
    ---
    """)

    # Projects Section
    st.subheader("🚀 Featured Projects")
    st.markdown("""
    - **[Credit Risk Scorecard System](https://github.com/datphan1504/Credit-Risk-Scorecard-System)** – End-to-End Probability of Default (PD) Application Scorecard with WoE/IV binning, MLflow, FastAPI, Streamlit, and Docker.  
    - **[Fraud Detection MLOps Pipeline](https://github.com/datphan1504/Fraud_Detection_MLOps)** – Real-time transaction fraud detection with SMOTE, threshold optimization, FastAPI, Docker, Kubernetes, Prometheus & Grafana.  
    
    ---
    """)

    # Links
    st.subheader("🌐 Connect with Me")
    st.markdown("""
    - **Email:** [pdat8778@gmail.com](mailto:pdat8778@gmail.com)  
    - **GitHub:** [github.com/datphan1504](https://github.com/datphan1504)  
    """)
