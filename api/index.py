import os
from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, EmailStr, SecretStr
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig, MessageType, NameEmail

app = FastAPI()

# Povolení CORS, aby formulář v HTML mohly odesílat prohlížeče
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # V produkci můžete omezit na konkrétní doménu
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Nacteni z Vercel Environment Variables (nebo výchozí hodnoty)
MAIL_USERNAME = os.getenv("MAIL_USERNAME", "jirihavran@seznam.cz")
MAIL_PASSWORD = os.getenv("MAIL_PASSWORD", "")
MAIL_SERVER = os.getenv("MAIL_SERVER", "smtp.seznam.cz")
MAIL_PORT = int(os.getenv("MAIL_PORT", "465"))

conf = ConnectionConfig(
    MAIL_USERNAME=MAIL_USERNAME,
    MAIL_PASSWORD=SecretStr(MAIL_PASSWORD),
    MAIL_FROM=MAIL_USERNAME,
    MAIL_PORT=MAIL_PORT,
    MAIL_SERVER=MAIL_SERVER,
    MAIL_STARTTLS=True,
    MAIL_SSL_TLS=False,
    USE_CREDENTIALS=True,
    VALIDATE_CERTS=True
)

class PoptavkaSchema(BaseModel):
    jmeno: str
    email: EmailStr
    telefon: str | None = None
    zprava: str

@app.post("/api/poptavka")
async def odeslat_poptavku(poptavka: PoptavkaSchema):
    if not MAIL_PASSWORD:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Server neni nakonfigurovan pro odesilani emailu (chybi MAIL_PASSWORD)."
        )

    html_obsah = f"""
    <h2>Nová poptávka z webu CA Havran Jiří</h2>
    <p><strong>Jméno a příjmení:</strong> {poptavka.jmeno}</p>
    <p><strong>Email klienta:</strong> {poptavka.email}</p>
    <p><strong>Telefon:</strong> {poptavka.telefon or 'Neuvedeno'}</p>
    <hr>
    <h3>Zpráva / Poptávka:</h3>
    <p>{poptavka.zprava.replace(chr(10), '<br>')}</p>
    """

    message = MessageSchema(
        subject=f"Nová poptávka z webu - {poptavka.jmeno}",
        recipients=[NameEmail(name="CA Havran Jiří", email=MAIL_USERNAME)],
        body=html_obsah,
        subtype=MessageType.html,
        reply_to=[NameEmail(name=poptavka.jmeno, email=poptavka.email)]
    )

    fm = FastMail(conf)

    try:
        await fm.send_message(message)
        return {"success": True, "message": "Poptávka byla úspěšně odeslána."}
    except Exception as e:
        print(f"Chyba při odesílání e-mailu: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Chyba při odesílání e-mailu."
        )
