# Aplikácia metód umelej inteligencie na riešenie problému

V druhom zadaní využijete poznatky získané počas semestra na riešenie štandardných problémov klasifikácie na reálnom datasete. Na vypracovanie zadania máte dve alternatívy, variant A a variant B (pričom odovzdávate iba jedno riešenie). Oba varianty sú za 15 bodov. Zadanie vypracujete vo dvojiciach alebo trojiciach - členovia tímu môžu byť z rôznych študijných skupín.

Na vypracovanie zadania môžete použiť ľubovoľný dataset, odporúčame ale použiť niektorý štandardný dataset [z tohto repozitára](https://archive.ics.uci.edu/ml/datasets.php) [alebo z Kaggle](https://www.kaggle.com/datasets). Dávajte si pozor na to, aby dataset bol určený na klasifikáciu a nie na regresiu! Vašou úlohou je potom natrénovať inteligentný model na danom datasete a poskytnúť ju tak, aby dokázal robiť nové predikcie pre údaje podobné tým z datasetu.

Pri vypracovaní zadanie všeobecne máte urobiť tieto kroky (pre oba varianty):

1. predspracovanie údajov - výber príznakov, normalizácia údajov, spracovanie chýbajúcich hodnôt
2. rozdelenie datasetu na trénovaciu a testovaciu množinu
3. návrh a trénovanie modelu
4. testovanie a vyhodnotenie modelu
5. vypracovanie dokumentácie

## Variant A
Vo variante A vytvoríte webovú službu na klasifikácia pomocou Microsoft Machine Learning Studio. Vašou úlohou je navrhnúť experiment podobný ako sme robili na treťom cvičení. Následne natrénovaný model a experiment potrebujete zverejniť ako webovú službu (umožňuje to samotné ML Studio). Súčasťou odovzdávky je aj Python skript, ktorý ukáže funkčnosť webovej služby: pomocou skriptu pošlite request na webovú službu - hodnoty príznakov pre hľadaný príklad, a potom vypíšte odpoveď - výsledok klasifikácie. Pri vytvorení webovej služby sa vám vygeneruje skript na takéto účely, ktorý potrebujete upraviť len minimálne.

Pri riešení zadania vyskúšajte rôzne metódy umelej inteligencie (minimálne 3), všetky s rôznymi nastaveniami parametrov (minimálne 10). Každý model s danými nastaveniami otestujte a zaznamenajte ich presnosť. Spolu by ste mali mať výsledky z minimálne 30 testov.

Štruktúra odovzdávky je nasledovná:

* experiment na ML Studio – natrénujte minimálne tri rôzne modely s 10 nastaveniami parametrov pre každý model; iba online, stačí jeden experiment na jeden model, ponechajte najlepšie nastavenia
* webová služba na ML Studio – iba pre najpresnejší model; iba online
* skript na ukážku funkčnosti webovej služby – pošlite mailom
* dokumentácia – popíšte váš postup, aké modely ste testovali, s akými nastaveniami a napíšte aj výsledky testovania jednotlivých modelov. (max. 2 strany A4, voľná forma); pošlite mailom

## Variant B
Vo variante B vytvoríte lokálnu implementáciu jedného modelu umelej inteligencie, pričom pri riešení môžete používať ľubovoľnú knižnicu v Pythone (nové knižnice viete nainštalovať pomocou príkazu [`pip`](https://pip.pypa.io/en/stable/user_guide/)). Oproti variantu A je potrebné implementovať iba jeden model, ale aj ten potrebujete otestovať s rôznymi nastaveniami (minimálne 10 testov). Odovzdáte skript spolu s datasetom - riešenie musí byť out-of-the-box, t.j. spustiteľné bez potreby konfigurácie.

Štruktúra odovzdávky je nasledovná:

* zazipovaný projekt – obsahuje dataset a skript s modelom; pošlite mailom
* dokumentácia – popíšte váš postup, ako ste vytvorili model a napíšte aj výsledky testovania s jednotlivými nastaveniami. (max. 2 strany A4, voľná forma); pošlite mailom

Vo variante B máte možnosť implementovať aj expertný systém, fuzzy systém, alebo evolučný algoritmus pre optimalizáciu, v tomto prípade kontaktujte cvičiaceho a na zadaní sa dohodne individuálne.

## Deadline a odovzdávka
Vaše riešenia odovzdáte mailom na jan.magyar@tuke.sk do 7. 5. 2020. Pre získanie bodov potrebujete vaše riešenie aj obhájiť do konca 13. týždňa (15. 5. 2020). 

## Hodnotenie
Za riešenie môžete získať maximálne 15 bodov a to nasledovne:

* predspracovanie údajov – 3 body
* návrh a implementácia modelu – 2 body
* testovanie modelu – 2 body
* nasadenie modelu (pre variant A: webová služba a ukážka, pre variant B: ukážka) – 3 body
* dokumentácia - 2 body
* obhajoba - 3 body
