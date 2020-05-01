# nethserver-bareos

Bareos uses rh-postgresql12, we need to enable scl before to use a bareos script and set the ENV custom port of postgresql (TCP 55434)

for example

- upgrade the database structure

```
  su - postgres  -c "export PGPORT=55434;scl enable rh-postgresql12 /usr/lib/bareos/scripts/update_bareos_tables"
```
- backup database to `/var/lib/bareos`

```
  export PGPORT=55434;scl enable rh-postgresql12 -- /usr/lib/bareos/scripts/make_catalog_backup.pl MyCatalog
```
