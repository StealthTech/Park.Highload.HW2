#!/bin/bash

gunicorn slowbackend.wsgi -b 127.0.0.1:8000
