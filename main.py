from machine import Machine
from maintenance_evaluator import MaintenanceEvaluator

machine1 = Machine("M-1007", 2400, 1850)

evaluator = MaintenanceEvaluator()

ratio = evaluator.usage_ratio(machine1)



hscore = evaluator.health_score(ratio)

status = evaluator.machine_status(hscore)

print("=" * 45)
print("         MACHINE MAINTENANCE REPORT")
print("=" * 45)
print(f"Machine ID           : {machine1.machine_id}")
print(f"Operating Hours      : {machine1.operating_hours} hours")
print(f"Maintenance Interval : {machine1.maintenance_interval} hours")
print("-" * 45)
print(f"Usage Ratio          : {ratio:.2f}")
print(f"Health Score         : {hscore}")
print(f"Machine Status       : {status}")
print("=" * 45)
