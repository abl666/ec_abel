# app.py
from flask import Flask, render_template, request
from mesa import Agent, Model
from mesa.time import RandomActivation

app = Flask(__name__)

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

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        energy_generation = float(request.form["energy_generation"])
        demand_data = float(request.form["demand_data"])

        agent_count = 10
        model = EnergyModel(agent_count, energy_generation)

        for i in range(10):
            model.step()

        # Process the results of the MESA model (e.g., count the number of agents using renewable energy)
        return "Model executed successfully."

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
