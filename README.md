Iniciar o projeto Django

```

python -m venv venv
. venv/bin/activate
pip install django
django-admin startproject project .
python manage.py startapp contact


```

Configurar o git

```

git config --global user.name "matheusbuenowb"
git config --global user.email "matheus@gmail.com"
git config --global init.defaultBranch main

#configure o git.ignore, pode copiar um padrão básico do google relacionado a Djang

git init
git add .
git commit -m "escreva aqui as alterações desse commit"
git remote add origin URL_DO_GIT
git push -u origin main

```

Migrando a base de dados do Django

```
python manage.py makemigrations
python manage.py migrate

```

Criando e modificando a senha de um super usuário Django

```
python manage.py createsuperuser
python manage.py changepassword USERNAME

```