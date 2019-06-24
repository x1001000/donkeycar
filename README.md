## 0. install this fork
https://github.com/tawnkramer/donkey
## 1. get some data
`python manage.py drive`
## 2. train a model
`python manage.py train --tub data/some_data --model models/some_model.h5 --type rnn`
## 3. test a model
`python manage.py drive --model models/some_model.h5 --type rnn`
