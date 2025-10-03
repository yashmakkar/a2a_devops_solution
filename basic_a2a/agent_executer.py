from a2a.server.agent_execution import AgentExecutor
from pydantic import BaseModel
from a2a.utils import new_agent_text_message


class GreetingAgent(BaseModel):
    """Greeting agent that returns a greeting"""

    async def invoke(self) -> str:
        return "Hi!! I am good. How May I help you??"


class GreetingAgentExecutor(AgentExecutor):
    def __init__(self):
        self.agent = GreetingAgent()

    async def execute(self, context, event_queue):
        result = await self.agent.invoke()
        await event_queue.enqueue_event(new_agent_text_message(result))
        
    async def cancel(self, context, event_queue):
        raise Exception("Cancel not supported")