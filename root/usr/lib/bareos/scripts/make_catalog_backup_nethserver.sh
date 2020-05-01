#!/usr/bin/bash

#
# wrapper to send the good ENV : https://docs.postgresql.fr/10/libpq-envars.html
#
export PGPORT=55434
scl enable rh-postgresql12 -- /usr/lib/bareos/scripts/make_catalog_backup.pl MyCatalog
