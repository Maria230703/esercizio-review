"""Calcola il totale di un carrello della spesa."""


def subtotale(prodotto):
    """Restituisce prezzo x quantità per un singolo prodotto."""
    return prodotto["prezzo"] * prodotto["quantita"]


def totale_carrello(carrello):
    """Somma i subtotali di tutti i prodotti nel carrello."""
    totale = 0
    for prodotto in carrello:
        totale += subtotale(prodotto)
    return totale


def stampa_scontrino(carrello):
    """Stampa ogni riga del carrello e il totale finale."""
    for prodotto in carrello:
        print(
            f"{prodotto['nome']:<12} "
            f"{prodotto['quantita']:>3} x {prodotto['prezzo']:>6.2f} € "
            f"= {subtotale(prodotto):>7.2f} €"
        )
    print("-" * 40)
    print(f"{'TOTALE':<29}{totale_carrello(carrello):>7.2f} €")


if __name__ == "__main__":
    carrello = [
        {"nome": "Pane", "prezzo": 2.50, "quantita": 2},
        {"nome": "Latte", "prezzo": 1.20, "quantita": 3},
        {"nome": "Mele", "prezzo": 0.40, "quantita": 6},
        {"nome": "Caffè", "prezzo": 4.90, "quantita": 1},
    ]
    stampa_scontrino(carrello)
