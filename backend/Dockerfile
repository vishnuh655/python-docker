ARG PYTHON_TAG
ARG BACKEND_PORT
ARG APP_PACKAGE_NAME
ARG WSGI_APP
FROM python:${PYTHON_TAG}
WORKDIR /code
RUN apk add --no-cache \
                        gcc \
                        musl-dev \
                        linux-headers \
                        build-base \
                        mariadb-connector-c-dev
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
EXPOSE ${BACKEND_PORT}
# ENV WSGI_APP ${WSGI_APP}
# ENV BACKEND_PORT ${BACKEND_PORT}
ENV APP_PACKAGE_NAME ${APP_PACKAGE_NAME}
COPY . .
# CMD [ "gunicorn"  , \
#         "--bind :8000" ,  \
#         "--workers" , "2" ,  \
#         "--timeout" , "3600" ,  \
#         "socimg:application"  \
#     ]
# ENTRYPOINT ["sh", "-c"]
# CMD [ "gunicorn"  , \
#         "--bind ${BACKEND_PORT}" ,  \
#         "--workers" , "2" ,  \
#         "--timeout" , "3600" ,  \
#         "${APP_PACKAGE_NAME} ${WSGI_APP}"  \
#     ]
CMD [ "gunicorn" ,  "socimg:application"]
# CMD gunicorn \
#         --bind :${BACKEND_PORT} \
#         --workers 2 \
#         --timeout 3600 \
#         ${APP_PACKAGE_NAME}:${WSGI_APP}