<!-- PORTADA / HERO -->
<p align="center">
  <!-- Cambia la ruta por donde guardes tu imagen -->
  <img src="docs/img/carrito.png" alt="Carrito ESP32 + L298N" width="260">
</p>

<h1 align="center" style="color:#0d47a1; font-weight:900;">
  Proyecto <span style="color:#1976d2;">“Carrito”</span> ESP32 + L298N
</h1>

<p align="center" style="color:#1565c0; font-size:16px;">
  Control de motores DC con ESP32, driver L298N y Bluetooth desde el celular.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Plataforma-ESP32-1976d2?style=for-the-badge&logo=espressif&logoColor=white">
  <img src="https://img.shields.io/badge/Lenguaje-MicroPython-0d47a1?style=for-the-badge">
  <img src="https://img.shields.io/badge/Driver-L298N-42a5f5?style=for-the-badge">
</p>

---

## 📚 Índice

- [👥 Equipo](#-equipo)
- [🧾 Descripción general](#-descripción-general)
- [🎨 Estilo del proyecto](#-estilo-del-proyecto)
- [⚙️ Componentes principales](#️-componentes-principales)
  - [ESP32](#esp32)
  - [Módulo L298N](#módulo-l298n)
  - [Alimentación y tierras](#alimentación-y-tierras)
- [🧠 Arquitectura del sistema](#-arquitectura-del-sistema)
- [🔌 Conexiones básicas](#-conexiones-básicas)
- [📶 Flujo de comandos desde el celular](#-flujo-de-comandos-desde-el-celular)
- [🎯 Objetivo académico](#-objetivo-académico)
- [🚀 Próximos pasos](#-próximos-pasos)

---

## 👥 Equipo

<div style="border-left:4px solid #0d47a1; padding:0.5rem 1rem; background:#e3f2fd;">
  <p style="margin:0;">
    <b style="color:#0d47a1;">Integrantes:</b><br>
    Julio César Maldonado Acuña<br>
    Roberto Emiliano Ortiz Cumpian<br>
    Ricardo Martin Pugliesse Macias<br>
    Felipe Pinzon Segura
  </p>
  <p style="margin:0.25rem 0 0;">
    <b style="color:#1565c0;">Grupo:</b> IM - 2
  </p>
</div>

<br>

- **Materia:** *(agrega aquí el nombre de la materia)*  
- **Profesor(a):** *(nombre del docente)*  
- **Periodo:** *(ej. Enero–Junio 2025)*  

---

## 🧾 Descripción general

El proyecto **“Carrito”** consiste en el diseño y construcción de un vehículo a escala controlado por un **ESP32**, que maneja dos motores DC mediante el **driver L298N**:

- Un motor de **tracción** para avanzar y retroceder.
- Un motor de **dirección** para girar las llantas.

El control se realiza de forma **inalámbrica**, usando **Bluetooth (BLE tipo UART)** desde un teléfono celular.  
Este README funciona como **introducción** a toda la documentación técnica del proyecto: esquemas, código, pruebas y conclusiones.

---

## 🎨 Estilo del proyecto

El diseño visual del proyecto (documentos, app y presentaciones) sigue una paleta **blanco + azul**:

- 🎨 **Blanco:** claridad, orden y legibilidad.
- 💙 **Azules (#0d47a1, #1565c0, #1976d2):** tecnología, estabilidad y confianza.

> Recomendación: usar esta misma combinación en diapositivas, portada del reporte y en el diseño de la app de control.

---

## ⚙️ Componentes principales

### ESP32

<div style="border-left:4px solid #1976d2; padding:0.5rem 1rem; background:#e3f2fd;">
El <b>ESP32</b> es el “cerebro” del carrito. Se encarga de recibir los comandos del celular por Bluetooth y traducirlos en señales PWM para el driver L298N.
</div>

**Funciones clave del ESP32:**

- Comunicación **Bluetooth (BLE / UART)** con el celular.
- Generación de **PWM** para controlar la velocidad de los motores:
  - `duty_u16` proporcional a la velocidad (0–65535).
- Determinar el sentido de giro:
  - Velocidad positiva → adelante.
  - Velocidad negativa → reversa.
- Administrar comandos como:
  - `F` (Forward), `B` (Backward),
  - `L` / `R` (Left / Right),
  - `S` (Stop),
  - `V###` para ajustar la velocidad.

---

### Módulo L298N

El **L298N** es un **driver de puente H doble** que permite controlar dos motores DC de forma independiente:

- **Canal A:** motor de tracción.  
- **Canal B:** motor de dirección.

**Características relevantes:**

- Puede cambiar el sentido del motor invirtiendo las entradas (IN1/IN2, IN3/IN4).
- Permite control de velocidad mediante señales PWM en las entradas.
- Presenta una **caída de voltaje interna** (~2 V), por lo qu
