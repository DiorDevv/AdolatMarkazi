
make run:
	python manage.py runserver

make mig:
	python manage.py makemigrations
	python manage.py migrate

make shell:
	python manage.py shell
make test:
	python manage.py test

make collectstatic:
	python manage.py collectstatic --noinput
make createsuperuser:
	python manage.py createsuperuser