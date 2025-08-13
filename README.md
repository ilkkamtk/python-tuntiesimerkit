# python-tuntiesimerkit

[suomi](README.md) | [english](README_en.md)

## Moduuli 2 - muuttujat ym.

Kirjoita Python-ohjelma, joka kysyy käyttäjältä kaksi lukua: ympyrän säteen ja neliön sivun pituuden. Ohjelman tulee laskea molempien kuvioiden pinta-alat ja tallentaa ne muuttujiin. Lopuksi ohjelman tulee tulostaa molemmat pinta-alat.

---

Kirjoita ohjelma, joka kysyy käyttäjältä kolmen eri hedelmän määrän kilogrammoina.
Ohjelma laskee hinnan käyttäen seuraavia kiinteitä kilohintoja:

* Banaani: 2.85 €/kg
* Omena: 3.15 €/kg
* Appelsiini: 4.05 €/kg

Ohjelma laskee ja näyttää jokaisen hedelmän hinnan erikseen sekä kaikkien hedelmien yhteishinnan.

**Esimerkki ohjelman toiminnasta**

```monospace
Anna banaanien määrä (kg).
1.2

Anna omenoiden määrä (kg).
2.5

Anna appelsiinien määrä (kg).
0.8

Ostosten yhteenveto:
Banaanit: 3.42 €
Omenat: 7.88 €
Appelsiinit: 3.24 €
Yhteensä: 14.54 €
```

---

Kirjoita ohjelma, joka toimii yksinkertaisena noppasimulaattorina. Ohjelman tulee arpoa ja tulostaa kahden nopan heitto. Toinen noppa on kuusitahoinen (luvut 1–6) ja toinen on kaksikymmentahoinen (luvut 1–20). Lopuksi ohjelman tulee laskea ja tulostaa molempien noppien yhteissumma.

---

## Moduuli 3 - Valintarakenne (if)

Kirjoita ohjelma, joka kysyy käyttäjältä hänen ikänsä. Ohjelman tulee tarkistaa ikä ja kertoa, onko henkilö riittävän vanha äänestämään Suomen eduskuntavaaleissa. Jos henkilö ei ole täysi-ikäinen, ohjelman tulee ilmoittaa, montako vuotta hänellä on vielä jäljellä täysi-ikäisyyteen ja äänestysoikeuteen. Suomessa äänestysikäraja on 18 vuotta.

---

Kirjoita ohjelma, joka kysyy käyttäjältä sähkönkulutusta kilowattitunteina (kWh). Ohjelman tulee laskea sähkölasku kolmen eri porrastetun hinnan mukaan ja tulostaa loppusumma.

* **Ensimmäiset 50 kWh** maksavat 10 senttiä/kWh.
* **Seuraavat 150 kWh** maksavat 8 senttiä/kWh.
* **Yli 200 kWh** menevä kulutus maksaa 6 senttiä/kWh.

---

Kirjoita ohjelma, joka kysyy käyttäjältä hänen suorituksensa kolmella eri osa-alueella: fysiikasta, matematiikasta ja kemiasta. Ohjelman tulee kertoa, saiko käyttäjä stipendin.

Stipendi myönnetään, jos:

käyttäjän tulos on yli 90 sekä fysiikassa että matematiikassa
tai

käyttäjän tulos on yli 95 kemiassa.

Lisäksi ohjelman on ilmoitettava, jos tulos jossain aineessa on alle 50. Tällöin käyttäjä ei voi saada stipendiä, vaikka muut ehdot täyttyisivätkin.

## Moduuli 4 - Alkuehdollinen toistorakenne (while)

Kirjoita ohjelma, joka kysyy käyttäjältä positiivisen kokonaisluvun. Ohjelman tulee laskea ja tulostaa kaikki parilliset luvut 0:sta käyttäjän antamaan lukuun asti. Jos käyttäjä antaa negatiivisen luvun tai nollan, ohjelma tulostaa virheilmoituksen.

---

Kirjoita ohjelma, joka pyytää käyttäjältä kokonaislukuja yksi kerrallaan. Ohjelma laskee lukujen summan ja kysyy uutta lukua, kunnes summa ylittää arvon 1000. Tämän jälkeen ohjelma tulostaa loppusumman ja ilmoittaa, kuinka monta lukua käyttäjältä kysyttiin.

---

Kirjoita ohjelma, joka simuloi putoavaa esinettä.

Ohjelma kysyy käyttäjältä esineen alkukorkeuden metreinä. Tämän jälkeen se laskee ja tulostaa esineen korkeuden sekunti sekunnilta **while-silmukkaa** käyttäen. Silmukka jatkuu, kunnes esineen korkeus on nolla tai alle sen. Lopuksi ohjelma tulostaa kokonaisajan, joka kului putoamiseen.

Esineen putoamismatka ($s$) ajan ($t$) funktiona lasketaan kaavalla: $s = \frac{1}{2}gt^2$, missä putoamiskiihtyvyys ($g$) on noin $9.81 m/s^2$.

Ohjelman tulee siis jokaisella silmukan kierroksella laskea, kuinka paljon esine on pudonnut, ja vähentää se alkukorkeudesta.

## Moduuli 5 - Listarakenne ja läpikäyvä toistorakenne (for)

Kirjoita ohjelma, joka kysyy käyttäjältä kokonaisluvun. Ohjelman tulee laskea ja tulostaa kaikki parilliset luvut 0:sta käyttäjän antamaan lukuun asti käyttäen **for-silmukkaa**. Jos käyttäjä antaa negatiivisen luvun tai nollan, ohjelma tulostaa virheilmoituksen.

---

Kirjoita ohjelma, joka pyytää käyttäjältä lukuja siihen saakka, kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi. Luvut tallennetaan listaan. Tämän jälkeen ohjelman tulee käydä listan alkiot läpi ja tulostaa ne yksilölliset luvut, jotka ovat suurempia kuin 100. Tulosta jokainen luku vain kerran, vaikka se olisi syötetty useammin kuin kerran.

---

## Moduuli 6 - Funktio

Kirjoita funktio, joka ottaa parametrinaan kaksi kokonaislukua ja palauttaa niiden summan. Kutsu funktiota pääohjelmassa ja tulosta sen palauttama arvo.

---

Kirjoita funktio, joka saa parametrinaan listan merkkijonoja (esim. nimiä tai sanoja). Funktio palauttaa uuden listan, jossa ovat ainoastaan ne alkuperäisen listan merkkijonot, joiden pituus on yli viisi merkkiä.

Kirjoita pääohjelma, jossa:
1.  Luot esimerkkilistan merkkijonoista (esim. eläinten nimiä: "kissa", "koira", "elefantti", "leijona", "kirahvi").
2.  Kutsut luomaasi funktiota tällä listalla.
3.  Tulostat sekä alkuperäisen listan että funktion palauttaman suodatetun listan.

---

## Moduuli 7 - Monikko, joukko ja sanakirja

Kirjoita ohjelma, joka kysyy käyttäjältä kolme eri hedelmää ja niiden määrät kilogrammoina. Tallenna hedelmät ja niiden määrät sanakirjaan, jossa hedelmän nimi on avain ja määrä arvo. Ohjelman tulee tulostaa sanakirja.

---

Kirjoita ohjelma, joka kysyy käyttäjältä lukuja yksi kerrallaan. Ohjelma jatkaa lukujen kysymistä, kunnes käyttäjä syöttää luvun 0. Luvut tallennetaan listaan. Tämän jälkeen ohjelman tulee tulostaa lista ilman duplikaatteja eli vain yksilölliset luvut, jotka on syötetty.

Vihje:
Voit luoda listasta uuden joukon (set), joka poistaa automaattisesti kaikki duplikaatit. Tämän jälkeen voit muuttaa joukon takaisin listaksi, jos tarvitset listan toimintoja.

---

Kirjoita ohjelma, joka toimii yksinkertaisena puhelinmuistiona. Ohjelma kysyy käyttäjältä, haluaako hän lisätä uuden yhteystiedon, hakea olemassa olevaa yhteystietoa vai lopettaa.

Jos käyttäjä valitsee uuden yhteystiedon lisäämisen, ohjelma kysyy yhteystiedon nimen ja puhelinnumeron.

Jos käyttäjä valitsee haun, ohjelma kysyy nimen ja tulostaa vastaavan puhelinnumeron.

Jos käyttäjä haluaa lopettaa, ohjelman suoritus päättyy.

Ohjelman tulee tallentaa tiedot sanakirjaan ja antaa käyttäjän valita toimintoja useita kertoja, kunnes hän päättää lopettaa. Ohjelman on myös käsiteltävä tilanne, jossa käyttäjä yrittää hakea olematonta nimeä.

## Moduuli 8 - Relaatiotietokannan käyttö



