FROM n8nio/n8n:latest

USER root
RUN apk add --no-cache build-base python3 python3-dev py3-pip
USER node
RUN pip3 install --break-system-packages scikit-learn nltk spacy kagglehub
RUN python3 -m spacy download en_core_web_sm -- --break-system-packages