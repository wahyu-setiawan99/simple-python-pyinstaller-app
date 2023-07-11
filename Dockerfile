# start by pulling the python image
FROM python:3.8-alpine

# switch working directory
WORKDIR /app

# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt


# configure the container to run in an executed manner
ENTRYPOINT [ "python" ]

CMD ["add2vals.py" ]