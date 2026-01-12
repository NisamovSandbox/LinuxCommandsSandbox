<!--
  _      _                     _____                                          _     
 | |    (_)                   / ____|                                        | |    
 | |     _ _ __  _   ___  __ | |     ___  _ __ ___  _ __ ___   __ _ _ __   __| |___ 
 | |    | | '_ \| | | \ \/ / | |    / _ \| '_ ` _ \| '_ ` _ \ / _` | '_ \ / _` / __|
 | |____| | | | | |_| |>  <  | |___| (_) | | | | | | | | | | | (_| | | | | (_| \__ \
 |______|_|_| |_|\__,_/_/\_\  \_____\___/|_| |_| |_|_| |_| |_|\__,_|_| |_|\__,_|___/
                                                                                    
Todos los derechos pertenecientes a Andrés Ruslan Abadías Otal | Nisamov: github.com/Nisamov
<style>
  body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background-color: #2f3136;
    color: #ffffff;
    line-height: 1.6;
    margin: 0;
    padding: 0px;
  }
  .doc-container {
    max-width: 800px;
    margin: 20px auto;
    background-color: #36393f;
    padding: 40px;
    border-radius: 10px;
    box-shadow: 0 6px 18px rgba(0,0,0,0.5);
  }
  .doc-header {
    text-align: left;
    margin-bottom: 20px;
  }
  .doc-header div {
    padding: 5px 0;
    font-weight: bold;
  }
  .doc-header a {
    color: #a69be9ff;
    text-decoration: none;
  }
  .doc-header a:hover {
    text-decoration: underline;
  }
  .separator {
    border-top: 2px solid #bdcabbff;
    border-radius: 2px;
    margin: 10px 0 20px 0;
  }
  h1, h2, h3 {
    color: #00b0f4;
    margin-top: 30px;
  }
  p, li {
    color: #ffffff;
  }
  a {
    color: #00b0f4;
    text-decoration: none;
  }
  a:hover {
    text-decoration: underline;
    color: #00b0f4;
  }
</style>
</head>
<body>

<div class="doc-container">
  <div class="doc-header">
    <div>Andrés Ruslan Abadías Otal</div>
    <div>Página web: <a href="https://github.com/Nisamov">Github</a></div>
    <div>Repositorio: <a href="https://github.com/Nisamov/LinuxCommands">Repositorio Origen</a></div>
    <div class="separator"></div>
  </div>
-->

![Cartel Principal](.github/media/LinuxCommandsWhiteTheme.png)

# LinuxCommands  
### Estructura y referencia para documentar comandos y servicios en Linux

LinuxCommands nació como una recopilación de apuntes personales para organizar y entender mejor distintos comandos, scripts y servicios en Linux.

Con el tiempo, se fue estructurando para que sea más fácil de navegar y consultar, tanto para mí como para cualquier persona interesada en aprender o consultar comandos y servicios de manera práctica.

---

## Objetivos del proyecto

- Proporcionar un **formato claro y reutilizable** para documentar comandos Linux.
- Facilitar una documentación **legible para humanos y mantenible a largo plazo**.
- Reducir duplicación, ambigüedad y variaciones innecesarias entre repositorios.
- Servir como referencia práctica para administradores de sistemas, desarrolladores y equipos técnicos.

---

## Enfoque

El repositorio no pretende sustituir herramientas existentes como `man`, sino **complementarlas** mediante:

- Ficheros `commands.md` estructurados,
- Convenciones claras de documentación,
- Ejemplos prácticos y homogéneos,
- Una organización pensada para crecer sin perder consistencia.

El formato utilizado está definido formalmente en un documento de origen y se aplica de forma uniforme en todo el repositorio.

---

## Formato de documentación

El formato base de los comandos se define en el documento de origen:

- [Documento de Origen](.github/origins/LinuxCommandsOrigen.md)

La versión más actual y aplicada del formato puede encontrarse en:

- [`document_management/commands.md`](/document_management/commands.md)

Este fichero actúa como **referencia canónica** del estándar utilizado en el repositorio.

---

## Estructura del repositorio

La organización del repositorio está pensada para facilitar la navegación y el crecimiento progresivo del contenido:

<!-- AUTO-GENERATED-INDEX:START -->
- [document_management](/document_management)
- [fundamentals](/fundamentals)
- [networking](/networking)
- [permission_management](/permission_management)
- [process_tasks](/process_tasks)
- [scripting](/scripting)
- [security](/security)
- [services](/services)
- [software_management](/software_management)
- [storage](/storage)
- [system_data](/system_data)
- [user_permissions](/user_permissions)
- [web_server](/web_server)
<!-- AUTO-GENERATED-INDEX:END -->

---

## Información adicional

-  [Información general del repositorio](.github/INFO.md)

---

## Contribuciones

Las contribuciones son bienvenidas siempre que respeten el formato y la estructura definidos.  
El objetivo es mantener una documentación coherente y de alta calidad.