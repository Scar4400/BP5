from apscheduler.schedulers.blocking import BlockingScheduler
from data_integration import integrate_data_and_train
import pickle

def update_model():
    model = integrate_data_and_train()

    # Save the updated model
    with open("saved_model.pkl", "wb") as f:
        pickle.dump(model, f)

    print("Model updated and saved.")

if __name__ == "__main__":
    scheduler = BlockingScheduler()
    scheduler.add_job(update_model, 'interval', hours=24)  # Update every 24 hours
    scheduler.start()
