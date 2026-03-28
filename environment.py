from models import Observation, Action, Reward

class ResumeScreeningEnv:

    def __init__(self):
        self.progress = 0.0
        self.task = "Screen candidate resume"

    def reset(self):
        self.progress = 0.0
        return Observation(task=self.task, progress=self.progress)

    def state(self):
        return Observation(task=self.task, progress=self.progress)

    def step(self, action: Action):
        if action.action_type == "analyze":
            self.progress += 0.4
        elif action.action_type == "score":
            self.progress += 0.3
        elif action.action_type == "finalize":
            self.progress += 0.3

        self.progress = min(self.progress, 1.0)

        done = self.progress >= 1.0
        reward = Reward(score=self.progress, done=done)

        return self.state(), reward
