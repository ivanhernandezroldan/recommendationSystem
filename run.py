import dataset
import reward


userDataset = dataset.getRandomDataset()
rewards = reward.assign_rewards(userDataset)
