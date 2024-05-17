#!/usr/bin/env bash
# populate database
echo "Enter your username"
read -r usr
echo "Enter your hostname"
read -r host
echo "Enter your Database's password"
read -r pwd
echo "drop database if exists ACME" | sudo mysql -u"$usr" -h"$host"
# Execute each command, and ensure that the next command is executed only if the previous one succeeds
D='ACME' u=$usr h=$host p=$pwd python3 populate_states_cities_1.py && \
D='ACME' u=$usr h=$host p=$pwd python3 populate_states_cities_2.py && \
D='ACME' u=$usr h=$host p=$pwd python3 populate_institutions.py && \
D='ACME' u=$usr h=$host p=$pwd python3 objects_creation_relationships.py && \
D='ACME' u=$usr h=$host p=$pwd python3 -m api.v1.app
