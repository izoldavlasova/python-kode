from random import randint
from celle import Celle

class Rutenett:
    def __init__(self, rader, kolonner):
        self._ant_rader = rader
        self._ant_kolonner = kolonner
        self._rutenett = [[]]
        self._rutenett = self._lag_tomt_rutenett()


    def _lag_tomt_rutenett(self):
        list1 = []
        a = self._ant_rader
        while a > 0:
            list1.append(self._lag_tom_rad())
            a -= 1
        return list1

    def _lag_tom_rad(self):
        list0 = []
        a = self._ant_kolonner
        while a > 0:
            list0.append(None)
            a -= 1
        return list0

    def fyll_med_tilfeldige_celler(self):
        for i in range(self._ant_rader):
            for j in range(self._ant_kolonner):
                self.lag_celle(i, j)

    def lag_celle(self, rad, kol):
        cell1 = Celle()
        a = randint(0, 2)
        if a == 0:
            cell1.sett_levende()
        self._rutenett[rad][kol] = cell1

    def hent_celle(self, rad, kol):
        if 0 <= rad < self._ant_rader and 0 <= kol < self._ant_kolonner:
            return self._rutenett[rad][kol]
        else:
            return None

    def tegn_rutenett(self):
        print("\n\n\n")
        for i in range(self._ant_rader):
            for j in range(self._ant_kolonner):
                print(self._rutenett[i][j].hent_status_tegn(), end="")
            print()

    def _sett_naboer(self, rad, kol):
        for i in range(rad-1,rad+2):
            for j in range(kol-1, kol+2):
                if i == rad and j == kol:
                    continue
                a = self.hent_celle(i, j)
                if a is not None:
                    self.hent_celle(rad, kol).legg_til_nabo(a)


    def koble_celler(self):
        for i in range(self._ant_rader):
            for j in range(self._ant_kolonner):
                self._sett_naboer(i, j)

    def hent_alle_celler(self):
        list0 = []
        for i in range(self._ant_rader):
            for j in range(self._ant_kolonner):
                list0.append(self.hent_celle(i, j))
        return list0

    def antall_levende(self):
        b = 0
        for i in range(self._ant_rader):
            for j in range(self._ant_kolonner):
                if self.hent_celle(i, j).er_levende():
                    b += 1
        return b
