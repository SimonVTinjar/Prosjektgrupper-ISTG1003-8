import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.formula.api as smf

class SkostrHoydeRegresjon:
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = None
        self.regresjon = None
    
    def les_data(self):
        """Leser inn data fra Excel-filen."""
        try:
            self.df = pd.read_excel(self.file_path)
            print("Kolonner i datasettet:", self.df.columns)
        except FileNotFoundError:
            print(f"Filen {self.file_path} ble ikke funnet.")
    
    def beregn_regresjon(self):
        """Utfører regresjonsanalyse."""
        if self.df is not None:
            self.regresjon = smf.ols('hoyde ~ skostr', data=self.df).fit()
            print("Regresjon beregnet.")
        else:
            print("Ingen data tilgjengelig for regresjonsanalyse.")
    
    def plott_regresjon(self, filnavn='plot0.pdf'):
        """Plotter regresjonslinjen og lagrer figuren som en PDF-fil."""
        if self.df is not None:
            sns.lmplot(x='skostr', y='hoyde', data=self.df, ci=None)
            plt.xlim(34, 50)
            plt.ylim(140, 220)
            plt.ylabel('Høyde [cm]')
            plt.xlabel('Skostr [EU]')
            
            try:
                # Lagre direkte uten å spesifisere sti (lagres i samme mappe som programmet kjører)
                plt.savefig(filnavn, format="pdf", bbox_inches='tight')
                print(f"Figur lagret som: {filnavn}")
            except Exception as e:
                print(f"Feil ved lagring av figur: {e}")
            plt.show()
        else:
            print("Ingen data tilgjengelig for plotting.")
    
    def print_polyfit(self):
        """Printer koeffisienten fra numpy polyfit."""
        if self.df is not None:
            polyfit_result = np.polyfit(self.df['skostr'], self.df['hoyde'], 1)
            print(f"Koeffisienten fra polyfit: {polyfit_result[0]}")
        else:
            print("Ingen data tilgjengelig for polyfit-beregning.")

# Bruk av klassen
regresjon_analyse = SkostrHoydeRegresjon('skostr_hoyde.xlsx')
regresjon_analyse.les_data()
regresjon_analyse.beregn_regresjon()
regresjon_analyse.plott_regresjon('plot0.pdf')  # Filen skal lagres i samme mappe som programmet
regresjon_analyse.print_polyfit()
