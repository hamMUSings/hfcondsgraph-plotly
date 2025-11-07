FROM debian:trixie-slim
RUN apt update
RUN apt install -y  python3 python3-pip curl imagemagick
RUN pip install pandas plotly plotly[express] --break-system-packages  
RUN pip install kaleido --upgrade --break-system-packages
RUN kaleido_get_chrome
RUN apt-get -y install libnss3 libatk-bridge2.0-0 libcups2 libxcomposite1 libxdamage1 libxfixes3 \
                    libxrandr2 libgbm1 libxkbcommon0 libpango-1.0-0 libcairo2 libasound2
WORKDIR /home
COPY ./*.sh /home/plotly/
COPY ./*.py /home/plotly/
WORKDIR /home/plotly
RUN mkdir output
RUN chmod +x hfconds-get-format.sh
RUN chmod +x wrapper-hfconds.sh 
CMD ./wrapper-hfconds.sh
