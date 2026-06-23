from models.customer_journey_event import CustomerJourneyEvent


def create_event(db, event):
    db.add(event)
    db.commit()
    db.refresh(event)
    return event


def get_user_events(db, user_id):
    return (
        db.query(CustomerJourneyEvent)
        .filter(CustomerJourneyEvent.user_id == user_id)
        .all()
    )