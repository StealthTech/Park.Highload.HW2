#!/bin/bash

source env/bin/activate && gunicorn slowbackend/slowbackend.wsgi -b 127.0.0.1:8000
