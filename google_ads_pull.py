import sqlite3
from google.ads.googleads.client import GoogleAdsClient

# Load Google Ads client
client = GoogleAdsClient.load_from_storage("google-ads.yaml")

# Replace with your Ads account ID (no dashes)
customer_id = "1234567890"

# Query (last 7 days campaign stats)
query = """
    SELECT
      campaign.id,
      campaign.name,
      metrics.clicks,
      metrics.impressions,
      metrics.cost_micros
    FROM campaign
    WHERE segments.date DURING LAST_7_DAYS
"""

ga_service = client.get_service("GoogleAdsService")
response = ga_service.search(customer_id=customer_id, query=query)

# Save into SQLite
conn = sqlite3.connect("google_ads.db")
cur = conn.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS campaign_stats (
  campaign_id TEXT,
  campaign_name TEXT,
  clicks INTEGER,
  impressions INTEGER,
  cost REAL
)
""")

for row in response:
    cur.execute("""
    INSERT INTO campaign_stats VALUES (?, ?, ?, ?, ?)
    """, (
        row.campaign.id,
        row.campaign.name,
        row.metrics.clicks,
        row.metrics.impressions,
        row.metrics.cost_micros / 1e6  # convert micros to currency
    ))

conn.commit()
conn.close()
print("✅ Data inserted into SQLite")
