rows_loaded = 9800
rows_failed = 200
runtime_minutes = 18

failure_rate = (rows_failed / (rows_loaded + rows_failed)) * 100

if failure_rate <= 2 and runtime_minutes <= 20:
    status = "Healthy"
elif failure_rate <= 5:
    status = "Warning"
else:
    status = "Critical"

print(f"Failure rate: {failure_rate}"  )
print(f"Pipeline status: {status}")