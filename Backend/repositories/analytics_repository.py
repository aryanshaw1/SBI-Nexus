from models.analytics_snapshot import AnalyticsSnapshot


def create_snapshot(db, snapshot):
    db.add(snapshot)
    db.commit()
    db.refresh(snapshot)
    return snapshot


def get_latest_snapshot(db):
    return (
        db.query(AnalyticsSnapshot)
        .order_by(AnalyticsSnapshot.created_at.desc())
        .first()
    )