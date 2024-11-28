from django.conf import settings
from django.contrib.auth.models import Group
from django.core.mail import send_mail

from apps.employees.services.email_service_templates import generateEmailTemplates

STATUS = {
    "Opened": "Opened",
    "Pending": "Pending",
    "Approved": "Approved",
    "Denied": "Denied",
    "Canceled": "Canceled",
}

def send_status_change_email(instance):
    # Get the TI and RH groups
    ti_group = Group.objects.get(name="TI")
    rh_group = Group.objects.get(name="RH")
    print("Grupos acessados com sucesso")

    # Get users from each group
    ti_users = ti_group.user_set.all()
    rh_users = rh_group.user_set.all()
    print("usuários recuperados com sucesso")

    # Get emails from both groups
    ti_emails = ti_users.values_list("email", flat=True)
    rh_emails = rh_users.values_list("email", flat=True)
    print("emails recuperados com sucesso")
    print(f"TI: {ti_users}")
    print(f"RH: {rh_users}")

    email_subject = ""
    email_body_intro = ""

    emails = []

    if instance.status == STATUS["Opened"]:
        email_subject = "Nova requisição de funcionário"
        emails = [instance.requester, instance.approver]
        print("Dados de email criados para status Opened")

    if instance.status == STATUS["Pending"]:
        email_subject = "Requisição de novo funcionário pendente"
        emails = [instance.requester, *rh_emails, *ti_emails]

    if instance.status == STATUS["Approved"]:
        email_subject = "Requisição de funcionário aprovada"
        emails = [instance.requester, *ti_emails]
        print("Dados de email criados para status Approved")

    if instance.status == STATUS["Denied"]:
        email_subject = "Requisição de novo funcionário negada"
        emails = [instance.requester]

    if instance.status == STATUS["Canceled"]:
        email_subject = "Requisição de novo funcionário negada"
        emails = [instance.requester, instance.approver]

    TEMPLATES = generateEmailTemplates(instance=instance)

    summary_body = TEMPLATES["summary_body"]
    email_body_intro = TEMPLATES["email_body_intro"][instance.status]

    if len(emails) == 0:
        emails = ["dev3.engenhadev@gmail.com"]
        summary_body = "Houve um erro"
        print("Não encontrei emails para enviar")


    button_html = '<a href="https://gimi-requisitions.vercel.app" target="_blank" class="btn">Acessar Webapp</a><br>'  # noqa: E501

    html_message = f"""
        <html>
            <head>
                <style>
                    * {{ font-size: 1rem; }}
                    table {{ border-collapse: collapse; }}
                    th, td {{ border: 1px solid black; padding: 5px; text-align: left; font-size: 0.9rem; }}
                    .btn {{
                        display: inline-block;
                        background-color: #f0f0f0;
                        padding: 8px 16px;
                        text-align: center;
                        text-decoration: none;
                        font-size: 16px;
                        border-radius: 10px;
                        margin-top: 10px;
                        border: 2px solid black;
                        font-weight: bold;
                    }}
                    ul{{
                        list-style: none;
                        margin: 0;
                        padding: 0;
                    }}
                    li{{
                        margin-left: 10px;
                    }}
                </style>
            </head>
            <body>
                <div>
                    {email_body_intro}<br>
                    {summary_body}<br>
                    {TEMPLATES["RH"][instance.status]}
                    {TEMPLATES["TI"][instance.status]}
                    {button_html}
                </div>
            </body>
        </html>
    """  # noqa: E501
    print(f"Preparando para enviar o email para {emails}")
    send_mail(
        email_subject,
        "This is a plain text for email clients that don't support HTML",
        settings.EMAIL_HOST_USER,
        emails,
        fail_silently=False,
        html_message=html_message,
    )
    print("Email enviado com sucesso!")
