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


def applica_sconto(totale, percentuale):
    """Applica al totale uno sconto espresso in percentuale (es. 10 = 10%)."""
    if percentuale == 0:
        return totale
    sconto = totale * percentuale / 100
    return round(totale - sconto, 1)


def stampa_scontrino(carrello, sconto=0):
    """Stampa ogni riga del carrello, l'eventuale sconto e il totale finale."""
    for prodotto in carrello:
        print(
            f"{prodotto['nome']:<12} "
            f"{prodotto['quantita']:>3} x {prodotto['prezzo']:>6.2f} € "
            f"= {subtotale(prodotto):>7.2f} €"
        )
    print("-" * 40)
    totale = totale_carrello(carrello)
    if sconto:
        totale_scontato = applica_sconto(totale, sconto)
        print(f"{'Subtotale':<29}{totale:>7.2f} €")
        print(f"{'Sconto ' + str(sconto) + '%':<29}{totale_scontato - totale:>7.2f} €")
    print(f"{'TOTALE':<29}{totale_scontato:>7.2f} €")


if __name__ == "__main__":
    carrello = [
        {"nome": "Pane", "prezzo": 2.50, "quantita": 2},
        {"nome": "Latte", "prezzo": 1.20, "quantita": 3},
        {"nome": "Mele", "prezzo": 0.40, "quantita": 6},
        {"nome": "Caffè", "prezzo": 4.90, "quantita": 1},
    ]
    stampa_scontrino(carrello, sconto=10)
