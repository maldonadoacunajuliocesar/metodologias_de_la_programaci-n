<!-- LOGO / PORTADA -->
<p align="center">
  <!-- Cambia la URL del logo por la imagen real de tu carrito -->
  <img src="https://via.placeholder.com/140x140.png?text=Carrito" alt="Carrito Logo" width="140">
</p>

<h1 align="center" style="color:#0d47a1;">
  Proyecto "Carrito" ESP32 + L298N
</h1>

<p align="center">
  <b style="color:#1565c0;">Control de motores DC con ESP32, L298N y comunicación Bluetooth</b>
</p>

<p align="center">
  <sub style="color:#1976d2;">Grupo IM - 2</sub>
</p>

---

## 👥 Integrantes del equipo

> <span style="color:#0d47a1;"><b>Proyecto desarrollado por:</b></span>

- Julio César Maldonado Acuña  
- Roberto Emiliano Ortiz Cumpian  
- Ricardo Martin Pugliesse Macias  
- Felipe Pinzon Segura  

**Grupo:** IM - 2  
**Materia:** (agrega aquí el nombre de la materia)  
**Fecha:** (agrega la fecha de entrega)

---

## 🧾 Descripción general del proyecto

Este repositorio documenta el desarrollo de un **carrito controlado por ESP32**, utilizando un módulo **L298N** para manejar dos motores de corriente directa (DC):

- Un motor de **tracción** (avance y retroceso).
- Un motor de **dirección** (giro de llantas).

El ESP32 se comunica con un **teléfono celular vía Bluetooth (BLE / UART)** y recibe comandos para controlar el movimiento del carrito.  
La idea principal es integrar:

- **Electrónica de potencia** (L298N + motores).
- **Microcontrolador ESP32** (lógica de control).
- **Comunicación inalámbrica** (Bluetooth).
- **Alimentación separada** para motores y lógica, con **tierra común (GND compartida)**.

Este README funciona como **introducción** a la parte electrónica, de control y de programación del proyecto.

---

## 🔵⚪ Pale
