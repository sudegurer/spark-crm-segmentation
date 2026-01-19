# Spark CRM Segmentation

A self-contained PySpark project that simulates a CRM dataset, applies segmentation techniques, and explores customer clustering using PySpark DataFrames.  
Developed as a practice project to understand **large-scale data handling**, **PySpark transformations**, and **clustering analysis**.

---

##  Project Overview

The project focuses on segmenting customers based on simulated transactional and behavioral data:

1. **Data Generation** – Create a synthetic CRM dataset (~500k customers)  
2. **Segmentation** – Apply clustering techniques to identify customer groups  
3. **Analysis** – Explore patterns and visualize clusters in PySpark/Notebook

Goal: Provide a hands-on environment to practice **Big Data transformations** and **customer segmentation workflows** without relying on real-world data.

---

##  Tech Stack

- **Python 3.9+** – core scripting for data generation and PySpark workflows  
- **PySpark** – distributed data processing and clustering  
- **Docker & Docker Compose** – optional containerized Spark environment  
- **Pandas & NumPy** – auxiliary data manipulation  
- **Jupyter Notebook** – interactive exploration (`PySpark_CRM_Segmentation.ipynb`)

---

##  Repository Structure
```
spark-crm-segmentation/
├── data/                   # Generated dataset (raw)  
├── venv/                   # Optional Python virtual environment  
├── docker-compose.yml      # Docker setup for Spark cluster  
├── generate_data.py        # Script to generate synthetic CRM data  
├── PySpark_CRM_Segmentation.ipynb  # Notebook for segmentation and analysis  
├── README.md               # Project documentation
```
---

##  Quick Start / Installation

> **Prerequisites:** Python 3.9+, Docker (optional for Spark)

### 1) Clone the repository
```
git clone https://github.com/sudegurer/spark-crm-segmentation.git
cd spark-crm-segmentation
```
### 2) Set up a Python virtual environment
```
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
# venv\Scripts\activate   # Windows
```
### 3) Install dependencies and generate data
```
pip install pandas numpy
python3 generate_data.py
```

### 4) Start Spark environment
```
docker compose up -d
```

### 5) Launch Notebook
Open PySpark_CRM_Segmentation.ipynb in Jupyter:
```
jupyter notebook
```
Navigate to the notebook in your browser and run the cells for data processing, segmentation, and cluster analysis.

### 7) Stop Spark environment (if used)

```
docker compose down
deactivate
```

⸻

 What I Learned
	•	Generating large synthetic datasets for testing
	•	PySpark DataFrame transformations
	•	Customer segmentation using clustering
	•	Notebook-based exploratory analysis on big datasets

⸻

 Notes & Limitations
	•	The dataset is synthetic, not real customer data
	•	Dockerized Spark is optional; PySpark can run locally for small datasets
	•	Clustering parameters and feature engineering are simplified for educational purposes

⸻

 Repository Link:
https://github.com/sudegurer/spark-crm-segmentation￼
