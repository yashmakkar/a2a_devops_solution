from a2a.types import AgentCapabilities, AgentCard, AgentSkill
from a2a.server.request_handlers import DefaultRequestHandler
from agent_executer import GreetingAgentExecutor
from a2a.server.tasks import InMemoryTaskStore
from a2a.server.apps import A2AStarletteApplication
import uvicorn


def main():

    skill = AgentSkill(
        id="helloWorld!!",
        name="Greet",
        description="Return a greeting",
        tags=["greetings", "hello", "world"],
        examples=["Hey", "Hello", "Hi"]
    )


    agent_card = AgentCard(
        name="Greeting Agent",
        description="A simple agent that returns a greeting",
        url="http://127.0.0.1:5001",
        default_input_modes=["text"],
        default_output_modes=["text"],
        skills=[skill],
        version="1.0.0",
        capabilities=AgentCapabilities()
    )

    request_handler = DefaultRequestHandler(
        agent_executor=GreetingAgentExecutor(),
        task_store=InMemoryTaskStore()
    )

    server = A2AStarletteApplication(
        agent_card=agent_card,
        http_handler=request_handler
    )

    uvicorn.run(server.build(), host="127.0.0.1", port=5001)

if __name__ == "__main__":
    main()