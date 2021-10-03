FROM python:3
ADD HTTPService.py /
RUN pip install requests
CMD [ "python", "./HTTPService.py" ]