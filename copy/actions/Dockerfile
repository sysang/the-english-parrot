# Extend the official Rasa SDK image
FROM rasa/rasa-sdk:1.10.2

# Change back to root user to install dependencies
USER root

# To install system dependencies
RUN apt-get update -qq && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# To install packages from PyPI
RUN pip install -U --no-cache-dir mailchimp3~=3.0.2 \
                            oauth2client~=4.1.2 \
                            gspread~=3.0.0 \
                            beautifulsoup4~=4.6.3 \
                            requests~=2.21.0 \
                            geopy~=1.18.1 \
                            pandas~=0.24.1 \
                            algoliasearch>=2.0,<3.0 \
                            spacy~=2.1.9

RUN python -m spacy download en

# Switch back to non-root to run code
USER 1001
