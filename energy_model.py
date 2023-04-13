# api/energy_model.py
from mesa import Agent, Model
from mesa.time import RandomActivation

class EnergyConsumer(Agent):
    def __init__(self, unique_id, model, demand):
        super().__init__(unique_id, model)
        self.demand = demand

    def step(self):
        renewable_energy_available = self.model.energy_generation
        if renewable_energy_available >= self.demand:
            self.model.energy_generation -= self.demand
        else:
            pass

class EnergyModel(Model):
    def __init__(self, agent_count, energy_generation):
        self.energy_generation = energy_generation
        self.schedule = RandomActivation(self)

        for i in range(agent_count):
            demand = 1
            agent = EnergyConsumer(i, self, demand)
            self.schedule.add(agent)

    def step(self):
        self.schedule.step()
