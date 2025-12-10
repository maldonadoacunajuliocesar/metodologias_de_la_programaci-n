<!-- LOGO / TÍTULO -->
<p align="center">
  <!-- Cambia esta ruta por la de tu imagen -->
  <img src="docs/img/carrito.png" alt="Carrito ESP32 + L298N" width="220">
</p>

<h1 align="center" style="color:#0d47a1;">Carrito ESP32 + L298N</h1>

<p align="center" style="color:#1565c0;">
  Carrito controlado con ESP32, driver L298N y un celular vía Bluetooth.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Plataforma-ESP32-1565c0?style=for-the-badge&logo=espressif&logoColor=white">
  <img src="https://img.shields.io/badge/Lenguaje-MicroPython-0d47a1?style=for-the-badge">
  <img src="https://img.shields.io/badge/Driver-L298N-42a5f5?style=for-the-badge">
</p>

---

<!-- COLABORADORES (BADGES) -->
<p align="center">
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
    <img src="https://img.shields.io/badge/Gael%20Sebastian%20Castillo%20Salazar-collaborator-1565c0?style=flat-square&labelColor=0d47a1&logo=github&logoColor=white">
  </a>
  <a href="#">
    <img src="https://img.shields.io/badge/Alexis%20Manuel%20Muñoz%20Aguilar-collaborator-1565c0?style=flat-square&labelColor=0d47a1&logo=github&logoColor=white">
  </a>
  <a href="#">
    <img src="https://img.shields.io/badge/Grupo-IM%20--%202-1e88e5?style=flat-square&labelColor=0d47a1">
  </a>
</p>

---

## 👥 Integrantes

> **Proyecto desarrollado por el equipo:**

- Julio César Maldonado Acuña  - 2530001
- Roberto Emiliano Ortiz Cumpian  
- Ricardo Martin Pugliesse Macias  
- Felipe Pinzon Segura  
- Gael Sebastian Castillo Salazar  
- Alexis Manuel Muñoz Aguilar  

**Grupo:** IM - 2  

---

## Descripción 📖

Este proyecto consiste en la construcción y programación de un **carrito controlado por un ESP32**, utilizando un módulo **L298N** para manejar dos motores DC:

- Un motor de **tracción** para avanzar y retroceder.  
- Un motor de **dirección** para girar las llantas.

El movimiento se controla desde un **teléfono celular** mediante **Bluetooth (BLE tipo UART)**.  
El ESP32 recibe comandos simples (por ejemplo `F`, `B`, `L`, `R`, `S`) y ajusta la velocidad y sentido de los motores usando **PWM**.

El software está desarrollado en **MicroPython**, aprovechando:

- Módulos de **Bluetooth BLE** para la comunicación con el celular.  
- **PWM** por hardware para el control de los motores a través del L298N.  

Este README funciona como **introducción** al resto de la documentación del proyecto:
código, esquemas eléctricos, pruebas y conclusiones.

---

## Hardware utilizado ⚙️

| Componente                  | Función                                         |
|----------------------------|-------------------------------------------------|
| ESP32 S3                   | Control principal / procesamiento               |
| Driver L298N               | Control de dos motores DC (puente H doble)     |
| 2 Motores DC               | Tracción y dirección del carrito               |
| Pack 6×AA NiMH (7.2–8 V)   | Fuente de energía para los motores             |
| Pilas 9v                   | Alimentación de ESP32 S3                       |
| Regulador de Voltaje 7805  | Regulación de alimentación de ESP32 S3         |
| Celular con app BLE (UART) | Envío de comandos de movimiento                |
| Chasis de carrito          | Soporte estructural de todos los componentes   |
| Cables jumper / protoboard | Conexiones eléctricas                          |

---

## Arquitectura del sistema 🧠

```text
          CELULAR
        (App BLE UART)
               |
           Bluetooth
               |
        +------v-------+
        |    ESP32     |
        | MicroPython  |
        +---+-------+--+
            |       |
      PWM Tracción  PWM Dirección
            |       |
       +----v-------v----+
       |      L298N      |
       |  Puente H x2    |
       +----+-------+----+
            |       |
      Motor Tracción   Motor Dirección
         (DC)              (DC)

     Pack baterías (6xAA NiMH)
          +Vmot  y  GND
               |
           L298N GND
               |
           ESP32 GND
        (tierra común)