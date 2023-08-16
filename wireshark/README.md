# Wireshark

Wireshark es una poderosa herramienta de análisis de tráfico de red que te permite capturar y examinar datos en tiempo real o desde archivos de captura previamente guardados. Puede ser utilizado para depurar problemas de red, analizar tráfico y comprender el funcionamiento de las comunicaciones en una red.

## Instalación

Visita el sitio web oficial de Wireshark para descargar e instalar la versión adecuada para tu sistema operativo: [Wireshark Official Website](https://www.wireshark.org/)

## Uso Básico

1. **Abrir Wireshark:**

   Abre Wireshark desde el menú de inicio o desde la terminal (si estás en Linux) usando el comando `wireshark`.

2. **Seleccionar la Interfaz:**

   Al abrir Wireshark, se te pedirá que elijas una interfaz de red para capturar el tráfico. Selecciona la interfaz correcta a través de la cual deseas capturar el tráfico. `En caso de que no salgan todas las interfaces, procura iniciar wireshark con privilegios de administrador`.

3. **Filtrar el Tráfico (opcional):**

   Puedes aplicar filtros para capturar solo el tipo de tráfico que deseas analizar. Por ejemplo, puedes usar `http` para filtrar el tráfico HTTP o `ip.addr == <IP_DESTINO>` para capturar tráfico hacia una dirección IP específica.

4. **Iniciar la Captura:**

   Haz clic en el botón de inicio (generalmente un ícono de play) para comenzar a capturar el tráfico.

5. **Realizar Acciones en la Red:**

   Realiza las acciones en la red que deseas analizar (navegar por sitios web, enviar solicitudes, etc.).

6. **Detener la Captura:**

   Una vez que hayas capturado suficiente tráfico, haz clic en el botón de detener (generalmente un ícono de stop) para detener la captura.

7. **Analizar el Tráfico:**

   Examina los paquetes capturados en la parte inferior de la ventana. Puedes hacer clic en un paquete para ver detalles adicionales, como encabezados, datos y más.

## Captura de Tráfico HTTPS

Si deseas capturar tráfico HTTPS, ten en cuenta que el contenido estará cifrado. Para capturar y analizar el contenido cifrado, es necesario configurar Wireshark con las claves privadas SSL/TLS correspondientes. Ten en cuenta que esto puede requerir acceso a las claves privadas utilizadas en el tráfico HTTPS y debe hacerse con responsabilidad y de manera ética.

## Captura de Tráfico en LocalHost (127.0.0.1)

Abre Wireshark y selecciona la interfaz de red que deseas monitorear. Esta interfaz debe ser aquella a través de la cual se envía y recibe el tráfico de la API. Por ejemplo, si estás ejecutando tu API localmente en tu máquina, selecciona la interfaz de loopback (por lo general, llamada "lo" o "Loopback: localhost").

## Licencia

Wireshark es una herramienta de código abierto y se distribuye bajo la [Licencia Pública General de GNU](https://www.gnu.org/licenses/gpl-2.0.html). Consulta la documentación de Wireshark para más detalles.

## Recursos Adicionales

- [Wireshark Official Documentation](https://www.wireshark.org/docs/)
- [Wireshark Wiki](https://wiki.wireshark.org/)
- [Wireshark University](https://www.wiresharktraining.com/)

## Páginas para hacer pruebas

- [Autenticación por HTTP #1](http://testphp.vulnweb.com/login.php)
- [Autenticación por HTTP #2](http://vbsca.ca/login/login.asp)
- [Autenticación por HTTP #3](http://demo.t3-framework.org/joomla30/index.php/en/joomla-pages/sample-page-2/login-page)
- [Autenticación por HTTPS](https://authenticationtest.com/)

**Nota:** La captura de tráfico de red puede ser sensible desde el punto de vista de la seguridad y la privacidad. Asegúrate de seguir buenas prácticas de seguridad y cumplir con las regulaciones y políticas antes de realizar capturas de tráfico.
