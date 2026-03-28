from environment import ResumeScreeningEnv
from models import Action

env = ResumeScreeningEnv()

obs = env.reset()
print("Start:", obs)

actions = ["analyze", "score", "finalize"]

for a in actions:
    obs, reward = env.step(Action(action_type=a))
    print("Observation:", obs)
    print("Reward:", reward)

print("Finished")
