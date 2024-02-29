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
    print("tipo de plan_nutricional",type(plan_nutricional))
    print("plan nutricional en el correo antes de dumps:",plan_nutricional)

        #El problema esta en que debo cortar la respuesta de Openai porque no es un JSON para trabajar directamente Es un strin con ```Json {debo extraer este objeto}```
    if isinstance(plan_nutricional, str):
        inicio_json = plan_nutricional.find('{')

        fin_json = plan_nutricional.rfind('}') + 1

        plan_nutricional_recortado = plan_nutricional[inicio_json:fin_json]
        try:
            plan_nutricional = json.loads(plan_nutricional_recortado)
            print("plan nutricional cargado como diccionario:", plan_nutricional)
        except json.JSONDecodeError as e:
            print("Error al cargar la cadena JSON:", e)
            return

    if isinstance(plan_nutricional, dict):
        print("Claves del JSON antes de la serialización:")
        print(plan_nutricional.keys())
    else:
        print("El objeto 'plan_nutricional' no es un diccionario.")

    plan_nutricional_str = json.dumps(plan_nutricional, indent=2, ensure_ascii=False)
    print("plan nutricional en el correo después de dumps:", plan_nutricional_str)
    
    print("tipo de plan_nutricional_str:", type(plan_nutricional_str))

    plan_nutricional_deserializado = json.loads(plan_nutricional_str)
    print("plan nutricional deserializado:", plan_nutricional_deserializado)

    print("tipo de plan_nutricional_deserializado:", type(plan_nutricional_deserializado))
    
    lista_html = "<ul>"
    for dia, comidas in plan_nutricional_deserializado.items():
        lista_html += f"<li><strong>{dia}:</strong>"
        lista_html += "<ul>"
        for comida, descripcion in comidas.items():
            lista_html += f"<li>{comida}: {descripcion}</li>"
        lista_html += "</ul></li>"
    lista_html += "</ul>"
   
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
                .saludo {{
                    font-size: medium;
                    font-weight: bold;
                    color: #333;
                }}
                /* Otros estilos, como para los días del plan, etc. */
            </style></head>
            <body>
            <div class="container">
                <img src="{imagen_url}" alt="Nutriplan Logo" class="logo">
                
                <h1 class="saludo">{saludo} {destinatario},</h1>
                <p>Aquí está tu plan nutricional para la semana:</p> 
                <div class="plan-nutricional">
                 {lista_html}
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