#!/bin/sh
# Reset environment

sqlite3 fifth.db << END_SQL
.read country_table.sql
END_SQL
