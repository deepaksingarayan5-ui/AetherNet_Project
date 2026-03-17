class AetherBrain:
    def __init__(self):
        self.stations = ["Goldstone (US)", "Madrid (Spain)", "Canberra (Australia)"]

    def check_handover_requirement(self, health, current_station):
        """AI predicts if a handover is necessary."""
        if health == "CRITICAL":
            next_station = [s for s in self.stations if s != current_station][0]
            return True, next_station
        return False, current_station

    def predict_correction(self, jitter, weather):
        """Calculates counter-adjustment for beam stability."""
        multiplier = 1.8 if weather == "Stormy" else 1.0
        return -jitter * 0.75 * multiplier
