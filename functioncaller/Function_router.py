from fastapi import APIRouter, UploadFile, File, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from .helper_class import find_patterns
from . import model, database

router = APIRouter()

@router.post("/upload/")
async def upload_file(
    file: UploadFile = File(...),
    db: Session = Depends(database.get_db)
):
    try:
        # Read the uploaded file content
        contents = await file.read()
        text = contents.decode("utf-8")
        
        # Use the helper function to find patterns
        results = find_patterns(text)
        
        # Create database entry
        db_pattern = model.PatternDetection(
            filename=file.filename,
            original_text=text,
            detected_patterns=results
        )
        db.add(db_pattern)
        db.commit()
        db.refresh(db_pattern)
        
        return JSONResponse(
            content={
                "status": "success",
                "filename": file.filename,
                "results": results,
                "db_id": db_pattern.id
            }
        )
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={
                "status": "error",
                "message": str(e)
            }
        )

@router.get("/patterns/{pattern_id}")
def get_pattern_detection(
    pattern_id: int,
    db: Session = Depends(database.get_db)
):
    pattern = db.query(model.PatternDetection).filter(model.PatternDetection.id == pattern_id).first()
    if pattern is None:
        return JSONResponse(
            status_code=404,
            content={"message": "Pattern detection not found"}
        )
    return pattern


