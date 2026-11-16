from contextlib import asynccontextmanager
import asyncio
import os
import asyncpg
import logging
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from dotenv import load_dotenv
from routers.journal_router import router as journal_router

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


# [ZMIANA - START]: Automatyczna inicjalizacja schematu bazy z mechanizmem retry
@asynccontextmanager
async def lifespan(app: FastAPI):
    db_url = os.getenv("DATABASE_URL")
    if db_url:
        for attempt in range(1, 11):
            try:
                logger.info(f"Connecting to PostgreSQL (attempt {attempt}/10) to verify schema...")
                conn = await asyncpg.connect(db_url)
                await conn.execute("""
                    CREATE TABLE IF NOT EXISTS entries (
                        id VARCHAR(255) PRIMARY KEY,
                        data JSONB NOT NULL,
                        created_at TIMESTAMPTZ DEFAULT NOW(),
                        updated_at TIMESTAMPTZ DEFAULT NOW()
                    );
                """)
                await conn.close()
                logger.info("Database schema verified/initialized successfully.")
                break
            except Exception as e:
                logger.warning(f"Database not ready yet ({e}). Retrying in 3s...")
                await asyncio.sleep(3)
    yield
# [ZMIANA - KONIEC]


# [ZMIANA]: Podpiecie lifespan do FastAPI
app = FastAPI(
    title="LearningSteps API",
    description="A simple learning journal API for tracking daily work, struggles, and intentions",
    lifespan=lifespan
)
app.include_router(journal_router)


@app.get("/", include_in_schema=False)
def root():
    return RedirectResponse(url="/docs")


# Log when the app starts
logger.info("LearningSteps API started successfully")
