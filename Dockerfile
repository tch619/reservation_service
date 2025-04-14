FROM python:3.11

WORKDIR /app
COPY .. /app


RUN pip install --no-cache-dir -r requirements.txt

# wait-for-it adn start.sh
COPY wait-for-it.sh /wait-for-it.sh
COPY start.sh /start.sh
RUN chmod +x /wait-for-it.sh /start.sh

CMD ["/start.sh"]