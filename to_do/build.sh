pip install -r requirements.txt

#!/bin/bash

# Install dependencies
pip install -r requirements.txt

# Run Django collectstatic

python manage.py collectstatic --noinput
python manage.py migrate