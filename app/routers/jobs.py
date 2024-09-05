from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas, db, job_scheduler

router = APIRouter()

@router.get("/jobs")
def list_jobs(db: Session = Depends(db.get_db)):
    jobs = db.query(models.Job).all()
    return jobs

@router.get("/jobs/{job_id}")
def get_job(job_id: int, db: Session = Depends(db.get_db)):
    job = db.query(models.Job).filter(models.Job.id == job_id).first()
    if job is None:
        raise HTTPException(status_code=404, detail="Job not found")
    return job

@router.post("/jobs")
def create_job(job: schemas.JobCreate, db: Session = Depends(db.get_db)):
    new_job = models.Job(name=job.name, interval=job.interval)
    db.add(new_job)
    db.commit()
    db.refresh(new_job)
    job_scheduler.schedule_job(new_job.id, new_job.interval, job_scheduler.dummy_job)
    return new_job
