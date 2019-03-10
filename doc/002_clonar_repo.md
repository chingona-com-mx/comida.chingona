## Clonar repositorio de comida chingona.

Pasos para clonar el repositorio de comida chingona y se hacer el primer commit.


```
# clonamos repo de github
git clone git@github.com:pixelead0/comida.chingona.git

cd comida.chingona/

#Creamos nuestro primer archivo
echo "# comida.chingona" >> README.md

# Añadir cambios al Index
git add README.md

# Incluye el archivo en el HEAD
git commit -m "first commit"

# Envía cambios a tu repositorio remoto.
git push -u origin master
```

## Video:

[![asciicast](https://asciinema.org/a/232786.svg)](https://asciinema.org/a/232786)