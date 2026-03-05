import sys
import yaml
import glob

REQUIRED_FIELDS = [
  "id",
  "name",
  "description",
  "severity",
  "owner" ]

def validate_file(file_path):
  print(f"Validating {file_path}...")

  with open(file_path, "r") as f:
    try:
      data = yaml.safe_load(f)
    except yaml.YAMLError as e:
      print(f"YAML syntax error in {file_path}")
      print(e)
      sys.exit(1)

  for field in REQUIRED_FIELDS:
    print(data[field])
    if field not in data:
      print(f"Missing required field '{field} in {field_path}")
      sys.exit(1)

  if "query" not in data["rule"]:
    print(f"Missing 'rule.query' in {file_path}")
    sys.exit(1)

  print(f"{file_path} is valid.\n")


if __name__ == "__main__":
  files =  glob.glob("detections/*.yaml")

  if not files:
    print("No detection files found")
    sys.exit(0)

  for file in files:
    validate_file(file)

  print("All Detection YAML files validated successfuly")

  
    
