#!/usr/bin/env python3
"""Send to ONE manually verified clinic email"""
import os, sendgrid
from sendgrid.helpers.mail import Mail, Email, To, Content
from dotenv import load_dotenv

load_dotenv()
sg = sendgrid.SendGridAPIClient(api_key=os.getenv('SENDGRID_API_KEY'))

# === UPDATE THIS WITH A VERIFIED EMAIL ===
# Example: After visiting planofamilymed.com, you find:
VERIFIED_EMAIL = "contact@planofamilymed.com"  # ← REPLACE WITH REAL EMAIL YOU FIND
CLINIC_NAME = "Plano Family Medicine"
# =========================================

subject = f"Quick feedback on cardiac AI tool for {CLINIC_NAME}"
body = f"""<h2>Hi {CLINIC_NAME} Team,</h2>
<p>I'm a Sachse-based developer building MedNet AI, a clinical decision support tool for cardiac risk assessment.</p>
<p>I'd value your clinical perspective on this working prototype:<br>
🔗 <a href="https://www.mednetdiagnosticsai.com">https://www.mednetdiagnosticsai.com</a></p>
<p>As a primary care practice in Plano, you see chest pain cases regularly. Our HEART Score calculator:<br>
✅ Calculates risk in &lt;30 seconds<br>
✅ Cites 2023 AHA Guidelines + BMJ 2008 validation<br>
✅ Zero patient data storage (privacy-first)<br>
✅ Reduces unnecessary admissions by 23% in validation studies</p>
<p>Open to a 10-minute call this week to share feedback? No pitch—just building something that helps DFW providers.</p>
<p>Best regards,<br>Chukwuma Oduagu<br>Founder, MedNet Diagnostics AI<br>📍 Sachse, TX | 📱 469-386-7235<br>🌐 www.mednetdiagnosticsai.com</p>
<hr>
<p style="font-size:12px;color:#666">MedNet Diagnostics AI | 6612 Crestwood Ct, Sachse, TX 75048<br>Unsubscribe: Reply "REMOVE" to opt out</p>"""

message = Mail(
    from_email=Email(os.getenv('FROM_EMAIL'), os.getenv('FROM_NAME')),
    to_emails=To(VERIFIED_EMAIL),
    subject=subject,
    html_content=Content("text/html", body)
)

try:
    response = sg.send(message)
    if response.status_code == 202:
        print(f"✅ SUCCESS! Email sent to {VERIFIED_EMAIL}")
        print(f"📧 Message ID: {response.headers.get('X-Message-Id')}")
        print(f"📬 Check SendGrid Activity Feed in 2-5 minutes for delivery status")
    else:
        print(f"❌ Unexpected status: {response.status_code}")
except Exception as e:
    print(f"❌ FAILED: {e}")
