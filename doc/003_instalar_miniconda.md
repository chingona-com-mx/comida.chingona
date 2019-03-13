# Primeros pasos para crear un proyecto en django

## Requisitos:
- Contar con un editor de código instalado como puede ser Sublime Text, Atom, Brackets, Notepad++, Vim, Emacs y otro que sea de tu preferencia.
- Instalar `Python 3` en tu laptop, para ello sugerimos descargar Miniconda para Python 3.7 para tu sistema operativo e instalarlo con las opciones por default.
- `Miniconda`: Para instalar Python en las plataformas Windows, Mac OS y Linux con características homogéneas. https://conda.io/miniconda.html (Para descargas) https://conda.io/docs/user-guide/install/index.html (Instrucciones de instalación para cada sistema operativo)
- `Django`: Un framework de desarrollo web de código abierto, escrito en Python, que respeta el patrón de diseño conocido como Modelo–Vista–Template.

## Pasos para instalar Miniconda desde linux

```
# Descargar miniconda con `python 3.7`
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
ls -l

#Le damos permisos de ejecución
chmod +x Miniconda3-latest-Linux-x86_64.sh

#Ejecutamos el script de instalación
./Miniconda3-latest-Linux-x86_64.sh

#Reiniciamos el usuario
source ~/.bashrc

#Ejecutamos conda
conda

## Instalar django
conda install django
```

## Vídeo

[![asciicast](https://asciinema.org/a/mCQPsWBpKJVX0gQpwGwiNcvax.svg)](https://asciinema.org/a/mCQPsWBpKJVX0gQpwGwiNcvax)
