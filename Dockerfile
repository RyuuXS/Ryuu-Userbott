# Using Python Slim-Buster
FROM vckyouuu/geezprojects:buster
#━━━━━ Userbot Telegram ━━━━━
#━━━━━ By Ryuu-Userbott ━━━━━

RUN git clone -b Ryuu-Userbott https://github.com/RyuuXS/Ryuu-Userbott /root/userbot
RUN mkdir /root/userbot/.bin
RUN pip install --upgrade pip setuptools
WORKDIR /root/userbot

#Install python requirements
RUN pip3 install -r https://raw.githubusercontent.com/RyuuXS/Ryuu-Userbott/Ryuu-Userbott/requirements.txt

EXPOSE 80 443

# Finalization
CMD ["python3", "-m", "userbot"]
