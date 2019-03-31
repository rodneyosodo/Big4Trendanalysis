FROM python
LABEL maintainer="blackd0t@protonmail.com"

#RUN mkdir /code
WORKDIR /code
COPY . /code/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN python -c "import nltk;nltk.download('stopwords')"

EXPOSE 80
CMD ["python", "api.py"]
