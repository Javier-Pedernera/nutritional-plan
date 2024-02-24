# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# import json

# def enviar_plan_nutricional_por_correo(plan_nutricional, destinatario, asunto, saludo, idioma):
#     # Configuración del servidor SMTP de Gmail
#     # servidor_smtp = 'smtp.gmail.com'
#     # puerto_smtp = 587
#     # usuario_smtp = 'tu_correo@gmail.com'  # Aquí va tu dirección de correo de Gmail
#     # contrasena_smtp = 'tu_contraseña'  # Aquí va tu contraseña

#     # Convertir el plan nutricional de JSON a un string en formato de texto plano
#     plan_nutricional_str = json.dumps(plan_nutricional, indent=2, ensure_ascii=False)
    
#     # # Crear el mensaje de correo electrónico
#     # mensaje = MIMEMultipart()
#     # mensaje['From'] = usuario_smtp
#     # mensaje['To'] = destinatario
#     # mensaje['Subject'] = asunto

#     # Preparar el cuerpo del correo
#     cuerpo = f"{saludo},\n\nAquí está tu plan nutricional para la semana:\n\n{plan_nutricional_str}"
#     # mensaje.attach(MIMEText(cuerpo, 'plain', _charset='utf-8'))
    
#     print("Mensaje a enviar:")
#     print(cuerpo)
    
#     # Iniciar sesión en el servidor SMTP y enviar el correo
#     # try:
#     #     with smtplib.SMTP(servidor_smtp, puerto_smtp) as server:
#     #         server.ehlo()
#     #         server.starttls()
#     #         server.ehlo()
#     #         server.login(usuario_smtp, contrasena_smtp)
#     #         server.sendmail(usuario_smtp, destinatario, mensaje.as_string())
#     #         print("Correo enviado exitosamente.")
#     # except Exception as e:
#     #     print(f"Error al enviar el correo: {e}")
