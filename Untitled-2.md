POST /products/create
DELETE /products/create


start einer Virtuellen Maschine
REST

GET /vm -> ressourcen Metadaten CPU, MEM...
PUT /vm/12 -> {"state": 0 //1 etc., "memorySize": 12Gb} -> aktionen sind nicht sichtbar

PUT /vm/...

GET, POST, PATCH, DELETE DDL/MUTATIONS

Datennormalisierung -> Kunden sollen überprüft werden und die Adressen nach Adressprüfung angepasst werden. Es kann das nach der Ausführung Daten geändert sind oder nicht.
POST /kunde/...

GET /kunde/12
....

Wie viele Aufrufe?


-> REST bin ich Ressourcen CRUD


-> GraphQL -> Mutationen eigene Methoden


### Ressource identigier Ressource

/kunde/vertrag/vertragsversion
/anbieter/anbieterkategorie...
