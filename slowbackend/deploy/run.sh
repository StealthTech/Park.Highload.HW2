#!/bin/bash

source env/bin/activate && cd slowbackend && gunicorn slowbackend.wsgi -b 127.0.0.1:8000
