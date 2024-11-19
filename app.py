from flask import Flask, render_template
import yfinance as yf

app = Flask(__name__)

# Funkce pro získání dat z Yahoo Finance
def get_stock_data(ticker, start_date, end_date):
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    return stock_data

@app.route('/')
def index():
    # Parametry akcie
    ticker = "AAPL"  # Ticker akcie (např. Apple)
    start_date = "2020-01-01"
    end_date = "2023-01-01"

    # Načtení dat
    stock_data = get_stock_data(ticker, start_date, end_date)

    # Připrava dat pro graf
    times = stock_data.index.strftime('%Y-%m-%d').tolist()
    close_prices = stock_data['Close'].tolist()
    volumes = stock_data['Volume'].tolist()

    # Posíláme data do šablony
    return render_template(
        'index.html',
        times=times,
        close_prices=close_prices,
        volumes=volumes,
        ticker=ticker
    )

if __name__ == '__main__':
    app.run(debug=True)
