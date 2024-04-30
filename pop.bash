#!/usr/bin/env bash
echo "Enter your Database's password"
read -r pwd
D='ACME' u='root' h='localhost' p=$pwd python3 populate_states_cities_1.py
D='ACME' u='root' h='localhost' p=$pwd python3 populate_states_cities_2.py
D='ACME' u='root' h='localhost' p=$pwd python3 populate_institutions.py
D='ACME' u='root' h='localhost' p=$pwd python3 main_test_2.py
D='ACME' u='root' h='localhost' p=$pwd python3 -m api.v1.app
