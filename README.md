# Curso pofesional de python -- Platzi

Para que este proyecto funcione a la perfeccion debes crear un entorno virtual y activarlo.

<pre style="background: #5444f4; color: white;">
> python -m venv venv
</pre>

Activamos el entorno virtual

<pre style="background: #5444f4; color: white;">
> .\venv\Scripts\activate
</pre>

Para instalar la dependencias utilizadas en este proyecto, ejecutamos **pip** con el archivo **requirements.txt**.

<pre style="background: #5444f4; color: white;">
> pip -r requirements
</pre>
</br>

## Tipado dinamico con python 

Para manejar el tipado dinamico con python hacemos uso del modulo **mypy** el cual requiere ser instalado si no ejecutaste el comando anterior, lo puedes hacer de la siguiente manera.
</br>

<pre style="background: #5444f4; color: white;">
> pip install mypy
</pre>
Si deseamos que python se comporte como un lenguaje de **tipado estatico** debemos ejecutar el comando mypy con el modulo que deseamos ejecutar.
</br>
<pre style="background: #5444f4; color: white;">
> mypy palindrome.py --check-untyped-defs
</pre>
