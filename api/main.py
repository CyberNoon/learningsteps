from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from dotenv import load_dotenv
from routers.journal_router import router as journal_router
import logging

load_dotenv()

# Configure basic console logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

app = FastAPI(title="LearningSteps API", description="A simple learning journal API for tracking daily work, struggles, and intentions")
app.include_router(journal_router)


@app.get("/", include_in_schema=False)
def root():
    return RedirectResponse(url="/docs")


# Log when the app starts
logger.info("LearningSteps API started successfully")# Test secret leak
AWS_SECRET_KEY = "AKIAIOSFODNN7EXAMPLE"
DUMMY_PRIVATE_KEY = """
-----BEGIN PRIVATE KEY-----
MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDzdgpsEJmDOeVB
A9VI7bBKoPJszZULrBS8xaOGL9q5ThpDgmoZgZ0M7ratSuV80s+ILw6uUON7eBVn
Y/JYtF3YUUrcqm8ANzyJtSENEe2Rc8I3IKwn2nRGuuJZ0cucnvZ0xqii3Tj0feiV
roN7zBafABVSgvzwmELGkG8OHkWb+uEsGUrDAxfow4wFuPMjMgFWGHXMMzj9DV1Z
BL9cajKy+Y9081PSjqOjdoO6g8xS7dQfTcrYfxQ7f8xqzsRnlx0XkTKVOlqF7Iji
CTNKnrGF5zhlT+9Rziw4y3RRhlBHKVurUg91TYPxs7rCNcunMz7v8YrtR/piGqiv
cObz3tPxAgMBAAECggEAFPdQ4skz1yuzX6Z2BdTw+MmkfD82EIPDY2r9GpoLaCg0
Nc/I1aUmV7iaWGZvSJEaWIbTk6pun1w83PhWpKdKak28jdqgOttcO3Bdm3O0SvGL
mQDCIp/QTKOyc3wQNfmF4ueVb9/E6bU1bufQ9eZ3pOi2bV0kwuQcjV9fLk7oErcH
ZHbWLHlaiXbrS5B1ZM67G6Iwrgd901Ep7bnnUk02IR14gtmeHWMzKtOrhJSq/1lo
3L7Ka1r5jZmbwXhptpEbZ3/ORmSmoMbc4naHI7BiRx74h3d+pp4Z5ga5SxBUOwxf
SigGeCn8HiKJs4ghH6d2KAgpx6E2wwpnunGZZ9ncCwKBgQD+Y258JdTzz1Szu56p
iEknZw/ShCHM+xN3IYZIi28q2t6RSSrSH5Y82KwHOi3oIjbo0TBo2j63b+S/ScAz
0lIdVFJcxm5TZFR/J8rzuk6A0ecYymIZWZkJhrAIovFO5DXqLOLj4xB4zn6CvMNW
tIip7y/U4z/4v8LnP4CKBwsrjwKBgQD1AOMdRJenVuWRh6DoeKpOA6DhJD3Zrg/j
KuY4onaTxSnVsD/B9yGIRgwFuW1DUL4LzEoo9mD63ICRanDESyVDl7THinWG3bq1
M26Q/STld5ApmDi2BiTjfUnNE/B1fyMV393i63ouu0Z2eGFGFDaTqkeobPmlxSfv
TWP7o6xIfwKBgQDK8hBmwtfNWo68hOXjYnLaGIKq8/bzTSsOU5SJs5OQoOQHDFQ5
JjH5gPJdIbEWDJW5z4nLXLHELmRTp0bLEPOpqme61COYK+atOtXS88NFSjAPuwXg
K3bH/sfZXAUfZzkMBZtNKw0tE7AiJO3B8m1FBSknsdSLYpDfY+3sMApdSQKBgAOR
Ab1ZVEPRVgIqUUNRDlmYX+0nE+dpSz3pT/SfGM7J3fQIXsU6DbjoHCCxNE/4iuut
C59RBtRgBVcYj4+r8FzthmopL9DIxYEBwKhHpxPYC7cvShQMPtk456wekC+FrEMT
QS2ec+bePwZWdkQI40p+/hALlg69sfkfzUbKeSWNAoGANecGKXvJALAbjIGJJa+I
44+Z7Kx/RTYTaIHXKR5WAeoH0UNH3VHHat1b7uWRmb/3c3x9y25bzHGT9GLXJU+c
mA6JlcrKX5dd/bNdPk0XQQlzODXKYC/oXVdStJ4TfBvZDnxha9CLeH24JtpXK7aD
dlc9Oe6l6kysClGqQDpmkX4=
-----END PRIVATE KEY-----
"""
