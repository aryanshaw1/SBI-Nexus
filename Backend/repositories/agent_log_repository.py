from models.agent_log import AgentLog


def create_agent_log(db, log):
    db.add(log)
    db.commit()
    db.refresh(log)
    return log


def get_agent_logs(db):
    return db.query(AgentLog).all()