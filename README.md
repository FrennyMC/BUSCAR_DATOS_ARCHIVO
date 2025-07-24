# 🦠 TICO SEGURO COVID

## 📌 Descripción General del Programa

**TICO SEGURO COVID** es una aplicación de escritorio desarrollada en **Python** utilizando la biblioteca **Tkinter**, cuyo objetivo es mostrar de forma visual diferentes documentos relacionados con la salud de una persona, en el contexto del control sanitario por COVID-19.

Se simula una especie de **pase digital** con una interfaz gráfica simple, donde se pueden visualizar la **cédula de identidad**, el **certificado de vacunación** y el **resultado de una prueba PCR**.

---

## 🎯 Objetivo Principal

Brindar una forma **sencilla y visual** de consultar e identificar archivos gráficos (como cédula, vacunas y prueba PCR) mediante botones en una interfaz amigable.

---

## 🖼️ Funcionamiento del Programa

### 🪟 Interfaz Principal

- Se abre una ventana con fondo azul y un encabezado que dice **"TICO SEGURO COVID"**.
- Se muestra el **nombre de la persona**, leído desde un archivo llamado `persona.txt`.

### 🗂️ Carga de Archivos

El programa carga cuatro imágenes:

- `Zona_Blanca.gif` → Logo principal (imagen decorativa).
- `cedula.txt` → Contiene el nombre del archivo de la cédula (por ejemplo: `cedula.gif`).
- `vacunas.txt` → Contiene el nombre del archivo del certificado de vacunas (por ejemplo: `vacunas.gif`).
- `examen.txt` → Contiene el nombre del archivo de la prueba PCR (por ejemplo: `prueba_1.gif`).

### 🔘 Botones de Acción

Hay tres botones principales:

- **"Foto ID"** → Muestra la imagen de la cédula.
- **"Vacunas"** → Muestra el certificado de vacunación.
- **"Prueba PCR"** → Muestra el resultado de la prueba.

Cada botón reemplaza la imagen central con el documento correspondiente.

---

## 🔍 Función `BuscarDato`

Esta función:

- Abre un archivo de texto (`.txt`).
- Lee el nombre del archivo de imagen indicado dentro.
- Lo retorna para que pueda ser cargado con `PhotoImage`.
- También realiza validaciones (longitud del contenido y existencia del archivo).

---

## 📁 Estructura Esperada de Archivos

Para que el programa funcione correctamente, todos estos archivos deben estar en la **misma carpeta** que el script `.py`:

|  Cédula            | Vacuna             | Prueba PCR           |
|--------------------|--------------------|--------------------|
| ![ID](img/cedula.gif) | ![Vacuna](img/vacunas.gif) | ![PCR](img/prueba_1.gif) |


