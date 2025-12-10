<!-- TÍTULO + LOGO -->
<p align="left">
  <!-- Cambia la ruta por la de tu imagen del carrito -->
  <img src="docs/img/carrito.png"
       alt="Carrito logo"
       width="90"
       style="vertical-align:middle; margin-right:10px;">
  <span style="font-size:2.8rem; font-weight:700; color:#0d47a1;">
    Carrito
  </span>
</p>

Nuestro carrito controlado con un **ESP32** y un **L298N**, manejado desde el celular vía **Bluetooth**.

---

<!-- COLABORADORES (BADGES AL ESTILO GITHUB) -->
<p>
  <a href="#">
    <img src="https://img.shields.io/badge/Julio%20César%20Maldonado%20Acuña-collaborator-1565c0?style=flat-square&labelColor=0d47a1&logo=github&logoColor=white">
  </a>
  <a href="#">
    <img src="https://img.shields.io/badge/Roberto%20Emiliano%20Ortiz%20Cumpian-collaborator-1565c0?style=flat-square&labelColor=0d47a1&logo=github&logoColor=white">
  </a>
  <a href="#">
    <img src="https://img.shields.io/badge/Ricardo%20Martin%20Pugliesse%20Macias-collaborator-1565c0?style=flat-square&labelColor=0d47a1&logo=github&logoColor=white">
  </a>
  <a href="#">
    <img src="https://img.shields.io/badge/Felipe%20Pinzon%20Segura-collaborator-1565c0?style=flat-square&labelColor=0d47a1&logo=github&logoColor=white">
  </a>
  <a href="#">
    <img src="https://img.shields.io/badge/Grupo-IM%20--%202-1e88e5?style=flat-square&labelColor=0d47a1">
  </a>
</p>

---

## Descripción

Este proyecto consiste en la construcción y programación de un **carrito controlado por un ESP32**, utilizando un **driver L298N** para manejar dos motores de corriente directa (DC):

- Un motor de **tracción** para avanzar y retroceder.  
- Un motor de **dirección** para girar las llantas.

El control del movimiento se realiza mediante un **teléfono celular** que envía comandos por **Bluetooth (BLE / UART)** al ESP32.  
El ESP32 interpreta esos comandos y genera señales **PWM** hacia el L298N para ajustar la **velocidad** y el **sentido de giro** de cada motor.

El software está desarrollado en **MicroPython**, aprovechando:

- Módulos de Bluetooth del ESP32.  
- PWM por hardware para el control preciso de los motores.  

Este README sirve como **introducción** al resto de la documentación del proyecto:
código, diagramas de conexión, pruebas y posibles mejoras.

---
