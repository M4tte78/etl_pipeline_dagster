from dagster import asset
import pandas as pd
from fpdf import FPDF
from matplotlib import pyplot as plt

@asset(deps=["daily_prices", "daily_returns", "daily_news"])
def market_pdf_report(daily_prices: pd.DataFrame, daily_returns: pd.DataFrame, daily_news: pd.DataFrame) -> str:
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="Daily Market Recap", ln=True, align='C')
    pdf.ln(10)

    pdf.set_font("Arial", size=10)
    pdf.cell(200, 10, txt="Top 5 Returns:", ln=True)

    top5 = daily_returns.head(5)
    for _, row in top5.iterrows():
        pdf.cell(200, 10, txt=f"{row['ticker']}: {row['return']:.2%}", ln=True)

    pdf.ln(10)
    pdf.cell(200, 10, txt="News Headlines:", ln=True)
    for _, row in daily_news.iterrows():
        pdf.cell(200, 10, txt=f"- {row['title']} ({row['source']})", ln=True)

    # Save chart
    fig, ax = plt.subplots()
    ax.bar(top5["ticker"], top5["return"])
    ax.set_title("Top 5 Returns")
    chart_path = "top5_chart.png"
    fig.savefig(chart_path)
    plt.close(fig)

    pdf.image(chart_path, x=10, y=None, w=180)

    output_path = "daily_market_report.pdf"
    pdf.output(output_path)
    return output_path
