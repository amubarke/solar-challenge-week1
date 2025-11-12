# ☀️ Solar Data Dashboard (Streamlit Branch)

This branch contains the **Streamlit version** of the Solar Data Dashboard, allowing interactive exploration of solar energy data for **Benin, Togo, and Sierra Leone**.

---

## 🌟 Features

- Upload country-specific CSV datasets (`benin_clean.csv`, `togo_clean.csv`, `sierra_leone_clean.csv`)
- Automatic detection of country from file name
- Interactive **widgets** for selecting metrics:
  - GHI (Global Horizontal Irradiance)
  - DNI (Direct Normal Irradiance)
  - DHI (Diffuse Horizontal Irradiance)
- Visualization options:
  - Boxplot
  - Line Plot (over time using `Timestamp` column)
  - Histogram
- Dynamic sidebar filters for year and metric selection

---

## 🛠 Installation

1. **Clone the repository** (if not already cloned):

```bash
git clone <your-repo-url>
cd <your-repo-folder>
git checkout streamlit

Dashboard Preview

Here’s a preview of the Solar Data Dashboard:

![Solar Dashboard](dashboard_screenshots/dashboard.png)
