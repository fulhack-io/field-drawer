FROM tiangolo/uwsgi-nginx:python3.5

RUN pip install flask simplejson

# Add app configuration to Nginx
COPY nginx.conf /etc/nginx/conf.d/

# Copy sample app
COPY ./app /app