import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --- Page Configuration ---
st.set_page_config(page_title="☀️ Solar Data Dashboard", layout="wide")

# --- Title ---
st.title("☀️ Solar Data Dashboard")
st.markdown("Upload your solar dataset (Benin, Togo, or Sierra Leone) to visualize solar metrics and insights.")

# --- File Upload ---
uploaded_file = st.file_uploader("📂 Upload your solar data CSV file", type=["csv"])

# --- Country Detection Function ---
def detect_country(filename):
    filename_lower = filename.lower()
    if "benin" in filename_lower:
        return "Benin"
    elif "togo" in filename_lower:
        return "Togo"
    elif "sierra" in filename_lower or "leone" in filename_lower:
        return "Sierra Leone"
    else:
        return "Unknown"

# --- When a file is uploaded ---
if uploaded_file is not None:
    # Detect country from filename
    selected_country = detect_country(uploaded_file.name)
    st.success(f"✅ File uploaded successfully — Detected Country: **{selected_country}**")

    # Load dataset
    df = pd.read_csv(uploaded_file)

    # Add Country column (important fix)
    df["Country"] = selected_country

    # Preview data
    st.dataframe(df.head(), use_container_width=True)

    # --- Sidebar Filters ---
    st.sidebar.header("🔍 Visualization Options")
    metric = st.sidebar.radio("Select Metric", ["GHI", "DNI", "DHI"])
    plot_type = st.sidebar.selectbox("📊 Choose Plot Type", ["Boxplot", "Line Plot", "Histogram"])

    # --- Visualization Section ---
    st.subheader(f"📈 {plot_type} of {metric} — {selected_country}")

    if metric in df.columns:
        if plot_type == "Boxplot":
            fig, ax = plt.subplots()
            sns.boxplot(data=df, y=metric, color="gold", ax=ax)
            ax.set_title(f"{metric} Distribution in {selected_country}")
            st.pyplot(fig)

        elif plot_type == "Line Plot":
            if "Timestamp" in df.columns:
                df["Timestamp"] = pd.to_datetime(df["Timestamp"], errors="coerce")
                df = df.dropna(subset=["Timestamp"])
                fig, ax = plt.subplots()
                ax.plot(df["Timestamp"], df[metric], color="orange")
                ax.set_title(f"{metric} Trend Over Time — {selected_country}")
                ax.set_xlabel("Timestamp")
                ax.set_ylabel(metric)
                st.pyplot(fig)
            else:
                st.warning("⚠️ No 'Timestamp' column found for line plot.")

        elif plot_type == "Histogram":
            fig, ax = plt.subplots()
            ax.hist(df[metric].dropna(), bins=30, color="skyblue", edgecolor="black")
            ax.set_title(f"{metric} Frequency Distribution — {selected_country}")
            ax.set_xlabel(metric)
            ax.set_ylabel("Count")
            st.pyplot(fig)
    else:
        st.warning(f"⚠️ The selected metric '{metric}' is not found in this dataset.")

    # --- Top Regions Table ---
    if "Region" in df.columns or "Location" in df.columns:
        region_col = "Region" if "Region" in df.columns else "Location"
        st.subheader(f"🏆 Top Regions by Average {metric} — {selected_country}")
        top_regions = (
            df.groupby(region_col)[metric]
            .mean()
            .sort_values(ascending=False)
            .reset_index()
            .head(10)
        )
        st.dataframe(top_regions, use_container_width=True)
    else:
        st.info("ℹ️ No 'Region' or 'Location' column found to display top regions.")

else:
    st.info("📤 Please upload a CSV file to begin.")
