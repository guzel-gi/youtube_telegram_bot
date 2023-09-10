FROM python

WORKDIR /youtube_bot

COPY . /youtube_bot

ENV token="<YOUR_TELEGRAM_BOT_TOKEN>"

RUN pip install -r requirements.txt

ENTRYPOINT ["python","bot.py"]

