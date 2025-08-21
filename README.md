# 📊 Digital Marketing Data Analysis Project  

This project is built to analyze **digital marketing performance data** by integrating data pipelines from **Google Analytics 4 (GA4)** and **Google Ads** into a centralized **SQLite database**. The system is fully automated to fetch fresh data daily, enabling **real-time dashboard reporting in Power BI**.  

---

## 🚀 Project Overview  

- Pulled **user behavior data** from **Google Analytics 4 API** (sessions, users, engagement metrics).  
- Extracted **ad performance data** from **Google Ads API** (impressions, clicks, ad spend, conversions).  
- Automated the **ETL pipeline** to fetch fresh data daily and store it in **SQLite**.  
- Connected **Power BI** to SQLite for **interactive dashboards and daily refreshed reports**.  
- Automated **Python scripts** with **Windows Task Scheduler**, ensuring reports are updated **without manual effort**.  

This project demonstrates a **complete data engineering + analytics workflow**, from API integration → ETL pipeline → database → dashboard.  

---

## 📂 Project Structure  

### 🔑 Credentials and Config Files  
- **`.env`** → Stores environment variables for GA4 (project ID, property ID).  
- **`client_secret_XXXX.json`** → Google Ads **OAuth2 credentials** for API authentication.  
- **`eastern-perigee-XXXX.json`** → GA4 **service account key** for fetching analytics data.  
- **`google-ads.yaml`** → Config file containing **Google Ads developer token, OAuth credentials, customer ID**.  

### 🐍 Python / Jupyter Scripts  
- **`GA4APIDataPull.ipynb`** → Fetches GA4 metrics (sessions, users, engagement duration, events).  
- **`google_ads_pull.py`** → Python script to pull **Google Ads performance data** (impressions, clicks, spend).  
- **`refreshToken.ipynb`** → Helps refresh **Google Ads OAuth2 tokens** when expired.  

### 💾 Database  
- **`mydatabase`** → SQLite database storing GA4 + Google Ads data.  
  - Tables:  
    - `ga4_data` → User sessions, engagement, new users, events.  
    - `google_ads` → Impressions, clicks, ad spend, CTR.  

### 📑 Documentation  
- **`ReadMe.md`** → Project documentation (this file).  

---

## ⚙️ ETL Workflow  

1. **Extract**  
   - GA4 API → Pulls user engagement, sessions, traffic sources.  
   - Google Ads API → Pulls impressions, clicks, ad cost, campaign data.  

2. **Transform**  
   - Data cleaned & structured in Python (removes nulls, formats dates).  
   - Consistent schema designed for joining GA4 + Ads data.  

3. **Load**  
   - Final data written to **SQLite database** (`mydatabase`).  
   - Data is appended or updated daily.  

---

## 📊 Reporting Layer  

- Connected **Power BI** to SQLite for **automated reports**.  
- Reports update daily with fresh API data.  
- Dashboards include:  
  - **Traffic Analysis** → Sessions, Users, Engagement Rates.  
  - **Campaign Performance** → Impressions vs Clicks, CTR, Conversions.  
  - **Revenue Analysis** → Ad Spend vs ROI.  
  - **Channel Attribution** → Traffic sources by default channel group.  

---

## 🔄 Automation  

- All scripts are automated with **Windows Task Scheduler**:  
  - GA4 Pull (`GA4APIDataPull.ipynb`).  
  - Google Ads Pull (`google_ads_pull.py`).  
  - SQLite refresh.  
- Runs **every morning**, so reports in Power BI always show **fresh data**.  

---

## 🛠️ Setup Instructions  

1. Clone the repository:  
   ```bash
   git clone https://github.com/yourusername/digital-marketing-analytics.git
   cd digital-marketing-analytics
   ```

2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```

3. Set up credentials:  
   - Add `.env` file with GA4 details.  
   - Place `client_secret.json` (Google Ads) & GA4 service account JSON in root.  
   - Fill `google-ads.yaml` with your Developer Token, OAuth2 client details, and Customer ID.  

4. Run GA4 Pull:  
   ```bash
   jupyter notebook GA4APIDataPull.ipynb
   ```

5. Run Google Ads Pull:  
   ```bash
   python google_ads_pull.py
   ```

6. View `mydatabase` in **DB Browser** or connect via **Power BI**.  

---

## 📊 Example Dashboards  

- 📈 **CTR (Click-Through Rate)** = Clicks ÷ Impressions.  
- 💰 **ROAS (Return on Ad Spend)** = Revenue ÷ Ad Spend.  
- 👥 **User Acquisition** = New Users by Channel.  
- ⏳ **Engagement Trends** = Avg. Engagement Duration per Session.  

---

## 🔒 Security Notes  

- Do **NOT** push `.env`, JSON, or YAML files with sensitive credentials to GitHub.  
- Add them to `.gitignore`.  
- Share only demo or anonymized data for public repositories.  

---

## ✅ Key Learnings  

- End-to-end **ETL automation** with GA4 + Google Ads.  
- Using **SQLite** as a lightweight data warehouse.  
- Building **interactive dashboards** with Power BI.  
- Automating **daily refresh pipelines** with Task Scheduler.  

---

## 📌 Future Improvements  

- Add **Tableau dashboards**.  
- Extend to **Google BigQuery** for large-scale data.  
- Include **Meta Ads API** integration.  

---

👨‍💻 Author: [Your Name]  
