# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# import json
# from dotenv import load_dotenv
# import os
# load_dotenv()
# gmail = 'Nutriplan <javierprogra1@gmail.com>'
# claveGmail = os.getenv('KEY_GMAIL')
# # print(claveGmail)

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

# ###########################################################################################################
#  # Iniciar sesión en el servidor SMTP y enviar el correo
#     try:
#         # Crear el mensaje de correo electrónico
#         mensaje = MIMEMultipart()
#         mensaje['From'] = gmail  # Tu dirección de correo de Gmail
#         mensaje['To'] = destinatario
#         mensaje['Subject'] = asunto

#         # Adjuntar el cuerpo del mensaje
#         mensaje.attach(MIMEText(cuerpo, 'plain', _charset='utf-8'))

#         # Configurar el servidor SMTP de Gmail y enviar el correo
#         with smtplib.SMTP('smtp.gmail.com', 587) as server:
#             server.starttls()
#             server.login(gmail, claveGmail)  # Tu dirección de correo y contraseña
#             server.send_message(mensaje)
#         print("Correo enviado exitosamente.")
#     except Exception as e:
#         print(f"Error al enviar el correo: {e}")


        ########Modificando estilo
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import json
import os
from dotenv import load_dotenv

load_dotenv()

gmail = 'javierprogra1@gmail.com'
claveGmail = os.getenv('KEY_GMAIL')

def enviar_plan_nutricional_por_correo(plan_nutricional, destinatario, asunto, saludo, idioma):
    print("plan nutricional en el correo:",plan_nutricional)

    plan_nutricional_str = json.dumps(plan_nutricional, indent=2, ensure_ascii=False)
    print("plan nutricional en el correo despues de dumps:",plan_nutricional_str)
        # Encontrar el índice de inicio del JSON

    
    imagen_url = 'https://res.cloudinary.com/dbwmesg3e/image/upload/v1709135936/Nutriplan/fondoNP_jlspdu.png'
    cuerpo = f"""
        <html>
        <head><style>
                /* Estilos personalizados */
                body {{
                    font-family: Arial, sans-serif;
                    background-color: #f2f2f2;
                }}
                .container {{
                    max-width: 600px;
                    margin: 0 auto;
                    padding: 20px;
                    background-color: #fff;
                    border-radius: 10px;
                    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                }}
                .logo {{
                    display: block;
                    margin: 0 auto;
                    width: 200px;
                }}
                .plan-nutricional {{
                    margin-top: 20px;
                    padding: 20px;
                    background-color: #f9f9f9;
                    border-radius: 5px;
                }}
                /* Otros estilos, como para los días del plan, etc. */
            </style></head>
            <body>
            <div class="container">
                <img src="{imagen_url}" alt="Nutriplan Logo" class="logo">
                
                <h1>{saludo} {destinatario},</h1>
                <div class="plan-nutricional">
                <pre>{plan_nutricional_str}</pre>
                </div>
                <p>Saludos,</p>
                <p>Nutriplan</p>
            </div>
        </body>
        </html>
    """

    # Crear el mensaje de correo electrónico
    mensaje = MIMEMultipart()
    mensaje['From'] = 'Nutriplan <javierprogra1@gmail.com>'
    mensaje['To'] = destinatario
    mensaje['Subject'] = asunto

    # Adjuntar el cuerpo del mensaje en formato HTML
    mensaje.attach(MIMEText(cuerpo, 'html'))


    # Configurar el servidor SMTP de Gmail y enviar el correo
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(gmail, claveGmail)
            server.send_message(mensaje)
        print("Correo enviado exitosamente.")
    except Exception as e:
        print(f"Error al enviar el correo: {e}")