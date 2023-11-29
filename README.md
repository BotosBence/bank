Bank szoftver
Bankok fiókjainak és ügyfeleinek nyilvántartására

Szoftveres megvalósítás:
- Új bank felvétele
- Új bankfiók felvétele
- Bankfiókok listázása
- Bankfiók törlése
- Ügyfél felvétele
- Ügyfél listázása
- Ügyfél törlése


Bank osztály
bankname  lista: [bank neve,székhely]
bankoffices lista: [bank neve,fiókok]


Metódusai: 
__init__(self): listák definiálása
add_new_bank(self): - új bank felvétele a bankname listába
check_bank_name:  - a bank bejegyzése létezik-e a bankname listában

add_bankoffices(self, újbank_neve): - új bankfiók felvétele
check_bank(self, bank_neve): - ha nem létezik a bank nevének bejegyzése a bankname listában, 
						akkor felkínálja a lehetőségét, hogy felveszi.
del_bankoffices(self): -  kitörli a megadott nevű bankfiókot
list_bankoffices(self, bankname): - bankfiókok listázása


Customer osztály

Metódusai: 
__init__(self):  - customer=[]   ügyfelek lista inicializálása
last_cust_id(self): - utolsó ügyfélazonostót adja vissza
add_customer(self): - ügyfél felvétele  
list_customer(self): - ügyfelek listázása
