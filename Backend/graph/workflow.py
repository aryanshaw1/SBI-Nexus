from langgraph.graph import StateGraph

from graph.state import AgentState

from graph.supervisor import supervisor_agent
from graph.lead_agent import lead_agent
from graph.recommendation_agent import recommendation_agent


workflow = StateGraph(AgentState)

workflow.add_node(
    "supervisor",
    supervisor_agent
)

workflow.add_node(
    "lead",
    lead_agent
)

workflow.add_node(
    "recommendation",
    recommendation_agent
)

workflow.set_entry_point(
    "supervisor"
)

workflow.add_edge(
    "supervisor",
    "lead"
)

workflow.add_edge(
    "lead",
    "recommendation"
)

graph = workflow.compile()