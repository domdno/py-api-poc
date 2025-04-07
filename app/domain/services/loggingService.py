from app.db.database import get_db
from typing import Any
from app.db.models.apiRequestResponse import ApiRequestResponse

def log_db_upload(request_data: dict[str, Any], response_data: dict[str, Any]):
    # db connection
    db_gen = get_db()
    db = next(db_gen)

    try:
        apiRequestResponse = ApiRequestResponse(
            request_data=request_data,
            response_data=response_data
        )
        db.add(apiRequestResponse)
        db.commit()
    except Exception as e:
        print(f"Logging error: {e}" )
        raise e
    finally:
        db.close()