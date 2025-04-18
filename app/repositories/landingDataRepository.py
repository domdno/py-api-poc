from app.db.models.landingData import LandingData

async def save_landing_data(landing_data: LandingData, db) -> LandingData:
    db.add(landing_data)
    return landing_data