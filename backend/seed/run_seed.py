from app.db.session import SessionLocal
from seed.seed_data import run_seed

def main():
  db = SessionLocal()
  try:
    run_seed(db)
    print("✅ Seed ejecutado correctamente")
  finally:
    db.close()

if __name__ == "__main__":
  main()
