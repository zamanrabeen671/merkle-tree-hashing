from fastapi import APIRouter, UploadFile, Depends
from app.database import SessionLocal
from app.models import FileRecord
from app.merkle.merkle import build_merkle_tree
from app.utils.dpes import get_current_user

router = APIRouter(prefix="/files")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/upload")
async def upload(file: UploadFile, db=Depends(get_db),current_user: str = Depends(get_current_user)):
    content = await file.read()

    chunks = [content[i:i+2048] for i in range(0, len(content), 2048)]
    merkle_root = build_merkle_tree(chunks)

    record = FileRecord(filename=file.filename, merkle_root=merkle_root)
    db.add(record)
    db.commit()
    db.refresh(record)

    return {"id": record.id, "filename": record.filename, "merkle_root": record.merkle_root}


@router.post("/verify/{file_id}")
async def verify(file_id: str, file: UploadFile, db=Depends(get_db)):
    record = db.query(FileRecord).filter_by(id=file_id).first()

    if not record:
        return {"error": "File not found"}

    content = await file.read()
    chunks = [content[i:i+2048] for i in range(0, len(content), 2048)]
    current_root = build_merkle_tree(chunks)

    return {
        "valid": current_root == record.merkle_root,
        "stored_root": record.merkle_root,
        "current_root": current_root
    }
