class MaintenanceEvaluator:
    def usage_ratio(self, machine):
        return machine.operating_hours / machine.maintenance_interval
    
    def health_score(self, usage_ratio):
        if usage_ratio <= 0.25:
            return "Excellent"
        elif usage_ratio <= 0.5:
            return "Good"
        elif usage_ratio <= 0.75:
            return "Fair"
        elif usage_ratio <= 1:
            return "Poor"
        else :
            return "Critical"
        
    def machine_status(self, health_score):
        if health_score in ["Excellent", "Good"]:
            return "Healthy"
        elif health_score == "Fair":
            return "Monitor"
        elif health_score == "Poor":
            return "Preventive Maintenance"
        else :
            return "Stop Machine"