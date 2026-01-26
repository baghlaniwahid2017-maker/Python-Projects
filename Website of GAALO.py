# ============================
# GAALO AGRICULTURE DASHBOARD
# ============================

from flask import Flask, render_template_string, request, send_file
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.io as pio
import io

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>GAALO Agriculture Dashboard</title>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
<style>
body { padding-top: 60px; background:#f4f4f4; }
header { background:#2e7d32; color:white; padding:20px 0; text-align:center; }
section { padding:40px 20px; }
.plotly-graph-div { margin-top: 20px; }
.analysis { margin-top:20px; padding:15px; background:#fff; border-radius:8px; box-shadow:0 0 5px #ccc; }
</style>
</head>
<body>
<header>
    <h1>GAALO Agriculture Dashboard</h1>
    <p>Monitoring Greenhouses, Livestock, and Community Projects</p>
</header>

<nav class="navbar navbar-expand-lg navbar-light bg-light mb-4">
<div class="container">
<a class="navbar-brand" href="#">GAALO</a>
<div class="collapse navbar-collapse">
<ul class="navbar-nav me-auto">
<li class="nav-item"><a class="nav-link" href="#home">Home</a></li>
<li class="nav-item"><a class="nav-link" href="#projects">Projects</a></li>
<li class="nav-item"><a class="nav-link" href="#dashboard">Dashboard</a></li>
<li class="nav-item"><a class="nav-link" href="#resources">Resources</a></li>
<li class="nav-item"><a class="nav-link" href="#contact">Contact</a></li>
</ul>
</div>
</div>
</nav>

<section id="home">
<h2>About GAALO</h2>
<p>GAALO works to improve agriculture, livestock, food security, and community livelihoods through sustainable initiatives across multiple provinces.</p>
</section>

<section id="projects">
<h2>Our Projects</h2>
<ul>
<li>Greenhouse Development & Household Training</li>
<li>Livestock Support Programs</li>
<li>Community-Based Food Security & Irrigation Projects</li>
<li>Farmer Education & Capacity Building</li>
</ul>
</section>

<section id="dashboard">
<h2>Farm & Livestock Analytics</h2>
<form method="post">
<input type="number" name="days" placeholder="Number of Days to Simulate" class="form-control" required>
<button type="submit" class="btn btn-success mt-2">Generate Dashboard</button>
</form>

{% if greenhouse_plot %}
<div class="analysis">
<h4>Greenhouse Yield & Water Usage</h4>
{{ greenhouse_plot|safe }}
</div>
{% endif %}

{% if livestock_plot %}
<div class="analysis">
<h4>Livestock Growth & Health</h4>
{{ livestock_plot|safe }}
</div>
{% endif %}

{% if csv_ready %}
<a href="/download_csv" class="btn btn-primary mt-2">Download Report CSV</a>
{% endif %}
</section>

<section id="resources">
<h2>Resources & Guides</h2>
<ul>
<li>Greenhouse Irrigation Best Practices</li>
<li>Livestock Feeding & Care Guidelines</li>
<li>Crop Rotation & Fertilization Methods</li>
<li>Community Farming Video Tutorials</li>
</ul>
</section>

<section id="contact">
<h2>Contact Us</h2>
<p>Email: contact@gaalo.org | Phone: +93 XXX XXX XXX</p>
<form>
<input type="text" placeholder="Your Name" class="form-control mb-2">
<input type="email" placeholder="Your Email" class="form-control mb-2">
<textarea placeholder="Message" class="form-control mb-2"></textarea>
<button type="submit" class="btn btn-primary">Send Message</button>
</form>
</section>

</body>
</html>
"""

# Global variable to store report CSV
report_df = pd.DataFrame()

# -------------------------------
# Simulated Data Generation
# -------------------------------
def generate_greenhouse_data(days):
    households = ['Household 1','Household 2','Household 3']
    data = []
    for h in households:
        cumulative_yield = np.cumsum(np.random.randint(5,20,days))
        cumulative_water = np.cumsum(np.random.randint(50,150,days))
        for i in range(days):
            data.append({
                'Household': h,
                'Day': i+1,
                'Yield_kg': cumulative_yield[i],
                'Water_Liters': cumulative_water[i]
            })
    df = pd.DataFrame(data)
    return df

def generate_livestock_data(days):
    herds = ['Herd A','Herd B','Herd C']
    data = []
    for h in herds:
        weight = np.cumsum(np.random.randint(1,5,days))
        health_score = np.clip(np.random.normal(80,5,days), 60, 100)
        for i in range(days):
            data.append({
                'Herd': h,
                'Day': i+1,
                'Weight_kg': weight[i],
                'Health_Score': health_score[i]
            })
    df = pd.DataFrame(data)
    return df

# -------------------------------
# Flask Routes
# -------------------------------
@app.route("/", methods=["GET","POST"])
def home():
    global report_df
    greenhouse_plot = None
    livestock_plot = None
    csv_ready = False
    if request.method=="POST":
        days = int(request.form["days"])
        # Generate data
        gh_df = generate_greenhouse_data(days)
        ls_df = generate_livestock_data(days)
        report_df = pd.concat([gh_df, ls_df], axis=1, join='inner')

        # Greenhouse Plot
        fig_gh = px.line(gh_df, x='Day', y=['Yield_kg','Water_Liters'], color='Household', 
                         labels={'value':'Amount','variable':'Metric'})
        greenhouse_plot = pio.to_html(fig_gh, full_html=False)

        # Livestock Plot
        fig_ls = px.line(ls_df, x='Day', y=['Weight_kg','Health_Score'], color='Herd', 
                         labels={'value':'Value','variable':'Metric'})
        livestock_plot = pio.to_html(fig_ls, full_html=False)

        csv_ready = True

    return render_template_string(HTML_TEMPLATE, greenhouse_plot=greenhouse_plot, 
                                  livestock_plot=livestock_plot, csv_ready=csv_ready)

@app.route("/download_csv")
def download_csv():
    global report_df
    output = io.BytesIO()
    report_df.to_csv(output, index=False)
    output.seek(0)
    return send_file(output, as_attachment=True, download_name="GAALO_Farm_Report.csv", mimetype="text/csv")

if __name__=="__main__":
    app.run(debug=True)
