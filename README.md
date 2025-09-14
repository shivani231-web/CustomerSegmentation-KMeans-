# Customer Segmentation Dashboard (Python + Power BI)

## 📌 Project Overview
This project applies **KMeans clustering** and statistical analysis to a mall customer dataset, followed by building an **interactive Power BI dashboard**.  
The goal is to identify customer segments based on **Age, Annual Income, and Spending Score** and visualize insights for business decision-making.

---

## 📂 Project Structure
customer_segmentation_project/
│── data/
│ └── Mall_Customers.csv # Raw dataset
│── notebooks/
│ └── analysis.ipynb # Jupyter notebook (data cleaning, clustering, EDA)
│── src/
│ └── clustering.py # Python script with KMeans model
│── powerbi/
│ └── customer_segmentation.pbix # Power BI dashboard file
│── images/
│ └── dashboard_preview.png # Screenshot of dashboard (add this yourself)
│── requirements.txt # Python dependencies
│── README.md # Project documentation
│── .gitignore # Ignore unnecessary files

---

## 🛠️ Tools & Technologies
- **Python** (Pandas, Scikit-learn, Matplotlib, Seaborn)  
- **Power BI** (visualization & dashboards)  
- **Git + GitHub** (version control & portfolio showcase)  

---

## 🔑 Key Steps
1. **Data Cleaning & Exploration**  
   - Loaded `Mall_Customers.csv`  
   - Checked for missing values, encoded gender, and explored distributions  

2. **Feature Engineering**  
   - Selected features: `Age`, `Annual Income (k$)`, `Spending Score (1-100)`  
   - Encoded categorical columns  

3. **Clustering (KMeans)**  
   - Applied **Elbow Method** to find optimal `k`  
   - Segmented customers into distinct groups  

4. **Insights Extraction**  
   - Profiled clusters (e.g., high-income vs. low-spending customers)  
   - Correlation and regression analysis for deeper insights  

5. **Power BI Dashboard**  
   - Imported clustered dataset  
   - Created visuals: scatter plots, cluster distribution, income vs. spending comparison  

---

## 🚀 How to Run
### Python Analysis
```bash
# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # for Mac/Linux
.venv\Scripts\activate     # for Windows

# Install requirements
pip install -r requirements.txt

# Run Jupyter notebook
jupyter notebook notebooks/analysis.ipynb
Power BI Dashboard
Open powerbi/customer_segmentation.pbix in Power BI Desktop.

Interact with the dashboard (filters, visuals, drill-downs).

📈 Insights
Cluster 1: Young, high income, high spending → potential premium customers

Cluster 2: Older, low income, low spending → budget-conscious customers

Cluster 3: Middle-aged, average income, moderate spending

Businesses can use these segments for targeted marketing & personalized offers.

🤝 Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss.

📧 Contact
Created by Shivani Mudagal
LinkedIn: www.linkedin.com/in/shivani-mudagal-3bba33378


yaml
Copy code
