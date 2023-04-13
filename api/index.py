from http.server import BaseHTTPRequestHandler
from urllib.parse import parse_qs
from energy_model import EnergyModel

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers["Content-Length"])
        post_data = self.rfile.read(content_length)
        post_data = parse_qs(post_data.decode("utf-8"))

        energy_generation = float(post_data["energy_generation"][0])
        demand_data = float(post_data["demand_data"][0])

        agent_count = 10
        model = EnergyModel(agent_count, energy_generation)

        for i in range(10):
            model.step()

        # Process the results of the MESA model (e.g., count the number of agents using renewable energy)

        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Model executed successfully.")
