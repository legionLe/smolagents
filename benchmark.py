import time
import random
import string

class ToolOutput:
    def __init__(self, observation):
        self.observation = observation

class MemoryStep:
    def __init__(self):
        self.observations = None

outputs = {}
for i in range(10000):
    # Random string
    obs = ''.join(random.choices(string.ascii_letters, k=100))
    outputs[f"call_{i}"] = ToolOutput(obs)

def old_method(outputs):
    memory_step = MemoryStep()
    memory_step.observations = memory_step.observations or ""
    for tool_output in [outputs[k] for k in sorted(outputs.keys())]:
        memory_step.observations += tool_output.observation + "\n"
    memory_step.observations = (
        memory_step.observations.rstrip("\n") if memory_step.observations else memory_step.observations
    )

def new_method(outputs):
    memory_step = MemoryStep()
    memory_step.observations = memory_step.observations or ""
    memory_step.observations += "".join(outputs[k].observation + "\n" for k in sorted(outputs.keys()))
    memory_step.observations = (
        memory_step.observations.rstrip("\n") if memory_step.observations else memory_step.observations
    )

start = time.perf_counter()
for _ in range(100):
    old_method(outputs)
old_time = time.perf_counter() - start

start = time.perf_counter()
for _ in range(100):
    new_method(outputs)
new_time = time.perf_counter() - start

print(f"Old time: {old_time:.4f}s")
print(f"New time: {new_time:.4f}s")
