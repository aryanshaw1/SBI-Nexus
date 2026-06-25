def get_workflow_stage(user):

    if not user:
        return "QUALIFICATION"

    return "RECOMMENDATION"