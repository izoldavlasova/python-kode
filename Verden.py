from rutenett import Rutenett

class Verden:
    def __init__(self, rader, kolonner):
        self._rutenett = Rutenett(rader, kolonner)
        self._generasjonsnummer = 0
        self._rutenett.fyll_med_tilfeldige_celler()
        self._rutenett.koble_celler()

    def tegn(self):
        self._rutenett.tegn_rutenett()
        print("Generasjonsnummer: " + str(self._generasjonsnummer))
        print("Antall levende celler: " + str(self._rutenett.antall_levende()))

    def oppdatering(self):
        for i in range(self._rutenett._ant_rader):
            for j in range(self._rutenett._ant_kolonner):
                self._rutenett.hent_celle(i, j).tell_levende_naboer()
                self._rutenett.hent_celle(i, j).oppdater_status()
        self._generasjonsnummer += 1
