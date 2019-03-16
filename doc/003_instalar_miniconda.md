# Primeros pasos para crear un proyecto en django

## Requisitos:
- Contar con un editor de código instalado como puede ser Sublime Text, Atom, Brackets, Notepad++, Vim, Emacs y otro que sea de tu preferencia.
- Instalar `Python 3` en tu laptop, para ello sugerimos descargar Miniconda para Python 3.7 para tu sistema operativo e instalarlo con las opciones por default.
- `Miniconda`: Para instalar Python en las plataformas Windows, Mac OS y Linux con características homogéneas. https://conda.io/miniconda.html (Para descargas) https://conda.io/docs/user-guide/install/index.html (Instrucciones de instalación para cada sistema operativo)
- `Django`: Un framework de desarrollo web de código abierto, escrito en Python, que respeta el patrón de diseño conocido como Modelo–Vista–Template.

## Pasos para instalar Miniconda desde cero en Linux

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

## Pasos para utilizar el contenedor con Miniconda

### Pre-requisitos

+ Tener instalado [Docker](https://docs.docker.com/glossary/?term=installation) ó [podman](https://github.com/containers/libpod/blob/master/docs/tutorials/podman_tutorial.md)

### Obtener el contenedor

Utilizaremos [docker-miniconda](https://hub.docker.com/r/continuumio/miniconda/)

+ Docker
```
docker pull continuumio/miniconda
```

+ podman
```
podman pull continuumio/miniconda
```

### Ejecutar el contenedor

+ Docker
```
docker run -it continuumio/miniconda /bin/bash
```

+ podman
```
podman run -it continuumio/miniconda /bin/bash
```

### Dentro del contenedor instalamos Django

```
# conda install django
```

<dl>
  <dt>Almacenamiento Persistente</dt>
  <dd>Para configurar almacenamiento persistente en contenedores es necesario realizar la siguiente configuración:</dd>
</dl>

+ Crear directorio compartido con el contenedor
```
# mkdir -p /opt/comida.chingona
```

+ Montamos el directorio compartido al ejecutar el contenedor

 + Docker
```
# docker run  -v /opt/comida.chingona:/home -it continuumio/miniconda /bin/bash
```

 + podman
 ```
 # podman run  -v /opt/comida.chingona:/home:Z -it continuumio/miniconda /bin/bash
 ```
