import pandas as pd


#Aufgabe3+4: Funktionen (Befehle) testen
def print_begriffe():
    #Datenstruktur: Dictionary (Hashmap)
    begriffe = {  'KI': 'Systeme loesen Aufgaben, die intelligentes Verhalten erfordern',
    'Machine Learning': 'Modelle lernen Muster aus Daten',
    'Deep Learning': 'ML mit mehrschichtigen neuronalen Netzen'
    }


    for k, v in begriffe.items():
        print(f'{k}: {v}')

#Methodenaufruf/Funktionsaufruf       
#print_begriffe()

#Aufgabe 4: Durchschnittspreis Änderungen
def berechne_durchschnittspreis():
    preise = [180000, 240000, 380000, 130000]
    durchschnitt = sum(preise) / len(preise)
    print('Durchschnittspreis:', round(durchschnitt, 2))

    df = pd.read_csv('../../notebooks/daten/haeuser.csv')
    df.head()

def berechne_durchschnittspreis_neu():
    preise = [180000, 440000, 380000, 230000]
    durchschnitt = sum(preise) / len(preise)
    print('Durchschnittspreis:', round(durchschnitt, 2))

    df = pd.read_csv('../../notebooks/daten/haeuser.csv')
    df.head()

#test: Methoden/Funktionsaufruf
berechne_durchschnittspreis()
berechne_durchschnittspreis_neu()

#Lösung: 5 Datenbasiert vs. Regelbasiert Was macht Notebooks? 
# Ein Notebook fuehrt Code schrittweise aus. 
# In der geaenderten Zelle wurden Listenwerte 
# angepasst und der neue Durchschnitt berechnet. 
# Das ist datenbasiert, weil das Ergebnis von den 
# eingegebenen Daten abhaengt. Ein fester Wenn-Dann-Block 
# waere regelbasiert.