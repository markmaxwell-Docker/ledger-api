# ledger-api

Fernhill Pay's transfer service. Fernhill Pay is a fictional company, and this
repo exists only for the Docker Sandboxes use-case demo.

Run the tests:

    python3 -m unittest discover -s tests -v

Build the image:

    docker build -t fernhill/ledger-api:dev .
